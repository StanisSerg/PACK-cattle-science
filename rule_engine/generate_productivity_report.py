#!/usr/bin/env python3
"""
generate_productivity_report.py — Генератор отчёта CS.WP.002 по продуктивности

Usage:
    python generate_productivity_report.py herd_data.csv --out report.md

Формат CSV:
    cow_id,dim,parity,milk_yield_actual,milk_yield_expected,milk_yield_peak,peak_week,bcs,veterinary_hold,is_lactating

Что делает:
    1. Читает CSV с данными стада
    2. Прогоняет каждую корову через RULE-012
    3. Агрегирует статистику по фазам лактации и парности
    4. Заполняет шаблон CS.WP.002 и сохраняет в Markdown
"""
from __future__ import annotations

import argparse
import csv
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from models import Prediction
from rules import rule_012


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


def load_herd_csv(path: str) -> list[dict]:
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Type conversion
            for key in ["dim", "parity"]:
                row[key] = int(row[key]) if row.get(key) else 0
            for key in ["milk_yield_actual", "milk_yield_expected", "milk_yield_peak", "bcs"]:
                val = row.get(key, "")
                row[key] = float(val) if val != "" else None
            for key in ["peak_week"]:
                val = row.get(key, "")
                row[key] = int(val) if val != "" else None
            for key in ["veterinary_hold", "dry_cow", "is_lactating"]:
                val = row.get(key, "")
                if val.lower() in ("true", "1", "yes"):
                    row[key] = True
                elif val.lower() in ("false", "0", "no", ""):
                    row[key] = False
                else:
                    row[key] = False
            if "is_lactating" not in row:
                row["is_lactating"] = True
            rows.append(row)
    return rows


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


def generate_report(rows: list[dict], farm_name: str = "FARM-001") -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_cows = len(rows)
    lactating_cows = sum(1 for r in rows if r.get("is_lactating") and not r.get("dry_cow"))

    # Run RULE-012 for all lactating rows with data
    results = []
    for r in rows:
        res = run_rule_012(r)
        results.append({**r, **res})

    # Aggregates by DIM phase
    phases = {}
    for r in results:
        if r.get("verdict") == "NO_DATA":
            continue
        ph = dim_phase(r["dim"])
        dr = dim_range(r["dim"])
        key = (ph, dr)
        if key not in phases:
            phases[key] = {"count": 0, "actual_sum": 0.0, "expected_sum": 0.0}
        phases[key]["count"] += 1
        phases[key]["actual_sum"] += r.get("milk_yield_actual") or 0
        phases[key]["expected_sum"] += r.get("milk_yield_expected") or 0

    # Aggregates by parity
    parity_data = {}
    for r in results:
        if r.get("verdict") == "NO_DATA":
            continue
        pg = parity_group(r["parity"])
        if pg not in parity_data:
            parity_data[pg] = {"count": 0, "actual_sum": 0.0, "peak_sum": 0.0}
        parity_data[pg]["count"] += 1
        parity_data[pg]["actual_sum"] += r.get("milk_yield_actual") or 0
        peak = r.get("milk_yield_peak") or r.get("milk_yield_actual") or 0
        parity_data[pg]["peak_sum"] += peak

    # Alerts
    critical = [r for r in results if r.get("verdict") == "RULE_012_CRITICAL_NEGATIVE"]
    moderate = [r for r in results if r.get("verdict") == "RULE_012_MODERATE_NEGATIVE"]
    hyper = [r for r in results if r.get("verdict") == "RULE_012_HYPERPRODUCTIVE_RISK"]
    persistence = [r for r in results if r.get("verdict") == "RULE_012_PERSISTENCE_ALERT"]

    # Herd averages
    valid_actual = [r["milk_yield_actual"] for r in results if r.get("milk_yield_actual") is not None]
    valid_expected = [r["milk_yield_expected"] for r in results if r.get("milk_yield_expected") is not None]
    avg_actual = sum(valid_actual) / len(valid_actual) if valid_actual else 0
    avg_expected = sum(valid_expected) / len(valid_expected) if valid_expected else 0

    # Build phase table rows
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

    # Parity rows
    parity_order = ["1 (первотёлки)", "2", "3-4", "≥5"]
    parity_rows = []
    for pg in parity_order:
        data = parity_data.get(pg, {"count": 0, "actual_sum": 0.0, "peak_sum": 0.0})
        cnt = data["count"]
        avg_a = round(data["actual_sum"] / cnt, 1) if cnt > 0 else 0
        avg_p = round(data["peak_sum"] / cnt, 1) if cnt > 0 else 0
        drop = round(((avg_a - avg_p) / avg_p) * 100, 1) if avg_p > 0 else 0
        parity_rows.append(f"| {pg} | {cnt} | {avg_a} кг | {avg_p} кг | {drop}% | 🟢 |")

    # Alert rows critical
    critical_rows = []
    for r in critical[:10]:
        dev = r.get("deviation_pct")
        dev_str = f"{dev:.1f}%" if dev is not None else "—"
        critical_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {dev_str} | RULE-001/006/011 | Срочный осмотр |"
        )

    # Alert rows moderate
    moderate_rows = []
    for r in moderate[:10]:
        dev = r.get("deviation_pct")
        dev_str = f"{dev:.1f}%" if dev is not None else "—"
        moderate_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {dev_str} | Кетоз/мастит/метрит/хромота | Проверить в течение 48ч |"
        )

    # Hyper rows
    hyper_rows = []
    for r in hyper[:10]:
        dev = r.get("deviation_pct")
        dev_str = f"{dev:.1f}%" if dev is not None else "—"
        hyper_rows.append(
            f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {dev_str} | Высокий риск NEB, кетоза | Усилить мониторинг BHB |"
        )

    # Economics
    crit_loss_day = sum((r.get("milk_yield_expected", 0) - r.get("milk_yield_actual", 0)) for r in critical)
    mod_loss_day = sum((r.get("milk_yield_expected", 0) - r.get("milk_yield_actual", 0)) for r in moderate)
    price = 40  # rub/kg placeholder
    crit_30 = round(crit_loss_day * 30, 1)
    mod_30 = round(mod_loss_day * 30, 1)

    report = f"""---
wp_ref: WP-093
entity_ref: CS.ENTITY.031
sota_refs:
  - CS.SOTA.284
rule_refs:
  - RULE-012
version: "1.0"
date_created: {now}
author: StanisSerg
---

# CS.WP.002: Отчёт о продуктивности стада по группам и дням лактации

> **Тип:** Рабочий продукт
> **Источник данных:** Доильные системы / АСУ ТП / индивидуальные взвешивания
> **Для роли:** Консультант / Зоотехник / Руководитель хозяйства
> **Генерация:** Автоматическая через `rule_engine/generate_productivity_report.py`

---

## 1. РЕКВИЗИТЫ ОТЧЁТА

| Поле | Данные |
|------|--------|
| **Номер отчёта** | CS.WP.002-{now}-001 |
| **Дата составления** | {now} |
| **Период анализа** | Последние 7-14 дней |
| **Хозяйство** | {farm_name} |
| **Размер стада** | {total_cows} голов (дойных: {lactating_cows}) |
| **Система доения** | [Уточнить] |
| **Источник данных** | CSV import |

---

## 2. СВОДКА ПО СТАДУ

### 2.1 Ключевые показатели

| Метрика | Факт | Целевой бенчмарк | Статус |
|---------|------|------------------|--------|
| Средний удой по стаду | {round(avg_actual, 1)} кг | 30-35 кг | {status_badge(avg_actual, 25, 38)} |
| Пиковый удой (средний) | [Рассчитать] кг | 40-50 кг | 🟢 |
| Время достижения пика | [Рассчитать] недель | 4-8 недель | 🟢 |
| Персистентность (снижение/день) | [Рассчитать] | > -0.15% | 🟢 |
| Удой/DMI | [Рассчитать] | 1.4-1.6 | 🟢 |
| Жир/Белок | [Рассчитать] | > 1.12 | 🟢 |

### 2.2 Распределение по фазам лактации

| Фаза | Диапазон DIM | Кол-во коров | Средний удой | % от пика | Статус |
|------|--------------|--------------|--------------|-----------|--------|
{chr(10).join(phase_rows)}

---

## 3. АНАЛИЗ ПО ГРУППАМ

### 3.1 По парности

| Парность | Кол-во | Средний удой | Пиковый удой | Снижение от пика | Статус |
|----------|--------|--------------|--------------|------------------|--------|
{chr(10).join(parity_rows)}

---

## 4. ЛАКТАЦИОННАЯ КРИВАЯ (факт vs ожидаемая)

> График строится внешним инструментом (Excel/Python matplotlib) на основе агрегированных данных.

### 4.1 Точечное сравнение по неделям

| Неделя DIM | Ожидаемый удой | Фактический удой | Отклонение | Статус |
|------------|----------------|------------------|------------|--------|
| 1 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 2 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 4 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 8 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 12 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 20 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 30 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |
| 40 | [XX.X] | [XX.X] | [±X.X]% | 🟢 |

---

## 5. ОТКЛОНЕНИЯ И АЛЕРТЫ (генерируется RULE-012)

### 5.1 Коровы с критическим отклонением удоя (> 20% ниже ожидаемого)

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Вероятная причина (Rule Engine) | Рекомендация |
|-----------|-----|-----------|-------------|------------|--------------------------------|--------------|
{chr(10).join(critical_rows) if critical_rows else "| — | — | — | — | — | — | Нет критических отклонений |"}

### 5.2 Коровы с умеренным отклонением (10-20% ниже ожидаемого)

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Приоритет проверки |
|-----------|-----|-----------|-------------|------------|-------------------|
{chr(10).join(moderate_rows) if moderate_rows else "| — | — | — | — | — | Нет умеренных отклонений |"}

### 5.3 Гиперпродуктивность с риском метаболизма (> 20% выше ожидаемого в ранней лактации)

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Риск |
|-----------|-----|-----------|-------------|------------|------|
{chr(10).join(hyper_rows) if hyper_rows else "| — | — | — | — | — | Нет гиперпродуктивных коров |"}

### 5.4 Быстрое снижение персистентности

| ID коровы | DIM | Пик | Фактический | Отклонение от ожидаемой кривой | Рекомендация |
|-----------|-----|-----|-------------|-------------------------------|--------------|
{chr(10).join([f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_peak', '—')} | {r.get('milk_yield_actual', '—')} | {r.get('deviation_pct', '—')}% | Проверить рацион средней лактации |" for r in persistence[:10]]) if persistence else "| — | — | — | — | — | Нет отклонений персистентности |"}

---

## 6. ЭКОНОМИЧЕСКАЯ ОЦЕНКА

### 6.1 Потери от недополученного молока

| Группа отклонений | Кол-во коров | Средняя потеря/день | Суммарная потеря/день | Потери за 30 дней |
|-------------------|--------------|---------------------|-----------------------|-------------------|
| Критическое (>20%) | {len(critical)} | {round(crit_loss_day / max(len(critical), 1), 1)} кг | {round(crit_loss_day, 1)} кг | {crit_30} кг |
| Умеренное (10-20%) | {len(moderate)} | {round(mod_loss_day / max(len(moderate), 1), 1)} кг | {round(mod_loss_day, 1)} кг | {mod_30} кг |
| **ИТОГО** | **{len(critical) + len(moderate)}** | — | **{round(crit_loss_day + mod_loss_day, 1)} кг** | **{round((crit_loss_day + mod_loss_day) * 30, 1)} кг** |

### 6.2 Пересчёт в деньги (по {price} ₽/кг)

| Статья | Расчёт | Сумма (руб/мес) |
|--------|--------|-----------------|
| Потери молока (критические) | {crit_30} кг × {price} ₽/кг | {crit_30 * price:,} |
| Потери молока (умеренные) | {mod_30} кг × {price} ₽/кг | {mod_30 * price:,} |
| **ИТОГО потери** | | **{(crit_30 + mod_30) * price:,}** |

### 6.3 Потенциал роста

| Мера | Ожидаемый эффект | Экономический эффект (руб/мес) |
|------|------------------|-------------------------------|
| Снижение критических отклонений на 50% | +{round(crit_loss_day * 0.5 * 30, 0)} кг/мес | {round(crit_loss_day * 0.5 * 30 * price):,} |
| Снижение умеренных отклонений на 30% | +{round(mod_loss_day * 0.3 * 30, 0)} кг/мес | {round(mod_loss_day * 0.3 * 30 * price):,} |
| **ИТОГО потенциал** | **+{round((crit_loss_day * 0.5 + mod_loss_day * 0.3) * 30, 0)} кг/мес** | **{round((crit_loss_day * 0.5 + mod_loss_day * 0.3) * 30 * price):,}** |

---

## 7. РЕКОМЕНДАЦИИ

### 7.1 Немедленные действия (0-7 дней)
- [ ] Проверить всех коров с критическим отклонением по RULE-001 (кетоз), RULE-006 (метрит), RULE-011 (мастит)
- [ ] Забрать кровь/мочу на BHB у коров с DIM < 30 и низким удоем
- [ ] Проверить качество ТМР и DMI в ранней лактации

### 7.2 Краткосрочные действия (7-30 дней)
- [ ] Настроить автоматические алерты RULE-012 для ежедневного мониторинга
- [ ] Провести тренинг персонала по ранним признакам метаболических заболеваний
- [ ] Оптимизировать рацион для групп с наибольшими отклонениями

### 7.3 Долгосрочные действия (1-3 месяца)
- [ ] Проанализировать генетическую реализацию потенциала — корректировать селекцию
- [ ] Интегрировать данные удоя с данными здоровья (Rule Engine) в единый дашборд

---

## 8. ПРИЛОЖЕНИЯ

### 8.1 Исходные данные
- Файл сырых данных: `herd_data.csv`
- Дата выгрузки: {now}
- Количество записей: {total_cows}

### 8.2 Методология расчёта ожидаемой кривой
- Используется стандартная лактационная кривая с поправкой на породу, парность и генетический потенциал
- Бенчмарки основаны на `CS.ENTITY.031` (Milk yield)

### 8.3 История изменений

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | {now} | Первоначальная версия | generate_productivity_report.py |

---

*Отчёт создан автоматически на основе:*
- *RULE-012: Milk-Yield-Deviation-Alert*
- *CS.ENTITY.031: Milk yield*
- *CS.SOTA.284: Milking the data for value-driven dairy farming*
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

    print(f"✓ Report generated: {args.out}")
    print(f"  Cows analyzed: {len(rows)}")


if __name__ == "__main__":
    main()
