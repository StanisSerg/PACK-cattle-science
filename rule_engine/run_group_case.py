#!/usr/bin/env python3
"""
run_group_case.py — Group-Level Rule Engine

Usage:
    python3 run_group_case.py cases/group_cases/GROUP-TRANSITION-DEMO-001.yaml

Что делает:
    1. Загружает GROUP CASE из YAML
    2. Рассчитывает derived_group флаги
    3. Прогоняет через group rules
    4. Выбирает primary group decision
    5. Сохраняет результат обратно в кейс
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from group_models import (
    attach_derived_group,
    dataclass_to_dict,
    init_execution_from_strategy,
    load_yaml,
    save_yaml,
)
from group_rules import rule_001g


def merge_group_decisions(case: dict[str, Any], decision_blocks: list[tuple[str, Any, Any]]) -> None:
    """
    Объединить решения от всех групповых правил.
    Приоритет: critical > high > medium > low > monitor > normal
    """
    case["group_rule_results"] = []

    severity_priority = {
        "critical": 100,
        "high": 80,
        "medium": 60,
        "low": 40,
        "monitor": 30,
        "normal": 10,
    }

    best_score = -1
    primary_rule = None
    final_decision = None
    final_prediction = None
    all_reasoning: list[str] = []
    all_verdicts: list[str] = []

    for rule_name, decision, prediction in decision_blocks:
        if decision is None:
            continue

        dec_dict = dataclass_to_dict(decision)
        pred_dict = dataclass_to_dict(prediction) if prediction is not None else None

        case["group_rule_results"].append({
            "rule": rule_name,
            "decision": dec_dict,
            "prediction": pred_dict,
        })

        all_verdicts.append(decision.verdict)
        all_reasoning.extend(decision.reasoning)

        score = severity_priority.get(decision.severity, 0)
        if score > best_score:
            best_score = score
            primary_rule = rule_name
            final_decision = dec_dict
            final_prediction = pred_dict

    case["group_decision"] = {
        "primary_rule": primary_rule,
        "verdicts": all_verdicts,
        "severity": final_decision["severity"] if final_decision else None,
        "label": final_decision["label"] if final_decision else None,
        "action": final_decision["action"] if final_decision else None,
        "strategy": final_decision.get("strategy", {}) if final_decision else {},
        "reasoning": all_reasoning,
        "basis": final_decision["basis"] if final_decision else {},
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    case["group_prediction"] = final_prediction


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 run_group_case.py cases/group_cases/GROUP-XXX.yaml")
        raise SystemExit(1)

    path = sys.argv[1]
    if not Path(path).exists():
        print(f"Error: File not found: {path}")
        raise SystemExit(1)

    case = load_yaml(path)
    attach_derived_group(case)

    results = [
        ("RULE-001G", *rule_001g.evaluate(case)),
    ]

    merge_group_decisions(case, results)

    # Инициализируем execution план на основе strategy
    init_execution_from_strategy(case)

    save_yaml(path, case)

    gd = case.get("group_decision", {})
    print(f"✓ Updated group case: {path}")
    print(f"  Primary group rule: {gd.get('primary_rule')}")
    print(f"  Label: {gd.get('label')}")
    print(f"  Severity: {gd.get('severity')}")
    print(f"  Action: {gd.get('action')}")
    print(f"  Derived GHI: {case.get('derived_group', {}).get('group_health_index')}")

    pred = case.get("group_prediction")
    if pred:
        print(f"  Prediction target: {pred.get('target_value')} ({pred.get('primary_metric')})")
        print(f"  Timeframe: {pred.get('timeframe')}")


if __name__ == "__main__":
    main()
