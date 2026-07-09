---
rule_id: RULE-006
dl_ref: DL-006
case_refs: []  # Требуется валидация
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: reproductive
tags: [metritis, retained-placenta, postpartum, rp, uterine-health, antibiotic, transition-cow]

# RULE STATE
rule_version: "1.0"
rule_maturity: conceptual  # Based on SoTA, requires validation
status: conceptual
trend: stable

# Временные метки
last_trigger: null
last_error: null
last_review: 2026-04-15
next_review: 2026-07-15

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

# RULE-006: Metritis-Retained-Placenta-Protocol

> **Тип:** executable decision operator — postpartum reproductive intervention  
> **Maturity:** conceptual (v1.0) — основано на reproductive herd-health literature  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-006  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: reproductive, фаза: early postpartum  
> **SoTA:** CS.SOTA.XXX (Postpartum uterine health), CS.SOTA.YYY (Antibiotic stewardship in dairy)

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:  # ALL must be TRUE
  - condition: "Early postpartum window"
    dim_range: "1 to 21 days"
    note: "Metritis / RP typically manifest in this window"

  - condition: "Uterine pathology suspected or confirmed"
    criteria: "ANY of: retained placenta >24h, fever >39.5°C, foul-smelling discharge, uterine tenderness"

soft_conditions:  # Risk factors increasing priority / confidence
  - condition: "Concurrent metabolic disorder"
    criteria: "BHB >1.2 OR total Ca <2.0 mmol/L"
    weight: 1
    note: "Metabolic deficit impairs immune function and uterine involution"

  - condition: "Difficult calving"
    criteria: "Dystocia or twinning"
    weight: 1
    note: "Trauma and contamination risk higher"

  - condition: "Advanced parity"
    criteria: "Parity >= 3"
    weight: 1
    note: "Older cows have slower uterine involution"

blocking_conditions:  # IF TRUE → RULE_BLOCKED
  - condition: "Severe systemic illness or septic shock"
    examples: [recumbency, toxic mucous membranes, weak pulse, severe dehydration]
    action: "REFER_TO_EMERGENCY_VETERINARY_PROTOCOL"
    note: "Farm-level protocol insufficient — needs intensive critical care"
```

### Verdict Logic

```
INITIAL ──► severe_systemic_illness? ──► BLOCKED
              │
              NO
              │
              ▼
        in_window_1_21_dim? ──► NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        hard_trigger_met? ──► NO ──► NOT_TRIGGERED
              │
              YES
              │
              ▼
        evaluate_soft_score ──► TRIGGERED HIGH / MEDIUM / LOW
```

**Verdict Types:**
- `RULE_006_BLOCKED`: Тяжёлая системная инфекция — экстренный ветеринарный вызов
- `RULE_006_NOT_APPLICABLE`: Вне окна 1-21 DIM — использовать другие протоколы
- `RULE_006_TRIGGERED_HIGH`: Высокий риск (2-3 soft) — системные антибиотики + местная терапия + метаболическая поддержка
- `RULE_006_TRIGGERED_MEDIUM`: Умеренный риск (1 soft) — системные антибиотики + мониторинг
- `RULE_006_TRIGGERED_LOW`: Ограниченный риск (0 soft) — местная терапия + интенсивный мониторинг
- `RULE_006_NOT_TRIGGERED`: Hard-триггеры не выявлены

---

## STATE MACHINE

```
┌─────────────────────────────────────────────────────────────┐
│  EARLY POSTPARTUM (1-21 DIM)                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SEVERE_SYSTEMIC_ILLNESS?                                   │
│       │                                                     │
│   YES ▼                                                     │
│  ┌─────────────┐                                            │
│  │   BLOCKED   │ ──► Emergency veterinary care              │
│  │  Critical   │                                            │
│  └─────────────┘                                            │
│       │                                                     │
│   NO  │                                                     │
│       ▼                                                     │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │   LOW RISK  │───►│ MEDIUM RISK │───►│  HIGH RISK  │     │
│  │ Local + mon │    │ Systemic AB │    │ Systemic +  │     │
│  │  (0 soft)   │    │  (1 soft)   │    │ local + meta│     │
│  └──────┬──────┘    └──────┬──────┘    │ (2+ soft)   │     │
│         │                  │            └──────┬──────┘     │
│         └──────────────────┴──────────────────┘            │
│                            │                               │
│                            ▼                               │
│              ┌─────────────────────────┐                   │
│              │  Re-evaluate at day 3   │                   │
│              │  and day 7               │                   │
│              └─────────────────────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### State Definitions

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Emergency vet + critical care | Immediate |
| NOT_APPLICABLE | INFO | Use lactation or other protocols | — |
| TRIGGERED (LOW) | WARNING | Local therapy (PGF2α / lavage if RP) + monitor | 48 hours |
| TRIGGERED (MEDIUM) | HIGH | Systemic antibiotic + monitor | 24-48 hours |
| TRIGGERED (HIGH) | CRITICAL | Systemic antibiotic + uterine therapy + metabolic support | 24 hours |

---

## ACTION PROTOCOL

### При RULE_006_TRIGGERED

**Step 1: Оценка (Assessment)**
```yaml
action: CONFIRM_DIAGNOSIS
substeps:
  - measure: "Rectal temperature"
  - inspect: "Character of vaginal discharge"
  - palpate: "Uterine tone and size (if safe)"
  - review: "Calving ease record, retention of fetal membranes"
  - test: "BHB and Ca if not done in last 48h"
```

**Step 2: Терапия (Treatment)**
```yaml
priority: 1

low_risk:
  local:
    - prostaglandin_F2a: "If RP >24h OR poor uterine tone"
    - uterine_lavage: "If RP or foul discharge, by trained staff only"
  monitoring: "Temperature 2x daily, appetite, milk yield"

medium_risk:
  systemic_antibiotic:
    - ceftiofur: "2.2 mg/kg SC q24h × 3-5 days"
    - alternative: "Penicillin per farm vet protocol"
  support:
    - ensure_hydration: "Free water access, oral fluids if needed"
    - pain_management: "NSAID per protocol (e.g. meloxicam)"

high_risk:
  systemic_antibiotic:
    - ceftiofur: "2.2 mg/kg SC q24h × 5 days or until afebrile 48h"
    - consider_culture: "If previous treatment failures on farm"
  uterine_therapy:
    - prostaglandin_F2a: "To enhance uterine involution"
    - uterine_lavage: "If RP or large volume fetid fluid"
  metabolic_support:
    - calcium: "If hypocalcemia present or suspected"
    - propylene_glycol: "If BHB >1.2 (refer RULE-003 after stabilization)"
    - fluids: "Oral or IV depending on dehydration"
```

**Step 3: Метаболическая координация (Metabolic Coordination)**
```yaml
priority: 2
note: "Metritis and metabolic disease often coexist."

coordination:
  - if BHB >1.2:
      action: "Systemic correction first (RULE-001), then PG if applicable (RULE-003)"
  - if milk_fever_signs:
      action: "Calcium therapy takes precedence (RULE-005)"
  - if both metritis + severe ketosis:
      action: "Treat metritis AND metabolism simultaneously — do not delay antibiotics"
```

**Step 4: Мониторинг (Monitoring)**
```yaml
priority: 3
timeline: "7 days minimum"

metrics:
  daily:
    - temperature: "Target <39.0°C by day 3"
    - appetite: "DMI tracking"
    - milk_yield: "Compare to pre-illness baseline"
  day_3_and_day_7:
    - uterine_discharge: "Should become mucoid, non-fetid"
    - general_attitude: "Alert, mobile, rumination"

success_criteria:
  - afebrile: "<39.0°C for 48h"
  - eating: "DMI >80% of expected"
  - milk: "Yield stable or recovering"
  - discharge: "Mucoid, no foul odor"

failure_indicators:
  - persistent_fever: ">39.5°C after 72h of therapy"
  - anorexia: "DMI <50% for >48h"
  - relapse: "Fetid discharge returns after improvement"
  
escalation_if_failure:
  - veterinary_review: "Culture, alternate antibiotic, imaging"
  - consider_abscess: "Retained twin / uterine tear / perimetritis"
```

---

## BECAUSE (Механизм)

### Патофизиология

```
Переходный период ──► иммунодепрессия + открытая матка
         │
         ▼
┌─────────────────────────────────────────────┐
│  Факторы риска:                             │
│  • Дистоция / двойня ──► травма матки       │
│  • Задержка последа ──► бактериальная       │
│    колонизация (E. coli, Trueperella)       │
│  • Кетоз / гипокальceмия ──► иммунная       │
│    недостаточность, замедленная инволюция   │
│  • Старшие тёлки ──► сниженный тонус матки  │
└─────────────────────────────────────────────┘
         │
         ▼
Метритис ──► системное воспаление ──► ↓DMI
         │                              ↓молоко
         │                              ↓концепция
         ▼
    Если не лечить:
    • Хронический эндометрит
    • Бесплодие
    • Выбытие
```

### Экономическая логика

```yaml
scenario_no_intervention:
  outcomes:
    chronic_endometritis: "30-50%"
    conception_delay: "+30-60 days"
    culling_risk: "+20-40%"
  costs:
    milk_loss: "5000-15000₽"
    reproduction_delay: "5000-10000₽"
    culling_replacement: "80000-150000₽"

scenario_rule_006_treated:
  costs:
    antibiotic_course: "800-1500₽"
    prostaglandin: "300-500₽"
    labor_monitoring: "500₽"
    total: "1600-2500₽"
  effectiveness:
    recovery_rate: ">85% if treated early"
    conception_delay: "minimized"
  savings_vs_no_treatment: ">30000₽ per cow"
  roi: "+1200%"
  
economic_verdict: "EXTREMELY_COST_EFFECTIVE"
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  phase: "Early postpartum (1-21 DIM)"
  species: "Dairy cattle"
  diagnosis: "Retained placenta or metritis suspected/confirmed"

NOT_APPLICABLE:
  late_lactation:
    dim: ">60 days"
    reason: "Different etiology (chronic endometritis, cysts)"
    action: "USE_REPRODUCTIVE_SPECIALIST_PROTOCOL"
    
  prepartum:
    dim: "<0"
    reason: "Uterine pathology not manifest before calving"
    
  pregnant_cow:
    note: "Therapy must be pregnancy-safe if bred recently"
    action: "VERIFY_PREGNANCY_STATUS_BEFORE_PGF2a"
```

### Soft Limits (Требуют адаптации)

```yaml
ORGANIC_FARM:
  restriction: "Antibiotic withdrawal restrictions"
  adjustment: "Emphasize local therapy, NSAIDs, homeopathy per farm policy"
  note: "May need longer recovery time"

SEASONAL_CALVING:
  issue: "High caseload during peak calving"
  adjustment: "Triage by severity; high-risk get priority"

LIMITED_VET_ACCESS:
  issue: "No veterinarian on call"
  adjustment: "Train farm staff in safe uterine lavage; use oral antibiotics where legal"
```

---

## VALIDATION

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| — | — | — | — | Нет собственной валидации | **LOW** |

### Required Validation

```yaml
minimum_cases: 10
farms_required: 3
design: "Prospective cohort or controlled before/after"

metrics_to_track:
  primary:
    - recovery_rate: "Afebrile + normal discharge by day 7"
    - conception_rate_150_dim: "% pregnant by 150 DIM"
  secondary:
    - antibiotic_use: "Days of therapy"
    - culling_rate: "% culled for reproduction <200 DIM"
    - milk_yield_recovery: "vs herd mates"
    - treatment_cost: "Per case"

success_criteria:
  - early_recovery: ">80% by day 7"
  - conception_preserved: "Within 10% of herd average"
  - cost_effectiveness: "ROI >500%"
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
  
  input_data:
    dim: 5
    retained_placenta_hours: 30
    fever: 40.1
    foul_smelling_discharge: true
    bhb: 1.4
    dystocia: false
    
  treatment:
    antibiotic: "ceftiofur"
    duration_days: 5
    prostaglandin: true
    
  actual_outcome:
    afebrile_by_day_3: true
    normal_discharge_by_day_7: true
    milk_yield_recovery: "95% by day 14"
    pregnant_by_150_dim: true
    
  classification: "TP"
  root_cause: null
```

### Root Cause Categories

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| **delayed_treatment** | **P1** | Начали лечить поздно | RP >48h без вмешательства |
| **wrong_antibiotic** | **P1** | Резистентность или неверный спектр | Нет эффекта от пенициллина |
| **missed_metabolic** | **P1** | Не увидели сопутствующий кетоз | BHB не проверили |
| **calving_hygiene** | **P2** | Загрязнённый маточник | Плохая гигиена при отёле |
| **individual_susceptibility** | **P3** | Генетика / анатомия | Некоторые коровы всегда рискуют |

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-04-15 | Создано на основе reproductive herd-health protocols | StanisSerg |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **No local validation** | Literature only | Medium | May need antibiotic adjustments | Validate with 10+ cases |
| **Subjective discharge scoring** | Known variability | Medium | Inconsistent diagnosis | Train staff, use photos |
| **Concurrent diseases** | Common | High | Metritis + ketosis + mastitis | Systematic screening panel |
| **Withdrawal times** | Regulatory | Low | Milk discard costs | Track records carefully |

### Acceptable Error Bounds

Target (post-validation):
- Recovery by day 7: > 80%
- False positives (treated without true metritis): < 15%
- False negatives (missed metritis): < 10%

---

## Execution Framework

### Phase 1: Validation + Light Automation (CRITICAL)

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - dim
    - retained_placenta_hours
    - fever
    - foul_smelling_discharge
    - uterine_tenderness
    - dystocia
    - twinning
    - bhb
    - total_ca
    - severe_systemic_illness
    
  prediction:
    risk_level: "LOW / MEDIUM / HIGH"
    recommendation: "Local / Systemic AB / Systemic + meta"
    
  outcome:
    afebrile_by_day_3: true/false
    normal_discharge_by_day_7: true/false
    pregnant_by_150_dim: true/false

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
```

### Phase 2: Robustness (HIGH)

```yaml
actions:
  - validate_antibiotic_protocol_per_farm
  - standardize_discharge_scoring
  - test_integration_with_metabolic_rules
  - measure_economic_precision
```

### Phase 3: Full Automation (MEDIUM)

```yaml
components:
  - automated_alert_21_day_window
  - treatment_compliance_tracker
  - fertility_outcome_linkage
```

---

## RELATIONSHIPS

### В портфеле метаболических и репродуктивных правил

```
┌─────────────────────────────────────────────────────────────────┐
│                    TRANSITION ZONE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PREVENTION (Prepartum)                                         │
│  ├── RULE-004: Dry Period Nutrition                             │
│  └── RULE-005: Hypocalcemia Prevention                          │
│                                                                 │
│  EARLY POSTPARTUM (0-21 DIM)                                    │
│  ├── RULE-005: Emergency Calcium (if milk fever)               │
│  ├── RULE-002: SCK Screening                                    │
│  ├── RULE-001: Metabolic Deficit Decision                       │
│  ├── RULE-003: PG Protocol                                      │
│  └── RULE-006: Metritis / RP Protocol  ← NEW                   │
│       │  ← Parallel with metabolic rules                        │
│       │                                                         │
│       ▼                                                         │
│  REPRODUCTIVE OUTCOMES                                          │
│       Conception, culling, milk yield                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Boundary Conditions with Other Rules

| Rule | Boundary | Coordination |
|------|----------|--------------|
| RULE-005 | Milk fever + metritis | Treat calcium emergency first, do not delay antibiotics |
| RULE-001 | Severe ketosis + metritis | Systemic correction + antibiotics together |
| RULE-003 | PG applicable but metritis present | Give PG if cow can swallow; antibiotics are priority |
| RULE-002 | SCK screening triggers | If SCK + metritis → escalate both RULE-003 and RULE-006 |

### Escalation / Applicability Logic

| Situation | Primary Rule | Logic |
|-----------|--------------|-------|
| Metritis + BHB>1.2 + can swallow | RULE-006 + RULE-003 | Antibiotics first, PG as support |
| Metritis + milk fever signs | RULE-005 (emergency) → then RULE-006 | Calcium stabilizes, then antibiotics |
| RP only, no fever, no metabolic issues | RULE-006 (LOW) | Local therapy + monitoring |
| RP + fever + ketosis | RULE-006 (HIGH) | Systemic AB + metabolic support |

---

*Framework: Execution Framework v4.0*  
*Format: CASE → DL → RULE (executable, managed)*  
*System Loop: CASE→PREDICTION→DECISION→FACT→ERROR→RULE→UPDATE→NEXT CASE*
