#!/usr/bin/env python3
"""
generate_metabolism_report.py — Скрининговый отчёт по метаболизму (CS.WP.003-META)

Usage:
    python generate_metabolism_report.py herd_data.csv --out report.md

Формат CSV:
    cow_id,dim,parity,milk_yield,pik_milk,pik_day,insemination_count,reproduction_status

Важно:
    Это СКРИНИНГОВЫЙ отчёт. Без лабораторных данных (BHB, Ca, температура,
    характер выделений) он не ставит диагноз, а указывает коров с высоким
    риском метаболических нарушений на основе прокси: DIM + отклонение удоя.
"""
from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from herd_loader import load_herd_csv


def dim_phase(dim: int) -> str:
    if dim <= 14:
        return "Переходный период"
    elif dim <= 30:
        return "Ранняя лактация"
    elif dim <= 60:
        return "Рост к пику"
    elif dim <= 100:
        return "Пик"
    elif dim <= 200:
        return "Плато"
    return "Снижение"


def generate_report(rows: list[dict], farm_name: str = "FARM-001") -> str:
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    total_cows = len(rows)
    lactating_cows = sum(1 for r in rows if r.get("is_lactating") and not r.get("dry_cow"))

    # --- ПРОКСИ-СКРИНИНГИ НА ОСНОВЕ ТОЛЬКО МОЛОЧНЫХ ДАННЫХ ---

    # 1. Риск кетоза (SCK): DIM 3-14 + отклонение < -10%
    ketosis_candidates = [
        r for r in rows
        if 3 <= r["dim"] <= 14
        and r.get("deviation_pct", 0) < -10
        and r.get("is_lactating")
    ]

    # 2. Риск тяжёлого/клинического кетоза: DIM 3-14 + отклонение < -20%
    clinical_ketosis_candidates = [
        r for r in rows
        if 3 <= r["dim"] <= 14
        and r.get("deviation_pct", 0) < -20
        and r.get("is_lactating")
    ]

    # 3. Риск гипокальceмии: DIM 1-3 + любое отрицательное отклонение
    hypocalcemia_candidates = [
        r for r in rows
        if 1 <= r["dim"] <= 3
        and r.get("deviation_pct", 0) < 0
        and r.get("is_lactating")
    ]

    # 4. Риск метритиса/RP: DIM 1-21 + отклонение < -10% + parity >= 2
    metritis_candidates = [
        r for r in rows
        if 1 <= r["dim"] <= 21
        and r.get("deviation_pct", 0) < -10
        and r.get("parity", 1) >= 2
        and r.get("is_lactating")
    ]

    # 5. Риск NEB: DIM < 60 + удой > 120% от expected (hyperproductive)
    neb_candidates = [
        r for r in rows
        if r["dim"] < 60
        and r.get("deviation_pct", 0) > 20
        and r.get("is_lactating")
    ]

    # 6. Хроническое метаболическое подавление: DIM 30-100 + отклонение < -20%
    chronic_metabolic = [
        r for r in rows
        if 30 <= r["dim"] <= 100
        and r.get("deviation_pct", 0) < -20
        and r.get("is_lactating")
    ]

    # 7. Поздняя лактация с резким падением: DIM > 200 + отклонение < -15%
    late_drop = [
        r for r in rows
        if r["dim"] > 200
        and r.get("deviation_pct", 0) < -15
        and r.get("is_lactating")
    ]

    # --- СТАТИСТИКА ПО ФАЗАМ ---
    phase_counts = {}
    for r in rows:
        if not r.get("is_lactating"):
            continue
        ph = dim_phase(r["dim"])
        phase_counts.setdefault(ph, {"count": 0, "at_risk": 0})
        phase_counts[ph]["count"] += 1

    # Mark at-risk per phase
    all_risk_ids = set()
    for r in (
        ketosis_candidates + clinical_ketosis_candidates + hypocalcemia_candidates
        + metritis_candidates + neb_candidates + chronic_metabolic + late_drop
    ):
        all_risk_ids.add(r["cow_id"])

    for r in rows:
        if r["cow_id"] in all_risk_ids and r.get("is_lactating"):
            ph = dim_phase(r["dim"])
            phase_counts[ph]["at_risk"] += 1

    phase_order = ["Переходный период", "Ранняя лактация", "Рост к пику", "Пик", "Плато", "Снижение"]
    phase_rows = []
    for ph in phase_order:
        data = phase_counts.get(ph, {"count": 0, "at_risk": 0})
        cnt = data["count"]
        risk = data["at_risk"]
        pct = round((risk / cnt) * 100, 0) if cnt > 0 else 0
        badge = "🔴" if pct > 25 else "🟡" if pct > 10 else "🟢"
        phase_rows.append(f"| {ph} | {cnt} | {risk} | {pct}% | {badge} |")

    # --- ХЕЛПЕРЫ ДЛЯ ТАБЛИЦ ---
    def row_fmt(r, note):
        return (
            f"| {r['cow_id']} | {r['dim']} | {r['parity']} | "
            f"{r.get('milk_yield_actual', '—')} | {r.get('milk_yield_expected', '—')} | "
            f"{r.get('deviation_pct', '—')}% | {note} |"
        )

    ketosis_rows = [row_fmt(r, "Взять BHB") for r in ketosis_candidates[:15]]
    hypocalcemia_rows = [row_fmt(r, "Контроль Ca, двигательная активность") for r in hypocalcemia_candidates[:10]]
    metritis_rows = [row_fmt(r, "Температура + выделения") for r in metritis_candidates[:15]]
    neb_rows = [row_fmt(r, "Мониторинг BHB, BCS, DMI") for r in neb_candidates[:10]]
    chronic_rows = [row_fmt(r, "Системный осмотр: кетоз, хромота, мастит") for r in chronic_metabolic[:10]]
    late_rows = [row_fmt(r, "Проверить питание поздней лактации") for r in late_drop[:10]]

    # --- ЭКОНОМИКА СКРИНИНГА ---
    total_at_risk = len(all_risk_ids)
    transition_at_risk = len(
        set(r["cow_id"] for r in ketosis_candidates + hypocalcemia_candidates + metritis_candidates)
    )

    # Оценка стоимости недообследованных коров
    # Предположим: 1 недиагностированный кетоз = ~28000₽ потерь
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
version: "1.0"
date_created: {now}
author: StanisSerg
---

# CS.WP.003: Скрининговый отчёт по метаболизму стада

> **Тип:** Рабочий продукт — Метаболизм (скрининг)
> **Источник данных:** Ежедневные удои (id, DIM, parity, milk_yield, pik_milk, pik_day)
> **Для роли:** Ветеринарный специалист / Зоотехник
> **Генерация:** Автоматическая через `rule_engine/generate_metabolism_report.py`

⚠️ **Важно:** Этот отчёт построен ТОЛЬКО на молочных данных. Он **не ставит диагноз**, а указывает коров с высоким риском, которых нужно взять на лабораторное/клиническое обследование (BHB, Ca, температура, выделения).

---

## 1. РЕКВИЗИТЫ ОТЧЁТА

| Поле | Данные |
|------|--------|
| **Номер отчёта** | CS.WP.003-{now}-001 |
| **Дата составления** | {now} |
| **Хозяйство** | {farm_name} |
| **Размер стада** | {total_cows} голов (дойных: {lactating_cows}) |
| **Источник данных** | CSV import (молочные данные) |

---

## 2. СВОДКА ПО РИСКАМ

### 2.1 Ключевые цифры

| Метрика | Значение | Примечание |
|---------|----------|------------|
| Всего коров в риске | {total_at_risk} | На основе отклонений удоя и DIM |
| Из них в переходном периоде | {transition_at_risk} | Наиболее критичная группа |
| Кандидаты на кетоз (SCK) | {len(ketosis_candidates)} | DIM 3-14, отклонение < -10% |
| Кандидаты на клинический кетоз | {len(clinical_ketosis_candidates)} | DIM 3-14, отклонение < -20% |
| Кандидаты на гипокальceмию | {len(hypocalcemia_candidates)} | DIM 1-3, отрицательное отклонение |
| Кандидаты на метритис/RP | {len(metritis_candidates)} | DIM 1-21, отклонение < -10%, parity ≥2 |
| Риск NEB (гиперпродуктивность) | {len(neb_candidates)} | DIM < 60, удой > +20% от нормы |
| Хроническое метаболическое подавление | {len(chronic_metabolic)} | DIM 30-100, отклонение < -20% |

### 2.2 Распределение рисков по фазам лактации

| Фаза лактации | Коров всего | В риске | % риска | Статус |
|---------------|-------------|---------|---------|--------|
{chr(10).join(phase_rows)}

---

## 3. СКРИНИНГ ПЕРЕХОДНОГО ПЕРИОДА (0-21 DIM)

> Переходный период — зона наивысшего метаболического риска. Здесь отклонение удоя является ранним маркером проблем.

### 3.1 Кандидаты на субклинический кетоз (SCK) — DIM 3-14, отклонение < -10%

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(ketosis_rows) if ketosis_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

### 3.2 Кандидаты на клинический кетоз — DIM 3-14, отклонение < -20%

> Эти коровы требуют немедленного ветеринарного осмотра.

{chr(10).join([f"- **{r['cow_id']}** (DIM {r['dim']}, {r.get('deviation_pct', '—')}%): взять BHB, проверить аппетит и рубцевую активность" for r in clinical_ketosis_candidates]) if clinical_ketosis_candidates else "Нет кандидатов на клинический кетоз."}

### 3.3 Кандидаты на гипокальceмию / молочную лихорадку — DIM 1-3

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(hypocalcemia_rows) if hypocalcemia_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

### 3.4 Кандидаты на метритис / задержку последа — DIM 1-21, parity ≥ 2

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(metritis_rows) if metritis_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

---

## 4. СКРИНИНГ РАННЕЙ И СРЕДНЕЙ ЛАКТАЦИИ

### 4.1 Риск негативного энергетического баланса (NEB) — DIM < 60, гиперпродуктивность

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(neb_rows) if neb_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

### 4.2 Хроническое метаболическое подавление — DIM 30-100, отклонение < -20%

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(chronic_rows) if chronic_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

---

## 5. ПОЗДНЯЯ ЛАКТАЦИЯ

### 5.1 Резкое падение удоя в поздней лактации — DIM > 200, отклонение < -15%

| ID коровы | DIM | Парность | Факт | Ожидаемый | Отклонение | Действие |
|-----------|-----|----------|------|-----------|------------|----------|
{chr(10).join(late_rows) if late_rows else "| — | — | — | — | — | — | Нет кандидатов |"}

---

## 6. ЭКОНОМИЧЕСКАЯ ОЦЕНКА РИСКА

### 6.1 Потенциальные потери от недиагностированных проблем

> Расчёт приблизительный. 1 клинический кетоз ~ 28 000 ₽, 1 запущенный метритис ~ 15 000 ₽.

| Риск | Кол-во кандидатов | Потенциальные потери |
|------|-------------------|----------------------|
| Клинический кетоз | {len(clinical_ketosis_candidates)} | {missed_ketosis_cost:,} ₽ |
| Метритис/RP | {len(metritis_candidates)} | {missed_metritis_cost:,} ₽ |
| **Итого потенциал экономии** | — | **{total_risk_cost:,} ₽** |

### 6.2 Стоимость скрининга

| Мера | Кол-во | Стоимость за единицу | Итого |
|------|--------|----------------------|-------|
| BHB-тест (кровь/молоко) | {len(ketosis_candidates)} | 200 ₽ | {len(ketosis_candidates) * 200:,} ₽ |
| Температура + визуальный осмотр | {len(metritis_candidates) + len(hypocalcemia_candidates)} | 50 ₽ | {(len(metritis_candidates) + len(hypocalcemia_candidates)) * 50:,} ₽ |
| **Итого затраты на скрининг** | — | — | **{len(ketosis_candidates) * 200 + (len(metritis_candidates) + len(hypocalcemia_candidates)) * 50:,} ₽** |

---

## 7. РЕКОМЕНДАЦИИ

### 7.1 Сегодня (0-24 часа)
- [ ] Взять **BHB** у всех коров из раздела 3.2 (клинический кетоз) и 3.1 (SCK)
- [ ] Измерить **температуру** и осмотреть выделения у коров из раздела 3.4
- [ ] Проверить на **подвёрнутость / слабость** коров из раздела 3.3 (гипокальceмия)

### 7.2 Эта неделя (1-7 дней)
- [ ] Настроить автоматический ежедневный скрининг: все коровы с DIM < 30 и отклонением < -10%
- [ ] Организовать взятие пропиленгликоля в аптечке для коров с BHB ≥ 1.2
- [ ] Провести тренинг персонала: как визуально определить кетоз и молочную лихорадку

### 7.3 Месяц (7-30 дней)
- [ ] Добавить в выгрузку минимум 2 поля: **BHB** и **температура** — для перехода от скрининга к диагностическим правилам RULE-002, RULE-005, RULE-006
- [ ] Связать данные молочного робота (удой) с ветеринарным журналом

---

## 8. ПРИЛОЖЕНИЯ

### 8.1 Исходные данные
- Файл: `herd_data.csv`
- Поля: `cow_id`, `dim`, `parity`, `milk_yield`, `pik_milk`, `pik_day`
- Дата выгрузки: {now}

### 8.2 Методология
- Ожидаемый удой рассчитан по упрощённой лактационной кривой (L0)
- Отклонение > 10% в переходном периоде считается сигналом к обследованию
- Пороги адаптированы под отсутствие лабораторных данных

### 8.3 История изменений

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | {now} | Первоначальная версия скринингового отчёта | generate_metabolism_report.py |

---

*Отчёт создан автоматически на основе:*
- *Прокси-скрининг метаболических рисков по молочным данным*
- *CS.ENTITY.031: Milk yield*
- *RULE-001/002/005/006/012*
"""
    return report


def main():
    parser = argparse.ArgumentParser(description="Generate CS.WP.003 metabolism screening report")
    parser.add_argument("csv", help="Path to herd data CSV")
    parser.add_argument("--out", "-o", default="CS.WP.003-metabolism-report.md", help="Output markdown file")
    parser.add_argument("--farm", "-f", default="FARM-001", help="Farm name")
    args = parser.parse_args()

    rows = load_herd_csv(args.csv)
    report = generate_report(rows, farm_name=args.farm)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✓ Metabolism screening report generated: {args.out}")
    print(f"  Cows analyzed: {len(rows)}")
    print(f"  At-risk cows identified: {len(set(r['cow_id'] for r in rows if r.get('is_lactating')))}")


if __name__ == "__main__":
    main()
