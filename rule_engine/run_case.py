"""
run_case.py - Главный скрипт для прогона кейса через правила

Usage:
    python run_case.py cases/CASE-001.yaml

Что делает:
    1. Загружает кейс из YAML
    2. Рассчитывает derived параметры
    3. Прогоняет через все активные правила
    4. Определяет primary decision
    5. Сохраняет результат обратно в кейс
"""
from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# Добавляем parent directory в path для импорта
sys.path.insert(0, str(Path(__file__).parent))

from models import (
    attach_derived,
    load_yaml,
    save_yaml,
    dataclass_to_dict,
)
from rules import rule_001, rule_002, rule_003, rule_004, rule_005, rule_006, rule_007, rule_008, rule_009, rule_010


def merge_decisions(case: dict[str, Any], decision_blocks: list[tuple[str, Any, Any]]) -> None:
    """
    Объединить решения от всех правил
    
    Логика приоритизации (v1):
    - BLOCKED правила имеют высший приоритет
    - Затем APPLICABLE / TRIGGERED
    - Затем GRAY_ZONE
    - Затем NOT_TRIGGERED
    """
    case["rule_results"] = []

    final_triggered: list[str] = []
    final_verdicts: list[str] = []
    final_reasoning: list[str] = []

    primary_rule = None
    action = None
    prediction = None

    # Приоритеты вердиктов
    priority = {
        "RULE_009_BLOCKED": 125,
        "RULE_005_EMERGENCY_IV_CALCIUM": 115,
        "RULE_005_ORAL_CALCIUM_PROTOCOL": 110,
        "RULE_006_BLOCKED": 108,
        "RULE_003_BLOCKED": 105,
        "RULE_003_NOT_APPLICABLE": 100,
        "RULE_001_BLOCKED": 95,
        "RULE_002_BLOCKED": 93,
        "RULE_004_BLOCKED": 92,
        "RULE_005_BLOCKED": 91,
        "RULE_007_BLOCKED": 90,
        "RULE_006_TRIGGERED_HIGH": 88,
        "RULE_001_TRIGGERED": 85,
        "RULE_003_APPLICABLE": 84,
        "RULE_002_TRIGGERED": 82,
        "RULE_004_RECOMMENDED_HIGH": 80,
        "RULE_005_DCAD_RECOMMENDED_HIGH": 79,
        "RULE_007_HIGH_RISK": 78,
        "RULE_009_HIGH_RISK": 76,
        "RULE_006_TRIGGERED_MEDIUM": 77,
        "RULE_004_RECOMMENDED_MEDIUM": 75,
        "RULE_005_DCAD_RECOMMENDED_MEDIUM": 74,
        "RULE_007_MEDIUM_RISK": 73,
        "RULE_009_MEDIUM_RISK": 72,
        "RULE_002_GRAY_ZONE": 70,
        "RULE_006_TRIGGERED_LOW": 69,
        "RULE_004_RECOMMENDED_LOW": 68,
        "RULE_005_DCAD_RECOMMENDED_LOW": 67,
        "RULE_007_LOW_RISK": 66,
        "RULE_009_LOW_RISK": 64,
        "RULE_005_PROPHYLACTIC_CALCIUM": 65,
        "RULE_010_CULL_RECOMMENDED_HIGH": 63,
        "RULE_008_HIGH_RISK": 62,
        "RULE_001_NOT_TRIGGERED": 60,
        "RULE_010_CULL_RECOMMENDED_MEDIUM": 59,
        "RULE_008_MEDIUM_RISK": 58,
        "RULE_006_NOT_APPLICABLE": 57,
        "RULE_005_NOT_APPLICABLE": 55,
        "RULE_004_NOT_APPLICABLE": 54,
        "RULE_005_MONITOR_PREVENTIVELY": 52,
        "RULE_006_NOT_TRIGGERED": 50,
        "RULE_010_CULL_RECOMMENDED_LOW": 49,
        "RULE_008_LOW_RISK": 48,
        "RULE_010_MONITOR_CLOSELY": 47,
        "RULE_008_NOT_APPLICABLE": 46,
        "RULE_007_NOT_APPLICABLE": 45,
        "RULE_009_NOT_TRIGGERED": 44,
        "RULE_007_NOT_TRIGGERED": 43,
        "RULE_010_NOT_TRIGGERED": 42,
        "RULE_010_NOT_APPLICABLE": 41,
        "RULE_003_NOT_TRIGGERED": 10,
        "RULE_002_NOT_TRIGGERED": 10,
    }

    best_score = -1

    for rule_name, decision, pred in decision_blocks:
        if decision is None:
            continue

        decision_dict = dataclass_to_dict(decision)
        pred_dict = dataclass_to_dict(pred) if pred is not None else None

        case["rule_results"].append(
            {
                "rule": rule_name,
                "decision": decision_dict,
                "prediction": pred_dict,
            }
        )

        final_triggered.extend(decision.triggered_rules)
        final_verdicts.extend(decision.verdicts)
        final_reasoning.extend(decision.reasoning)

        # Определяем приоритет этого решения
        local_score = max((priority.get(v, 0) for v in decision.verdicts), default=0)
        if local_score > best_score:
            best_score = local_score
            primary_rule = decision.primary_rule
            action = decision.action
            prediction = pred_dict

    case["decision"] = {
        "triggered_rules": final_triggered,
        "verdicts": final_verdicts,
        "primary_rule": primary_rule,
        "action": action,
        "reasoning": final_reasoning,
        "timestamp": datetime.now(timezone.utc).isoformat(),  # TODO: добавить реальное время
    }
    case["prediction"] = prediction


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python run_case.py cases/CASE-001.yaml")
        print("\nExample:")
        print("  python run_case.py cases/CASE-001.yaml")
        raise SystemExit(1)

    path = sys.argv[1]
    
    # Проверяем существование файла
    if not Path(path).exists():
        print(f"Error: File not found: {path}")
        raise SystemExit(1)

    # Загружаем кейс
    case = load_yaml(path)
    
    # Рассчитываем derived параметры
    attach_derived(case)
    
    # Прогоняем через правила
    results = [
        ("RULE-001", *rule_001.evaluate(case)),
        ("RULE-002", *rule_002.evaluate(case)),
        ("RULE-003", *rule_003.evaluate(case)),
        ("RULE-004", *rule_004.evaluate(case)),
        ("RULE-005", *rule_005.evaluate(case)),
        ("RULE-006", *rule_006.evaluate(case)),
        ("RULE-007", *rule_007.evaluate(case)),
        ("RULE-008", *rule_008.evaluate(case)),
        ("RULE-009", *rule_009.evaluate(case)),
        ("RULE-010", *rule_010.evaluate(case)),
    ]

    # Объединяем решения
    merge_decisions(case, results)
    
    # Сохраняем результат
    save_yaml(path, case)

    # Выводим результат
    print(f"✓ Updated case: {path}")
    print(f"  Primary rule: {case.get('decision', {}).get('primary_rule')}")
    print(f"  Action: {case.get('decision', {}).get('action')}")
    print(f"  Verdicts: {case.get('decision', {}).get('verdicts', [])}")
    
    # Показываем prediction если есть
    pred = case.get('prediction')
    if pred:
        print(f"  Prediction: {pred.get('direction')}")
        print(f"  Confidence: {pred.get('confidence')}")


if __name__ == "__main__":
    main()
