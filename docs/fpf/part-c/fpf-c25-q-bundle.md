---
type: fpf-study
pattern: C.25
title: "Q-Bundle: распутывание сложных family labels на ферме"
domain: cattle-science
difficulty: intermediate
reading_time: 35 min
created: 2026-06-19
---

# C.25 — Q-Bundle

## 1. Зачем это читать

Если вы когда-нибудь видели, как на ферме говорят: **«Этот рацион хороший»** — без уточнения, что именно «хорошо» (цена, здоровье, удои, экология, приёмлемость коровами) — вы встретили C.25 «в диком виде».

> **FPF-тезис:** *«Когда качество называют одним словом, но под ним скрывается несколько разных измерений, это quality-family chimera. Q-Bundle разбивает такие метки на отдельные оси, каждая со своим типом, весом и политикой.»*

C.25 — Quality Bundle. Это паттерн для работы со сложными, многомерными метками качества, которые люди склонны использовать как единое слово («качественный», «эффективный», «устойчивый»).

**Фермерский пример:**

> «Силос хороший». Но что это значит? pH 4,0? NDF 45%? Запах? Консистенция? Привкус для коров? Энергетическая ценность? Каждый из этих аспектов — отдельная ось Q-Bundle. Смешивать их в одно слово — значит терять возможность измерять и управлять.

---

## 2. История одной ошибки

Представьте ферму, где оценивают **«качество переходного периода»**:

> «Качество переходного периода у нас 4 из 5.»

Через год приходит аудитор. Он спрашивает:

- «4 из 5 — по какой шкале?» — Ответ: «По нашей» (ordinal, не ratio).
- «Что входит в оценку?» — Ответ: «И BHB, и удои, и отёл» (mixed criteria).
- «Можно ли увеличить одну ось без другой?» — Ответ: «Не думали» (trade-off не исследован).
- «Какой критерий главный?» — Ответ: «Все важны» (нет policy).

Аудитор уходит ни с чем. Потому что «качество» — chimera. C.25 предлагает: разбить на bundle, измерить каждую ось, задать policy.

---

## 3. Q-Bundle — полное описание

### 3.1 Что такое quality-family chimera

**Chimera** — это лингвистическая метка, которая выглядит как одно качество, но на самом деле объединяет несколько измерений.

**На ферме:**
- «Хороший рацион» = {ценовая доступность, питательная ценность, приёмлемость коров, стабильность поставок, экологичность, простота приготовления}.
- «Здоровая корова» = {отсутствие клинических заболеваний, BHB в норме, BCS в целевом диапазоне, подвижность, репродуктивный статус}.
- «Надёжный ветеринар» = {квалификация, доступность, скорость реакции, цена, коммуникация}.

### 3.2 Структура Q-Bundle

**Q-Bundle = {axis_id, type, weight, target, measure, policy}**

**На ферме для «качества силоса»:**

| axis_id | type | measure | target | weight | policy |
|---|---|---|---|---|---|
| fermentation | ratio | pH | 3,8–4,2 | 0,30 | must |
| fiber | ratio | NDF, % | ≤ 45 | 0,25 | soft |
| palatability | ordinal | intake score 1–5 | ≥ 4 | 0,20 | tie-breaker |
| stability | ratio | temp rise, °C | ≤ 5 | 0,15 | soft |
| safety | boolean | mycotoxin pass | true | 0,10 | must |

**Ключевой признак:** Веса — policy-governed. Нельзя тихо агрегировать в scalar score без объявленной policy.

### 3.3 Types of axes

- **ratio** — можно сравнивать отношения (pH, NDF, BHB).
- **ordinal** — можно ранжировать, но не усреднять (score 1–5).
- **boolean** — pass/fail.
- **nominal** — категории без порядка (тип корма: силос, сено, жмых).

### 3.4 Aggregation rules

**По умолчанию:**
- Must-оси — gate: fail одной = fail всего bundle.
- Soft-оси — Pareto front.
- Tie-breaker — разрешает неоднозначность по policy.

**Запрещено:**
- Усреднять ordinal и ratio в одно число.
- Применять веса без явного policy id.
- Смешивать design-time и run-time оси.

### 3.5 Связь с TaskSignature

**На ферме:**
- ObjectiveProfile в TaskSignature может ссылаться на Q-Bundle.
- Пример: `ObjectiveProfile: maximize Q-Bundle-TransitionHealth with must = [BHB, DystociaRisk]`.
- Selector понимает, что «TransitionHealth» — это bundle, а не scalar.

---

## 4. Каскад типичных ошибок

Возьмём снова:

> *«Качество переходного периода у нас 4 из 5.»*

**Разложение по C.25:**

| Часть утверждения | Что это в FPF | Почему ошибка |
|---|---|---|
| «Качество переходного периода» | **Quality-family chimera** | Одна метка, несколько осей |
| «4 из 5» | **Ordinal scalar score** | Смешение осей, веса не объявлены |
| «По нашей шкале» | **Ad-hoc policy** | Нет версионирования, нет inter-subjectivity |
| «Все важны» | **Отсутствие dominance regime** | Нет must/soft/tie-breaker разделения |

**Что плохого в смешивании:**

1. **Невозможно улучшить целенаправленно.** «Поднять качество с 4 до 5» — не actionable.
2. **Невозможно сравнить фермы.** У каждой своя шкала.
3. **Скрытые trade-offs.** Улучшение BHB может ухудшить удои, но chimera это скроет.

---

## 5. Как это выглядит на ферме: правильное применение

Перепишем оценку переходного периода.

**Было (смешанное):**
> «Качество переходного периода у нас 4 из 5.»

**Стало (разложенное):**

**Q-Bundle-TransitionHealth_v1:**

| axis_id | type | measure | target | role |
|---|---|---|---|---|
| metabolic_stability | ratio | BHB max, ммоль/л | ≤ 0,8 | must |
| calving_ease | ratio | dystocia rate, % | ≤ 5 | must |
| early_lactation_yield | ratio | milk kg at 30 DIM | ≥ 28 | soft |
| body_condition | ratio | BCS at 7 DIM | 2,75–3,25 | soft |
| rumen_health | ordinal | rumination score 1–5 | ≥ 4 | tie-breaker |

**Результат для фермы А:**
> BHB = 0,7 (pass), dystocia = 4% (pass), yield = 26 кг (fail soft), BCS = 3,0 (pass), rumination = 4 (pass).

**Bundle-вердикт:**
> Must pass. Soft: yield below target → trade-off with BCS. Policy: accept because BCS on target and rumination good; flag yield for next review.

**Что это даёт:**
- Вместо «4 из 5» — явные оси и решения.
- Видно, что must выполнены, но yield — soft-fail.
- Есть explicit policy для trade-off.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Найдите chimera-слова в своих документах: «качество», «эффективность», «здоровье», «надёжность», «устойчивость».

**Шаг 2.** Для каждого слова выпишите 3–7 осей.

**Шаг 3.** Определите тип каждой оси (ratio/ordinal/boolean/nominal).

**Шаг 4.** Разделите роли: must / soft / tie-breaker.

**Шаг 5.** Задайте меры и целевые значения.

**Шаг 6.** Запишите policy id и версию. Никаких scalar scores без policy.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Есть ли оценки «качества» одним числом? | Quality-family chimera |
| Смешиваете ли ratio и ordinal в одном score? | Незаконная агрегация |
| Объявлены ли веса и policy? | Ad-hoc aggregation |
| Есть ли must-оси как gates? | Must не отделены от soft |
| Можно ли увидеть trade-offs между осями? | Скрытые компромиссы |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---------|-------|
| A.18 CSLC | CHR-типизация осей |
| C.16 Measurement | Measures[CHR] для каждой оси |
| C.17 Creativity | ValueGain по оси bundle |
| C.18 NQD | Archive по characteristic space bundle'а |
| C.22 Selection Kernel | ObjectiveProfile ссылается на Q-Bundle |
| G.5 Multi-Method Dispatcher | Selector понимает bundle-структуру |

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §C.25*
