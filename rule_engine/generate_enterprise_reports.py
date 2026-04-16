#!/usr/bin/env python3
"""
generate_enterprise_reports.py — Генерация продуктивности + метаболизма
из реальных данных предприятия (Data.csv + MilkBot кривая из Примера 3)

Usage:
    python generate_enterprise_reports.py /path/to/Data.csv --farm "ОАО МТК"

Выход:
    CS.WP.002-{date}-{farm}-productivity-report.md
    CS.WP.003-{date}-{farm}-metabolism-report.md
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from enterprise_loader import load_enterprise_csv
from models import Prediction
from rules import rule_010, rule_012


def dim_phase(dim: int) -> str:
    if dim <= 14:
        return "Переходный период"
    elif dim <= 30:
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


def generate_productivity_report(rows: list[dict], farm_name: str = "FARM-001") -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_cows = len(rows)
    lactating_cows = sum(1 for r in rows if r.get("is_lactating") and not r.get("dry_cow"))

    results = []
    for r in rows:
        res_012 = run_rule_012(r)
        res_010 = run_rule_010(r)
        results.append({**r, "rule_012": res_012, "rule_010": res_010})

    # Фазы
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

    # Парности
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

    # Алерты
    critical = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_CRITICAL_NEGATIVE"]
    moderate = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_MODERATE_NEGATIVE"]
    hyper = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_HYPERPRODUCTIVE_RISK"]
    persistence = [r for r in results if r["rule_012"]["verdict"] == "RULE_012_PERSISTENCE_ALERT"]
    cull_high = [r for r in results if r["rule_010"]["verdict"] == "RULE_010_CULL_RECOMMENDED_HIGH"]
    cull_medium = [r for r in results if r["rule_010"]["verdict"] == "RULE_010_CULL_RECOMMENDED_MEDIUM"]

    avg_actual = sum(r["milk_yield_actual"] for r in results if r.get("milk_yield_actual") is not None) / max(1, len(results))
    avg_expected = sum(r["milk_yield_expected"] for r in results if r.get("milk_yield_expected") is not None) / max(1, len(results))
    avg_m305 = sum(r["m305"] for r in results if r.get("m305") is not None) / max(1, len(results))

    phase_order = [
        ("Переходный период", "0-30"),
        ("Ранняя лактация", "0-30"),
        ("Рост к пику", "31-60"),
        ("Пик лактации", "61-100"),
        ("Плато", "101-200"),
        ("Снижение", "201-305"),
        ("Поздняя лактация", ">305"),
    ]
    phase_rows = []
    seen = set()
    for ph, dr in phase_order:
        if ph in seen:
            continue
        seen.add(ph)
        data = phases.get((ph, dr), {"count": 0, "actual_sum": 0.0, "expected_sum": 0.0})
        cnt = data["count"]
        avg_a = round(data["actual_sum"] / cnt, 1) if cnt > 0 else 0
        avg_e = round(data["expected_sum"] / cnt, 1) if cnt > 0 else 0
        pct = round((avg_a / avg_e) * 100, 0) if avg_e > 0 else 0
        phase_rows.append(f"| {ph} | {cnt} | {avg_a} кг | {pct}% | 🟢 |")

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

    critical_rows = [f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Срочный осмотр |" for r in critical[:10]]
    moderate_rows = [f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Проверить в течение 48ч |" for r in moderate[:10]]
    hyper_rows = [f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_expected', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Усилить мониторинг BHB |" for r in hyper[:10]]
    persistence_rows = [f"| {r['cow_id']} | {r['dim']} | {r.get('milk_yield_peak', '—')} | {r.get('milk_yield_actual', '—')} | {fmt_dev(r)} | Проверить рацион средней лактации |" for r in persistence[:10]]
    cull_high_rows = [f"| {r['cow_id']} | {r['dim']} | {r['parity']} | {r.get('m305', '—')} | {r['reproduction_status']} | Отсев оправдан |" for r in cull_high[:10]]
    cull_medium_rows = [f"| {r['cow_id']} | {r['dim']} | {r['parity']} | {r.get('m305', '—')} | {r['reproduction_status']} | Пересмотреть через 30 дней |" for r in cull_medium[:10]]

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
version: "2.0"
date_created: {now}
author: StanisSerg
---

# CS.WP.002: Отчёт о продуктивности стада

> **Тип:** Рабочий продукт — Продуктивность
> **Источник данных:** Data.csv предприятия (№, Stat, DIM, Lactno, Milk, M305)
> **Метод ожидаемой кривой:** MilkBot (кривая стада из Примера 3), масштабированная по M305
> **Для роли:** Консультант / Зоотехник / Руководитель хозяйства

---

## 1. РЕКВИЗИТЫ ОТЧЁТА

| Поле | Данные |
|------|--------|
| **Номер отчёта** | CS.WP.002-{now}-001 |
| **Дата составления** | {now} |
| **Хозяйство** | {farm_name} |
| **Размер стада** | {total_cows} голов (дойных: {lactating_cows}) |
| **Средний M305** | {round(avg_m305, 0)} кг |

---

## 2. СВОДКА ПО СТАДУ

### 2.1 Ключевые показатели

| Метрика | Факт | Целевой бенчмарк | Статус |
|---------|------|------------------|--------|
| Средний удой по стаду | {round(avg_actual, 1)} кг | 30-35 кг | {status_badge(avg_actual, 25, 38)} |
| Средний ожидаемый удой (MilkBot) | {round(avg_expected, 1)} кг | — | 🟢 |
| Средний M305 | {round(avg_m305, 0)} кг | 9500+ | {status_badge(avg_m305, 8000, 10000)} |

### 2.2 Распределение по фазам лактации

| Фаза | Кол-во коров | Средний удой | % от ожидаемого | Статус |
|------|--------------|--------------|-----------------|--------|
{chr(10).join(phase_rows)}

---

## 3. АНАЛИЗ ПО ГРУППАМ

### 3.1 По парности

| Парность | Кол-во | Средний удой | Пик (оценка) | Снижение от пика | Статус |
|----------|--------|--------------|--------------|------------------|--------|
{chr(10).join(parity_rows)}

### 3.2 По репродуктивному статусу

| Статус | Кол-во | Средний удой | Средний M305 | Примечание |
|--------|--------|--------------|--------------|------------|
| Течка (open) | {len([r for r in results if r['reproduction_status'] == 'open'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'open') / max(len([r for r in results if r['reproduction_status'] == 'open']), 1), 1)} кг | {round(sum(r.get('m305', 0) for r in results if r['reproduction_status'] == 'open') / max(len([r for r in results if r['reproduction_status'] == 'open']), 1), 0)} | Основная масса стада |
| Осеменённые (bred) | {len([r for r in results if r['reproduction_status'] == 'bred'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'bred') / max(len([r for r in results if r['reproduction_status'] == 'bred']), 1), 1)} кг | {round(sum(r.get('m305', 0) for r in results if r['reproduction_status'] == 'bred') / max(len([r for r in results if r['reproduction_status'] == 'bred']), 1), 0)} | Ожидание диагностики |
| Стельные (pregnant) | {len([r for r in results if r['reproduction_status'] == 'pregnant'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'pregnant') / max(len([r for r in results if r['reproduction_status'] == 'pregnant']), 1), 1)} кг | {round(sum(r.get('m305', 0) for r in results if r['reproduction_status'] == 'pregnant') / max(len([r for r in results if r['reproduction_status'] == 'pregnant']), 1), 0)} | Блокировка отсева |
| Брак (cull) | {len([r for r in results if r['reproduction_status'] == 'cull'])} | {round(sum(r.get('milk_yield_actual', 0) for r in results if r['reproduction_status'] == 'cull') / max(len([r for r in results if r['reproduction_status'] == 'cull']), 1), 1)} кг | {round(sum(r.get('m305', 0) for r in results if r['reproduction_status'] == 'cull') / max(len([r for r in results if r['reproduction_status'] == 'cull']), 1), 0)} | Исключены из анализа |

---

## 4. ОТКЛОНЕНИЯ УДОЯ (RULE-012)

### 4.1 Критическое снижение (> 20% ниже MilkBot)

| ID коровы | DIM | Ожидаемый | Фактический | Отклонение | Рекомендация |
|-----------|-----|-----------|-------------|------------|--------------|
{chr(10).join(critical_rows) if critical_rows else "| — | — | — | — | — | Нет критических отклонений |"}

### 4.2 Умеренное снижение (10-20% ниже MilkBot)

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

| ID коровы | DIM | Парность | M305 | Статус | Рекомендация |
|-----------|-----|----------|------|--------|--------------|
{chr(10).join(cull_high_rows) if cull_high_rows else "| — | — | — | — | — | Нет коров с высоким приоритетом |"}

### 5.2 Средний приоритет

| ID коровы | DIM | Парность | M305 | Статус | Рекомендация |
|-----------|-----|----------|------|--------|--------------|
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
- *MilkBot herd curve (a=54.5, b=33, c=5, d=0.0025)*
- *RULE-012: Milk-Yield-Deviation-Alert*
- *RULE-010: Culling-Decision-Support*
"""
    return report


def generate_metabolism_report(rows: list[dict], farm_name: str = "FARM-001") -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_cows = len(rows)
    lactating_cows = sum(1 for r in rows if r.get("is_lactating") and not r.get("dry_cow"))

    # Скрининги
    ketosis_candidates = [r for r in rows if 3 <= r["dim"] <= 14 and r.get("deviation_pct", 0) < -10 and r.get("is_lactating")]
    clinical_ketosis_candidates = [r for r in rows if 3 <= r["dim"] <= 14 and r.get("deviation_pct", 0) < -20 and r.get("is_lactating")]
    hypocalcemia_candidates = [r for r in rows if 1 <= r["dim"] <= 3 and r.get("deviation_pct", 0) < 0 and r.get("is_lactating")]
    metritis_candidates = [r for r in rows if 1 <= r["dim"] <= 21 and r.get("deviation_pct", 0) < -10 and r.get("parity", 1) >= 2 and r.get("is_lactating")]
    neb_candidates = [r for r in rows if r["dim"] < 60 and r.get("deviation_pct", 0) > 20 and r.get("is_lactating")]
    chronic_metabolic = [r for r in rows if 30 <= r["dim"] <= 100 and r.get("deviation_pct", 0) < -20 and r.get("is_lactating")]
    late_drop = [r for r in rows if r["dim"] > 200 and r.get("deviation_pct", 0) < -15 and r.get("is_lactating")]

    all_risk_ids = set(r["cow_id"] for r in ketosis_candidates + clinical_ketosis_candidates + hypocalcemia_candidates + metritis_candidates + neb_candidates + chronic_metabolic + late_drop)

    phase_counts = {}
    for r in rows:
        if not r.get("is_lactating"):
            continue
        ph = dim_phase(r["dim"])
        phase_counts.setdefault(ph, {"count": 0, "at_risk": 0})
        phase_counts[ph]["count"] += 1
    for r in rows:
        if r["cow_id"] in all_risk_ids and r.get("is_lactating"):
            ph = dim_phase(r["dim"])
            phase_counts[ph]["at_risk"] += 1

    phase_order = ["Переходный период", "Ранняя лактация", "Рост к пику", "Пик лактации", "Плато", "Снижение"]
    phase_rows = []
    for ph in phase_order:
        data = phase_counts.get(ph, {"count": 0, "at_risk": 0})
        cnt = data["count"]
        risk = data["at_risk"]
        pct = round((risk / cnt) * 100, 0) if cnt > 0 else 0
        badge = "🔴" if pct > 25 else "🟡" if pct > 10 else "🟢"
        phase_rows.append(f"| {ph} | {cnt} | {risk} | {pct}% | {badge} |")

    def row_fmt(r, note):
        return f"| {r['cow_id']} | {r['dim']} | {r['parity']} | {r.get('milk_yield_actual', '—')} | {r.get('milk_yield_expected', '—')} | {r.get('deviation_pct', '—')}% | {note} |"

    ketosis_rows = [row_fmt(r, "Взять BHB") for r in ketosis_candidates[:15]]
    hypocalcemia_rows = [row_fmt(r, "Контроль Ca, двигательная активность") for r in hypocalcemia_candidates[:10]]
    metritis_rows = [row_fmt(r, "Температура + выделения") for r in metritis_candidates[:15]]
    neb_rows = [row_fmt(r, "Мониторинг BHB, BCS, DMI") for r in neb_candidates[:10]]
    chronic_rows = [row_fmt(r, "Системный осмотр: кетоз, хромота, мастит") for r in chronic_metabolic[:10]]
    late_rows = [row_fmt(r, "Проверить питание поздней лактации") for r in late_drop[:10]]

    total_at_risk = len(all_risk_ids)
    transition_at_risk = len(set(r["cow_id"] for r in ketosis_candidates + hypocalcemia_candidates + metritis_candidates))
    missed_ketosis_cost = len(clinical_ketosis_candidates) * 28000
    missed_metritis_cost = len(metritis_candidates) * 15000
    total_risk_cost = missed_ketosis_cost + missed_metritis_cost

    report = f"""---
wp_ref: WP-093
entity_ref: CS.ENTITY.031
sota_refs:
  - CS.SOTA.071
  - CS.SOTA.284
rule_refs:
  - RULE-001
  - RULE-002
  - RULE-005
  - RULE-006
  - RULE-012
version: "2.0"
date_created: {now}
author: StanisSerg
---

# CS.WP.003: Скрининговый отчёт по метаболизму стада

> **Тип:** Рабочий продукт — Метаболизм (скрининг)
> **Источник данных:** Data.csv предприятия
> **Метод ожидаемой кривой:** MilkBot herd curve (Пример 3), масштабированная по M305
> **Для роли:** Ветеринарный специалист / Зоотехник

⚠️ **Важно:** Отчёт построен только на молочных данных. Он не ставит диагноз, а указывает коров для обследования.

---

## 1. РЕКВИЗИТЫ ОТЧЁТА

| Поле | Данные |
|------|--------|
| **Номер отчёта** | CS.WP.003-{now}-001 |
| **Дата составления** | {now} |
| **Хозяйство** | {farm_name} |
| **Размер стада** | {total_cows} голов (дойных: {lactating_cows}) |

---

## 2. СВОДКА ПО РИСКАМ

| Метрика | Значение | Примечание |
|---------|----------|------------|
| Всего коров в риске | {total_at_risk} | На основе отклонений от MilkBot |
| Из них в переходном периоде | {transition_at_risk} | Наиболее критичная группа |
| Кандидаты на кетоз (SCK) | {len(ketosis_candidates)} | DIM 3-14, отклонение < -10% |
| Кандидаты на клинический кетоз | {len(clinical_ketosis_candidates)} | DIM 3-14, отклонение < -20% |
| Кандидаты на гипокальceмию | {len(hypocalcemia_candidates)} | DIM 1-3, отрицательное отклонение |
| Кандидаты на метритис/RP | {len(metritis_candidates)} | DIM 1-21, отклонение < -10%, parity ≥2 |
| Риск NEB (гиперпродуктивность) | {len(neb_candidates)} | DIM < 60, удой > +20% от MilkBot |
| Хроническое метаболическое подавление | {len(chronic_metabolic)} | DIM 30-100, отклонение < -20% |

### 2.1 Распределение рисков по фазам лактации

| Фаза лактации | Коров всего | В риске | % риска | Статус |
|---------------|-------------|---------|---------|--------|
{chr(10).join(phase_rows)}

---

## 3. СКРИНИНГ ПЕРЕХОДНОГО ПЕРИОДА (0-21 DIM)

### 3.1 Кандидаты на субклинический кетоз (SCK)

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(ketosis_rows) if ketosis_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

### 3.2 Кандидаты на клинический кетоз

{chr(10).join([f"- **{r['cow_id']}** (DIM {r['dim']}, {r.get('deviation_pct', '—')}%): немедленно взять BHB, проверить аппетит" for r in clinical_ketosis_candidates]) if clinical_ketosis_candidates else "Нет кандидатов на клинический кетоз."}

### 3.3 Кандидаты на гипокальceмию

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(hypocalcemia_rows) if hypocalcemia_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

### 3.4 Кандидаты на метритис / задержку последа

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(metritis_rows) if metritis_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

---

## 4. СКРИНИНГ РАННЕЙ И СРЕДНЕЙ ЛАКТАЦИИ

### 4.1 Риск NEB — DIM < 60, гиперпродуктивность

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(neb_rows) if neb_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

### 4.2 Хроническое метаболическое подавление

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(chronic_rows) if chronic_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

---

## 5. ЭКОНОМИЧЕСКАЯ ОЦЕНКА РИСКА

| Риск | Кол-во кандидатов | Потенциальные потери |
|------|-------------------|----------------------|
| Клинический кетоз | {len(clinical_ketosis_candidates)} | {missed_ketosis_cost:,} ₽ |
| Метритис/RP | {len(metritis_candidates)} | {missed_metritis_cost:,} ₽ |
| **Итого потенциал экономии** | — | **{total_risk_cost:,} ₽** |

---

## 6. РЕКОМЕНДАЦИИ

### Сегодня
- [ ] BHB у коров с клиническим риском кетоза
- [ ] Температура + выделения у коров с риском метритиса
- [ ] Контроль Ca у коров DIM 1-3 с отклонением

### Эта неделя
- [ ] Настроить ежедневный скрининг: DIM < 30 + отклонение < -10%
- [ ] Пропиленгликоль для коров с BHB ≥ 1.2

### Месяц
- [ ] Добавить в выгрузку: BHB, температура, хромота
- [ ] Связать молочные данные с ветжурналом

---

*Отчёт создан автоматически на основе:*
- *MilkBot herd curve (a=54.5, b=33, c=5, d=0.0025)*
- *RULE-001/002/005/006/012*
"""
    return report


def main():
    parser = argparse.ArgumentParser(description="Generate enterprise reports from Data.csv")
    parser.add_argument("csv", help="Path to Data.csv")
    parser.add_argument("--farm", "-f", default="ОАО", help="Farm name")
    parser.add_argument("--out-dir", "-d", default=".", help="Output directory")
    args = parser.parse_args()

    rows = load_enterprise_csv(args.csv)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    safe_farm = args.farm.replace(" ", "-").replace("/", "-")

    prod_path = Path(args.out_dir) / f"CS.WP.002-{now}-{safe_farm}-productivity-report.md"
    meta_path = Path(args.out_dir) / f"CS.WP.003-{now}-{safe_farm}-metabolism-report.md"

    prod_report = generate_productivity_report(rows, farm_name=args.farm)
    with open(prod_path, "w", encoding="utf-8") as f:
        f.write(prod_report)
    print(f"✓ Productivity report: {prod_path}")

    meta_report = generate_metabolism_report(rows, farm_name=args.farm)
    with open(meta_path, "w", encoding="utf-8") as f:
        f.write(meta_report)
    print(f"✓ Metabolism report: {meta_path}")

    print(f"  Cows analyzed: {len(rows)}")


if __name__ == "__main__":
    main()
