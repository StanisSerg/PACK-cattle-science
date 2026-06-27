---
type: fpf-study
pattern: E.10
title: "LEX-BUNDLE: восстанавливай смысл слов, прежде чем их использовать"
domain: cattle-science
difficulty: advanced
reading_time: 45 min
created: 2026-06-27
fpf_context: ["E.10", "A.6.P", "A.6.F", "A.3", "A.19.SPR", "C.2.P", "C.16.P", "C.16.Q", "F.18"]
---

# E.10 — Lexical Bundle (LEX-BUNDLE): восстанавливай смысл слов, прежде чем их использовать

> **Цель capture:** объяснить, как в FPF проверяют слова перед их использованием в claim'ах, чтобы расплывчатые термины не заменялись синонимами, а восстанавливался их FPF-род.

---

## 1. Зачем это читать

Если на ферме один и тот же термин означает разное в разных протоколах — «рацион» у зоотехника, «рацион» у ветеринара и «рацион» в учёте затрат, — вы сталкиваетесь с лексической проблемой. Этот паттерн учит не заменять расплывчатые слова синонимами, а восстанавливать их FPF-род: сущность, отношение, шкалу, метод или роль.

> **FPF-тезис:** *«Лексический ремонт — не замена одного слова другим. Это восстановление вида (kind), регистра и допустимого использования.»*

**Фермерский пример:**

> В одном протоколе написано: «При стрессе увеличить витамин С». В другом: «Стресс при транспортировке снижает продуктивность». В третьем: «Социальный стресс в группе тёлок требует перегруппировки». Если не восстановить, что такое «стресс» в каждом случае, получится одно слово для трёх разных `Characteristic`: кортизол, снижение удоя, агрессивное поведение.

---

## 2. История одной ошибки

Ферма внедряла протокол оценки «состояния коровы». В документе использовались слова:

- «состояние тела» — кто-то понял как BCS (Body Condition Score),
- «состояние здоровья» — кто-то понял как клинический скоринг,
- «состояние вымени» — кто-то понял как PALM-оценку.

В результате зоотехник вносил в `HerdLog` BCS под заголовком «Состояние», ветеринар — клинический скоринг под тот же заголовок, а аналитика стала бесполезной: одна колонка содержала несопоставимые величины.

E.10 предлагает не запрещать слово «состояние», а применять **триггер-скан**: если слово несёт claim — восстановить `Characteristic` и `Scale`; если нет — пометить как ordinary prose.

---

## 3. Unified Lexical Rules for FPF — полное описание

### 3.1 Определение

**Lexical Bundle / Unified Lexical Rules for FPF (E.10)** — это лексический триггер-скан и паттерн conformance, который определяет, когда слово в FPF-управляемом тексте скрывает свой kind, регистр, контекст смысла или отношение, и выбирает минимальный способ восстановления.

### 3.2 Почему это важно

Ремонт точности легко превращается в замену одного широкого слова другим: «поддержка» → «обеспечение», «объект» → «сущность», «нагрузка» → «воздействие». Если при этом не восстановлен FPF-род, смысл остаётся таким же расплывчатым. E.10 останавливает такой «синонимный театр» и требует восстановить kind, relation, admissible use и remaining reader use.

### 3.3 Триггер-скан: не каждое слово — проблема

**Определение.** `E.10` — это дешёвый триггер-скан перед более тяжёлым ремонтом. Если слово используется в обычной речи без FPF-управляемого claim, оно остаётся **ordinary prose**. Триггер срабатывает, когда слово может нести: ontic kind, relation, admissibility, evidence / assurance / gate / work / decision, characteristic / scale / quality, state-family, method / transformation / flow, architecture / stratification.

**Пояснение.** Цель — не переопределить каждый термин, а остановиться на тех случаях, где слово влияет на claim, admissibility или downstream use. Если слово не несёт FPF-управляемого смысла, локальный ремонт не нужен.

**Пример из животноводства.**

| Триггер-слово | Возможный FPF-род | Что восстановить |
|---|---|---|
| «стресс» | `Characteristic` | кортизол, поведение, температура, снижение удоя? |
| «рацион» | `U.Method` / `U.WorkPlan` | формула, ингредиенты, NRC/CNCPS-нормы? |
| «состояние» | `Characteristic` / state-family | BCS, клинический скоринг, PALM? |
| «баланс» | relation / `CharacteristicSpace` | энергетический баланс, минеральный баланс? |
| «достаточно» | admissibility / threshold | threshold по какой шкале? |
| «продуктивность» | `Characteristic` | удой, масса тела, плодовитость? |

**Ключевой признак.** После скана для каждого claim-bearing слова указан kind, relation или governing pattern; иначе слово помечено как ordinary prose или blocked use.

### 3.4 Восстановление kind и register

**Определение.** Если слово скрывает род, применяется **precision-restoration**: сначала восстановить, что именно именуется, и только потом — заменить или оставить.

**Пояснение.** Основные направления: relation-like wording → `A.6.P`; source-expression / publication wording → `C.2.P`; method / workflow wording → `A.3` family; transformation / flow wording → `A.3.4.P` или `E.18`; characteristic / scale wording → `C.16.P`; quality / evaluative wording → `C.16.Q`; state-family wording → `A.19.SPR`; architecture / stratification wording → `C.30.P` / `C.30.STRAT`; durable reusable head → `F.18`.

**Пример из животноводства.**

> Фраза: «Провести коррекцию рациона при низкой продуктивности.»
>
> Разбор:
> - «коррекция рациона» — method/work wording → восстановить `U.Method` или `U.WorkPlan` (`DietAdjustmentProtocol`).
> - «низкая продуктивность» — characteristic/quality wording → восстановить `Characteristic=MilkYield`, `Scale=ratio`, comparator set (`HerdBaseline_30d`), threshold.
> - «при» — relation / admissibility → восстановить `triggerCondition`.
>
> Исправленный вариант:
> `DietAdjustmentProtocol` активируется, если `MilkYield` отдельной коровы ниже 90 % от её 30-дневного базового уровня (`HerdBaseline_30d`) в течение 7 дней.

**Ключевой признак.** Замена слова не закрывает ремонт, пока не восстановлен kind и admissible use.

### 3.5 Fail-closed: если восстановить нельзя — не используй

**Определение.** Если смысл слова не удаётся восстановить, применяется **fail closed**: quote-only, reduced-use cue, blocked use или ordinary prose. Нельзя использовать слово в normative claim, если его FPF-род не восстановлен.

**Пояснение.** Это последняя линия защиты. Лучше явно заблокировать термин, чем позволить ему нести скрытый claim.

**Пример из животноводства.**

> «Корова в хорошей форме» — без восстановления `Characteristic` (BCS? мышечный тон? двигательная активность?) это blocked use в normative context. Можно оставить как ordinary prose в Plain-register описании, но не в Conformance Checklist или trigger condition.

**Ключевой признак.** В normative claim каждое слово либо имеет восстановленный kind, либо помечено как blocked/reduced use.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Обеспечить коровам комфортные условия содержания.»*

**Разложение по E.10:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «комфортные» | quality / evaluative wording | Нет `Scale`; разные люди понимают по-разному |
| «условия содержания» | architecture / stratification wording | Не ясно: микроклимат, площадь, социальная среда, гигиена? |
| «обеспечить» | method / work wording | Не ясно: кто, как, по какому протоколу? |

**Основные риски смешивания:**

1. **Несопоставимость данных.** Один и тот же термин записывается в разных шкалах.
2. **Произвол в compliance.** Проверяющий не может определить pass/fail.
3. **Потеря Bridge/CL.** При переносе протокола в другой контекст непонятно, какие потери смысла.
4. **Ошибки аналитики.** Модели интерпретируют overloaded term по-своему.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** описать условия содержания в normative document.

**Было (смешанное / нечёткое):**

> «Обеспечить коровам комфортные условия содержания.»

**Стало (разложенное / ясное):**

**Ordinary prose (Plain register):**

> Цель фермы — снижение теплового и социального стресса в группах содержания.

**FPF-governed claims:**

> `Characteristic_Housing_ThermalComfort`:
> - `EntityOfConcern`: `FarmA.LactatingCows`
> - `Scale`: interval (°C)
> - `Method`: `THI_Calculation_v2`
> - `Threshold`: `THI ≤ 72` (target), `THI > 78` (trigger for intervention)
> - `Role`: `HerdManagerRole`
> - `EvidenceRef`: `BarnClimateLog`
>
> `Characteristic_Housing_SpaceAllowance`:
> - `EntityOfConcern`: `FarmA.LactatingCows`
> - `Scale`: ratio (m²/голова)
> - `Method`: `BarnLayoutAudit_v1`
> - `Threshold`: `≥ 6 m²/head`
> - `Role`: `FacilityManagerRole`
> - `EvidenceRef`: `BarnAudit_2026`

**Результат:**

- Каждое слово «комфорт» разложено на проверяемые `Characteristic`.
- Разные роли отвечают за разные измерения.
- Evidence path понятен.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Возьмите существующий фермерский протокол и выделите термины, которые могут нести нормативную нагрузку: характеристики, отношения, допустимость, методы, преобразования.

**Шаг 2.** Для каждого термина задайте вопрос: «Что именно это именует в FPF-терминах?» Если ответа нет — термин либо ordinary prose, либо blocked use.

**Шаг 3.** Если термин relation-like — примените `A.6.P`. Если method-like — `A.3` family. Если characteristic/scale — `C.16.P`. Если quality/evaluative — `C.16.Q`. Если state-like — `A.19.SPR`.

**Шаг 4.** Заменяйте слово только после восстановления kind. Не принимайте «более плавный синоним» как доказательство ремонта.

**Шаг 5.** Если kind не восстанавливается — используйте quote-only, reduced-use cue или explicit blocker. Не несите слово в normative claim.

**Шаг 6.** Для часто используемых терминов создайте durable reusable names через `F.18` (например, `BCS_FarmA` как имя для `BodyConditionScore` с локальным comparator set).

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| В normative text есть слова вроде «комфортный», «хороший», «достаточный», «адекватный» без шкалы? | Quality/evaluative wording не восстановлено через `C.16.Q`. |
| Один термин используется для разных измерений в разных протоколах? | Overloaded term — нужна разметка kind/scale/role. |
| Слово заменено на синоним, но смысл не прояснился? | Ложный lexical repair; нужно восстановить kind. |
| Термин несёт claim, но его FPF-род не назван? | Blocked use до восстановления. |
| Встречаются «рацион», «стресс», «состояние», «продуктивность» как самоочевидные? | Нужен триггер-скан E.10. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.6.P Relation Precision Restoration | relation-like wording |
| A.6.F Function-like Wording | `function`, `effect`, `role` |
| A.3 / A.3.4 | method / transformation wording |
| A.19.SPR | state-family wording |
| C.2.P Source-Expression & Publication Precision | source/publication wording |
| C.16.P / C.16.Q | characteristic / scale / quality wording |
| C.30.P / C.30.STRAT | architecture / stratification wording |
| E.18 Transformation Flow Structure | flow / transformation wording |
| F.18 Naming Discipline | durable reusable heads |
| E.8 Pattern Authoring Discipline | шаблон, в котором lexical discipline применяется |

---

## 9. Что запомнить

1. E.10 — это триггер-скан, а не полный лексический аудит.
2. Не заменяй широкое слово другим широким словом — восстанови kind.
3. Ordinary prose не требует ремонта; claim-bearing wording требует.
4. Если kind не восстанавливается — fail closed.
5. Durable names создаются через F.18 только после восстановления kind.

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.10*
