---
type: fpf-study
pattern: G.7
title: "Калибровочный набор междутрадиционных мостов: когда одно и то же — не одно и то же"
domain: cattle-science
difficulty: hard
reading_time: 22 min
created: 2026-05-26
---

# G.7 — Cross-Tradition Bridge Calibration Kit

## 1. Зачем это читать

Если вы когда-нибудь сравнивали «уровень мастита на своей ферме» с «уровнем мастита в Нидерландах» и думали, что говорите об одном и том же — вы, скорее всего, ошибались.

В США «мастит» может учитываться по клиническим случаям, записанным дояркой. В Новой Зеландии — по соматическим клеткам в баклаборатории. В России — по визуальной оценке ветеринара. Это **три разных конструкта**, замаскированных под одно слово.

G.7 учит, как **материализовать** сравнение между контекстами в проверяемые артефакты: `BridgeCard`, `BridgeCalibrationTable (BCT)`, `CalibrationLedger`, `RegressionSet`, `SentinelSet` — вместо того чтобы полагаться на «ну, это же очевидно».

---

## 2. История одной ошибки

Консалтинговая компания «AgriGlobal» разработала для фермы «Молочная река» норматив по маститу: *«Держите уровень ниже 20%»*. Норматив был позаимствован из новозеландского отчёта, где 20% считалось по SCC > 200 000, с лабораторным контролем каждую неделю.

На «Молочной реке»:
- Учёт вёлся по клиническим случаям (не SCC).
- Лаборатория работала раз в месяц.
- Доярки не записывали лёгкие случаи.

Результат: ферма «держала 15%» и считала себя в безопасности. На самом деле, если бы пересчитать по SCC с еженедельным контролем, показатель был бы 35%+. Ферма пропустила вспышку субклинического мастита, потому что **мост между NZ-контекстом и своим фермерским контекстом был не откалиброван**.

Если бы G.7 был применён, `BridgeCard` для «мастита» содержал бы:
- `ReferencePlane(src)` = NZ_dairy_SCC_weekly
- `ReferencePlane(tgt)` = RU_farm_clinical_monthly
- `RowCL_min = 1` (NOT admissible без явного `Waiver`)
- `LossNote`: «разные определения случая, разная частота контроля, разная чувствительность"

Компания бы увидела: переход запрещён или только guarded. Вместо этого она увидела «20%» и успокоилась.

---

## 3. Core concepts

### 3.1 BridgeMatrix → BridgeCards: от намёток к артефактам

`BridgeMatrix` (из G.2) — это инвентарь «сопоставимых конструктов» между традициями с предварительными заметками. Но потребители (селекторы, логгеры, аудиторы) **не могут** безопасно использовать матрицу, пока переходы не **материализованы** в явные артефакты.

`BridgeCard` (из F.9) — это проверяемый артефакт для конкретного `SenseCell`-уровня выравнивания. Он не говорит «это почти то же самое». Он говорит: «вот точное соответствие, вот потери, вот `CL`, вот политика».

**На ферме:** не «мастит в NZ ≈ мастит в RU», а:
- `BridgeCard_Mastitis_NZ_RU_001`: SCC>200k_weekly_lab ↔ clinical_signs_monthly_visual
- Потери: чувствительность к лёгким случаям, регулярность, объективность
- `CL = 1` — reuse только под явным waiver

### 3.2 BCT (Bridge Calibration Table) — таблица калибровки

`BCT` — это реестр откалиброванных записей для пары традиций. Каждая запись (`RowEntry`) содержит:

| Поле | Смысл |
|---|---|
| `RowEntryId` | Идентификатор записи |
| `ComparableConstructId` | Что сравнивается (например, «уровень мастита») |
| `BridgeCardId[]` | Какие BridgeCards материализуют переход |
| `RowCL_min` | Минимальный CL в строке (bottleneck) |
| `LossNoteRef[]` | Потери — не информативные сноски, а первоклассные цитаты |
| `CounterExampleRef[]` | Контрпримеры, если CL ≤ 2 |
| `PolicyPins` | `Φ(CL)`, `Ψ(CL^k)?`, `Φ_plane?` — идентификаторы политик |
| `PlanePins` | `ReferencePlane(src)`, `ReferencePlane(tgt)` |

**Правило bottleneck:** если строка агрегирует несколько bridge cells, итоговый CL — **минимум**, не среднее.

### 3.3 CalibrationLedger — аудируемая «история строки»

`CalibrationLedger` — это запись о том, что было откалибровано, что было потеряно, какие артефакты и политики это подтверждают.

**На ферме:** для строки «мастит NZ↔RU» ledger содержит:
- Дата калибровки
- Какие BridgeCards использовались
- Почему `CL = 1`
- Какие waiver были применены
- Результаты regression run (если проводился)

### 3.4 RegressionSet — регрессионные пробы

`RegressionSet` — это небольшой набор тестов, которые можно запустить против BCT для обнаружения дрейфа:
- Изменения bridge
- Изменения политик
- Изменения плоскостей
- Изменения edition pins

**На ферме:** если NZ изменила определение мастита (новое издание стандарта), `RegressionSet` обнаружит, что `BridgeCard_Mastitis_NZ_RU_001` больше не валиден, и выдаст RSCR trigger.

### 3.5 SentinelSet & BridgeSentinel — дозорные

`BridgeSentinel` следит за изменениями в калибровке и генерирует типизированные RSCR-триггеры для затронутых `PathId/PathSliceId`.

**Ключевой момент:** триггеры — **путь-локальные**, не pack-wide. Если изменился один BridgeCard, пересчитывается только связанный с ним путь, а не весь пакет.

### 3.6 CL / CL^k / CL^plane — режимы допустимости

| Уровень | Значение | Допустимость |
|---|---|---|
| `RowCL_min = 3` | Полное доверие | Admissible, но всё равно с `LossNote` если присутствует |
| `RowCL_min = 2` | Ограниченное доверие | Admissible с guards |
| `RowCL_min = 1` | Низкое доверие | **NOT admissible** без явного `WaiverRef[]`; reuse только guarded |
| `RowCL_min = 0` | Запрещено | Forbidden; остаётся в BCT как документированный non-bridge |

**Kind channel (`CL^k`):** если переход затрагивает kind (например, метод → измерение), требуется `RowCL_k_min` и `Ψ(CL^k)`.

**Plane guard (`CL^plane`):** если `ReferencePlane(src) ≠ ReferencePlane(tgt)`, требуется `RowCL_plane_min` и `Φ_plane`. Плоскость **не переписывает** `CL/CL^k`; её эффект маршрутизируется через политики.

### 3.7 Honesty rule — правило честности

- Если `RowCL_min ≤ 2` — нужен хотя бы один `CounterExampleRef`
- Если `RowCL_min = 3` и нет контрпримеров — нужен `CounterExampleAbsenceRef` (явное «искали — не нашли»)
- Если есть `LossNoteRef[]`, строка **не может** быть представлена как «free substitution"

---

## 4. Антипаттерны

| Антипаттерн | Почему опасно | Как выглядит на ферме |
|---|---|---|
| **«Синонимия» (Informal Synonymy)** | Полагаться на «это же одно и то же» без материализации моста. | «Мастит и мастит — везде мастит» — без учёта разных определений. |
| **«Средний CL» (Averaged CL)** | Усреднение CL по строке вместо bottleneck (минимум). | «В среднем доверие 2.5» — когда один cell даёт CL=1, а другой CL=3. |
| **«Скрытая плоскость» (Hidden Plane)** | Игнорирование разницы в `ReferencePlane` (мир ↔ концепт ↔ эпистема). | Сравнение «практического опыта фермера» (world) с «лабораторным исследованием» (episteme) без явного plane guard. |
| **«Вечный мост» (Eternal Bridge)** | BridgeCard без edition pins и freshness window — дрейф не обнаруживается. | Использование моста 2015 года без проверки, изменились ли определения в источнике или приёмнике. |
| **«Waiver как лекарство» (Waiver Abuse)** | Понижение CL до 1 и использование waiver для обхода проверки. | «Ну, CL=1, но мы подпишем waiver» — без понимания, что reuse всё равно guarded-only. |

---

## 5. Пример на ферме: калибровка «уровня мастита» между США и Новой Зеландией

**Сравниваемые конструкты:** «уровень мастита» в US Midwest dairy research и NZ dairy industry reports.

**Шаг 1. Материализация BridgeCards**

| SenseCell | US (src) | NZ (tgt) | Loss Notes |
|---|---|---|---|
| Определение случая | Клинические признаки + ветеринарный осмотр | SCC > 200 000 (лаборатория) | NZ не ловит лёгкие клинические случаи; US зависит от квалификации ветеринара |
| Частота контроля | По факту случая | Еженедельная лаборатория | Разная чувствительность к вспышкам |
| Порода | Преимущественно Holstein | Преимущественно Jersey | Разная восприимчивость к маститу |
| Кормовая база | Corn silage + alfalfa | Пастбищная система | Разная метаболическая нагрузка |

**BridgeCards:**
- `BC-Mastitis-Def-US-NZ-001`: определение случая → `CL=1`
- `BC-Mastitis-Freq-US-NZ-001`: частота → `CL=1`
- `BC-Mastitis-Breed-US-NZ-001`: порода → `CL=2`
- `BC-Mastitis-Diet-US-NZ-001`: корм → `CL=1`

**Шаг 2. BCT RowEntry**

```
RowEntryId: RE-Mastitis-US-NZ-001
ComparableConstructId: Mastitis_Rate
BridgeCardId: [BC-Mastitis-Def-001, BC-Mastitis-Freq-001, BC-Mastitis-Breed-001, BC-Mastitis-Diet-001]
RowCL_min: 1  // bottleneck: min(1,1,2,1)
RowCL_k_min: 1
RowCL_plane_min: 1  // world (US фермы) → episteme (NZ отчёты)
LossNoteRef: [LN-001, LN-002, LN-003, LN-004]
CounterExampleRef: [CE-2019-NZ-SCC-underestimation]
WaiverRef: []  // нет waiver — reuse запрещён
PolicyPins: Φ(CL)=POL-TRUST-MASTITIS-001, Ψ(CL^k)=POL-KIND-001, Φ_plane=POL-PLANE-001
PlanePins: ReferencePlane(src)=US_Farm_World, ReferencePlane(tgt)=NZ_Report_Episteme
```

**Шаг 3. CalibrationLedger**

```
LedgerId: CL-Mastitis-US-NZ-2026
Entry:
  - RowEntryId: RE-Mastitis-US-NZ-001
  - BridgeCards: [BC-001, BC-002, BC-003, BC-004]
  - CL-minima: [1,1,2,1]
  - Bottleneck: 1
  - Losses: 4 notes, 1 counterexample
  - Waiver: none
  - UTS rows: published
  - RegressionRunRef: RR-2026-05-15 (all failed — expected)
```

**Шаг 4. SentinelSet**

```
BridgeSentinel:
  SentinelId: SENT-Mastitis-US-NZ
  watchedBridgeIds: [BC-001, BC-002, BC-003, BC-004]
  watchedScope: [PathSliceId-Mastitis-001, PathSliceId-Mastitis-002]
  payloadPins: {BCT.id=BCT-Mastitis-US-NZ, RegressionSetId=RS-001, FreshnessWindowRef=FW-2026}
```

**Итог:** любой потребитель, который хочет использовать «уровень мастита» из NZ для US-контекста, видит: **запрещено (CL=0/1)** или **guarded-only с явным waiver**. Никаких «ну, это же стандартный показатель».

---

## 6. Практика

**Шаг 1. Выберите пару контекстов.**
Возьмите два контекста, которые вы обычно смешиваете (например, «европейские исследования» и «моя ферма»).

**Шаг 2. Найдите один comparable construct.**
Один термин, который встречается в обоих контекстах (например, «конверсия корма», «уровень мастита»).

**Шаг 3. Разложите на SenseCells.**
На каком уровне детализации термины совпадают? Определение? Метод измерения? Частота? Порода?

**Шаг 4. Создайте BridgeCards.**
Для каждого SenseCell: что в src, что в tgt, какие потери. Назначьте CL честно (не оптимистично).

**Шаг 5. Вычислите bottleneck.**
`RowCL_min = min(CL всех cells)`. Не усредняйте.

**Шаг 6. Запишите LossNotes и CounterExamples.**
Если CL ≤ 2 — обязательны контрпримеры. Если CL = 3 без контрпримеров — запишите `CounterExampleAbsenceRef`.

**Шаг 7. Опубликуйте и подключите SentinelSet.**
Создайте `RegressionSet` для проверки дрейфа и `SentinelSet` для RSCR-триггеров.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Сравниваете ли вы показатели с других ферм/стран без явной калибровки? | Informal Synonymy |
| Усредняете ли вы «доверие» к нескольким аспектам перехода? | Averaged CL |
| Считаете ли вы, что «практический опыт» и «научное исследование» сравнимы без оговорок? | Hidden Plane |
| Используете ли вы мосты, созданные более 3 лет назад, без перепроверки? | Eternal Bridge |
| Применяете ли вы waiver, чтобы «пропустить» сомнительный переход? | Waiver Abuse |

---

## 8. Связи

- **G.Core** — универсальные инварианты: penalty routing к R_eff, tri-state guard, типизированные RSCR triggers.
- **G.2 (SoTA Synthesis)** — поставщик `BridgeMatrix`, который G.7 материализует в `BridgeCards`.
- **F.9 (BridgeCard + CL)** — семантика BridgeCard и confidence level; G.7 добавляет калибровку.
- **F.3/F.7 (SenseCell)** — anchoring на уровне SenseCell; bottleneck discipline.
- **G.6 (Evidence Graph)** — `PathId/PathSliceId` цитируют BridgeCards в графах доказательств.
- **G.5 (Method Dispatcher)** — потребитель калиброванных переходов для eligibility/selection.
- **G.11 (Refresh Orchestration)** — потребитель RSCR triggers от SentinelSet.
- **C.21 (DHC)** — `AlignmentDensity` и другие метрики, если bridge используется для QD.
- **E.18/A.21 (GateCrossing)** — проверка crossing bundles через harness.

---

*Этот capture создан в рамках изучения FPF Part G для PACK-cattle-science.*
*Цель: сделать архитектурный паттерн читаемым без погружения в 50 страниц спецификации.*
