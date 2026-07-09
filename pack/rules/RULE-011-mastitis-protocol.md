---
rule_id: RULE-011
dl_ref: DL-011
case_refs: []
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: health
tags: [mastitis, udder-health, scc, antibiotic, culture, milk-quality, clinical-mastitis]

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

# RULE-011: Mastitis-Protocol

> **Тип:** executable decision operator — udder health intervention  
> **Maturity:** conceptual (v1.0)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-011  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: health, фаза: lactation  
> **SoTA:** CS.SOTA.XXX (Mastitis treatment guidelines), CS.SOTA.YYY (SCC-based management)

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:
  - condition: "Lactating cow"
    note: "Dry cow mastitis uses different protocol"

  - condition: "Mastitis suspected or confirmed"
    criteria: "ANY of: clinical signs in milk/clf, SCC > 400k, CMT score >= 3, abnormal udder tissue"

soft_conditions:
  - condition: "Severe clinical mastitis"
    criteria: "Systemic illness OR udder gangrene OR toxic milk"
    weight: 1

  - condition: "Repeated case"
    criteria: "3+ cases in current lactation OR 2+ cases same quarter"
    weight: 1

  - condition: "High SCC chronic"
    criteria: "SCC > 400k for > 30 days"
    weight: 1

  - condition: "Culture available"
    criteria: "CMT or lab culture result within 48h"
    weight: 1
    note: "Enables targeted therapy"

  - condition: "Late lactation"
    criteria: "DIM > 250"
    weight: 1
    note: "Recovery time limited before dry-off"

blocking_conditions:
  - condition: "Gangrenous mastitis or septic shock"
    examples: [udder_gangrene, systemic_toxicosis, recumbency]
    action: "REFER_TO_EMERGENCY_VETERINARY_PROTOCOL"
```

### Verdict Logic

```
INITIAL ──► gangrene_or_septic? ──► BLOCKED
              │
              NO
              │
              ▼
        lactating_and_mastitis? ──► NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        evaluate_severity_and_history
              │
              ├── Severe clinical ──► EMERGENCY_ANTIBIOTIC_+_SYSTEMIC_SUPPORT
              │
              ├── Repeated/chronic ──► CULL_OR_SEGREGATE_+_CULTURE
              │
              ├── Mild clinical + culture ──► TARGETED_INTRAMAMMARY_THERAPY
              │
              └── Subclinical + SCC high ──► MONITOR_OR_TREAT_BASED_ON_CULTURE
```

**Verdict Types:**
- `RULE_011_BLOCKED`: Гангренозный/септический мастит — немедленно ветврач
- `RULE_011_NOT_APPLICABLE`: Не лактирующая корова / нет признаков мастита
- `RULE_011_EMERGENCY`: Тяжёлый клинический мастит — системные антибиотики + поддержка
- `RULE_011_CHRONIC_CULL_CANDIDATE`: Хронический/рецидивирующий — рассмотреть отсев после культуры
- `RULE_011_TARGETED_TREATMENT`: Культура доступна — целевое внутривымянное лечение
- `RULE_011_BLIND_TREATMENT`: Лёгкий клинический без культуры — стандартная терапия + взятие пробы
- `RULE_011_MONITOR_CULTURE`: Субклинический — культура + решение по результату

---

## STATE MACHINE

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Emergency vet + intensive care | Immediate |
| EMERGENCY | HIGH | Systemic antibiotic + anti-inflammatory + udder support | 0-4 hours |
| CHRONIC_CULL_CANDIDATE | HIGH | Culture → treat if curable, else cull decision | 24-48 hours |
| TARGETED_TREATMENT | MEDIUM | Intramammary antibiotic per culture + monitoring | 24-48 hours |
| BLIND_TREATMENT | MEDIUM | Standard intramammary + sample for culture before first treatment | First milking |
| MONITOR_CULTURE | LOW | Culture, treat only if gram-positive or SCC trending up | 3-7 days |

---

## ACTION PROTOCOL

### При RULE_011_EMERGENCY

```yaml
priority: 1
actions:
  systemic_antibiotic:
    - ceftiofur: "2.2 mg/kg SC q24h"
    - oxytetracycline: "Alternative per vet protocol"
  anti_inflammatory:
    - flunixin_meglumine: "Or meloxicam per protocol"
  supportive:
    - fluids: "Oral or IV if dehydrated"
    - udder_support: "Frequent milk-out, warm compresses"
    - isolation: "Segregate from herd"

monitoring:
  - temperature: "Every 4-6 hours until afebrile 24h"
  - appetite: "Every 12 hours"
  - udder_texture: "Every 12 hours"
  - milk_appearance: "Every milking"

success_criteria:
  - afebrile: "< 39.0°C for 48h"
  - milk: "Returns to normal appearance by day 3-5"
  - udder: "Soft, non-painful"

failure_indicators:
  - persistent_fever: "> 39.5°C after 72h"
  - milk_worsening: "Blood, clots, fetid odor"
  - udder_gangrene: "Cold, discolored skin"
  
escalation_if_failure:
  - veterinary_review: "Culture, imaging, possible surgery"
```

### При RULE_011_TARGETED_TREATMENT

```yaml
priority: 2
actions:
  gram_positive:
    - intramammary: "Cloxacillin or cephalexin"
    - duration: "Per label (typically 3-5 days)"
  gram_negative:
    - note: "Often self-limiting; systemic therapy may be more effective"
    - action: "Consult vet for systemic antibiotic or supportive care"
  no_growth:
    - action: "Supportive care + environmental review"

sample_timing:
  - before_first_treatment: "Aseptic sample for culture"
  - during_treatment: "Daily CMT or visual score"
  - post_treatment: "Culture at 7-14 days to confirm cure"
```

### При RULE_011_BLIND_TREATMENT

```yaml
priority: 2
actions:
  intramammary:
    - first_line: "Cloxacillin or cephalexin IM"
    - duration: "3-5 days"
  sampling:
    - before_first_treatment: "MUST take aseptic sample for culture"
  monitoring:
    - milk_appearance: "Every milking"
    - udder_texture: "Daily"

rationale: |
  Blind treatment is acceptable ONLY for first-case mild clinical mastitis
  in early lactation, BUT culture sample must be taken before first infusion.
  This preserves the option to switch therapy based on results.
```

### При RULE_011_CHRONIC_CULL_CANDIDATE

```yaml
priority: 2
actions:
  - culture: "Mandatory before any further treatment"
  - economic_review: |
      Calculate: treatment cost + milk discard + lost production
      vs. replacement heifer value + expected first-lactation yield
  - decision_tree:
      - curable_pathogen + reasonable_cost: "Treat one final time"
      - resistant_or_unknowable: "Cull at next opportunity"
      - near_dry_off: "Dry cow therapy, cull if not cured after calving"
```

---

## BECAUSE (Механизм)

### Патофизиология

```
Вход инфекции (через сосковый канал)
         │
         ├──► Environmental (E. coli, Klebsiella, S. uberis)
         │      → Острая, часто системная, может самоограничиться
         │
         └──► Contagious (S. aureus, Strep. agalactiae, Mycoplasma)
                → Хроническая, трудноизлечимая, распространяется на других

Экономика мастита:
  • Клинический случай: 3000-8000₽ (лечение + потери молока + дискард)
  • Субклинический высокий SCC: 1500-3000₽/корову/год (потери молока + штрафы)
  • Хронический S. aureus: часто невыгодно лечить, отсев дешевле
```

### Почему культура важна

```
Blind therapy → резистентность → лечение перестаёт работать
Culture-based → точный выбор антибиотика → выше % излечения
  • Gram-positive (Staph, Strep): отлично лечится внутривымянно
  • Gram-negative (E. coli): часто самоограничивается, антибиотики не нужны
  • No growth: проблема в управлении/гигиене, не в инфекции
```

### Экономическая логика

```yaml
scenario_blind_treatment_all_cases:
  treatment_cost: "500₽ × 100 cases = 50000₽"
  effectiveness: "60-70% for gram-positive, 20-30% for gram-negative"
  hidden_cost: "Resistant herd, repeated cases, culling of treatable cows"

scenario_rule_011_culture_based:
  culture_cost: "300₽ × 100 samples = 30000₽"
  targeted_treatment: "Treat only 70 cases (gram-pos + severe)"
  treatment_cost: "500₽ × 70 = 35000₽"
  total: "65000₽"
  
  savings:
    - avoided_unnecessary_treatment: "30 cases × 500₽ = 15000₽"
    - improved_cure_rate: "+15-20%"
    - reduced_resistance: "Long-term herd benefit"
    - better_culling_decisions: "Avoid culling curable cows, cull chronic faster"
    
  net_benefit_per_100_cases: "> 25000₽"
  roi: "+40% direct, +200% long-term"
  
economic_verdict: "COST_EFFECTIVE_WITH_STRONG_LONG_TERM_BENEFIT"
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  status: "Lactating cow"
  diagnosis: "Mastitis suspected or confirmed"

NOT_APPLICABLE:
  dry_cows:
    reason: "Different pathogens, different antibiotics, different goals"
    action: "USE_DRY_COW_MASTITIS_PROTOCOL"
    
  heifers_pre_calving:
    reason: "No mammary gland lactation, different anatomy"
    action: "USE_HEIFER_PROTOCOL"
    
  non_mammary_infection:
    examples: [udder_edema, hematoma, abscess]
    reason: "Not mastitis — requires different diagnosis"
```

### Soft Limits (Требуют адаптации)

```yaml
ORGANIC_FARM:
  restriction: "Withdrawal times, antibiotic restrictions"
  adjustment: "Emphasize prevention, homeopathy per policy, extended milk discard"

HIGH_SCC_PREMIUM_MARKET:
  note: "Penalties are severe"
  adjustment: "Lower threshold for treatment, aggressive culling of chronic cows"

AUTOMATED_MILKING:
  advantage: "AMR provides SCC and conductivity data automatically"
  adjustment: "Integrate AMR alerts into rule triggers"
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
design: "Prospective before/after or cohort"

metrics:
  primary:
    - cure_rate: "% clinical cure by day 7-14"
    - culture_compliance: "% cases with pre-treatment sample"
    - unnecessary_treatment_reduction: "% gram-negative cases NOT treated with antibiotic"
  secondary:
    - scc_reduction: "30-day post-treatment SCC trend"
    - milk_discard_days: "Total per case"
    - culling_accuracy: "% chronic cows correctly identified"
    - resistance_pattern: "Change in pathogen susceptibility over time"
    
success_criteria:
  - culture_compliance: "> 80%"
  - cure_rate_improvement: "> 10% vs baseline"
  - unnecessary_treatment_reduction: "> 20% of gram-negatives spared"
  - scc_stabilization: "No increase in bulk tank SCC"
```

---

## RULE METRICS

### Outcome Registration

```yaml
outcome_record:
  timestamp: "YYYY-MM-DD HH:MM"
  farm_id: "FARM-XXX"
  cow_id: "COW-XXXXX"
  quarter: "LF / RF / LR / RR"
  
  input_data:
    clinical_signs: [clots, watery_milk, swelling]
    scc: 850000
    cmt_score: 3
    dim: 45
    cases_this_lactation: 2
    
  treatment:
    culture_taken: true
    pathogen: "Staphylococcus aureus"
    antibiotic: "Cloxacillin IM"
    duration_days: 5
    
  actual_outcome:
    clinical_cure: true
    scc_day_14: 120000
    milk_returned_to_tank: "Day 8"
    
  classification: "TP"
  root_cause: null
```

### Root Cause Categories

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| **missed_culture** | **P1** | Не взяли пробу перед лечением | Невозможно переключить терапию |
| **wrong_antibiotic** | **P1** | Резистентность или неверный спектр | S. aureus не чувствителен к первой линии |
| **milking_hygiene** | **P2** | Загрязнённые соски / оборудование | Повторные случаи у доярок |
| **environmental_contamination** | **P2** | Грязные стойла / подстилка | Колiforms в пробе |
| **chronic_carrier** | **P3** | Корова хронически инфицирована | SCC > 400k 60+ дней |

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-04-15 | Создано на основе mastitis treatment guidelines и SCC management principles | StanisSerg |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **No local culture capability** | Common | High | Blind treatment becomes default | Train staff or use on-farm CMT |
| **Delayed diagnosis** | Common | Medium | Mild becomes chronic | AMR/conductivity alerts |
| **Pathogen variation by farm** | Known | Medium | Culture results needed per farm | Periodic bulk tank culture |
| **Organic restrictions** | Regulatory | Low | Limits antibiotic choice | Prevention focus |

### Acceptable Error Bounds

Target (post-validation):
- False positive (treat non-infected): < 15%
- False negative (miss clinical case): < 5%
- Cure rate gram-positive: > 85%
- Unnecessary antibiotic for gram-negative: < 10%

---

## Execution Framework

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - dim
    - quarter_affected
    - clinical_signs
    - scc
    - cmt_score
    - udder_swelling
    - systemic_illness
    - cases_this_lactation
    - culture_result
    - pathogen_if_known
    
  prediction:
    severity: "MILD / MODERATE / SEVERE"
    recommendation: "TREAT / CULTURE_FIRST / CULL_CANDIDATE / EMERGENCY"
    expected_cure_probability: "qualitative"
    
  outcome:
    clinical_cure: true/false
    scc_day_14: "int"
    milk_returned_day: "int"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
```

---

## RELATIONSHIPS

### В портфеле здоровья

```
┌─────────────────────────────────────────────────────────────────┐
│                    UDDER HEALTH ZONE                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PREVENTION                                                     │
│  ├── RULE-015: Milk Quality / SCC Management (herd level)      │
│  └── Milking hygiene protocols                                  │
│                                                                 │
│  INDIVIDUAL CASE                                                │
│  └── RULE-011: Mastitis Protocol  ← THIS RULE                  │
│       │  ← Treat vs. culture vs. cull decision                 │
│       │                                                         │
│  CONSEQUENCES                                                   │
│       ├──► RULE-010: Culling Decision (if chronic/recurrent)   │
│       └──► RULE-009: Lameness (if altered gait from udder pain)│
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Boundary Conditions with Other Rules

| Rule | Boundary | Coordination |
|------|----------|--------------|
| RULE-010 | Chronic mastitis → cull | RULE-011 identifies chronic candidates, RULE-010 makes economic decision |
| RULE-009 | Severe mastitis causes guarded gait | Do not double-count as lameness unless independent hoof pathology |
| RULE-006 | Postpartum metritis + mastitis common | Treat both simultaneously, do not delay antibiotics for either |
| RULE-008 | Heat stress depresses immunity | High THI + mastitis = more aggressive therapy |

---

*Framework: Execution Framework v4.0*
