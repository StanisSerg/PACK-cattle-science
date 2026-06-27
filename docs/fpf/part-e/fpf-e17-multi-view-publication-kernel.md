---
type: fpf-study
pattern: E.17
title: "MVPK: публикуй одну и ту же идею разным читателям без потери смысла"
domain: cattle-science
difficulty: advanced
reading_time: 45 min
created: 2026-06-27
fpf_context: ["E.17", "E.17.0", "E.17.1", "E.17.2", "A.6.2", "A.6.3", "A.7", "C.2.1", "E.10", "E.18", "F.18", "A.10", "B.3"]
---

# E.17 — Multi-View Publication Kernel (MVPK): публикуй одну и ту же идею разным читателям без потери смысла

> **Цель capture:** объяснить, как в FPF публиковать одно и то же знание для разных аудиторий так, чтобы каждая публикация оставалась проекцией источника и не добавляла новых claim'ов.

---

## 1. Зачем это читать

Если одно и то же решение на ферме приходится объяснять владельцу простыми словами, ветеринару — по клиническим пунктам, программисту — в формате данных, а аудитору — через evidence trail, вы уже делаете multi-view publication. E.17 учит делать это не создавая каждый раз новый claim, а порождая разные faces от одного и того же source episteme.

> **FPF-тезис:** *«Publication — это проекция, а не новое знание. Лицо (face) должно помогать читать, но не добавлять семантику.»*

**Фермерский пример:**

> Ферма ввела новый протокол кормления свеженадоенных коров. Владельцу показали презентацию: «более здоровый старт лактации». Ветеринару дали Excel-таблицу с BHB и Ca. Программисту — JSON со списком ингредиентов. Аудитор попросил evidence trail — и выяснилось, что в презентации указана одна дата внедрения, в Excel — другая, в JSON — третья. MVPK требует: все три face проецируются от одного source episteme.

---

## 2. История одной ошибки

Ферма «Нива» разработала «стандарт доения» и опубликовала его тремя способами:

- **SOP для операторов** — говорил «доить 3 раза в день».
- **Отчёт для банка** — говорил «производительность выросла на 12 %».
- **API для сенсоров** — содержал другой порядок шагов.

Когда аудитор сравнил документы:

- SOP не содержал edition pin и был датирован 2024 годом.
- Отчёт для банка содержал цифру 12 %, но без comparator set и reference plane.
- API использовал другой `MethodRef`, потому что разработчик понял задачу иначе.

Получилось три разных «знания» вместо одного. MVPK решает эту проблему: каждый face — проекция одного source, и каждый face указывает на тот же `U.Episteme` или `U.View`.

---

## 3. Multi-View Publication Kit — полное описание

### 3.1 Определение

**Multi-View Publication Kernel / Kit (E.17)** — это паттерн публикации, который порождает typed projection от существующего source episteme или view в виде набора faces (`PlainView`, `TechCard`, `InteropCard`, `AssuranceLane`), управляемых `publication face/form`, `PublicationVPId`, `PublicationScope` и source pins, без добавления новых claim'ов.

### 3.2 Почему это важно

Без MVPK разные аудитории получают независимые тексты, которые со временем расходятся: даты, пороги, роли и claim'ы перестают совпадать. MVPK фиксирует один источник и делает каждую публикацию проверяемой проекцией, сохраняя traceability и предотвращая semantic drift.

### 3.3 Publication, presentation, rendering и representation

**Определение.** В MVPK различают четыре вида деятельности:
- **Publication** — типизированная проекция от source к face;
- **Presentation** — риторическая аранжировка published carrier, не добавляющая claim'ов;
- **Rendering** — графический/визуальный layout carrier;
- **Representation** — отношение episteme к referent'у, governed by C.2.1 / A.6.2–A.6.4.

**Пояснение.** MVPK занимается только publication. Presentation и rendering — это work над carriers; representation — отдельная онтическая работа. Смешение их приводит к тому, что внешний вид документа начинает нести скрытые claim'ы.

**Пример из животноводства.**

| Термин | Смысл в FPF | Пример на ферме |
|---|---|---|
| Publication | typed projection from source to face | `PlainView` протокола отёла |
| Presentation | arrangement of carrier | порядок слайдов для совета |
| Rendering | graphical layout | PDF-верстка карточки |
| Representation | отношение к реальности | `MilkYield` как `Characteristic` коровы |

**Ключевой признак.** MVPK face не создаёт нового claim; оно помогает читать существующий.

### 3.4 Четыре canonical face

**Определение.** MVPK-Max определяет четыре canonical publication face: `PlainView` (P) — для не-технического читателя; `TechCard` (T) — техническая карточка для специалиста; `InteropCard` (I) — форма для машинного обмена; `AssuranceLane` (A) — evidence trail для аудита.

**Пояснение.** Каждый face выбирает подмножество source и формат, подходящий аудитории, но не меняет смысл. PlainView может опускать детали, TechCard фокусируется на методах и порогах, InteropCard — на структуре данных, AssuranceLane — на доказательствах и решениях.

**Пример из животноводства.**

| Face | Читатель | Что содержит | Чего не содержит |
|---|---|---|---|
| PlainView | Владелец фермы | «Что изменилось и зачем» | Технические детали без расшифровки |
| TechCard | Зоотехник | MethodRef, thresholds, roles | Новые numeric claims без source |
| InteropCard | Программист | Структура данных, edition pins | Интерпретация или business logic |
| AssuranceLane | Аудитор | Evidence refs, gate decisions, DRR | Неподтверждённые выводы |

**Ключевой признак.** Каждый face помечен `publication-face kind`, `PublicationVPId`, `PublicationScope` и source pins.

### 3.5 Source pinning и no-new-claims

**Определение.** Каждый face обязан ссылаться на source `U.Episteme` или `U.View`, содержать edition pins, reference plane, unit, scale для numeric claims и не вводить новых claim'ов.

**Пояснение.** Если face вводит новую цифру, оценку, gate decision или comparator set, это уже не publication problem — это claim, который должен быть оформлен через соответствующий паттерн (evidence, gate, work, decision, assurance). No-new-claims — главный инвариант MVPK.

**Пример из животноводства.**

> TechCard для протокола переходного периода должен содержать:
> - `sourceEpistemeRef`: `TransitionCowProtocol_v4`
> - `PublicationVPId`: `NutritionistVP`
> - `PublicationScope`: `FarmA.Internal`
> - `editionPins`: `CG-Spec_2026_v2`, `ComparatorSet_FarmA_30d`
> - `faceKind`: `TechCard`
>
> Не должно содержать: «ожидаемый прирост удоя 5 %» без отсылки к `B.3` assurance или `C.11` decision.

**Ключевой признак.** Если face вводит новый claim, это не publication problem — это claim needs its own FPF pattern.

### 3.6 Compositionality

**Определение.** В morphism profile MVPK публикует `U.Morphism`. Face'ы должны коммутировать с композицией: face от `g∘f` должен соответствовать композиции face'ов от `f` и `g`. Это сохраняет traceability при составных изменениях.

**Пояснение.** Если изменение рациона и изменение графика доения — два morphism'а, то их композиция — новый протокол. MVPK требует, чтобы TechCard для композиции был явно связан с TechCard'ами составляющих, а не переписан заново.

**Пример из животноводства.**

> Изменение рациона (`f`) и изменение графика доения (`g`) — два morphism'а. Их композиция `g∘f` — новый протокол. MVPK требует, чтобы TechCard для `g∘f` был явно связан с TechCard для `f` и TechCard для `g`, чтобы при изменении одного из них была видна цепочка re-emission.

**Ключевой признак.** Составные arrow'ы публикуются композиционно, а не как новые истории.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Презентация для банка показывает, что проект успешен.»*

**Разложение по E.17:**

| Часть утверждения | Что это в FPF | Почему |
|---|---|---|
| «Презентация» | MVPK face (likely PlainView) | Допустимо, если source-pinned |
| «показывает, что проект успешен» | overread | Publication face не может сама по себе доказывать успех |
| «успешен» | quality/evaluative claim | Требует `C.16.Q`, `B.3` assurance или `C.11` decision |

**Основные риски смешивания:**

1. **Semantic drift.** Face начинает нести claim'ы, которых нет в source.
2. **Непроверяемость.** Цифры на слайде не привязаны к evidence path.
3. **Множественные истины.** Один и тот же вопрос имеет разные ответы в разных face'ах.
4. **Регуляторный риск.** Аудитор находит несоответствие между PlainView и AssuranceLane.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** опубликовать изменение протокола кормления свеженадоенных коров.

**Было (смешанное / нечёткое):**

> Для владельца: «улучшим старт лактации». Для зоотехника: Excel-таблица. Для программиста: JSON. Для аудитора: куча распечаток.

**Стало (разложенное / ясное):**

**Source episteme:**
> `U.Episteme`: `TransitionCowProtocol_v4`
> `DescriptionContext`: ⟨`EntityOfConcern=FarmA.TransitionCows`, `BoundedContext=FarmA`, `Viewpoint=NutritionVP`⟩

**MVPK faces:**

**PlainView (P)**
> `PublicationVPId`: `OwnerVP`
> `PublicationScope`: `FarmA.BoardReport`
> `sourceEpistemeRef`: `TransitionCowProtocol_v4`
> Содержание: «С 1 июля вводится протокол переходного периода: рацион согласовывается за 21 день до отёла, контролируются BHB и Ca²⁺. Цель — снизить клинический кетоз.»

**TechCard (T)**
> `PublicationVPId`: `NutritionistVP`
> `PublicationScope`: `FarmA.InternalSOP`
> `sourceEpistemeRef`: `TransitionCowProtocol_v4`
> Содержание: `MethodRef`, `RoleAssignments`, `CharacteristicSpace` {BHB, Ca²⁺, NEFA}, thresholds, edition pins.

**InteropCard (I)**
> `PublicationVPId`: `SoftwareVP`
> `PublicationScope`: `FarmA.API`
> `sourceEpistemeRef`: `TransitionCowProtocol_v4`
> Содержание: schema с `protocolId`, `edition`, `feedIngredients[]`, `thresholds[]`, `measurementSchedule[]`.

**AssuranceLane (A)**
> `PublicationVPId`: `AuditorVP`
> `PublicationScope`: `FarmA.AuditPack`
> `sourceEpistemeRef`: `TransitionCowProtocol_v4`
> Содержание: evidence refs (`HerdLog`, `LabReports`), `DRR` link, `GateDecision` refs, `Work` refs.

**Результат:**
- Все four faces указывают на один source.
- Ни один face не вводит новых claim'ов.
- При изменении `TransitionCowProtocol_v4` все faces re-emitted с новыми edition pins.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Выберите одно решение или протокол на ферме, который нужно объяснять разным аудиториям.

**Шаг 2.** Опишите его как source episteme: `U.Episteme`, `EntityOfConcern`, `DescriptionContext`, claim graph.

**Шаг 3.** Определите аудитории и выберите face kind для каждой: PlainView, TechCard, InteropCard, AssuranceLane. Не все four обязательны одновременно — выбирайте по нужде.

**Шаг 4.** Для каждого face укажите:
- `PublicationVPId` (viewpoint);
- `PublicationScope` (где face используется);
- `sourceEpistemeRef` (источник);
- `publication-face kind`;
- edition pins, reference plane, unit/scale для numeric claims.

**Шаг 5.** Проверьте, что face не добавляет новых claim'ов. Если хочется добавить — создайте отдельный evidence/gate/work/decision record.

**Шаг 6.** При изменении source пересоздайте faces с новыми pins (re-emission).

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Face содержит цифру, не привязанную к source edition и reference plane? | Unpinned numeric claim; нарушение MVPK discipline |
| PlainView делает выводы вроде «успешно» или «эффективно» без отсылки на assurance/decision? | Overread; quality claim требует `C.16.Q` / `B.3` / `C.11` |
| Один и тот же термин в разных faces означает разное? | Semantic drift; faces не проекции одного source |
| TechCard перечисляет I/O заново вместо ссылки на source? | Нарушение no-new-claims |
| InteropCard содержит business logic или interpretation? | Interop face должен быть data-only |
| AssuranceLane делает выводы, а не указывает evidence refs? | AssuranceLane — trail, не judgment |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| E.17.0 U.MultiViewDescribing | базовая онтология viewpoints, views, correspondences |
| E.17.1 / E.17.2 ViewpointBundle / TEVB | библиотеки viewpoint'ов для engineering faces |
| A.6.2–A.6.4 Epistemic Morphing | morphism profile MVPK: face'ы композиционны |
| A.7 Strict Distinction | разделение publication lane от episteme, carrier, work |
| C.2.1 EpistemeSlotRelation | source episteme и view slots |
| E.10 LEX-BUNDLE | lexical discipline для publication wording |
| E.18 Transformation Flow Structure | publication faces для path/crossing/structure |
| F.18 Naming Discipline | durable names для face kinds и viewpoint ids |
| A.10 Evidence Graph Referring | evidence refs в AssuranceLane |
| B.3 F-G-R Trust Framework | assurance claims, если face их цитирует |

---

## 9. Что запомнить

1. Publication — это проекция source, а не новое знание.
2. MVPK-Max определяет четыре face: PlainView, TechCard, InteropCard, AssuranceLane.
3. Каждый face должен быть source-pinned и не добавлять claim'ов.
4. Presentation и rendering — это work над carrier, не part of MVPK publication semantics.
5. Составные изменения публикуются композиционно.

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.17*
