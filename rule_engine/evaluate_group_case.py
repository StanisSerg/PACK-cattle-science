#!/usr/bin/env python3
"""
evaluate_group_case.py — Group Evaluation Loop

Usage:
    python3 evaluate_group_case.py cases/group_cases/GROUP-TRANSITION-DEMO-001.yaml
    python3 evaluate_group_case.py cases/group_cases/GROUP-TRANSITION-DEMO-001.yaml --fact-yaml cases/group_cases/GROUP-TRANSITION-DEMO-001-fact.yaml

Что делает:
    1. Загружает GROUP CASE
    2. Загружает фактовые метрики (из --fact-yaml или из секции case['fact'])
    3. Берёт execution: сначала embedded case['execution'], потом fact['execution_status']
    4. Сравнивает факт с success_criteria стратегии
    5. Считает delta (факт vs baseline)
    6. Формирует group_evaluation: status, interpretation, root_cause
    7. Сохраняет обратно в кейс
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from group_models import compute_execution_summary, load_yaml, save_yaml


def parse_target(target: str) -> tuple[str, float]:
    """
    Парсит строку target вида '<25%', '> -15%', '<60', '>= 1.2'.
    Возвращает (operator, value).
    """
    s = target.strip().replace("%", "")
    m = re.match(r"^(<=|>=|<|>)\s*([+-]?\d+(?:\.\d+)?)$", s)
    if not m:
        raise ValueError(f"Cannot parse target: {target!r}")
    return m.group(1), float(m.group(2))


def check_criterion(target: str, fact: float) -> bool:
    op, val = parse_target(target)
    if op == "<":
        return fact < val
    if op == "<=":
        return fact <= val
    if op == ">":
        return fact > val
    if op == ">=":
        return fact >= val
    return False


def get_baseline(case: dict, metric: str) -> float | None:
    metrics = case.get("metrics", {})
    derived = case.get("derived_group", {})

    mapping = {
        "bhb_prevalence_gt_1_2": lambda: metrics.get("metabolic", {}).get("prevalence_bhb_gt_1_2"),
        "milk_deviation_mean": lambda: metrics.get("milk", {}).get("mean_deviation_pct"),
        "group_health_index": lambda: derived.get("group_health_index"),
    }

    getter = mapping.get(metric)
    if getter:
        val = getter()
        return float(val) if isinstance(val, (int, float)) else None
    return None


def get_fact(fact_data: dict, metric: str) -> float | None:
    metrics = fact_data.get("metrics", {})
    mapping = {
        "bhb_prevalence_gt_1_2": lambda: metrics.get("metabolic", {}).get("prevalence_bhb_gt_1_2"),
        "milk_deviation_mean": lambda: metrics.get("milk", {}).get("mean_deviation_pct"),
        "group_health_index": lambda: fact_data.get("derived_group", {}).get("group_health_index"),
    }
    getter = mapping.get(metric)
    if getter:
        val = getter()
        return float(val) if isinstance(val, (int, float)) else None
    return None


def resolve_execution(case: dict[str, Any], fact_data: dict[str, Any]) -> dict[str, Any]:
    """
    Выбираем источник execution:
    1. Embedded execution в кейсе (приоритет)
    2. execution_status из fact-yaml (fallback)
    """
    embedded = case.get("execution")
    if embedded and embedded.get("actions"):
        return embedded

    # fallback: старая схема execution_status из fact-yaml
    status_map = fact_data.get("execution_status", {})
    actions = []
    for action_id, status in status_map.items():
        actions.append({
            "id": action_id,
            "mandatory": True,
            "status": status,
            "started_at": None,
            "completed_at": None,
            "notes": "from_fact_yaml",
        })
    execution = {"actions": actions}
    execution["summary"] = compute_execution_summary(execution)
    return execution


def evaluate_group_case(case: dict[str, Any], fact_data: dict[str, Any]) -> dict[str, Any]:
    strategy = None
    gd = case.get("group_decision", {})
    strategy = gd.get("basis", {}).get("strategy") or {}
    if not strategy:
        for rr in case.get("group_rule_results", []):
            dec = rr.get("decision", {})
            if dec.get("strategy"):
                strategy = dec["strategy"]
                break

    success_criteria = strategy.get("success_criteria", [])
    execution = resolve_execution(case, fact_data)

    criteria_checks = []
    any_passed = False
    any_failed = False
    missing_metrics = []

    for crit in success_criteria:
        metric = crit["metric"]
        target = crit["target"]
        fact_val = get_fact(fact_data, metric)
        baseline_val = get_baseline(case, metric)

        if fact_val is None:
            missing_metrics.append(metric)
            passed = None
        else:
            try:
                passed = check_criterion(target, fact_val)
            except ValueError as e:
                passed = None
                missing_metrics.append(f"{metric} ({e})")

        if passed is True:
            any_passed = True
        elif passed is False:
            any_failed = True

        delta = None
        if fact_val is not None and baseline_val is not None:
            delta = round(fact_val - baseline_val, 2)

        criteria_checks.append({
            "metric": metric,
            "target": target,
            "fact": fact_val,
            "baseline": baseline_val,
            "delta": delta,
            "passed": passed,
        })

    exec_summary = execution.get("summary", compute_execution_summary(execution))

    # --- Определяем статус ---
    if missing_metrics:
        status = "unable_to_assess"
    elif not success_criteria:
        status = "unable_to_assess"
    elif any_failed and not any_passed:
        status = "failure"
    elif any_failed:
        status = "partial"
    elif any_passed and not any_failed:
        status = "success"
    else:
        status = "unable_to_assess"

    # Если execution неполный и статус success — понижаем до partial
    if status == "success" and not exec_summary["execution_complete"]:
        status = "partial"

    # --- Delta summary ---
    delta_summary = {}
    for cc in criteria_checks:
        if cc["delta"] is not None:
            delta_summary[f"{cc['metric']}_change"] = cc["delta"]

    # --- Interpretation ---
    if status == "success":
        primary_result = "full_response"
    elif status == "partial":
        primary_result = "partial_response"
    elif status == "failure":
        primary_result = "no_response"
    else:
        primary_result = "unable_to_assess"

    # --- Root cause ---
    root_causes = []
    if not exec_summary["execution_complete"] and status in ("partial", "failure"):
        root_causes.append("incomplete_execution")
    if any_failed and exec_summary["execution_complete"]:
        root_causes.append("ineffective_intervention")
    for cc in criteria_checks:
        if cc["metric"] == "milk_deviation_mean" and cc["delta"] is not None and cc["delta"] < -5:
            root_causes.append("condition_deteriorated")
            break
        if cc["metric"] == "bhb_prevalence_gt_1_2" and cc["delta"] is not None and cc["delta"] > 5:
            root_causes.append("condition_deteriorated")
            break

    return {
        "status": status,
        "criteria_check": criteria_checks,
        "execution": exec_summary,
        "delta": delta_summary,
        "interpretation": {
            "primary_result": primary_result,
        },
        "root_cause": root_causes if root_causes else ["under_investigation"],
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate group case against factual outcomes")
    parser.add_argument("case", help="Path to group case YAML")
    parser.add_argument("--fact-yaml", help="Path to YAML with factual metrics and optional execution_status")
    args = parser.parse_args()

    case = load_yaml(args.case)

    if args.fact_yaml:
        fact_data = load_yaml(args.fact_yaml)
    else:
        fact_data = case.get("fact", {})

    if not fact_data:
        print("Error: No fact data found. Provide --fact-yaml or add 'fact:' section to the case.")
        raise SystemExit(1)

    evaluation = evaluate_group_case(case, fact_data)
    case["group_evaluation"] = evaluation
    save_yaml(args.case, case)

    print(f"✓ Evaluated group case: {args.case}")
    print(f"  Status: {evaluation['status']}")
    print(f"  Primary result: {evaluation['interpretation']['primary_result']}")
    if evaluation['root_cause']:
        print(f"  Root cause: {', '.join(evaluation['root_cause'])}")
    print()
    print("  Criteria checks:")
    for cc in evaluation["criteria_check"]:
        status_mark = "✅" if cc["passed"] is True else "❌" if cc["passed"] is False else "❓"
        print(f"    {status_mark} {cc['metric']}: target {cc['target']}, fact {cc['fact']}, baseline {cc['baseline']}, delta {cc['delta']}")
    print()
    exec_info = evaluation["execution"]
    print(f"  Execution: {exec_info['mandatory_done']}/{exec_info['mandatory_total']} mandatory done, "
          f"{exec_info['mandatory_in_progress']} in progress, {exec_info['mandatory_missing']} missing")
    if exec_info["incomplete_action_ids"]:
        print(f"    Incomplete actions: {', '.join(exec_info['incomplete_action_ids'])}")


if __name__ == "__main__":
    main()
