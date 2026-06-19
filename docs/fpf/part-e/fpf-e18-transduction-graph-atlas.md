---
type: fpf-study
pattern: E.18
title: "E.TGA: структура потока преобразований — выбирай, планируй, работай, обновляй"
domain: cattle-science
difficulty: advanced
reading_time: 60 min
created: 2026-06-19
---

# E.18 — E.TGA (Transduction Graph Atlas): структура потока преобразований — выбирай, планируй, работай, обновляй

## 1. Зачем это читать

Если на вашей ферме есть цепочка: «выбрать метод → спланировать работу → выполнить → измерить → обновить протокол», — и каждый раз вы забываете, где именно переходите от одного контекста к другому, — вы в зоне E.18. Этот паттерн учит **моделировать сложные преобразования как выбранную структуру потока с явными loci, переходами и gate crossings**.

**FPF-тезис:** *«Flow — это не процедура и не граф. Flow — это valuation над структурой преобразований с явными gate crossings, path slices и edition pins.»*

В животноводстве многие процессы — это потоки: корм → пищеварение → метаболизм → молоко; семя → отёл → лактация → сухостой; данные → аналитика → решение → действие. E.18 даёт единую дисциплину описывать их так, чтобы они были сопоставимы, auditable и локально обновляемы.

**Фермерский пример:**

> Ферма внедряет систему раннего выявления кетоза. Поток выглядит так: сенсор молока → алгоритм → предупреждение зоотехнику → ветеринарное обследование → лечение → повторный анализ. Но нигде не зафиксировано: где меняется `BoundedContext` (данные → решение), где меняется `ReferencePlane` (молоко → кровь), где происходит `GateCrossing` (решение о лечении). В результате при аудите невозможно восстановить, на каком основании была принята каждая мера.

E.18 превращает этот поток в `TransformationFlowStructure`: loci, `U.Transfer`, gates, path slices, edition pins.

## 2. История одной ошибки

Ферма «Рассвет» построила «цифровой двойник стада». В него входили:

- модель кормления,
- модель воспроизводства,
- модель здоровья,
- финансовая модель.

Казалось бы, всё связано. Но на практике:

- Каждая модель работала в своём `ReferencePlane` (кг корма, дни отёла, процент заболеваний, рубли), и переходы между ними не были оформлены как `GateCrossing`.
- При обновлении одной модели приходилось переписывать всё, потому что не было `PathSlice` — локальных областей обновления.
- «Flow» воспринимался как единый prescribed workflow, хотя на самом деле это была структура, в которой могли быть разные пути.

E.18 разделяет **selected structure**, **flow valuation**, **path**, **path slice**, **gate crossing** и **publication face**. Это позволяет обновлять часть потока, не ломая всё.

## 3. Transformation Flow Structure — полное описание

> **Соответствие с FPF-Spec.** В реестре паттерн назван *E.TGA (Transduction Graph Atlas)*. В спецификации FPF он развивается под именем *Transformation Flow Structure* — см. §E.18. Capture сохраняет registry-название E.TGA в заголовке, но все normative ссылки ведут к §E.18.

### 3.1 Что такое TransformationFlowStructure

**Вопрос:** Что является EntityOfConcern в E.18?

**Ответ:** **Выбранная составная структура** (`TransformationFlowStructure`) из atomic `U.Transformation` values и transformation-adjacent governed loci. Структура содержит:
- **Loci** — позиционированные loci разных видов: Transformation, Signature, Mechanism, WorkPlanning, Work, Check, StructuralReinterpretation;
- **U.Transfer** — единственный тип отношения переноса в структуре;
- **tau_L / tau_Transfer** — типизация loci и transfer'ов;
- **Γ_time** — бюджеты и горизонты;
- **Bridge + CL** — для cross-context crossings;
- **PublicationScope** — для MVPK-лиц.

**На ферме:**
> Структура «Управление переходным периодом коровы» включает loci:
> - `Transformation`: изменение метаболического статуса коровы (сухостой → ранняя лактация);
> - `Signature`: формальный профиль коровы (порода, номер лактации, BCS);
> - `Mechanism`: механизм адаптации печени к отрицательному энергетическому балансу;
> - `WorkPlanning`: план работ по мониторингу BHB и Ca²⁺;
> - `Work`: фактические измерения и корректировки рациона;
> - `Check`: gate на принятие решения о лечении;
> - `StructuralReinterpretation`: перенос данных с уровня группы на уровень отдельной коровы.

**Ключевой признак:** структура — это не метод, не work plan и не публикация; это каркас, в котором размещаются эти элементы.

### 3.2 Flow как valuation, а не процедура

**Вопрос:** В чём разница между flow и TransformationFlowStructure?

**Ответ:** **Flow** — это **valuation** `ν` над отношениями `U.Transfer` и cut-sets, вместе с допустимым путём `p` в структуре. Flow — не «пошаговая инструкция», а функция, сопоставляющая transfer'ам значения (tokens, state) под текущим `CtxState`.

**На ферме:**
> Для одной и той же структуры «Управление переходным периодом» может быть несколько flow valuations:
> - **development-flow**: создание протокола;
> - **application-flow**: применение протокола к конкретной корове;
> - **evaluation-flow**: сбор evidence и возврат к обновлению протокола.

**Ключевой признак:** одинаковая структура допускает разные пути и valuations; это делает её reusable и comparable.

### 3.3 GateCrossing и CtxState

**Вопрос:** Что считается crossing в структуре?

**Ответ:** `GateCrossing` — типизированный переход на locus, который изменяет любой элемент `CtxState = ⟨L, P, E⃗, D⟩`:
- `L` — `U.BoundedContext` (Context);
- `P` — `ReferencePlane` (единицы измерения);
- `E⃗` — edition vector (CG-Spec, ComparatorSet, TransportRegistry^Φ и др.);
- `D` — `DesignRunTag` (design `T^D` ↔ run `T^R`).

Raw `U.Transfer` **сохраняет** `CtxState`; crossing происходит только на `OperationalGate(profile)`.

**На ферме:**
| Crossing | Что меняется | Пример |
|---|---|---|
| Context | `L` | Переход от группы к отдельной корове |
| ReferencePlane | `P` | Переход от молока (BHB косвенный) к крови (BHB прямой) |
| Edition | `E⃗` | Обновление `CG-Spec` кормления |
| Design/Run | `D` | Переход от планирования (`T^D`) к выполнению (`T^R`) |

**Ключевой признак:** каждый crossing публикует `CrossingBundle` с `BridgeCard`, `UTS row`, `CL`, `PublicationScopeId`, `PathSliceId`.

### 3.4 PathSlice и локальное обновление

**Вопрос:** Как обновлять структуру, не переписывая всё?

**Ответ:** Через **PathSlice** — slice-scoped execution window. Когда меняется edition pin или срабатывает sentinel, re-emission затрагивает только тот `PathSlice`, который затронут изменением.

**На ферме:**
> Если обновляется `ComparatorSet` для BHB, re-emission нужна только для slice `PS-BHB-Monitoring`, а не для всей структуры «Управление стадом».

**Ключевой признак:** refresh локализован по `PathSlice`.

## 4. Почему смешивать / игнорировать — значит рисковать

Возьмём фразу: *«Наш цифровой поток кормления настроен и работает.»*

**Разложение по E.18:**

| Часть утверждения | Что это в FPF | Почему |
|---|---|---|
| «цифровой поток» | может означать `TransformationFlowStructure`, flow valuation, или просто IT-процесс | Нужно восстановить kind |
| «кормления» | `U.Method` / `U.Work` | Не путать со структурой |
| «настроен и работает» | functioning claim / Work claim | Требует `A.3.4`, `A.15` |

**Что плохого в смешивании:**

1. **Путаница structure vs procedure.** Flow становится негибким «workflow».
2. **Скрытые crossings.** Переходы между контекстами/единицами не видны.
3. **Невозможность comparability.** Нельзя сравнить два потока без explicit structure и pins.
4. **Глобальные обновления.** Любое изменение вынуждает переписывать всё.

## 5. Как это выглядит на ферме: правильное применение

**Задача:** описать структуру управления тепловым стрессом в жаркое время.

**Было (смешанное / нечёткое):**
> «Летом мы следим за коровами: включаем вентиляцию, даём больше воды, корректируем рацион.»

**Стало (разложенное / ясное):**

**TransformationFlowStructure:** `HeatStressManagement_v2`

**Loci:**
| Locus | Kind | FPF-значение |
|---|---|---|
| L1 | Transformation | Переход коровы из состояния `Normothermia` в `HeatStress` или обратно |
| L2 | Signature | `THI_Calculation_v2` + `CowProfile` (порода, лактация, BCS) |
| L3 | Mechanism | `EvaporativeCoolingMechanism`, `ShadeMechanism` |
| L4 | WorkPlanning | `WP-HeatStress-2026` — мониторинг THI, предоставление воды, корректировка рациона |
| L5 | Work | Фактические измерения THI, фактические действия персонала |
| L6 | Check | `OperationalGate`: THI > 72 → активировать меры; THI > 78 → escalate |
| L7 | StructuralReinterpretation | Агрегация данных с уровня борозды/группы на уровень коровы |

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

**Что это даёт:**
- Ясно, где происходят переходы между контекстами и единицами.
- Можно обновить THI-формулу, не переписывая весь протокол.
- Аудитор видит полный trace от данных до действий.

## 6. Практическое применение: с чего начать

**Шаг 1.** Выберите один комплексный процесс на ферме (переходный период, тепловой стресс, воспроизводство).

**Шаг 2.** Опишите его как `TransformationFlowStructure`: назовите loci, `U.Transfer`, `CtxState`.

**Шаг 3.** Для каждого locus определите kind: Transformation, Signature, Mechanism, WorkPlanning, Work, Check, StructuralReinterpretation.

**Шаг 4.** Найдите все crossings (изменения Context, ReferencePlane, Edition, Design/Run) и оформите их как `GateCrossing` с `CrossingBundle`.

**Шаг 5.** Определите `PathSlice`'ы — области локального обновления.

**Шаг 6.** Проверьте, что flow — это valuation, а не prescribed workflow: допустимы ли альтернативные пути?

**Шаг 7.** Опубликуйте MVPK faces для разных аудиторий, сохраняя source pins.

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| «Flow» описан как единственная последовательность шагов? | Путаем flow valuation с prescribed workflow. |
| Переходы между единицами/контекстами не оформлены как GateCrossing? | Скрытые потери и невосстановимость. |
| Raw transfer меняет ReferencePlane или Edition? | Нарушение сохранения CtxState. |
| Структура смешана с Method, WorkPlan или Publication? | Нарушение разделения kind'ов. |
| Обновление одного параметра требует переписывания всей структуры? | Нет PathSlice-локализации. |
| MVPK face добавляет новые claim'ы? | Semantic drift; face — проекция, не source. |

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.3.4 U.Transformation | bounded transformation в loci. |
| A.6.0 U.Signature | signature loci. |
| A.6.1 U.Mechanism | mechanism loci. |
| A.15 U.Work / U.WorkPlan | work и work-planning loci. |
| A.20 / A.21 Gate/Constraint | check loci и OperationalGate. |
| A.6.4 U.EpistemicRetargeting | structural reinterpretation loci. |
| C.2.1 EpistemeSlotRelation | CtxState и slots. |
| E.17 MVPK | publication faces для структуры, path, crossing. |
| F.9 Bridges & Congruence Levels | Bridge/CL для GateCrossings. |
| G.5 / G.11 Selection & Refresh | selector locus и slice-scoped refresh. |

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.18*
