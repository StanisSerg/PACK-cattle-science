---
type: fpf-study
pattern: G.6
title: "Evidence Graph: декларативная родословная знания"
domain: cattle-science
difficulty: advanced
reading_time: 28 min
created: 2026-06-27
fpf_context: ["G.6", "A.10", "G.Core", "G.11", "G.7"]
---

# G.6 — Evidence Graph: декларативная родословная знания

> **Цель capture:** объяснить, как паттерн G.6 строит декларативный граф происхождения знания, адресуемый через PathId и PathSliceId, и как он связывает evidence с downstream решениями.

---

## 1. Зачем это читать

В скотоводстве решения часто принимаются на основе цепочки утверждений: «корова в группе риска, потому что BHB высокий; BHB высокий, потому что лаборатория так измерила; лаборатория использовала протокол №7». Если эта цепочка не зафиксирована как граф с идентификаторами, проверить, обновить или перенести решение невозможно. Evidence Graph делает родословную знания декларативной и адресуемой.

> **FPF-тезис:** *«Claim без PathId — это утверждение без адреса; Evidence Graph даёт каждому claim проверяемый путь.»*

**Фермерский пример:**

> Фермер решает, вводить ли профилактику кетоза группе коров. Решение основано на отчёте, который ссылается на BHB-измерения, те — на лабораторный протокол, а протокол — на исследование. Evidence Graph позволяет проследить каждое звено по PathId и увидеть, какие части цепочки можно безопасно обновить, если изменится протокол.

---

## 2. История одной ошибки

В хозяйстве приняли решение о массовой профилактике кетоза на основе отчёта «риск высокий». Через год аудитор запросил доказательную базу. Оказалось, что отчёт ссылался на таблицу, таблица — на выгрузку из программы мониторинга, а выгрузка — на показания датчиков, калибровка которых была изменена без фиксации. Ни одно звено не имело стабильного идентификатора, и цепочка оказалась разорванной. Evidence Graph мог бы сохранить PathId для каждого шага.

---

## 3. Evidence Graph — полное описание

### 3.1 Определение

**Evidence Graph** — это декларативный ориентированный граф, который связывает observation, method, transformer, carrier и claim через отношения происхождения. Граф адресуется через PathId и PathSliceId и сопровождается ProvenanceLedger.

### 3.2 Почему это важно

Доказательная база в животноводстве быстро устаревает: меняются протоколы, появляются новые исследования, корректируются пороги. Если цепочка evidence не зафиксирована как граф, обновление одного звена требует ручного пересмотра всех зависимых решений. Evidence Graph позволяет находить затронутые PathSliceId и планировать выборочный refresh.

### 3.3 EvidenceGraph object

**Определение.** EvidenceGraph — это объект, содержащий множество узлов и рёбер, которые фиксируют происхождение и преобразование знания.

**Пояснение.** Узлы графа соответствуют категориям A.10: SymbolCarrier, TransformerRole, MethodDescription, Observation, s.Episteme. Рёбра выражают отношения происхождения. EvidenceGraph — декларативный: он описывает, что произошло, а не задаёт workflow.

**Пример из животноводства.**

```text
EvidenceGraph EG-001:
  - node N1: SymbolCarrier «farmA_BHB_2026-06-19.csv»
  - node N2: MethodDescription «SOP_BHB_v3»
  - node N3: TransformerRole «Lab_X#analyst»
  - node N4: Observation «BHB cow #1847 = 1.4 mmol/L»
  - node N5: s.Episteme «cow #1847 at risk of ketosis»
  - edge E1: N4 measuredBy N2
  - edge E2: N4 usedCarrier N1
  - edge E3: N4 interpretedBy N3
  - edge E4: N5 evidences N4
```

**Ключевой признак.** EvidenceGraph содержит узлы и рёбра с идентификаторами и не является workflow engine.

### 3.4 PathId и PathSliceId

**Определение.** PathId — это идентификатор пути в EvidenceGraph от источника к claim. PathSliceId — это идентификатор подмножества пути, которое имеет общий scope (например, одно измерение, одна корова, одно временное окно).

**Пояснение.** PathId позволяет ссылаться на всю цепочку evidence, а PathSliceId — на конкретный фрагмент, который интересует downstream потребителя. PathSliceId используется в RSCR-триггерах для выборочного refresh.

**Пример из животноводства.**

```text
PathId P-001: N1 → N4 → N5 (полная цепочка для cow #1847)
PathSliceId PS-001: N4 → N5 (только observation и claim)
PathSliceId PS-002: N1 → N4 (только carrier и observation)
```

**Ключевой признак.** Каждый claim или decision ссылается на PathId или PathSliceId.

### 3.5 PathCitationRecord

**Определение.** PathCitationRecord — это запись, фиксирующая, какой PathId/PathSliceId использован для поддержки конкретного claim или decision.

**Пояснение.** PathCitationRecord связывает downstream артефакты (acceptance clauses, parity reports, dashboard rows) с evidence. Без такой записи claim висит в воздухе.

**Пример из животноводства.**

```text
PCR-001:
  - citingClaim: AC-001 (BHB ≥ 1.2 → propylene glycol)
  - pathSliceId: PS-001
  - evidenceSupportClass: VA (verified observation)
```

**Ключевой признак.** PathCitationRecord содержит citing artefact id, pathSliceId и evidence support class.

### 3.6 ProvenanceLedger

**Определение.** ProvenanceLedger — это книга изменений evidence graph: какие узлы и рёбра добавлены, изменены или устарели, с указанием причин.

**Пояснение.** ProvenanceLedger не дублирует EvidenceGraph, а фиксирует его эволюцию. Он используется для refresh planning и для доказательства, что изменения были явными.

**Пример из животноводства.**

```text
PL-001:
  - action: add node N6 (new SOP_BHB_v4)
  - reason: RSCRTriggerKindId.EditionPinChange
  - affectedPathSliceIds: [PS-002]
```

**Ключевой признак.** ProvenanceLedger содержит action, reason, affected paths и timestamp.

### 3.7 NotCarried field

**Определение.** NotCarried — это поле, которое явно указывает, какие части evidence не переносятся в downstream использование, что делает downstream claim более слабым, но честным.

**Пояснение.** Иногда evidence переносится из одного контекста в другой с потерями. NotCarried фиксирует, что именно потеряно, чтобы downstream потребитель не переоценил силу claim.

**Пример из животноводства.** Observation BHB измерено лабораторно на Holstein. При переносе на Jersey порода меняется; NotCarried указывает, что точная интерпретация породы не сохранена, и claim требует дополнительного evidence.

**Ключевой признак.** NotCarried содержит перечень потерянных элементов evidence или scope.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Риск кетоза подтверждён данными.»*

**Разложение по G.6:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «риск кетоза» | s.Episteme / claim | Требует PathId |
| «подтверждён» | evidences relation | Должен быть явный observation и method |
| «данными» | SymbolCarrier / Observation | Нужен PathSliceId и carrier id |

**Основные риски смешивания:**

1. **Claim без адреса.** Невозможно проверить, какие именно observation поддерживают утверждение.
2. **Потерянные потери.** Перенос evidence в другой контекст без NotCarried завышает силу claim.
3. **Невозможный refresh.** Без PathSliceId обновление требует полного пересмотра.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** фиксация evidence для решения о профилактике кетоза.

**Было (смешанное / нечёткое):**
> «Данные показывают риск, начинаем профилактику.»

**Стало (разложенное / ясное):**

**EvidenceGraph EG-001:**
> N1: carrier `farmA_BHB_2026-06-19.csv`
> N2: method `SOP_BHB_v3`
> N3: transformer `Lab_X#analyst`
> N4: observation `BHB cow #1847 = 1.4 mmol/L`
> N5: claim `cow #1847 at risk`

**PathId:**
> P-001: N1 → N2 → N3 → N4 → N5.

**PathCitationRecord:**
> PCR-001: AC-001 cites PS-001 (N4→N5), evidence class VA.

**ProvenanceLedger:**
> PL-001: SOP_BHB_v3 → v4, reason EditionPinChange, affected PS-002.

**Результат:**
- Каждое решение связано с конкретным путём.
- Обновление метода затрагивает только указанные slices.
- Аудитор может проверить всю цепочку за минуты.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Для каждого значимого claim постройте EvidenceGraph с узлами A.10.

**Шаг 2.** Назначьте PathId полным цепочкам и PathSliceId ключевым фрагментам.

**Шаг 3.** Создайте PathCitationRecord, связывающие claim/decision с PathSliceId.

**Шаг 4.** Ведите ProvenanceLedger для всех изменений графа.

**Шаг 5.** При переносе evidence указывайте NotCarried для потерянных элементов.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Claim не ссылается на PathId/PathSliceId? | Claim не имеет проверяемой родословной. |
| EvidenceGraph используется как workflow engine? | Нарушена декларативность; риск смешения с процессом. |
| Изменения evidence не фиксируются в ProvenanceLedger? | Невозможно планировать refresh. |
| Перенос evidence в другой контекст без NotCarried? | Downstream claim может быть переоценён. |
| PathCitationRecord не указывает evidence support class? | Неясна сила evidence. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.10 Evidence-Provenance DAG | задаёт базовые узлы и рёбра графа |
| G.4 CAL Authoring | использует PathSliceId в ProofLedger |
| G.7 Bridge Calibration | ссылается на PathId/PathSliceId для bridge evidence |
| G.11 Telemetry Refresh | использует PathSliceId для scope planning |
| G.Core | обеспечивает Δ-discipline и typed RSCR triggers |

---

## 9. Что запомнить

1. Evidence Graph — декларативный граф происхождения знания.
2. PathId и PathSliceId делают evidence адресуемым для downstream артефактов.
3. PathCitationRecord связывает claim с evidence path.
4. ProvenanceLedger фиксирует изменения графа.
5. NotCarried делает downstream claim честным относительно потерь.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.6*
