---
type: fpf-study
pattern: G.11
title: "Telemetry-Driven Refresh: выборочное обновление SoTA-упаковок"
domain: cattle-science
difficulty: advanced
reading_time: 28 min
created: 2026-06-27
fpf_context: ["G.11", "G.Core", "G.6", "G.7", "G.10", "G.12"]
---

# G.11 — Telemetry-Driven Refresh: выборочное обновление SoTA-упаковок

> **Цель capture:** объяснить, как паттерн G.11 превращает telemetry, edition drift и bridge evolution в slice-scoped refresh plans и reports, избегая полной перестройки SoTA-упаковок.

---

## 1. Зачем это читать

В скотоводстве знание и методы быстро устаревают: появляются новые исследования по кетозу, меняются пороги BHB, обновляются лабораторные протоколы, пересматриваются рекомендации по кормлению. Без явного refresh orchestration команда либо перестраивает всё после каждого малого изменения, либо продолжает использовать устаревшие pack'и. G.11 предлагает orchestration kit, который планирует выборочные обновления на основе typed RSCR triggers.

> **FPF-тезис:** *«Обновление должно быть таким же scoped и auditable, как и первоначальное создание pack'а.»*

**Фермерский пример:**

> В лаборатории обновился протокол измерения BHB. Без G.11 команда могла бы пересобрать все отчёты, дашборды и parity-отчёты. G.11 находит PathSliceId, затронутые этим изменением, и планирует refresh только для них, оставляя остальные pack'и неизменными.

---

## 2. История одной ошибки

Хозяйство использовало систему мониторинга метаболического статуса. Когда вышло новое исследование, изменившее рекомендуемый порог BHB, IT-отдел запустил полную перестройку всех dashboard'ов, parity reports и recommendation packs. Процесс занял две недели, и часть pack'ов была случайно пересобрана на новых данных, а часть — на старых. В результате фермер получил противоречивые рекомендации. G.11 мог бы создать slice-scoped RefreshPlan и обновить только affected slices.

---

## 3. Telemetry-Driven Refresh — полное описание

### 3.1 Определение

**Telemetry-Driven Refresh** — это паттерн, который превращает typed RSCR triggers в scoped RefreshPlan@Context и RefreshReport@Context, публикует DeprecationNotice@Context и EditionBumpLog@Context, и координирует downstream actions через делегирование governing patterns.

### 3.2 Почему это важно

Полная перестройка SoTA-pack'ов при любом изменении непрактична и рискованна. С другой стороны, игнорирование drift приводит к использованию устаревших решений. G.11 находит баланс: вычисляет минимальную dependency closure, планирует обновление и публикует auditable report.

### 3.3 RefreshQueue

**Определение.** RefreshQueue — это очередь refresh-кандидатов, keyed by PathSliceId (preferred) или PatternScopeId, каждый из которых несёт канонический RSCRTriggerKindId.

**Пояснение.** RefreshQueue не выполняет действия; она накапливает триггеры для планирования. Ordering и prioritization — policy-bound, но каждый item должен иметь канонический trigger kind.

**Пример из животноводства.**

```text
RefreshQueue:
  - item 1: PathSliceId PS-001, trigger EditionPinChange, payload DHCMethodRef.edition
  - item 2: PathSliceId PS-002, trigger PolicyPinChange, payload Φ(CL)=POL-001
  - item 3: PathSliceId PS-003, trigger TelemetryDelta, payload illumination
```

**Ключевой признак.** Queue items содержат canonical RSCRTriggerKindId и scope.

### 3.4 RefreshPlan@Context

**Определение.** RefreshPlan@Context — это WorkPlanning plan item, который декларирует scope, planned triggers, planned actions и required pins. Он не выполняет Work.

**Пояснение.** RefreshPlan разделяет планирование и исполнение. Он указывает, какие slices затронуты, какие actions делегируются каким паттернам, и какие pins нужны для rerun.

**Пример из животноводства.**

```text
RP-001: RefreshPlan@Context
  - TargetScope: [PS-001, PS-002]
  - PlannedTriggers: [EditionPinChange, PolicyPinChange]
  - PlannedActions:
    - RecomputeSelectionOrSetPublication → G.5
    - UpdateEvidenceBindings → G.6
    - ReshipPack → G.10
  - RequiredPins: {DHCMethodRef.edition, Φ(CL)=POL-001, PathSliceId[]}
```

**Ключевой признак.** RefreshPlan — planning object с делегированием actions; не содержит gate decisions.

### 3.5 RefreshReport@Context

**Определение.** RefreshReport@Context — это Work или Audit artefact, фиксирующий executed actions, observed deltas, RSCR refs, emitted notices и canonical trigger kinds.

**Пояснение.** RefreshReport отвечает на вопрос: «Что было сделано и почему?» Он связывает действия с триггерами и evidence.

**Пример из животноводства.**

```text
RR-001: RefreshReport@Context
  - ExecutedActions:
    - G.5 recompute → new selector outcome REF-002
    - G.10 reship → PACK-002
  - ObservedDeltas: DHCMethodRef.edition 2.1 → 2.2
  - RSCRRefs: [RSCR-001]
  - EmittedNotices: [EditionBumpLog EBL-001]
```

**Ключевой признак.** RefreshReport содержит executed actions, deltas, RSCR refs и emitted notices.

### 3.6 DeprecationNotice и EditionBumpLog

**Определение.** DeprecationNotice@Context — это controlled-evolution artefact, который объясняет scope, reason class и successor refs для deprecated artefact'ов. EditionBumpLog@Context — это запись edition increment и pins, которые его обосновывают.

**Пояснение.** Эти artefacts сохраняют ID-continuity. Вместо удаления старого понятия или порога система публикует deprecation или bump, чтобы старые pack'и оставались интерпретируемыми.

**Пример из животноводства.**

```text
EBL-001: EditionBumpLog
  - artefact: DHCMethodRef BHB measurement
  - old edition: 2.1
  - new edition: 2.2
  - reason: RSCRTriggerKindId.EditionPinChange
  - affectedPathSliceIds: [PS-001, PS-002]

DN-001: DeprecationNotice
  - artefact: AC-001 (BHB ≥ 1.2)
  - reason: new evidence suggests threshold 1.0
  - successor: AC-002
```

**Ключевой признак.** DeprecationNotice и EditionBumpLog содержат reason class, scope и successor refs.

### 3.7 Scope closure

**Определение.** Scope closure — это минимальная dependency closure over cited evidence, source relations, crossings и pinned references, которая определяет affected slices.

**Пояснение.** Closure — это planning-time claim, не Work-time output. Она гарантирует, что refresh не слишком узок (пропускает зависимости) и не слишком широк (перестраивает всё).

**Пример из животноводства.** Изменение DHCMethodRef для BHB затрагивает: observation nodes в EG-001, acceptance clauses AC-001 и AC-002, dashboard rows PS-001, parity report PR-001. Closure не затрагивает, например, копытное здоровье, если BHB не используется там.

**Ключевой признак.** Closure rationale фиксируется в RefreshPlan.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Поменялся порог BHB, пересоберём все отчёты.»*

**Разложение по G.11:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «поменялся порог BHB» | RSCRTriggerKindId.EditionPinChange | Нужен canonical trigger и payload pins |
| «пересоберём все отчёты» | full-rerun | Требуется closure rationale; обычно избыточно |

**Основные риски смешивания:**

1. **Full-rerun mania.** Любое изменение влечёт дорогую перестройку.
2. **Editionless refresh.** Обновление происходит без фиксации edition pins.
3. **Alias-as-semantics.** Текстовые причины вместо canonical trigger kinds.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** обновление порога BHB и его влияние на pack.

**Было (смешанное / нечёткое):**
> «Порог BHB поменялся, пересоберём отчёты.»

**Стало (разложенное / ясное):**

**Trigger:**
> TR-001: RSCRTriggerKindId.EditionPinChange, payload {DHCMethodRef.edition 2.1→2.2}, scope PS-001.

**Scope closure:**
> PS-001 (dashboard rows), PS-002 (acceptance clauses), PS-003 (parity report).

**RefreshPlan RP-001:**
> TargetScope = [PS-001, PS-002, PS-003]
> PlannedActions = [UpdateEvidenceBindings → G.6, RecomputeSelection → G.5, ReshipPack → G.10]

**RefreshReport RR-001:**
> ExecutedActions = [G.6 update, G.5 recompute, G.10 reship]
> EmittedNotices = [EBL-001]

**Результат:**
- Обновление ограничено затронутыми slices.
- Каждый шаг делегирован соответствующему паттерну.
- ID-continuity сохранена через EditionBumpLog.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Настройте ingestion канонических RSCR triggers из telemetry hooks, bridge sentinels и freshness events.

**Шаг 2.** Вычислите scope closure over evidence, crossings и pinned refs.

**Шаг 3.** Создайте RefreshPlan@Context с TargetScope, PlannedTriggers и PlannedActions.

**Шаг 4.** Выполните actions как Work и опубликуйте RefreshReport@Context.

**Шаг 5.** При необходимости опубликуйте DeprecationNotice или EditionBumpLog.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Refresh не scoped к PathSliceId? | Риск full-rerun и избыточных затрат. |
| Триггеры используют локальные aliases вместо canonical ids? | Семантика размывается между командами. |
| RefreshPlan содержит gate decisions? | Нарушено P2W boundary; planning ≠ work. |
| RefreshReport не фиксирует RSCRRefs? | Невозможно проверить обоснование обновления. |
| Изменения понятий не сопровождаются EditionBumpLog? | Теряется ID-continuity. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| G.Core | предоставляет RSCR trigger catalogue и Default Governing Definition Index |
| G.6 Evidence Graph | предоставляет PathId/PathSliceId для scope closure |
| G.7 Bridge Calibration | отправляет sentinel triggers через BridgeSentinel |
| G.10 SoTA Pack Shipping | получает ReshipPack action |
| G.12 DHC Dashboards | предоставляет dashboard telemetry pins |

---

## 9. Что запомнить

1. G.11 — thin orchestration kit для refresh; semantics делегируются другим паттернам.
2. RefreshQueue и RefreshPlan@Context scoped to PathSliceId.
3. Все triggers — canonical RSCRTriggerKindId; aliases — только labels.
4. RefreshReport фиксирует actions, deltas, RSCR refs и notices.
5. DeprecationNotice и EditionBumpLog сохраняют ID-continuity.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.11*
