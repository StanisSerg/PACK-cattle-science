---
type: fpf-study
pattern: G.7
title: "Bridge Calibration: калибровка мостов между традициями в скотоводстве"
domain: cattle-science
difficulty: advanced
reading_time: 30 min
created: 2026-06-27
fpf_context: ["G.7", "G.2", "G.Core", "F.9", "G.9", "G.11"]
---

# G.7 — Bridge Calibration: калибровка мостов между традициями в скотоводстве

> **Цель capture:** объяснить, как паттерн G.7 превращает предварительные строки BridgeMatrix в калиброванные BridgeCards, BridgeCalibrationTable, RegressionSet и SentinelSet, пригодные для безопасного повторного использования между традициями.

---

## 1. Зачем это читать

В скотоводстве одно и то же понятие часто встречается в разных традициях: «субклинический кетоз» у ветеринара означает BHB в крови, у нутрициолога — энергетический дефицит в рационе, у генетика — полигенный риск. SoTA Harvester (G.2) фиксирует эти сходства в BridgeMatrix, но для безопасного использования их нужно откалибровать: явно задать scope, уровень доверия, потери и политики штрафов. G.7 выполняет эту калибровку.

> **FPF-тезис:** *«Сравнимость между традициями — не синонимия, а откалиброванный мост с явными потерями и политиками.»*

**Фермерский пример:**

> Фермер хочет использовать молочный тест на кетоновые тела вместо лабораторного BHB для скрининга. Поставщик говорит, что «это практически одно и то же». G.7 требует создать BridgeCard, в котором указано: row scope = «бинарная классификация риска кетоза», RowCL_min = 2 ( guarded reuse ), LossNote = «теряется количественное значение BHB», RegressionSet = «проверка чувствительности при смене порога».

---

## 2. История одной ошибки

Хозяйство внедрило новый онлайн-сервис, который обещал «переводить» результаты молочного кетонового теста в BHB. Сервис использовал неявное соответствие без BridgeCard. Через несколько месяцев выяснилось, что при низких удоях тест давал ложноположительные результаты, а при высоких — ложноотрицательные. Поскольку соответствие не было откалибровано, потери не были видны, и фермер принимал неверные решения о лечении.

---

## 3. Bridge Calibration — полное описание

### 3.1 Определение

**Bridge Calibration** — это паттерн, который превращает строки BridgeMatrix из G.2 в явные BridgeCards (F.9), публикует BridgeCalibrationTable (BCT), CalibrationLedger, RegressionSet и SentinelSet, и настраивает typed RSCR triggers для отслеживания изменений.

### 3.2 Почему это важно

Неявные соответствия между традициями создают иллюзию эквивалентности. G.7 заставляет автора явно указать: что именно считается сопоставимым, какие потери возникают, какой уровень доверия допустим и какие policy pins управляют штрафами. Это делает cross-tradition reuse аудитоспособным и обновляемым.

### 3.3 BridgeCalibrationTable (BCT)

**Определение.** BCT — это таблица калибровки мостов для пары традиций, содержащая RowEntry для каждого сопоставимого конструкта.

**Пояснение.** Каждая RowEntry связывает ComparableConstructId, BridgeCardId[], RowCL_min, PlanePins, PolicyPins, RegressionSetId и SentinelSetId. BCT делает калибровку проверяемым объектом, а не описанием в тексте.

**Пример из животноводства.**

```text
BCT-001: BridgeCalibrationTable
  TradPairId: veterinary ↔ nutrition
  RowEntry RE-001:
    - ComparableConstructId: subclinical_ketosis_risk
    - BridgeCardId: [BC-001, BC-002]
    - RowCL_min: 2
    - RowScopeId: binary_risk_classification
    - PlanePins: ReferencePlane(src)=world, ReferencePlane(tgt)=world
    - PolicyPins: Φ(CL)=POL-001
    - RegressionSetId: RS-001
    - SentinelSetId: SS-001
```

**Ключевой признак.** BCT содержит RowEntryId, BridgeCardId[], RowCL_min, RowScopeId и policy pins.

### 3.4 BridgeCard

**Определение.** BridgeCard — это артефакт F.9, который фиксирует SenseCell-уровневое соответствие между двумя понятиями, включая уровень доверия CL, потери и политики.

**Пояснение.** BridgeCard не утверждает, что понятия «одинаковы». Он заявляет, что при определённом scope и с учётом явных потерь их можно использовать совместно.

**Пример из животноводства.**

```text
BC-001: BridgeCard
  - source: Lab_BHB (mmol/L)
  - target: Milk_Ketone_Test (positive / negative)
  - scope: binary classification of ketosis risk in Holstein cows days 1–30
  - CL: 2
  - LossNoteRef: LN-001 (quantitative BHB value lost)
  - SenseCell anchors: BHB molecule detection
```

**Ключевой признак.** BridgeCard имеет source, target, scope, CL, LossNoteRef и SenseCell anchors.

### 3.5 RowCL_min и admissibility regime

**Определение.** RowCL_min — минимальный уровень доверия для строки BCT. Admissibility regime: CL ≥ 2 разрешает guarded reuse; CL = 1 требует WaiverRef и допускает только guarded-only reuse; CL = 0 запрещает reuse.

**Пояснение.** CL (confidence level) идёт от F.9. G.7 задаёт правила допустимости: только мосты с достаточным уровнем доверия могут использоваться в downstream сравнениях.

**Пример из животноводства.**

| RowCL_min | Интерпретация | Пример |
|---|---|---|
| 3 | free substitution | BHB крови ↔ BHB плазмы при одном методе |
| 2 | guarded reuse | BHB крови ↔ молочный кетоновый тест |
| 1 | reuse только с waiver | BHB ↔ визуальная оценка риска |
| 0 | reuse запрещён | BHB ↔ показатель иммунитета |

**Ключевой признак.** RowCL_min принимает значения {3,2,1,0}, и каждое значение имеет явные условия reuse.

### 3.6 CL^k и CL^plane

**Определение.** CL^k — уровень доверия в kind-канале; CL^plane — уровень доверия при переходе между ReferencePlane. Ψ(CL^k) и Φ_plane — соответствующие policy pins.

**Пояснение.** Если мост использует kind-канал (например, сравнение разных видов кетоза) или переходит между плоскостями (например, от лабораторного измерения к фермерскому наблюдению), должны быть явно указаны дополнительные CL и policy pins.

**Пример из животноводства.** Переход от понятия «кетоз как клиническое заболевание» (kind) к «субклинический кетоз как метаболический риск» требует CL^k и Ψ(CL^k), потому что это разные категории заболевания.

**Ключевой признак.** При kind-bridge или plane-bridge в BCT присутствуют RowCL_k_min / RowCL_plane_min и соответствующие policy pins.

### 3.7 RegressionSet

**Определение.** RegressionSet — это набор регрессионных проверок, которые выявляют drift при изменении моста, policy pins или edition pins.

**Пояснение.** Calibration без regression быстро устаревает. RegressionSet содержит TestCaseId[], ExpectedOutcomesRef и RegressionRunRef. Он показывает, что мост остаётся валидным после изменений.

**Пример из животноводства.**

```text
RS-001: RegressionSet
  - TestCaseId: [TC-001, TC-002, TC-003]
  - TC-001: при BHB 1,4 молочный тест должен быть positive
  - TC-002: при BHB 0,8 молочный тест должен быть negative
  - TC-003: смена порога BHB с 1,2 на 1,0 не должна повышать RowCL_min
```

**Ключевой признак.** RegressionSet содержит конкретные проверки и ожидаемые результаты для каждого моста.

### 3.8 SentinelSet

**Определение.** SentinelSet — это набор sentinels, которые отслеживают изменения в bridge calibration и эмитируют typed RSCR triggers для затронутых PathSliceId или PatternScopeId.

**Пояснение.** SentinelSet позволяет G.11 планировать выборочный refresh. Когда меняется BridgeCard, policy pin или edition pin, sentinel эмитирует trigger с scope и payload pins.

**Пример из животноводства.**

```text
SS-001: SentinelSet
  - Sentinel S-001:
    - watchedBridgeIds: [BC-001]
    - watchedScope: [PS-001, PS-002]
    - payloadPins: {BCT-001, RS-001, Φ(CL)=POL-001}
```

**Ключевой признак.** SentinelSet связывает BridgeCardId с PathSliceId и RSCRTriggerKindId.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Молочный тест на кетоновые тела — то же самое, что BHB в крови, только дешевле.»*

**Разложение по G.7:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «молочный тест» | MethodFamilyId | Должен быть в ComparatorSet |
| «BHB в крови» | MethodFamilyId | Должен быть в ComparatorSet |
| «то же самое» | BridgeCard claim | Требует RowCL_min, RowScopeId и LossNoteRef |
| «дешевле» | economic criterion | Относится к CAL/selector, не к bridge |

**Основные риски смешивания:**

1. **Скрытые потери.** Количественная точность BHB теряется, но это не зафиксировано.
2. **Неправильный reuse.** Молочный тест используется как free substitution, хотя CL = 2.
3. **Неотслеживаемые изменения.** Смена порога или метода не вызывает пересчёта downstream решений.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** калибровка перехода от лабораторного BHB к молочному кетоновому тесту.

**Было (смешанное / нечёткое):**
> «Молочный тест заменяет BHB.»

**Стало (разложенное / ясное):**

**BridgeCard BC-001:**
> source: Lab_BHB; target: Milk_Ketone_Test; scope: binary risk classification days 1–30; CL = 2; LossNoteRef LN-001.

**BCT RowEntry RE-001:**
> ComparableConstructId: subclinical_ketosis_risk; RowCL_min = 2; RowScopeId = binary_risk; PolicyPins Φ(CL) = POL-001.

**RegressionSet RS-001:**
> TC-001: BHB 1,4 → milk test positive; TC-002: BHB 0,8 → milk test negative.

**SentinelSet SS-001:**
> S-001 watches BC-001, scope PS-001, payload {BCT-001, RS-001, POL-001}.

**Результат:**
- Переход между методами явен и проверяем.
- Потери зафиксированы и не скрываются.
- Любое изменение моста вызывает typed RSCR trigger.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Возьмите BridgeMatrix из G.2 и для каждой строки определите RowScopeId.

**Шаг 2.** Создайте BridgeCards с SenseCell anchors, CL и LossNoteRef.

**Шаг 3.** Соберите BCT с RowCL_min, PlanePins, PolicyPins, RegressionSetId и SentinelSetId.

**Шаг 4.** Определите RegressionSet с проверками на drift.

**Шаг 5.** Настройте SentinelSet для typed RSCR triggers с PathSliceId scope.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Между традициями нет BridgeCard? | Переход незаконен; возможны скрытые потери. |
| RowCL_min не указан или преувеличен? | Reuse может быть неоправданным. |
| LossNoteRef отсутствует при CL ≤ 2? | Нарушена honesty rule. |
| RegressionSet не задан? | Drift моста останется незамеченным. |
| SentinelSet не связан с PathSliceId? | Обновления потребуют полного пересчёта. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| G.2 SoTA Harvester | предоставляет BridgeMatrix |
| F.9 BridgeCard | определяет семантику BridgeCard и CL |
| G.Core | обеспечивает bridge-only crossings и penalty routing |
| G.9 Parity Harness | использует откалиброванные bridges для сравнения |
| G.11 Telemetry Refresh | потребляет sentinel triggers |

---

## 9. Что запомнить

1. G.7 превращает BridgeMatrix в калиброванные BridgeCards и BCT.
2. Каждая строка BCT имеет RowCL_min, RowScopeId, LossNoteRef и policy pins.
3. Admissibility regime: CL ≥ 2 — guarded reuse, CL = 1 — только с waiver, CL = 0 — запрещено.
4. RegressionSet проверяет drift; SentinelSet эмитирует typed RSCR triggers.
5. BridgeCard — не заявление об эквивалентности, а явное сопоставление с потерями.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.7*
