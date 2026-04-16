---
rule_id: RULE-010
dl_ref: DL-010
case_refs: []
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: economic
tags: [culling, economics, replacement, metabolic, reproduction, roi]

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

# RULE-010: Culling-Decision-Support

> **Тип:** executable decision operator — economic threshold rule  
> **Maturity:** conceptual (v1.0)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** [DL-010](../../DS-cattle-operations/decisions/DL-010.md)  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: economic, фаза: any lactation

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:
  - condition: "Cow is lactating"
    note: "Culling decisions for dry cows use different logic"

  - condition: "At least one persistent problem"
    criteria: "ANY of: chronic metabolic issues, chronic reproduction failure, severe lameness, multiple mastitis cases"

soft_conditions:
  - condition: "Multiple concurrent issues"
    criteria: "2+ of: metabolic, reproductive, mastitis, lameness"
    weight: 1

  - condition: "High days open"
    criteria: "Days open > 150"
    weight: 1

  - condition: "Low production relative to herd"
    criteria: "Milk yield < 70% of herd average for DIM"
    weight: 1

  - condition: "High treatment cost accumulation"
    criteria: "> 15000₽ in last 90 days"
    weight: 1

  - condition: "Late lactation"
    criteria: "DIM > 250"
    weight: 1
    note: "Less time to recover investment"

  - condition: "Replacement heifer available"
    criteria: "Heifer ready to calve within 60 days"
    weight: 1

blocking_conditions:
  - condition: "Pregnant high-value cow"
    criteria: "Confirmed pregnant + expected 305d yield > 9000L"
    action: "DO_NOT_CULL_UNLESS_EMERGENCY"
    note: "Genetic and gestation investment too high"
    
  - condition: "Recent purchase or embryo transfer"
    criteria: "Acquired within 6 months OR ET donor/recipient"
    action: "REQUIRES_INDIVIDUAL_ECONOMIC_REVIEW"
```

### Verdict Logic

```
INITIAL ──► pregnant_high_value? ──► BLOCKED (do not cull)
              │
              NO
              │
              ▼
        recent_purchase_or_et? ──► BLOCKED (individual review)
              │
              NO
              │
              ▼
        persistent_problem? ──► NO ──► NOT_TRIGGERED
              │
              YES
              │
              ▼
        evaluate_soft_score ──► CULL_RECOMMENDED / MONITOR / DO_NOT_CULL
```

**Verdict Types:**
- `RULE_010_BLOCKED`: Не отсевать (ценная беременная / недавняя покупка / ET)
- `RULE_010_NOT_TRIGGERED`: Нет оснований для отсева
- `RULE_010_CULL_RECOMMENDED_HIGH`: Сильные основания (4+ soft) — отсев экономически оправдан
- `RULE_010_CULL_RECOMMENDED_MEDIUM`: Умеренные основания (2-3 soft) — рассмотреть отсев
- `RULE_010_CULL_RECOMMENDED_LOW`: Слабые основания (1 soft) — мониторить, отсев не срочен
- `RULE_010_MONITOR_CLOSELY`: Проблема есть, но пока рано для решения

---

## STATE MACHINE

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | INFO | Do not cull / Individual review | — |
| CULL_RECOMMENDED_HIGH | HIGH | Confirm pregnancy status, schedule culling, prepare replacement | 7-14 days |
| CULL_RECOMMENDED_MEDIUM | WARNING | Economic review, re-evaluate in 30 days | 30 days |
| CULL_RECOMMENDED_LOW | INFO | Monitor, treat if cost-effective | 60 days |
| MONITOR_CLOSELY | INFO | Track metrics, reassess at next check | Next routine exam |

---

## ACTION PROTOCOL

### При RULE_010_CULL_RECOMMENDED_HIGH

```yaml
priority: 1
actions:
  - confirm_pregnancy: "Verify via ultrasound or rectal"
  - calculate_breakeven: "Expected future milk vs treatment + feed costs"
  - check_market: "Current cull cow price vs replacement cost"
  - schedule: "Cull before next expected calving if not pregnant"
  - replacement: "Activate replacement heifer protocol"
  
documentation:
  - reason_for_culling: "Metabolic + reproductive + lameness"
  - economic_calculation: "Recorded for future rule refinement"
```

### При RULE_010_CULL_RECOMMENDED_MEDIUM

```yaml
priority: 2
actions:
  - set_review_date: "30 days"
  - attempt_last_treatment: "If one issue is treatable and cost < 3000₽"
  - reassess: "If no improvement → escalate to HIGH"
```

---

## BECAUSE (Механизм)

```
Постоянные проблемы накапливают затраты:
  • Лечение
  • Потери молока
  • Потери воспроизводства
  • Риск выбытия в неподходящий момент
  
Каждый день удержания "проблемной" коровы = альтернативная стоимость.
Замена на здоровую телку часто имеет положительный NPV уже через 1-2 лактации.
```

### Экономическая логика

```yaml
scenario_keep_chronic_cow:
  annual_treatment: "12000₽"
  milk_loss: "20000₽"
  reproduction_delay: "8000₽"
  feed_cost: "35000₽"
  total_annual_cost: "75000₽"
  expected_305d_yield: "5500L"
  
scenario_replace_with_heifer:
  heifer_cost: "80000₽"
  first_lactation_yield: "8000L"
  first_lactation_revenue: "280000₽"
  feed_cost: "45000₽"
  net_first_lactation: "155000₽"
  
comparison:
  chronic_cow_net: "~50000₽ (5500L × 35₽ - 75000₽)"
  heifer_net_year1: "155000₽"
  delta: "+105000₽"
  
  culling_verdict: "ECONOMICALLY_JUSTIFIED"
```

---

## LIMITS

```yaml
APPLICABLE:
  lactating_cows: true
  data_required:
    - production_records
    - reproduction_history
    - health_treatment_costs
    - replacement_heifer_pipeline

NOT_APPLICABLE:
  dry_cows:
    reason: "Different economics (investment already made in gestation)"
    action: "USE_DRY_COW_CULLING_PROTOCOL"
    
  known_genetic_elite:
    reason: "Breeding value may exceed current production losses"
    action: "INDIVIDUAL_GENETIC_ECONOMIC_REVIEW"
```

---

## VALIDATION

```yaml
minimum_cases: 10
farms_required: 3
metrics:
  primary:
    - actual_vs_predicted_roi: "Did replacement outperform kept cow?"
    - culling_accuracy: "% of recommended culls that were economically justified"
  secondary:
    - false_positives: "Recommended cull but cow recovered profitably"
    - false_negatives: "Not recommended but became chronic cost drain"
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
    - milk_yield_current
    - milk_yield_expected
    - days_open
    - pregnancy_status
    - treatment_cost_90d
    - metabolic_issues_count
    - reproductive_failures_count
    - mastitis_cases_90d
    - locomotion_score
    - heifer_available
    - genetic_value
    
  prediction:
    recommendation: "CULL / MONITOR / KEEP"
    confidence: "LOW / MEDIUM / HIGH"
    expected_replacement_roi: "float"
    
  outcome:
    actual_decision: "CULL / KEEP"
    replacement_performance: "L first lactation"
    actual_roi: "float"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
```

---

## RELATIONSHIPS

### Integration with other rules

```
┌─────────────────────────────────────────────────────────────────┐
│                    CULLING DECISION LAYER                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  INPUTS FROM OTHER RULES:                                       │
│  ├── RULE-001: Metabolic deficit chronic?                       │
│  ├── RULE-002: Repeated SCK episodes?                           │
│  ├── RULE-003: PG non-responsive?                               │
│  ├── RULE-006: Chronic metritis / no conception?                │
│  ├── RULE-007: Recurrent DA risk?                               │
│  ├── RULE-009: Chronic lameness (LS >= 3)?                      │
│  └── External: Mastitis records, production, reproduction       │
│                                                                 │
│  RULE-010 aggregates these into economic threshold              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

*Framework: Execution Framework v4.0*
