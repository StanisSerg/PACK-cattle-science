---
type: fpf-study
pattern: C.22
title: "Selection Kernel: правильный выбор начинается с типизации задачи"
domain: cattle-science
difficulty: advanced
reading_time: 35 min
created: 2026-06-27
fpf_context: ["C.22", "A.18", "C.16", "C.17-C.19", "G.5", "F.9"]
---

# C.22 — Selection Kernel: правильный выбор начинается с типизации задачи

> **Цель capture:** объяснить, почему в FPF выбор метода или модели возможен только после явной типизации задачи через TaskSignature, и как избежать незаконного смешения шкал и скалярных победителей.

---

## 1. Зачем это читать

Если на ферме сравнивают два совершенно разных решения по «эффективности», не спросив: «А это вообще одна задача?» — это C.22 «в диком виде». Problem Typing & TaskSignature Assignment (Problem-CHR) готовит задачу к выбору метода: не связывает метод заранее, но делает задачу достаточно типизированной, чтобы downstream selector мог применить eligibility, acceptance и policy-governed choice.

> **FPF-тезис:** *«Законный выбор возможен только после явной типизации задачи (TaskSignature). Нельзя сравнивать яблоки с апельсинами, смешивать ординальные и отношественные шкалы или выдавать скалярного победителя там, где остаётся частичный порядок.»*

**Фермерский пример:**

> Ферма выбирает между двумя протоколами профилактики кетоза: «пропиленгликоль в первые 5 дней» и «хром-пиколинат на весь переходный период». Зоотехник сравнивает «снижение BHB» и объявляет победителя. Но протоколы имеют разный TaskKind, разный Work target и разный evidence basis. C.22 требует сначала присвоить каждому TaskSignature, а потом сравнивать внутри совместимого frame.

---

## 2. История одной ошибки

Ферма выбирала модель прогноза кетоза. Инженер заявил: «Модель X точность 87 %, модель Y — 84 %. Берём X». Через год выяснилось, что X — облачная модель, а ферма требовала локального развёртывания; Y была интерпретируемой, а X — чёрным ящиком; данные на входе у моделей различались; accuracy не учитывала, что ложные срабатывания дороже пропусков. Сравнение было сделано до типизации задачи. Если бы ферма заполнила TaskSignature, она увидела бы, что X не удовлетворяет constraints и что trade-offs требуют Pareto set.

---

## 3. Selection Kernel — полное описание

### 3.1 Определение

C.22 — это паттерн присвоения типизированной `TaskSignature` задаче перед тем, как выбирать метод или модель. TaskSignature описывает контекст, вид задачи, данные, целевой профиль, ограничения, scope, evidence, масштаб, freshness и модель пропусков. Она не связывает метод, но делает выбор admissible.

### 3.2 Почему это важно

Без TaskSignature сравнение методов становится сравнением несравнимого. Разные входные данные, разные TaskKind, смешение design-time и run-time метрик, усреднение ординальных и ratio шкал — всё это приводит к неправильному выбору и потере trade-offs.

### 3.3 TaskSignature

**Определение.** `TaskSignature` — это минимальная типизация задачи, достаточная для lawful selection. Она включает Context, TaskKind, TaskFamilyRef, KindSet, DataShape, NoiseModel, ObjectiveProfile, Constraints, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness и Missingness.

**Пояснение.** TaskSignature не говорит, какой метод выбрать. Она описывает задачу так, чтобы можно было проверить eligibility каждого метода и вернуть Pareto set, если objective смешанномасштабный.

**Пример из животноводства.** Для прогноза кетоза:
> Context: `HerdA_TransitionPeriod_2026`
> TaskKind: `KetosisRiskPrediction`
> TaskFamilyRef: `EarlyWarning_0-21_DIM`
> KindSet: [U.Cow, U.BloodSample, U.MilkSample]
> DataShape: таблица {BHB, BCS, milk_yield, DIM} + история коровы
> NoiseModel: MAR для пропусков BHB; iid для измерений при условии сезона
> ObjectiveProfile: {↑ sensitivity@ratio, ↓ false_alarm_rate@ratio}, lexicographic: sensitivity ≻ specificity
> Constraints: {budget ≤ X, inference_time ≤ 1 min, local_deployment = true, explainable = true}
> ScopeSlice(G): коровы фермы А, 0–21 DIM
> EvidenceGraphRef: A.10-REF-789
> Size/Scale: n ≈ 500 коров/год, 10 признаков
> Freshness: модель переобучается каждый квартал
> Missingness: MAR

**Ключевой признак.** TaskSignature задаёт вопрос «что за задача?», а не «какой метод лучше?».

### 3.4 CHR-типизация: нет среднего по ординальным шкалам

**Определение.** ObjectiveProfile должен соблюдать шкальную легальность из `A.18 CSLC`. Ординальные и ratio характеристики нельзя усреднять или складывать.

**Пояснение.** Если objective содержит mixed-scale характеристики, selector должен вернуть Pareto set, а не scalar winner. Скрытая скаляризация — незаконная агрегация.

**Пример из животноводства.** Sensitivity — ratio, можно сравнивать отношения. UsabilityScore (1–5) — ordinal, нельзя усреднять. DeploymentReadiness (ready / not_ready) — nominal. Если ObjectiveProfile требует и sensitivity, и usability, selector возвращает front с trade-notes.

**Ключевой признак.** Если objective содержит mixed scales, появляется Pareto set.

### 3.5 Tri-state unknowns

**Определение.** Если какой-либо элемент TaskSignature неизвестен, допустимые ответы: `pass`, `degrade`, `abstain` или `sandbox`. Unknown нельзя приводить к 0 или false молча.

**Пояснение.** Например, если DataShape неизвестен, eligibility может быть `degrade` или `abstain`. Если NoiseModel неизвестен, нельзя делать inference без явного предположения. Если ShiftClass неизвестен, результат для другого сезона не переносится без Bridge.

**Пример из животноводства.** Модель Z — облачная, но constraint требует local_deployment = true. Eligibility: `abstain`. Модель X — чёрный ящик, но explainable = true. Eligibility: `degrade` (может быть waived явно).

**Ключевой признак.** Unknown не превращается в 0; поведение должно быть явным в Acceptance profile.

### 3.6 Crossings: Bridge + CL → R_eff

**Определение.** При переносе TaskSignature в другой контекст используется Bridge с Congruence Level. G пересчитывается через translate(Bridge, ·), а R_eff падает на Φ(CL).

**Пояснение.** Перенос задачи — это не копирование. Scope может сузиться, reliability — упасть. F и G не штрафуются напрямую, но G транслируется.

**Пример из животноводства.** TaskSignature для фермы А переносится на ферму Б через Bridge с CL = 2. F остаётся F3; G сужается до доступных признаков и условий фермы Б; R_eff = R_base × Φ(2).

**Ключевой признак.** При переносе задачи всегда нужен Bridge и пересчёт R_eff.

### 3.7 QD и Illumination extensions

**Определение.** Если задача — open-ended search, TaskSignature дополняется CharacteristicSpaceRef, ArchiveConfig, EmitterPolicyRef, DominanceRegime и IlluminationSummary.

**Пояснение.** IlluminationSummary — report-only telemetry. Она не входит в dominance без явной CAL-политики.

**Пример из животноводства.** Для подбора рациона CharacteristicSpaceRef = {yield, cost, robustness}. ArchiveConfig = grid/CVT, K = 1. DominanceRegime = ParetoOnly.

**Ключевой признак.** Если в задаче много кандидатов и многокритериальность — нужны QD-поля.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Модель X точность 87 %, модель Y — 84 %. Берём X.»*

**Разложение по C.22:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «точность 87 %» | одиночная ratio характеристика | Игнорируются ObjectiveProfile, Constraints, DataShape |
| «Модель X» и «Модель Y» | разные MethodFamilies | Нет TaskSignature, нет Eligibility comparison |
| «Берём X» | скалярный выбор без Pareto check | Может быть, Y доминирует по скорости/стоимости |
| отсутствие TaskKind | нетипизированная задача | «Прогноз кетоза» — слишком широко |

**Основные риски смешивания:**

1. **Неправильный метод для задачи.** Модель X точнее, но не работает локально.
2. **Несравнимые сущности.** Разные входные данные, разные TaskKind.
3. **Потеря trade-offs.** Один критерий скрывает другие.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** ферма выбирает модель прогноза кетоза.

**Было (смешанное / нечёткое):**

> «Модель X — 87 %, модель Y — 84 %. Берём X.»

**Стало (типизированное):**

**TaskSignature S2-Ketosis-HerdA:**
> Context: `HerdA_Transition_2026`
> TaskKind: `KetosisRiskPrediction`
> TaskFamilyRef: `EarlyWarning_0-21_DIM`
> KindSet: [U.Cow, U.BloodSample, U.MilkSample]
> DataShape: таблица {BHB, BCS, yield, DIM, season}, MAR missingness
> NoiseModel: iid conditional on season
> ObjectiveProfile: {↑ sensitivity@ratio, ↓ false_alarm_rate@ratio, ↑ inference_speed@ratio}, lexicographic: sensitivity ≻ false_alarm_rate
> Constraints: {budget ≤ 200K руб., local_inference = true, explainable = true}
> ScopeSlice(G): коровы HerdA, 0–21 DIM
> EvidenceGraphRef: A.10-REF-789
> Size/Scale: n ~ 500/год, 10 признаков
> Freshness: quarterly retrain
> Missingness: MAR

**Eligibility:**
> Модель Z (cloud-only) → `abstain` (local_inference = false).
> Модель X (87 % accuracy, local, black-box) → `degrade` (explainable = true не выполнен, но может быть waived).
> Модель Y (84 % accuracy, local, explainable) → `admit`.

**Selection:**
> Если ObjectiveProfile требует explainable, Y может доминировать X, несмотря на lower accuracy.
> Если waive explainable, X остаётся на фронте.
> Selector возвращает Pareto set с trade-notes.

**Результат:**
- Выбор обоснован не одной цифрой, а типизированной задачей.
- Ограничения работают как gates, а не как afterthought.
- Результат auditable: видно, почему отсеяна Z и почему X vs Y — front.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Опишите задачу одним предложением, не называя метода.

**Шаг 2.** Заполните TaskSignature: Context, TaskKind, TaskFamilyRef, DataShape, NoiseModel, ObjectiveProfile, Constraints, ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness.

**Шаг 3.** Проверьте CHR-admissibility: нет средних по ординальным, нет unit mixing.

**Шаг 4.** Проверьте Eligibility каждого метода/модели.

**Шаг 5.** Если objective mixed-scale — возвращайте Pareto set, не scalar winner.

**Шаг 6.** На crossing'ах добавьте Bridge + CL → R_eff.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Сравниваете ли методы без TaskSignature? | Нетипизированный выбор |
| Смешиваете ли design-time и run-time метрики? | DesignRunTag chimera |
| Используете ли weighted sum для mixed scales? | Незаконная агрегация |
| Есть ли unknown, приведённые к 0? | Скрытая coercion |
| Возвращает ли selector всегда одного победителя? | Потеря Pareto front |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.2.6 USM | ScopeSlice(G) — set-valued scope |
| A.18 CSLC | CHR-типизация и scale legality |
| C.16 Measurement | Measures[CHR] в ObjectiveProfile |
| C.17–C.19 Search/Select | QD-поля в TaskSignature |
| G.5 Multi-Method Dispatcher | Потребитель TaskSignature |
| G.4 Acceptance | Acceptance-gate thresholds |
| F.9 Bridges | Cross-context TaskSignature reuse |

---

## 9. Что запомнить

1. Сначала TaskSignature, потом выбор метода.
2. TaskSignature не связывает метод, но делает выбор lawful.
3. Mixed-scale objective → Pareto set.
4. Unknown ≠ 0; используйте pass/degrade/abstain/sandbox.
5. Перенос TaskSignature требует Bridge и R_eff.

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §C.22*
