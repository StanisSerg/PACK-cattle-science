---
rule_id: RULE-009
dl_ref: DL-009
case_refs: []
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: welfare
tags: [lameness, locomotion-score, hoof-health, bcs, bedding, milk-yield]

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

# RULE-009: Lameness-Early-Detection

> **Тип:** executable decision operator — welfare & production screening  
> **Maturity:** conceptual (v1.0)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-009  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: welfare, фаза: lactation

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:
  - condition: "Locomotion score available"
    note: "LS 1-5 scale or equivalent"

  - condition: "Lame or borderline"
    criteria: "LS >= 2"

soft_conditions:
  - condition: "Severely lame"
    criteria: "LS >= 3"
    weight: 1

  - condition: "Thin cow"
    criteria: "BCS < 2.75"
    weight: 1
    note: "Negative energy balance impairs hoof horn quality"

  - condition: "Poor bedding / standing surface"
    criteria: "Bedding score < 2 (wet, shallow) OR concrete without rubber"
    weight: 1

  - condition: "Milk yield drop"
    criteria: "Yield >5% below herd average for DIM"
    weight: 1

  - condition: "Overgrown hooves"
    criteria: "Hoof trimming overdue >60 days"
    weight: 1

blocking_conditions:
  - condition: "Non-ambulatory or severely injured"
    examples: [fracture, septic arthritis, deep digital sepsis]
    action: "REFER_TO_VETERINARY_EMERGENCY_PROTOCOL"
```

### Verdict Logic

```
INITIAL ──► non_ambulatory? ──► BLOCKED
              │
              NO
              │
              ▼
        locomotion_score >= 2? ──► NO ──► NOT_TRIGGERED
              │
              YES
              │
              ▼
        evaluate_soft_score ──► HIGH / MEDIUM / LOW RISK
```

**Verdict Types:**
- `RULE_009_BLOCKED`: Немобильная или тяжело травмированная — экстренный ветврач
- `RULE_009_NOT_TRIGGERED`: LS=1, хромоты нет
- `RULE_009_HIGH_RISK`: LS>=3 + 2+ дополнительных фактора
- `RULE_009_MEDIUM_RISK`: LS=2 + 1-2 фактора
- `RULE_009_LOW_RISK`: LS=2 без других факторов

---

## STATE MACHINE

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Emergency veterinary care | Immediate |
| HIGH_RISK | HIGH | Hoof trim + block + antibiotic if needed + environment fix | 24-48 hours |
| MEDIUM_RISK | WARNING | Scheduled hoof care + environment review | 3-7 days |
| LOW_RISK | INFO | Monitor + routine trim scheduling | 1-2 weeks |

---

## ACTION PROTOCOL

### При RULE_009_HIGH_RISK

```yaml
priority: 1
hoof_care:
  - trim: "Functional trim immediately"
  - block: "Apply hoof block to sound claw"
  - treat: "Topical antibiotic / wrap per lesion type"
  
environment:
  - bedding: "Increase depth, improve dryness"
  - walking_surfaces: "Add rubber where possible"
  - hoof_bath: "Check concentration and frequency"
  
metabolic:
  - nutrition: "Ensure adequate energy and trace minerals (Zn, Cu, biotin)"
  - body_condition: "Target BCS 3.0-3.25"

monitoring:
  - locomotion_recheck: "7 days"
  - milk_yield: "Daily until recovery"
  - lesion_healing: "Photo log if possible"
```

### При RULE_009_MEDIUM_RISK

```yaml
priority: 2
hoof_care:
  - schedule_trim: "Within 7 days"
  - inspect_lesions: "During next routine check"
  
environment:
  - review_bedding: "Spot-check problem areas"
  
monitoring:
  - locomotion_recheck: "14 days"
```

---

## BECAUSE (Механизм)

```
Плохие поверхности / влажность ──► мягкий рог + бактерии
         │
         ▼
    Пододерматит / белая линия / язвы
         │
         ▼
    Хромота ──► ↓DMI ──► ↓молоко ──► ↓BCS ──► ухудшение рога
         │                              │
         └────────── усиливается ◄──────┘

Раннее выявление критично:
  • LS 2 → лечение: ~500-1500₽, восстановление 1-2 недели
  • LS 3-4 → лечение: ~3000-8000₽, молочные потери, риск выбытия
```

### Экономическая логика

```yaml
scenario_late_detection_ls4:
  treatment: "5000₽"
  milk_loss: "8000₽ (3-4 weeks)"
  reproduction_delay: "3000₽"
  culling_risk: "+15%"
  total: "16000₽ + риск выбытия"

scenario_early_detection_ls2:
  trim_treatment: "1000₽"
  milk_loss: "minimal"
  total: "1000₽"
  
  savings: "15000₽"
  roi: "+1500%"
  
economic_verdict: "EXTREMELY_COST_EFFECTIVE"
```

---

## LIMITS

```yaml
APPLICABLE:
  species: "Dairy cattle"
  requirement: "Reliable locomotion scoring"

NOT_APPLICABLE:
  tie_stall_systems:
    note: "Different risk factors and assessment methods"
    action: "USE_TIE_STALL_LAMENESS_PROTOCOL"
    
  pasture_only_no_milking_parlor:
    note: "Difficult to score locomotion routinely"
```

---

## VALIDATION

```yaml
minimum_cases: 10
farms_required: 3
metrics:
  primary:
    - prevalence_change: "% lame cows before vs after intervention"
    - recovery_rate_ls2: "% returning to LS 1 within 14 days"
  secondary:
    - milk_yield_maintained: "vs herd mates"
    - culling_for_lameness: "%"
    - hoof_trimming_compliance: "% cows trimmed on schedule"
```

---

## Execution Framework

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - date
    - locomotion_score
    - bcs
    - bedding_score
    - surface_type
    - milk_yield_current
    - milk_yield_expected
    - days_since_last_trim
    - visible_lesions
    
  prediction:
    risk_level: "LOW / MEDIUM / HIGH"
    expected_recovery_days: "int"
    
  outcome:
    locomotion_score_14d: "int"
    recovered: true/false
    treatment_cost: "float"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
```

---

*Framework: Execution Framework v4.0*
