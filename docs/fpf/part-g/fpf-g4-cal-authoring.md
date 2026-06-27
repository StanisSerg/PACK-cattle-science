---
type: fpf-study
pattern: G.4
title: "CAL Authoring: операторы, acceptance и пороги решений"
domain: cattle-science
difficulty: advanced
reading_time: 28 min
created: 2026-06-27
fpf_context: ["G.4", "G.3", "G.5", "G.Core", "G.0"]
---

# G.4 — CAL Authoring: операторы, acceptance и пороги решений

> **Цель capture:** объяснить, как в паттерне G.4 создаются операторы, acceptance clauses, flows, evidence profiles и proof ledger, и почему именно здесь живут пороги принятия решений.

---

## 1. Зачем это читать

В скотоводстве измерения превращаются в действия только через пороги и правила: при BHB ≥ 1,2 начать профилактику, при удое ниже нормы — пересмотреть рацион. CAL (Computation and Acceptance Logic) — это паттерн, в котором эти правила формализуются. В отличие от CHR, который описывает, что измеряется, CAL говорит, какие значения требуют каких действий, и на каких основаниях.

> **FPF-тезис:** *«Пороги — это acceptance clauses в CAL, а не определения характеристик в CHR.»*

**Фермерский пример:**

> Ветеринар замеряет BHB коровы. Значение 1,4 ммоль/л само по себе не говорит, что делать. CAL-правило гласит: «Если BHB ≥ 1,2, то применить оральный пропиленгликоль; если BHB ≥ 1,4, то вызвать ветеринара». Пороги 1,2 и 1,4 живут в CAL, а BHB — в CHR.

---

## 2. История одной ошибки

Хозяйство автоматизировало рекомендации по метаболическому риску. Пороги BHB были зашиты в коде расчёта «индекса риска» вместо того, чтобы быть вынесены в acceptance clauses. Когда ветеринар решил изменить порог, разработчикам пришлось искать по всей системе, где он используется. В одном месте порог остался старым, и две группы коров получили противоречивые рекомендации. CAL Pack централизует пороги и делает их видимыми.

---

## 3. CAL Authoring — полное описание

### 3.1 Определение

**CAL Authoring** — это паттерн создания CAL Pack@CG-Frame, который содержит Operators, Acceptance clauses, Flows, EvidenceProfiles, ProofLedger и опциональный NQD (non-quality-diversity) профиль. CAL Pack определяет, какие действия следуют из значений характеристик, и обеспечивает аудитоспособность этих решений.

### 3.2 Почему это важно

Без CAL пороги разбросаны по документам, коду и договорённостям. Это приводит к противоречивым решениям, невозможности аудита и скрытым изменениям. CAL собирает все acceptance clauses и flows в одном месте, связывает их с evidence и передаёт TaskMap в G.5 для dispatch.

### 3.3 Operators

**Определение.** Operators — это именованные вычислительные операторы, которые принимают характеристики из CHR и порождают новые значения или решения.

**Пояснение.** Operators должны быть scale-legal: каждый оператор ссылается на SCP из CG-Spec и не выполняет недопустимых операций. Они могут быть простыми (сравнение с порогом) или сложными (многокритериальная свёртка).

**Пример из животноводства.**

```text
OP-001: GreaterThanOrEqual
  - inputs: BHB (SC-001), threshold parameter
  - output: boolean
  - scaleLegalityRef: SCP-001

OP-002: ParetoDominance
  - inputs: {cost, efficacy, labor}
  - output: dominance relation
  - scaleLegalityRef: SCP-002
```

**Ключевой признак.** Каждый operator имеет идентификатор, входы, выход и ссылку на scale legality.

### 3.4 Acceptance clauses

**Определение.** Acceptance clauses — это условия вида «если X, то Y», где X — выражение над характеристиками, а Y — действие, статус или переход.

**Пояснение.** Acceptance clause — это единственное место, где живут пороги. Оно явно указывает: значение какой характеристики, при каком условии и с каким действием связано. Это позволяет изменять пороги, не трогая определения характеристик.

**Пример из животноводства.**

```text
AC-001: «IF BHB ≥ 1.2 mmol/L THEN trigger_propylene_glycol_protocol"
AC-002: «IF BHB ≥ 1.4 mmol/L AND BCS ≤ 2 THEN escalate_veterinarian"
AC-003: «IF MilkYield < 25 kg/day AND BHB ≥ 1.2 THEN flag_energy_deficit"
```

**Ключевой признак.** Acceptance clause содержит явный threshold, characteristic refs, action и policy id.

### 3.5 Flows

**Определение.** Flows — это композиции acceptance clauses и operators, которые описывают последовательность принятия решения.

**Пояснение.** Flow соединяет несколько clauses в единый процесс: сначала скрининг, затем подтверждение, затем действие. Flow фиксирует, какие ветви возможны и какие guard-решения применяются.

**Пример из животноводства.**

```text
FL-001: KetosisRiskFlow
  - step 1: AC-001 (screening)
  - step 2: IF AC-001 pass → AC-002 (escalation check)
  - step 3: IF AC-002 abstain → monitor
  - guard outcomes: pass / degrade / abstain
```

**Ключевой признак.** Flow содержит упорядоченные шаги, ссылки на acceptance clauses и трихотомию guard-решений.

### 3.6 EvidenceProfiles

**Определение.** EvidenceProfiles — это профили, указывающие, какие evidence требуются для каждого acceptance clause или operator.

**Пояснение.** EvidenceProfile не заменяет EvidenceGraph, а декларирует, какие типы evidence нужны. Это позволяет проверить, достаточно ли evidence для применения CAL-правила.

**Пример из животноводства.**

```text
EP-001: EvidenceProfile for AC-001
  - required: BHB observation (PathSliceId), SOP ref, freshness window ≤ 7 days
  - optional: BCS observation
```

**Ключевой признак.** EvidenceProfile содержит список required/optional evidence и их freshness requirements.

### 3.7 ProofLedger

**Определение.** ProofLedger — это аудиторская книга, фиксирующая, какие acceptance clauses были применены, к каким характеристикам, на каком основании и с каким результатом.

**Пояснение.** ProofLedger делает каждое CAL-решение проверяемым. Он связывает acceptance clause, evidence path, operator run и guard outcome.

**Пример из животноводства.**

```text
PL-001:
  - acceptanceClause: AC-001
  - subject: cow #1847
  - observation: BHB 1.4 mmol/L (PathSliceId PS-001)
  - operator: OP-001
  - outcome: pass → trigger propylene glycol protocol
  - evidenceProfile: EP-001
```

**Ключевой признак.** ProofLedger содержит clause id, subject, observation refs, operator id и outcome.

### 3.8 NQD profile

**Определение.** NQD (non-quality-diversity) profile — это опциональный профиль, который указывает, что CAL-операторы не используют QD-семантику (archive, illumination), и сохраняют обычный acceptance flow.

**Пояснение.** NQD нужен, когда в CG-Frame присутствуют QD-паттерны, но конкретный CAL Pack к ним не относится. Это предотвращает неявное смешение QD и non-QD логики.

**Пример из животноводства.** CAL Pack для линейного протокола лечения кетоза помечается NQD, чтобы отличить его от QD-архива методов профилактики.

**Ключевой признак.** NQD profile присутствует, когда CAL не использует QD/illumination semantics.

### 3.9 TaskMap handoff to G.5

**Определение.** TaskMap — это карта, которая передаёт CAL-задачи в Method Dispatcher (G.5), указывая, какие TaskSignature, MethodFamily и acceptance gates должны быть применены.

**Пояснение.** CAL не выбирает методы; он формулирует задачи и критерии. G.5 выполняет dispatch, сохраняя set-return semantics.

**Пример из животноводства.**

```text
TM-001: TaskMap
  - taskSignature: metabolic_support_protocol
  - methodFamilies: {propylene_glycol, ration_adjustment, iv_glucose}
  - acceptanceGates: {AC-001, AC-002}
  - handoff to G.5
```

**Ключевой признак.** TaskMap содержит TaskSignatureRef, MethodFamilyId[] и AcceptanceClauseId[], и передаёт управление G.5.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Если корова худощавая и BHB высокий, нужно срочно лечить.»*

**Разложение по G.4:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «худощавая» | BCS level (CHR) | Требует scale-legal оператора |
| «BHB высокий» | BHB value + acceptance threshold (CAL) | Порог должен быть явным |
| «срочно лечить» | action (CAL acceptance clause) | Требует policy id и escalation flow |

**Основные риски смешивания:**

1. **Неявные пороги.** «Высокий BHB» без числа приводит к разным интерпретациям.
2. **Смешение шкал.** BCS и BHB требуют scale-legal оператора и явного coordinate.
3. **Отсутствие аудита.** Решение не фиксируется в ProofLedger.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** автоматизация рекомендаций при субклиническом кетозе.

**Было (смешанное / нечёткое):**
> «Если BHB высокий и корова худощавая — лечим.»

**Стало (разложенное / ясное):**

**CHR (G.3):**
> CH-001: BHB (ratio, ммоль/л); CH-002: BCS (ordinal, 1–5).

**CAL Operators:**
> OP-001: BHB ≥ threshold; OP-002: BCS ≤ threshold.

**Acceptance clauses:**
> AC-001: IF BHB ≥ 1.2 THEN start propylene glycol protocol.
> AC-002: IF BHB ≥ 1.4 AND BCS ≤ 2 THEN escalate to veterinarian.

**Flow:**
> FL-001: screening → AC-001 → if pass then AC-002 → outcome pass/degrade/abstain.

**ProofLedger:**
> PL-001: cow #1847, BHB 1.4, BCS 2, AC-002 triggered, outcome escalate.

**Результат:**
- Пороги централизованы и легко изменяются.
- Каждое решение фиксируется с evidence.
- G.5 получает TaskMap для выбора конкретного метода.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Соберите характеристики из CHR Pack.

**Шаг 2.** Определите operators, проверив их scale legality по SCP.

**Шаг 3.** Авторизуйте acceptance clauses с явными thresholds и actions.

**Шаг 4.** Постройте flows, соединяющие clauses в guard-aware последовательности.

**Шаг 5.** Создайте EvidenceProfiles и ProofLedger, затем сформируйте TaskMap для G.5.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Пороги находятся в CHR или в коде? | Их место — в CAL acceptance clauses. |
| Acceptance clause не имеет policy id? | Решение нельзя аудитировать и обновлять. |
| Operator смешивает ординальные и количественные шкалы? | Нарушение SCP и scale legality. |
| ProofLedger не фиксирует outcome? | Решение не проверяемо. |
| TaskMap передаёт не в G.5, а напрямую выбирает метод? | Нарушено разделение CAL и dispatch. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| G.3 CHR Authoring | предоставляет характеристики и шкалы |
| G.5 Method Dispatcher | получает TaskMap и возвращает selected set |
| G.0 CG-Spec | задаёт SCP и ComparatorSet для scale legality |
| G.6 Evidence Graph | предоставляет evidence paths для ProofLedger |
| G.Core | обеспечивает tri-state guard и set-return semantics |

---

## 9. Что запомнить

1. CAL — это место для acceptance clauses, operators и flows.
2. Пороги живут в CAL, а не в CHR.
3. Каждый operator должен быть scale-legal.
4. ProofLedger фиксирует каждое CAL-решение с evidence.
5. TaskMap передаёт задачи в G.5, не выбирая методы самостоятельно.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.4*
