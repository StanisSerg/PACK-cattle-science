"""
enterprise_loader.py — Загрузчик данных предприятия + интеграция MilkBot

Поддерживает:
  - Data.csv: поля №, Pen, Stat, DIM, Lactno, Milk, M305 (разделитель ';', запятая как десятичная)
  - Пример 3.csv: извлечение herd-level MilkBot кривой (колонка 'Длина лактации')
"""
from __future__ import annotations

import csv
from pathlib import Path


# Herd-level MilkBot curve из Пример 3.csv (DIM -> expected daily yield)
# Это эталонная кривая стада, масштабируется по M305 каждой коровы
HERD_MILKBOT_CURVE = {
    5: 26.91, 15: 33.11, 25: 37.23, 35: 39.87, 45: 41.46,
    55: 42.28, 65: 42.57, 75: 42.47, 85: 42.12, 95: 41.57,
    105: 40.91, 115: 40.15, 125: 39.35, 135: 38.51, 145: 37.66,
    155: 36.80, 165: 35.94, 175: 35.09, 185: 34.25, 195: 33.42,
    205: 32.61, 215: 31.81, 225: 31.03, 235: 30.27, 245: 29.53,
    255: 28.80, 265: 28.09, 275: 27.40, 285: 26.72, 295: 26.07,
    305: 25.42, 315: 24.80, 325: 24.18, 335: 23.59, 345: 23.00,
    355: 22.44, 365: 21.88, 375: 21.34, 385: 20.82, 395: 20.30,
    405: 19.80,
}

HERD_MILKBOT_DIMS = sorted(HERD_MILKBOT_CURVE.keys())
HERD_AVG_M305 = 7901.4  # Рассчитано из Data.csv


def lookup_herd_milkbot(dim: int) -> float:
    """Интерполяция herd-level MilkBot по DIM."""
    dims = HERD_MILKBOT_DIMS
    if dim <= dims[0]:
        return HERD_MILKBOT_CURVE[dims[0]]
    if dim >= dims[-1]:
        return HERD_MILKBOT_CURVE[dims[-1]]

    # Находим ближайшие точки
    for i in range(len(dims) - 1):
        if dims[i] <= dim <= dims[i + 1]:
            d1, d2 = dims[i], dims[i + 1]
            y1, y2 = HERD_MILKBOT_CURVE[d1], HERD_MILKBOT_CURVE[d2]
            # Линейная интерполяция
            return round(y1 + (y2 - y1) * (dim - d1) / (d2 - d1), 2)
    return HERD_MILKBOT_CURVE[dims[-1]]


def estimate_expected_yield_milkbot(dim: int, m305: float, herd_avg_m305: float = None) -> float:
    """Оценить ожидаемый удой коровы по herd MilkBot + её M305."""
    if herd_avg_m305 is None:
        herd_avg_m305 = HERD_AVG_M305
    if herd_avg_m305 <= 0:
        herd_avg_m305 = 7901.4
    base = lookup_herd_milkbot(dim)
    if not isinstance(m305, (int, float)) or m305 <= 0:
        return base
    return round(base * (m305 / herd_avg_m305), 2)


def parse_stat(stat: str) -> dict:
    """Преобразовать статус из Data.csv в нашу модель."""
    s = (stat or "").strip().upper()
    mapping = {
        "ТЕЧКА": {"reproduction_status": "open", "in_heat": True},
        "ОСЕМ": {"reproduction_status": "bred", "insemination_count": 1},
        "СТЕЛ": {"reproduction_status": "pregnant"},
        "БРАК": {"reproduction_status": "cull", "veterinary_hold": True},
        "ЯЛОВ": {"reproduction_status": "open", "barren": True},
    }
    return mapping.get(s, {"reproduction_status": "open"})


def load_enterprise_csv(path: str) -> list[dict]:
    """Загрузить Data.csv предприятия."""
    rows = []
    with open(path, "r", encoding="windows-1251") as f:
        reader = csv.DictReader(f, delimiter=";")
        for raw in reader:
            row = {}
            # ID
            row["cow_id"] = str(raw.get("№", "")).strip()
            if not row["cow_id"] or row["cow_id"].lower() == "№":
                continue

            # DIM и парность
            row["dim"] = int(raw.get("DIM", "0")) if raw.get("DIM") else 0
            row["parity"] = int(raw.get("Lactno", "0")) if raw.get("Lactno") else 0

            # Удой (запятая как десятичная)
            milk_str = (raw.get("Milk", "0") or "0").replace(",", ".")
            row["milk_yield"] = float(milk_str) if milk_str else 0.0
            row["milk_yield_actual"] = row["milk_yield"]

            # M305
            m305_str = (raw.get("M305", "0") or "0").replace(",", ".")
            row["m305"] = float(m305_str) if m305_str else 0.0

            # Pen / группа
            row["pen"] = raw.get("Pen", "").strip()

            # Статус
            stat_info = parse_stat(raw.get("Stat", ""))
            row["reproduction_status"] = stat_info.get("reproduction_status", "open")
            row["pregnancy_status"] = row["reproduction_status"]
            row["veterinary_hold"] = stat_info.get("veterinary_hold", False)
            row["in_heat"] = stat_info.get("in_heat", False)
            row["barren"] = stat_info.get("barren", False)

            # Осеменения — прокси из статуса
            row["insemination_count"] = 1 if row["reproduction_status"] == "bred" else 0
            row["reproductive_failures_count"] = max(0, row["insemination_count"] - 1)
            row["days_open"] = None

            # MilkBot expected yield
            row["milk_yield_expected"] = estimate_expected_yield_milkbot(row["dim"], row["m305"])

            # Пиковые данные — вычисляем приблизительно из M305
            # Пиковый удой ≈ M305 / 305 * 1.8 (эмпирика для высокопродуктивных)
            row["pik_milk"] = round(row["m305"] / 305 * 1.8, 1) if row["m305"] > 0 else None
            row["peak_day"] = 45  # Значение по умолчанию из их данных
            row["peak_week"] = 6
            row["milk_yield_peak"] = row["pik_milk"]

            # Заглушки для RULE-010
            row["metabolic_issues_count"] = 0
            row["mastitis_cases_90d"] = 0
            row["locomotion_score"] = None
            row["treatment_cost_90d"] = 0
            row["heifer_available"] = False
            row["genetic_value"] = None
            row["recent_purchase"] = False
            row["embryo_transfer"] = False
            row["expected_305d_yield"] = row["m305"]
            row["milk_yield_current"] = row["milk_yield_actual"]

            # Лактация
            row["is_lactating"] = row["reproduction_status"] not in ("dry", "cull")
            row["dry_cow"] = row["reproduction_status"] == "dry"
            row["bcs"] = None

            # Deviation
            actual = row["milk_yield_actual"] or 0
            expected = row["milk_yield_expected"] or 0
            row["deviation_pct"] = round(((actual - expected) / expected) * 100, 1) if expected > 0 else 0.0

            rows.append(row)
    return rows
