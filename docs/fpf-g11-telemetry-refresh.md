---
type: fpf-study
pattern: G.11
title: "Telemetry-Driven Refresh: как обновлять знание, не пересчитывая всё"
domain: cattle-science
difficulty: hard
reading_time: 18 min
created: 2026-05-26
---

# G.11 — Telemetry-Driven Refresh & Decay Orchestrator (Оркестрация обновления по телеметрии)

## 1. Зачем это читать

Если вы когда-нибудь слышали на ферме фразу *«вышла новая версия NASEM — давайте всё пересчитаем»* — вы столкнулись с проблемой G.11. Этот паттерн не про то, **когда обновлять**. Он про то, **что именно обновлять, почему, и как делать это целенаправленно, а не методом «всё снести и построить заново»**.

В мире software это называется selective re-computation: при изменении одной библиотеки пересобирается только то, что от неё зависит. В мире ферм — при выходе NASEM-2025 не нужно переписывать все протоколы. Нужно понять: **какие расчёты затронуты, какие evidence-пути изменились, какие pack требуют обновления**.

**Без G.11:** либо всё устаревает молча, либо каждое изменение вызывает глобальный пересчёт, который невозможно аудитировать.

**С G.11:** телеметрия → очередь обновления → выборочный пересчёт → публикация новой редакции. Каждый шаг отслеживается, каждый шаг обоснован.

---

## 2. История одной ошибки

Ферма «Орловское» использовала NASEM-2001 для расчёта энергетических потребностей дойного стада. В 2021 году вышла NASEM-2021 с обновлёнными коэффициентами переваримости и новой моделью предсказания сухого вещества.

Зоотехник сказал: «Нужно всё пересчитать». И начал:

- Пересчитал **все** рационы для **всех** групп — от телок до высокопродуктивных.
- Обновил **все** протоколы переходного периода.
- Пересмотрел **все** нормы минералов и витаминов.
- Потратил три месяца.

Аудит через полгода показал:

- NASEM-2021 **значимо изменила** только модель для **высокопродуктивных коров > 45 кг молока** и **коэффициенты для кукурузного силоса**.
- Рационы для сухостойных и телок **не изменились** существенно — но их тоже пересчитали.
- При пересчёте **не было зафиксировано**, какие именно коэффициенты изменились, и почему принято то или иное решение.
- Несколько протоколов **были обновлены ошибочно** — потому что пересчитывали всё подряд, а не по мере необходимости.

FPF G.11 говорит: *не «пересчитывай всё», а «пересчитывай только то, что затронуто, и документируй почему»*.

---

## 3. Core concepts

### 3.1 RSCR-Trigger — триггер обновления

`RSCRTrigger` (Refresh / Selective Computation / Re-publication Trigger) — это **типизированная причина обновления** с каноническим идентификатором, областью действия и полезными штифтами.

Типичные триггеры в cattle-science:

| Trigger Kind | Что случилось | Пример |
|---|---|---|
| `EvidenceSurfaceEdit` | Изменилась evidence-поверхность | Новое исследование по кетозу опубликовано в PubMed |
| `EditionPinChange` | Вышла новая редакция спецификации | NASEM-2025 заменяет NASEM-2021 |
| `PolicyPinChange` | Изменилась политика | Новый порог BHB на ферме |
| `TelemetryDelta` | Изменилась телеметрия | Показатели мастита за квартал отклонились от baseline |
| `FreshnessOrDecayEvent` | Окно свежести истекло | Данные 2023 года больше не считаются свежими |
| `CrossingBundleEdit` | Изменился мост между контекстами | Новая ферма вошла в холдинг, требуется перекалибровка Bridge |
| `BaselineBindingEdit` | Изменилась базовая линия | Золотой стандарт диагностики заменён на новый |

**Ключевой принцип:** триггер несёт **канонический id**, а не текстовое описание («вышла новая NASEM»). Это позволяет машине понять, что делать, а человеку — аудитировать.

### 3.2 RefreshQueue — очередь на обновление

`RefreshQueue` — концептуальная очередь кандидатов на обновление, ключированная по `PathSliceId` или `PatternScopeId`.

```
RefreshQueueItem := ⟨
  QueueItemId,
  scope: PathSliceId[] | PatternScopeId,
  triggerKindId: RSCRTriggerKindId,
  payloadPins: {EditionPins, PolicyPins, UTS/Path pins},
  priority?,  // policy-bound
  batchTag?   // для группировки
⟩
```

**На ферме:** при выходе NASEM-2025 очередь получает элементы:

- `PathSliceId: RATION-HIGH-YIELD-2024` → `EditionPinChange: NASEM-2001→2025`
- `PathSliceId: RATION-DRY-COW-2024` → `TelemetryDelta: разница < 2%, отложить`
- `PathSliceId: PROTOCOL-TRANSITION-2024` → `EvidenceSurfaceEdit: новое исследование по DCAD`

### 3.3 RefreshPlan@Context — план обновления

`RefreshPlan@Context` — это **WorkPlanning-объект**, который объявляет, что будет обновлено, но **не выполняет Work** и **не принимает gate-решения**.

```
RefreshPlan@Context := ⟨
  RefreshPlanId,
  describedEntity, ReferencePlane,
  TargetScope := PathSliceId[] | PatternScopeId[],
  PlannedTriggers := RSCRTrigger[],
  PlannedActions := RefreshAction[],
  RequiredPins := {EditionPins, PolicyPins, UTS/Path pins},
  PlanItemRefs := SlotFillingsPlanItemRef[]?
⟩
```

**Действия (RefreshAction):**

| Действие | Делегируется |
|---|---|
| `RerunHarvest` | G.2 / G.1 |
| `RerunParity` | G.9 |
| `RecomputeSelectionOrSetSurface` | G.5 |
| `RebindBridgeOrCrossing` | G.7 |
| `UpdateEvidenceBindings` | G.6 |
| `ReshipPack` | G.10 |
| `UpdateDashboardSlice` | G.12 |
| `EmitDeprecationNotice` | G.11 (локально) |

### 3.4 RefreshReport@Context — отчёт об обновлении

```
RefreshReport@Context := ⟨
  RefreshReportId,
  ExecutedActions[]
    → ссылки на новые артефакты (ParityReportId, PackId и т.д.)
  ObservedDeltas
    → telemetry deltas, legality changes, evidence-path changes
  RSCRRefs[]
    → задействованные RSCR/regression harness
  EmittedNotices[]
    → DeprecationNoticeId[], EditionBumpLogId[]
⟩
```

**На ферме:** после обновления NASEM-2001 → NASEM-2025 отчёт говорит:

- «Обновлены рационы для групп ВЫСОКАЯ и СРЕДНЯЯ (12 PathSlice). Рационы СУХОСТОЙНЫХ — без изменений (delta < ε). Протокол переходного периода — дополнен разделом DCAD (новое evidence). Отчёт опубликован как RRPT-2026-001».

---

## 4. Антипаттерны

| Антипаттерн | Проявление на ферме | Почему опасно | Как исправить |
|---|---|---|---|
| **Full-Rerun Mania** | «Вышла NASEM-2025 — пересчитываем всё» | Тратятся ресурсы на неизменённое; риск внесения ошибок | Scope closure: считать минимальное замыкание зависимостей |
| **Editionless Telemetry** | «Показатели изменились» — без указания редакции | Невозможно воспроизвести или сравнить | Каждый сигнал несёт `…Ref.edition` |
| **Alias-as-Semantics** | «Триггер Т3 сработал» — без канонического id | Фрагментация семантики; разные команды понимают по-разному | Использовать `RSCRTriggerKindId` из `G.Core` |
| **Silent Crossings** | Обновление меняет контекстные предположения без видимого CrossingBundle | Результат неприменим в другом контексте | Публиковать `CrossingBundle` при каждом обновлении |
| **Orchestration Smuggling** | «Для удобства» вводятся новые правила доминирования | Скрытая фрагментация спецификации | Политики — только через `PolicyId`, не через «удобство» |
| **Audit-Only Posture** | «Мы не обновляем, просто фиксируем устаревание» | Растёт эпистемический долг; решения принимаются на невалидных данных | RefreshQueue + RefreshPlan с планированием обновлений |

---

## 5. Пример на ферме: выход NASEM-2025

**Контекст:** Ферма «Орловское», 1500 голов, использует NASEM-2001 + дополнения. В январе 2026 выходит NASEM-2025.

**Step 1 — Ingestion (приём триггеров):**

```
RSCRTrigger := ⟨
  triggerKindId: RSCRTriggerKindId.EditionPinChange,
  scope: PatternScopeId.NASEM-BASED-RATIONS-2024,
  payloadPins: {
    oldEdition: NASEM-2001.v2,
    newEdition: NASEM-2025.v1,
    affectedCharacteristicIds: [ENERGY-REQ, DMI-PREDICTION, FATTY-ACID-PROFILE],
    sourcePath: PathSliceId_2026_01_NASEM_RELEASE
  }
⟩
```

**Step 2 — Scope Closure (замыкание зависимостей):**

Система анализирует EvidenceGraph и находит все PathSlice, которые зависят от NASEM-2001:

- `RATION-HIGH-YIELD-2024` → зависит от ENERGY-REQ, DMI-PREDICTION → **включить**
- `RATION-MEDIUM-YIELD-2024` → зависит от ENERGY-REQ → **включить**
- `RATION-DRY-COW-2024` → зависит от ENERGY-REQ, но FATTY-ACID-PROFILE не используется → **проверить delta**
- `RATION-HEIFER-2024` → не зависит от изменённых характеристик → **исключить**
- `PROTOCOL-TRANSITION-2024` → зависит от DCAD → **включить** (новое evidence в NASEM-2025)

**Step 3 — Planning (формирование плана):**

```
RefreshPlanId: RPLAN-2026-NASEM-001
TargetScope: [
  PathSliceId.RATION-HIGH-YIELD-2024,
  PathSliceId.RATION-MEDIUM-YIELD-2024,
  PathSliceId.PROTOCOL-TRANSITION-2024
]
PlannedTriggers: [RSCR-2026-001]
PlannedActions: [
  RecomputeSelectionOrSetSurface (G.5) для рационов,
  UpdateEvidenceBindings (G.6) для протокола,
  ReshipPack (G.10) для обновлённых pack
]
RequiredPins: {
  NASEM-2025.v1,
  POLICY-ENERGY-CALC.v3,
  UTS-ROW-2026-001
}
```

**Step 4 — Execution + Audit:**

Выполнение фиксируется как Work:

- Дата: 2026-02-15
- Исполнитель: `Petrova#NutritionistRole:Orlovskoye`
- Действия: пересчёт рационов, обновление evidence, переиздание pack
- Результат: `RefreshReportId: RRPT-2026-001`

**Step 5 — Deprecation + Edition Bump:**

```
DeprecationNoticeId: DEP-2026-001
  scope: RATION-HIGH-YIELD-2024 (old edition)
  reason: EditionPinChange (NASEM-2001 → NASEM-2025)
  successor: RATION-HIGH-YIELD-2026

EditionBumpLogId: EBL-2026-001
  oldEdition: NASEM-2001.v2
  newEdition: NASEM-2025.v1
  justification: RSCR-2026-001
```

---

## 6. Практика: с чего начать

**Шаг 1. Выберите один источник изменений.**
Что у вас регулярно меняется? Новые редакции NASEM? Сезонные данные? Изменения в стаде? Выберите один источник и опишите его как `RSCRTriggerKindId`.

**Шаг 2. Найдите зависимости.**
Возьмите один протокол или рацион. Какие evidence-пути от него ведут к изменяемому источнику? Запишите `PathSliceId`.

**Шаг 3. Сформируйте RefreshPlan.**
Не выполняйте обновление сразу. Сначала создайте план: что обновляется, почему, какие штифты нужны. Это `RefreshPlan@Context`.

**Шаг 4. Выполните и зафиксируйте.**
Сделайте обновление. Запишите результат как `RefreshReport@Context` с `ExecutedActions`, `ObservedDeltas`, `RSCRRefs`.

**Шаг 5. Опубликуйте DeprecationNotice.**
Если старая версия протокола устаревает — опубликуйте уведомление с указанием причины и преемника. Это предотвращает использование устаревших данных.

---

## 7. Проверь себя

| Вопрос | Если ответ «не знаю» — проблема |
|---|---|
| При выходе новой NASEM вы пересчитываете всё или только затронутое? | Full-Rerun Mania |
| Знаете ли вы, какие именно PathSlice зависят от NASEM-2001? | Отсутствие EvidenceGraph |
| Фиксируете ли вы причины обновления с каноническими id? | Alias-as-Semantics |
| Можете ли вы через год воспроизвести, почему был обновлён конкретный протокол? | Отсутствие RefreshReport |
| Публикуете ли вы уведомления об устаревании старых версий? | Audit-Only Posture |
| Проверяете ли вы, что обновление не меняет контекстных предположений скрытно? | Silent Crossings |

---

## 8. Связи

- **G.Core** — каталог RSCR-триггеров, `TriggerAliasMap`, Default Governing Definition Index.
- **G.6 (EvidenceGraph)** — `PathId/PathSliceId` — основа scope closure.
- **G.7 (Bridge Sentinels)** — при обновлении Bridge/CL/Φ требуется `RebindBridgeOrCrossing`.
- **G.9 (Parity Harness)** — parity rerun может быть запланирован через RefreshPlan.
- **G.10 (Shipping)** — `ReshipPack` — одно из действий обновления.
- **G.12 (Dashboards)** — `UpdateDashboardSlice` — обновление срезов дашбордов.
- **B.3.4 (Freshness/Decay)** — триггеры `FreshnessOrDecayEvent` поступают отсюда.
- **A.15 (Role–Method–Work)** — выполнение RefreshPlan — это Work с трассировкой.

---

## 9. Что читать дальше

- **G.11:Ext.LegacyTriggers** — докирование старых триггерных меток (T0…T7)
- **G.11:Ext.DecayAndDebt** — специфика свежести и эпистемического долга
- **G.11:Ext.QDRefreshWiring** — обновление QD-артефактов
- **FPF-Spec.md §G.11** — полная нормативная версия

---

*Этот capture создан в рамках WP-1 (Саморазвитие — изучение FPF) для PACK-cattle-science.*
*Цель: сделать архитектурный паттерн читаемым без погружения в 50 страниц спецификации.*
