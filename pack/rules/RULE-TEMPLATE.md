---
# RULE TEMPLATE v4.0
# Обязательные поля для всех RULE
# Использовать как основу для создания новых правил

---

rule_id: RULE-NNN
dl_ref: DL-NNN  # ссылка на Decision Layer
case_refs: [CASE-NNN]  # подтверждающие кейсы
date_created: YYYY-MM-DD
date_updated: YYYY-MM-DD
author: "Name"
category: metabolic  # metabolic / reproductive / infectious / nutritional / management
tags: []  # ключевые слова для поиска

# RULE STATE — наблюдаемый объект
rule_version: "1.0"
rule_maturity: conceptual  # conceptual / pilot-ready / pilot-active / production / deprecated
status: conceptual  # conceptual / testing / stable / degraded / deprecated
trend: stable  # improving / stable / degrading

# Временные метки
last_trigger: null
last_error: null
last_review: YYYY-MM-DD
next_review: YYYY-MM-DD  # обычно +3 месяца

# Управляемый актив
metrics_enabled: false
confidence: low  # low / medium / high (растёт из данных)

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

# RULE-NNN: Rule-Name-Here

> **Тип:** executable decision operator  
> **Maturity:** {maturity} (v{version})  
> **Управление:** metrics to be enabled at 10+ triggers  
> **Источник:** DL-NNN  
> **Валидация:** [CASE-NNN](../../DS-cattle-cases/cases/CASE-NNN/)  
> **Портфель:** [REGISTRY.md](REGISTRY.md) — зона: {zone}

---

## DECISION (Решение)

### Trigger Conditions

```yaml
hard_conditions:  # все должны быть TRUE
  - condition: ""
    threshold: 
    operator: 
    
soft_conditions:  # 0-2 для confidence level
  - condition: ""
    threshold: 
    weight: 1

blocking_conditions:  # если TRUE → RULE_BLOCKED
  - condition: ""
    action: "REFER_TO_"
```

### Verdict Logic

```
IF blocking_conditions.any? → RULE_BLOCKED
ELSE IF hard_conditions.all? → EVALUATE_SOFT
  IF soft_score >= 2 → TRIGGERED (HIGH)
  IF soft_score == 1 → TRIGGERED (MEDIUM)
  IF soft_score == 0 → TRIGGERED (LOW)
ELSE → NOT_TRIGGERED
```

---

## STATE MACHINE

```
INITIAL ──► clinical? ──► BLOCKED
              │
              НЕТ
              │
              ▼
        hard_met? ──► НЕТ ──► NOT_TRIGGERED
              │
              ДА
              │
              ▼
        soft_score ──► TRIGGERED (LOW/MEDIUM/HIGH)
```

### State Definitions

| State | Alert Level | Required Action | Timeline |
|-------|-------------|-----------------|----------|
| BLOCKED | CRITICAL | Клинический протокол | Немедленно |
| NOT_TRIGGERED | INFO | Мониторинг | Обычный |
| TRIGGERED (LOW) | WARNING | {action} | 48 часов |
| TRIGGERED (MEDIUM) | HIGH | {action} | 24 часа |
| TRIGGERED (HIGH) | CRITICAL | {action} | Немедленно |

---

## ACTION PROTOCOL

### При {VERDICT}

**Step 1: {Action Category}**
```yaml
action: 
target: 
reason: 
```

**Step 2: {Action Category}**
```yaml
priority: 
condition: 
action: 
```

**Step 3: Monitoring**
```yaml
metrics: []
timeline: 
escalation: 
```

---

## BECAUSE (Механизм)

### Научное обоснование

```
{Объяснение биохимического/физиологического механизма}
```

### Экономическая логика

```yaml
scenario_standard:
  costs: 
  outcome: 
  roi: 
  
scenario_rule_based:
  costs: 
  outcome: 
  roi: 
  
comparison:
  delta_roi: 
  economic_verdict: 
```

---

## LIMITS (Границы)

### Hard Limits

```yaml
APPLICABLE:
  - condition: 
    
NOT_APPLICABLE:
  - condition: 
    action: 
```

### Soft Limits

```yaml
ADJUSTMENTS:
  - scenario: 
    adjustment: 
```

---

## VALIDATION

### Current Evidence Base

| Кейс | Исход | Дата | Ферма | Case Outcome | Rule Confidence |
|------|-------|------|-------|--------------|-----------------|
| [CASE-NNN]() | ✅/❌ | YYYY-MM | Farm | Confirmed/Failed | {level} |

### Metrics

| Метрика | Определение | Текущее | Целевое |
|---------|-------------|---------|---------|
| total_triggers | | | — |
| confirmed_outcomes | | | ≥5 |
| true_positives | | | — |
| false_positives | | | <20% |
| false_negatives | | | <15% |
| precision | TP / (TP + FP) | | >80% |
| recall | TP / (TP + FN) | | >85% |
| economic_precision | Положительный ROI | | >70% pilot, >80% production |

---

## RULE METRICS

### Outcome Registration

```yaml
outcome_record:
  timestamp: 
  farm_id: 
  cow_id: 
  input_data: {}
  prediction: {}
  actual_outcome: {}
  classification:  # TP / FP / FN
  root_cause:  # если FP/FN
```

### Root Cause Categories

| Category | Priority | Description | Example |
|----------|----------|-------------|---------|
| data_quality | **P1** | Проблемы с данными | |
| threshold_issue | **P1** | Порог неверен | |
| ontology_issue | **P1** | Неправильная онтология | |
| missing_variable | **P2** | Не хватает переменной | |
| temporal_issue | **P2** | Проблема времени | |
| acceptable_noise | **P3** | Биологическая вариация | |
| unpredictable | **P3** | Случайность | |

### Action by Priority

```yaml
P1 (critical):
  threshold: "2+ ошибки с одним root cause"
  timeline: "24–48 часов"
  action: "targeted fix"
  
P2 (planned):
  threshold: "3+ ошибки"
  timeline: "в ближайший scheduled review"
  
P3 (no_action):
  threshold: "acceptable_noise или unpredictable"
  timeline: "не требует действия"
```

### Review Schedule

| Trigger | Action | Тип |
|---------|--------|-----|
| 10 triggers + 5 outcomes | Включить метрики | scheduled |
| 5+ ошибок total | Экстренный review | emergency |
| 2+ одинаковых root cause | Targeted fix | targeted |

---

## CHANGE LOG

| Версия | Дата | Изменения | Автор |
|--------|------|-----------|-------|
| 1.0 | YYYY-MM-DD | Создано | |

---

## ROBUSTNESS ANALYSIS

### Known Limitations

| Limitation | Evidence | Risk | Влияние | Митигация |
|------------|----------|------|---------|-----------|
| | | | | |

### Acceptable Error Bounds

**Пока НЕ определены.**

Для production:
- False Positive Rate: < X%
- False Negative Rate: < Y%

---

## Execution Framework

---

### Phase 1: Validation + Light Automation (CRITICAL)

**Принцип:** сразу фиксируем правильно → потом масштабируем

#### Light Automation

```yaml
structured_capture:
  CASE-INPUT: [farm_id, date, {params}]
  derived_params: {}
  prediction: {}
  decision: {}
  basis: {rule, conditions}
  
traceability:
  prediction_id: "PRED-{timestamp}-{cow_id}"
  case_id: "CASE-{n}"

data_policy:
  structured_only: true
  notes_raw: "context only (НЕ используется для расчётов)"
```

#### Validation Steps

1. Применить на 3+ фермах
2. Создать 3+ кейса (success AND failure)
3. Document outcomes (structured)
4. Calculate FP / FN
5. Define error bounds

```yaml
precision_recall_tradeoff:
  principle:
    - recall ↑ → больше FP
    - precision ↑ → больше FN
  priority: recall > precision  # или precision > recall
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
  - test_edge_cases
  - validate_seasonality
  - validate_breed_effects

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
  - evaluate_rule_NNN()
  - monitoring_integration
  - dashboard
  - alerts

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
```

---

### Phase 4: ML (LOW)

```yaml
requirements:
  - ≥50 structured cases
  - error_patterns understood
  - ontology stable

steps:
  - feature_engineering (from errors)
  - train_model
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
stage: conceptual  # conceptual / pilot-ready / pilot-active / production / deprecated
mode: structured validation active
execution: deterministic capture from day 1
metrics: enabled at ≥10 triggers
confidence: auto by criteria
status: применять, не переписывать
```

---

## CHECKLIST (при создании нового RULE)

- [ ] Заполнен frontmatter (rule_id, category, теги)
- [ ] Есть ссылка на DL и CASE
- [ ] DECISION: hard/soft/blocking conditions
- [ ] STATE MACHINE: диаграмма и таблица
- [ ] ACTION PROTOCOL: пошаговый план
- [ ] BECAUSE: механизм + экономика
- [ ] LIMITS: hard и soft
- [ ] VALIDATION: минимум 1 кейс
- [ ] CHANGE LOG: версия 1.0
- [ ] Execution Framework: все фазы
