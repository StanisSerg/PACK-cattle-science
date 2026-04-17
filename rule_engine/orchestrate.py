#!/usr/bin/env python3
"""
orchestrate.py — Orchestrator v1: CSV → Group Case → Strategy

Scope: только metabolic/transition группы из herd CSV.
Не парсит markdown отчёты (хрупко) — работает с исходными данными.

Usage:
    python3 orchestrate.py \
        --csv templates/merged_herd_data.csv \
        --farm Demo-Farm-12 \
        --group-type transition_period \
        --dim-range 0-21 \
        --out-dir cases/group_cases/

Что делает:
    1. Загружает CSV (merged или enterprise формат)
    2. Фильтрует коров по dim_range
    3. Считает групповые метрики (milk, metabolic, reproduction)
    4. Определяет boundary sub-cases (крайние коровы)
    5. Создаёт GROUP CASE YAML
    6. Запускает run_group_case.py (через импорт)
    7. Выводит strategy и execution summary
"""
from __future__ import annotations

import argparse
import csv
import statistics
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from enterprise_loader import load_merged_csv
from group_models import (
    attach_derived_group,
    init_execution_from_strategy,
    load_yaml,
    save_yaml,
)
from run_group_case import merge_group_decisions
from group_rules import rule_001g


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────

def parse_dim_range(dim_range: str) -> tuple[int, int]:
    parts = dim_range.split("-")
    if len(parts) != 2:
        raise ValueError(f"dim_range must be 'min-max', got: {dim_range}")
    return int(parts[0]), int(parts[1])


def filter_rows(rows: list[dict], dim_min: int, dim_max: int) -> list[dict]:
    return [r for r in rows if dim_min <= r.get("dim", 0) <= dim_max and r.get("is_lactating")]


def compute_group_metrics(rows: list[dict]) -> dict[str, Any]:
    n = len(rows)
    if n == 0:
        return {"milk": {}, "metabolic": {}, "reproduction": {}}

    # Milk
    actuals = [r.get("milk_yield_actual", 0) or 0 for r in rows]
    expecteds = [r.get("milk_yield_expected", 0) or 0 for r in rows]
    deviations = [
        ((a - e) / e * 100) if e and e > 0 else 0.0
        for a, e in zip(actuals, expecteds)
    ]
    mean_deviation = round(statistics.mean(deviations), 1) if deviations else 0.0

    milk_metrics = {
        "mean_actual_kg": round(statistics.mean(actuals), 2) if actuals else 0.0,
        "mean_expected_kg": round(statistics.mean(expecteds), 2) if expecteds else 0.0,
        "mean_deviation_pct": mean_deviation,
    }

    # Metabolic
    bhbs = [r.get("bhb") for r in rows if r.get("bhb") is not None]
    temps = [r.get("temperature") for r in rows if r.get("temperature") is not None]
    ca_values = [r.get("calcium_mmol_l") for r in rows if r.get("calcium_mmol_l") is not None]

    prevalence_bhb = round(sum(1 for b in bhbs if b >= 1.2) / n * 100, 1) if bhbs else 0.0
    prevalence_ca = round(sum(1 for c in ca_values if c < 2.0) / n * 100, 1) if ca_values else 0.0
    prevalence_fever = round(sum(1 for t in temps if t is not None and t >= 39.2) / n * 100, 1) if temps else 0.0

    metabolic_metrics = {
        "bhb_mean": round(statistics.mean(bhbs), 2) if bhbs else None,
        "bhb_median": round(statistics.median(bhbs), 2) if bhbs else None,
        "prevalence_bhb_gt_1_2": prevalence_bhb,
        "prevalence_ca_lt_2_0": prevalence_ca,
        "prevalence_fever": prevalence_fever,
        "temperature_mean_c": round(statistics.mean(temps), 2) if temps else None,
    }

    # Reproduction
    rp_values = [r.get("retained_placenta_hours") for r in rows if r.get("retained_placenta_hours") is not None]
    foul = [r for r in rows if r.get("uterine_discharge_foul")]
    milk_fever = [r for r in rows if r.get("clinical_milk_fever")]

    reproduction_metrics = {
        "prevalence_rp_gt_24h": round(sum(1 for h in rp_values if h > 24) / n * 100, 1) if rp_values else 0.0,
        "prevalence_foul_discharge": round(len(foul) / n * 100, 1),
        "prevalence_clinical_milk_fever": round(len(milk_fever) / n * 100, 1),
    }

    return {
        "milk": milk_metrics,
        "metabolic": metabolic_metrics,
        "reproduction": reproduction_metrics,
    }


def pick_boundary_sub_cases(rows: list[dict], max_cases: int = 3) -> list[dict]:
    """
    Выбираем крайние коровы для sub_cases.
    Приоритет: самое низкое отклонение удоя + наличие L1-флагов.
    """
    scored = []
    for r in rows:
        dev = r.get("deviation_pct", 0) or 0
        flags = 0
        if r.get("bhb") is not None and r["bhb"] >= 1.2:
            flags += 1
        if r.get("calcium_mmol_l") is not None and r["calcium_mmol_l"] < 2.0:
            flags += 1
        if r.get("temperature") is not None and r["temperature"] >= 39.2:
            flags += 1
        if r.get("clinical_milk_fever"):
            flags += 1
        if r.get("retained_placenta_hours") is not None and r["retained_placenta_hours"] > 24:
            flags += 1
        if r.get("uterine_discharge_foul"):
            flags += 1
        # чем ниже удой и больше флагов — тем важнее
        score = -dev + flags * 20
        scored.append((score, r))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [x[1] for x in scored[:max_cases]]


def build_raw_block(rows: list[dict]) -> dict[str, Any]:
    raw = {"cows": {}}
    for r in rows:
        cid = r["cow_id"]
        raw["cows"][cid] = {
            "dim": r.get("dim"),
            "parity": r.get("parity"),
            "milk_yield_actual_kg": r.get("milk_yield_actual"),
            "milk_yield_expected_kg": r.get("milk_yield_expected"),
            "bhb": r.get("bhb"),
            "temperature_c": r.get("temperature"),
            "retained_placenta_hours": r.get("retained_placenta_hours"),
            "uterine_discharge_foul": bool(r.get("uterine_discharge_foul")),
            "clinical_milk_fever": bool(r.get("clinical_milk_fever")),
            "calcium_mmol_l": r.get("calcium_mmol_l"),
        }
    return raw


def build_sub_cases(boundary_rows: list[dict]) -> list[dict]:
    sub_cases = []
    for r in boundary_rows:
        rationale_parts = []
        if r.get("bhb") is not None and r["bhb"] >= 1.2:
            rationale_parts.append(f"BHB {r['bhb']}")
        if r.get("calcium_mmol_l") is not None and r["calcium_mmol_l"] < 2.0:
            rationale_parts.append(f"Ca {r['calcium_mmol_l']}")
        if r.get("temperature") is not None and r["temperature"] >= 39.2:
            rationale_parts.append(f"T {r['temperature']}")
        if r.get("clinical_milk_fever"):
            rationale_parts.append("молочная лихорадка")
        if r.get("retained_placenta_hours") is not None and r["retained_placenta_hours"] > 24:
            rationale_parts.append(f"RP {r['retained_placenta_hours']}ч")
        if r.get("uterine_discharge_foul"):
            rationale_parts.append("гнойные выделения")

        sub_cases.append({
            "cow_id": r["cow_id"],
            "role": "boundary_case",
            "rationale": ", ".join(rationale_parts) if rationale_parts else "крайнее отклонение удоя",
        })
    return sub_cases


# ─────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Orchestrator v1: CSV → Group Case → Strategy")
    parser.add_argument("--csv", required=True, help="Path to merged/enterprise CSV")
    parser.add_argument("--farm", default="FARM-001", help="Farm name")
    parser.add_argument("--group-type", default="transition_period", help="Group type (v1: transition_period)")
    parser.add_argument("--dim-range", default="0-21", help="DIM range, e.g. 0-21")
    parser.add_argument("--out-dir", default="cases/group_cases", help="Where to save group case YAML")
    args = parser.parse_args()

    csv_path = Path(args.csv)
    if not csv_path.exists():
        print(f"Error: CSV not found: {csv_path}")
        raise SystemExit(1)

    # 1. Загружаем коров
    rows = load_merged_csv(str(csv_path))

    dim_min, dim_max = parse_dim_range(args.dim_range)
    group_rows = filter_rows(rows, dim_min, dim_max)

    if not group_rows:
        print(f"No cows found in DIM range {args.dim_range}. Nothing to orchestrate.")
        raise SystemExit(0)

    # 2. Считаем метрики
    metrics = compute_group_metrics(group_rows)

    # 3. Boundary sub-cases
    boundary_rows = pick_boundary_sub_cases(group_rows, max_cases=3)

    # 4. Строим group case
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    case_id = f"GROUP-{args.group_type.upper().replace('_', '-')}-{now.replace('-', '')}-001"
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{case_id}.yaml"

    n_at_risk = sum(
        1 for r in group_rows
        if (r.get("deviation_pct") or 0) < -10
        or (r.get("bhb") is not None and r["bhb"] >= 1.2)
        or (r.get("calcium_mmol_l") is not None and r["calcium_mmol_l"] < 2.0)
        or (r.get("temperature") is not None and r["temperature"] >= 39.2)
    )

    case = {
        "case_id": case_id,
        "date_created": now,
        "farm_id": args.farm,
        "analyst": "StanisSerg",
        "group": {
            "type": args.group_type,
            "dim_range": args.dim_range,
            "n_total": len(group_rows),
            "n_tested": len(group_rows),  # v1: считаем, что все протестированы
            "n_at_risk": n_at_risk,
        },
        "raw": build_raw_block(group_rows),
        "metrics": metrics,
        "sub_cases": build_sub_cases(boundary_rows),
    }

    # 5. Сохраняем и запускаем group engine
    save_yaml(str(out_path), case)

    attach_derived_group(case)
    results = [("RULE-001G", *rule_001g.evaluate(case))]
    merge_group_decisions(case, results)
    init_execution_from_strategy(case)
    save_yaml(str(out_path), case)

    # 6. Вывод
    gd = case.get("group_decision", {})
    strategy = gd.get("strategy") or {}
    exec_summary = case.get("execution", {}).get("summary", {})

    print()
    print("=" * 60)
    print(f"Orchestrator v1 — Group Case Created")
    print("=" * 60)
    print(f"  File: {out_path}")
    print(f"  Cows in group: {len(group_rows)} (at risk: {n_at_risk})")
    print()
    print(f"  Primary rule: {gd.get('primary_rule')}")
    print(f"  Label: {gd.get('label')}")
    print(f"  Severity: {gd.get('severity')}")
    print(f"  Action: {gd.get('action')}")
    print(f"  GHI: {case.get('derived_group', {}).get('group_health_index')}")
    print()
    print("  Strategy actions:")
    for a in strategy.get("actions", []):
        m = "[M]" if a.get("mandatory") else "[O]"
        print(f"    {m} {a['id']} ({a['type']}, scope={a['scope']})")
    print()
    print(f"  Execution: {exec_summary.get('mandatory_done', 0)}/{exec_summary.get('mandatory_total', 0)} mandatory planned")
    print("=" * 60)


if __name__ == "__main__":
    main()
