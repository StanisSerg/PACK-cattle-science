# P2S Flow Card для CS.METHOD.007

**README card:** `ARCHITECTURE — Shape architecture from problem pressure`  
**Прямой паттерн:** `C.32.P2S — Problem-to-Structure Architecturing Unfolding`  
**Результат:** `ProblemToStructureArchitecturingFlowCard@Project`

---

## Зачем это нужно на языке фермы

CS.METHOD.007 — это не просто инструкция, а **скелет рабочего процесса**: технолог видит проблему → собирает факты → находит нужный паттерн → проверяет гипотезу → фиксирует результат. Сейчас этот процесс описан в одном файле. Архитектурный вопрос: как организовать «мясо» вокруг скелета, чтобы система не превратилась в бесконечный текст, а осталась удобной, расширяемой и связанной с FPF?

Этот документ — первая архитектурная запись, которая фиксирует давление проблемы и возможные структуры, не пытаясь сразу нарисовать окончательную схему.

---

## ProblemToStructureArchitecturingFlowCard@Project

```yaml
flowId: CS.METHOD.007-P2S-001
describedHolonRef: CS.METHOD.007-feeding-technologist-problem-solving-system
boundedContextRef: Cattle Science / кормление КРС / диагностика и решение рационных проблем
architectingHolonOrRoleRef: Автор метода в роли технолога по кормлению
firstGoverningPatternRef: C.32.P2S
problemPressure:
  pressureKind: structural-uncertainty
  problemPressureSignalRefs:
    - CS.METHOD.007 содержит алгоритм, но не содержит структуры для хранения типовых проблем
    - capture-уроки не имеют постоянного места, теряются между сессиями
    - связь между практической проблемой и паттерном CS.DPF.001 не формализована
    - непонятно, где заканчивается метод и начинается библиотека проблем
  sourceUseRecordRefs:
    - /PACK-cattle-science/pack/cattle-science/03-methods/CS.METHOD.007-feeding-technologist-problem-solving-system.md
    - /PACK-cattle-science/pack/cattle-science/08-dpf/CS.DPF.001-cncps-feeding-model-principles-framework.md
  architectureConcernRefs:
    - usability: технолог должен быстро найти похожую проблему
    - extensibility: новые типовые проблемы добавляются без переписывания метода
    - traceability: каждое решение должно ссылаться на паттерн
    - maintainability: capture не должны растворяться в общих папках
  currentStopOrReturnReason: нужно определить структурную схему, прежде чем создавать десятки Problem Card
architectureContent:
  candidateStructureKindRefs:
    - problem-card-directory
    - capture-registry
    - method-step-template
    - pattern-index-bridge
    - decision-log-per-problem
  selectedStructureRefs: []
  expectedStructureRefs:
    - problem-card: один файл = одна типовая проблема
    - capture-entry: короткая запись внутри Problem Card или отдельный capture-log
    - pattern-bridge: ссылка из Problem Card на паттерн CS.DPF.001
  actualStructureRefs:
    - CS.METHOD.007 как единый файл-носитель всего метода
  architectureCharacteristicRefs:
    - usability
    - extensibility
    - traceability
    - maintainability
  architectureCharacteristicCriteriaSetRef: CS.METHOD.007-ACS-001 (требует создания)
  qBundleRefs: []
  candidateSynthesisRef: CS.METHOD.007-CANDIDATE-001 (требует создания)
structuralInformation:
  unknownStructure:
    - Как связать Problem Card с методом: встроить в CS.METHOD.007 или вынести в отдельный каталог?
    - Где хранить capture: внутри Problem Card, в общем capture-log или в обоих местах?
    - Нужен ли отдельный шаблон Problem Card или достаточно свободного markdown?
  selectedStructure: {}
  expectedStructure:
    - Корневой метод (CS.METHOD.007) остаётся статичным.
    - Проблемы живут в отдельных карточках в подкаталоге.
    - Capture фиксируется в Problem Card и агрегируется в коротком регистре.
  actualStructure:
    - CS.METHOD.007 содержит текстовое описание алгоритма и пример.
  capturedInDescriptionsOrDecisions:
    - CS.METHOD.007 как описание метода
  handedToMethodsOrWork: []
  latentOrHiddenStructure:
    - Возможность автоматической сборки индекса Problem Card
    - Возможность связи с CS.DPF.001 через машиночитаемые ссылки
  lostStructure:
    - Пока не фиксируется, какие проблемы уже решены и какой у них статус
  strongerStructureInspectionReturnCondition: если выбранная структура не позволит добавить новую проблему за 10 минут — вернуться к C.32.P2S
decisionAndWorkDocking:
  candidateSetOrPaletteRef: CS.METHOD.007-CANDIDATE-001
  selectedSetRef: []
  architectureDecisionRef: []
  adrProjectionRef: []
  methodDescriptionRefs:
    - CS.METHOD.007
  workPlanRefs: []
  readinessRefs: []
  performedWorkRefs: []
transformerTransformed:
  changingRelationRef: метод → библиотека проблем
  transformerHolonRef: автор метода / технолог
  transformedHolonRef: CS.METHOD.007 как статичный документ → CS.METHOD.007 как система с расширяемой библиотекой проблем
  transformerSelectedStructureRefs:
    - организация каталога
    - шаблон Problem Card
    - capture-регистр
  transformedSelectedStructureRefs:
    - расширяемая библиотека типовых проблем
    - связанный с DPF справочник
  correspondenceFrameRef: pattern-bridge между Problem Card и CS.DPF.001
feedback:
  evalProgramRefs: []
  evalResultRefs: []
  measurementRefs: []
  operationOrUseObservationRefs:
    - Время, которое технолог тратит на поиск похожей проблемы
    - Количество capture, добавленных за месяц
    - Количество повторных вопросов по одной и той же проблеме
  functionalCharacteristicImplications:
    - usability: поиск проблемы ≤ 2 минуты
    - extensibility: новая проблема добавляется без изменения CS.METHOD.007
    - traceability: каждая Problem Card ссылается на 1–3 паттерна
  freshnessOrDecaySignalRefs:
    - Устаревание Problem Card при изменении CS.DPF.001
  governingPatternSpecificReturnOrRepair:
    c32NextSynthesisExit: true
    c32PadOrAdaDecisionRepairOrSupersessionExit: true
governingPatternForNextClaim: C.32.PAD — Project Architecture Decision After Candidate Synthesis
```

---

## Первый полезный результат

Эта карточка делает архитектурную работу обозримой. Она не решает всё сразу, но превращает размытое «надо бы систематизировать проблемы» в конкретный набор вопросов:

1. Где жить Problem Card — внутри метода или отдельно?
2. Как фиксировать capture — в карточке проблемы или в общем журнале?
3. Как связать каждую проблему с паттерном CS.DPF.001?
4. Какие характеристики качества важны: usability, extensibility, traceability, maintainability?

## Конкретный следующий ход проекта

**Сделать архитектурное решение (C.32.PAD) по структурной схеме CS.METHOD.007.**

После этого решения можно будет:
- Создать каталог `pack/cattle-science/03-methods/CS.METHOD.007-problems/`.
- Утвердить шаблон `Problem Card`.
- Перенести пример с pH мочи из CS.METHOD.007 в первую Problem Card.
- Добавить короткий capture-регистр.

Без этой P2S-карточки следующий шаг был бы рискован: можно было бы начать создавать файлы вразнобой и получить библиотеку, которую никто не сможет поддерживать.

---

## Использованные FPF-паттерны

- **ARCHITECTURE (README card)** — выбор паттерна для архитектурной работы.
- **C.32.P2S** — создание `ProblemToStructureArchitecturingFlowCard@Project`.
- **C.22.2** — problem-side record (Problem Card как часть метода).
- **A.1.1** — bounded context для кормления КРС.
- **A.15** — role-method-work alignment.
- **C.32.PAD** — следующий паттерн для фиксации архитектурного решения.
