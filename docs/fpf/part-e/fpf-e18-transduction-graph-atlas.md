---
type: fpf-study
pattern: E.18
title: "E.TGA: структура потока преобразований — выбирай, планируй, работай, обновляй"
domain: cattle-science
difficulty: advanced
reading_time: 50 min
created: 2026-06-27
fpf_context: ["E.18", "A.3.4", "A.6.0", "A.6.1", "A.15", "A.15.1", "A.20", "A.21", "A.6.4", "E.17", "F.9", "G.5", "G.11"]
---

# E.18 — E.TGA (Transduction Graph Atlas): структура потока преобразований — выбирай, планируй, работай, обновляй

> **Цель capture:** объяснить, как в FPF моделировать сложные цепочки преобразований так, чтобы переходы между контекстами, единицами измерения и design/run были видны, а обновления локализованы.

---

## 1. Зачем это читать

Если на ферме есть цепочка «выбрать метод → спланировать работу → выполнить → измерить → обновить протокол», и каждый раз забывают, где именно переходят от одного контекста к другому, — вы в зоне E.18. Этот паттерн учит моделировать сложные преобразования как выбранную структуру потока с явными loci, переходами и gate crossings.

> **FPF-тезис:** *«Flow — это не процедура и не граф. Flow — это valuation над структурой преобразований с явными gate crossings, path slices и edition pins.»*

**Фермерский пример:**

> Ферма внедряет систему раннего выявления кетоза. Поток: сенсор молока → алгоритм → предупреждение зоотехнику → ветеринарное обследование → лечение → повторный анализ. Но нигде не зафиксировано: где меняется `BoundedContext` (данные → решение), где меняется `ReferencePlane` (молоко → кровь), где происходит `GateCrossing` (решение о лечении). При аудите невозможно восстановить, на каком основании была принята каждая мера.

---

## 2. История одной ошибки

Ферма «Рассвет» построила «цифровой двойник стада». В него входили модель кормления, модель воспроизводства, модель здоровья и финансовая модель.

- Каждая модель работала в своём `ReferencePlane` (кг корма, дни отёла, процент заболеваний, рубли), и переходы между ними не были оформлены как `GateCrossing`.
- При обновлении одной модели приходилось переписывать всё, потому что не было `PathSlice` — локальных областей обновления.
- «Flow» воспринимался как единый prescribed workflow, хотя на самом деле это была структура, в которой могли быть разные пути.

E.18 разделяет **selected structure**, **flow valuation**, **path**, **path slice**, **gate crossing** и **publication face**. Это позволяет обновлять часть потока, не ломая всё.

---

## 3. Transformation Flow Structure — полное описание

### 3.1 Определение

**Transformation Flow Structure / Transduction Graph Atlas (E.18)** — это выбранная составная структура из atomic `U.Transformation` values и transformation-adjacent governed loci, связанных отношением `U.Transfer`, с типизацией loci, бюджетами `Γ_time`, Bridge/CL для cross-context crossings и `PublicationScope` для MVPK-лиц.

### 3.2 Почему это важно

Без E.18 сложные процессы описывают либо как жёсткие workflow (что ломается при изменениях), либо как набор независимых моделей (что скрывает переходы и потери). E.18 делает структуру reusable, comparable и auditable, позволяя локально обновлять отдельные slices.

### 3.3 TransformationFlowStructure и её loci

**Определение.** `TransformationFlowStructure` — это каркас, состоящий из **loci** разных видов: `Transformation`, `Signature`, `Mechanism`, `WorkPlanning`, `Work`, `Check`, `StructuralReinterpretation`. Между loci действует единственный тип переноса — `U.Transfer`.

**Пояснение.** Структура — это не метод, не work plan и не публикация. Это каркас, в котором размещаются эти элементы. Каждый locus имеет свой kind и не может быть заменён другим без явного `StructuralReinterpretation`.

**Пример из животноводства.**

> Структура «Управление тепловым стрессом» включает loci:
> - `Transformation`: переход коровы из `Normothermia` в `HeatStress` или обратно;
> - `Signature`: `THI_Calculation_v2` + `CowProfile` (порода, лактация, BCS);
> - `Mechanism`: `EvaporativeCoolingMechanism`, `ShadeMechanism`;
> - `WorkPlanning`: план работ по мониторингу THI, предоставлению воды, корректировке рациона;
> - `Work`: фактические измерения THI и действия персонала;
> - `Check`: `OperationalGate`: THI > 72 → активировать меры; THI > 78 → escalate;
> - `StructuralReinterpretation`: агрегация данных с уровня группы на уровень отдельной коровы.

**Ключевой признак.** Структура — это каркас с типизированными loci; она отделена от метода, плана работы и публикации.

### 3.4 Flow как valuation, а не процедура

**Определение.** **Flow** — это **valuation** `ν` над отношениями `U.Transfer` и cut-sets, вместе с допустимым путём `p` в структуре. Flow — не пошаговая инструкция, а функция, сопоставляющая transfer'ам значения (tokens, state) под текущим `CtxState`.

**Пояснение.** Для одной и той же структуры может быть несколько flow valuations: development-flow, application-flow, evaluation-flow. Это делает структуру reusable и позволяет сравнивать разные пути.

**Пример из животноводства.**

> Для структуры «Управление переходным периодом коровы» возможны:
> - **development-flow**: создание протокола;
> - **application-flow**: применение протокола к конкретной корове;
> - **evaluation-flow**: сбор evidence и возврат к обновлению протокола.
>
> Одинаковая структура, разные valuations.

**Ключевой признак.** Одинаковая структура допускает разные пути и valuations; это делает её reusable и comparable.

### 3.5 GateCrossing и CtxState

**Определение.** `GateCrossing` — типизированный переход на locus, который изменяет любой элемент `CtxState = ⟨L, P, E⃗, D⟩`: `L` — `U.BoundedContext`, `P` — `ReferencePlane`, `E⃗` — edition vector, `D` — `DesignRunTag`. Raw `U.Transfer` сохраняет `CtxState`; crossing происходит только на `OperationalGate(profile)`.

**Пояснение.** Crossing делает видимыми места, где меняется контекст, единица измерения, редакция или design/run stance. Каждый crossing публикует `CrossingBundle` с `BridgeCard`, `UTS row`, `CL`, `PublicationScopeId`, `PathSliceId`.

**Пример из животноводства.**

| Crossing | Что меняется | Пример |
|---|---|---|
| Context | `L` | Переход от группы к отдельной корове |
| ReferencePlane | `P` | Переход от молока (BHB косвенный) к крови (BHB прямой) |
| Edition | `E⃗` | Обновление `CG-Spec` кормления |
| Design/Run | `D` | Переход от планирования (`T^D`) к выполнению (`T^R`) |

**Ключевой признак.** Каждый crossing публикует `CrossingBundle` с Bridge/CL и локальными pins.

### 3.6 PathSlice и локальное обновление

**Определение.** `PathSlice` — это slice-scoped execution window. Когда меняется edition pin или срабатывает sentinel, re-emission затрагивает только тот `PathSlice`, который затронут изменением.

**Пояснение.** PathSlice позволяет локализовать обновления. Вместо переписывания всей структуры при изменении одного параметра обновляется только соответствующий slice, сохраняя остальные loci и flows стабильными.

**Пример из животноводства.**

> Если обновляется `ComparatorSet` для BHB, re-emission нужна только для slice `PS-BHB-Monitoring`, а не для всей структуры «Управление стадом». Аналогично, изменение формулы THI затрагивает только `PS-HeatStress-THI`.

**Ключевой признак.** Refresh локализован по `PathSlice`.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Наш цифровой поток кормления настроен и работает.»*

**Разложение по E.18:**

| Часть утверждения | Что это в FPF | Почему |
|---|---|---|
| «цифровой поток» | может означать `TransformationFlowStructure`, flow valuation, или просто IT-процесс | Нужно восстановить kind |
| «кормления» | `U.Method` / `U.Work` | Не путать со структурой |
| «настроен и работает» | functioning claim / Work claim | Требует `A.3.4`, `A.15` |

**Основные риски смешивания:**

1. **Путаница structure vs procedure.** Flow становится негибким «workflow».
2. **Скрытые crossings.** Переходы между контекстами/единицами не видны.
3. **Невозможность comparability.** Нельзя сравнить два потока без explicit structure и pins.
4. **Глобальные обновления.** Любое изменение вынуждает переписывать всё.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** описать структуру управления тепловым стрессом в жаркое время.

**Было (смешанное / нечёткое):**

> «Летом мы следим за коровами: включаем вентиляцию, даём больше воды, корректируем рацион.»

**Стало (разложенное / ясное):**

**TransformationFlowStructure:** `HeatStressManagement_v2`

**Loci:**

| Locus | Kind | FPF-значение |
|---|---|---|
| L1 | Transformation | Переход коровы из `Normothermia` в `HeatStress` или обратно |
| L2 | Signature | `THI_Calculation_v2` + `CowProfile` (порода, лактация, BCS) |
| L3 | Mechanism | `EvaporativeCoolingMechanism`, `ShadeMechanism` |
| L4 | WorkPlanning | `WP-HeatStress-2026` — мониторинг THI, вода, рацион |
| L5 | Work | Фактические измерения THI, действия персонала |
| L6 | Check | `OperationalGate`: THI > 72 → меры; THI > 78 → escalate |
| L7 | StructuralReinterpretation | Агрегация данных с уровня группы на уровень коровы |

**U.Transfer:**
> Перенос состояния между loci сохраняет `CtxState`. Например, измерение THI на L5 передаётся на L6 без изменения `ReferencePlane` (°C / % влажности).

**GateCrossings:**
> - `GC-1`: THI измерен в борозде (`ReferencePlane=ambient`) → адаптирован под конкретную корову (`ReferencePlane=animal-exposure`) с `BridgeCard` и `CL^plane`.
> - `GC-2`: `DesignRunTag` crossing: план мероприятий (`T^D`) → выполненные меры (`T^R`) на `LaunchGate`.

**PathSlice:**
> `PS-HeatStress-July2026` — slice для июля; при изменении `THI_Calculation_v2` re-emission только этого slice.

**MVPK faces:**
> - PlainView для владельца: «Когда жарко, мы снижаем тепловой стресс тремя способами».
> - TechCard для зоотехника: `THI thresholds`, `MethodRef`, `RoleAssignments`.
> - AssuranceLane для аудитора: `Work` refs, `BridgeCards`, `DecisionLog`.

**Результат:**
- Ясно, где происходят переходы между контекстами и единицами.
- Можно обновить THI-формулу, не переписывая весь протокол.
- Аудитор видит полный trace от данных до действий.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Выберите один комплексный процесс на ферме (переходный период, тепловой стресс, воспроизводство).

**Шаг 2.** Опишите его как `TransformationFlowStructure`: назовите loci, `U.Transfer`, `CtxState`.

**Шаг 3.** Для каждого locus определите kind: Transformation, Signature, Mechanism, WorkPlanning, Work, Check, StructuralReinterpretation.

**Шаг 4.** Найдите все crossings (изменения Context, ReferencePlane, Edition, Design/Run) и оформите их как `GateCrossing` с `CrossingBundle`.

**Шаг 5.** Определите `PathSlice`'ы — области локального обновления.

**Шаг 6.** Проверьте, что flow — это valuation, а не prescribed workflow: допустимы ли альтернативные пути?

**Шаг 7.** Опубликуйте MVPK faces для разных аудиторий, сохраняя source pins.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| «Flow» описан как единственная последовательность шагов? | Путаем flow valuation с prescribed workflow |
| Переходы между единицами/контекстами не оформлены как GateCrossing? | Скрытые потери и невосстановимость |
| Raw transfer меняет ReferencePlane или Edition? | Нарушение сохранения CtxState |
| Структура смешана с Method, WorkPlan или Publication? | Нарушение разделения kind'ов |
| Обновление одного параметра требует переписывания всей структуры? | Нет PathSlice-локализации |
| MVPK face добавляет новые claim'ы? | Semantic drift; face — проекция, не source |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.3.4 U.Transformation | bounded transformation в loci |
| A.6.0 U.Signature | signature loci |
| A.6.1 U.Mechanism | mechanism loci |
| A.15 U.Work / U.WorkPlan | work и work-planning loci |
| A.20 / A.21 Gate/Constraint | check loci и OperationalGate |
| A.6.4 U.EpistemicRetargeting | structural reinterpretation loci |
| C.2.1 EpistemeSlotRelation | CtxState и slots |
| E.17 MVPK | publication faces для структуры, path, crossing |
| F.9 Bridges & Congruence Levels | Bridge/CL для GateCrossings |
| G.5 / G.11 Selection & Refresh | selector locus и slice-scoped refresh |

---

## 9. Что запомнить

1. `TransformationFlowStructure` — каркас из типизированных loci, а не workflow.
2. Flow — это valuation над структурой; одна структура допускает разные пути.
3. `GateCrossing` делает видимыми изменения Context, ReferencePlane, Edition, Design/Run.
4. `PathSlice` локализует обновления.
5. MVPK faces публикуют структуру без добавления claim'ов.

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.18*
