---
rule_id: RULE-005
dl_ref: DL-005
case_refs: []  # Требуется валидация
date_created: 2026-04-11
date_updated: 2026-04-11
author: StanisSerg
category: metabolic
tags: [hypocalcemia, milk-fever, parturient-paresis, DCAD, calcium, transition-cow, anionic-salts]

# RULE STATE
rule_version: "1.0"
rule_maturity: conceptual  # Based on SoTA, requires validation
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

# RULE-005: Hypocalcemia-Milk-Fever-Prevention-and-Treatment

> **Тип:** executable decision operator — prevention & emergency treatment  
> **Maturity:** conceptual (v1.0) — основано на DCAD research (Goff, Horst, Roche)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** [DL-005](../../DS-cattle-operations/decisions/DL-005.md)  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: metabolic, фаза: transition  
> **SoTA:** CS.SOTA.XXX (DCAD diets), CS.SOTA.YYY (Calcium homeostasis)

---

## DECISION (Решение)

### Prevention Track (DCAD Protocol)

```yaml
hard_conditions:  # ALL must be TRUE for DCAD prevention
  - condition: "Parity"
    threshold: ">= 2"
    operator: ">="
    note: "First-lactation heifers excluded"
    
  - condition: "Days before calving"
    threshold: "21"
    operator: ">="
    unit: "days"
    note: "DCAD must start at least 21 days prepartum"
    
  - condition: "Close-up diet feasible"
    check: "Can separate and feed close-up group"

soft_conditions:  # Risk factors increasing priority
  - condition: "High risk breed"
    threshold: "Jersey or high-producing Holstein"
    weight: 1
    
  - condition: "Previous milk fever"
    threshold: "Had clinical hypocalcemia in previous lactation"
    weight: 1
    
  - condition: "BCS at dry-off"
    threshold: "> 3.5"
    weight: 1
    note: "Over-conditioned cows at higher risk"
    
  - condition: "Age"
    threshold: "> 5 years (3+ lactations)"
    weight: 1

blocking_conditions:
  - condition: "First-lactation heifer"
    reason: "Low hypocalcemia risk in heifers + negative DCAD may impair reproduction and bone development"
    risk_assessment: "Heifers have active bone remodeling; milk fever incidence < 2%"
    cost_benefit: "Prevention costs exceed benefits for this group"
    action: "USE_POSITIVE_DCAD_OR_STANDARD_DIET (DCAD 0 to +30)"
    
  - condition: "Pre-existing metabolic acidosis"
    reason: "Cannot tolerate additional acid load"
    action: "REFER_TO_VETERINARY_PROTOCOL"
```

### Emergency Treatment Track (Clinical Milk Fever)

```yaml
emergency_triggers:
  - condition: "Clinical signs of milk fever"
    signs: [sternal_recumbency, weakness, cold_ears, bloat]
    action: "IMMEDIATE_IV_CALCIUM"
    
  - condition: "Subclinical hypocalcemia confirmed"
    threshold: "Total Ca < 2.0 mmol/L OR Ionized Ca < 1.0 mmol/L"
    action: "ORAL_CALCIUM_SUPPLEMENTATION"
    
  - condition: "Imminent calving + high risk"
    factors: [Jersey, older cow, previous milk fever]
    action: "PROPHYLACTIC_CALCIUM"
```

### Verdict Logic

```
PREVENTION MODE (Prepartum):
─────────────────────────────
INITIAL ──► first_lactation? ──► BLOCKED (use standard diet)
              │
              NO
              │
              ▼
        close_up_period? ──► NOT_APPLICABLE (too early)
              │
              YES (within 21 days)
              │
              ▼
        evaluate_risk ──► DCAD_RECOMMENDED (LOW/MEDIUM/HIGH)
              │
              ▼
        IMPLEMENT_NEGATIVE_DCAD

EMERGENCY MODE (Postpartum):
────────────────────────────
INITIAL ──► clinical_signs? ──► EMERGENCY_IV_CALCIUM
              │
              NO
              │
              ▼
        subclinical_low_ca? ──► ORAL_CALCIUM_PROTOCOL
              │
              NO
              │
              ▼
        MONITOR_PREVENTIVELY
```

---

## STATE MACHINE

### Prevention States

```
┌─────────────────────────────────────────────────────────────┐
│  PREVENTION PHASE (Prepartum -21 to 0 days)                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  FIRST_LACTATION?                                           │
│       │                                                     │
│   YES ▼                                                     │
│  ┌─────────────┐                                            │
│  │   BLOCKED   │ ──► Standard diet (positive DCAD)          │
│  │  Heifers    │                                            │
│  └─────────────┘                                            │
│       │                                                     │
│   NO  │                                                     │
│       ▼                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   LOW RISK  │───►│ MEDIUM RISK │───►│  HIGH RISK  │     │
│  │  DCAD -50   │    │  DCAD -100  │    │  DCAD -150  │     │
│  │  (0 soft)   │    │  (1 soft)   │    │  (2+ soft)  │     │
│  └──────┬──────┘    └──────┬──────┘    └──────┬──────┘     │
│         │                  │                  │            │
│         └──────────────────┴──────────────────┘            │
│                            │                               │
│                            ▼                               │
│              ┌─────────────────────────┐                   │
│              │  MONITOR Urine pH       │                   │
│              │  Target: 6.0-6.5        │                   │
│              │  (5.8-6.8 acceptable)   │                   │
│              └─────────────────────────┘                   │
│                            │                               │
│                            ▼                               │
│              ┌─────────────────────────┐                   │
│              │  If pH < 5.5: REDUCE    │                   │
│              │  If pH > 7.0: INCREASE  │                   │
│              │  anion supplementation   │                   │
│              └─────────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Emergency Treatment States

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| CLINICAL_PARESIS | CRITICAL | IV Calcium borogluconate 23% | Immediate |
| SUBCLINICAL_LOW | HIGH | Oral calcium bolus | Within 2 hours |
| HIGH_RISK_PRECALVING | WARNING | Prophylactic calcium | At calving |
| STABLE | INFO | Continue monitoring | Regular |

---

## ACTION PROTOCOL

### Prevention: DCAD Implementation

**Step 1: Diet Formulation**
```yaml
action: FORMULATE_NEGATIVE_DCAD_DIET

target_dcac:
  low_risk: "-50 mEq/kg DM"
  medium_risk: "-100 to -120 mEq/kg DM"
  high_risk: "-150 mEq/kg DM"
  
formula: "DCAD (mEq/kg) = (Na + K) - (Cl + 0.6×S)"

implementation:
  - select_low_potassium_forages
  - add_anionic_salts:
      - calcium_chloride
      - magnesium_chloride
      - calcium_sulfate
      - magnesium_sulfate
      - or_hydrochloric_acid_preblend
      
  - ensure_mineral_adequacy:
      calcium: "1.0-1.2% DM"
      phosphorus: "0.35-0.40% DM"
      magnesium: "0.40-0.45% DM"
      sulfur: "0.40-0.45% DM"
```

**Step 2: Monitoring Urine pH**
```yaml
action: MONITOR_URINE_PH

protocol:
  frequency: "2 times per week"
  minimum_cows: "8 cows per group"
  timing: "After 2+ days on acidogenic diet"
  
target_ph:
  holstein: "6.0-6.5 (optimal)"
  jersey: "5.8-6.0 (may need lower)"
  
adjustments:
  - if_ph_below_5.5: "Reduce anions (over-acidified, DMI risk)"
  - if_ph_above_7.0: "Increase anions (under-acidified, no protection)"
  - if_ph_6.0_6.5: "Maintain current formulation"
```

**Step 3: Calving Transition**
```yaml
action: TRANSITION_TO_LACTATION_DIET
timing: "Immediately after calving"

diet_change:
  dcad: "Switch to positive DCAD (+35 to +45 mEq/100g)"
  calcium: "Increase to support lactation"
  energy: "Transition to high-energy lactation diet"
  
monitoring:
  - check_for_milk_fever_signs: "First 24-48 hours"
  - calcium_status: "If suspicious, test serum Ca"
```

### Emergency Treatment

**Step 1: Clinical Milk Fever (Recumbent Cow)**
```yaml
priority: CRITICAL
action: IV_CALCIUM_THERAPY

dosage:
  calcium_borogluconate_23%: "500-800 mL slow IV"
  rate: "Administer over 10-20 minutes"
  
monitoring_during_treatment:
  - heart_rate: "Watch for bradycardia"
  - auscultation: "Listen for cardiac arrhythmias"
  - body_temperature: "Monitor for hypothermia"
  
supportive_care:
  - keep_warm: "Blankets if needed"
  - maintain_sternal: "Prevent aspiration"
  - elevate_rear: "If bloated"
  
repeat_if_needed: "May repeat in 4-6 hours if partial response"
```

**Step 2: Oral Calcium for Subclinical/Prevention of Relapse**
```yaml
priority: HIGH
action: ORAL_CALCIUM_SUPPLEMENTATION

indications:
  - subclinical_hypocalcemia: "Ca < 2.0 mmol/L, standing"
  - high_risk_at_calving: "Jersey, old cow, previous case"
  - prevention_of_relapse: "After successful IV treatment"
  
dosage_options:
  calcium_gel: "50-100g elemental calcium"
  calcium_boluses: "2-4 boluses (check Ca content)"
  
timing:
  at_calving: "Immediately after calving"
  repeat: "12 hours later if high risk"
  
contraindications:
  - down_cow: "Cannot swallow safely"
  - severe_depression: "Aspiration risk"
  - already_hypercalcemic: "Test before administering"
```

**Step 3: Post-Treatment Monitoring**
```yaml
priority: 2
timeline: "24-48 hours post-treatment"

success_criteria:
  - standing: "Cow stands unassisted"
  - eating: "Normal appetite within 12 hours"
  - no_relapse: "No recurrence within 48 hours"
  
failure_indicators:
  - recurrent_paresis: "Second episode within 48h"
  - partial_response: "Weak but standing"
  - complications: "DA, ketosis, mastitis"
  
escalation_if_failure:
  - consider_hypomagnesemia: "Test Mg, may need Mg therapy"
  - check_for_other_metabolic: "Ketosis, DA concurrent"
  - intensive_monitoring: "Every 4-6 hours"
```

---

## BECAUSE (Механизм)

### Научное обоснование

```
Кальциевая homeostasis при отёле:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Проблема:
• Колострум содержит 2-3g Ca/L
• Суточная потребность: 30-50g Ca
• Резерв крови: ~3g (быстро истощается)
• Кишечная абсорбция недостаточна в первые дни

Механизм DCAD (Negative Dietary Cation-Anion Difference):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. МЕТАБОЛИЧЕСКИЙ АЦИДОЗ
   Низкий DCAD → Компенсированный ацидоз
   ↓
   Снижение pH крови
   ↓
   Увеличение чувствительности рецепторов PTH

2. АКТИВАЦИЯ PTH (Parathyroid Hormone)
   PTH + кислая среда →
   • ↑ Резорбция костной ткани (↑ Ca в кровь)
   • ↑ Реабсорбция Ca в почках
   • ↑ Синтез 1,25-(OH)₂-D₃ (активный витамин D)
   • ↑ Абсорбция Ca в кишечнике

3. МОНИТОРИНГ ЧЕРЕЗ pH МОЧИ
   Целевой pH: 6.0-6.5
   • < 5.5: Переацидификация, риск снижения DMI
   • > 7.0: Недостаточная защита
   • 6.0-6.5: Оптимальная активация механизмов

Эффективность (Research Evidence):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Negative DCAD (-100 to -150 mEq/kg):
  - Снижение клинической гипокальцемии на 70-80%
  - Снижение субклинической на 40-50%
  - Улучшение последующей репродукции (multiparous)

• Исключение первотелок:
  - У них активная ремоделизация костей
  - Негативный DCAD может ухудшить репродукцию
  - Стандартная диета или DCAD близкий к 0

• Jersey vs Holstein:
  - Jersey более чувствительны (низкий pH мочи 5.8-6.0)
  - Нужен более агрессивный подход или более низкий DCAD
```

### Экономическая логика

```yaml
scenario_no_prevention:
  incidence_clinical: "5-10% in high-risk herds"
  incidence_subclinical: "25-50%"
  
  costs_per_clinical_case:
    treatment: "3000-5000₽ (IV calcium + vet)"
    milk_loss: "5000-10000₽ (3-5 days reduced yield)"
    complications: "DA 15000₽, ketosis 8000₽, mastitis 5000₽"
    reproduction_delay: "5000₽"
  total_per_case: "30000-40000₽"
  
scenario_dcad_prevention:
  costs:
    anionic_salts: "+150-300₽/корова/сухостой"
    monitoring_urine_ph: "+100₽ (labor)"
    additional_magnesium: "+50₽"
  total_per_cow: "300-450₽"
  
  effectiveness:
    reduction_clinical: "70-80%"
    reduction_subclinical: "40-50%"
    
  savings:
    prevented_cases: "8% × 80% = 6.4% herd protected"
    saved_per_100_cows: "6.4 cases × 35000₽ = 224000₽"
    cost_per_100_cows: "100 × 400₽ = 40000₽"
    net_benefit_per_100: "184000₽"
    
  roi: "+460%"
  payback: "Immediate (prevention always cheaper)"
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  parity: ">= 2nd lactation (multiparous)"
  timing: "Close-up period (-21 to 0 days)"
  species: "Dairy cattle"
  management: "Can feed separate close-up group"
  
NOT_APPLICABLE:
  first_lactation_heifers:
    reason: "May impair reproduction, bone still growing"
    alternative: "Standard diet or neutral DCAD (0 to +30)"
    
  pre_existing_acidosis:
    conditions: [diarrhea, renal_failure, severe_ketosis]
    reason: "Cannot tolerate additional acid load"
    action: "Modified protocol with veterinary supervision"
    
  lack_of_monitoring_capacity:
    reason: "Cannot verify urine pH"
    risk: "Risk of over/under-acidification"
    mitigation: "Use palatable anion supplements or zeolite A"
```

### Soft Limits (Требуют адаптации)

```yaml
JERSEY_COWS:
  description: "Higher susceptibility to milk fever"
  adjustment: "More aggressive DCAD (-150) or lower urine pH target (5.8-6.0)"
  
HIGH_PRODUCING_HOLSTEIN:
  description: ">40L peak yield"
  adjustment: "Higher end of DCAD range (-120 to -150)"
  
PREVIOUS_MILK_FEVER:
  description: "Had clinical case in previous lactation"
  adjustment: "Consider prophylactic oral calcium at calving in addition to DCAD"
  
HOT_CLIMATE:
  description: "Heat stress reduces DMI"
  adjustment: "More palatable anion sources, ensure water availability"
  
LIMITED_FORAGE_OPTIONS:
  description: "Cannot source low-K forages"
  adjustment: "Rely more on anionic salts, increase monitoring"
```

### System Constraints (Системные ограничения)

```yaml
DCAD_vs_DMI_constraint:
  description: "DCAD strategy must not compromise energy intake"
  rule: "If DMI drops > 10% on DCAD diet → REDUCE acidification"
  mechanism: "Ketosis risk from low DMI > Milk fever risk from moderate DCAD"
  coordination_with_RULE-004: "Both rules monitor DMI; whichever detects drop first triggers adjustment"
  
  threshold:
    normal_dmi: "12-14 kg DM/day in close-up"
    critical_drop: "< 10.8 kg DM/day (10% reduction)"
    action_if_violated: "Reduce anion supplementation, prioritize energy intake"
    
  trade_off_resolution:
    priority: "DMI preservation > Maximum DCAD negative"
    reasoning: "Starvation ketosis more dangerous than moderate hypocalcemia risk"
```

---

## VALIDATION

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| — | — | — | — | Нет собственной валидации | **LOW** |

**Note:** RULE-005 основано на обширной научной базе (Goff, Horst, Roche), но требует локальной валидации для конкретных условий фермы.

### Required Validation

```yaml
minimum_cases: 10
farms_required: 3
design: "Controlled before/after or cohort study"

distribution:
  prevention_cases: "Monitor DCAD implementation in close-up group"
  treatment_cases: "Document emergency IV calcium responses"
  
metrics_to_track:
  clinical_milk_fever_rate: "% cows with paresis"
  subclinical_hypocalcemia: "% cows with Ca < 2.0 mmol/L at 0-2 DIM"
  urine_ph_compliance: "% samples in target range (6.0-6.5)"
  dmi_close_up: "Ensure no significant reduction"
  subsequent_reproduction: "First service conception rate"
  
success_criteria:
  - clinical_reduction: "> 70% vs baseline or control"
  - subclinical_reduction: "> 40% vs baseline"
  - no_dmi_depression: "< 5% reduction in close-up DMI"
```

---

## RULE METRICS

### Outcome Registration

```yaml
outcome_record:
  timestamp: "YYYY-MM-DD HH:MM"
  farm_id: "FARM-XXX"
  cow_id: "COW-XXXXX"
  parity: "2nd, 3rd, etc."
  
  prevention_data:
    dcad_start_date: "YYYY-MM-DD"
    urine_ph_values: [6.2, 6.4, 6.1]  # Monitoring log
    anion_source: "MgCl2 + CaCl2"
    close_up_dmi: "12.5 kg"
    
  calving_data:
    calving_date: "YYYY-MM-DD"
    ease_of_calving: "1-5 scale"
    milk_fever_occurred: true/false
    
  treatment_data:  # If applicable
    treatment_time: "Hours post-calving"
    calcium_iv_ml: "500"
    response_time: "Minutes to stand"
    relapse: true/false
    
  classification: "TP / FP / FN"  # For prevention effectiveness
  root_cause: null  # If prevention failed
```

### Root Cause Categories

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| **inadequate_dcadminus** | **P1** | DCAD not negative enough | Urine pH > 7.0, diet formulation error |
| **over_acidification** | **P1** | Too negative DCAD | Urine pH < 5.5, DMI depression |
| **timing_error** | **P1** | Started DCAD too late | < 21 days before calving |
| **heifer_included** | **P2** | Accidentally fed to first-lactation | Management error in grouping |
| **compliance_failure** | **P2** | Cows didn't eat supplemented diet | Sorting, palatability issues |
| **concurrent_disease** | **P2** | Metritis, mastitis masking response | Complex metabolic case |
| **individual_variation** | **P3** | Some cows always high-risk | Genetic susceptibility |

### Action by Priority

```yaml
P1 (critical):
  threshold: "2+ formulation или timing errors"
  timeline: "24–48 часов"
  action: "Review DCAD calculation, verify forage mineral content"
  
P2 (planned):
  threshold: "3+ compliance или grouping issues"
  timeline: "в ближайший scheduled review"
  action: "Improve feed delivery, check forage sorting"
  
P3 (no_action):
  threshold: "individual_variation"
  timeline: "не требует действия"
  action: "Document for genetic selection consideration"
```

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-04-11 | Создано на основе SoTA (DCAD research, Goff, Horst, Roche) | StanisSerg |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **Heifer exclusion** | Well documented | Medium | May be hard to manage separate groups | Physical separation or neutral DCAD for heifers |
| **Urine pH variability** | Known variation | Medium | Individual cows vary in response | Test 8+ cows, use average |
| **Forage mineral variation** | Field reality | High | K content varies, affecting DCAD | Frequent forage testing |
| **Palatability issues** | Some anions unpalatable | Medium | Reduced DMI | Use palatable sources (MgCl2, CaCl2) |
| **No local validation** | Research-based only | Medium | May not work in specific conditions | Validate with 10+ cases |

### Acceptable Error Bounds

**Пока НЕ определены — требуется валидация.**

Target (post-validation):
- Clinical milk fever rate: < 2% in multiparous cows
- Subclinical hypocalcemia: < 15% (Ca < 2.0 mmol/L)
- Urine pH in target range: > 80% of samples
- Close-up DMI maintained: > 95% of control

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
    - date
    - cow_id
    - parity
    - dcad_start_date
    - urine_ph_values: []
    - calving_date
    - milk_fever_occurred: true/false
    - treatment_given: "IV Ca / Oral Ca / None"
    
  prediction:
    risk_level: "LOW / MEDIUM / HIGH"
    dcad_target: "-50 / -100 / -150"
    
  decision:
    heifer_or_multiparous: "Determines DCAD applicability"
    
  outcome:
    clinical_case: true/false
    subclinical_ca_level: "mmol/L"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
```

#### Validation Steps

1. Применить на 3+ фермах (только multiparous cows)
2. Создать 10+ кейсов (close-up cows with DCAD monitoring)
3. Document:
   - Urine pH trends
   - Actual DCAD achieved (feed analysis)
   - Milk fever incidence vs control group
   - DMI in close-up period
4. Calculate:
   - Reduction in clinical cases
   - Cost per prevented case
   - ROI of DCAD implementation

```yaml
precision_recall_tradeoff:
  prevention_context: "Not applicable — this is prevention, not screening"
  key_metrics:
    - "Incidence reduction (clinical and subclinical)"
    - "Cost-effectiveness vs treatment"
    - "Safety (no DMI depression)"
```

---

### Phase 2: Robustness (HIGH)

```yaml
actions:
  - validate_different_anion_sources
  - test_without_urine_monitoring (palatability approach)
  - validate_in_hot_climate
  - validate_with_high_potassium_forages
  - test_zeolite_a_as_alternative

metrics_activation:
  conditions:
    - ≥10 triggers
    - ≥5 outcomes
```

---

### Phase 3: Full Automation (MEDIUM)

```yaml
components:
  - automatic_dcad_calculator
  - urine_ph_tracking_app
  - early_warning_alerts (high-risk cows)
  - integration_with_feed_software

readiness_criteria:
  - dcad_formulation_reliable: true
  - urine_monitoring_sustainable: true
```

---

### Phase 3.5: Rule Saturation (CRITICAL)

```yaml
saturation_criteria:
  rules_stable: ">=3–5"
  zones_defined: true
  conflicts_mapped: true
  decision_layer_clear: true

dependencies:
  - RULE-004: "Dry period nutrition (may overlap — coordinate)"
  - RULE-002: "SCK screening (concurrent metabolic risk)"
  
integration:
  - RULE-005 (Ca prevention) runs parallel to RULE-004 (energy balance)
  - Both active in close-up period
  - Coordinate through shared monitoring (urine pH, DMI)
```

---

### Phase 4: ML (LOW)

```yaml
potential_improvements:
  prevention_layer:
    - predict_individual_ca_mobilization: "Genetic markers, parity, history"
    - optimize_dcad_by_cow: "Individual vs group formulation"
    - predict_urine_ph_without_testing: "From diet composition"
    
  treatment_layer:
    - predict_iv_calcium_response: "Duration of effect"
    - optimize_oral_calcium_timing: "Best time post-calving"
    - prevent_relapse: "Who needs second dose?"

requirements:
  - ≥50 structured cases
  - error_patterns understood
  - mineral_analysis_accurate
```

---

### Critical Principle

```
Rule Saturation → понятная структура → ML усиливает
НЕ:
ML → попытка заменить неустойчивую систему
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
┌─────────────────────────────────────────────────────────────────┐
│                    METABOLIC ZONE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PREVENTION PHASE (Prepartum)                                   │
│  ├── RULE-004: Dry Period Nutrition (energy balance)            │
│  └── RULE-005: Hypocalcemia Prevention (calcium homeostasis)    │
│       │  ← Parallel, coordinate through close-up management     │
│       │                                                         │
│  TRANSITION → POSTPARTUM                                        │
│       │                                                         │
│       ├──► RULE-002: SCK Screening (if metabolic issues)        │
│       └──► Emergency: RULE-005 treatment mode (if milk fever)   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

Parallel Prevention (Close-up period):
  - RULE-004 manages: Energy, BCS, NEFA, ketosis risk
  - RULE-005 manages: Calcium, DCAD, milk fever risk
  - Both monitored through: DMI, urine pH, cow behavior
```

### Boundary Conditions with Other Rules

| Rule | Boundary | Coordination |
|------|----------|--------------|
| RULE-004 | Both in close-up | Monitor DMI together (acidosis affects intake) |
| RULE-002 | Postpartum detection | If milk fever → may not need SCK screening immediately |
| RULE-001 | Postpartum decision | Milk fever takes precedence over metabolic deficit evaluation |
| RULE-003 | Postpartum treatment | Oral calcium (005) vs PG (003) — different pathways |

### Escalation / Applicability Logic

| Situation | Primary Rule | Logic |
|-----------|--------------|-------|
| Close-up cow, multiparous | RULE-005 (prevention) + RULE-004 | Parallel prevention protocols |
| Clinical milk fever at calving | RULE-005 (emergency) | Overrides routine postpartum protocols |
| Milk fever + ketosis signs | RULE-005 (IV Ca) → then RULE-001 | Treat calcium emergency first |
| First-lactation heifer | RULE-004 only | RULE-005 prevention BLOCKED |
| Suspected milk fever but standing | RULE-005 (oral Ca) | Subclinical treatment |

---

*Framework: Execution Framework v4.0*  
*Format: CASE → DL → RULE (executable, managed)*  
*System Loop: CASE→PREDICTION→DECISION→FACT→ERROR→RULE→UPDATE→NEXT CASE*
