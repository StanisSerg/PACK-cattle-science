---
rule_id: RULE-004
dl_ref: DL-004
case_refs: []  # Требуется валидация
date_created: 2026-04-11
date_updated: 2026-04-11
author: StanisSerg
category: metabolic
tags: [dry-period, transition-cow, nutrition, prevention, ketosis, bcs, energy-balance]

# RULE STATE
rule_version: "4.0"
rule_maturity: conceptual  # Based on Litherland 2025, requires validation
status: conceptual
trend: stable

# Временные метки
last_trigger: null
last_error: null
last_review: 2026-04-11
next_review: 2026-07-11

# Управляемый актив
metrics_enabled: false
confidence: low  # SoTA-based

# Критерии confidence upgrade
confidence_upgrade:
  trigger:
    farms: ">=3"
    cases: ">=10"
    precision: ">80%"
    recall: ">85%"
    economic_precision: ">70%"
    no_p1_unresolved: true
    conflicts: "none critical unresolved"
  process: automatic

# Критерии production
production_criteria:
  farms: ">=3 независимых"
  cases: ">=10 подтверждённых"
  fp_fn_documented: true
  error_bounds_defined: true
  seasonal_stability: true
  management_variation_stable: true
  no_p1_errors: true
---

# RULE-004: Dry-Period-Nutrition-Optimization

> **Тип:** executable decision operator — prevention protocol  
> **Maturity:** conceptual (v4.0) — основано на Litherland 2025  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** [DL-004](../../DS-cattle-operations/decisions/DL-004.md)  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: metabolic, фаза: prepartum  
> **SoTA:** CS.SOTA.XXX (Litherland 2025), CS.SOTA.YYY (Drackley)

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:  # ALL must be TRUE
  - condition: "Dry period active"
    dim_range: "-60 to -1 days"
    
  - condition: "BCS assessment available"
    criteria: "BCS at dry-off and current"
    
soft_conditions:  # 0-2 for confidence level
  - condition: "Over-conditioned at dry-off"
    criteria: "BCS >3.5"
    weight: 1
    note: "Higher risk of postpartum issues"
    
  - condition: "BCS gain during dry period"
    criteria: "ΔBCS >0"
    weight: 1
    note: "Overfeeding energy"
    
  - condition: "Previous lactation issues"
    criteria: "Previous SCK or displaced abomasum"
    weight: 1
    note: "Higher genetic/metabolic risk"

blocking_conditions:  # IF TRUE → RULE_BLOCKED
  - condition: "Clinical illness during dry period"
    examples: [mastitis, severe metritis, lameness]
    action: "TREAT_ILLNESS_FIRST"
    
  - condition: "Extremely emaciated"
    criteria: "BCS <2.5"
    action: "REFER_TO_NUTRITION_SPECIALIST"
```

### Verdict Logic

```
INITIAL ──► clinical_illness? ──► BLOCKED
              │
              NO
              │
              ▼
        in_dry_period? ──► NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        evaluate_risk ──► RECOMMENDED_ADJUSTMENTS
              │
              ▼
        ACTION: Optimize ration
```

**Verdict Types:**
- `RULE_004_BLOCKED`: Клиническое заболевание — сначала лечение
- `RULE_004_NOT_APPLICABLE`: Не в сухостойном периоде
- `RULE_004_RECOMMENDED_HIGH`: Высокий риск (2-3 soft factors)
- `RULE_004_RECOMMENDED_MEDIUM`: Умеренный риск (1 soft factor)
- `RULE_004_RECOMMENDED_LOW`: Стандартная оптимизация (0 soft)

---

## STATE MACHINE

```
                    ┌─────────────────────────────────────┐
                    │         INITIAL (начало)            │
                    └─────────────────┬───────────────────┘
                                      │
                    clinical_illness? │
                    ┌──────────────┐  │  ┌──────────────┐
           YES ────►│   BLOCKED    │  │  │   EVALUATE   │◄──── NO
                    │              │  │  │   dry period │
                    │ Лечение      │  │  │   status     │
                    │ болезни      │  │  │              │
                    └──────────────┘  │  └──────┬───────┘
                                       │         │
                                       │    in_dry?
                                       │    ┌──────────┐
                                       │NO  │ NOT_APP  │
                                       │    │ LICABLE  │
                                       │    └──────────┘
                                       │
                         ┌─────────────┼─────────────┐
                         │             │             │
                    soft=2-3│        soft=1│        soft=0│
                         │             │             │
                         ▼             ▼             ▼
                    ┌─────────┐  ┌─────────┐  ┌─────────┐
                    │ RECOMM  │  │ RECOMM  │  │ RECOMM  │
                    │  HIGH   │  │  MEDIUM │  │   LOW   │
                    └────┬────┘  └────┬────┘  └────┬────┘
                         │             │             │
                         └─────────────┴─────────────┘
                                       │
                                       ▼
                         ┌─────────────────────────────┐
                         │   RATION OPTIMIZATION       │
                         │   (specific to risk level)  │
                         └─────────────────────────────┘
```

### State Definitions

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | WARNING | Лечение заболевания | До выздоровления |
| NOT_APPLICABLE | INFO | Не применимо | — |
| RECOMMENDED (LOW) | INFO | Стандартная оптимизация | 1-2 недели |
| RECOMMENDED (MEDIUM) | WARNING | Активная коррекция | 3-7 дней |
| RECOMMENDED (HIGH) | HIGH | Интенсивное вмешательство | Немедленно |

---

## ACTION PROTOCOL

### При RULE_004_RECOMMENDED

**Step 1: Оценка риска (Risk Assessment)**
```yaml
action: ASSESS_TRANSITION_RISK
substeps:
  - measure: "Current BCS"
  - compare: "BCS at dry-off vs current"
  - review: "Previous lactation metabolic issues"
  - assess: "Ration energy density vs requirements"
  
risk_factors:
  - bcs_at_dry_off: ">3.5 = high risk"
  - bcs_gain_dry_period: ">0 = high risk"
  - previous_sck: "Yes = high risk"
  - ration_energy: ">110% NRC = high risk"
```

**Step 2: Коррекция рациона (Ration Adjustment)**
```yaml
priority: 1

standard_optimization_low_risk:
  target_energy: "100-105% NRC"
  fiber: "NDF >45% (lower energy density)"
  protein: "MP 1100-1200 g/day"
  minerals: "Ca, P, Mg, DCAD per NRC"
  
active_correction_medium_risk:
  target_energy: "95-100% NRC"
  fiber: "NDF >48%"
  limit: "Concentrate <2 kg/day"
  body_condition: "Maintain or slight loss (-0.1 to 0 BCS)"
  
intensive_intervention_high_risk:
  target_energy: "90-95% NRC"
  fiber: "NDF >50%, straw if needed"
  restrict: "Concentrate <1 kg/day or eliminate"
  body_condition: "Controlled loss (-0.25 to -0.5 BCS acceptable)"
  monitoring: "BCS every 2 weeks"
```

**Step 3: Управление группами (Group Management)**
```yaml
priority: 2

separation_strategy:
  - group_by_bcs: "Separate over-conditioned (BCS>3.5)"
  - group_by_due_date: "Calving within 3 weeks together"
  - avoid: "Mixing far-off and close-up dry cows"
  
close_up_period:
  timeframe: "-21 to 0 days"
  special_management:
    - anionic_salts: "If DCAD positive"
    - increased_Mg: "0.4% DM"
    - gradual_increase: "Energy 105-110% NRC in last 2 weeks"
```

**Step 4: Мониторинг (Monitoring)**
```yaml
priority: 3

metrics:
  every_2_weeks:
    - bcs: "Score 1-5, same scorer"
    - body_weight: "If scales available"
    
  weekly_close_up:
    - urine_pH: "Target 6.0-6.5 (if anionic)"
    - feed_intake: "DMI tracking"
    
  at_calving:
    - bcs: "Final score"
    - condition: "Alert, mobile, eating"
    
  postpartum:
    - bhb: "Day 3-7 (screening)"
    - dmi: "Daily tracking"
    
success_criteria:
  - bcs_at_calving: "3.0-3.5"
  - no_bcs_gain_dry: "ΔBCS ≤0"
  - smooth_transition: "No metabolic crisis"
  - bhb_postpartum: "<1.2 mmol/L (most cows)"
```

**Step 5: Оценка результата (Outcome Assessment)**
```yaml
priority: 4
timeline: "0-30 DIM (post-calving)"

success_metrics:
  - metabolic_disease_rate: "<5% clinical ketosis"
  - bhb_elevated_rate: "<15% BHB>1.2"
  - smooth_transition: ">90% cows eating well by day 3"
  
failure_indicators:
  - ketosis_rate: ">10%"
  - displaced_abomasum: ">2%"
  - poor_start: ">20% cows with DMI <80% at day 7"
  
root_cause_analysis:
  - if_failure: "Review dry period records"
  - check: "Ration formulation vs actual intake"
  - verify: "BCS trends during dry period"
```

---

## BECAUSE (Механизм)

### Научное обоснование

```
Патофизиология переходного периода:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Проблема: Over-conditioned cows (BCS >3.5)
• Жировая ткань: больше рецепторов к инсулину
• Результат: инсулинорезистентность
• Последствие: невозможность переключить липолиз

Механизм развития кетоза:
1. Высокий BCS ──► Большие жировые депо
2. Отёл ──► Энергетический дефицит
3. Липолиз ──► Высокие NEFA
4. Печень перегружена ──► Кетоз + жировая инфильтрация

Логика оптимизации сухостоя:
• Ограничить энергию в дальнем сухостое
  → Предотвратить набор жира
  → Улучшить чувствительность к инсулину
  
• Постепенное увеличение перед отёлом
  → Подготовить рубец к лактации
  → Адаптация метаболизма

Эффективность (Litherland 2025):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• BCS 3.25-3.5 at calving: оптимально
• BCS gain during dry: ассоциировано с +40% риска кетоза
• Controlled energy restriction: -30% кетоза

Drackley & Douglas 2022:
• One-group dry cow system: работает если правильно сбалансировано
• Two-group (far-off/close-up): лучше для неоднородных групп
• Ключ: не перекармливать в дальнем сухостое!
```

### Экономическая логика

```yaml
scenario_poor_management:
  description: "BCS >3.5, energy excess, no monitoring"
  outcomes:
    ketosis_rate: "15-20%"
    da_rate: "5-8%"
    culling_risk: "+30%"
  
  costs:
    ketosis_treatment: "3000 × 15% = 450 per cow"
    da_surgery: "15000 × 5% = 750 per cow"
    milk_loss: "5000 per case × 20% = 1000"
    reproduction_delay: "2000 per affected cow"
  expected_cost_per_cow: "4200"
  
scenario_rule_004_optimized:
  description: "BCS controlled 3.0-3.5, proper ration"
  outcomes:
    ketosis_rate: "5-8%"
    da_rate: "1-2%"
    culling_risk: "baseline"
  
  costs:
    ration_adjustment: "+200 per dry period"
    monitoring_labor: "300 per cow"
    total_investment: "500"
  
  savings:
    reduced_ketosis: "3000 × 10% = 300"
    reduced_da: "15000 × 4% = 600"
    reduced_milk_loss: "5000 × 10% = 500"
    total_saved: "1400"
    
  net_benefit: "1400 - 500 = 900"
  roi: "+180%"
  
comparison:
  per_cow_benefit: "900₽"
  herd_500_cows: "450,000₽ annually"
  payback_period: "Immediate (prevention cheaper than treatment)"
  
  economic_verdict: "HIGHLY_COST_EFFECTIVE"
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  phase: "Dry period (-60 to 0 days)"
  species: "Dairy cattle"
  breed: "Primarily Holstein (other breeds adapt)"
  bcs_measurable: "Reliable BCS scoring available"
  
NOT_APPLICABLE:
  lactating_cows:
    reason: "Different metabolism, different needs"
    action: "USE_LACTATION_PROTOCOLS"
    
  heifers_first_calf:
    note: "Still growing, higher energy needs"
    adjustment: "Use higher end of energy range"
    
  severe_health_issues:
    conditions: [chronic_mastitis, severe_lameness, cancer]
    action: "INDIVIDUALIZED_CARE_OR_CULL"
```

### Soft Limits (Требуют адаптации)

```yaml
JERSEY_COWS:
  description: "Smaller, higher BCS target acceptable"
  adjustment: "Target BCS 3.0-3.75 (vs 3.0-3.5 Holstein)"
  
HEAT_STRESS:
  description: "Climate affects intake"
  adjustment: "Increase NDF, add fat, night feeding"
  
ROBOTIC_MILKING:
  description: "Different behavior patterns"
  adjustment: "Adapt to robot feed tables"
  
PASTURE_BASED:
  description: "Grazing during dry period"
  adjustment: "Monitor BCS more frequently, supplement as needed"
  
SHORT_DRY_PERIOD:
  description: "<40 days dry"
  adjustment: "Focus only on close-up phase, intensify monitoring"
```

---

## VALIDATION

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| — | — | — | — | Нет собственной валидации | **LOW** |

**Note:** RULE-004 основано на сильной SoTA (Litherland 2025), но требует валидации:
- Реальные BCS тренды
- Фактический прием корма
- Результаты по кетозу

### Required Validation

```yaml
minimum_cases: 10
farms_required: 3
design: "Cohort study or controlled trial"

control_group: "Standard dry cow management"
intervention_group: "RULE-004 optimized protocol"

duration: "Complete dry period through 30 DIM"

metrics:
  primary:
    - ketosis_rate: "BHB>1.2 at 3-14 DIM"
    - bcs_at_calving: "Target 3.0-3.5"
  secondary:
    - da_rate: "Displaced abomasum"
    - milk_yield_30_dim: "+ vs control"
    - reproduction: "First service conception"
    
success_criteria:
  - ketosis_reduction: ">30% vs control"
  - bcs_optimization: ">80% cows 3.0-3.5 at calving"
  - roi_positive: ">100% return on investment"
```

---

## RULE METRICS

### Outcome Registration

```yaml
outcome_record:
  timestamp: "YYYY-MM-DD"
  farm_id: "FARM-XXX"
  cow_id: "COW-XXXXX"
  
  input_data:
    bcs_dry_off: 3.75
    bcs_at_calving: 3.25
    dry_period_length: 55
    ration_energy: "95% NRC"
    
  prediction:
    risk_level: "HIGH (BCS>3.5)"
    recommendation: "Intensive intervention"
    
  actual_outcome:
    protocol_followed: true
    bhb_7_dim: 0.8
    clinical_ketosis: false
    milk_day_30: 38
    
  classification: "TP (successful prevention)"
  root_cause: null
```

### Root Cause Categories (для ошибок)

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| **bcs_measurement_error** | **P1** | Неправильная оценка BCS | Разные скореры, нет калибровки |
| **ration_formulation** | **P1** | Рацион не соответствует плану | Факт ≠ расчёт |
| **intake_overestimated** | **P1** | Коровы едят меньше нормы | Конкуренция, качество корма |
| **group_mixing** | **P2** | Неправильное группирование | Far-off + close-up вместе |
| **timing_error** | **P2** | Неправильное время коррекции | Слишком поздно в сухостое |
| **acceptable_variability** | **P3** | Индивидуальная вариативность | 5-10% коров всегда рискуют |

### Action by Priority

```yaml
P1 (critical):
  threshold: "2+ BCS scoring or ration errors"
  timeline: "24–48 часов"
  action: "Train BCS scoring, verify ration mix"
  
P2 (planned):
  threshold: "3+ timing или grouping issues"
  timeline: "в ближайший scheduled review"
  action: "Revise dry cow management protocols"
  
P3 (no_action):
  threshold: "acceptable_variability"
  timeline: "не требует действия"
  action: "Continue monitoring"
```

### Review Schedule

| Trigger | Action | Тип |
|---------|--------|-----|
| 10 triggers + 5 outcomes | Включить метрики | scheduled |
| Ketosis rate >10% despite protocol | Emergency review | emergency |
| BCS measurement variance >0.5 | Retrain scorers | targeted |

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-04-11 | Создано на основе Litherland 2025 | StanisSerg |
| 4.0 | 2026-04-11 | Переписано под стандарт v4.0 | StanisSerg |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **BCS subjective** | Known variability | Medium | Inconsistent scoring | Training, same scorer |
| **Intake unpredictable** | Affected by many factors | High | Ration ≠ actual intake | Monitor refusals |
| **No local validation** | Literature only | Medium | May not work locally | Validate ASAP |
| **Requires discipline** | Long-term protocol | High | Compliance drops over time | Regular audits |
| **Individual variation** | Genetics | Medium | Some cows always at risk | Individual tracking |

### Acceptable Error Bounds

Target (post-validation):
- BCS at calving 3.0-3.5: > 80% cows
- Ketosis rate: < 8%
- BCS scoring variance: < 0.25 points

---

## Execution Framework

---

### Phase 1: Validation + Light Automation (CRITICAL)

**Принцип:** сразу фиксируем правильно → потом масштабируем

#### Light Automation

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - date_dry_off
    - bcs_dry_off
    - date_calving
    - bcs_at_calving
    - ration_energy_planned
    - ration_energy_actual
    
  prediction:
    risk_level: "LOW / MEDIUM / HIGH"
    recommendation: "Standard / Active / Intensive"
    
  outcome:
    bhb_7_dim: "value"
    clinical_ketosis: true/false
    milk_30_dim: "value"
    
  basis:
    rule: "RULE-004"
    soTA: "Litherland 2025"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
```

#### Validation Steps

1. Применить на 3+ фермах (полный цикл сухостой-отёл)
2. Создать 10+ кейсов (включая failures)
3. Document BCS trends, ration compliance, outcomes
4. Calculate ketosis rate vs control
5. Define error bounds

```yaml
precision_recall_tradeoff:
  not_applicable: "RULE-004 is prevention, not screening"
  key_metrics:
    - "Ketosis rate reduction"
    - "BCS optimization rate"
  target:
    ketosis_reduction: ">30% vs baseline"
    bcs_optimization: ">80% in target range"
```

---

### Phase 2: Robustness (HIGH)

```yaml
actions:
  - analyze_bcs_scoring_variance
  - verify_ration_compliance
  - validate_intake_estimates
  - test_variations:
      - one_group_vs_two_group
      - different_ndf_levels
  - validate_across_seasons

metrics_activation:
  conditions:
    - ≥10 triggers
    - ≥5 outcomes
```

---

### Phase 3: Full Automation (MEDIUM)

```yaml
components:
  - bcs_tracking_system
  - automatic_ration_adjustment
  - early_warning_alerts

readiness_criteria:
  - bcs_measurement_reliable: true
  - intake_prediction_accurate: true
```

---

### Phase 3.5: Rule Saturation (CRITICAL)

```yaml
saturation_criteria:
  rules_stable: ">=3–5"
  
dependencies:
  downstream:
    - RULE-002: "Detects postpartum SCK (should be reduced)"
    - RULE-001: "Intervenes if SCK occurs"
    
integration:
  - RULE-004 (prevention) ──► RULE-002 (detection) ──► RULE-003 (treatment)
```

---

### Phase 4: ML (LOW)

```yaml
potential_improvements:
  - predict_individual_risk: "By parity, history, genetics"
  - optimize_ration_personalization: "Individual vs group"
  - predict_feed_intake: "Weather, behavior, health"
```

---

### Critical Principle

```
Rule Saturation → понятная структура → ML усиливает
```

---

### System Loop

```
CASE → PREDICTION → DECISION → FACT → ERROR → RULE → UPDATE → NEXT CASE
```

---

### Maturity

```yaml
stage: conceptual
mode: structured validation active
execution: deterministic capture from day 1
metrics: enabled at ≥10 triggers
confidence: auto by criteria
status: применять, не переписывать
```

---

## RELATIONSHIPS

### В портфеле метаболических правил

```
┌─────────────────────────────────────────────┐
│           METABOLIC ZONE                    │
│                                             │
│  RULE-004 (prevention)                      │
│     Dry period optimization                 │
│              │                              │
│              ▼                              │
│  RULE-002 (detection)                       │
│     SCK screening (BHB≥1.2)                 │
│              │                              │
│              ▼                              │
│  RULE-001 (intervention)                    │
│     Systemic correction decision            │
│              │                              │
│              ▼                              │
│  RULE-003 (treatment)                       │
│     PG protocol execution                   │
│                                             │
└─────────────────────────────────────────────┘

Flow: Prevention → Detection → Decision → Treatment
```

### Conflicts

| Conflict | Resolution |
|----------|------------|
| RULE-004 recommends restriction, cow losing too much BCS | Individual adjustment, maintain minimum BCS |
| Close-up energy increase conflicts with obesity | Prioritize body condition over close-up increase |
| Farm cannot separate dry cow groups | Use one-group system with controlled average energy |

---

*Framework: Execution Framework v4.0*  
*Format: CASE → DL → RULE (executable, managed)*  
*System Loop: CASE→PREDICTION→DECISION→FACT→ERROR→RULE→UPDATE→NEXT CASE*
