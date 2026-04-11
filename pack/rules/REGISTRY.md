---
registry_id: RULE-REGISTRY-001
version: "4.0"
date_created: 2026-04-11
description: "Портфель правил крупного рогатого скота — управляемая экосистема"
---

# Rule Registry — Портфель правил

> **v4.0**: Экосистема взаимодействующих правил
> 
> Правила больше не изолированы — они влияют друг на друга, конфликтуют, усиливают, делят зоны ответственности.

---

## INVENTORY (Инвентарь правил)

| ID | Название | Категория | Статус | Confidence | Последний Trigger | Trend | Version |
|----|----------|-----------|--------|------------|-------------------|-------|---------|
| [RULE-001](RULE-001-ketosis-threshold.md) | Ketosis-Threshold-Invalidation | metabolic | testing | medium | 2026-04-11 | stable | v4.0 |
| [RULE-002](RULE-002-sck-bhb-threshold.md) | SCK-BHB-Threshold | metabolic | conceptual | low | — | stable | v4.0 |
| [RULE-003](RULE-003-propylene-glycol-protocol.md) | Propylene-Glycol-Protocol | metabolic | conceptual | low | — | stable | v4.0 |
| [RULE-004](RULE-004-dry-period-nutrition.md) | Dry-Period-Nutrition | metabolic | conceptual | low | — | stable | v4.0 |

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
RULE-004 ──► RULE-001

Последовательность:
  phase_1: "Dry Period Nutrition (004) — предотвращение"
  phase_2: "Ketosis Threshold (001) — раннее обнаружение"
  
  Если 004 выполнен правильно → 001 срабатывает реже
  Если 001 срабатывает → проверить выполнение 004
```

### 3. Conflict Detection (Обнаружение конфликтов)

```
CONFLICT-001: Противоречивые интервенции

Сценарий:
  RULE-001: "DO NOT use hepatoprotectors as primary"
  MARKET_CONVENTION: "Use hepatoprotectors immediately"
  
  Конфликт: Действие vs Недействие
  Разрешение: RULE-001 имеет приоритет при BHB>1.2 + DMI<80%
  
  escalation:
    - При конфликте → использовать rule priority
    - Если не уверены → BLOCKED → клинический протокол
```

### 4. Dependency (Зависимость)

```
RULE-003 зависит от RULE-001:

  condition: "Propylene glycol применять ТОЛЬКО если"
  
  dependency_check:
    - RULE-001 статус: TRIGGERED
    - action: "Сначала системная коррекция, потом поддержка"
    
  warning: "Изолированное применение 003 без 001 = suboptimal"
```

---

## ZONES (Зоны ответственности)

### Зона: Metabolic (Метаболические)

```
┌─────────────────────────────────────────────────────────────┐
│  ЗОНА: Metabolic                                            │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  PREVENTION          DETECTION           INTERVENTION       │
│  ├─ RULE-004         ├─ RULE-002         ├─ RULE-001        │
│  │  Dry Period       │  SCK Threshold    │  Invalidation    │
│  │  Nutrition        │  (早期 warning)    │  (core decision) │
│  │                   │                   │                  │
│  │                   │                   ├─ RULE-003        │
│  │                   │                   │  Support (PG)    │
│  │                   │                   │                  │
│  └───────────────────┴───────────────────┴──────────────────┘
│                         │                                   │
│                         ▼                                   │
│              ┌──────────────────────┐                       │
│              │   OUTCOME:           │                       │
│              │   BHB normalized     │                       │
│              │   DMI restored       │                       │
│              └──────────────────────┘                       │
│                                                             │
│  Zone Owner: metabolic_team                                 │
│  Rules: 4 active, 1 production-ready                        │
└─────────────────────────────────────────────────────────────┘
```

**Hierarchy внутри зоны:**
1. **RULE-004** (превентивный) — приоритет: предотвращение
2. **RULE-002** (диагностический) — приоритет: раннее обнаружение  
3. **RULE-001** (интервенционный) — приоритет: core decision
4. **RULE-003** (поддерживающий) — приоритет: adjunct

---

## CONFLICT RESOLUTION (Разрешение конфликтов)

### Priority Matrix

| Situation | Primary Rule | Secondary Rule | Resolution |
|-----------|--------------|----------------|------------|
| BHB>1.2 + клинические признаки | Clinical Protocol | RULE-001 (blocked) | Клинический протокол |
| BHB>1.2 + DMI<80% + ранняя стадия | RULE-001 | RULE-003 | 001 first, 003 as support |
| BHB 1.0-1.2 (серая зона) | RULE-002 | RULE-001 (not triggered) | 002 early warning, monitor |
| Гепатопротекторы prescribed | RULE-001 | MARKET | Проверить conditions — возможно invalidation |

### Escalation Path

```
При конфликте правил:

1. Проверить applicability (limits каждого правила)
2. Проверить confidence (высокий > низкого)
3. Проверить maturity (production > pilot > conceptual)
4. Если равны → Zone Owner решает
5. Если критично → escalation to technical committee
```

---

## CROSS-RULE METRICS (Метрики портфеля)

### Portfolio Health

| Метрика | Описание | Текущее | Цель |
|---------|----------|---------|------|
| **coverage** | % клинических сценариев покрыто | 25% | >80% |
| **conflict_rate** | % случаев с конфликтами | 0% | <10% |
| **handoff_success** | % успешных передач между правилами | N/A | >90% |
| **portfolio_roi** | Совокупный ROI всех правил | +164% (001) | >+100% |

### Rule Interaction Matrix

```
        R-001   R-002   R-003   R-004
R-001     —     weak   strong   weak
R-002    weak     —     none   strong
R-003  strong   none     —     none
R-004    weak  strong   none     —

Legend:
  strong = reinforce или sequence
  weak = awareness, cross-check
  none = независимы
```

---

## EVOLUTION ROADMAP (Дорожная карта)

### Phase 1: Foundation (Q2 2026)
- [x] RULE-001 → pilot-ready (testing)
- [ ] RULE-002 → conceptual → pilot-ready
- [ ] Определить зоны: reproductive, infectious

### Phase 2: Expansion (Q3 2026)
- [ ] RULE-003, RULE-004 → pilot-ready
- [ ] Разрешить первые конфликты
- [ ] Настроить cross-rule metrics

### Phase 3: Integration (Q4 2026)
- [ ] Автоматическое разрешение конфликтов
- [ ] Portfolio-level optimization
- [ ] RULE-001 → production

### Phase 4: Intelligence (2027)
- [ ] ML на уровне портфеля (не отдельных правил)
- [ ] Predictive conflict detection
- [ ] Auto-evolution правил

---

## GOVERNANCE (Управление)

### Zone Owners

| Zone | Owner | Rules |
|------|-------|-------|
| metabolic | @metabolic_team | RULE-001 to 004 |
| reproductive | TBD | — |
| infectious | TBD | — |

### Change Process

```
Изменение правила:

1. Создать RFC в /docs/rfc/
2. Проверить impact на связанные правила (this registry)
3. Запустить pilot (min 5 cases)
4. Update registry (relationships, conflicts)
5. Merge при approval Zone Owner + 1 другой owner
```

---

## APPENDIX

### A. Rule Lifecycle

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
Confidence: насколько данных подтверждает правило (low/medium/high)
Maturity: насколько правило готово к использованию (conceptual/pilot/production)

Матрица:
  low + conceptual = не использовать
  medium + pilot = использовать с осторожностью
  high + production = полное доверие
  high + deprecated = мигрировать
```

---

*Registry обновляется при каждом изменении статуса любого правила*
