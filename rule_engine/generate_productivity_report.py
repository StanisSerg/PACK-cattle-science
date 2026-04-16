#!/usr/bin/env python3
"""
generate_productivity_report.py — Генератор отчёта CS.WP.002 по продуктивности

Usage:
    python generate_productivity_report.py herd_data.csv --out report.md

Формат CSV:
    cow_id,dim,parity,milk_yield,pik_milk,pik_day,insemination_count,reproduction_status
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from herd_loader import load_herd_csv
from models import Prediction
from rules import rule_010, rule_012


def dim_phase(dim: int) -> str:
    if dim <= 30:
        return "Ранняя лактация"
    elif dim <= 60:
        return "Рост к пику"
    elif dim <= 100:
        return "Пик лактации"
    elif dim <= 200:
        return "Плато"
    elif dim <= 305:
        return "Снижение"
    return "Поздняя лактация"


def dim_range(dim: int) -> str:
    if dim <= 30:
        return "0-30"
    elif dim <= 60:
        return "31-60"
    elif dim <= 100:
        return "61-100"
    elif dim <= 200:
        return "101-200"
    elif dim <= 305:
        return "201-305"
    return ">305"


def parity_group(parity: int) -> str:
    if parity == 1:
        return "1 (первотёлки)"
    elif parity == 2:
        return "2"
    elif 3 <= parity <= 4:
        return "3-4"
    return "≥5"


def status_badge(value: float, low: float, high: float) -> str:
    if value < low:
        return "🔴"
    elif value > high:
        return "🟡"
    return "🟢"


def run_rule_012(row: dict) -> dict:
    case = {"input": row}
    decision, prediction = rule_012.evaluate(case)
    if decision is None:
        return {
            "verdict": "NO_DATA",
            "action": "—",
            "deviation_pct": None,
            "confidence": "—",
        }
    deviation = decision.basis.get("conditions", {}).get("deviation_pct")
    return {
        "verdict": decision.verdicts[0],
        "action": decision.action,
        "deviation_pct": deviation,
        "confidence": prediction.confidence.upper() if prediction and prediction.confidence else "—",
    }


def run_rule_010(row: dict) -> dict:
    case = {"input": row}
    decision, prediction = rule_010.evaluate(case)
    if decision is None:
        return {
            "verdict": "NO_DATA",
            "action": "—",
            "confidence": "—",
        }
    return {
        "verdict": decision.verdicts[0],
        "action": decision.action,
        "confidence": prediction.confidence.upper() if prediction and prediction.confidence else "—",
    }


def generate_report(rows: list[dict], farm_name: str = "FARM-001") -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_cows = len(rows)
    lactating_cows = sum(1 for r in rows if r.get("is_lactating") and not r.get("dry_cow"))

    # Прогоняем правила
    results = []
    for r in rows:
        res_012 = run_rule_012(r)
        res_010 = run_rule_010(r)
        results.append({**r, "rule_012": res_012, "rule_010": res_010})

    # Агрегации по фазам DIM
    phases = {}
    for r in results:
        if r["rule_012"]["verdict"] == "NO_DATA":
            continue
        ph = dim_phase(r["dim"])
        dr = dim_range(r["dim"])
        key = (ph, dr)
        if key not in phases:
            phases[key] = {"count": 0, "actual_sum": 0.0, "expected_sum": 0.0}
        phases[key]["count"] += 1
        phases[key]["actual_sum"] += r.get("milk_yield_actual") or 0
        phases[key]["expected_sum"] += r.get("milk_yield_expected") or 0

    # Агрегации по парности
    parity_data = {}
    for r in results:
        if r["rule_012"]["verdict"] == "NO_DATA":
            continue
        pg = parity_group(r["parity"])
        if pg not in parity_data:
            parity_data[pg] = {"count": 0, "actual_sum": 0.0, "peak_sum": 0.0}
        parity_data[pg]["count"] += 1
        parity_data[pg]["actual_sum"] += r.get("milk_yield_actual") or 0
        peak = r.get("milk_yield_peak") or r.get("milk_yield_actual") or 0
        parity_data[pg]["peak_sum"] += peak

    # Алерты RULE-012
    critical = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_CRITICAL_NEGATIVE"]
    moderate = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_MODERATE_NEGATIVE"]
    hyper = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_HYPERPRODUCTIVE_RISK"]
    persistence = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_PERSISTENCE_ALERT"]

    # Алерты RULE-010
    cull_high = [r for r in results if r["rule_010"]["verdict"] == "RULE_010_CULL_RECOMMENDED_HIGH"]
    cull_medium = [r for r in results if r["rule_010"]["verdict"] == "RULE_010_CULL_RECOMMENDED_MEDIUM"]

    # Средние по стаду
    valid_actual = [r["milk_yield_actual"] for r in results if r.get("milk_yield_actual") is not None]
    valid_expected = [r["milk_yield_expected"] for r in results if r.get("milk_yield_expected") is not None]
    avg_actual = sum(valid_actual) / len(valid_actual) if valid_actual else 0
    avg_expected = sum(valid_expected) / len(valid_expected) if valid_expected else 0

    # Таблица фаз
    phase_order = [
        ("Ранняя лактация", "0-30"),
        ("Рост к пику", "31-60"),
        ("Пик лактации", "61-100"),
        ("Плато", "101-200"),
        ("Снижение", "201-305"),
        ("Поздняя лактация", ">305"),
    ]
    phase_rows = []
    for ph, dr in phase_order:
        data = phases.get((ph, dr), {"count": 0, "actual_sum": 0.0, "expected_sum": 0.0})
        cnt = data["count"]
        avg_a = round(data["actual_sum"] / cnt, 1) if cnt > 0 else 0
        avg_e = round(data["expected_sum"] / cnt, 1) if cnt > 0 else 0
        pct = round((avg_a / avg_e) * 100, 0) if avg_e > 0 else 0
        phase_rows.append(f"| {ph} | {dr} | {cnt} | {avg_a} кг | {pct}% | 🟢 |")

    # Таблица парностей
    parity_order = ["1 (первотёлки)", "2", "3-4", "≥5"]
    parity_rows = []
    for pg in parity_order:
        data = parity_data.get(pg, {"count": 0, "actual_sum": 0.0, "peak_sum": 0.0})
        cnt = data["count"]
        avg_a = round(data["actual_sum"] / cnt, 1) if cnt > 0 else 0
        avg_p = round(data["peak_sum"] / cnt, 1) if cnt > 0 else 0
        drop = round(((avg_a - avg_p) / avg_p) * 100, 1) if avg_p > 0 else 0
        parity_rows.append(f"| {pg} | {cnt} | {avg_a} кг | {avg_p} кг | {drop}% | 🟢 |")

    def fmt_dev(r):
        dev = r["rule_012"].get("deviation_pct")
        return f"{dev:.1f}%" if dev is not None else "—"

    critical_rows = []
    for r in critical[:10]:
        critical_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Срочный осмотр |"
        )

    moderate_rows = []
    for r in moderate[:10]:
        moderate_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Проверить в течение 48ч |"
        )

    hyper_rows = []
    for r in hyper[:10]:
        hyper_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Усилить мониторинг BHB |"
        )

    persistence_rows = []
    for r in persistence[:10]:
        persistence_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_peak', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Проверить рацион средней лактации |"
        )

    cull_high_rows = []
    for r in cull_high[:10]:
        cull_high_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r['parity']} | {r.get('insemination_count', 0)} | {r['reproduction_status']} | Отсев оправдан |"
        )

    cull_medium_rows = []
    for r in cull_medium[:10]:
        cull_medium_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r['parity']} | {r.get('insemination_count', 0)} | {r['reproduction_status']} | Пересмотреть через 30 дней |"
        )

    # Экономика
    crit_loss_day = sum((r.get("milk_yield_expected", 0) - r.get("milk_yield_actual", 0)) for r in critical)
    mod_loss_day = sum((r.get("milk_yield_expected", 0) - r.get("milk_yield_actual", 0)) for r in moderate)
    price = 40
    crit_30 = round(crit_loss_day * 30, 1)
    mod_30 = round(mod_loss_day * 30, 1)

    report = f"""---
wp_ref: WP-093
entity_ref: CS.ENTITY.031
sota_refs:
  - CS.SOTA.284
rule_refs:
  - RULE-012
  - RULE-010
version: "1.1"
date_created: {now}
author: StanisSerg
---

# CS.WP.002: Отчёт о продуктивности стада

> **Тип:** Рабочий продукт — Продуктивность
> **Источник данных:** Доильные системы (id, DIM, parity, milk_yield, pik_milk, pik_day, insemination_count, reproduction_status)
> **Для роли:** Консультант / Зоотехник / Руководитель хозяйства
> **Генерация:** Автоматическая через `rule_engine/generate_productivity_report.py`

---

## 1. РЕКВИЗИТЫ ОТЧЁТА

| Поле | Данные |
|------|--------|
| **Номер отчёта** | CS.WP.002-{now}-001 |
| **Дата составления** | {now} |
| **Период анализа** | Текущие данные |
| **Хозяйство** | {farm_name} |
| **Размер стада** | {total_cows} голов (дойных: {lactating_cows}) |

---

## 2. СВОДКА ПО СТАДУ

### 2.1 Ключевые показатели

| Метрика | Факт | Целевой бенчмарк | Статус |
|---------|------|------------------|--------|
| Средний удой по стаду | {round(avg_actual, 1)} кг | 30-35 кг | {status_badge(avg_actual, 25, 38)} |
| Средний ожидаемый удой | {round(avg_expected, 1)} кг | — | 🟢 |

### 2.2 Распределение по фазам лактации

| Фаза | Диапазон DIM | Кол-во коров | Средний удой | % от ожидаемого | Статус |
|------|--------------|--------------|--------------|-----------------|--------|
{chr(10).join(phase_rows)}

---

## 3. АНАЛИЗ ПО ГРУППАМ

### 3.1 По парности

| Парность | Кол-во | Средний удой | Пиковый удой | Снижение от пика | Статус |
|----------|--------|--------------|--------------|------------------|--------|
{chr(10).join(parity_rows)}

### 3.2 По репродуктивному статусу

| Статус | Кол-во | Средний удой | Среднее осеменений | Примечание |
|--------|--------|--------------|--------------------|------------|
| Открытые (open) | {len([r for r in results if r['reproduction_status'] == 'open'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'open') / max(len([r for r in results if r['reproduction_status'] == 'open']), 1), 1)} кг | {round(sum(r.get('insemination_count', 0) for r in results if r['reproduction_status'] == 'open') / max(len([r for r in results if r['reproduction_status'] == 'open']), 1), 1)} | Риск при insem ≥ 3 |
| Осеменённые (bred) | {len([r for r in results if r['reproduction_status'] == 'bred'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'bred') / max(len([r for r in results if r['reproduction_status'] == 'bred']), 1), 1)} кг | {round(sum(r.get('insemination_count', 0) for r in results if r['reproduction_status'] == 'bred') / max(len([r for r in results if r['reproduction_status'] == 'bred']), 1), 1)} | Ожидание диагностики |
| Стельные (pregnant) | {len([r for r in results if r['reproduction_status'] == 'pregnant'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'pregnant') / max(len([r for r in results if r['reproduction_status'] == 'pregnant']), 1), 1)} кг | {round(sum(r.get('insemination_count', 0) for r in results if r['reproduction_status'] == 'pregnant') / max(len([r for r in results if r['reproduction_status'] == 'pregnant']), 1), 1)} | Блокировка отсева |

---

## 4. ОТКЛОНЕНИЯ УДОЯ (RULE-012)

### 4.1 Критическое снижение (> 20% ниже ожидаемого)

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Рекомендация |
|-----------|-----|-----------|-------------|------------|--------------|
{chr(10).join(critical_rows) if critical_rows else "| — | — | — | — | — | Нет критических отклонений |"}

### 4.2 Умеренное снижение (10-20% ниже)

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Рекомендация |
|-----------|-----|-----------|-------------|------------|--------------|
{chr(10).join(moderate_rows) if moderate_rows else "| — | — | — | — | — | Нет умеренных отклонений |"}

### 4.3 Гиперпродуктивность с риском метаболизма

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Рекомендация |
|-----------|-----|-----------|-------------|------------|--------------|
{chr(10).join(hyper_rows) if hyper_rows else "| — | — | — | — | — | Нет гиперпродуктивных коров |"}

### 4.4 Быстрое снижение персистентности

| ID коровы | DIM | Пик | Фактический | Отклонение | Рекомендация |
|-----------|-----|-----|-------------|------------|--------------|
{chr(10).join(persistence_rows) if persistence_rows else "| — | — | — | — | — | Нет отклонений персистентности |"}

---

## 5. РЕКОМЕНДАЦИИ ПО ОТСЕВУ (RULE-010)

### 5.1 Высокий приоритет

| ID коровы | DIM | Парность | Осеменений | Статус | Рекомендация |
|-----------|-----|----------|------------|--------|--------------|
{chr(10).join(cull_high_rows) if cull_high_rows else "| — | — | — | — | — | Нет коров с высоким приоритетом |"}

### 5.2 Средний приоритет

| ID коровы | DIM | Парность | Осеменений | Статус | Рекомендация |
|-----------|-----|----------|------------|--------|--------------|
{chr(10).join(cull_medium_rows) if cull_medium_rows else "| — | — | — | — | — | Нет коров со средним приоритетом |"}

---

## 6. ЭКОНОМИЧЕСКАЯ ОЦЕНКА

| Группа | Кол-во | Потеря/день | Потери за 30 дней | Сумма ({price} ₽/кг) |
|--------|--------|-------------|-------------------|----------------------|
| Критическое (>20%) | {len(critical)} | {round(crit_loss_day / max(len(critical), 1), 1)} кг | {crit_30} кг | {crit_30 * price:,} ₽ |
| Умеренное (10-20%) | {len(moderate)} | {round(mod_loss_day / max(len(moderate), 1), 1)} кг | {mod_30} кг | {mod_30 * price:,} ₽ |
| **ИТОГО** | **{len(critical) + len(moderate)}** | — | **{round((crit_loss_day + mod_loss_day) * 30, 1)} кг** | **{(crit_30 + mod_30) * price:,} ₽** |

---

*Отчёт создан автоматически:*
- *RULE-012: Milk-Yield-Deviation-Alert*
- *RULE-010: Culling-Decision-Support*
- *CS.ENTITY.031: Milk yield*
"""
    return report


def main():
    parser = argparse.ArgumentParser(description="Generate CS.WP.002 productivity report")
    parser.add_argument("csv", help="Path to herd data CSV")
    parser.add_argument("--out", "-o", default="CS.WP.002-productivity-report.md", help="Output markdown file")
    parser.add_argument("--farm", "-f", default="FARM-001", help="Farm name")
    args = parser.parse_args()

    rows = load_herd_csv(args.csv)
    report = generate_report(rows, farm_name=args.farm)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✓ Productivity report generated: {args.out}")
    print(f"  Cows analyzed: {len(rows)}")


if __name__ == "__main__":
    main()
