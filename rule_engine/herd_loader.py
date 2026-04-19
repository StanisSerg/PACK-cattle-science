"""
herd_loader.py — Общий загрузчик herd CSV и расчёт expected yield

Формат CSV:
    cow_id,dim,parity,milk_yield,pik_milk,pik_day,insemination_count,reproduction_status
"""
from __future__ import annotations

import csv


def estimate_expected_yield(dim: int, peak_milk: float, peak_day: int, parity: int) -> float:
    """Оценить ожидаемый удой по упрощённой лактационной кривой (L0)."""
    if not isinstance(peak_milk, (int, float)) or peak_milk <= 0:
        return 0.0
    if peak_day <= 0:
        peak_day = 35
    # До пика: линейный рост
    if dim <= peak_day:
        return round(peak_milk * (dim / peak_day), 1)
    # После пика: снижение ~0.15% в день
    return round(peak_milk * (0.9985 ** (dim - peak_day)), 1)


def load_herd_csv(path: str) -> list[dict]:
    rows = []
    with open(path, "r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Целочисленные поля
            for key in ["dim", "parity", "insemination_count"]:
                row[key] = int(row[key]) if row.get(key) else 0

            # Числа с плавающей точкой
            for key in ["milk_yield", "pik_milk"]:
                val = row.get(key, "")
                row[key] = float(val) if val != "" else None

            # pik_day -> peak_day и peak_week
            pik_day = row.get("pik_day", "")
            row["peak_day"] = int(pik_day) if pik_day != "" else 35
            row["peak_week"] = row["peak_day"] // 7 if row["peak_day"] > 0 else 5

            # Маппинг для rule engine
            row["milk_yield_actual"] = row.get("milk_yield")
            row["milk_yield_peak"] = row.get("pik_milk")
            row["milk_yield_expected"] = estimate_expected_yield(
                row["dim"],
                row.get("pik_milk") or 0,
                row.get("peak_day", 35),
                row.get("parity", 2),
            )

            # Репродуктивный статус
            row["reproduction_status"] = (row.get("reproduction_status") or "").strip().lower()
            row["pregnancy_status"] = row["reproduction_status"] if row["reproduction_status"] else "open"

            # Прокси для репродуктивных неудач
            insem = row.get("insemination_count", 0)
            row["reproductive_failures_count"] = max(0, insem - 1)
            row["days_open"] = None

            # Заглушки для health-полей RULE-010
            row["metabolic_issues_count"] = 0
            row["mastitis_cases_90d"] = 0
            row["locomotion_score"] = None
            row["treatment_cost_90d"] = 0
            row["heifer_available"] = False
            row["genetic_value"] = None
            row["recent_purchase"] = False
            row["embryo_transfer"] = False
            row["expected_305d_yield"] = 0
            row["milk_yield_current"] = row["milk_yield_actual"]

            # Статус лактации
            row["is_lactating"] = row["reproduction_status"] != "dry"
            row["dry_cow"] = row["reproduction_status"] == "dry"
            row["veterinary_hold"] = False
            row["bcs"] = None

            # Deviation для скрининга
            actual = row.get("milk_yield_actual") or 0
            expected = row.get("milk_yield_expected") or 0
            row["deviation_pct"] = round(((actual - expected) / expected) * 100, 1) if expected > 0 else 0.0

            rows.append(row)
    return rows
