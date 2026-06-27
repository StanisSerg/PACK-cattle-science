---
type: fpf-study
pattern: F.9
title: "Bridges & Congruence Levels: переноси смыслы между контекстами, не смешивая их"
domain: cattle-science
difficulty: intermediate
reading_time: 20 min
created: 2026-06-27
fpf_context: ["F.9", "F.9.1", "A.1.1", "A.6.9", "A.6.3.CSC", "B.3", "F.7", "F.17", "E.10"]
---

# F.9 — Bridges & Congruence Levels: переноси смыслы между контекстами, не смешивая их

> **Цель capture:** объяснить, как в FPF переносят термины и утверждения из одного контекста в другой так, чтобы сохранить локальный смысл и явно записать, что при этом теряется.

---

## 1. Зачем это читать

В животноводстве одно и то же слово часто означает разное в разных источниках: «требование к Mg» в NASEM-2021, у Weiss и на ферме — это разные сущности. Если молча считать их одинаковыми, рацион получится неверным, а решение — ненадёжным. F.9 учит строить между такими смыслами явные мосты: с видом связи, направлением, уровнем конгруэнтности и записями о потерях.

> **FPF-тезис:** *«Мосты нужны не для того, чтобы доказать, что всё одинаково. Мосты нужны для того, чтобы явно записать, что теряется при переходе.»*

**Фермерский пример:**

> В вебинаре Weiss сказано: «Mg 0,4–0,45 % DM в рационе pre-fresh». В NASEM-2021: «Mg requirement = 0,16 % DM». Один и тот же элемент, но разные контексты: Weiss даёт практическую рекомендацию для высоко-K рационов с учётом антагонизма, NASEM — базовое требование для средней дойной коровы. Без моста цифры выглядят противоречиво.

---

## 2. История одной ошибки

Ферма внедряла протокол профилактики гипокальциемии. Зоотехник увидел две цифры:

- SoTA 1 (Weiss): Mg 0,4 % DM pre-fresh.
- SoTA 2 (NASEM-2021): Mg 0,16 % DM.

Он решил, что одна из них ошибочна, и выбрал 0,16 %, потому что «NASEM новее». В итоге коровы на высоко-K рационе получили недостаточно Mg, и случаи гипокальциемии участились.

Проблема была не в цифрах, а в отсутствии моста. Если бы был explicit Bridge Card, было бы видно: Weiss 0,4 % — более широкое (broader) понятие, которое включает safety margin и K-антагонизм; NASEM 0,16 % — базовое (narrower) требование. Переход Weiss → NASEM безопасен в части базового требования; обратный — требует проверки контекста.

---

## 3. Alignment and Bridge across Contexts — полное описание

### 3.1 Определение

**Bridge (F.9)** — это явно объявленная связь между двумя локальными смыслами (`SenseCells`) из разных `U.BoundedContext`. Bridge фиксирует вид связи, направление, уровень конгруэнтности (`CL`), потери и допустимое использование при переходе из одного контекста в другой.

### 3.2 Почему это важно

Без Bridge одинаковые или похожие термины начинают работать как скрытая онтология: люди подменяют написание смыслом, переносят выводы туда, где они не применимы, и смешивают проектирование с исполнением. F.9 делает каждый переход проверяемым и ограничивает его допустимое использование.

### 3.3 Bridge Card — обязательные поля

**Определение.** `BridgeCard` — это компактная запись о мосте, который публикуется, когда cross-context use становится live. Обязательные поля: `CellA`, `CellB`, `senseFamilyA`, `senseFamilyB`, `BridgeKind`, `Direction`, `CL`, `LossNotes`, `CounterExampleOrInvariantEvidence`, `AdmittedUse`, `NonAdmittedUse`, `DirectGoverningPatternIfNotF9`, `RevisionTrigger`.

**Пояснение.** Каждый Bridge относится к паре локальных смыслов, а не к целым контекстам и не к строкам. `AdmittedUse` ограничивает сильнейшее использование, которое мост разрешает; `NonAdmittedUse` перечисляет соблазнительные overclaim'ы, которые требуют открытия прямого паттерна.

**Пример из животноводства.**

```text
BridgeCard:
  CellA: Weiss_2024 #MgPreFresh (high-K practical recommendation)
  CellB: NASEM_2021 #MgRequirement (base requirement)
  senseFamilyA: MethodRecommendation
  senseFamilyB: NutrientRequirement
  BridgeKind: Broader-than (Weiss ⊃ NASEM)
  Direction: NASEM → Weiss safe; Weiss → NASEM unsafe without K-context check
  CL: 2 (translatable with stated losses)
  LossNotes: Weiss includes safety margin and K-antagonism; NASEM omits them.
  CounterExampleOrInvariantEvidence: high-K diet without extra Mg shows hypocalcemia risk
  AdmittedUse: naming-only row and role-description naming; no direct substitution into ration
  NonAdmittedUse: do not replace NASEM base with Weiss value without checking K context
  DirectGoverningPatternIfNotF9: C.16 / A.19.CHR for ration calculation; C.26 for cross-context transport
  RevisionTrigger: K level in diet, source edition, or new counter-example
```

**Ключевой признак.** Любой cross-context use сопровождается опубликованным Bridge Card с явным `CL` и Loss Notes.

### 3.4 Виды мостов

**Определение.** F.9 различает **substitution bridges** (в одном `senseFamily`, допускают ограниченную подстановку смысла) и **interpretation bridges** (между разными `senseFamily`, только объяснение).

**Пояснение.** Substitution bridges: `Equivalence` (почти тождество, симметрично, редкость), `Narrower-than` / `Broader-than` (один смысл включает другой, направлено), `Partial-overlap` (пересечение без включения), `Disjoint` (явное различие). Interpretation bridges: `Design-spec-to-run-occurrence`, `Measurement-evidence-for`, `Policy-constraint-on`, `Viewpoint-correspondence`.

**Пример из животноводства.**

| Вид | Пример |
|---|---|
| Equivalence | `NASEM-2021 Mg req ↔ NRC-2001 Mg req` при CL=3 с незначительными редакционными различиями |
| Broader-than | `Weiss pre-fresh Mg` ⊃ `NASEM base Mg` — Weiss шире |
| Partial-overlap | `DCAD у Weiss (pH мочи)` ⋂ `DCAD у формулировщика (mEq/kg)` — пересечение, но не тождество |
| Disjoint | «Mg в % DM» vs «Mg в массе элемента» — разные шкалы до явного преобразования |
| Interpretation | `BHB в крови` → `кетозный статус` — измерение объясняет состояние, но не заменяет его |

**Ключевой признак.** Substitution bridge сохраняет `senseFamily`; interpretation bridge пересекает семейства, но не допускает подстановки.

### 3.5 CL scale и допустимое использование

**Определение.** `Congruence Level (CL)` — ординальная шкала от 0 до 3, которая показывает, насколько безопасно переносить смысл через мост. CL определяет admitted use: Naming-only, Role-description naming, Type-structure row или Explanation-only.

**Пояснение.** CL3 требует инвариантного доказательства и допускает Type-structure row. CL2 требует контр-примера и ограниченных потерь. CL1 — только Naming-only. CL0 — contrastive explanation. Низкий CL штрафует `R` в B.3, но не оправдывает подстановки.

**Пример из животноводства.**

| CL | Название | Что допускается | Пример |
|---|---|---|---|
| 3 | Near-identity | Type-structure row, инвариантная подстановка | `NASEM-2021 Mg req = NRC-2001 Mg req` |
| 2 | Translatable | Naming-only; role-description naming при том же senseFamily | `Weiss pre-fresh Mg ⊃ NASEM base Mg` |
| 1 | Comparable | Только Naming-only | `DCAD` как метка без подстановки pH ↔ mEq/kg |
| 0 | Opposed | Только контрастивное объяснение | «Mg требование в % DM» vs «в массе» до преобразования |

**Ключевой признак.** Каждый Bridge публикует `CL` и Loss Notes; row не сильнее слабейшего Bridge.

### 3.6 Weakest-link, direction guard и loss accumulation

**Определение.** Row, использующий несколько Bridges, ограничен слабейшим из них: `admittedUse(row) ≤ min_i admittedUse(Bridge_i)` и `CL(row) ≤ min_i CL(Bridge_i)`. Направленные Bridge'и не инвертируются. Цепочки Bridge'ей накапливают потери и понижают CL.

**Пояснение.** Это защита от scope creep: нельзя усилить утверждение за счёт комбинации мостов. Direction guard говорит, что `Narrower-than A → B` не даёт права заменять B на A. Loss accumulation говорит, что A → B с потерями L1 и B → C с потерями L2 даёт A → C с потерями L1+L2.

**Пример из животноводства.**

> Мост 1: `NASEM Mg req → Weiss pre-fresh Mg` (Broader-than, CL2, loss: K context).
> Мост 2: `Weiss pre-fresh Mg → FarmA actual ration Mg` (Interpretation, CL2, loss: source variability, farm conditions).
> Цепочка: `NASEM → FarmA` сохраняет senseFamily только при CL = min(2,2)=2, но loss notes накапливают оба набора потерь. Нельзя сказать: «поскольку NASEM рекомендует 0,16 %, ферма должна дать 0,4 %».

**Ключевой признак.** Row, Bridge и цепочка Bridge'ей всегда проверяются по weakest-link и direction.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«В NASEM-2021 и у Weiss сказано одно и то же про Mg, значит, можно взять любую цифру.»*

**Разложение по F.9:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «одно и то же про Mg» | смешение `SenseCells` | Разные контексты, разные senseFamily |
| «можно взять любую цифру» | несанкционированная подстановка | Нет Bridge Card с CL и Loss |
| (скрытое) «NASEM новее» | аргумент об источнике, не о смысле | Authority bias, вместо bridge reasoning |

**Основные риски смешивания:**

1. **String-equals fallacy.** Одинаковое написание принимается за одинаковое значение.
2. **Scope creep.** Naming convenience растягивается до замены рациона или назначения роли.
3. **Direction amnesia.** Асимметричный мост используют в обе стороны.
4. **Loss blindness.** Единицы, масштаб, методология и контекст остаются незамеченными.
5. **DesignRunTag jumping.** Модель (NASEM) подменяет реальность (фактический рацион).

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** сопоставить рекомендации по Mg и DCAD из разных источников.

**Было (смешанное / нечёткое):**

> «Weiss говорит 0,4 %, NASEM — 0,16 %. Возьмём среднее.»

**Стало (разложенное / ясное):**

**Bridge Card 1 — Mg requirements:**

```text
Bridge ID: BRIDGE-F9-001
From: CS.SOTA.332 (Weiss) — Mg pre-fresh 0.4–0.45% DM
To: CS.SOTA.301 (NASEM-2021) — Mg requirement 0.16% DM
Kind: Broader-than (Weiss ⊃ NASEM)
Direction: NASEM → Weiss safe; Weiss → NASEM unsafe without K check
CL: 2
Loss Notes: Weiss adds safety margin + K antagonism; NASEM is base for average cow.
Admitted use: naming row, role-description naming, explanation.
Non-admitted use: direct substitution into ration without K-context check.
```

**Bridge Card 2 — DCAD pH vs mEq/kg:**

```text
Bridge ID: BRIDGE-F9-002
From: Weiss — «DCAD effective if urinary pH < 7»
To: Weiss — «DCAD optimal -100 to -200 mEq/kg»
Kind: Partial-overlap
Direction: symmetric but disconnected languages
CL: 1
Loss Notes: pH is mechanism language; mEq/kg is practical target. No explicit conversion verified.
Admitted use: naming-only orientation.
Non-admitted use: automatic pH → mEq/kg substitution.
```

**Результат:**

- Каждый источник сохраняет свой локальный смысл.
- Переходы документированы и ограничены.
- Рацион рассчитывается с учётом явных потерь, а не похожих цифр.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Найдите в своём PACK два источника с «похожими» claim'ами.

**Шаг 2.** Задайте вопросы:
- Это тождество? → `Equivalence` (редко).
- Одно включает другое? → `Narrower-than` / `Broader-than`.
- Есть пересечение? → `Partial-overlap`.
- Это разные вещи? → `Disjoint`.
- Это измерение и то, что оно объясняет? → `Interpretation` bridge.

**Шаг 3.** Определите `CL`:
- CL3 — инварианты совпадают, нет материальных контр-примеров.
- CL2 — механизм объясняет связь, есть контр-примеры.
- CL1 — похоже, но не проверено.
- CL0 — догадка или контраст.

**Шаг 4.** Запишите `Loss Notes`: единицы, шкала, контекст, методология, порода, сезон, источник.

**Шаг 5.** Создайте Bridge Card. Не полагайтесь на память или на «понятно и так».

**Шаг 6.** Проверьте weakest-link: row не сильнее слабейшего Bridge.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Используете термины из разных источников как взаимозаменяемые? | String-equals fallacy |
| Переносите результаты с одной фермы/региона на другую без оговорок? | Scope creep |
| Считаете отношение «Weiss ⊃ NASEM» симметричным? | Direction amnesia |
| Забываете записать, что теряется при переходе? | Loss blindness |
| Подменяете модель (NASEM) фактическим рационом? | DesignRunTag jumping |
| Row требует большего, чем разрешает weakest Bridge? | Row outruns Bridge |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.1.1 BoundedContext | Bridge связывает SenseCells из разных контекстов |
| A.6.9 RPR-XCTX | ремонт cross-context «same/equivalent/align» |
| A.6.3.CSC | Controlled Semantic Coarsening — граница Bridge и coarsened note |
| B.3 F-G-R | CL штрафует R при агрегации |
| F.7 Concept-Set rows | строки таблицы понятий зависят от Bridge |
| F.9.1 Bridge Stance Overlay | stance-аннотации поверх Bridge Card |
| F.17 UTS | публикация cross-context терминов |
| E.10 LEX-BUNDLE | лексический триггер-скан перед Bridge |
| C.26 Cross-Context Transport | Bridge — семантическая основа transport |

---

## 9. Что запомнить

1. Bridge — это declared correspondence между двумя локальными смыслами, не синоним и не онтология.
2. Всегда указывайте kind, direction, CL и Loss Notes.
3. Substitution bridges сохраняют senseFamily; interpretation bridges — только объясняют.
4. Row не может быть сильнее слабейшего Bridge (weakest-link).
5. Одинаковое написание не доказывает одинаковое значение.

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §F.9*
