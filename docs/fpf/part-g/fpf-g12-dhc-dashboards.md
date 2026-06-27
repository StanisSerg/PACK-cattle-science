---
type: fpf-study
pattern: G.12
title: "DHC Dashboards: дисциплинарно-здоровые дашборды с evidence-путями"
domain: cattle-science
difficulty: advanced
reading_time: 28 min
created: 2026-06-27
fpf_context: ["G.12", "C.21", "G.Core", "G.6", "G.11", "G.3"]
---

# G.12 — DHC Dashboards: дисциплинарно-здоровые дашборды с evidence-путями

> **Цель capture:** объяснить, как паттерн G.12 превращает DHC slots из C.21 в edition-pinned, evidence-citable time series и view-only dashboard slices, которые можно обновлять выборочно.

---

## 1. Зачем это читать

В скотоводстве дашборды часто превращаются в набор красивых графиков без явной связи с источниками и методами. «Средний BHB по стаду», «уровень зрелости протокола», «плотность bridge'ов» — все эти метрики могут быть полезны, но только если видно, как они получены, какие шкалы используются и какие edition pins зафиксированы. G.12 делает дашборды reproducible artefacts, а не screenshots.

> **FPF-тезис:** *«Dashboard value имеет смысл только вместе с DHC slot, method edition, evidence path и reference plane.»*

**Фермерский пример:**

> Фермер видит на дашборде, что «средний BHB стада снизился за месяц». Без G.12 он не знает, какой метод измерения использовался, какие коровы входили в выборку, и какой freshness window применялся. С G.12 каждая точка ряда сопровождается DHCMethodRef.edition, PathSliceId и Γ_time, и фермер может проверить вычисление.

---

## 2. История одной ошибки

Хозяйство внедрило dashboard метаболического здоровья. Один из показателей — «средний уровень риска кетоза» — строился по ординальной шкале риска, и система вычисляла среднее. Никто не заметил, что ординальная шкала не допускает усреднения. Руководство принимало решения на основе тренда «среднего риска», который математически не имел смысла. G.12 мог бы запретить такую агрегацию через legality matrix.

---

## 3. DHC Dashboards — полное описание

### 3.1 Определение

**DHC Dashboards** — это паттерн, который определяет dashboard kit surfaces (DHCSeries@Context, DHCRow@Context, DashboardSlice@Context, DHCTelemetryPin) для вычисления и публикации discipline-health time series, привязанных к C.21 slots, с evidence paths и edition-aware refresh.

### 3.2 Почему это важно

Dashboards часто смешивают шкалы, скрывают нормализацию и превращают множественные результаты в scalar headlines. G.12 запрещает недопустимую арифметику, требует pinned method editions и сохраняет set-return semantics. Это делает dashboards auditable и refreshable.

### 3.3 DHCSeries@Context

**Определение.** DHCSeries@Context — это UTS-published time series для заданного Discipline × ContextSlice, построенная из C.21 DHC slots и привязанная к method/spec editions.

**Пояснение.** Series фиксирует TargetSlice (USM tuple), DHCSlotId[], DHCMethodSpecRef.edition, WindowSpec и ReferencePlane. Она не содержит interpretation thresholds; они живут в CAL.

**Пример из животноводства.**

```text
DS-001: DHCSeries@Context
  - TargetSlice: FarmA, Holstein, transition_period
  - DHCSlotId: [SLOT-001 BHB, SLOT-002 BCS, SLOT-003 ReproducibilityRate]
  - DHCMethodSpecRef.edition: 1.3
  - CNSpecRef.edition: 1.2
  - CGSpecRef.edition: 1.0
  - WindowSpec: 7-day rolling
```

**Ключевой признак.** DHCSeries содержит TargetSlice, DHCSlotId[], method/spec editions и ReferencePlane.

### 3.4 DHCRow@Context

**Определение.** DHCRow@Context — это одна временная точка/окно в DHCSeries с value, scale/unit, stance (pass/degrade/abstain), method editions и PathSliceId.

**Пояснение.** Каждая строка — это run-time Work/Audit-citable artefact. Stance не означает acceptance decision; он показывает, может ли строка быть вычислена/доверена при текущих evidence.

**Пример из животноводства.**

```text
DR-001: DHCRow@Context
  - DHCSeriesId: DS-001
  - Γ_time: 2026-06-19
  - DHCSlotId: SLOT-001 BHB
  - value: 1.1
  - units: mmol/L
  - stance: pass
  - DHCMethodRef.edition: 2.1
  - PathSliceId: [PS-001]
```

**Ключевой признак.** DHCRow имеет value, stance, method edition и PathSliceId.

### 3.5 DashboardSlice@Context

**Определение.** DashboardSlice@Context — это view-only grouping over DHCSeries/DHCRow. Она не вводит новой агрегации или legality semantics.

**Пояснение.** Slice — это проекция уже вычисленных строк. Она может группировать, аннотировать и визуализировать, но не может пересчитывать значения или изменять scale legality.

**Пример из животноводства.**

```text
DASH-001: DashboardSlice@Context
  - DHCSeriesId: [DS-001]
  - IncludedRowIds: [DR-001, DR-002, DR-003]
  - SliceAnnotations: «BHB trend, FarmA, June 2026»
```

**Ключевой признак.** DashboardSlice содержит series/row ids и annotations; не содержит operators.

### 3.6 DHCTelemetryPin

**Определение.** DHCTelemetryPin — это emitted refresh input с canonical RSCRTriggerKindId, scope (PathSliceId/PatternScopeId) и payload pins (editions, policies, UTS row ids).

**Пояснение.** DHCTelemetryPin позволяет G.11 планировать slice-scoped refresh. Он не является частью dashboard view; он — wiring pin.

**Пример из животноводства.**

```text
TP-001: DHCTelemetryPin
  - triggerKindId: EditionPinChange
  - scope: PS-001
  - payloadPins: {DHCMethodRef.edition=2.1→2.2, policy-id=POL-003}
```

**Ключевой признак.** DHCTelemetryPin несёт canonical trigger kind, scope и payload pins.

### 3.7 No illicit arithmetic

**Определение.** Dashboard pipeline не должен выполнять недопустимую арифметику над ординальными или категориальными шкалами; любая операция должна быть разрешена CN-Spec/CG-Spec и ссылаться на scale-legal operator.

**Пояснение.** «Средний уровень зрелости» или «средний BCS» — типичные ошибки. G.12 требует, чтобы каждая агрегация была явно разрешена и имела operator id.

**Пример из животноводства.** Для BHB (ratio scale) допустим weekly mean. Для BCS (ordinal scale) допустима только медиана или rank comparison; mean запрещён.

**Ключевой признак.** Каждая числовая операция имеет scale-legal operator ref и SCP permission.

### 3.8 Set-return preserved

**Определение.** Если dashboard потребляет selector set-result outputs, он должен сохранять set-return semantics; scalar headline — это view projection, не legality-bearing decision.

**Пояснение.** Dashboard может визуализировать Pareto-архив или shortlist, но не должен скрыто выбирать «победителя». Любое продвижение telemetry в dominance требует CAL policy id.

**Пример из животноводства.** Dashboard показывает Pareto-набор методов профилактики кетоза по осям cost/efficacy. Он не может объявить «лучший метод» без CAL policy.

**Ключевой признак.** Selector-derived dashboard panels сохраняют множественность и цитируют DominanceRegime/PortfolioMode defaults.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«На дашборде видно, что средний риск кетоза снизился.»*

**Разложение по G.12:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «средний риск» | illicit arithmetic | Риск — ординальная/категориальная шкала; mean недопустим |
| «снизился» | trend claim | Требует pinned method edition и Γ_time |
| «на дашборде» | DashboardSlice | View-only projection |

**Основные риски смешивания:**

1. **Ложная тенденция.** Среднее по ординальной шкале создаёт видимость тренда.
2. **Edition drift.** Без pinned method edition изменение метода выглядит как изменение phenomenon.
3. **Telemetry→dominance.** Trend превращается в решение безявной политики.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** dashboard метаболического здоровья для переходного периода.

**Было (смешанное / нечёткое):**
> «Средний риск кетоза по стаду за месяц.»

**Стало (разложенное / ясное):**

**DHCSeries DS-001:**
> TargetSlice = FarmA, Holstein, transition_period
> DHCSlotId = [SLOT-001 BHB, SLOT-002 BCS]
> DHCMethodSpecRef.edition = 1.3

**DHCRow DR-001:**
> Γ_time = 2026-06-19, SLOT-001 BHB, value 1.1, stance pass, PathSliceId PS-001.

**DHCRow DR-002:**
> Γ_time = 2026-06-19, SLOT-002 BCS, value median=3, stance pass, PathSliceId PS-002.

**DashboardSlice DASH-001:**
> series DS-001, rows DR-001..DR-030, annotation «BHB trend, FarmA, June 2026».

**DHCTelemetryPin TP-001:**
> EditionPinChange, scope PS-001, payload DHCMethodRef.edition.

**Результат:**
- Каждая точка привязана к методу и evidence path.
- Ординальные шкалы не усредняются.
- Refresh возможен по slice.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Выберите DHCSlotId[] из C.21 для вашей дисциплины.

**Шаг 2.** Определите TargetSlice, ReferencePlane и Γ_time regime.

**Шаг 3.** Закрепите DHCMethodSpecRef.edition и DHCMethodRef.edition для каждого slot.

**Шаг 4.** Вычисляйте rows, используя scale-legal operators, и сохраняйте PathSliceId.

**Шаг 5.** Публикуйте DashboardSlice как view-only projection и emit DHCTelemetryPin для G.11.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Dashboard выполняет арифметику над ординальными шкалами? | Нарушение no-illicit-arithmetic. |
| DHCRow не содержит PathSliceId? | Значение не проверяемо. |
| Method edition не закреплён? | Невозможно отличить тренд от drift. |
| DashboardSlice пересчитывает значения? | Slice должна быть view-only. |
| Telemetry не keyed by PathSliceId? | Refresh становится глобальным. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| C.21 | определяет DHC slots и методы |
| G.3 CHR Authoring | предоставляет характеристики и шкалы для DHCSlotId |
| G.6 Evidence Graph | предоставляет PathSliceId для rows |
| G.11 Telemetry Refresh | потребляет DHCTelemetryPin |
| G.Core | гарантирует set-return, no-illicit-arithmetic и default citation |

---

## 9. Что запомнить

1. DHC Dashboards строятся из C.21 DHC slots.
2. Каждая DHCRow pinned к method edition и PathSliceId.
3. DashboardSlice — view-only projection, не пересчитывает значения.
4. Ординальные/категориальные шкалы не допускают illicit arithmetic.
5. DHCTelemetryPin делает dashboards refreshable через G.11.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.12*
