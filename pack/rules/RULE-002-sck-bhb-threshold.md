---
rule_id: RULE-002
dl_ref: DL-002
case_refs: []  # Требуется валидация
date_created: 2026-04-11
date_updated: 2026-04-11
author: StanisSerg
category: metabolic
tags: [ketosis, bhb, threshold, diagnosis, sck, transition-period, screening]

# RULE STATE
rule_version: "4.0"
rule_maturity: conceptual  # Основано на Chapinal 2011, но требует валидации
status: conceptual
trend: stable

# Временные метки
last_trigger: null
last_error: null
last_review: 2026-04-11
next_review: 2026-07-11

# Управляемый актив
metrics_enabled: false
confidence: low  # SoTA-based, но без собственной валидации

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

# RULE-002: SCK-BHB-Threshold

> **Тип:** executable decision operator — diagnostic screening  
> **Maturity:** conceptual (v4.0) — основано на Chapinal 2011, требует валидации  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-002  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: metabolic  
> **SoTA:** CS.SOTA.071 (Chapinal), CS.SOTA.054 (Horst), CS.SOTA.055 (Drackley)

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:  # ALL must be TRUE
  - condition: "BHB plasma/serum"
    threshold: ">= 1.2"
    unit: "mmol/L"
    operator: ">="
    
  - condition: "DIM"
    threshold: "3-14"
    unit: "days"
    operator: "in_range"
    
  - condition: "No clinical ketosis signs"
    check: "acetone_breath == false AND ataxia == false"
    
soft_conditions:  # 0-2 for confidence level
  - condition: "NEFA elevated"
    threshold: ">= 0.7"
    unit: "mEq/L"
    weight: 1
    note: "Strong predictor per Chapinal"
    
  - condition: "BCS loss"
    threshold: "> 0.5"
    unit: "points in 30 days"
    weight: 1
    
  - condition: "DMI deficit"
    threshold: "< 80%"
    unit: "of norm"
    weight: 1

blocking_conditions:  # IF TRUE → RULE_BLOCKED
  - condition: "Clinical ketosis signs present"
    signs: [acetone_breath, ataxia, hypersalivation, severe_depression]
    action: "REFER_TO_CLINICAL_KETOSIS_PROTOCOL"
```

### Verdict Logic

```
INITIAL ──► clinical_signs? ──► BLOCKED
              │
              NO
              │
              ▼
        hard_met? ──► NO ──► NOT_TRIGGERED
              │
              YES
              │
              ▼
        soft_score ──► TRIGGERED (LOW/MEDIUM/HIGH)
              │
              ▼
        ACTION: Screen for SCK + check inflammation
```

**Verdict Types (Rule-002 specific language):**

```yaml
verdict_states:
  - RULE_002_BLOCKED
  - RULE_002_NOT_TRIGGERED
  - RULE_002_GRAY_ZONE
  - RULE_002_TRIGGERED_LOW
  - RULE_002_TRIGGERED_MEDIUM
  - RULE_002_TRIGGERED_HIGH
  
RULE_002_BLOCKED:
  trigger: "clinical_signs present"
  meaning: "Not SCK — clinical ketosis"
  action: "REFER_TO_CLINICAL_KETOSIS_PROTOCOL"
  confidence: N/A

RULE_002_NOT_TRIGGERED:
  trigger: "hard conditions not met"
  meaning: "No SCK detected"
  action: "CONTINUE_MONITORING"
  confidence: LOW

RULE_002_GRAY_ZONE:
  trigger: "BHB 1.0-1.2 mmol/L"
  meaning: "Uncertain — insufficient confidence"
  action: "REPEAT_BHB_IN_3_5_DAYS"
  confidence: LOW
  note: "Explicit state for uncertainty, not forced binary"

RULE_002_TRIGGERED_LOW:
  trigger: "hard met, soft = 0"
  meaning: "SCK possible (BHB≥1.2)"
  action: "SCREEN_FOR_SCK"
  confidence: LOW

RULE_002_TRIGGERED_MEDIUM:
  trigger: "hard met, soft = 1"
  meaning: "SCK likely"
  action: "START_SCK_PROTOCOL"
  confidence: MEDIUM

RULE_002_TRIGGERED_HIGH:
  trigger: "hard met, soft ≥ 2"
  meaning: "SCK confirmed"
  action: "START_SCK_PROTOCOL + CHECK_INFLAMMATION"
  confidence: HIGH
```

---

## STATE MACHINE

```
                    ┌─────────────────────────────────────┐
                    │         INITIAL (начало)            │
                    └─────────────────┬───────────────────┘
                                      │
                    clinical_signs?   │
                    ┌──────────────┐  │  ┌──────────────┐
           YES ────►│   BLOCKED    │  │  │   EVALUATE   │◄──── NO
                    │              │  │  │   hard/soft  │
                    │ Клинический  │  │  │              │
                    │ протокол     │  │  └──────┬───────┘
                    └──────────────┘  │         │
                                       │    hard_met?
                                       │    ┌──────────┐
                                       │NO  │ NOT_TRIG │
                                       │    │ GERED    │
                                       │    └──────────┘
                                       │
                         ┌─────────────┼─────────────┐
                         │             │             │
                    soft=2│        soft=1│        soft=0│
                         │             │             │
                         ▼             ▼             ▼
                    ┌─────────┐  ┌─────────┐  ┌─────────┐
                    │ TRIGGERED│  │ TRIGGERED│  │ TRIGGERED│
                    │  HIGH    │  │  MEDIUM  │  │   LOW    │
                    └────┬────┘  └────┬────┘  └────┬────┘
                         │             │             │
                         └─────────────┴─────────────┘
                                       │
                                       ▼
                         ┌─────────────────────────────┐
                         │   SCK SCREENING +          │
                         │   INFLAMMATION CHECK        │
                         └─────────────────────────────┘
```

### State Definitions

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Клинический протокол кетоза | Немедленно |
| NOT_TRIGGERED | INFO | Мониторинг BHB через 7 дней | Обычный |
| TRIGGERED (LOW) | WARNING | SCK screening, check ration | 48 часов |
| TRIGGERED (MEDIUM) | HIGH | SCK confirmed, start PG protocol | 24 часа |
| TRIGGERED (HIGH) | HIGH | SCK confirmed + inflammation check | Немедленно |

---

## ACTION PROTOCOL

### При RULE_002_TRIGGERED

**Step 1: Диагностика (Diagnostics)**
```yaml
action: CONFIRM_SCK_AND_SCREEN_INFLAMMATION
target: Subclinical ketosis
reason: "BHB≥1.2 + DIM 3-14 + no clinical signs = SCK per Chapinal 2011"

substeps:
  - verify: "BHB measurement method (plasma/serum vs milk)"
  - check: "DIM calculation correct"
  - screen: "Inflammation markers (haptoglobin, albumin)"
  - evaluate: "NEFA if available (strong predictor)"
```

**Step 2: Интервенция (Intervention)**
```yaml
priority: 1
condition: "SCK confirmed (any confidence level)"
action: START_PROPGLYCOL_PROTOCOL
reference: "RULE-003"

details:
  - Propylene glycol 300 ml/day × 3-5 days
  - OR Glycerol (alternative)
  - Monitor BHB in 5-7 days
```

**Step 3: Профилактика осложнений (Complication Prevention)**
```yaml
priority: 2
condition: "NEFA elevated OR soft_score >= 2"
actions:
  - assess_reproductive_risk: "OR=3.2 for metritis, OR=2.8 for mastitis"
  - monitor_uterine_involution: "Days 21-30"
  - track_first_service_conception: "Target >40%"
  
escalation: "If no improvement in 7 days → check secondary causes"
```

**Step 4: Мониторинг (Monitoring)**
```yaml
metrics:
  - BHB: repeat in 5-7 days
  - NEFA: if available, day 7-10
  - Milk yield: daily tracking
  - Reproduction: first service conception
  
timeline: 30 days
success_criteria:
  - BHB: < 1.2 mmol/L
  - No clinical ketosis development
  - Normal reproductive performance
```

---

## BECAUSE (Механизм)

### Научное обоснование

```
Chapinal et al. 2011 (JDS, n=100 cows, 4 farms):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINDING:
  BHB ≥1.2 mmol/L at 7 DIM → OR=4.5 для клинического кетоза
  
OPTIMAL THRESHOLD:
  1.2 mmol/L — баланс sensitivity/specificity
  
VALIDATION:
  • Ospina 2010 (meta-analysis): порог 1.2-1.4 mmol/L оптимален
  • McArt 2011 (field trial): скрининг на 7 DIM эффективен

Horst et al. 2021 (paradigm shift):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KEY INSIGHT:
  BHB — маркёр, не причина
  
DUAL ROLE:
  1. Diagnostic marker (valid) ✓
  2. Causal factor (overrated) ✗
  
CRITICAL DISTINCTION:
  High BHB reflects:
    a) Normal adaptation (acceptable)
    b) Inflammation→hypophagia (requires intervention)
  
  → Always check inflammation status
```

### Экономическая логика

```yaml
scenario_no_screening:
  description: "SCK progresses to clinical ketosis undetected"
  costs:
    clinical_ketosis_treatment: 8000
    milk_loss: 15000
    reproduction_delay: 5000
  total_cost: 28000
  roi: -100%
  
scenario_rule_002_screening:
  description: "Early SCK detection + PG protocol"
  costs:
    bhb_testing: 200
    pg_protocol: 1500
    monitoring: 500
  total_cost: 2200
  
  outcome:
    prevented_clinical: "80% of cases"
    saved_costs: 28000 × 0.8 = 22400
    
  roi: +918%
  economic_verdict: HIGHLY_EFFICIENT
  
comparison:
  delta_roi: "+1018%"
  cost_per_case_prevented: 2200 / 0.8 = 2750
  break_even: "1 prevented clinical case per 12.7 screened"
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  breed: Holstein
  productivity: ">30 L/day"
  housing: [tie_stall, free_stall]
  dim_range: [3, 14]
  bhb_source: [plasma, serum]
  
NOT_APPLICABLE:
  clinical_ketosis:
    signs: [acetone_breath, ataxia, hypersalivation]
    action: RULE_BLOCKED → Clinical Ketosis Protocol
    
  late_lactation:
    dim: ">30 days"
    mechanism: "Different pathophysiology"
    
  jersey_cows:
    reason: "More ketosis-sensitive, different threshold may apply"
    action: "Use with caution, consider BHB ≥1.0 threshold"
    
  low_productivity:
    milk_yield: "<20 L/day"
    reason: "Different metabolism"
```

### Soft Limits (Требуют адаптации)

```yaml
GRAY_ZONE:
  bhb_range: [1.0, 1.2]
  action: "Monitor closely, repeat in 3-5 days"
  
SEVERE_SCK:
  bhb: ">3.0 mmol/L"
  action: "Near clinical, aggressive intervention"
  
CONCURRENT_DISEASE:
  conditions: [metritis, mastitis, retained_placenta]
  action: "Combined therapy approach"
  note: "SCK may be secondary to inflammation"
  
MILK_BHB:
  note: "Milk BHB ~0.8× Plasma BHB"
  adjustment: "Use threshold ~1.4-1.5 mmol/L for milk"
```

---

## VALIDATION

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| — | — | — | — | Нет собственной валидации | **LOW** |

**Note:** Confidence LOW потому что нет собственных кейсов. Правило основано на SoTA (Chapinal 2011 — HIGH evidence), но требует валидации в конкретных условиях.

### Required Validation

```yaml
minimum_cases: 10
farms_required: 3
distribution:
  - success_cases: "≥5 (SCK detected, PG effective)"
  - failure_cases: "≥2 (SCK → clinical despite intervention)"
  - false_positive: "≥2 (BHB≥1.2 but normal adaptation)"
  
metrics_to_track:
  - ppv: "Positive Predictive Value (how many BHB≥1.2 truly SCK)"
  - npv: "Negative Predictive Value"
  - sensitivity_at_1.2: "vs BHB≥1.4 as gold standard"
```

---

## RULE METRICS

### Outcome Registration

```yaml
outcome_record:
  timestamp: "YYYY-MM-DD HH:MM"
  farm_id: "FARM-XXX"
  cow_id: "COW-XXXXX"
  
  input_data:
    bhb_mmol_l: 1.4
    dim: 7
    clinical_signs: false
    nefa_meq_l: 0.8
    
  prediction:
    verdict: "RULE_002_TRIGGERED_HIGH"
    confidence: "HIGH"
    action: "SCK_SCREENING_PG_PROTOCOL"
    
  actual_outcome:
    bhb_day_7: 0.9
    clinical_ketosis_developed: false
    pg_protocol_completed: true
    milk_yield_change: "+2 L/day"
    
  classification: "TP"  # TP / FP / FN
  root_cause: null
```

### Root Cause Categories (для ошибок)

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| **threshold_issue** | **P1** | Порог неверен | BHB 1.0-1.2 gray zone cases |
| **data_quality** | **P1** | Проблемы с данными | Milk BHB vs Plasma BHB confusion |
| **missing_variable** | **P2** | Не хватает переменной | NEFA not measured |
| **temporal_issue** | **P2** | Проблема времени | BHB measured at wrong DIM |
| **acceptable_noise** | **P3** | Нормальная адаптация | BHB 1.2-1.3 without issues |
| **unpredictable** | **P3** | Случайность | Rapid progression despite intervention |

### Action by Priority

```yaml
P1 (critical):
  threshold: "2+ threshold_issue OR data_quality errors"
  timeline: "24–48 часов"
  action: "Review BHB measurement protocols, clarify gray zone handling"
  
P2 (planned):
  threshold: "3+ missing_variable (NEFA not available)"
  timeline: "в ближайший scheduled review"
  action: "Add NEFA as optional input, assess without it"
  
P3 (no_action):
  threshold: "acceptable_noise (normal adaptation high BHB)"
  timeline: "не требует действия"
  action: "Document as normal variation, do not change threshold"
```

### Review Schedule

| Trigger | Action | Тип |
|---------|--------|-----|
| 10 triggers + 5 outcomes | Включить метрики, первый review | scheduled |
| 5+ threshold_issue errors | Пересмотр BHB порога | targeted |
| 3+ farms validated | Рассмотрение confidence upgrade | scheduled |
| Conflicts with RULE-001 | Cross-rule review | emergency |

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-04-11 | Создано на основе Chapinal 2011 + SoTA | StanisSerg |
| 4.0 | 2026-04-11 | Переписано под стандарт v4.0: Execution Framework, State Machine, Action Protocol, Economic Logic | StanisSerg |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **No own validation** | SoTA only | High | Over-reliance on literature | Validate locally |
| **Gray zone BHB 1.0-1.2** | Some evidence | Medium | Unclear action | Monitor closely |
| **Jersey breed** | Unknown | Medium | Different threshold | Use with caution |
| **Milk vs Plasma BHB** | Known difference | Medium | Misclassification | Use plasma preferred |
| **Concurrent inflammation** | Horst 2021 | Medium | May need different approach | Check haptoglobin |

### Acceptable Error Bounds

**Пока НЕ определены — требуется валидация.**

Target (post-validation):
- False Positive Rate (unnecessary PG): < 15%
- False Negative Rate (missed SCK): < 10%
- Sensitivity: > 85%
- Specificity: > 80%

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
    - bhb_mmol_l
    - dim
    - clinical_signs
    - nefa_meq_l (optional)
    - milk_yield
    
  derived_params:
    - bhb_category: "<1.0 / 1.0-1.2 / 1.2-1.4 / >1.4"
    
  prediction:
    verdict: "RULE_002_TRIGGERED_{LEVEL} / NOT_TRIGGERED / BLOCKED"
    confidence: "LOW / MEDIUM / HIGH"
    
  decision:
    pg_protocol_started: true/false
    inflammation_checked: true/false
    
  basis:
    rule: "RULE-002"
    conditions: ["BHB>=1.2", "DIM 3-14", "no clinical signs"]
    
traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"
  
data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
  goal: "фиксация реальности, не автоматизация"
```

#### Validation Steps

1. Применить на 3+ фермах (Holstein, DIM 3-14)
2. Создать 10+ кейсов:
   - 5+ SCK detected + PG effective (TP)
   - 2+ SCK → clinical despite intervention (FN)
   - 2+ BHB≥1.2 but normal adaptation (FP)
3. Document outcomes (structured)
4. Calculate FP / FN rates
5. Define error bounds

```yaml
precision_recall_tradeoff:
  principle:
    - recall ↑ → больше FP (over-treatment)
    - precision ↑ → больше FN (missed cases)
    
  rule_002_priority:
    focus: "slightly recall-biased"
    reasoning: "Screening should catch most SCK; some over-treatment acceptable"
    target:
      precision: ">80%"
      recall: ">85%"
```

---

### Phase 2: Robustness (HIGH)

```yaml
actions:
  - analyze_error_patterns (≥5 ошибок)
  - root_cause_analysis
  - test_edge_cases:
      - BHB 1.0-1.2 (gray zone)
      - Jersey breed
      - Milk BHB vs Plasma
  - validate_with_inflammation_markers
  - validate_without_nefa

metrics_activation:
  conditions:
    - ≥10 triggers
    - ≥5 outcomes

review_triggers:
  - total_errors >= 5
  - same_root_cause >= 2
  - P1_error >= 1
```

---

### Phase 3: Full Automation (MEDIUM)

Только после Phase 1 + Phase 2

```yaml
components:
  - evaluate_rule_002()
  - auto_bhb_screening (DIM 3-14 trigger)
  - dashboard (SCK prevalence by farm)
  - alerts (HIGH confidence SCK)

readiness_criteria:
  - validation_complete: true
  - robustness_proven: true
  - errors_analyzed: true
  - ontology_stable: true
  - prediction_fact_traceable: true
```

---

### Phase 3.5: Rule Saturation (CRITICAL)

Обязательный этап перед ML

```yaml
saturation_criteria:
  rules_stable: ">=3–5"
  zones_defined: true
  conflicts_mapped: true
  decision_layer_clear: true

indicators:
  - REGISTRY.md populated
  - cross_rule_links defined
  - conflict_resolution tested
  
dependencies:
  - RULE-001: "What to do when BHB≥1.2 (intervention)"
  - RULE-003: "PG protocol details"
```

---

### Phase 4: ML (LOW)

```yaml
requirements:
  - ≥50 structured cases
  - error_patterns understood
  - ontology stable

potential_improvements:
  screening_layer:  # RULE-002 improvements
    - predict_bhb_trajectory: "Will BHB rise or fall without intervention?"
    - optimize_screening_timing: "Best DIM for one-time BHB check"
    - predict_screening_yield: "Which farms/groups benefit most?"
    
  decision_layer:  # RULE-001 improvements  
    - differentiate_adaptation_vs_deficit: "High BHB normal vs pathological"
    - predict_systemic_correction_response: "Who needs what intensity?"
    
  treatment_layer:  # RULE-003 improvements
    - optimize_pg_duration: "3 vs 5 days based on NEFA, BCS loss"
    - predict_non_responders: "Who needs alternative therapy?"
    - personalize_pg_dose: "By weight, BHB level, DIM"

steps:
  - feature_engineering (from errors)
  - train_classifier
  - validate vs rule_engine
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
stage: conceptual  # SoTA-based, requires validation
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
RULE-002 (this) ──► RULE-001 ──► RULE-003
   screening          intervention      treatment
   
Flow:
  1. RULE-002 detects SCK (BHB≥1.2, DIM 3-14)
  2. RULE-001 decides intervention (systemic correction)
  3. RULE-003 executes PG protocol
```

### Escalation / Override Logic

| Situation | Primary Rule | Logic |
|-----------|--------------|-------|
| RULE-002 detects SCK (BHB≥1.2) | RULE-002 | Initial screening — entrance to decision chain |
| RULE-001 identifies metabolic deficit | RULE-001 | Higher resolution override — RULE-002 is coarse filter |
| BHB≥1.2 + clinical signs | Clinical Protocol | RULE_002_BLOCKED — escalation to emergency |
| BHB 1.0-1.2 | RULE_002_GRAY_ZONE | Explicit uncertainty — no forced decision |
| BHB normal, but strong clinical suspicion | Clinical Protocol | RULE-002 does not override clinical judgment |

**Principle:**
```
RULE-002 (coarse screening) ──► RULE-001 (fine discrimination)
       BHB≥1.2                        Systemic correction needed?
       "Something wrong"               "What exactly to do"
```

This is not conflict — it's **hierarchical refinement**.

---

### Rule Role (в портфеле)

```yaml
rule_role:
  type: screening
  specificity: coarse
  layer: entrance
  handoff_to: RULE-001
  
  function: "Initial triage — detects potential SCK and routes to appropriate intervention"
  
  position_in_chain:
    - RULE-004 (prevention, prepartum)
    - RULE-002 (screening, postpartum) ← THIS RULE
    - RULE-001 (discrimination, intervention decision)
    - RULE-003 (treatment, execution)
    
  design_principle: "Catch most cases with simple criteria; let downstream rules refine"
```

---

*Framework: Execution Framework v4.0*  
*Format: CASE → DL → RULE (executable, managed)*  
*System Loop: CASE→PREDICTION→DECISION→FACT→ERROR→RULE→UPDATE→NEXT CASE*
