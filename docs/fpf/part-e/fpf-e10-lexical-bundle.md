---
type: fpf-study
pattern: E.10
title: "LEX-BUNDLE: восстанавливай смысл слов, прежде чем их использовать"
domain: cattle-science
difficulty: advanced
reading_time: 50 min
created: 2026-06-19
---

# E.10 — Lexical Bundle (LEX-BUNDLE): восстанавливай смысл слов, прежде чем их использовать

## 1. Зачем это читать

Если на вашей ферме один и тот же термин означает разное в разных протоколах — «рацион» у зоотехника, «рацион» у ветеринара и «рацион» в учёте затрат — вы сталкиваетесь с лексической проблемой. Этот паттерн учит **не заменять расплывчатые слова синонимами, а восстанавливать их FPF-род: сущность, отношение, шкалу, метод или роль**.

**FPF-тезис:** *«Лексический ремонт — не замена одного слова другим. Это восстановление вида (kind), регистра и допустимого использования.»*

В животноводстве многие слова несут нагрузку одновременно: «здоровье», «продуктивность», «стресс», «баланс». E.10 предлагает дешёвый триггер-скан: если слово может нести FPF-управляемый смысл — сначала восстановить, что именно оно именует, а только потом использовать в claim'е.

**Фермерский пример:**

> В одном протоколе написано: «При стрессе увеличить витамин С». В другом: «Стресс при транспортировке снижает продуктивность». В третьем: «Социальный стресс в группе тёлок требует перегруппировки». Если не восстановить, что такое «стресс» в каждом случае, получится одно слово для трёх разных `Characteristic`: кортизол, снижение удоя, агрессивное поведение.

E.10 требует: для каждого такого слова указать `EntityOfConcern`, `Characteristic`, `Scale`, `Method` и `EvidenceRef` — и только тогда использовать в normative claim.

## 2. История одной ошибки

Ферма внедряла протокол оценки «состояния коровы». В документе использовались слова:

- «состояние тела» — кто-то понял как BCS (Body Condition Score),
- «состояние здоровья» — кто-то понял как клинический скоринг,
- «состояние вымени» — кто-то понял как PALM-оценку.

В результате:

- Зоотехник вносил в `HerdLog` BCS под заголовком «Состояние».
- Ветеринар вносил клинический скоринг под тот же заголовком.
- Аналитика стала бесполезной: одна колонка содержала несопоставимые величины.

E.10 предлагает не запрещать слово «состояние», а применять **триггер-скан**: если слово несёт claim — восстановить `Characteristic` и `Scale`; если нет — пометить как ordinary prose.

## 3. Unified Lexical Rules for FPF — полное описание

> **Соответствие с FPF-Spec.** В реестре паттерн назван *Lexical Bundle (LEX-BUNDLE)*. В спецификации FPF он развивается как *Unified Lexical Rules for FPF* — см. §E.10. Capture сфокусирован на триггер-скане, восстановлении kind/регистра и fail-closed поведении.

### 3.1 Триггер-скан: не каждое слово — проблема

**Вопрос:** Нужно ли переопределять каждый термин?

**Ответ:** Нет. `E.10` — это **дешёвый триггер-скан** перед более тяжёлым ремонтом. Если слово используется в обычной речи, без FPF-управляемого claim — оставьте ordinary prose. Триггер срабатывает, когда слово может нести:
- ontic kind (какой объект именуется),
- relation (какое отношение),
- admissibility (допустимость),
- evidence / assurance / gate / work / decision,
- characteristic / scale / quality,
- state-family,
- method / transformation / flow,
- architecture / stratification.

**На ферме:**
| Триггер-слово | Возможный FPF-род | Что восстановить |
|---|---|---|
| «стресс» | `Characteristic` | кортизол, поведение, температура, снижение удоя? |
| «рацион» | `U.Method` / `U.WorkPlan` | формула, ингредиенты, NRC/CNCPS-нормы? |
| «состояние» | `Characteristic` / state-family | BCS, клинический скоринг, PALM? |
| «баланс» | relation / `CharacteristicSpace` | энергетический баланс, минеральный баланс? |
| «достаточно» | admissibility / threshold | threshold по какой шкале? |
| «продуктивность» | `Characteristic` | удой, масса тела, плодовитость? |

**Ключевой признак:** после скана для каждого claim-bearing слова указан `kind`, `relation` или `governing pattern`.

### 3.2 Восстановление kind и register

**Вопрос:** Что делать, если слово скрывает род?

**Ответ:** Применить **precision-restoration**: сначала восстановить, что именно именуется, и только потом — заменить или оставить. Основные направления:
- relation-like wording → `A.6.P`;
- source-expression / publication wording → `C.2.P`;
- method / workflow wording → `A.3` family;
- transformation / flow wording → `A.3.4.P` or `E.18`;
- characteristic / scale wording → `C.16.P`;
- quality / evaluative wording → `C.16.Q`;
- state-family wording → `A.19.SPR`;
- architecture / stratification wording → `C.30.P` / `C.30.STRAT`;
- durable reusable head → `F.18`.

**На ферме:**
> Фраза: «Провести коррекцию рациона при низкой продуктивности.»
> 
> Разбор:
> - «коррекция рациона» — method/work wording → восстановить `U.Method` или `U.WorkPlan` (`DietAdjustmentProtocol`).
> - «низкая продуктивность» — characteristic/quality wording → восстановить `Characteristic=MilkYield`, `Scale=ratio`, comparator set (`HerdBaseline_30d`), threshold.
> - «при» — relation / admissibility → восстановить `triggerCondition`.

Исправленный вариант:
> `DietAdjustmentProtocol` активируется, если `MilkYield` отдельной коровы ниже 90% от её 30-дневного базового уровня (`HerdBaseline_30d`) в течение 7 дней.

**Ключевой признак:** замена слова не закрывает ремонт, пока не восстановлен kind и admissible use.

### 3.3 Fail-closed: если восстановить нельзя — не используй

**Вопрос:** Что делать, если смысл слова не удаётся восстановить?

**Ответ:** **Fail closed**: quote-only, reduced-use cue, blocked use или ordinary prose. Нельзя использовать слово в normative claim, если его FPF-род не восстановлен.

**На ферме:**
> «Корова в хорошей форме» — без восстановления `Characteristic` (BCS? мышечный тон? двигательная активность?) это blocked use в normative context. Можно оставить как ordinary prose в Plain-register описании, но не в CC или trigger condition.

**Ключевой признак:** в normative claim каждое слово либо имеет восстановленный kind, либо помечено как blocked/reduced use.

## 4. Почему смешивать / игнорировать — значит рисковать

Возьмём фразу: *«Обеспечить коровам комфортные условия содержания.»*

**Разложение по E.10:**

| Триггер-слово | Что скрывает | Риск |
|---|---|---|
| «комфортные» | quality/ evaluative wording | Нет `Scale`; разные люди понимают по-разному |
| «условия содержания» | architecture / stratification wording | Не ясно: микроклимат, площадь, социальная среда, гигиена? |
| «обеспечить» | method / work wording | Не ясно: кто, как, по какому протоколу? |

**Что плохого в смешивании:**

1. **Несопоставимость данных.** Один и тот же термин записывается в разных шкалах.
2. **Произвол в compliance.** Проверяющий не может определить pass/fail.
3. **Потеря Bridge/CL.** При переносе протокола в другой контекст непонятно, какие потери смысла.
4. **Ошибки ИИ/аналитики.** Модели интерпретируют overloaded term по-своему.

## 5. Как это выглядит на ферме: правильное применение

**Задача:** описать условия содержания в normative document.

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

**Что это даёт:**
- Каждое слово «комфорт» разложено на проверяемые `Characteristic`.
- Разные роли отвечают за разные измерения.
- Evidence path понятен.

## 6. Практическое применение: с чего начать

**Шаг 1.** Возьмите существующий фермерский протокол и выделите термины, которые могут нести нормативную нагрузку: характеристики, отношения, допустимость, методы, преобразования.

**Шаг 2.** Для каждого термина задайте вопрос: «Что именно это именует в FPF-терминах?» Если ответа нет — термин либо ordinary prose, либо blocked use.

**Шаг 3.** Если термин relation-like — примените `A.6.P`. Если method-like — `A.3` family. Если characteristic/scale — `C.16.P`. Если quality/evaluative — `C.16.Q`. Если state-like — `A.19.SPR`.

**Шаг 4.** Заменяйте слово только после восстановления kind. Не принимайте «более плавный синоним» как доказательство ремонта.

**Шаг 5.** Если kind не восстанавливается — используйте quote-only, reduced-use cue или explicit blocker. Не несите слово в normative claim.

**Шаг 6.** Для часто используемых терминов создайте durable reusable names через `F.18` (например, `BCS_FarmA` как имя для `BodyConditionScore` с локальным comparator set).

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| В normative text есть слова вроде «комфортный», «хороший», «достаточный», «адекватный» без шкалы? | Quality/evaluative wording не восстановлено через `C.16.Q`. |
| Один термин используется для разных измерений в разных протоколах? | Overloaded term — нужна разметка kind/scale/role. |
| Слово заменено на синоним, но смысл не прояснился? | Ложный lexical repair; нужно восстановить kind. |
| Термин несёт claim, но его FPF-род не назван? | Blocked use до восстановления. |
| Встречаются «рацион», «стресс», «состояние», «продуктивность» как самоочевидные? | Нужен триггер-скан E.10. |

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.6.P Relation Precision Restoration | relation-like wording. |
| A.6.F Function-like Wording | `function`, `effect`, `role`. |
| A.3 / A.3.4 | method / transformation wording. |
| A.19.SPR | state-family wording. |
| C.2.P Source-Expression & Publication Precision | source/publication wording. |
| C.16.P / C.16.Q | characteristic / scale / quality wording. |
| C.30.P / C.30.STRAT | architecture / stratification wording. |
| E.18 Transformation Flow Structure | flow / transformation wording. |
| F.18 Naming Discipline | durable reusable heads. |
| E.8 Pattern Authoring Discipline | шаблон, в котором lexical discipline применяется. |

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.10*
