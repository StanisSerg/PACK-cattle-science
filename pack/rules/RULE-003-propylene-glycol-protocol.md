---
rule_id: RULE-003
dl_ref: DL-003
case_refs: []  # Требуется валидация
date_created: 2026-04-11
date_updated: 2026-04-11
author: StanisSerg
category: metabolic
tags: [ketosis, treatment, propylene-glycol, gluconeogenesis, therapy, sck]

# RULE STATE
rule_version: "4.0"
rule_maturity: conceptual  # SoTA-based, requires local validation
status: conceptual
trend: stable

# Временные метки
last_trigger: null
last_error: null
last_review: 2026-04-11
next_review: 2026-07-11

# Управляемый актив
metrics_enabled: false
confidence: low  # Based on literature (high), but no local validation

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

# RULE-003: Propylene-Glycol-Protocol

> **Тип:** executable decision operator — treatment protocol  
> **Maturity:** conceptual (v4.0) — основано на RCT (Duffield, McArt, Chapinal)  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** [DL-003](../../DS-cattle-operations/decisions/DL-003.md)  
> **Валидация:** Требуется  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: metabolic  
> **SoTA:** CS.SOTA.071, CS.SOTA.093, CS.SOTA.092, CS.SOTA.106

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:  # ALL must be TRUE
  - condition: "SCK diagnosis confirmed"
    criteria: "BHB 1.2-2.9 mmol/L"
    unit: "mmol/L"
    source: "plasma_or_serum"
    
  - condition: "Animal conscious"
    check: "no ataxia, no severe depression"
    
  - condition: "No contraindications"
    check: "see LIMITS → NOT_APPLICABLE"

soft_conditions:  # 0-2 for confidence level
  - condition: "Early detection"
    criteria: "DIM 3-14"
    weight: 1
    note: "Earlier treatment = better response"
    
  - condition: "No concurrent severe metritis"
    check: "uterine discharge normal or mild"
    weight: 1
    
  - condition: "Proper administration possible"
    check: "animal eating, can receive oral treatment"
    weight: 1

blocking_conditions:  # IF TRUE → RULE_BLOCKED
  - condition: "Clinical ketosis"
    signs: [severe_ataxia, recumbency, coma]
    action: "REFER_TO_CLINICAL_KETOSIS_EMERGENCY_PROTOCOL"
    
  - condition: "Severe hepatic lipidosis"
    criteria: "AST >500 U/L or bilirubin >50 μmol/L"
    action: "REFER_TO_VETERINARY_DIAGNOSTIC_WORKUP"
    
  - condition: "Complete anorexia >48h"
    action: "REFER_TO_PARENTERAL_THERAPY"
```

### Verdict Logic

```
INITIAL ──► contraindications? ──► BLOCKED
              │
              NO
              │
              ▼
        hard_met? ──► NO ──► NOT_APPLICABLE
              │
              YES
              │
              ▼
        soft_score ──► RECOMMENDED (LOW/MEDIUM/HIGH)
              │
              ▼
        ACTION: Start PG Protocol
```

**Verdict Types:**
- `RULE_003_BLOCKED`: Противопоказания — другой протокол
- `RULE_003_NOT_APPLICABLE`: Не подходит для PG (например, клинический кетоз)
- `RULE_003_RECOMMENDED_HIGH`: Оптимальные условия (2-3 soft)
- `RULE_003_RECOMMENDED_MEDIUM`: Хорошие условия (1 soft)
- `RULE_003_RECOMMENDED_LOW`: PG возможен но риск неуспеха (0 soft)

---

## STATE MACHINE

```
                    ┌─────────────────────────────────────┐
                    │         INITIAL (начало)            │
                    └─────────────────┬───────────────────┘
                                      │
                    contraindications?│
                    ┌──────────────┐  │  ┌──────────────┐
           YES ────►│   BLOCKED    │  │  │   EVALUATE   │◄──── NO
                    │              │  │  │   hard/soft  │
                    │ Другой       │  │  │              │
                    │ протокол     │  │  └──────┬───────┘
                    └──────────────┘  │         │
                                       │    hard_met?
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
                         │   START PG PROTOCOL         │
                         │   300 ml/day × 3-5 days     │
                         └─────────────────────────────┘
```

### State Definitions

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Экстренная терапия | Немедленно |
| NOT_APPLICABLE | WARNING | Альтернативное лечение | 24 часа |
| RECOMMENDED (LOW) | INFO | PG с осторожностью, усиленный мониторинг | 48 часов |
| RECOMMENDED (MEDIUM) | INFO | PG стандартный протокол | 24 часа |
| RECOMMENDED (HIGH) | INFO | PG оптимальный протокол | 24 часа |

---

## ACTION PROTOCOL

### При RULE_003_RECOMMENDED

**Step 1: Подготовка (Preparation)**
```yaml
action: VERIFY_PG_ADMINISTRATION_FEASIBLE
substeps:
  - check: "Animal can swallow"
  - check: "No severe nausea/vomiting risk"
  - prepare: "300 ml propylene glycol (food grade)"
  - prepare: "Dosing equipment (syringe, oral drench)"
  
contraindication_check:
  - liver_function: "AST <500, bilirubin <50"
  - renal_function: "not severely compromised"
  - hydration: "adequate (can be supplemented)"
```

**Step 2: Администрация (Administration)**
```yaml
priority: 1
dosage:
  amount: "300 ml/day"
  frequency: "2 times daily (150 ml AM, 150 ml PM)"
  duration: "3-5 days standard"
  extension: "Up to 7 days if BHB >2.0 or rebound"
  
route:
  primary: "Oral (per os)"
  method: "Via oral drench gun or mixed with palatable feed"
  
forbidden_routes:
  - IV: "Ineffective, risk of hemolysis"
  - Rumen: "Fermentation, unpredictable absorption"
  - SC: "Poor absorption, tissue irritation"
  
timing:
  - avoid: "Immediately before/after large meal"
  - best: "2-3 hours after feeding"
```

**Step 3: Мониторинг (Monitoring)**
```yaml
priority: 2
metrics:
  daily:
    - appetite: "DMI estimation"
    - attitude: "alertness, activity"
    - feces: "consistency (PG may cause loose stool)"
    
  day_3:
    - bhb: "If available, check trend"
    
  day_5_or_end:
    - bhb: "Must be <1.2 mmol/L"
    - milk_yield: "Compare to baseline"
    
  day_7_if_extended:
    - full_panel: "BHB, NEFA if available"
    
success_criteria:
  - BHB: "<1.2 mmol/L by day 5-7"
  - Appetite: "Normal or improving"
  - Milk: "Stable or increasing"
  
failure_indicators:
  - BHB: ">1.4 mmol/L at day 5"
  - Appetite: "Declining"
  - Rebound: "BHB dropped then rose again"
  action_on_failure: "Extend to 7 days OR consider alternative therapy"
```

**Step 4: Оценка результата (Outcome Assessment)**
```yaml
priority: 3
timeline: "Day 5-7 post-treatment"

classification:
  success:
    criteria:
      - "BHB <1.2 mmol/L"
      - "DMI >90% of norm"
      - "No clinical ketosis developed"
    outcome: "TP (True Positive)"
    
  partial_success:
    criteria:
      - "BHB 1.2-1.4 mmol/L (improved but not normalized)"
      - "Clinical status stable"
    action: "Extend to 7 days OR add supportive therapy"
    
  failure:
    criteria:
      - "BHB >1.4 mmol/L or rising"
      - "Clinical ketosis developed"
      - "Severe anorexia"
    outcome: "FN (False Negative - protocol failed)"
    action: "Escalate to veterinary intervention"
    root_cause_analysis: "Required"
```

---

## BECAUSE (Механизм)

### Научное обоснование

```
Механизм действия пропиленгликоля (PG):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. БЫСТРЫЙ ЭНЕРГЕТИЧЕСКИЙ СУБСТРАТ
   PG ──► Печень ──► Глюкоза (глюконеогенез)
   
   • Абсорбция: 50-70% через 30 минут
   • Пик глюкозы: 2-4 часа после приёма
   • Эффект: немедленная энергия для ЦНС

2. ПРЕКУРСОР ГЛЮКОЗЫ
   PG ──► Propionate ──► Глюкоза
   
   • Эффективность: 1 моль PG → 1 моль глюкозы
   • Контраст: глицерол менее эффективен (1→0.5)

3. ИНГИБИРОВАНИЕ ЛИПОЛИЗА (вторичный эффект)
   Глюкоза ↑ ──► Инсулин ↑ ──► NEFA мобилизация ↓
   
   • Улучшает энергетический баланс
   • Снижает нагрузку на печень

Эффективность (RCT Evidence):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Duffield et al. 1998, 2009:
  • PG 300 мл/день × 5 дней → BHB снижается на 35-45%
  • Уменьшение риска клинического кетоза на 50%
  
McArt et al. 2011:
  • Скрининг + PG → снижение удалений на 25%
  
Chapinal et al. 2011:
  • PG эффективен при BHB 1.2-2.5
  • При BHB >3.0 эффективность снижается (нужно комбинировать)

Фармакокинетика:
━━━━━━━━━━━━━━━━
• Период полувыведения: 2-4 часа
• Почти полная абсорбция в рубце (но не рубцовое введение!)
• Метаболизм: 90% в печени → глюкоза
• Выведение: почки ( unchanged <5%)
```

### Экономическая логика

```yaml
scenario_no_pg:
  description: "SCK без лечения → прогрессия к клиническому"
  probability_progression: "30-40%"
  costs_if_progresses:
    clinical_treatment: 8000
    milk_loss: 15000
    reproduction_delay: 5000
    risk_culling: 10000
  expected_cost: "38000 × 0.35 = 13300"
  
scenario_pg_protocol:
  description: "SCK + PG 300 мл × 5 дней"
  costs:
    pg_15_liters: 1200
    labor_administration: 800
    monitoring_bhb: 400
  total_cost: 2400
  
  effectiveness:
    success_rate: "70-75%"
    prevented_progression: "70%"
    
  savings:
    prevented_costs: "13300 × 0.70 = 9310"
    net_benefit: "9310 - 2400 = 6910"
    
  roi: "+288%"
  
comparison:
  cost_per_success: "2400 / 0.72 = 3333₽"
  cost_per_prevented_clinical: "2400 / 0.25 = 9600₽"
  break_even: "Предотвращение 1 клинического случая на 4 протокола"
  
  economic_verdict: "HIGHLY_COST_EFFECTIVE"
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  diagnosis: "SCK confirmed (BHB 1.2-2.9)"
  consciousness: "Alert, no severe ataxia"
  route_feasible: "Can receive oral treatment"
  liver_function: "AST <500 U/L"
  
NOT_APPLICABLE:
  clinical_ketosis_severe:
    signs: [recumbency, coma, severe_ataxia]
    reason: "PG недостаточно быстрый, требуется в/в глюкоза"
    action: "EMERGENCY_CLINICAL_PROTOCOL"
    
  complete_anorexia_48h:
    reason: "Невозможно пероральное введение"
    action: "PARENTERAL_GLUCOSE_PROTOCOL"
    
  severe_hepatic_lipidosis:
    criteria: "AST >500 (provisional, validate locally) OR bilirubin >50 OR hepatic encephalopathy"
    reason: "Печень не справится с метаболизмом PG"
    action: "SPECIALIZED_VETERINARY_CARE"
    note: "AST threshold requires local validation"
    
  suspected_renal_failure:
    criteria: "Creatinine >300 μmol/L OR urea >25 mmol/L with oliguria/anuria"
    reason: "Нарушена экскреция метаболитов PG"
    action: "MODIFIED_PROTOCOL with veterinary supervision"
    
  rumen_acidosis:
    reason: "PG усугубит ацидоз"
    action: "TREAT_ACIDOSIS_FIRST"
```

### Soft Limits (Требуют адаптации)

```yaml
BHB_2.5_2.9:
  description: "Верхняя граница эффективности PG"
  adjustment: "Consider extending to 7 days OR adding glycerol"
  
BHB_3.0_plus:
  description: "За пределами SCK (severe)"
  adjustment: "PG может быть поддержкой, но не основная терапия"
  
concurrent_metritis_moderate:
  description: "Сопутствующий метрит средней тяжести"
  adjustment: "PG effective, but also treat metritis"
  
jersey_cows:
  description: "Более чувствительны к PG"
  adjustment: "May reduce dose to 250 ml if loose stool occurs"
  
repeat_treatment:
  description: "Повторный курс PG"
  adjustment: "Acceptable, but investigate underlying cause if >2 courses per lactation"
```

---

## VALIDATION

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| — | — | — | — | Нет собственной валидации | **LOW** |

**Note:** RULE-003 основан на сильной RCT-эвиденсности (Duffield, McArt), но требует валидации:
- Эффективность в локальных условиях
- Приверженность протоколу (compliance)
- Фактические затраты на PG

### Required Validation

```yaml
minimum_cases: 10
farms_required: 3
distribution:
  goal: "Create ≥10 cases with full outcome capture"
  types: ["success", "partial_response", "failure"]
  
metrics_to_track:
  - response_rate: "% with BHB <1.2 at day 5 (target: >70%)"
  - time_to_response: "Day when BHB first <1.2"
  - rebound_rate: "% with BHB rise after stopping PG (target: <20%)"
  - compliance: "% of prescribed doses actually given (target: >85%)"
```

### Success Criteria & Failure Response

```yaml
success_criteria:
  primary:
    - bhb_normalized: "< 1.2 mmol/L within 3-5 days"
    - appetite_maintained: "DMI ≥ 80% of norm"
    - no_progression: "No clinical ketosis developed"
    
  secondary:
    - milk_yield: "Stable or increasing by day 7"
    - attitude: "Alert, mobile, responsive"
    
  economic:
    - cost_per_case: "< 3500₽"
    - roi: "> 200%"

failure_response:  # Что делать если PG не сработал
  trigger: "BHB > 1.4 at day 5 OR clinical ketosis developed"
  
  immediate_actions:
    - extend_protocol: "7 days total (if BHB improving but > 1.2)"
    - reassess_diagnosis: "Check for underlying disease (metritis, mastitis)"
    - verify_compliance: "Confirm all doses were given correctly"
    
  escalation_path:
    - step_1: "Review by RULE-001 — is metabolic deficit severe?"
    - step_2: "Add glycerol OR increase PG to 400 ml/day"
    - step_3: "Consider IV glucose if oral intake poor"
    - step_4: "Veterinary intervention if no response"
    
  root_cause_analysis:
    - compliance_check: "Were all 10 doses given?"
    - timing_check: "Was PG started early enough (DIM 3-14 optimal)?"
    - underlying_disease: "Concurrent infection/inflammation?"
    - severity_assessment: "Was it severe SCK (BHB > 2.5) from start?"
    
  documentation_required:
    - classify_as: "FN (False Negative — protocol failed)"
    - record_root_cause: "For rule improvement"
    - update_statistics: "Response rate tracking"
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
    bhb_mmol_l: 1.8
    dim: 9
    ast_u_l: 120
    concurrent_disease: "none"
    
  prediction:
    verdict: "RULE_003_RECOMMENDED_HIGH"
    confidence: "HIGH"
    action: "PG_PROTOCOL_5_DAYS"
    
  actual_outcome:
    protocol_completed: true
    doses_given: "10/10 (100%)"
    bhb_day_5: 0.9
    side_effects: "mild_loose_stool_day_2"
    milk_yield_change: "+3 L/day vs baseline"
    
  classification: "TP"
  root_cause: null
```

### Root Cause Categories (для ошибок)

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| **compliance_issue** | **P1** | Неполное соблюдение протокола | Дано только 6 из 10 доз |
| **dose_inadequate** | **P1** | Доза ниже 300 мл | Экономия, недостаточный объём |
| **timing_wrong** | **P2** | Неправильное время дачи | Сразу после корма, плохая абсорбция |
| **underlying_disease** | **P2** | Нелеченое сопутствующее | Метрит, мастит не диагностирован |
| **severe_sck** | **P2** | BHB >2.9, PG недостаточен | Требовалась комбинированная терапия |
| **acceptable_variability** | **P3** | Нормальная вариативность ответа | 10-15% коров медленно отвечают |

### Action by Priority

```yaml
P1 (critical):
  threshold: "2+ compliance или dose issues"
  timeline: "24–48 часов"
  action: "Retrain staff, check PG supply quality"
  
P2 (planned):
  threshold: "3+ underlying disease missed"
  timeline: "в ближайший scheduled review"
  action: "Add systematic health check before PG protocol"
  
P3 (no_action):
  threshold: "acceptable_variability"
  timeline: "не требует действия"
  action: "Document, continue monitoring"
```

### Review Schedule

| Trigger | Action | Тип |
|---------|--------|-----|
| 10 triggers + 5 outcomes | Включить метрики | scheduled |
| Compliance <70% | Retraining required | emergency |
| 3+ underlying disease missed | Add health screening | targeted |

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | 2026-04-11 | Создано на основе SoTA (Duffield, McArt, Chapinal) | StanisSerg |
| 4.0 | 2026-04-11 | Переписано под стандарт v4.0 | StanisSerg |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence Status | Risk Level | Влияние | Митигация |
|------------|-----------------|------------|---------|-----------|
| **Compliance dependent** | RCT assumes 100% | High | Under-dosing ineffective | Training, monitoring |
| **No local validation** | Literature only | Medium | May not work locally | Validate ASAP |
| **BHB >2.9 less effective** | Known from literature | Medium | Higher failure rate | Extend duration or combine |
| **Concurrent disease** | Often missed | High | PG fails, disease progresses | Systematic screening |
| **PG quality varies** | Unknown locally | Medium | Sub-therapeutic doses | Quality control |

### Acceptable Error Bounds

Target (post-validation):
- Response rate (BHB <1.2 by day 5): > 70%
- Compliance: > 85%
- Rebound rate (after stopping): < 20%

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
    - bhb_mmol_l_start
    - dim
    - ast_u_l
    - concurrent_disease
    
  prediction:
    verdict: "RULE_003_RECOMMENDED_{LEVEL} / BLOCKED / NOT_APPLICABLE"
    protocol_duration: "3 / 5 / 7 days"
    
  decision:
    protocol_started: true/false
    actual_doses_planned: "6 or 10"
    
  outcome:
    doses_given: "N/M (compliance %)"
    bhb_day_5: "value"
    response: "success / partial / failure"
    
  basis:
    rule: "RULE-003"
    soTA: "Duffield, McArt, Chapinal"

traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
```

#### Validation Steps

1. Применить на 3+ фермах (SCK cases)
2. Создать 10+ кейсов (6 success, 2 partial, 2 failure)
3. Document outcomes (compliance critical!)
4. Calculate response rate, rebound rate
5. Define error bounds

```yaml
precision_recall_tradeoff:
  not_applicable: "RULE-003 is treatment, not screening"
  key_metric: "Response rate (not FP/FN)"
  target_response_rate: ">70%"
```

---

### Phase 2: Robustness (HIGH)

```yaml
actions:
  - analyze_compliance_failures
  - root_cause_analysis (non-responders)
  - test_variations:
      - dose_250_vs_300_ml
      - duration_3_vs_5_vs_7_days
  - validate_pg_quality_sources
  - validate_concurrent_disease_screening

metrics_activation:
  conditions:
    - ≥10 triggers
    - ≥5 outcomes
```

---

### Phase 3: Full Automation (MEDIUM)

```yaml
components:
  - pg_protocol_reminders
  - compliance_tracking
  - outcome_prediction (who will respond?)

readiness_criteria:
  - response_rate_known: true
  - compliance_optimized: true
```

---

### Phase 3.5: Rule Saturation (CRITICAL)

```yaml
saturation_criteria:
  rules_stable: ">=3–5"
  
dependencies:
  - RULE-002: "Provides SCK diagnosis"
  - RULE-001: "May override if metabolic deficit severe"
  
integration:
  - RULE-002 ──► RULE-003: "Sequential"
```

---

### Phase 4: ML (LOW)

```yaml
potential_improvements:
  treatment_layer:
    - optimize_intervention_window:
        "When to start PG relative to DIM, BHB trajectory, and feed intake for maximum effect"
    - optimize_pg_duration: "3 vs 5 vs 7 days based on NEFA, BCS loss, initial BHB"
    - predict_non_responders: "Who needs alternative therapy?"
    - personalize_pg_dose: "By weight, BHB level, DIM"
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
RULE-002 (diagnosis) ──► RULE-003 (treatment)
   SCK detected            PG protocol
   
Dependency:
  RULE-003 DEPENDS on RULE-002
  Не применять PG без подтверждения SCK
  
Sequence:
  1. RULE-002: BHB≥1.2 + DIM 3-14 + no clinical → SCK
  2. RULE-003: PG 300ml × 3-5 days
```

### Applicability (Явные границы применения)

```yaml
applicability:
  requires:  # Что должно быть TRUE
    - "RULE_002_TRIGGERED (SCK confirmed)"
    - "BHB 1.2-2.9 mmol/L"
    - "Animal conscious and can swallow"
    - "No severe hepatic lipidosis (AST <=500, provisional threshold)"
    
  appropriate_if:  # Когда применение оптимально
    - "Early detection (DIM 3-14)"
    - "BHB 1.2-2.0 (moderate SCK)"
    - "Good compliance expected"
    
  blocked_if:  # Что делает применение невозможным
    - "Clinical ketosis signs present"
    - "BHB > 2.9 (severe SCK)"
    - "Complete anorexia >48h"
    - "Severe hepatic lipidosis (AST >500, provisional)"
    - "Suspected renal failure (requires veterinary assessment)"
    
  success_criteria:  # Что считаем успехом
    - "BHB <1.2 within 3-5 days"
    - "No progression to clinical ketosis"
    - "Appetite maintained or improved"
    
  failure_response:  # Что делать при неудаче
    - "Reassess diagnosis via RULE-002"
    - "Check compliance (were all doses given?)"
    - "Screen for concurrent disease (metritis, mastitis)"
    - "Escalate to combined therapy if needed"
    
  escalates_to:  # Куда передаём, если не применимо
    clinical_ketosis: "Clinical Ketosis Emergency Protocol"
    severe_sck: "Combined Therapy (PG + IV glucose)"
    anorexia: "Parenteral Glucose Protocol"
    hepatic_lipidosis: "Specialized Veterinary Care"
    renal_failure: "Modified protocol with veterinary supervision"
    
  priority_rule: "RULE-001 overrides RULE-003 if metabolic deficit severe"
```

### Escalation / Applicability Logic

| Situation | Primary Rule | Logic |
|-----------|--------------|-------|
| RULE-001 says "systemic correction first" | RULE-001 | Priority — address root cause before symptom treatment |
| BHB >2.9 (severe SCK) | Clinical Protocol | RULE_003 insufficient alone — escalate |
| Concurrent clinical ketosis | Clinical Protocol | RULE_003_BLOCKED — emergency intervention required |
| Complete anorexia >48h | Parenteral Therapy | Cannot administer oral PG |
| Severe hepatic lipidosis | Veterinary Care | Liver cannot metabolize PG |
| BHB normal, but strong clinical suspicion | Clinical Protocol | RULE-003 does not override clinical judgment |

**Principle:**
```
RULE-003 is adjunctive treatment, not primary intervention.
It works within metabolic stability, not instead of it.
```

---

*Framework: Execution Framework v4.0*  
*Format: CASE → DL → RULE (executable, managed)*  
*System Loop: CASE→PREDICTION→DECISION→FACT→ERROR→RULE→UPDATE→NEXT CASE*
