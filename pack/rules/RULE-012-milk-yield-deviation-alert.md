---
rule_id: RULE-012
dl_ref: DL-012
case_refs: []
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: productivity
tags: [milk-yield, lactation-curve, deviation, alert, productivity, dim, parity]

# RULE STATE
rule_version: "1.0"
rule_maturity: conceptual
status: conceptual
trend: stable

# Временные метки
last_trigger: null
last_error: null
last_review: 2026-04-15
next_review: 2026-07-15

# Управляемый актив
metrics_enabled: false
confidence: low

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

# RULE-012: Milk-Yield-Deviation-Alert

> **Тип:** executable decision operator — productivity monitoring  
> **Maturity:** conceptual (v1.0)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-012  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: productivity, фаза: lactation  
> **SoTA:** CS.SOTA.284 (dairy analytics), CS.ENTITY.031 (Milk yield)

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:
  - condition: "Lactating cow with known DIM and milk yield"
    note: "DIM and actual milk yield must be available"

  - condition: "Expected milk yield baseline available"
    note: "Either herd average for DIM/parity or genetic potential estimate"

soft_conditions:
  - condition: "Severe negative deviation"
    criteria: "Actual yield < 80% of expected for DIM and parity"
    weight: 2
    note: "Critical drop — requires immediate health/rule check"

  - condition: "Moderate negative deviation"
    criteria: "Actual yield 80-90% of expected"
    weight: 1
    note: "Warning zone — investigate within 48h"

  - condition: "Hyperproductive with metabolic risk"
    criteria: "Actual yield > 120% of expected in early lactation (DIM < 60)"
    weight: 1
    note: "High genetic potential realization may outpace DMI → NEB risk"

  - condition: "Persistence drop"
    criteria: "Decline from own peak > 0.25% per day after peak"
    weight: 1
    note: "Faster-than-expected lactation curve decline"

  - condition: "Peak timing abnormal"
    criteria: "Peak before week 3 or after week 10"
    weight: 1
    note: "Nutritional or health issue affecting curve shape"

blocking_conditions:
  - condition: "Dry cow or recently dried off"
    action: "USE_DRY_COW_PROTOCOL"
    
  - condition: "Sick leave / veterinary hold"
    action: "ALREADY_UNDER_TREATMENT"
    note: "Do not duplicate alerts while clinical protocol is active"
```

### Verdict Logic

```
INITIAL ──► lactating_with_data?
              │
              NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        veterinary_hold? ──► BLOCKED
              │
              NO
              │
              ▼
        calculate_deviation
              │
              ├── > +20% early lactation ──► HYPERPRODUCTIVE_RISK
              │
              ├── < -20% ──► CRITICAL_NEGATIVE_DEVIATION
              │
              ├── -20% to -10% ──► MODERATE_NEGATIVE_DEVIATION
              │
              ├── persistence_drop ──► PERSISTENCE_ALERT
              │
              └── within normal ──► WITHIN_EXPECTED_RANGE
```

**Verdict Types:**
- `RULE_012_BLOCKED`: Корова под ветеринарным наблюдением или сухостойная
- `RULE_012_NOT_APPLICABLE`: Недостаточно данных для оценки
- `RULE_012_CRITICAL_NEGATIVE`: Критическое снижение удоя (< -20%) — немедленная проверка здоровья
- `RULE_012_MODERATE_NEGATIVE`: Умеренное снижение (-10% до -20%) — проверка в течение 48h
- `RULE_012_PERSISTENCE_ALERT`: Слишком быстрое снижение после пика
- `RULE_012_HYPERPRODUCTIVE_RISK`: Удой сильно выше нормы в ранней лактации — риск NEB
- `RULE_012_WITHIN_RANGE`: Отклонения в пределах нормы

---

## STATE MACHINE

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| CRITICAL_NEGATIVE | CRITICAL | Health screening (RULE-001, RULE-006, RULE-011) | Same day |
| MODERATE_NEGATIVE | WARNING | Check ration, environment, health | 24-48 hours |
| PERSISTENCE_ALERT | WARNING | Review mid-lactation ration, body condition | 3-7 days |
| HYPERPRODUCTIVE_RISK | HIGH | Intensify metabolic monitoring, energy support | Ongoing |
| WITHIN_RANGE | INFO | Continue routine monitoring | Scheduled |

---

## ACTION PROTOCOL

### При RULE_012_CRITICAL_NEGATIVE

```yaml
priority: 1
actions:
  - immediate_health_check:
      - bhb: "If DIM < 30 or recent peak"
      - temperature: "Fever?"
      - udder_exam: "Mastitis signs?"
      - uterine_discharge: "Metritis?"
      - locomotion_score: "Lameness?"
  - nutrition_check:
      - dmi_actual_vs_expected: "Eating enough?"
      - tmr_consistency: "Sorting? Freshness?"
  - environment_check:
      - thi: "Heat stress?"
      - bunk_space: "Competition?"
      - water_access: "Clean and adequate?"
```

### При RULE_012_MODERATE_NEGATIVE

```yaml
priority: 2
actions:
  - schedule_review: "Within 48 hours"
  - check_feed_records: "Ration change? Mold?"
  - check_group_composition: "Overcrowding? Social stress?"
  - amr_data_review: "Step count, rumination, temperature trends"
```

### При RULE_012_HYPERPRODUCTIVE_RISK

```yaml
priority: 2
actions:
  - metabolic_monitoring:
      - bhb: "Weekly for DIM < 30"
      - bcs: "Ensure not dropping > 0.5 units"
  - energy_support:
      - increase_energy_density: "If DMI cannot increase further"
      - propylene_glycol: "Consider preventive if BHB borderline"
  - dry_matter_intake: "Track daily, maximize palatability"
```

---

## BECAUSE (Механизм)

### Лактационная кривая как системный индикатор

```
Ожидаемая кривая = f(DIM, parity, genetic_potential, season)
         │
         ▼
    Фактический удой
         │
    ┌────┴────┐
    │         │
Отклонение   Отклонение
вниз         вверх
    │         │
    ▼         ▼
Здоровье    Метаболизм
/ питание   перегружен
/ стресс    (NEB)
```

### Экономическая логика

```yaml
scenario_undetected_drop:
  cow_count: 10
  average_drop: 5 kg/day
  duration: 14 days
  price_per_kg: 40₽
  loss: "10 × 5 × 14 × 40 = 28000₽"
  plus_treatment_costs: "+15000₽"
  total: "43000₽"

scenario_rule_012_early_alert:
  detection: "Day 2 of drop"
  intervention: "Immediate ration + health check"
  recovery: "Drop limited to 2 kg × 3 days"
  saved_milk: "10 × (5×14 - 2×3) × 40 = 25600₽"
  intervention_cost: "5000₽"
  net_savings: "20600₽"
  roi: "+410%"
```

---

## LIMITS

```yaml
APPLICABLE:
  status: "Lactating cow"
  data: "DIM and at least one milk yield measurement"
  
NOT_APPLICABLE:
  dry_cows: true
  heifers_pre_calving: true
  first_week_postpartum_with_metabolic_crisis:
    note: "Yield naturally volatile; use clinical rules (RULE-001/RULE-005) instead"
```

---

## VALIDATION

```yaml
minimum_cases: 10
farms_required: 3
metrics:
  primary:
    - alert_accuracy: "% alerts leading to confirmed problem"
    - false_alert_rate: "% alerts with no identifiable cause"
    - economic_impact: "Milk saved per alerted cow vs non-alerted controls"
  secondary:
    - time_to_detection: "Days between yield drop and alert"
    - time_to_recovery: "Days from alert to yield normalization"
```

---

## Execution Framework

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - dim
    - parity
    - milk_yield_actual
    - milk_yield_expected
    - milk_yield_peak
    - peak_week
    - bcs
    - veterinary_hold
    
  prediction:
    deviation_pct: "float"
    risk_level: "CRITICAL / MODERATE / HYPER / NORMAL"
    recommended_checks: "list of rules to evaluate"
    
  outcome:
    cause_identified: "string"
    days_to_recovery: "int"
    milk_saved_vs_baseline: "float"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
```

---

## RELATIONSHIPS

### Integration with other rules

| Rule | Relationship |
|------|-------------|
| RULE-001 | CRITICAL_NEGATIVE often triggers ketosis check |
| RULE-005 | Early lactation drop may indicate hypocalcemia |
| RULE-006 | Postpartum drop may indicate metritis |
| RULE-008 | Heat stress is common cause of moderate drop |
| RULE-009 | Lameness reduces DMI → yield drop |
| RULE-011 | Mastitis directly suppresses milk yield |
| RULE-010 | Chronic unresolving drop → culling candidate |

---

*Framework: Execution Framework v4.0*
