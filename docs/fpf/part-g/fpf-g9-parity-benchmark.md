---
type: fpf-study
pattern: G.9
title: "Parity Harness: сравнение методов под одним baseline"
domain: cattle-science
difficulty: advanced
reading_time: 28 min
created: 2026-06-27
fpf_context: ["G.9", "G.5", "G.0", "G.7", "G.Core", "G.11"]
---

# G.9 — Parity Harness: сравнение методов под одним baseline

> **Цель capture:** объяснить, как паттерн G.9 сравнивает методы под единым baseline, freshness window и comparator set, публикуя ParityPlan@Context и ParityReport@Context, которые можно воспроизвести.

---

## 1. Зачем это читать

В скотоводстве часто сравнивают методы, которые изначально оценивались в разных условиях: разные временные окна, разные породы, разные исходы. Без явного baseline и pinned comparator set такое сравнение некорректно. Parity Harness фиксирует всё, что должно быть постоянным, чтобы сравнение было воспроизводимым и CSLC-законным.

> **FPF-тезис:** *«Parity возможна только тогда, когда baseline, freshness, comparator и bridge pins зафиксированы заранее.»*

**Фермерский пример:**

> Фермер сравнивает две системы раннего выявления кетоза: анализатор BHB в крови и молочный тест. ParityPlan фиксирует: baseline set = коровы FarmA, Holstein, дни 1–30 лактации; freshness window = 2023–2025; ComparatorSpecRef.edition = 1.0; bridge pins = BC-001 (BHB ↔ молочный тест). Без этого плана сравнение чувствительности и специфичности было бы некорректным.

---

## 2. История одной ошибки

Хозяйство решило заменить лабораторный BHB на новый молочный тест, потому что «исследования показывают хорошую чувствительность». При проверке выяснилось, что исследование молочного теста проводилось на Jersey в позднюю лактацию, а лабораторный BHB — на Holstein в раннюю лактацию. Baseline set и freshness window не совпадали, поэтому сравнение чувствительности не имело смысла. Parity Harness мог бы потребовать единый baseline до начала сравнения.

---

## 3. Parity Harness — полное описание

### 3.1 Определение

**Parity Harness** — это паттерн, который планирует и выполняет сравнение методов под явно зафиксированным baseline, freshness window, comparator set и bridge pins, публикуя ParityPlan@Context и ParityReport@Context.

### 3.2 Почему это важно

Сравнения методов часто оказываются невоспроизводимыми, потому что разные исследования используют разные окна, породы и исходы. Parity Harness делает эти параметры явными и pinned, чтобы downstream потребитель мог понять, что было постоянным, а что — telemetry.

### 3.3 ParityPlan@Context

**Определение.** ParityPlan@Context — это planning record, который фиксирует: entity of concern, ReferencePlane, BaselineSet, BaselineBindingRef, FreshnessWindows, CNSpecRef.edition, CGSpecRef.edition, ComparatorSpecRef.edition, SCPRef.edition, MinimalEvidenceRef.edition, ParityPinSet и optional планируемые slot fillings.

**Пояснение.** ParityPlan — это не результат, а условия сравнения. Он говорит: «мы будем сравнивать эти методы при этих фиксированных условиях».

**Пример из животноводства.**

```text
PP-001: ParityPlan@Context
  - entityOfConcern: cows FarmA, Holstein, days 1–30 lactation
  - ReferencePlane: world
  - BaselineSet: {Lab_BHB, Milk_Ketone_Test}
  - BaselineBindingRef: BBR-001 (herd records 2023–2025)
  - FreshnessWindows: 2023-01-01..2025-12-31
  - CGSpecRef.edition: 1.0
  - ComparatorSpecRef.edition: 1.0
  - ParityPinSet: {BridgeCard BC-001, Φ(CL)=POL-001}
```

**Ключевой признак.** ParityPlan содержит все pins, необходимые для воспроизведения сравнения.

### 3.4 ParityPinSet

**Определение.** ParityPinSet — это набор идентификаторов edition, policy и bridge, необходимых для воспроизводимости parity run.

**Пояснение.** ParityPinSet включает ComparatorSpecRef.edition, bridge pins (BridgeCardId, CL, Φ/Ψ/Φ_plane), normalization method ids (UNM_id), и mode-specific pins (DHC, QD, OEE) через Extensions.

**Пример из животноводства.**

```text
ParityPinSet for PP-001:
  - ComparatorSpecRef.edition = 1.0
  - BridgeCardId = BC-001
  - CL = 2
  - Φ(CL) = POL-001
  - DHCMethodRef.edition = 2.1 (if DHC parity used)
```

**Ключевой признак.** ParityPinSet содержит только id-значения; семантика определяется в referenced patterns.

### 3.5 ParityReport@Context

**Определение.** ParityReport@Context — это publication record, который фиксирует результат parity run: baseline, freshness, active pins, outcome refs, abstain reasons, telemetry summary, guard outcome trace, evidence trace, crossing pins, edition/policy deltas и RSCR refs.

**Пояснение.** ParityReport не является gate decision или audit performance; он документирует, что произошло под зафиксированными условиями. Он должен позволить rerun.

**Пример из животноводства.**

```text
PR-001: ParityReport@Context
  - ParityPlanId: PP-001
  - BaselineSet: {Lab_BHB, Milk_Ketone_Test}
  - OutcomeRefs: Pareto-shortlist {Lab_BHB, Milk_Ketone_Test}
  - AbstainReasons: []
  - TelemetrySummary: sensitivity difference = +5% (report-only)
  - EvidenceTrace: EG-001, PathId [P-001, P-002]
  - CrossingPins: BC-001, CL=2, Φ(CL)=POL-001
  - EditionPinsDelta: none
  - RSCRRefs: [RSCR-001]
```

**Ключевой признак.** ParityReport echo'ит все активные pins и outcome shape.

### 3.6 Equal windows and budgets

**Определение.** ParityPlan должен объявить единое FreshnessWindows для всех baseline; если используется Budgeting, оно должно быть общим.

**Пояснение.** Сравнение методов под разными окнами или бюджетами некорректно. ParityPlan фиксирует единое окно, чтобы исключить это искажение.

**Пример из животноводства.** Если Lab_BHB оценивался на данных 2020–2024, а Milk_Ketone_Test — на 2023–2025, ParityPlan требует пересечение или явное justification для неравных окон.

**Ключевой признак.** FreshnessWindows одинаково применяется ко всем BaselineSet.

### 3.7 Telemetry vs dominance

**Определение.** Illumination, coverage, regret и другие telemetry signals остаются report-only по умолчанию. Любое продвижение telemetry в dominance требуетявной CAL policy id.

**Пояснение.** Parity Harness не превращает вспомогательные метрики в критерии выбора. Если фермер хочет, чтобы coverage влиял на выбор, это должно быть явно объявлено в CAL и зафиксировано в audit pins.

**Пример из животноводства.** Разница в чувствительности 5% — это telemetry. Она не делает один метод доминирующим, если в CAL нет policy, которая это утверждает.

**Ключевой признак.** Telemetry summary отделена от outcome/dominance; promotion требует CAL policy id.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Новый тест лучше, потому что в последнем исследовании у него чувствительность 95 %.»*

**Разложение по G.9:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «новый тест» | MethodFamilyId | Должен быть в BaselineSet |
| «лучше» | dominance claim | Требует ParityPlan с общим baseline |
| «последнее исследование» | freshness window | Должно совпадать с другими baseline |
| «95 %» | telemetry metric | Не доминирование без CAL policy |

**Основные риски смешивания:**

1. **Разные окна.** «Последнее исследование» может относиться к другому контексту.
2. **Скрытое доминирование.** Одна метрика превращается в общий вывод.
3. **Невоспроизводимость.** Без ParityPinSet нельзя повторить сравнение.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** сравнение двух методов скрининга кетоза.

**Было (смешанное / нечёткое):**
> «Новый молочный тест лучше, потому что чувствительность выше.»

**Стало (разложенное / ясное):**

**ParityPlan PP-001:**
> BaselineSet = {Lab_BHB, Milk_Ketone_Test}
> entity of concern = FarmA Holstein days 1–30
> FreshnessWindows = 2023–2025
> ComparatorSpecRef.edition = 1.0
> ParityPinSet = {BC-001, CL=2, Φ(CL)=POL-001}

**ParityReport PR-001:**
> Outcome = Pareto-shortlist {Lab_BHB, Milk_Ketone_Test}
> Telemetry = sensitivity difference +5% (report-only)
> EvidenceTrace = EG-001, PathId [P-001, P-002]
> RSCRRefs = [RSCR-001]

**Результат:**
- Сравнение проводится под едиными условиями.
- Telemetry не превращается в dominance.
- Отчёт можно перепроверить rerun.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Определите BaselineSet и зафиксируйте BaselineBindingRef.

**Шаг 2.** Установите единое FreshnessWindows и ComparatorSpecRef.edition.

**Шаг 3.** Укажите ParityPinSet: bridge pins, normalization ids, mode-specific pins.

**Шаг 4.** Запустите selector (G.5) и зафиксируйте outcome refs.

**Шаг 5.** Опубликуйте ParityReport@Context со всеми активными pins и evidence trace.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| BaselineSet не зафиксирован или не опирается на evidence? | Сравнение некорректно. |
| FreshnessWindows различается для разных baseline? | Сравнение методов несопоставимо. |
| ParityReport не echo'ит ParityPinSet? | Результат невоспроизводим. |
| Telemetry используется как dominance без CAL policy? | Нарушена telemetry-vs-dominance separation. |
| Crossing pins отсутствуют при cross-tradition parity? | Нарушена bridge visibility. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| G.5 Method Dispatcher | предоставляет selected-set outcomes для parity |
| G.0 CG-Spec | задаёт ComparatorSet, SCP, MinimalEvidence |
| G.7 Bridge Calibration | предоставляет BridgeCards и BCT для cross-tradition parity |
| G.11 Telemetry Refresh | потребляет RSCRRefs из ParityReport |
| G.Core | гарантирует set-return, equal handling и default citation |

---

## 9. Что запомнить

1. ParityPlan фиксирует baseline, freshness, comparator и bridge pins.
2. ParityReport echo'ит активные pins и outcome shape.
3. FreshnessWindows и Budgeting должны быть общими для всех baseline.
4. Telemetry остаётся report-only; promotion в dominance требует CAL policy.
5. Parity — это method of obtaining outputs, а не gate decision.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.9*
