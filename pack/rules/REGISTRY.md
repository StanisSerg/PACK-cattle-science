---
registry_id: RULE-REGISTRY-001
version: "4.0"
date_created: 2026-04-11
description: "Портфель правил крупного рогатого скота — управляемая экосистема"
---

# Rule Registry — Портфель правил

> **v4.0**: Экосистема взаимодействующих правил
> 
> Правила больше не изолированы — они влияют друг на друга, усиливают, делят зоны ответственности.

---

## INVENTORY (Инвентарь правил)

| ID | Название | Категория | Статус | Confidence | Последний Trigger | Trend | Version |
|----|----------|-----------|--------|------------|-------------------|-------|---------|
| [RULE-001](RULE-001-ketosis-threshold.md) | Ketosis-Threshold-Invalidation | metabolic | testing | medium | 2026-04-11 | stable | v4.0 |
| [RULE-002](RULE-002-sck-bhb-threshold.md) | SCK-BHB-Threshold | metabolic | conceptual | low | — | stable | v4.0 |
| [RULE-003](RULE-003-propylene-glycol-protocol.md) | Propylene-Glycol-Protocol | metabolic | conceptual | low | — | stable | v4.0 |
| [RULE-004](RULE-004-dry-period-nutrition.md) | Dry-Period-Nutrition | metabolic | conceptual | low | — | stable | v4.0 |

---

## DOMAIN: METABOLIC ZONE

### Граница домена

```yaml
domain: metabolic
timeframe: prepartum → transition → postpartum
key_variables:
  - BHB (beta-hydroxybutyrate)
  - DMI (dry matter intake)
  - NEFA (non-esterified fatty acids)
  - BCS (body condition score)
  - DIM (days in milk)
  
economic_driver: "Prevent ketosis → reduce treatment costs + maintain milk production"

rules_in_domain: 4
  - RULE-004: prevention (prepartum)
  - RULE-002: detection (postpartum screening)
  - RULE-001: decision (intervention logic)
  - RULE-003: treatment (execution)
```

---

## FLOW: Цепочка принятия решений

### Ось времени

```
Prepartum          Transition        Postpartum
   │                    │                  │
   ▼                    ▼                  ▼
RULE-004 ─────────► RULE-002 ─────────► RULE-001 ─────────► RULE-003
(prevention)         (detection)        (decision)         (treatment)
   │                    │                  │                  │
   │                    │                  │                  │
   └────────────────────┴──────────────────┴──────────────────┘
                        METABOLIC ZONE
```

### Transition Conditions (Условия переходов)

```yaml
RULE-004 → RULE-002:
  trigger: "DIM >= 3 (fresh cow entry)"
  condition: "Postpartum monitoring begins"
  data_capture: "First BHB check scheduled"
  
RULE-002 → RULE-001:
  trigger: "BHB >= 1.2 mmol/L"
  condition: "SCK detected by screening"
  data_capture: "Record BHB, DIM, clinical signs"
  
RULE-001 → RULE-003:
  trigger: "intervention decision = PG applicable"
  condition: "RULE-001 TRIGGERED (not BLOCKED) AND metabolic deficit moderate"
  data_capture: "Confirm SCK diagnosis, rule out contraindications"
  
RULE-001 BLOCKED → Clinical Protocol:
  trigger: "clinical_signs = true OR BHB > 2.9 OR severe deficit"
  condition: "Emergency intervention required"
  data_capture: "Escalation reason, emergency actions"
```

### Feedback Loops (Обратные связи)

```yaml
RULE-003 → RULE-001 (failure feedback):
  trigger: "PG protocol failed (BHB > 1.4 at day 5)"
  action: "Reassess by RULE-001"
  learning: "Check if metabolic deficit was underestimated"
  
RULE-001 → RULE-004 (pattern feedback):
  trigger: "Multiple cases requiring RULE-001 intervention"
  action: "Review dry period management"
  learning: "Preventive measures insufficient"
  
RULE-002 → RULE-004 (efficacy feedback):
  trigger: "High SCK rate despite RULE-004"
  action: "Audit dry period protocols"
  learning: "RULE-004 implementation gap"
  
system_loop:
  description: "Continuous improvement cycle"
  flow: "CASE → PREDICTION → DECISION → FACT → ERROR → RULE → UPDATE → NEXT CASE"
```

---

## ROLES (Роли правил)

| Rule | Layer | Function | Specificity | Handoff To |
|------|-------|----------|-------------|------------|
| RULE-004 | Prevention | Reduce probability | Herd-level | RULE-002 |
| RULE-002 | Detection | Catch signal | Individual screening | RULE-001 |
| RULE-001 | Decision | Interpret & route | High-resolution | RULE-003 or Emergency |
| RULE-003 | Treatment | Execute intervention | Protocol execution | Follow-up |

---

## BOUNDARY CONDITIONS (Граничные условия)

### System Constraints

```yaml
constraint_001:
  name: "Sequential dependency"
  description: "Cannot apply RULE-003 without RULE-002 confirmation"
  enforcement: "Hard block in workflow"
  
constraint_002:
  name: "Priority override"
  description: "RULE-001 overrides RULE-003 if metabolic deficit severe"
  enforcement: "Automatic escalation"
  
constraint_003:
  name: "Clinical judgment supremacy"
  description: "Any rule can be overridden by veterinarian decision"
  enforcement: "Veto mechanism in all rules"
  
constraint_004:
  name: "Time windows"
  description: "Each rule has specific DIM applicability"
  enforcement: "BLOCKED if outside window"
```

### Trade-offs

```yaml
recall_vs_precision:
  context: "RULE-002 screening"
  trade_off: "Higher recall → More false positives → Overtreatment"
  current_setting: "Slightly recall-biased (recall >85%, precision >80%)"
  
cost_vs_outcome:
  context: "RULE-003 PG protocol"
  trade_off: "Higher compliance cost → Better outcomes"
  optimal: "Balance at >85% compliance"
  
prevention_vs_treatment:
  context: "RULE-004 vs downstream rules"
  trade_off: "Invest in dry period → Less postpartum issues"
  roi: "Prevention 3-5x more cost-effective than treatment"
```

---

## RELATIONSHIPS (Связи между правилами)

### 1. Reinforcement (Усиление)

```
RULE-001 ──► RULE-003
   │            │
   │            └─► "Если RULE-001 сработал → RULE-003 как support"
   │
   └─► "Системная коррекция (001) + Пропиленгликоль (003) = synergistic effect"

Усиление:
  trigger: RULE-001 TRIGGERED
  effect: RULE-003 priority повышается
  reasoning: "Метаболический дефицит требует и системной коррекции, и поддержки"
```

### 2. Sequencing (Последовательность)

```
RULE-004 ──► [time passes] ──► RULE-002 ──► RULE-001 ──► RULE-003

Sequence with conditions:
  - RULE-004 active: DIM -60 to 0
  - Transition: DIM 0 (calving)
  - RULE-002 active: DIM 3-14 (screening window)
  - RULE-001 evaluates: if BHB >= 1.2
  - RULE-003 executes: if PG applicable
```

### 3. Dependency (Зависимость)

```
RULE-003 DEPENDS ON RULE-002:
  condition: "SCK must be confirmed before PG administration"
  enforcement: "Do not apply PG without RULE-002_TRIGGERED"
  
RULE-001 DEPENDS ON CONTEXT:
  inputs: [RULE-002 output, clinical signs, DMI, BCS]
  processing: "Discriminate adaptation vs deficit"
  output: "Intervention decision"
```

---

## ZONES (Зоны ответственности)

### Metabolic Zone — Complete Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    METABOLIC ZONE                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  PREVENTION          DETECTION           DECISION    TREATMENT  │
│  ├─ RULE-004         ├─ RULE-002         ├─ RULE-001  ├─ RULE-003│
│  │  Dry Period       │  SCK Screening    │  Systemic  │  PG     │
│  │  Optimization     │  (BHB≥1.2)        │  Decision  │  Protocol│
│  │                   │                   │            │         │
│  │  Goal: Reduce     │  Goal: Early      │  Goal:     │  Goal:  │
│  │  probability      │  detection        │  Correct   │  Execute│
│  │                   │                   │  routing   │         │
│  └───────────────────┴───────────────────┴────────────┴─────────┘
│                         │                                       │
│                         ▼                                       │
│              ┌──────────────────────┐                           │
│              │   OUTCOME:           │                           │
│              │   BHB normalized     │                           │
│              │   DMI restored       │                           │
│              │   Milk maintained    │                           │
│              └──────────────────────┘                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

Zone Owner: metabolic_team
Rules: 4 active
Validation Status: 1 pilot, 3 conceptual
```

---

## CONFLICT RESOLUTION (Разрешение конфликтов)

### Priority Matrix

| Situation | Primary Rule | Secondary Rule | Resolution |
|-----------|--------------|----------------|------------|
| BHB>1.2 + clinical signs | Clinical Protocol | RULE-002 (blocked) | Emergency intervention |
| BHB>1.2 + DMI<80% | RULE-001 | RULE-002 | RULE-001 decides systemic correction |
| BHB 1.0-1.2 | RULE-002_GRAY_ZONE | — | Monitor, repeat BHB |
| PG indicated but anorexia | Clinical Protocol | RULE-003 (blocked) | Parenteral therapy |
| RULE-001 vs Market convention | RULE-001 | Market | Evidence-based priority |

### Escalation Path

```
При неопределённости:
  1. Check rule applicability (limits)
  2. Check confidence levels
  3. If conflict persists → Zone Owner decides
  4. If critical → Escalate to veterinary committee
```

---

## CROSS-RULE METRICS (Метрики портфеля)

### Portfolio Health

| Метрика | Описание | Текущее | Цель |
|---------|----------|---------|------|
| **coverage** | % клинических сценариев покрыто | 60% | >80% |
| **handoff_success** | % успешных переходов между правилами | N/A | >90% |
| **feedback_loop_closure** | % кейсов с завершённым циклом | N/A | >95% |
| **portfolio_roi** | Совокупный ROI всех правил | N/A | >+150% |

### Zone Metrics

```yaml
metabolic_zone:
  prevention_effectiveness: "SCK rate with vs without RULE-004"
  detection_yield: "Cases found per 100 screened"
  decision_accuracy: "Correct routing rate"
  treatment_response: "PG success rate"
  
  integration_metric: "Smooth transition rate between rules"
```

---

## EVOLUTION ROADMAP (Дорожная карта)

### Phase 1: Foundation (Q2 2026)
- [x] RULE-001 → pilot-ready (testing)
- [ ] RULE-002, 003, 004 → validation begins
- [ ] Document transition conditions in practice
- [ ] Test feedback loops

### Phase 2: Integration (Q3 2026)
- [ ] Validate handoff success rate >90%
- [ ] Refine boundary conditions based on cases
- [ ] Add automation for transitions
- [ ] RULE-001 → production

### Phase 3: Expansion (Q4 2026)
- [ ] New zone: Reproductive
- [ ] New zone: Infectious
- [ ] Cross-zone integration
- [ ] Portfolio-level optimization

---

## QUICK REFERENCE (Быстрая справка)

### When to Apply Which Rule

```
DIM -60 to 0 (Dry period)     → RULE-004
DIM 3-14 + BHB ≥ 1.2          → RULE-002
BHB ≥ 1.2 + Low DMI          → RULE-001
SCK confirmed + No blockers   → RULE-003
```

### Emergency Overrides

```
Clinical signs present        → Bypass all rules → Emergency protocol
Severe deficit (BHB > 2.9)   → RULE-001 BLOCKED → Combined therapy
Anorexia > 48h               → RULE-003 BLOCKED → Parenteral glucose
```

---

## APPENDIX

### A. Rule State Summary

```
conceptual ──► pilot-ready ──► testing ──► stable ──► deprecated
     │              │             │           │            │
     │              │             │           │            │
     ▼              ▼             ▼           ▼            ▼
  идея         документ      валидация    production   замена
               готов         на ферме                  найдена
```

### B. Confidence vs Maturity

```
Confidence: данные подтверждают (low/medium/high)
Maturity: готовность к применению (conceptual/pilot/production)

Matrix:
  low + conceptual    = не использовать
  medium + pilot      = использовать с осторожностью
  high + production   = полное доверие
```

---

*Registry обновляется при каждом изменении статуса любого правила*
*Last updated: 2026-04-11*
