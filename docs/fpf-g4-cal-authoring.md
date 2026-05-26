---
type: fpf-study
pattern: G.4
title: "CAL Authoring: законные операции, приёмка и свидетельства"
domain: cattle-science
difficulty: hard
reading_time: 20 min
created: 2026-05-26
---

# G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring

## 1. Зачем это читать

Если вы когда-нибудь спрашивали: **«А можно ли усреднить BHB за неделю? А можно ли сравнить BHB с BCS? А что делать, если лаборатория не прислала результаты?»** — вы стоите на границе между CHR (типизированными измерениями) и CAL (законными операциями над ними).

G.4 — это не «настройка формул в Excel». Это **аудируемая публикация операторов**, которые знают, какие CHR-типы они принимают, какие гарды проверяют, что считают приёмлемым, и к каким свидетельствам привязаны. Если CHR говорит «BHB — ratio, ммоль/л, полярность ↓», то CAL говорит: «Оператор WeeklyMean_BHB lawful при едином ReferencePlane и N ≥ 5. Оператор Compare_BHB_BCS — незаконен. Классификатор Acceptable_BHB — порог 1.2 ммоль/л, свежесть данных 48 часов, при пропуске — abstain».

В мире ферм CAL — это **различие между протоколом и его имплементацией**, между «измерили» и «решили», между «похоже на правду» и «доказуемо приемлемо».

---

## 2. История одной ошибки

Ферма «Молочный берег» внедрила автоматическую систему раннего оповещения. Датчики молока измеряли BHB на каждой дойке. Система считала **среднее BHB за 3 дня** и, если оно превышало 1.0 ммоль/л, отправляла ветеринару алерт: «Корова в группе риска».

Проблема 1: среднее BHB — это `CAL.Operator: RollingMean`. Но BHB измерялся с разной частотой: в дойке 2 раза в день, но если доярка пропускала дойку — данных не было. Система считала среднее по **имеющимся точкам**, не учитывая пропуски. Получался смещённый RollingMean — оператор не декларировал своё поведение при Missingness.

Проблема 2: порог 1.0 ммоль/л был выбран «по умолчанию из статьи». Но статья исследовала Jersey на пастбище. Ферма держала Holstein в стойле. **Acceptance Clause** не декларировал `BoundedContext` порога и не связывал его с evidence profile.

Проблема 3: когда BHB в одной дойке был 2.5 ммоль/л, а в другой 0.3 (норма), система усредняла в 1.4 и алертил. Но ** Flow ** (композиция операторов) не содержал Acceptance Clause на внутреннюю вариативность. Оператор считал скаляр, где lawful был бы selected-set («возможно, есть выброс; нужен осмотр»).

Результат: ветеринар получал 15–20 ложных алертов в неделю. Через месяц он перестал на них реагировать. Через три месяца настоящий случай кетоза (BHB стабильно 2.1) был пропущен, потому что ветеринар не открыл письмо.

G.4 говорит: *«Операторы, приёмка и Flow должны быть опубликованы, типизированы и привязаны к свидетельствам — иначе это не система поддержки решений, это генератор шума»*.

---

## 3. Core concepts

### 3.1 CAL.Charter@Context — хартия операций

**CAL.Charter** — якорь scope для CAL Pack. Он цитирует `CG-FrameContext`, `describedEntity`, `ReferencePlane`, governance card (`CNSpecRef`, `CGSpecRef`) и **предположительный конверт** (assumption envelope), на который опираются acceptance predicates.

**На ферме:** `CAL.Charter@Farm_MB_MetabolicHealth_2026` декларирует:
- «Все операции в этом pack применимы к Holstein-Friesian, стойловое содержание, 0–21 день postpartum»
- «Пороги acceptance основаны на NASEM-2021 и Drackley 2018; при несоответствии контекста — abstain»
- «Evidence lanes: F (фермерские наблюдения), G (лабораторные данные), R (литература)»

### 3.2 CAL.Operator — типизированный, законный оператор

Каждый оператор — UTS-опубликованная единица с:
- `OperatorId (UTS)` — стабильный идентификатор
- `Signature` over CHR types — какие характеристики принимает
- `Preconditions` — ссылки на CHR guard macros
- `Postconditions / invariants` — что гарантируется на выходе
- `EvidenceProfileRef[]` — к каким свидетельствам привязан
- `FailureBehaviorRef` — что делать при деградации

**На ферме:**

```
CAL.Operator: WeeklyMean_BHB_Serum
- Signature: BHB_Serum_Postpartum[] → BHB_Serum_Postpartum (scalar)
- Preconditions: UNIT_CHECK, REFPLANE_UNIFORM, N_MIN_5
- Postconditions: RESULT_IS_RATIO, UNCERTAINTY_PROPAGATED
- EvidenceProfileRef: EP_Lab_VetLab_Ivanovo_2024
- FailureBehaviorRef: FB_DEGRADE_TO_MEDIAN_IF_OUTLIERS
```

Если входные данные содержат BHB из разных ReferencePlane — оператор **блокируется**.

### 3.3 CAL.Acceptance — типизированные предикаты приёмки

**Acceptance Clause** — UTS-опубликованный предикат с:
- `ClauseId (UTS)` — для цитирования
- `CharacteristicRefs` — какие CHR использует
- `PredicateRef` — логика приёмки (threshold, range, pattern)
- `Freshness envelope` — окно свежести + decay/Γ_time selector
- `UnknownHandling` — tri-state: accept / reject / abstain
- `FailureBehaviorRef` — что делать при неопределённости
- `GateCrossingId[]` — если клауза опирается на cross-context импорт

**На ферме:**

```
CAL.Acceptance: Acceptable_BHB_Serum
- CharacteristicRefs: BHB_Serum_Postpartum
- PredicateRef: BHB < 1.2 mmol/L
- Freshness envelope: 48 hours from sampling
- UnknownHandling: ABSTAIN (если данных нет — не accept, не reject — abstain)
- FailureBehaviorRef: FB_ALERT_VET_FOR_MANUAL_CHECK
```

Порог 1.2 ммоль/л — **не встроен в CHR**. Он живёт в CAL.Acceptance, потому что пороги — политика, а не измерение.

### 3.4 CAL.Flow — композиция с проверкой легальности

**CAL.Flow** компонует операторы в DAG (направленный ациклический граф) и декларирует:
- какие Acceptance clauses gate the flow,
- какие выходы decision-relevant, а какие report-only,
- **result kind** — scalar только где lawful; иначе selected-set / set-surface.

**На ферме:**

```
CAL.Flow: TransitionRiskAssessment
- DAG: RawBHB → WeeklyMean_BHB → Classify_BHB_Category
- Gate: Acceptable_BHB_Serum
- Result kind: SELECTED_SET (не scalar!)
  - {LOW_RISK, MEDIUM_RISK, HIGH_RISK, MANUAL_CHECK_REQUIRED}
```

Если BHB неоднозначен (на границе категорий) — Flow возвращает **множество**, не скаляр. Это предотвращает ложную уверенность.

### 3.5 CAL.EvidenceProfile — поверхность свидетельственной проводки

**EvidenceProfile** делает привязку к свидетельствам явной:
- `lane tags` (F/G/R) — для каждого вклада evidence
- `provenance anchor references` (A.10-style carriers)
- `freshnessPolicyPins` — окно свежести + decay selectors
- `penaltyPolicyPins` — куда маршрутизировать штрафы (только в R_eff, per G.Core)

**На ферме:**

```
CAL.EvidenceProfile: EP_Lab_VetLab_Ivanovo_2024
- Lane G: лабораторные данные BHB, NEFA
- Anchors: VetLab-Cert-2024, ProficiencyTest-Q2-2024
- Freshness: 48h from sampling, 2-year protocol validity
- Penalty routing: Φ(CL) → R_eff (если данные просрочены — штраф в effective risk, не в доминантный вывод)
```

### 3.6 CAL.ProofLedger — книга доказательств

**ProofLedger** связывает каждый оператор/flow/clause с:
- legality proof refs (включая CSLC refs для numeric comparison/aggregation),
- monotonicity/boundedness proofs для penalty/aggregation policies,
- явными условиями деградации (что происходит, когда предположения ломаются).

**На ферме:** `WeeklyMean_BHB` требует proof ref: «Mean lawful для ratio-scale при едином ReferencePlane». Если ReferencePlane различается — ProofLedger указывает на доказательство, что оператор **должен деградировать** в `ReturnSet` или `Abstain`.

---

## 4. Anti-patterns

| Анти-паттерн | Проявление на ферме | Почему опасно |
|---|---|---|
| **Implicit Cardinalization** (Неявная кардинализация) | «BHB-категория 1=низкий, 2=средний, 3=высокий; считаем среднее» | Ordinal → число → mean. Легальность нарушена. Результат — ложные алерты. |
| **Threshold Laundering** (Отмывание порогов) | «Порог 1.2 взят из статьи» — без указания контекста статьи | Acceptance не трассируется. Порог может быть неприменим к вашей породе/системе. |
| **Silent Lane Mixing** (Смешение дорожек) | «У нас есть данные лаборатории + наблюдения доярки + статья — всё в одну кучу» | F/G/R lanes смешаны. Penalties маршрутизируются неправильно. Доверие не учтено. |
| **Scalar Obsession** (Одержимость скаляром) | «Система выдаёт одно число — риск 73%» | Flow должен возвращать selected-set, если порядок частичный. Скаляр создаёт ложную уверенность. |
| **Tool-as-Semantics** (Инструмент как семантика) | «Excel считает AVERAGE — значит lawful» | Инструмент не знает о шкалах и ReferencePlane. Семантика определяется CAL, не Excel. |
| **Missingness-as-Zero** (Пропуск как ноль) | «Нет данных за день = 0» | Tri-state обработка нарушена. Abstain превращается в Reject. |

---

## 5. Пример на ферме: какие агрегаторы lawful для BHB? Можно ли усреднять ординалы?

**Контекст:** Ферма «Молочный берег», CG-Frame `Farm_MB_MetabolicHealth_2026`. CHR Pack уже опубликован (см. G.3). Теперь нужен CAL Pack для оперативных решений.

### C1 — CAL Charter

`CAL.Charter@Farm_MB_MetabolicHealth_2026`:
- Scope: Holstein-Friesian, стойловое, 0–21 день postpartum
- Cites: CHR Pack `CHR_Farm_MB_2026`, NASEM-2021, Drackley 2018
- Assumption envelope: «Все операции предполагают единый ReferencePlane (VetLab_Ivanovo_2024). При смене лаборатории — пересмотр CAL Pack.»
- TaskMap: связывает задачи с eligible Flows, gating clauses, evidence profiles

### C2 — Operator Cards

**Operator: DailyMean_BHB**
- Signature: BHB_Serum_Postpartum[2..N] → BHB_Serum_Postpartum
- Preconditions: `UNIT_CHECK`, `REFPLANE_UNIFORM`, `N_MIN_2`
- Postconditions: scalar, ratio preserved
- EvidenceProfile: EP_Lab_VetLab_Ivanovo_2024
- **Lawful: ДА** (ratio-scale, один ReferencePlane)

**Operator: WeeklyMean_BHB_CrossLab**
- Signature: BHB_Serum_Postpartum[] → BHB_Serum_Postpartum
- Preconditions: `UNIT_CHECK`, `REFPLANE_UNIFORM`
- **Lawful: НЕТ** — требуется GateCrossing, если ReferencePlane различаются. Блокируется.

**Operator: Average_BCS**
- Signature: BCS_Ordinal_1to5[] → scalar
- Preconditions: `CSLC_PROOF_REQUIRED(BCS)`
- **Lawful: НЕТ** — Guard Macro отклоняет. BCS — ordinal. Mean незаконен.
- Fallback: `Median_BCS` — lawful (ordinal, rank-preserving)

### C3 — Acceptance Clauses

**Acceptance: Normal_BHB_Range**
- BHB_Serum_Postpartum < 1.2 ммоль/л → ACCEPT
- 1.2–1.5 ммоль/л → PARTIAL (selected-set: {MONITOR, RECHECK_24H})
- > 1.5 ммоль/л → REJECT (требуется ветеринарное вмешательство)
- Missing / stale (> 48h) → ABSTAIN (vet manual check)

**Acceptance: Optimal_BCS_Range**
- BCS_Ordinal_1to5 ∈ {3, 3.5} → ACCEPT
- BCS ∈ {2, 4} → PARTIAL
- BCS ∈ {1, 5} → REJECT
- Missing → ABSTAIN

### C4 — Flow

**Flow: MetabolicAlert_Daily**
- DAG: RawBHB → DailyMean_BHB → Classify_BHB_Category
- Gate: Normal_BHB_Range
- Result kind: SELECTED_SET
  - Output: {NORMAL, ELEVATED, CRITICAL, MANUAL_CHECK}
- Decision-relevant outputs: ELEVATED, CRITICAL
- Report-only: NORMAL (логируется, не алертит)

**Flow: BodyCondition_Weekly**
- DAG: BCS_Records → Median_BCS → Classify_BCS_Category
- Gate: Optimal_BCS_Range
- Result kind: SELECTED_SET (ordinal → нет scalar dominance)
  - Output: {OPTIMAL, LOW_MONITOR, HIGH_MONITOR, CRITICAL}

### C5 — Evidence Wiring

**EvidenceProfile: EP_Farm_MB_2026**
- Lane G (лаборатория): BHB, NEFA, Glucose
  - Anchors: VetLab-Cert-2024, QC-Sample-Log
- Lane F (фермерские наблюдения): BCS, аппетит, манура
  - Anchors: ObserverTrainingCert-2023, BCS-Calibration-Log
- Lane R (литература): пороги из NASEM-2021
  - Anchors: NASEM-2021-ISBN, Drackley-2018-DOI
- Freshness: G — 48h; F — 7 дней; R — 5 лет (литература)
- Penalty routing: stale G-data → R_eff elevated; stale F-data → R_eff moderate

### C6 — ProofLedger (фрагмент)

| Flow/Operator | Legality Proof | Boundedness | Degradation Condition |
|---|---|---|---|
| DailyMean_BHB | CSLC-Ratio-Mean-001 | mean bounded [0, ∞) | If N < 2 → degrade to ABSTAIN |
| Median_BCS | CSLC-Ordinal-Median-002 | median rank-preserving | If N < 5 → degrade to MANUAL_CHECK |
| MetabolicAlert | Threshold-NASEM-2021-1.2 | tri-state bounded | If stale data → ABSTAIN + alert vet |

### C7 — Publication

CAL Pack опубликован в UTS:
- Name Cards для всех OperatorId, ClauseId, FlowId
- RSCR tests:
  - Попытка Average_BCS — отклонена (illegal ordinal arithmetic detected)
  - Попытка CrossLab mean — отклонена (REFPLANE_UNIFORM failed)
  - Abstain на stale данных — подтверждён
- Worked examples: Path/PathSlice для каждого Flow
- Deprecation notice: «При смене лаборатории — edition bump + review Acceptance clauses»

---

## 6. Практика: с чего начать

**Шаг 1. Назовите один оператор, который вы сейчас используете.**
«Средний удой», «суммарный корм», «сравнение с порогом». Запишите: какие входные данные он принимает?

**Шаг 2. Проверьте легальность через CHR.**
Есть ли у вас CHR Pack? Какие guard macros применимы? Если mean(BCS) — система должна сказать «нет».

**Шаг 3. Определите одну Acceptance Clause.**
Возьмите один порог (BHB, соматика, pH). Запишите: что = ACCEPT, что = REJECT, что = ABSTAIN при пропуске?

**Шаг 4. Проверьте EvidenceProfile.**
Откуда данные? Какая у них свежесть? Что происходит, если данные просрочены? Куда идёт penalty?

**Шаг 5. Проверьте, что Flow возвращает.**
Если результат неоднозначен — возвращает ли ваша система scalar (одно число) или selected-set (множество вариантов)? Selected-set — безопаснее.

---

## 7. Проверь себя

| Вопрос | Если ответ «не знаю» — проблема |
|---|---|
| Можете ли вы назвать 3 оператора в вашей системе и их CHR-сигнатуры? | Операторы не типизированы — риск illicit ops |
| Есть ли явные пороги ACCEPT/REJECT/ABSTAIN для каждого показателя? | Acceptance scattered — решения непредсказуемы |
| Что ваша система делает при пропуске данных? | Missingness-as-Zero или Silent Degrade |
| Возвращает ли система scalar, когда порядок частичный? | Scalar Obsession — ложная уверенность |
| Привязаны ли пороги к конкретным источникам (статьям, протоколам)? | Threshold Laundering — пороги невоспроизводимы |
| Может ли ваша система отклонить операцию «средний BCS»? | Tool-as-Semantics — инструмент решает вместо CAL |

---

## 8. Связи

- **G.3 CHR Authoring** — поставщик типизированных характеристик, scale, legality matrix, guard macros. CAL потребляет CHR Pack.
- **G.2 SoTA Harvester** — поставщик Claim Sheets и MethodFamilyCards, на основе которых CAL строит acceptance и evidence profiles.
- **G.5 Selector & Dispatch** — потребитель TaskMap@Context. CAL Pack передаёт selector'у eligible flows, gating clauses, evidence profiles.
- **G.Core** — универсальные инварианты: tri-state guard, penalties→R_eff-only, set-return semantics, GateCrossing discipline.
- **B.3 Trust / Freshness / Decay** — управляет freshness envelopes, lane tags, penalty routing в evidence profiles.
- **A.10 Provenance Anchors** — обеспечивает addressable evidence surfaces для CAL.EvidenceProfile.
- **E.18 / A.21 / F.9 / F.17 / E.17** — GateCrossing / CrossingBundle harnesses. CAL блокирует publication, если required crossing artefacts отсутствуют.
- **G.11 Refresh Orchestration** — потребляет edition/policy pins из CAL Pack для пересмотра при drift.

---

*Этот capture создан в рамках PACK-cattle-science для перевода архитектурного паттерна FPF в предметную область молочного скотоводства.*
