---
type: fpf-study
pattern: C.22
title: "Selection Kernel: правильный выбор начинается с типизации задачи"
domain: cattle-science
difficulty: advanced
reading_time: 40 min
created: 2026-06-19
---

# C.22 — Selection Kernel

## 1. Зачем это читать

Если вы когда-нибудь видели, как на ферме **сравнивают два совершенно разных решения по «эффективности»**, не спросив: «А это вообще одна задача?» — вы встретили C.22 «в диком виде».

> **FPF-тезис:** *«Законful выбор возможен только после явной типизации задачи (TaskSignature). Нельзя сравнивать яблоки с апельсинами, смешивать ординальные и отношественные шкалы или выдавать скалярный победителя там, где остаётся частичный порядок.»*

C.22 — Problem Typing & TaskSignature Assignment (Problem-CHR). Это паттерн, который готовит задачу к выбору метода: не связывает метод заранее, но делает задачу достаточно типизированной, чтобы downstream selector (G.5) мог применить eligibility, acceptance и policy-governed choice.

**Фермерский пример:**

> Ферма выбирает между двумя протоколами профилактики кетоза: «пропиленгликоль в первые 5 дней» и «хром-пиколинат на весь переходный период». Зоотехник сравнивает «снижение BHB» и объявляет победителя. Но протоколы имеют разный TaskKind (один — короткое вмешательство, другой — долгосрочная добавка), разный Work target и разный evidence basis. C.22 требует сначала присвоить каждому TaskSignature, а потом сравнивать внутри совместимого frame.

---

## 2. История одной ошибки

Представьте ферму, где выбирают **модель прогноза кетоза**:

> «Модель X точность 87%, модель Y — 84%. Берём X.»

Через год приходит аудитор. Он спрашивает:

- «Какой TaskKind?» — Ответ: «Прогноз кетоза» (но это слишком широко: ранняя диагностика? риск-скоринг? триаж?)
- «Какие данные на входе?» — Ответ: «Разные» (но DataShape — часть TaskSignature; без неё сравнение незаконно).
- «Какая ObjectiveProfile?» — Ответ: «Точность» (но это ординальное/булево решение может важнее AUC; weighted sum запрещён).
- «Какой ReferencePlane?» — Ответ: «Не знаем» (но design-time и run-time метрики нельзя смешивать).

Аудитор уходит ни с чем. Потому что выбор **был сделан до типизации задачи**. C.22 предлагает: сначала TaskSignature, потом сравнение.

---

## 3. Selection Kernel — полное описание

### 3.1 TaskSignature (S2) — минимальная типизация

**Вопрос:** Что нужно знать о задаче, чтобы lawful выбрать метод?

**TaskSignature — это запись:**
```
⟨Context, TaskKind, TaskFamilyRef?, KindSet, DataShape, NoiseModel,
 ObjectiveProfile, Constraints, ScopeSlice(G), EvidenceGraphRef,
 Size/Scale, Freshness, Missingness, [опционально QD/OEE-поля]⟩
```

**На ферме:**
- **Context:** `HerdA_TransitionPeriod_2026`.
- **TaskKind:** `KetosisRiskPrediction`.
- **TaskFamilyRef:** `EarlyWarning_0-21_DIM`.
- **KindSet:** [U.Cow, U.BloodSample, U.MilkSample].
- **DataShape:** таблица {BHB, BCS, milk_yield, DIM} + история коровы.
- **NoiseModel:** MAR (Missing At Random) для пропусков BHB; iid для измерений при условии сезона.
- **ObjectiveProfile:** {↑ sensitivity@ratio, ↓ false_alarm_rate@ratio, lexicographic: sensitivity ≻ specificity}.
- **Constraints:** {budget ≤ X, inference_time ≤ 1 min, local_deployment = true}.
- **ScopeSlice(G):** коровы фермы А, 0–21 DIM, BHB крови или молока.
- **EvidenceGraphRef:** журнал измерений, калибровки, исследования.
- **Size/Scale:** n ≈ 500 коров/год, 10 признаков.
- **Freshness:** модель переобучается каждый квартал.
- **Missingness:** MAR.

**Ключевой признак:** TaskSignature **не связывает метод**. Она только описывает задачу достаточно для admissible selection.

### 3.2 CHR-типизация: нет среднего по ординальным шкалам

**Вопрос:** Какие операции допустимы над характеристиками?

**На ферме:**
- **Sensitivity** — ratio, можно сравнивать отношения.
- **Specificity** — ratio, но не путать с precision.
- **UsabilityScore** (1–5) — ordinal, нельзя усреднять, нельзя взвешивать с ratio.
- **DeploymentReadiness** (ready / not_ready) — nominal.

**Ключевой признак:** Если ObjectiveProfile содержит mixed-scale характеристики, selector должен вернуть Pareto set, а не scalar winner.

### 3.3 Tri-state unknowns

**Вопрос:** Что делать с неизвестным?

**На ферме:**
- Если DataShape = unknown → eligibility может быть degrade/abstain/sandbox.
- Если NoiseModel = unknown → нельзя делать inference без явного предположения.
- Если ShiftClass = unknown → результат для другого сезона не переносится без Bridge.

**Ключевой признак:** Unknown не приводится к 0 или false молча. Поведение должно быть явным в Acceptance profile.

### 3.4 Crossings: Bridge + CL → R_eff only

**Вопрос:** Как перенести TaskSignature в другой контекст?

**На ферме:**
- TaskSignature для фермы А переносится на ферму Б через Bridge с CL=2.
- F и G не штрафуются. G пересчитывается через translate(Bridge, ·).
- R_eff падает на Φ(CL).

**Ключевой признак:** Перенос задачи — это не копирование. Scope может сузиться, reliability — упасть.

### 3.5 QD и Illumination extensions

**Вопрос:** Что добавлять, если задача — open-ended search?

**На ферме:**
- **CharacteristicSpaceRef** (d≥2): {yield, cost, robustness}.
- **ArchiveConfig:** grid/CVT, K=1, InsertionPolicy.
- **EmitterPolicyRef:** ссылка на C.19.
- **DominanceRegime:** ParetoOnly по умолчанию.
- **IlluminationSummary:** report-only telemetry.

**Ключевой признак:** Illumination не входит в dominance без явной CAL-политики.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Возьмём снова:

> *«Модель X точность 87%, модель Y — 84%. Берём X.»*

**Разложение по C.22:**

| Часть утверждения | Что это в FPF | Почему ошибка |
|---|---|---|
| «точность 87%» | **Одиночная ratio характеристика** | Игнорируются ObjectiveProfile, Constraints, DataShape |
| «Модель X» и «Модель Y» | **Разные MethodFamilies** | Нет TaskSignature, нет Eligibility comparison |
| «Берём X» | **Скалярный выбор без Pareto check** | Может быть, Y доминирует по скорости/стоимости |
| Отсутствие TaskKind | **Нетипизированная задача** | «Прогноз кетоза» — слишком широко |

**Что плохого в смешивании:**

1. **Неправильный метод для задачи.** Модель X может быть точнее, но не работать локально.
2. **Несравнимые сущности.** Разные входные данные, разные TaskKind.
3. **Потеря trade-offs.** Один критерий скрывает другие.

---

## 5. Как это выглядит на ферме: правильное применение

Перепишем выбор модели прогноза кетоза.

**Было (смешанное):**
> «Модель X — 87%, модель Y — 84%. Берём X.»

**Стало (типизированное):**

**TaskSignature S2-Ketosis-HerdA:**
> Context: HerdA_Transition_2026  
> TaskKind: KetosisRiskPrediction  
> TaskFamilyRef: EarlyWarning_0-21_DIM  
> KindSet: [U.Cow, U.BloodSample, U.MilkSample]  
> DataShape: tabular, {BHB, BCS, yield, DIM, season}, MAR missingness  
> NoiseModel: iid conditional on season  
> ObjectiveProfile: {↑ sensitivity@ratio, ↓ false_alarm_rate@ratio, ↑ inference_speed@ratio}, lexicographic: sensitivity ≻ false_alarm_rate  
> Constraints: {budget ≤ 200K руб, local_inference = true, explainable = true}  
> ScopeSlice(G): коровы HerdA, 0–21 DIM  
> EvidenceGraphRef: A.10-REF-789  
> Size/Scale: n~500/год, 10 features  
> Freshness: quarterly retrain  
> Missingness: MAR

**Eligibility:**
- Модель Z (cloud-only) → **abstain** (constraint local_inference = false).
- Модель X (87% accuracy, local, black-box) → **degrade** (constraint explainable = true не выполнен, но может быть waived).
- Модель Y (84% accuracy, local, explainable) → **admit**.

**Selection:**
- Если ObjectiveProfile требует explainable, Y может доминировать X, несмотря на lower accuracy.
- Если waive explainable, X остаётся на фронте.
- Selector возвращает Pareto set с trade-notes.

**Что это даёт:**
- Выбор обоснован не одной цифрой, а типизированной задачей.
- Ограничения работают как gates, а не как afterthought.
- Результат auditable: видно, почему отсеяна Z и почему X vs Y — фронт.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Опишите задачу одним предложением, не называя метода.

**Шаг 2.** Заполните TaskSignature:
- Context, TaskKind, TaskFamilyRef.
- DataShape, NoiseModel, ObjectiveProfile, Constraints.
- ScopeSlice(G), EvidenceGraphRef, Size/Scale, Freshness, Missingness.

**Шаг 3.** Проверьте CHR-admissibility: нет средних по ординальным, нет unit mixing.

**Шаг 4.** Проверьте Eligibility каждого метода/модели.

**Шаг 5.** Если objective mixed-scale — возвращайте Pareto set, не scalar winner.

**Шаг 6.** На crossing'ах добавьте Bridge + CL → R_eff only.

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
|---------|-------|
| A.2.6 USM | ScopeSlice(G) — set-valued scope |
| A.18 CSLC | CHR-типизация и scale legality |
| C.16 Measurement | Measures[CHR] в ObjectiveProfile |
| C.17–C.19 Search/Select | QD-поля в TaskSignature |
| G.5 Multi-Method Dispatcher | Потребитель TaskSignature |
| G.4 Acceptance | Acceptance-gate thresholds |
| F.9 Bridges | Cross-context TaskSignature reuse |

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §C.22*
