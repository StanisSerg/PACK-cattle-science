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
from rules import rule_002, rule_003


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
        "RULE_003_BLOCKED": 100,
        "RULE_003_NOT_APPLICABLE": 95,
        "RULE_002_BLOCKED": 90,
        "RULE_003_APPLICABLE": 80,
        "RULE_002_TRIGGERED": 70,
        "RULE_002_GRAY_ZONE": 60,
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
        ("RULE-002", *rule_002.evaluate(case)),
        ("RULE-003", *rule_003.evaluate(case)),
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
