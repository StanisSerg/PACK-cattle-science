"""
evaluate_case.py - Оценка результата (prediction vs fact)

Usage:
    python evaluate_case.py cases/CASE-001.yaml

Что делает:
    1. Загружает кейс с фактическими результатами
    2. Сравнивает prediction с fact
    3. Определяет success / partial / failure
    4. Классифицирует ошибку если есть
    5. Сохраняет результат
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).parent))

from models import load_yaml, save_yaml


def evaluate(case: dict[str, Any]) -> None:
    """Оценить кейс сравнив prediction с fact"""
    prediction = case.get("prediction") or {}
    fact = case.get("fact") or {}

    result: dict[str, Any] = {
        "status": None,
        "delta": {},
        "error_type": None,
        "root_cause": None,
    }

    # Извлекаем предсказанные и фактические значения
    bhb_fact = fact.get("bhb_day_7")
    dmi_fact = fact.get("dmi_day_7")

    bhb_range = (prediction.get("range") or {}).get("bhb_day_7")
    dmi_range = (prediction.get("range") or {}).get("dmi_day_7")

    checks = []

    # Проверяем BHB
    if isinstance(bhb_range, list) and len(bhb_range) == 2 and isinstance(bhb_fact, (int, float)):
        in_range = bhb_range[0] <= bhb_fact <= bhb_range[1]
        result["delta"]["bhb_day_7"] = {
            "predicted_range": bhb_range,
            "fact": bhb_fact,
            "within_range": in_range,
            "deviation": round(bhb_fact - sum(bhb_range) / 2, 3),
        }
        checks.append(in_range)

    # Проверяем DMI
    if isinstance(dmi_range, list) and len(dmi_range) == 2 and isinstance(dmi_fact, (int, float)):
        in_range = dmi_range[0] <= dmi_fact <= dmi_range[1]
        result["delta"]["dmi_day_7"] = {
            "predicted_range": dmi_range,
            "fact": dmi_fact,
            "within_range": in_range,
            "deviation": round(dmi_fact - sum(dmi_range) / 2, 3),
        }
        checks.append(in_range)

    # Определяем статус
    if checks and all(checks):
        result["status"] = "success"
        result["notes"] = "All metrics within predicted ranges"
    elif checks and any(checks):
        result["status"] = "partial"
        result["error_type"] = "PARTIAL_RESPONSE"
        result["notes"] = "Some metrics within range, others outside"
    else:
        result["status"] = "failure"
        result["error_type"] = "PREDICTION_MISS"
        result["notes"] = "Metrics outside predicted ranges"
        
        # Пытаемся определить root cause
        decision = case.get("decision", {})
        action = decision.get("action", "")
        
        if "PG" in action and bhb_fact and bhb_fact > 1.2:
            result["root_cause"] = "PG_PROTOCOL_FAILED"
        elif bhb_fact and bhb_fact > 1.2:
            result["root_cause"] = "TREATMENT_INADEQUATE"

    case["result"] = result


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python evaluate_case.py cases/CASE-001.yaml")
        print("\nExample:")
        print("  python evaluate_case.py cases/CASE-001.yaml")
        raise SystemExit(1)

    path = sys.argv[1]
    
    if not Path(path).exists():
        print(f"Error: File not found: {path}")
        raise SystemExit(1)

    case = load_yaml(path)
    
    # Проверяем наличие fact
    if not case.get("fact"):
        print(f"Warning: No 'fact' data in {path}")
        print("Add fact: section with actual outcomes before evaluating")
        raise SystemExit(1)
    
    evaluate(case)
    save_yaml(path, case)

    result = case.get("result", {})
    print(f"✓ Evaluation complete: {path}")
    print(f"  Status: {result.get('status')}")
    print(f"  Error type: {result.get('error_type') or 'None'}")
    print(f"  Root cause: {result.get('root_cause') or 'None'}")
    
    # Показываем delta
    delta = result.get("delta", {})
    for metric, values in delta.items():
        status = "✓" if values.get("within_range") else "✗"
        print(f"  {status} {metric}: fact={values.get('fact')}, predicted={values.get('predicted_range')}")


if __name__ == "__main__":
    main()
