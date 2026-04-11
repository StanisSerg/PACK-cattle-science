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
rule_version: "3.0"
confidence_criteria:
  high: ">=3 independent confirmed cases, no critical conflicts"
  medium: "1-2 confirmed cases"
  low: "theoretical or single unconfirmed case"
---

# RULE-001: Ketosis-Threshold-Invalidation

> **Тип:** executable decision operator  
> **Уровень:** executable operator  
> **Готовность:** pilot-ready  
> **Production criteria:** 3+ farms, multi-context validation, stable false-positive control  
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

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-03-25 | Создано на основе DL-001 | StanisSerg |
| 2.0 | 2026-04-11 | Усилено до исполняемого оператора | StanisSerg |
| 3.0 | 2026-04-11 | Pilot-ready:<br>• Разделение hard/soft conditions<br>• Блокирующая ветка clinical_signs<br>• Reasoning array<br>• Economic verdict<br>• Псевдокод production-ready<br>• Убраны гиперболы, добавлена трезвость | StanisSerg |

---

## ROBUSTNESS ANALYSIS (Критически важно)

### Known Limitations (Известные ограничения)

| Тип | Описание | Вероятность | Влияние | Митигация |
|-----|----------|-------------|---------|-----------|
| False Positive | Правило сработало, но стандартная терапия сработала бы | Unknown | Потеря времени на системную коррекцию | Требуется валидация |
| False Negative | Правило не сработало (BHB 1.1), но дефицит прогрессировал | Unknown | Упущенное лечение | Дополнительное исследование порога |
| Edge Case | BHB 1.0-1.2 (ниже порога) | Medium | Недолечивание | Дополнительное исследование |
| Edge Case | BHB >2.5 (тяжёлый SCK) | Medium | Недостаточная агрессия терапии | Дополнительное исследование |
| Seasonality | Разное поведение летом/зимой | Unknown | Непредсказуемость | Сбор данных по сезонам |
| Breed | Jersey более чувствительны | Unknown | Пере/недолечивание | Отдельное исследование |

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
     - Проанализировать: почему?
  4. Обновить statistics
  5. При накоплении 5+ ошибок → review правила
```

---

## NEXT STEPS

### Phase 1: Validation (Приоритет: КРИТИЧЕСКИЙ)
1. Применить на 3+ фермах
2. Создать CASE-002, CASE-003, CASE-004
3. **Document all outcomes (success AND failure)**
4. **Calculate FP/FN rates**
5. **Define acceptable error bounds**
6. Rule confidence becomes HIGH automatically (не руками!) при ≥3 подтверждённых кейсах

### Для автоматизации:
1. Реализовать evaluate_rule_001() на Python
2. Интегрировать с системой мониторинга (BHB авто)
3. Создать dashboard для ветеринаров
4. Настроить алерты (SMS/app)

### Phase 2: Robustness (Приоритет: HIGH)
1. **Analyze error patterns** (5+ ошибок минимум)
2. Adjust hard/soft conditions based on data
3. Test edge cases (BHB 1.0-1.2, BHB >2.5)
4. **Validate seasonality effects**
5. **Validate breed differences** (Jersey vs Holstein)

### Phase 3: Automation (Приоритет: MEDIUM)
1. Реализовать evaluate_rule_001() на Python
2. Интегрировать с системой мониторинга (BHB авто)
3. Создать dashboard для ветеринаров
4. Настроить алерты (SMS/app)

### Phase 4: ML (Приоритет: LOW — только после Phase 2)
1. Собрать 50+ кейсов с outcomes
2. **Analyze errors before ML** (критически!)
3. Feature engineering на основе ошибок
4. Train classifier
5. Validate vs rule-based approach

**Критический принцип:** ML только после robustness. Иначе модель на слабой онтологии.

---

*Формат: CASE → DL → RULE (executable)*  
*Уровень: executable operator*  
*Готовность: pilot-ready*  
*Production criteria: 3+ farms, multi-context validation, stable false-positive control*
