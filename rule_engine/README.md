# Rule Engine v1.0

Исполняемая система правил для PACK-cattle-science.

> **v1.0 — 12 правил, 47 тестов, групповой движок, интеграция с предприятием.**
>
> Предыдущая версия описывала только RULE-002/003. Текущий README отражает полное состояние системы.

---

## Архитектура

```
rule_engine/
├── models.py                 # Dataclasses: Prediction, Decision, Evaluation
├── requirements.txt          # Зависимости
│
├── rules/                    # Исполняемые модули (12 правил)
│   ├── __init__.py
│   ├── rule_001.py           # Ketosis-Threshold-Invalidation
│   ├── rule_002.py           # SCK-BHB-Threshold
│   ├── rule_003.py           # Propylene-Glycol-Protocol
│   ├── rule_004.py           # Dry-Period-Nutrition
│   ├── rule_005.py           # Hypocalcemia-Milk-Fever
│   ├── rule_006.py           # Metritis-Retained-Placenta
│   ├── rule_007.py           # Displaced-Abomasum-Risk
│   ├── rule_008.py           # Heat-Stress-Intervention
│   ├── rule_009.py           # Lameness-Early-Detection
│   ├── rule_010.py           # Culling-Decision-Support
│   ├── rule_011.py           # Mastitis-Protocol
│   └── rule_012.py           # Milk-Yield-Deviation-Alert
│
├── run_case.py               # Индивидуальный кейс → правила → decision
├── evaluate_case.py          # Оценка: prediction vs fact
├── test_rules.py             # Тестовый набор (47 кейсов)
│
├── group_models.py           # Модели группового анализа
├── group_rules.py            # Групповые правила (rule_001g)
├── run_group_case.py         # Групповой кейс → стратегия
├── orchestrate.py            # CSV → группа → стратегия + boundary cases
│
├── enterprise_loader.py      # Загрузка Data.csv предприятия
├── herd_loader.py            # Загрузка merged herd CSV
├── generate_enterprise_reports.py  # CS.WP.002 + CS.WP.003
├── generate_productivity_report.py # Только продуктивность
├── generate_metabolism_report.py   # Только метаболизм
│
├── cases/                    # Кейсы
│   ├── CASE-001.yaml         # Пройденный метаболический кейс
│   ├── test_suite/           # 47 YAML-тестов (по 3–7 на каждое правило)
│   └── group_cases/          # Групповые кейсы переходного периода
│
└── templates/                # Шаблоны и отчёты
    ├── herd-data-template-L0.csv   # 10 полей (продуктивность)
    ├── herd-data-template-L1.csv   # 16 полей (+ метаболизм)
    ├── herd-data-template-L2.csv   # 23 поля (все 12 правил)
    ├── merged_herd_data.csv        # Демо-данные
    └── *.md                        # Сгенерированные отчёты
```

---

## Инвентарь правил

| ID | Название | Категория | Зрелость | Описание |
|----|----------|-----------|----------|----------|
| RULE-001 | Ketosis-Threshold-Invalidation | metabolic | pilot-active | Системное решение при метаболическом дефиците (BHB + DMI + BCS) |
| RULE-002 | SCK-BHB-Threshold | metabolic | conceptual | Скрининг субклинического кетоза (BHB ≥ 1.2, DIM 3–14) |
| RULE-003 | Propylene-Glycol-Protocol | metabolic | conceptual | Протокол пропиленгликоля при подтверждённом SCK |
| RULE-004 | Dry-Period-Nutrition | metabolic | conceptual | Оптимизация сухостойного периода (профилактика) |
| RULE-005 | Hypocalcemia-Milk-Fever | metabolic | conceptual | Гипокальceмия / молочная лихорадка (Ca < 1.5 → экстренная помощь) |
| RULE-006 | Metritis-Retained-Placenta | reproductive | conceptual | Метритис / задержка последа (температура + выделения) |
| RULE-007 | Displaced-Abomasum-Risk | metabolic | conceptual | Риск смещения сычуга (отказ от корма, тимпания) |
| RULE-008 | Heat-Stress-Intervention | management | conceptual | Тепловой стресс (ТГИ, вентиляция, рацион) |
| RULE-009 | Lameness-Early-Detection | health | conceptual | Ранняя диагностика хромоты (Locomotion Score ≥ 2) |
| RULE-010 | Culling-Decision-Support | economic | conceptual | Поддержка решения об отсеве (продуктивность + затраты + здоровье) |
| RULE-011 | Mastitis-Protocol | health | conceptual | Протокол мастита (SCC, CMT, культура, терапия) |
| RULE-012 | Milk-Yield-Deviation-Alert | production | conceptual | Алерт отклонения удоя (MilkBot-кривая, M305, персистентность) |

> **Зрелость:** `pilot-active` = протестирован на реальном кейсе; `conceptual` = реализовано, ждёт валидации на ферме.

---

## Установка

```bash
cd rule_engine
pip install -r requirements.txt
```

---

## Workflow 1: Индивидуальный кейс

### Шаг 1. Создать кейс

```yaml
# cases/CASE-002.yaml
case_id: CASE-002
date_created: '2026-04-20'
farm_id: FARM-001
cow_id: COW-99999
parity: 3
input:
  bhb: 1.4
  dim: 6
  dmi_actual: 9.5
  dmi_norm: 16.0
  bcs_at_calving: 3.5
  bcs_current: 3.0
  clinical_signs: []
  can_swallow: true
  anorexia_hours: 0
  severe_hepatic_lipidosis: false
```

### Шаг 2. Запустить rule engine

```bash
python run_case.py cases/CASE-002.yaml
```

**Вывод:**
```
✓ Updated case: cases/CASE-002.yaml
  Primary rule: RULE-001
  Action: DO_NOT_USE_AS_PRIMARY_INTERVENTION
  Verdicts: ['RULE_001_TRIGGERED', 'RULE_002_TRIGGERED', 'RULE_003_APPLICABLE']
  Prediction: {'bhb': 'down_with_systemic_correction', 'dmi': 'up'}
  Confidence: medium
```

### Шаг 3. Добавить фактические результаты

Отредактировать `cases/CASE-002.yaml`:

```yaml
fact:
  bhb_day_7: 0.7
  dmi_day_7: 15.2
```

### Шаг 4. Оценить результат

```bash
python evaluate_case.py cases/CASE-002.yaml
```

**Вывод:**
```
✓ Evaluation complete: cases/CASE-002.yaml
  Status: success
  Error type: None
  Root cause: None
  ✓ bhb_day_7: fact=0.7, range=[0.6, 0.9]
  ✓ dmi_day_7: fact=15.2, range=[14.0, 18.0]
```

---

## Workflow 2: Групповой кейс (стадо)

```bash
python orchestrate.py \
    --csv templates/merged_herd_data.csv \
    --farm Demo-Farm-12 \
    --group-type transition_period \
    --dim-range 0-21 \
    --out-dir cases/group_cases/
```

**Что делает:**
1. Загружает CSV (merged или enterprise формат)
2. Фильтрует коров по `dim_range`
3. Считает групповые метрики (milk, metabolic, reproduction)
4. Определяет boundary sub-cases (крайние коровы)
5. Создаёт GROUP CASE YAML
6. Запускает `run_group_case.py`
7. Выводит strategy и execution summary

---

## Workflow 3: Интеграция с предприятием

```bash
# Генерация отчётов из выгрузки предприятия
python generate_enterprise_reports.py /path/to/Data.csv --farm "ОАО МТК"
```

**Выход:**
- `CS.WP.002-{date}-{farm}-productivity-report.md` — продуктивность по группам/DIM
- `CS.WP.003-{date}-{farm}-metabolism-report.md` — скрининг метаболизма

**Пилот:** ОАО МТК, 206 голов, средний M305 = 7901 кг, 60 коров (31%) в метаболическом риске.

### Шаблоны данных

| Уровень | Поля | Активные правила |
|---------|------|------------------|
| **L0** | 10 (cow_id, dim, milk_yield, m305…) | RULE-010, RULE-012 |
| **L1** | 16 (+ BHB, Ca, температура, RP…) | + RULE-002, RULE-005, RULE-006 |
| **L2** | 23 (+ SCC, CMT, locomotion_score, BCS…) | + RULE-001, RULE-009, RULE-011 |

Подробнее: [`templates/README.md`](templates/README.md)

---

## Тестовый набор

```bash
python test_rules.py
```

**Результат:** `47 passed, 0 failed`

| Правило | Тестов | Покрытие вердиктов |
|---------|--------|-------------------|
| RULE-001 | 3 | blocked, triggered, not-triggered |
| RULE-002 | 3 | gray, triggered, blocked |
| RULE-003 | 3 | applicable, blocked, not-applicable |
| RULE-004 | 3 | blocked, high, medium |
| RULE-005 | 5 | blocked, emergency, oral, dcad-high, dcad-medium |
| RULE-006 | 4 | blocked, high, medium, low |
| RULE-007 | 3 | blocked, high, medium |
| RULE-008 | 3 | high, low, not-applicable |
| RULE-009 | 3 | blocked, high, medium |
| RULE-010 | 4 | blocked, high, medium, not-triggered |
| RULE-011 | 7 | blind, blocked, chronic, emergency, targeted, monitor, not-app |
| RULE-012 | 6 | critical, moderate, hyper, persistence, normal, blocked |

---

## Принципы

1. **Прозрачность** — каждое решение объяснено (reasoning, basis)
2. **Детерминированность** — одинаковый input → одинаковый output
3. **Объяснимость** — можно проследить логику от input до decision
4. **Повторяемость** — кейс живёт во времени, дополняется fact

---

## Структура кейса

```yaml
case_id: CASE-XXX
input:          # Исходные данные
  bhb: 1.4
  dim: 6
  ...

derived:        # Рассчитывается автоматически
  dmi_ratio: 0.594
  bcs_loss: 0.5

decision:       # Заполняется run_case.py
  triggered_rules: [RULE-002, RULE-003]
  primary_rule: RULE-003
  action: PG_300ML_X_5_DAYS_2X_DAILY
  reasoning: [...]
  basis: {...}

prediction:     # Заполняется run_case.py
  direction: {bhb: down, dmi: up}
  range: {bhb_day7: [0.6, 0.9], dmi_day7: [14.0, 18.0]}
  confidence: medium

fact:           # Заполняется вручную через 7 дней
  bhb_day7: 0.7
  dmi_day7: 15.2

result:         # Заполняется evaluate_case.py
  status: success
  delta: {...}
```

---

## Приоритизация правил (v1)

Priority (high to low):

| Score | Verdict | Ситуация |
|-------|---------|----------|
| 135 | RULE_011_BLOCKED | Мастит: клиническая авария |
| 133 | RULE_011_EMERGENCY | Мастит: системная терапия |
| 130 | RULE_012_CRITICAL_NEGATIVE | Удой: критическое падение |
| 128 | RULE_012_HYPERPRODUCTIVE_RISK | Удой: гиперпродуктивность → метаболический риск |
| 125 | RULE_009_BLOCKED | Хромота: хирургическая |
| 115 | RULE_005_EMERGENCY_IV_CALCIUM | Гипокальceмия: IV кальций немедленно |
| 110 | RULE_005_ORAL_CALCIUM_PROTOCOL | Гипокальceмия: оральный протокол |
| 108 | RULE_006_BLOCKED | Метритис: критическое состояние |
| 105 | RULE_003_BLOCKED | SCK: клинические признаки → экстренная помощь |
| 100 | RULE_003_NOT_APPLICABLE | SCK: тяжёлая форма → RULE-001 решает |
| 95 | RULE_001_BLOCKED | Метаболизм: тяжёлый дефицит → комбинированная терапия |
| 93 | RULE_002_BLOCKED | SCK: клинические признаки → обход скрининга |
| 92 | RULE_004_BLOCKED | Сухостой: противопоказания |
| 91 | RULE_005_BLOCKED | Гипокальceмия: противопоказания |
| 90 | RULE_007_BLOCKED | Сычуг: хирургическое вмешательство |
| 88 | RULE_006_TRIGGERED_HIGH | Метритис: высокий риск |
| 85 | RULE_001_TRIGGERED | Метаболизм: системная коррекция |
| 84 | RULE_003_APPLICABLE | SCK: пропиленгликоль применим |
| 82 | RULE_002_TRIGGERED | SCK: подтверждён |
| 80 | RULE_004_RECOMMENDED_HIGH | Сухостой: высокий приоритет профилактики |
| 79 | RULE_005_DCAD_RECOMMENDED_HIGH | Гипокальceмия: высокий DCAD |
| 78 | RULE_007_HIGH_RISK | Сычуг: высокий риск |
| 77 | RULE_006_TRIGGERED_MEDIUM | Метритис: средний риск |
| 76 | RULE_009_HIGH_RISK | Хромота: высокий риск |
| 75 | RULE_004_RECOMMENDED_MEDIUM | Сухостой: средний приоритет |
| 74 | RULE_005_DCAD_RECOMMENDED_MEDIUM | Гипокальceмия: средний DCAD |
| 73 | RULE_007_MEDIUM_RISK | Сычуг: средний риск |
| 72 | RULE_009_MEDIUM_RISK | Хромота: средний риск |
| 70 | RULE_002_GRAY_ZONE | SCK: серая зона (1.0–1.2) |
| 69 | RULE_006_TRIGGERED_LOW | Метритис: низкий риск |
| 68 | RULE_004_RECOMMENDED_LOW | Сухостой: низкий приоритет |
| 67 | RULE_005_DCAD_RECOMMENDED_LOW | Гипокальceмия: низкий DCAD |
| 66 | RULE_007_LOW_RISK | Сычуг: низкий риск |
| 65 | RULE_005_PROPHYLACTIC_CALCIUM | Гипокальceмия: профилактика |
| 64 | RULE_009_LOW_RISK | Хромота: низкий риск |
| 10 | NOT_TRIGGERED | Нет действия |

---

## Дорожная карта

### v1.0 ✅ (апрель 2026)
- [x] 12 правил с исполняемым ядром
- [x] 47 тестов, все проходят
- [x] Индивидуальный кейс: input → decision → prediction → evaluation
- [x] Групповой движок v1: CSV → групповая стратегия + boundary cases
- [x] Интеграция с данными предприятия (ОАО МТК, 206 голов)
- [x] MilkBot-кривая для прогноза M305
- [x] Генерация отчётов CS.WP.002 / CS.WP.003
- [x] G.2 SoTA Synthesis Pack (CG-Frame для Decision Layer)

### v1.1 (май 2026)
- [ ] Валидация RULE-005 … RULE-012 на реальных фермерских кейсах
- [ ] Новые кейсы: CASE-002 (гипокальceмия), CASE-003 (мастит), CASE-004 (сычуг)
- [ ] Обратная связь от ферм: prediction vs fact для групповых кейсов
- [ ] Расширенная выгрузка предприятия (коровы с DIM < 35)

### v1.2 (июнь 2026)
- [ ] Автоматизация переходов между правилами (state machine)
- [ ] Улучшение точности группового прогноза (ML на исторических данных)
- [ ] Интеграция с PLF-датчиками (активность, жвачка, температура)

### v2.0 (Q3 2026)
- [ ] Межзоновая интеграция: metabolic ↔ reproductive ↔ infectious
- [ ] Портфельная оптимизация: ROI всех правил в совокупности
- [ ] Продакшен-режим: real-time scoring для всего стада

---

## Связанные документы

- [`pack/rules/REGISTRY.md`](../pack/rules/REGISTRY.md) — полный реестр правил с диаграммами состояний
- [`pack/rules/RULE-*.md`](../pack/rules/) — спецификации каждого правила
- [`templates/README.md`](templates/README.md) — шаблоны CSV и руководство по уровням L0/L1/L2
- [`docs/G2-SoTA-Synthesis-Pack.md`](../docs/G2-SoTA-Synthesis-Pack.md) — научная база Decision Layer (4 Tradition)

---

*Обновлено: 2026-04-20 (WP-93)*
