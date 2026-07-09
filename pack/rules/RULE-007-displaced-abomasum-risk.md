---
rule_id: RULE-007
dl_ref: DL-007
case_refs: []
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: metabolic
tags: [displaced-abomasum, da, ketosis, dmi, ph, postpartum, surgery-risk]

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

# RULE-007: Displaced-Abomasum-Risk-Screening

> **Тип:** executable decision operator — early risk screening  
> **Maturity:** conceptual (v1.0)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-007  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: metabolic, фаза: early postpartum

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:
  - condition: "Early postpartum window"
    dim_range: "5 to 30 days"
    note: "Peak DA incidence window"

  - condition: "At least one primary DA risk factor"
    criteria: "ANY of: BHB >= 1.2, DMI ratio < 0.7, ruminal pH > 7.0 (left displacement)"

soft_conditions:
  - condition: "Concurrent ketosis"
    criteria: "BHB >= 1.4"
    weight: 1

  - condition: "Severe DMI depression"
    criteria: "DMI ratio < 0.6"
    weight: 1

  - condition: "High-producing cow"
    criteria: "Previous lactation yield > 40L OR peak yield > 42L"
    weight: 1

  - condition: "Previous DA"
    criteria: "Had DA in previous lactation"
    weight: 1

blocking_conditions:
  - condition: "Clinical DA already confirmed"
    examples: [pinging_left, abomasal_tympany, scissor_posture, complete_anorexia]
    action: "REFER_TO_SURGICAL_PROTOCOL_IMMEDIATELY"
```

### Verdict Logic

```
INITIAL ──► clinical_DA_confirmed? ──► BLOCKED (surgery)
              │
              NO
              │
              ▼
        in_window_5_30_dim? ──► NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        primary_risk_met? ──► NO ──► NOT_TRIGGERED
              │
              YES
              │
              ▼
        evaluate_soft_score ──► HIGH / MEDIUM / LOW RISK
```

**Verdict Types:**
- `RULE_007_BLOCKED`: Клиническое DA подтверждено — немедленно к хирургу
- `RULE_007_NOT_APPLICABLE`: Вне окна риска (рано или поздно)
- `RULE_007_HIGH_RISK`: Высокий риск (3-4 soft) — активное вмешательство
- `RULE_007_MEDIUM_RISK`: Умеренный риск (1-2 soft) — усиленный мониторинг + профилактика
- `RULE_007_LOW_RISK`: Низкий риск (0 soft) — стандартный мониторинг
- `RULE_007_NOT_TRIGGERED`: Нет признаков риска

---

## STATE MACHINE

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Surgical referral | Immediate |
| HIGH_RISK | HIGH | Active intervention + vet on standby | 12-24 hours |
| MEDIUM_RISK | WARNING | Enhanced monitoring + rumen support | 24-48 hours |
| LOW_RISK | INFO | Standard monitoring | Routine |

---

## ACTION PROTOCOL

### При RULE_007_HIGH_RISK

```yaml
priority: 1
actions:
  - rumen_support: "Oral rumen transfaunate or prokinetics per vet protocol"
  - diet_correction: "Increase effective fiber (NDF >35%), reduce concentrate"
  - feeding_frequency: "≥3x daily, avoid sorting"
  - hydration: "Ensure unlimited water access"
  - vet_standby: "Daily clinical exam, auscultation both sides"
monitoring:
  - dmi: "Every 12 hours"
  - rumen_contractions: "2x daily"
  - abomasal_sounds: "Auscultation + percussion"
```

### При RULE_007_MEDIUM_RISK

```yaml
priority: 2
actions:
  - rumen_support: "Consider oral prokinetics"
  - diet_check: "Verify fiber levels, TMR consistency"
  - group_check: "Avoid overstocking, ensure bunk space"
monitoring:
  - dmi: "Daily"
  - general_attitude: "2x daily"
  - recheck_auscultation: "Day 2 and day 4"
```

---

## BECAUSE (Механизм)

```
Кетоз / низкий DMI ──► ↓ рубцовая моторика ──► газ в рубце
         │                                    │
         ▼                                    ▼
    Атония преджелудков                  Потеря объёма абомазума
         │                                    │
         └────────────┬───────────────────────┘
                      ▼
              Абомазум теряет фиксацию
                      ▼
              Смещение влево (LDA) или вправо (RDA)
```

### Экономическая логика

```yaml
scenario_untreated_da:
  surgery_cost: "25000-40000₽"
  milk_loss: "15000-30000₽"
  culling_risk: "15-25%"
  total: "50000-90000₽"

scenario_early_intervention:
  rumen_support: "800₽"
  diet_correction: "0₽ (management)"
  prevented_da_rate: "~60% of high-risk cases"
  savings_per_prevented_case: "45000₽"
  roi: "+5500%"
```

---

## LIMITS

```yaml
APPLICABLE:
  dim: "5-30 days"
  species: "Dairy cattle"
  
NOT_APPLICABLE:
  late_lactation:
    reason: "Different etiology and risk profile"
  beef_cattle:
    reason: "Different feeding systems, lower DA incidence"
```

---

## VALIDATION

```yaml
minimum_cases: 10
farms_required: 3
metrics:
  primary:
    - da_incidence_in_screened_group: "% cows developing clinical DA"
    - early_intervention_success: "% high-risk cows recovering without surgery"
  secondary:
    - false_positive_rate: "High-risk screened but no DA"
    - cost_per_case_prevented: "Total intervention cost / prevented cases"
```

---

## Execution Framework

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - dim
    - bhb
    - dmi_actual
    - dmi_norm
    - ruminal_ph
    - previous_da
    - peak_yield
    - clinical_da_signs
    
  prediction:
    risk_level: "LOW / MEDIUM / HIGH"
    da_probability: "qualitative"
    
  outcome:
    clinical_da_occurred: true/false
    surgery_required: true/false
    days_to_da_if_occurred: int

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
```

---

*Framework: Execution Framework v4.0*
