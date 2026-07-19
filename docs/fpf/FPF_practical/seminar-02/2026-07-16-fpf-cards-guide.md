---
type: fpf-study-guide
title: "Как работают карточки в FPF"
wp: 109
domain: cattle-science
difficulty: beginner
reading_time: 15 min
created: 2026-07-16
fpf_context: ["E.11", "E.11.PUA", "C.22.2", "C.32.P2S", "F.18", "C.30.AD"]
---

# Как работают карточки в FPF

> **Цель:** объяснить, какие карточки есть в FPF, зачем они нужны и как по ним работать. Материал рассчитан на человека, который проходит практический курс FPF (WP-109) и хочет отличать публичные входные карточки от внутренних результатов паттернов.

---

## 1. Что такое карточки в FPF

FPF — не линейный учебник и не чек-лист. Это язык паттернов для трудной работы: когда обычного обсуждения недостаточно, чтобы сохранить смысл между людьми, командами, инструментами и временем.

**Карточки в FPF — это не бумажки для бюрократии, а инструменты мышления.** Каждая карточка:

- распознаёт ситуацию («что сейчас происходит»);
- задаёт точный вопрос («что именно нужно получить»);
- указывает на прямой паттерн FPF («какой паттерн решает эту задачу»);
- фиксирует точный первый результат («что можно использовать дальше»);
- задаёт границу («где остановиться или вернуться»).

FPF различает два слоя карточек:

1. **Публичные практические карточки (15 practical-use cards).** Это входные точки для человека, который пришёл со своим рабочим вопросом. Они описаны в публичном `Readme.md` и в паттерне `E.11 Practical-Use Guidance and Pattern Discovery`.
2. **Внутренние карточки-результаты паттернов.** Это артефакты, которые порождаются при применении конкретного паттерна: `ProblemCard@Context`, `NameCard`, `ProblemToStructureArchitecturingFlowCard@Project`, `ArchitectureDescriptionUseCard@Project` и другие.

> **Важно:** публичная карточка — это ситуация + шаблон. Внутренняя карточка — это структурированный результат, который получается после применения паттерна.

---

## 2. Пятнадцать публичных практических карточек

Эти карточки — не пошаговый план, а 15 семантических ключей. Каждый ключ соответствует типичному проектному вопросу. Начинают не с первой карточки, а с той, которая описывает текущую ситуацию.

| Карточка | Вопрос, который она задаёт | Типичный первый результат |
|----------|---------------------------|----------------------------|
| **ARCHITECTURE** | Архитектурное давление проблемы есть, но структура ещё не ясна. Что делать первым? | `ProblemToStructureArchitecturingFlowCard@Project` (C.32.P2S) или `ArchitectureDescriptionUseCard@Project` (C.30.AD) |
| **WORKING-DOCUMENTS** | Нужен документ, который другой участник сможет использовать. Какой именно? | Claim Register, U.MethodDescription, U.Commitment, U.WorkPlan, CallPlan, evidence-provenance graph, NameCard, publication face |
| **OPTION-COMPARISON** | Есть несколько вариантов. Что с ними делать: сравнивать, сохранить пул, выбрать? | EvaluationCharacteristicSpaceSpec, ExplorationArchiveRecord, PoolPolicyResult, Shortlist, ChoiceResult |
| **PROBLEM-SHAPING** | Что-то важно, но это ещё ранний сигнал, маршрут или готовая проблема? | U.PreArticulationCuePack, RoutedCueSet, U.AbductivePrompt, `ProblemCard@Context` |
| **IMPROVEMENT** | Нужно улучшить объект. Что для этого должно быть согласовано? | QualityEvaluationQuestionFrame, Q-Bundle, EvaluationCharacteristicSpaceSpec, QualityImprovementLoopRecord |
| **COSTLY-ACTION** | Действие дорогое, опасное или необратимое. Что тормозит ответственное решение? | evidence-provenance graph, Assurance(H,C\|K,S), CV result, OperationalGate, CausalUseTriageRecord, ChoiceResult, WorkEntryReadiness |
| **TIME** | Утверждение про сроки, ритм, текущность или окно валидности используется для действия. Насколько оно обосновано? | `Dyn2TemporalClaimAdequacyCard` (C.27) или `RefreshCurrentnessLine@Context` (G.11) |
| **CAUSAL-USE** | Используется причинно-следственный язык для решения. Какой рунг поддержки? | `CausalUseTriageRecord` (C.28) |
| **DESCRIPTION-USE** | Создаём или используем описание, модель, отчёт, дашборд. Не теряем ли его предмет? | DescriptionContext, RepresentationSchemeTransitionRelation, StructuralInformationAdequacyNote, ComparativeReviewUnit, ArchitectureDescriptionUseCard |
| **NAMING** | Нужно стабильное название для управляемой величины в рамках контекста. | `NameCard` (F.18) |
| **WORDING** | Предложение звучит гладко, но скрывает, что именно оно делает. Как исправить без смены вида? | `KindRestorationCheck` (E.10) |
| **MATHEMATICAL-MODELING** | Может ли математический объект изменить следующее действие? | `MathLensUse.LensCandidateNote` или `MathLensUse.OneLine` (C.29) |
| **SOTA-PORTFOLIO** | Нужно текущее поле методов, теорий или технологий, а не один любимый источник. | `SoTA Synthesis Pack@CG-Frame` (G.2) |
| **DPF-AUTHORING** | Нужен локальный FPF-совместимый фреймворк, а не отдельные советы. | FrameworkOrganizationDesignProposal, PrincipleFrameworkArchitectureDecision, ArchitectureDescriptionUseCard, FrameworkAuthoringDependencyDescription |
| **SYSTEM-IN-CONTEXT** | Есть система, но текущий системный вопрос ещё не явен. | HolonDelimitationRelation, SystemAggregationRelation, SystemParticipationRelation, ArchitectureQuestionCard, U.WorkPlan, U.Work |

> **Ключевой принцип:** карточки — не шаги. Если несколько подходят, сравнивают их ситуации, первые результаты и границы, а затем выбирают прямой паттерн.

---

## 3. Как работает карточка: механика

Каждая публичная карточка устроена по одному шаблону:

```
Ситуация и вопрос → необязательное препятствие → шаблон(ы) → границы → публичное упрощение
```

### 3.1. Ситуация и вопрос

Карточка начинается с описания ситуации и вопроса, который стоит за ней. Например, карточка ARCHITECTURE:

> «Architecture-relevant problem pressure and competing characteristics are present, but the project needs to carry them toward candidate, selected, expected, or actual structures. Ask: which architecturing flow or description-use result is needed first?»

### 3.2. Опциональное препятствие

Некоторые карточки указывают, что мешает двигаться. Например, для ARCHITECTURE:

> «Candidate structures, architecture characteristics, or the relation between problem pressure and structure are not yet reviewable.»

### 3.3. Шаблон

Шаблон — это указание вида: `Паттерн → Тип результата`. Например:

> **Template A.** `C.32.P2S Solution -> ProblemToStructureArchitecturingFlowCard@Project`.

Это означает: примени решение паттерна `C.32.P2S`, получи `ProblemToStructureArchitecturingFlowCard@Project`.

### 3.4. Границы (Boundaries)

Границы говорят, когда остановиться или вернуться. Например, для ARCHITECTURE:

> «Stop when the selected first card makes the receiving architecture work reviewable. Return when problem pressure, EntityOfConcern, characteristics, description edition, or actual-structure feedback changes.»

### 3.5. Публичное упрощение (Public coarsening)

Это защитный механизм. Если кто-то говорит «архитектурная карточка» в разговоре, FPF требует восстановить точный смысл: либо `ProblemToStructureArchitecturingFlowCard@Project`, либо `ArchitectureDescriptionUseCard@Project`. Слова вроде «архитектурная работа» не заменяют точный результат.

---

## 4. Внутренние карточки-результаты

Публичные карточки ведут к прямым паттернам. Прямые паттерны порождают структурированные результаты. Вот основные внутренние карточки, которые стоит знать на практике:

### 4.1. `ProblemCard@Context` (C.22.2)

**Зачем:** превратить раннее давление или сигнал в честную проблемную запись, не подсовывая выбранное решение.

**Когда:** затронутый объект (EntityOfConcern), ограничения, неразрешённые отношения, различия, которые надо сохранить, и базис принятия можно сформулировать без решения.

**Структура (минимум):**

- `EntityOfConcern` — объект, с которым проблема;
- `constraints` — ограничения;
- `unresolvedRelations` — неразрешённые отношения;
- `distinctionsToPreserve` — различия, которые нельзя стирать;
- `acceptanceBasis` — на каком основании проблема будет считаться решённой.

**Граница:** остановиться на самом раннем результате, который и правдив, и полезен. Не превращать любой сигнал в `ProblemCard` только чтобы работа выглядела начатой.

### 4.2. `NameCard` (F.18)

**Зачем:** дать управляемой величине стабильное название в рамках bounded context, не меняя её вид.

**Когда:** нужно, чтобы разные читатели восстанавливали одну и ту же величину по названию.

**Структура:**

- управляемая величина (governed value);
- управляющий паттерн (governing pattern);
- bounded context;
- кандидат-названия и отвергнутые;
- обоснование;
- мосты (bridges) к другим контекстам;
- линия происхождения и условие обновления.

### 4.3. `ProblemToStructureArchitecturingFlowCard@Project` (C.32.P2S)

**Зачем:** вести архитектурную работу от давления проблемы к кандидатным, выбранным, ожидаемым и фактическим структурам.

**Когда:** есть архитектурное давление проблемы и конкурирующие характеристики, но нет готовой структуры.

**Пример структуры:** см. `PACK-cattle-science/docs/fpf/CS.METHOD.007-p2s-architecture-flow-card.md`. Там записаны `problemPressure`, `candidateStructureKindRefs`, `selectedStructureRefs`, `expectedStructureRefs`, `actualStructureRefs`, `architectureCharacteristicRefs`, `decisionAndWorkDocking` и другие поля.

### 4.4. `ArchitectureDescriptionUseCard@Project` (C.30.AD)

**Зачем:** использовать готовое описание архитектуры или view, не путая его с самой архитектурой.

**Когда:** объектом использования является именно описание или view, и важна его допустимая граница использования.

### 4.5. Другие карточки

| Карточка-результат | Паттерн | Назначение |
|--------------------|---------|------------|
| `CausalUseTriageRecord` | C.28 | Ограничить причинно-следственные утверждения перед действием |
| `MathLensUse.*` | C.29 | Зафиксировать математический объект, который может изменить следующий ход |
| `Dyn2TemporalClaimAdequacyCard` | C.27 | Проверить, поддерживает ли временное утверждение использование |
| `RefreshCurrentnessLine@Context` | G.11 | Зафиксировать линию текущности и источники |
| `FrameworkOrganizationDesignProposal@Context` | E.4.DPF | Предложение об организации локального фреймворка |
| `PrincipleFrameworkArchitectureDecision@Context` | E.4.PFAD | Архитектурное решение локального фреймворка |
| `ComparativeReviewUnit` | E.17.ID.CR | Ограниченное сравнение уже доступных эпистем |

---

## 5. Пример прохождения по карточке

### Ситуация

Технолог на ферме говорит: «У нас проблема: корова даёт мало молока. Нужно что-то сделать с рационом.»

### Шаг 1. Выбор публичной карточки

Вопрос ещё расплывчатый. Это может быть PROBLEM-SHAPING или ARCHITECTURE. Пока нет готовой структуры и непонятно, какие кандидатные решения сравнивать, — это **PROBLEM-SHAPING**.

### Шаг 2. Шаблон PROBLEM-SHAPING

Карточка предлагает четыре шаблона:

- A. `A.16.1 Solution -> U.PreArticulationCuePack` — слишком рано, сигнал ещё не стабилен;
- B. `B.4.1 Solution -> RoutedCueSet` — возможно, если есть несколько маршрутов расследования;
- C. `B.5.2.0 Solution -> U.AbductivePrompt` — если можно сформулировать открытый вопрос;
- D. `C.22.2 Solution -> ProblemCard@Context` — если объект, ограничения, различия и базис принятия уже можно сформулировать.

В данном случае технолог уже называет объект (корова/рацион) и ограничения (молочная продуктивность). Подходит **Template D** — `ProblemCard@Context`.

### Шаг 3. Применяем C.22.2

Формируем `ProblemCard@Context`:

- **EntityOfConcern:** конкретная корова или группа коров в текущем периоде лактации;
- **Constraints:** молочная продуктивность ниже ожидаемой, рацион уже составлен, но неясно, какой параметр нарушен;
- **Unresolved relations:** связь между фактическим потреблением, составом рациона, КПД переваривания и продуктивностью;
- **Distinctions to preserve:** различие между проблемой кормления, проблемой здоровья и проблемой учёта;
- **Acceptance basis:** проблема будет считаться сформулированной, когда можно будет назвать один конкретный параметр рациона, который подлежит проверке.

### Шаг 4. Граница

Останавливаемся на `ProblemCard@Context`. Не переходим сразу к выбору метода или работе. Следующий шаг — `C.22 TaskSignature` или прямой паттерн, который решает эту проблему (например, CS.METHOD.007 для технолога по кормлению).

---

## 6. Когда использовать карточки, а когда нет

### Использовать FPF-карточки, когда:

- работа пересекает границы команды, инструмента или времени;
- решение дорогое, необратимое или требует ответственности;
- разные читатели должны понимать одно и то же по-разному (инженер, менеджер, регулятор);
- имена, роли, критерии качества или варианты начинают путаться;
- нужно сохранить рассуждение для повторного использования или аудита.

### Не нужны FPF-карточки, когда:

- задача маленькая, обратная связь быстрая и дешевая;
- словарь уже стабилен;
- решение не будет повторно использоваться и не важно для аудита;
- достаточно быстрого ответа.

---

## 7. Связь с практическим курсом FPF (WP-109)

В практическом курсе 5 семинаров. Каждый семинар заканчивается capture — фиксацией того, как FPF-принцип изменил рабочий ход. Карточки помогают в этом:

- **Семинар 1:** FPF-мантра, README-card selection, problem-to-work carry-through.
- **Семинар 2:** работа с паттернами и карточками-результатами (ProblemCard, P2S Flow Card, NameCard).
- **Семинары 3–5:** углубление в архитектуру, evidence, description-use и DPF-authoring.

Capture за семинар 2 может быть, например, записью того, как одна публичная карточка (ARCHITECTURE или PROBLEM-SHAPING) привела к конкретной внутренней карточке-результату и изменила следующий рабочий ход.

---

## 8. Что запомнить

1. **FPF-карточки — это не чек-листы, а инструменты мышления.** Они помогают удержать смысл, когда обычного разговора недостаточно.
2. **15 публичных карточек — это входные точки.** Каждая начинается с ситуации и ведёт к прямому паттерну.
3. **Внутренние карточки — это результаты паттернов.** Например, `ProblemCard@Context`, `NameCard`, `ProblemToStructureArchitecturingFlowCard@Project`.
4. **Каждая карточка имеет границы.** Она говорит, где остановиться и когда вернуться, если условия изменились.
5. **Название карточки в разговоре не заменяет её точный результат.** «Архитектурная карточка» восстанавливается либо в `ProblemToStructureArchitecturingFlowCard@Project`, либо в `ArchitectureDescriptionUseCard@Project`.

---

## 9. Источники

- `FPF/Readme.md` — публичные 15 practical-use cards.
- `FPF/FPF-Spec.md` — паттерны `E.11`, `C.22.2`, `C.32.P2S`, `C.30.AD`, `F.18`, `C.28`, `C.29`, `C.27`, `G.11`, `E.4.DPF`.
- `PACK-cattle-science/docs/fpf/CS.METHOD.007-p2s-architecture-flow-card.md` — пример заполненного `ProblemToStructureArchitecturingFlowCard@Project`.
- `PACK-cattle-science/docs/fpf/fpf-capture-template.md` — шаблон capture для фиксации применения паттерна.

---

*Создано в рамках WP-109 (FPF-practical) 2026-07-16.*
*FPF Source: FPF/Readme.md, FPF/FPF-Spec.md §E.11, C.22.2, C.32.P2S, F.18, C.30.AD*
