---
rule_id: RULE-008
dl_ref: DL-008
case_refs: []
date_created: 2026-04-15
date_updated: 2026-04-15
author: StanisSerg
category: environmental
tags: [heat-stress, thi, temperature, humidity, dmi, milk-yield, cooling]

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

# RULE-008: Heat-Stress-Intervention

> **Тип:** executable decision operator — environmental management  
> **Maturity:** conceptual (v1.0)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-008  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: environmental, фаза: lactation

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:
  - condition: "THI above threshold"
    thi: "> 68"
    note: "Mild heat stress begins >68; severe >72"

soft_conditions:
  - condition: "Severe heat stress"
    criteria: "THI > 72"
    weight: 1

  - condition: "Concurrent DMI drop"
    criteria: "DMI ratio < 0.9 vs baseline"
    weight: 1

  - condition: "Milk yield drop"
    criteria: "Current yield >10% below 3-day average"
    weight: 1

  - condition: "High-producing cow"
    criteria: "> 35L/day"
    weight: 1

  - condition: "Inadequate cooling infrastructure"
    criteria: "No fans OR no soakers OR poor barn ventilation"
    weight: 1

blocking_conditions:
  - condition: "Already implementing full cooling protocol"
    check: "All cooling measures active and THI still rising"
    action: "ESCALATE_TO_ENGINEERING_REVIEW"
```

### Verdict Logic

```
INITIAL ──► THI > 68?
              │
              NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        evaluate_soft_score ──► HIGH / MEDIUM / LOW
```

**Verdict Types:**
- `RULE_008_BLOCKED`: Охлаждение уже максимально — проблема инфраструктуры
- `RULE_008_NOT_APPLICABLE`: THI в норме
- `RULE_008_HIGH_RISK`: THI>72 + DMI↓ + milk↓ (3+ soft)
- `RULE_008_MEDIUM_RISK`: THI>68 + 1-2 soft фактора
- `RULE_008_LOW_RISK`: THI>68, но без других признаков

---

## STATE MACHINE

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| HIGH_RISK | CRITICAL | Full cooling protocol + ration adjustments | Immediate |
| MEDIUM_RISK | HIGH | Enhanced cooling + monitor DMI | 0-4 hours |
| LOW_RISK | WARNING | Preventive cooling activation | Same day |

---

## ACTION PROTOCOL

### При RULE_008_HIGH_RISK

```yaml
priority: 1
cooling_measures:
  - soakers: "Cycle: 3 min on / 12 min off during day"
  - fans: "All holding area and feedbunk fans ON"
  - shade: "Verify pasture shade or keep indoors"
  - night_cooling: "Maximize night ventilation"
  
ration_adjustments:
  - increase_energy_density: "Add fat bypass if DMI depressed"
  - increase_minerals: "K, Na, Mg supplementation"
  - shift_feeding: "70% of ration at night"
  - water: "Ensure clean, cool water (<20°C), unlimited"

monitoring:
  - dmi: "Track vs pre-heat baseline"
  - respiration_rate: "Target <60 breaths/min"
  - milk_yield: "Daily"
  - rectal_temp: "Spot-check high-risk cows"
```

### При RULE_008_MEDIUM_RISK

```yaml
priority: 2
cooling_measures:
  - fans: "ON during peak heat hours"
  - soakers: "Activate if available"
  - check_water: "All troughs functional"

monitoring:
  - respiration_rate: "2x daily sample"
  - dmi: "Daily"
```

---

## BECAUSE (Механизм)

```
THI > 68 ──► Тепловой стресс
       │
       ├──► ↓ DMI (корова избегает метаболического тепла)
       ├──► ↑ дыхание (панты) ──► pH дыхательный алкалоз
       ├──► ↓ молоко (энергия уходит на терморегуляцию)
       └──► ↓ репродукция (эмбриональная смертность)

Интервенция дешевле потерь:
  • Потери молока: -2 до -5 L/день/корова
  • Снижение концепции: -10 до -20%
  • Клинический кетоз: +2-3x риск
```

### Экономическая логика

```yaml
scenario_no_intervention_thi_72:
  milk_loss: "4L/day × 30 days × 40₽ = 4800₽"
  reproduction_delay: "5000₽"
  ketosis_risk_increase: "+1500₽ expected cost"
  total: "11300₽"

scenario_rule_008_intervention:
  electricity_water: "+300₽"
  ration_adjustment: "+400₽"
  labor: "+200₽"
  total: "900₽"
  
  effectiveness:
    milk_loss_reduction: "~70%"
    reproduction_preserved: "Near baseline"
    
  net_savings: "10400₽"
  roi: "+1150%"
  
economic_verdict: "HIGHLY_COST_EFFECTIVE"
```

---

## LIMITS

```yaml
APPLICABLE:
  season: "Warm months or climate-controlled barns year-round"
  species: "Dairy cattle"
  
NOT_APPLICABLE:
  cold_climate:
    thi: "< 60 consistently"
    reason: "No heat stress risk"
  
  no_cooling_capacity:
    note: "Pasture-based with no infrastructure"
    action: "SHIFT_TO_NIGHT_GRAZING_AND_ADAPT_RATION"
```

---

## VALIDATION

```yaml
minimum_cases: 10
farms_required: 3
metrics:
  primary:
    - dmi_maintenance: "% of baseline DMI maintained"
    - milk_yield_drop: "L/day vs pre-heat baseline"
  secondary:
    - respiration_rate_compliance: "% cows <60 bpm"
    - water_consumption: "L/day per cow"
    - reproduction_impact: "Conception rate during heat stress period"
```

---

## Execution Framework

```yaml
structured_capture:
  CASE-INPUT:
    - farm_id
    - cow_id
    - date
    - thi
    - temperature_c
    - humidity_pct
    - dmi_actual
    - dmi_baseline
    - milk_yield_current
    - milk_yield_baseline
    - cooling_fans_available
    - cooling_soak_available
    
  prediction:
    risk_level: "LOW / MEDIUM / HIGH"
    expected_milk_loss: "L/day"
    
  outcome:
    dmi_maintained: true/false
    milk_drop_actual: "L/day"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
```

---

*Framework: Execution Framework v4.0*
