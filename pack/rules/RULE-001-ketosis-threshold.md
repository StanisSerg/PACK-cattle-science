---
rule_id: RULE-001
dl_ref: DL-001
case_refs: [CASE-001]
date_created: 2026-03-25
date_updated: 2026-04-11
author: StanisSerg
category: metabolic
tags: [ketosis, bhb, threshold, metabolic-deficit, liver-function, dmi, bcs]
status: active
confidence: medium  # 1 confirmed case
rule_version: "3.1"
rule_maturity: pilot-ready

# Управляемый актив (managed asset)
metrics_enabled: false  # Включить при: ≥10 triggers И ≥5 confirmed outcomes
last_reviewed: 2026-04-11
next_review: 2026-07-11

# Критерии confidence (не руками!)
confidence_upgrade:
  trigger:
    farms: ">=3"
    cases: ">=10"
    precision: ">80%"           # TP / (TP + FP)
    recall: ">85%"              # TP / (TP + FN)
    economic_precision: ">70%"  # Доля решений с положительным ROI
    conflicts: "none critical unresolved"
  process: automatic  # Не ручное решение

# Критерии production (формальные)
production_criteria:
  farms: ">=3 независимых"
  cases: ">=10 подтверждённых"
  fp_fn_documented: true
  error_bounds_defined: true
  seasonal_stability: true
  management_variation_stable: true
---

# RULE-001: Ketosis-Threshold-Invalidation

> **Тип:** executable decision operator  
> **Maturity:** pilot-ready (v3.1)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** [DL-001](../../DS-cattle-operations/decisions/DL-001-bhb-threshold.md)  
> **Валидация:** [CASE-001](../../DS-cattle-operations/cases/CASE-001-bhb-threshold.md)

---

## EXECUTIVE SUMMARY

**Функция:** Определяет, когда стандартная терапия (гепатопротекторы) **инвалидирована** и требуется системная коррекция.

**Ключевой инсайт:** При метаболическом дефиците гепатопротекторы = «присадки в пустой бак».

---

## EXECUTION LOGIC (Исполняемая логика)

### Псевдокод (production-ready)

```python
def evaluate_rule_001(data):
    """
    Исполняемый оператор принятия решения
    
    Args:
        data: {
            'bhb': float,           # mmol/L
            'dim': int,             # days in milk
            'dmi_actual': float,    # kg
            'dmi_norm': float,      # kg (NRC)
            'bcs_at_calving': float,
            'bcs_current': float,
            'clinical_signs': list  # ['acetone', 'ataxia', ...]
        }
    
    Returns:
        dict: {
            'verdict': str,
            'confidence': str,
            'action': str,
            'reasoning': list,
            'economic_verdict': str
        }
    """
    
    # ═══════════════════════════════════════════════════════
    # БЛОК 1: БЛОКИРУЮЩАЯ ВЕТКА (Blocking Branch)
    # ═══════════════════════════════════════════════════════
    
    if len(data['clinical_signs']) > 0:
        return {
            'verdict': 'RULE_001_BLOCKED',
            'confidence': 'N/A',
            'action': 'REFER_TO_CLINICAL_PROTOCOL',
            'required': 'CLINICAL_INTERVENTION',
            'alert': 'КРИТИЧЕСКИЙ: Клинические признаки присутствуют. RULE-001 не применять как основной сценарий. Перейти на клинический протокол.',
            'reasoning': ['clinical_signs_present: ' + ', '.join(data['clinical_signs'])],
            'economic_verdict': 'N/A',
            'hard_conditions_met': False,
            'soft_conditions_met': 0
        }
    
    # ═══════════════════════════════════════════════════════
    # БЛОК 2: HARD CONDITIONS (Якорные условия)
    # ═══════════════════════════════════════════════════════
    
    hard_bhb = data['bhb'] > 1.2
    hard_dim = data['dim'] < 30
    
    hard_met = hard_bhb and hard_dim
    
    if not hard_met:
        reasons = []
        if not hard_bhb:
            reasons.append(f"BHB={data['bhb']} <= 1.2 (норма)")
        if not hard_dim:
            reasons.append(f"DIM={data['dim']} >= 30 (поздний постпартум)")
        
        return {
            'verdict': 'RULE_001_NOT_TRIGGERED',
            'confidence': 'LOW',
            'action': 'GATHER_MORE_DATA',
            'required': 'MONITORING',
            'alert': 'RULE-001 не активирован. Жёсткие условия не выполнены. Стандартный протокол.',
            'reasoning': reasons,
            'economic_verdict': 'N/A',
            'hard_conditions_met': False,
            'soft_conditions_met': 0
        }
    
    # ═══════════════════════════════════════════════════════
    # БЛОК 3: SOFT CONDITIONS (Условия усиления)
    # ═══════════════════════════════════════════════════════
    
    soft_dmi = (data['dmi_actual'] / data['dmi_norm']) < 0.8
    soft_bcs = (data['bcs_at_calving'] - data['bcs_current']) > 0.5
    
    soft_score = sum([soft_dmi, soft_bcs])
    
    # ═══════════════════════════════════════════════════════
    # БЛОК 4: ОПРЕДЕЛЕНИЕ CONFIDENCE
    # ═══════════════════════════════════════════════════════
    
    if soft_score == 2:
        confidence = 'HIGH'
        alert_level = 'КРИТИЧЕСКИЙ'
        urgency = 'НЕМЕДЛЕННО'
    elif soft_score == 1:
        confidence = 'MEDIUM'
        alert_level = 'ВНИМАНИЕ'
        urgency = 'В течение 24 часов'
    else:
        confidence = 'LOW'
        alert_level = 'ИНФО'
        urgency = 'Мониторинг'
    
    # ═══════════════════════════════════════════════════════
    # БЛОК 5: ФОРМИРОВАНИЕ REASONING
    # ═══════════════════════════════════════════════════════
    
    reasoning = [
        f"BHB={data['bhb']} > 1.2 (hard)",
        f"DIM={data['dim']} < 30 (hard)"
    ]
    
    if soft_dmi:
        dmi_pct = (data['dmi_actual'] / data['dmi_norm']) * 100
        reasoning.append(f"DMI={dmi_pct:.0f}% < 80% (soft)")
    
    if soft_bcs:
        bcs_loss = data['bcs_at_calving'] - data['bcs_current']
        reasoning.append(f"BCS_loss={bcs_loss:.1f} > 0.5 (soft)")
    
    # ═══════════════════════════════════════════════════════
    # БЛОК 6: ФИНАЛЬНЫЙ ВЕРДИКТ
    # ═══════════════════════════════════════════════════════
    
    return {
        'verdict': 'RULE_001_TRIGGERED',
        'confidence': confidence,
        'action': 'DO_NOT_USE_AS_PRIMARY_INTERVENTION',
        'target': 'HEPATOPROTECTORS',
        'required': 'SYSTEM_CORRECTION',
        'alert': f"{alert_level}: Метаболический дефицит подтверждён ({confidence}). НЕ назначать гепатопротекторы как основное. Системная коррекция {urgency}.",
        'reasoning': reasoning,
        'economic_verdict': 'LIKELY_INEFFICIENT_STANDARD_THERAPY',
        'hard_conditions_met': True,
        'soft_conditions_met': soft_score,
        'expected_roi_standard': '-100%',
        'expected_roi_systemic': '+164%'
    }
```

---

## CONDITION MATRIX (Матрица условий)

### Hard Conditions (Якорные)

| Условие | Оператор | Значение | Роль |
|---------|----------|----------|------|
| BHB | `>` | 1.2 mmol/L | **БЛОКИРУЮЩЕЕ** — без этого правило не триггерится |
| DIM | `<` | 30 дней | **БЛОКИРУЮЩЕЕ** — период риска |

**Логика:** Если hard не выполнены → правило не активируется (независимо от soft).

### Soft Conditions (Усиления)

| Условие | Оператор | Значение | Роль |
|---------|----------|----------|------|
| DMI | `<` | 80% от нормы | **УСИЛЕНИЕ** — подтверждает дефицит |
| BCS loss | `>` | 0.5 ед. | **УСИЛЕНИЕ** — подтверждает мобилизацию |

**Логика:**
- soft_score = 2 → **HIGH** (все признаки дефицита)
- soft_score = 1 → **MEDIUM** (частичная картина)
- soft_score = 0 → **LOW** (только hard, требует наблюдения)

### Blocking Conditions (Блокирующие)

| Условие | Результат |
|---------|-----------|
| clinical_signs > 0 | RULE_001_BLOCKED → клинический протокол |

**Важно:** Это **не часть confidence**, а отдельная ветка. Клинический случай не может получить MEDIUM confidence.

---

## DECISION TREE (Дерево решений)

```
START
  │
  ▼
┌─────────────────────┐
│ Есть clinical_signs? │
└─────────────────────┘
  │
  ├── ДА ──► RULE_001_BLOCKED
  │           action: REFER_TO_CLINICAL_PROTOCOL
  │
  └── НЕТ
        │
        ▼
  ┌─────────────────────┐
  │ Hard met?           │
  │ (BHB>1.2 AND DIM<30)│
  └─────────────────────┘
        │
        ├── НЕТ ──► RULE_001_NOT_TRIGGERED
        │            confidence: LOW
        │            action: GATHER_MORE_DATA
        │
        └── ДА
              │
              ▼
        ┌─────────────────┐
        │ Soft score?     │
        └─────────────────┘
              │
              ├── 2 ──► confidence: HIGH
              │          action: DO_NOT_USE_AS_PRIMARY
              │          urgency: НЕМЕДЛЕННО
              │
              ├── 1 ──► confidence: MEDIUM
              │          action: DO_NOT_USE_AS_PRIMARY
              │          urgency: 24 часа
              │
              └── 0 ──► confidence: LOW
                         action: DO_NOT_USE_AS_PRIMARY
                         urgency: Мониторинг
```

---

## VERDICT TYPES (Типы вердиктов)

### 1. RULE_001_BLOCKED
```yaml
trigger: clinical_signs present
action: REFER_TO_CLINICAL_PROTOCOL
confidence: N/A
reason: "Клинические признаки требуют немедленного вмешательства"
```

### 2. RULE_001_NOT_TRIGGERED
```yaml
trigger: hard conditions not met
action: GATHER_MORE_DATA
confidence: LOW
reason: "Недостаточно данных для активации"
```

### 3. RULE_001_TRIGGERED
```yaml
trigger: hard met + soft evaluated
action: DO_NOT_USE_AS_PRIMARY_INTERVENTION
target: HEPATOPROTECTORS
required: SYSTEM_CORRECTION
confidence: HIGH | MEDIUM | LOW
```

---

## SYSTEM STATE (Состояние системы)

```
╔════════════════════════════════════════════════════════════════╗
║  SYSTEM STATE: Metabolic Deficit (Confirmed)                   ║
╠════════════════════════════════════════════════════════════════╣
║  Hard indicators:                                              ║
║    • BHB elevation: [value] mmol/L (threshold: >1.2)          ║
║    • Early postpartum: [value] DIM (threshold: <30)           ║
║                                                                ║
║  Soft indicators:                                              ║
║    • DMI: [value]% of NRC norm (threshold: <80%)              ║
║    • BCS loss: [value] units (threshold: >0.5)                ║
║                                                                ║
║  System status: UNSTABLE                                       ║
║  Resource allocation:                                          ║
║    ├─ Basal metabolism: HIGH priority                         ║
║    ├─ Lactation: ACTIVE                                       ║
║    ├─ Deficit compensation: MOBILIZATION active               ║
║    └─ Detoxification: DEPRIORITIZED                           ║
╚════════════════════════════════════════════════════════════════╝
```

---

## ACTION PROTOCOL (Протокол действий)

### При VERDICT: RULE_001_TRIGGERED

**Step 1: Инвалидация (Invalidation)**
```yaml
action: DO_NOT_USE_AS_PRIMARY_INTERVENTION
target: 
  - Essentiale (hepatoprotector)
  - Liv-52 (hepatoprotector)
  - Heptral (hepatoprotector)
  - Symptomatic IV glucose (isolated)
reason: "No substrate available for these interventions"
```

**Step 2: Системная коррекция (Required)**
```yaml
priority: 1
actions:
  - Separate groups (if DO + dry mixed)
  - Reduce energy density of DO ration
  - Increase NDF to >40%
  - Feeding frequency: ≥3x daily, no gaps >2h
target_metric: DMI >90% of NRC norm
timeline: 0-3 days
```

**Step 3: Поддержка (Support)**
```yaml
priority: 2
condition: "If BHB >1.4 or no improvement in 3 days"
action: Propylene glycol 300ml/day × 5 days
note: "Supportive, not replacement for systemic correction"
reference: RULE-003
```

**Step 4: Мониторинг (Monitoring)**
```yaml
metrics:
  - BHB: repeat in 7 days
  - DMI: daily
  - General condition: 2x daily
timeline: 14 days
escalation: "If no improvement → check secondary causes (metritis, mastitis)"
```

---

## BECAUSE (Механизм)

### Биохимическая логика

```
При BHB >1.2 + DMI <80%:

┌─ ENERGY BALANCE ───────────────────────────────┐
│  Intake: LOW (DMI deficit)                     │
│  Demand: HIGH (basal + lactation)              │
│  Gap: CRITICAL (negative balance)              │
├─ SUBSTRATE REALLOCATION ───────────────────────┤
│  Glucose: Preferentially to mammary gland      │
│  Amino acids: Diverted to gluconeogenesis      │
│  NEFA: Mobilized from adipose tissue           │
├─ HEPATIC FUNCTION ─────────────────────────────┤
│  ATP production: Limited (substrate shortage)  │
│  Protein synthesis: Reduced                    │
│  Detoxification: Deprioritized                 │
├─ HEPATOPROTECTOR MECHANISM ────────────────────┤
│  Required: ATP, phospholipids, cofactors       │
│  Available: NONE (all diverted to survival)    │
│  Effect: NULL (no substrate to protect)        │
└────────────────────────────────────────────────┘
```

### Аналогия

```
СИТУАЦИЯ: Машина не заводится

ОШИБКА РЫНКА:
  "Нужны присадки в бензин" (гепатопротекторы)
  → Бак пустой → Присадки бесполезны

ПРАВИЛЬНОЕ РЕШЕНИЕ:
  "Нужно залить топливо" (системная коррекция)
  → Устранить дефицит → Система работает

ЛОГИКА: 
  Присадки работают ТОЛЬКО при наличии бензина.
  Без бензина — нужно заправиться, не улучшать присадки.
```

---

## ECONOMIC VERDICT (Экономический вердикт)

### Сценарий А: Стандартная терапия (инвалидирована)

```yaml
costs:
  hepatoprotectors: 3500
  vitamins: 800
  veterinary: 2000
total: 6300

outcome:
  effect: "Minimal (BHB: 1.6→1.4)"
  duration: "10 days suffering"
  risk_progression: HIGH

roi: -100%
economic_verdict: INEFFICIENT
```

### Сценарий Б: Системная коррекция (валидирована)

```yaml
costs:
  ration_adjustment: 1200
  monitoring: 800
  propylene_glycol: 1500
total: 3500

outcome:
  bhb: "1.6→0.4 (normalized)"
  dmi: "14.2→19.2 kg (+35%)"
  milk: "28→34 L (+6 L/day)"
  gain_14_days: "+84 L"

revenue:
  milk_gain: "84 L × 35₽ = 2940₽"
  savings_vs_standard: 2800₽
total_benefit: 5740₽

roi: +164%
economic_verdict: HIGHLY_EFFICIENT
```

### Сравнение

| Метрика | Стандарт | Системный | Дельта |
|---------|----------|-----------|--------|
| Затраты | 6,300₽ | 3,500₽ | -2,800₽ |
| Эффект | Плохой | Отличный | — |
| ROI | -100% | +164% | +264% |
| Риск | Прогрессия | Решение | — |

---

## LIMITS (Границы)

### Hard Limits (Жёсткие)

```yaml
APPLICABLE:
  breed: Holstein
  dim_range: [7, 30]
  bcs_at_calving: [3.0, 3.5]
  productivity: ">30L/day"
  
NOT_APPLICABLE:
  clinical_ketosis:
    signs: [acetone_breath, ataxia, hypersalivation]
    action: EMERGENCY_PROTOCOL
    
  severe_hepatic_lipidosis:
    ast: ">500 U/L"
    action: DIAGNOSTIC_WORKUP
    
  late_lactation:
    dim: ">60 days"
    mechanism: "Different pathophysiology"
    
  concurrent_infection:
    conditions: [mastitis, metritis, endometritis]
    action: COMBINED_THERAPY
```

### Soft Limits (Требуют адаптации)

```yaml
JERSEY:
  sensitivity: "Higher to energy deficit"
  adjustment: "Consider BHB threshold >1.0"
  
EXTREME_CLIMATE:
  temperature: [">30°C", "<-20°C"]
  adjustment: "Increase monitoring frequency"
  
ROBOTIC_MILKING:
  behavior_pattern: "Different feeding pattern"
  adjustment: "Adapt to robot system"
```

---

## VALIDATION (Валидация)

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| [CASE-001](../../DS-cattle-operations/cases/CASE-001-bhb-threshold.md) | ✅ Успех | 2026-03 | Пилот-01 | Confirmed | **MEDIUM** |

**Примечание:** Rule confidence = MEDIUM потому что 1 кейс. Case outcome = Confirmed потому что внутри кейса всё сработало.

### Metrics from CASE-001

```yaml
before:
  bhb: 1.6
  ast: 142
  dmi: 14.2
  milk: 28
  
after:
  bhb: 0.4
  ast: 89
  dmi: 19.2
  milk: 34
  
delta_percentage:
  bhb: -75%
  ast: -37%
  dmi: +35%
  milk: +21%
  
roi: +164%
```

### Confidence Escalation Criteria

Rule confidence becomes HIGH automatically when:
- [ ] ≥3 independent confirmed cases (different farms)
- [ ] No critical conflicts detected
- [ ] Prediction convergence within acceptable delta
- [ ] Documented in REGISTRY.md

NOT raised by hand.

---

## INTEGRATION (Интеграция)

### API Response Format

```json
{
  "rule_id": "RULE-001",
  "version": "3.0",
  "verdict": "RULE_001_TRIGGERED",
  "confidence": "HIGH",
  "action": "DO_NOT_USE_AS_PRIMARY_INTERVENTION",
  "target": "HEPATOPROTECTORS",
  "required": "SYSTEM_CORRECTION",
  "alert": "КРИТИЧЕСКИЙ: Метаболический дефицит подтверждён (HIGH). НЕ назначать гепатопротекторы как основное. Системная коррекция НЕМЕДЛЕННО.",
  "reasoning": [
    "BHB=1.6 > 1.2 (hard)",
    "DIM=18 < 30 (hard)",
    "DMI=79% < 80% (soft)",
    "BCS_loss=0.75 > 0.5 (soft)"
  ],
  "economic_verdict": "LIKELY_INEFFICIENT_STANDARD_THERAPY",
  "hard_conditions_met": true,
  "soft_conditions_met": 2,
  "expected_roi_standard": "-100%",
  "expected_roi_systemic": "+164%",
  "next_steps": [
    "Separate groups if mixed",
    "Reduce energy density",
    "Monitor BHB in 7 days"
  ]
}
```

### Dashboard Integration

| Поле | Отображение | Цвет |
|------|-------------|------|
| verdict | Бadge | Зелёный/Жёлтый/Красный |
| confidence | Progress bar | 0-100% |
| reasoning | Expandable list | Нейтральный |
| economic_verdict | Icon | 💰/⚠️/❌ |
| action | Button | Primary/Warning/Danger |

---

## STATE MACHINE (Состояния вердикта)

### Verdict States

```
                    ┌─────────────────────────────────────┐
                    │         INITIAL (начало)            │
                    └─────────────────┬───────────────────┘
                                      │
                    clinical_signs?   │
                    ┌──────────────┐  │  ┌──────────────┐
           ДА ─────►│   BLOCKED    │  │  │   EVALUATE   │◄──── НЕТ
                    │              │  │  │   hard/soft  │
                    │ Клинический  │  │  │              │
                    │ протокол     │  │  └──────┬───────┘
                    └──────────────┘  │         │
                                       │    hard_met?
                                       │    ┌──────────┐
                                       │НЕТ │ NOT_TRIG │
                                       │    │ GERED    │
                                       │    └──────────┘
                                       │
                         ┌─────────────┼─────────────┐
                         │             │             │
                    soft=2│        soft=1│        soft=0│
                         │             │             │
                         ▼             ▼             ▼
                    ┌─────────┐  ┌─────────┐  ┌─────────┐
                    │ TRIGGERED│  │ TRIGGERED│  │ TRIGGERED│
                    │  HIGH    │  │  MEDIUM  │  │   LOW    │
                    └────┬────┘  └────┬────┘  └────┬────┘
                         │             │             │
                         └─────────────┴─────────────┘
                                       │
                                       ▼
                         ┌─────────────────────────────┐
                         │   SYSTEM_CORRECTION         │
                         │   (обязательное действие)   │
                         └─────────────────────────────┘
```

### Переходы между состояниями

| From | To | Trigger | Action Required |
|------|----|---------|-----------------|
| INITIAL | BLOCKED | clinical_signs > 0 | Перейти на клинический протокол |
| INITIAL | NOT_TRIGGERED | hard = false | Мониторинг, сбор данных |
| INITIAL | TRIGGERED (LOW) | hard = true, soft = 0 | Системная коррекция + усиленный мониторинг |
| INITIAL | TRIGGERED (MEDIUM) | hard = true, soft = 1 | Системная коррекция в течение 24ч |
| INITIAL | TRIGGERED (HIGH) | hard = true, soft = 2 | Системная коррекция немедленно |

### Обязательные действия по состоянию

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Клинический протокол | Немедленно |
| NOT_TRIGGERED | INFO | Мониторинг | Обычный |
| TRIGGERED (LOW) | WARNING | Системная коррекция | 48 часов |
| TRIGGERED (MEDIUM) | HIGH | Системная коррекция | 24 часа |
| TRIGGERED (HIGH) | CRITICAL | Системная коррекция | Немедленно |

---

## RULE METRICS (Метрики правила)

> **Включить после 10+ triggers**
> `metrics_enabled: false` → `true` после 10 triggers

### Текущие метрики (пока не собираются)

| Метрика | Определение | Текущее значение | Целевое значение |
|---------|-------------|------------------|------------------|
| **total_triggers** | Сколько раз правило сработало | 1 | — |
| **confirmed_outcomes** | Подтверждённых outcomes (TP + FP + FN) | 1 | ≥5 для метрик |
| **true_positives** | Правило сработало + подтвердилось | 1 | — |
| **false_positives** | Правило сработало + не подтвердилось | 0 | <20% |
| **false_negatives** | Правило не сработало + был дефицит | Unknown | <15% |
| **precision** | TP / (TP + FP) | 100% (1/1) | >80% |
| **recall** | TP / (TP + FN) | Unknown | >85% |
| **f1_score** | 2 × (P × R) / (P + R) | Unknown | >82% |
| **economic_precision** | Доля решений с положительным ROI | Unknown | >70% |

### Регистрация outcomes

```yaml
# Структура записи для каждого trigger
outcome_record:
  timestamp: "YYYY-MM-DD HH:MM"
  farm_id: "FARM-001"
  cow_id: "COW-12345"
  input_data:
    bhb: 1.6
    dim: 18
    dmi_pct: 79
    bcs_loss: 0.75
  prediction:
    verdict: "TRIGGERED"
    confidence: "HIGH"
    action: "SYSTEM_CORRECTION"
  actual_outcome:
    bhb_after_7d: 0.4
    dmi_after_7d: 19.2
    therapy_applied: "systemic_correction"
    success: true  # BHB <1.2, DMI >90%
  classification:
    type: "TP"  # TP, FP, FN
    root_cause: null  # если FP/FN
```

### Root Cause Categories (для ошибок)

| Category | Description | Example |
|----------|-------------|---------|
| **data_quality** | Проблемы с данными | Неправильный замер BHB |
| **threshold_issue** | Порог неверен | BHB 1.1 — пропущен случай |
| **ontology_issue** | Неправильная онтология | Не учли породу |
| **missing_variable** | Не хватает переменной | Не учли инфекцию |
| **temporal_issue** | Проблема времени | Задержка между измерением и действием |
| **acceptable_noise** | Вариативность биологии | Нормальная биологическая вариация, не требует фикса |
| **unpredictable** | Случайность | Редкая комбинация факторов |

### Review Schedule

| Trigger | Action | Тип |
|---------|--------|-----|
| 10 triggers + 5 outcomes | Включить метрики, первый review | scheduled |
| 25 triggers | Анализ ошибок, возможная корректировка | scheduled |
| 50 triggers | Рассмотрение confidence upgrade | scheduled |
| Каждые 50 triggers | Регулярный review | scheduled |
| **5+ ошибок total** | **Экстренный review** | **emergency** |
| **2+ одинаковых root cause** | **Targeted fix** | **targeted** |

### Review Types

```yaml
scheduled:
  trigger: "Накопление данных"
  scope: "Общий анализ правила"
  outcome: "Плановое улучшение или статус-quo"

emergency:
  trigger: "5+ ошибок любого типа"
  scope: "Критический пересмотр всей логики"
  outcome: "Rollback, major revision или status-quo с ограничениями"

targeted:
  trigger: "2+ ошибки с одинаковым root cause"
  scope: "Фокус на конкретной оси: данные/порог/онтология/время"
  outcome: "Быстрый фикс по конкретной оси"
  examples:
    - "2 threshold_issue → пересмотр порога BHB"
    - "2 temporal_issue → добавление lag-переменной"
    - "2 missing_variable → расширение inputs"
```

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-03-25 | Создано на основе DL-001 | StanisSerg |
| 2.0 | 2026-04-11 | Усилено до исполняемого оператора | StanisSerg |
| 3.0 | 2026-04-11 | Pilot-ready:<br>• Разделение hard/soft conditions<br>• Блокирующая ветка clinical_signs<br>• Reasoning array<br>• Economic verdict<br>• Псевдокод production-ready<br>• Убраны гиперболы, добавлена трезвость | StanisSerg |
| 3.1 | 2026-04-11 | Managed asset:<br>• State machine для verdict states<br>• Rule metrics (таблица)<br>• Root cause categories<br>• Review schedule (3 типа: scheduled/emergency/targeted)<br>• Confidence upgrade criteria<br>• Убрано дублирование Automation | StanisSerg |
| 3.2 | 2026-04-11 | Evolution-ready:<br>• Review types: scheduled/emergency/targeted<br>• acceptable_noise класс (не чинить биологическую вариативность)<br>• Economic Precision метрика (ROI-based)<br>• Metrics activation: ≥10 triggers И ≥5 outcomes<br>• Temporal issue как future ML input<br>• Root cause priorities (P1/P2/P3) | StanisSerg |

---

## ROBUSTNESS ANALYSIS (Критически важно)

### Known Limitations (Известные ограничения)

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **False Positive** | Unknown (no data) | Medium | Потеря времени на системную коррекцию | Требуется валидация |
| **False Negative** | Unknown (no data) | High | Упущенное лечение | Дополнительное исследование порога |
| **Edge Case: BHB 1.0-1.2** | Some evidence (literature) | Medium | Недолечивание | Дополнительное исследование |
| **Edge Case: BHB >2.5** | Some evidence (literature) | Medium | Недостаточная агрессия | Дополнительное исследование |
| **Seasonality** | Unknown (no data) | Medium | Непредсказуемость | Сбор данных по сезонам |
| **Breed: Jersey** | Unknown (no data) | Medium | Пере/недолечивание | Отдельное исследование |

**Evidence Status:** Unknown / Some evidence / Well documented  
**Risk Level:** Low / Medium / High (по влиянию на outcome)

### Acceptable Error Bounds (Допустимые границы ошибок)

**Пока НЕ определены.**

Для production нужно зафиксировать:
- False Positive Rate: < X% (сколько ложных тревог допустимо)
- False Negative Rate: < Y% (сколько пропущенных случаев допустимо)
- Precision: > Z% (точность срабатываний)
- Recall: > W% (полнота охвата)

### Error Analysis Process (Процесс анализа ошибок)

```
При каждом кейсе:
  1. Зафиксировать prediction (правило что сказало)
  2. Зафиксировать outcome (что получилось)
  3. Сравнить:
     - Если prediction ≠ outcome → ERROR
     - Классифицировать: FP или FN
  4. Root Cause Analysis:
     - data_quality? (проблемы с данными)
     - threshold_issue? (порог неверен)
     - ontology_issue? (неправильная онтология)
     - missing_variable? (не хватает переменной)
     - temporal_issue? (проблема времени)
     - unpredictable? (случайность)
  5. Обновить statistics
  6. При накоплении 5+ ошибок → review правила
```

**Root Cause Categories:**
| Category | Check | Example |
|----------|-------|---------|
| **data_quality** | Данные корректны? | Неправильный замер BHB |
| **threshold_issue** | Порог адекватен? | BHB 1.1 — пропущен случай |
| **ontology_issue** | Модель верна? | Не учли породу |
| **missing_variable** | Все факторы учтены? | Не учли инфекцию |
| **temporal_issue** | Время корректно? | Задержка в измерениях |
| **unpredictable** | Это случайность? | Редкая комбинация факторов |

---

## NEXT STEPS

### Phase 1: Validation (Приоритет: КРИТИЧЕСКИЙ)
1. Применить на 3+ фермах
2. Создать CASE-002, CASE-003, CASE-004 (success AND failure)
3. **Document all outcomes в DS-cattle-operations**
4. **Calculate FP/FN rates**
5. **Define acceptable error bounds** (Precision >80%, Recall >85%)
6. Confidence upgrade сработает автоматически при достижении критериев

### Phase 2: Robustness (Приоритет: HIGH)
1. **Analyze error patterns** (5+ ошибок минимум) + root cause analysis
2. Test edge cases (BHB 1.0-1.2, BHB >2.5)
3. Validate seasonality effects
4. Validate breed differences (Jersey vs Holstein)
5. **Enable rule metrics** (после 10+ triggers)

### Phase 3: Automation (Приоритет: MEDIUM)
1. Реализовать evaluate_rule_001() на Python
2. Интегрировать с системой мониторинга (BHB авто)
3. Создать dashboard с metrics
4. Настроить алерты (SMS/app)

### Phase 4: ML (Приоритет: LOW — только после Phase 2)
1. Собрать 50+ кейсов с outcomes
2. **Analyze errors before ML** (критически!)
3. Feature engineering на основе ошибок
4. Train classifier
5. Validate vs rule-based approach

**Критический принцип:** ML только после robustness. Иначе модель на слабой онтологии.

---

*Формат: CASE → DL → RULE (executable, managed)*  
*Maturity: pilot-ready (v3.1)*  
*Metrics: to be enabled at 10+ triggers*  
*Confidence upgrade: automatic by criteria*
