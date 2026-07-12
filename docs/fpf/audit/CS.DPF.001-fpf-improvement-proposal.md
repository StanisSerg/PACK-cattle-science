---
type: fpf-audit
target: CS.DPF.001
title: Аудит и улучшение CNCPS-DPF через FPF
date: 2026-07-12
agent: Kimi
status: draft
---

# Аудит и улучшение CS.DPF.001 через FPF

> **Цель:** применить First Principles Framework (FPF) для усиления Domain Principle Framework (DPF) по применению модели CNCPS. Результат — не замена CS.DPF.001, а предложения по его доработке.
> **Метод:** карточка `DPF-AUTHORING` из `FPF/Readme.md` + ключевые принципы FPF.
> **Исходный файл:** `PACK-cattle-science/pack/cattle-science/08-dpf/CS.DPF.001-cncps-feeding-model-principles-framework.md`

---

## 1. Какую карточку FPF используем

Для улучшения DPF в целом наиболее подходит карточка **DPF-AUTHORING** (`E.4.DPF`, `E.4.PFAD`, `C.30.AD`). Она задаёт четыре шаблона:

| Шаблон | Вопрос | Что проверяем в CS.DPF.001 |
|---|---|---|
| **A. FrameworkOrganizationDesignProposal** | Как организован фреймворк, какие паттерны входят, как они связаны? | Есть ли явная архитектура паттернов DPF? |
| **B. PrincipleFrameworkArchitectureDecision (PFAD)** | Какие архитектурные решения приняты: bounded context, зависимость от FPF Core, edition? | Есть ли PFAD-запись? |
| **C. ArchitectureDescriptionUseCard** | Как используется описание архитектуры? | Понятна ли роль DPF для downstream-потребителей? |
| **D. FrameworkAuthoringDependencyDescription** | Какие зависимости нужны для следующего шага авторинга? | Что нужно для продолжения работы? |

Помимо этого, применяем универсальные принципы: **L/A/D/E** (`A.6.B`), **Role–Method–Work** (`A.15`), **Strict Distinction** (`A.7`), **Evidence Graph** (`A.10`), **F-G-R** (`B.3`), **MVPK** (`E.17`), **Bounded Contexts** (`A.1`), **Structural Information Adequacy** (`C.33`).

---

## 2. Проверка по шаблонам DPF-AUTHORING

### 2.1. FrameworkOrganizationDesignProposal

- **README card:** DPF-AUTHORING → Template A
- **PatternID:** `E.4.DPF`
- **Kind:** `FrameworkOrganizationDesignProposal@Context` — draft source-pack summary, candidate pattern list, relation-record candidates

**Что есть сейчас:**
CS.DPF.001 содержит 8 разделов (подготовка данных, Kd, MCP, MP, животные, калибровка, инструменты, новые корма) + acceptance cases. Это хороший практический скелет, но **архитектура паттернов не выведена явно**.

**Чего не хватает по FPF:**
- Нет явного списка **recurring problem situations** (повторяющихся ситуаций), для которых DPF даёт решение.
- Нет явного разделения **problem frame → solution → worked slice → anti-pattern** для каждого паттерна.
- Нет карты связей между разделами: например, раздел 1 (фракции) питает раздел 3 (MCP), раздел 5 (DMI) влияет на раздел 2 (Kd).

**Предложение:**
Добавить раздел **«Архитектура паттернов CNCPS-DPF»** с таблицей:

| Паттерн | Ситуация | Силы (forces) | Решение | Worked slice | Антипаттерн |
|---|---|---|---|---|---|
| P1. FeedFractionation | Есть лабораторный анализ, нужно перевести в фракции CNCPS | Неточность таблиц, партийность, базис | Разбить CHO/CP на фракции; указать originTag | Пример кукурузы/сои | Средний CP/NDT вместо фракций |
| P2. KdSelection | Нужно выбрать Kd для корма | pH, passage rate, обработка | Корректировать табличное Kd по условиям рубца | Пример кукурузы при pH 5,9 | Брать Kd из таблицы без корректировки |
| P3. MicrobialProteinBalance | Нужно сбалансировать RDP и энергию рубца | Избыток/дефицит RDP, MUN | Рассчитать MCP, оценить RDP vs FCHO | Пример соевого шрота | Ориентироваться только на CP |
| P4. MPandAminoAcids | Нужно проверить белок и аминокислоты | Lys/Met лимитируют | MP = MCP + RUP − потери; Lys/Met как % MP | Пример группы 40 кг | Смотреть только абсолютные граммы |
| P5. DMIEstimation | Нужен DMI для расчёта | Измерить vs прогноз | Использовать факт; если прогноз — указать уравнение | Пример группы 14–60 DIM | «Средняя корова» |
| P6. ModelCalibration | Прогноз не совпадает с фактом | Ошибка во входных данных, Kd, DMI | 6 шагов калибровки | Пример Farm B | Обвинять модель |
| P7. ToolVersioning | Используется программа | Разные версии, библиотеки | Фиксировать версию, parallel run | Пример миграции | Сравнивать результаты разных программ напрямую |
| P8. NewFeedAdmission | Новый корм не в библиотеке | Аналогии ненадёжны | Анализ + originTag + валидация 14–21 день | Пример подсолнечного жмыха | «Это как соевый шрот» |

### 2.2. PrincipleFrameworkArchitectureDecision (PFAD)

- **README card:** DPF-AUTHORING → Template B
- **PatternID:** `E.4.PFAD`
- **Kind:** `PrincipleFrameworkArchitectureDecision@Context`

**Что есть сейчас:**
- В `Integration Gate Record` указаны роли, implementation, service clause.
- В `Relation Records` перечислены связи с FPF Core и доменными сущностями.
- В `Refresh Route` — триггеры обновления.

**Чего не хватает по FPF:**
- Нет явной **PFAD-записи** как отдельного артефакта.
- Не зафиксированы ключевые архитектурные решения:
  - Почему DPF использует именно эти 8 паттернов, а не 12 или 5?
  - Почему граница DPF заканчивается на «добавлении нового корма», а не уходит в экономику фермы?
  - Почему выбрана именно такая последовательность разделов?
  - Какая версия FPF Core принята за основу?
  - Какие rival traditions учтены (CNCPS v5/v6/v7, NRC 2001, NASEM 2021)?

**Предложение:**
Добавить раздел **«PFAD: Архитектурные решения CNCPS-DPF»** с полями:

```markdown
## PFAD: CNCPS-DPF Architecture Decision

- **frameworkDecisionId:** PFAD-CS.DPF.001-2026-07-12
- **governedFrameworkRef:** CS.DPF.001
- **boundedContextRef:** cattle-science / feeding / ration-formulation
- **frameworkEditionRef:** CNCPSFeedingModelPrinciplesFramework@2026-07-03
- **fpfCoreEditionRef:** FPF Core July 2026
- **decisionQuestion:** Какая минимальная структура паттернов нужна практику для применения CNCPS в условиях неполных данных?
- **sourceBasisRefs:** Fox et al. 2004, Van Amburgh et al. 2015, NRC 2001
- **sotaSynthesisPackRefs:** CS.SOTA.012, CS.SOTA.015, CS.SOTA.018, CS.SOTA.029, CS.SOTA.048, CS.SOTA.054, CS.SOTA.056, CS.SOTA.066

### Key decisions
1. DPF ограничивается рационированием молочного скота; лечебная ветеринария и экономика вынесены за границу.
2. Восемь паттернов покрывают полный цикл: входные данные → фракции → Kd → MCP → MP → DMI → калибровка → инструменты → новые корма.
3. Каждый паттерн даёт worked slice и антипаттерн, чтобы практик мог проверить себя.
4. Acceptance cases используются как downstream-проверка применимости, а не как полный набор тестов.
5. DPF зависит от FPF Core, SPF (общие понятия кормления) и SoTA-cattle-science; не переопределяет научные уравнения CNCPS.
```

### 2.3. ArchitectureDescriptionUseCard

- **README card:** DPF-AUTHORING → Template C
- **PatternID:** `C.30.AD`
- **Kind:** `ArchitectureDescriptionUseCard@Project`

**Что есть сейчас:**
- Файл описывает DPF для практика-рациональщика, технолога, преподавателя.
- Integration Gate Record упоминает downstream-потребителя DS-cattle-course.

**Чего не хватает по FPF:**
- Нет явного описания **admissible use boundary**: что можно делать с DPF, а что нельзя.
- Нет разных **views** для разных читателей (MVPK).

**Предложение:**
Добавить карточку использования:

```markdown
## Architecture Description Use Card

| Роль | Что читает | Что делает с DPF | Ограничение |
|---|---|---|---|
| Практик-рациональщик | Разделы 1–9, acceptance cases | Составляет и калибрует рацион | Не заменяет ветеринарную диагностику |
| Технолог фермы | Быстрый старт, чек-листы | Контролирует входные данные и DMI | Не модифицирует уравнения модели |
| Преподаватель DS-cattle-course | Структура паттернов, кейсы | Готовит занятия | Учебные материалы хранит отдельно |
| Разработчик ПО | Relation Records, Integration Gate | Интегрирует DPF в инструмент | Должен фиксировать версию и parallel run |
| Аудитор / верификатор | PFAD, acceptance cases, refresh route | Проверяет качество и актуальность | Не делает рационных рекомендаций |
```

### 2.4. FrameworkAuthoringDependencyDescription

- **README card:** DPF-AUTHORING → Template D
- **PatternID:** `E.4.DPF`
- **Kind:** `FrameworkAuthoringDependencyDescription@Context`

**Что есть сейчас:**
- Change Log показывает две версии.
- Refresh Route описывает, что обновлять.

**Чего не хватает по FPF:**
- Нет явного списка **зависимостей**, которые нужны для следующего шага авторинга.

**Предложение:**
Добавить раздел **«Зависимости для следующего шага авторинга»**:

```markdown
## Framework Authoring Dependencies

| Зависимость | Статус | Что нужно для продолжения |
|---|---|---|
| FPF Core edition | Доступен (July 2026) | Отслеживать изменения Core |
| SPF feeding notions | Частично | Уточнить связи с `SPF/docs/` |
| SoTA records (CS.SOTA.*) | Доступны | Обновлять при появлении новых исследований |
| Domain entities (CS.ENTITY.*) | Доступны | Проверить, что все related_entities актуальны |
| Acceptance cases telemetry | Нет | Собрать пилотную обратную связь с ферм |
| Tool comparison data | Нет | Провести parallel run между AMTS / CPM Dairy / Spartan |
| Glossary / UTS | Нет | Создать Unified Term Sheet для PACK-cattle-science |
```

---

## 3. Проверка по ключевым принципам FPF

Формат каждого пункта: **README-карточка → PatternID → Kind результата → находка и предложение.**

### 3.1. L/A/D/E routing

- **README card:** WORKING-DOCUMENTS → Branch A
- **PatternID:** `A.6.B` Boundary Norm Square
- **Kind:** Claim Register (L/A/D/E classification)
- **Находка:** В тексте смешаны четыре вида утверждений без явной маркировки.

**Проблема:** В тексте смешаны четыре вида утверждений без явной маркировки.

**Примеры:**
- **L (Law/Definition):** «CNCPS разбивает углеводы и белки на фракции по скорости деградации».
- **D (Deontic/Commitment):** «Для каждого корма в расчёте должно быть ясно, какой источник используется».
- **A (Admissibility/Gate):** «Если лаборатория не выдаёт готовые фракции, можно рассчитать их по минимальному набору».
- **E (Evidence/Effect):** «MCP (г/день) ∝ [FCHO × Kd_CHO + FPROT × Kd_PROT] × эффективность».

**Улучшение:**
Добавить в каждый раздел подзаголовки L / A / D / E или пометить утверждения тегами inline:

```markdown
### 1.1 Подготовка данных (L/A/D/E)

**L:** Фракции CHO: CA, CB1, CB2, CC. Фракции CP: PA, PB1, PB2, PB3, PC.
**A:** Если нет лабораторного анализа — допускаются табличные или оценочные значения с originTag.
**D:** Каждый корм в расчёте MUST иметь указанный источник данных.
**E:** Практический вывод: два корма с одинаковым CP могут давать разный MCP и RUP.
```

### 3.2. Role–Method–Work Alignment

- **README card:** WORKING-DOCUMENTS → Branch B / SYSTEM-IN-CONTEXT
- **PatternID:** `A.15` Role–Method–Work Alignment
- **Kind:** `U.MethodDescription`, `U.WorkPlan`, `U.Work`
- **Находка:** Роли, методы и работа не разделены явно.

**Проблема:** Роли, методы и работа не разделены явно.

**Улучшение:**
Добавить раздел **«Роли, методы и работа в CNCPS-DPF»**:

```markdown
| Уровень | Сущность в DPF | Пример |
|---|---|---|
| Role | Практик-рациональщик, технолог, преподаватель | «Рациональщик» |
| MethodDescription | CS.DPF.001 как метод | Этот документ |
| Capability | Умение размечать корма, выбирать Kd | Подтверждается acceptance cases |
| WorkPlan | WeekPlan / рационная задача фермы | «Составить рацион для группы A» |
| Work | Конкретный рацион + записи калибровки | `ration-farm-a-2026-07-12.md` |
```

### 3.3. Strict Distinction

- **README card:** SYSTEM-IN-CONTEXT
- **PatternID:** `A.7` Strict Distinction
- **Kind:** Object/Description/Carrier separation
- **Находка:** Несколько разных вещей могут быть спутаны.

**Проблема:** Несколько разных вещей могут быть спутаны.

**Улучшение:**
Добавить явные различения:
- **Модель ≠ Программа:** CNCPS v6.5 ≠ AMTS 4.7.
- **Рацион ≠ Рационный кейс:** конкретный рацион фермы ≠ шаблон в DPF.
- **Прогноз ≠ Факт:** прогноз MP ≠ измеренный белок молока.
- **DPF ≠ Учебник:** DPF — метод, учебные материалы DS-cattle-course — carrier.

### 3.4. Evidence Graph

- **README card:** WORKING-DOCUMENTS → Branch C / COSTLY-ACTION
- **PatternID:** `A.10` Evidence Graph Referring
- **Kind:** claim-bound evidence-provenance graph relation, `PathId`
- **Находка:** Многие claims не имеют явных evidence-ссылок.

**Проблема:** Многие claims не имеют явных evidence-ссылок.

**Примеры claims без evidence:**
- «Ошибка в DMI на 5 % может привести к ошибке в прогнозе энергии и протеина на такую же величину».
- «Лизин — первый лимитирующий аминокислотный фактор».

**Улучшение:**
Добавить **PathId** / evidence-ссылки. Например:

```markdown
**Claim:** Ошибка в DMI на 5 % приводит к ошибке в прогнозе энергии и протеина ~5 %.
**Evidence:** Van Amburgh et al. 2015, sensitivity analysis; CS.SOTA.015.
**PathId:** `CS.DPF.001/5.1/DMI-sensitivity`
```

### 3.5. F-G-R Trust & Assurance

- **README card:** WORKING-DOCUMENTS → Branch C / COSTLY-ACTION
- **PatternID:** `B.3` Trust & Assurance F-G-R
- **Kind:** `Assurance(H, C | K, S)` disposition
- **Находка:** Утверждения не имеют явной оценки Formality / ClaimScope / Reliability.

**Проблема:** Утверждения не имеют явной оценки Formality / ClaimScope / Reliability.

**Улучшение:**
Добавить таблицу F-G-R для ключевых claims:

```markdown
| Claim | Formality (F) | ClaimScope (G) | Reliability (R) |
|---|---|---|---|
| Фракции CHO/CP структурируют корм | F=7 (consensus model) | Молочное ското, рационирование | High (CNCPS v6.5, multiple validations) |
| Kd CB1 кукурузы = 55 %/ч | F=5 (literature value) | Дроблёная кукуруза, типичные условия | Medium (depends on pH, passage rate) |
| Lys:Met 2,8–3,1 оптимален | F=6 (meta-analysis) | Высокоудойные коровы, типичные рационы | Medium-High |
| DMI error → energy error ~same % | F=4 (model sensitivity) | CNCPS v6.5, группы 600+ кг | Medium |
```

### 3.6. MVPK — Multi-View Publication Kernel

- **README card:** WORKING-DOCUMENTS → Branch D / DESCRIPTION-USE
- **PatternID:** `E.17` Multi-View Publication Kernel
- **Kind:** source-pinned publication face (PlainView / TechCard / InteropCard / AssuranceLane)
- **Находка:** DPF сейчас имеет только один view — практико-технологический.

**Проблема:** DPF сейчас имеет только один view — практико-технологический.

**Улучшение:**
Добавить 4 view:

```markdown
## MVPK Views for CNCPS-DPF

| View | Аудитория | Формат | Что включает |
|---|---|---|---|
| **PlainView** | Владелец фермы / менеджер | 1 страница | Зачем CNCPS, 6 шагов, риски, ROI |
| **TechCard** | Рациональщик / технолог | Полный DPF с примерами | Все 8 разделов, таблицы, чек-листы |
| **InteropCard** | Разработчик ПО | JSON/YAML + relation records | Структура паттернов, сущности, API-мэппинг |
| **AssuranceLane** | Аудитор / верификатор | PFAD + F-G-R + evidence refs | Архитектурные решения, версии, acceptance cases |
```

### 3.7. Bounded Contexts

- **README card:** SYSTEM-IN-CONTEXT / DESCRIPTION-USE
- **PatternID:** `A.1` Bounded Contexts + `A.6.3.CSC` selected source structure
- **Kind:** `HolonDelimitationRelation@Context`, Glossary, Invariants, Bridges
- **Находка:** Нет явного bounded context с glossary и invariants.

**Проблема:** Нет явного bounded context с glossary и invariants.

**Улучшение:**
Добавить раздел **«Bounded Context: CNCPS Ration Formulation»**:

```markdown
### Glossary

| Термин | Plain name | Техническое определение | Контекст |
|---|---|---|---|
| CP | Сырой протеин | Crude protein, % DM | Химический анализ |
| MP | Метаболизируемый протеин | Протеин, доступный животному для метаболизма | Физиология / рационирование |
| MCP | Микробный протеин | Протеин, синтезированный в рубце | Рубец |
| RUP | Недеградируемый протеин | Протеин, прошедший в кишечник | Рубец → кишечник |
| Kd | Скорость деградации | Fractional degradation rate, %/ч | Рубец |
| DMI | Съём сухого вещества | kg DM / day | Потребление |

### Invariants
- Сумма фракций CHO = 100 % CHO (в рамках допустимой погрешности).
- Сумма фракций CP = 100 % CP.
- MP = MCP + RUP − endogenous losses.
- Каждый входной параметр имеет originTag.

### Bridges
- `CP (химия)` → `RDP + RUP (рубец)` → `MP (физиология)`.
- `DMI (потребление)` → `passage rate (рубец)` → `effective Kd (рубец)`.
```

### 3.8. Structural Information Adequacy

- **README card:** ARCHITECTURE / DESCRIPTION-USE
- **PatternID:** `C.33` Structural Information Adequacy for Architecture Capture and Source Return
- **Kind:** `StructuralInformationAdequacyNote@Context`
- **Находка:** Не указано, какая структура сохраняется в каждом view, а что теряется.

**Проблема:** Не указано, какая структура сохраняется в каждом view, а что теряется.

**Улучшение:**
Добавить в каждый раздел примечание:

```markdown
> **C.33 Note:** В этом разделе сохраняется структура фракционного состава корма и источник данных. Стертая структура — индивидуальная вариация партии, погрешность лаборатории, сезонные изменения. Вернуться к исходному анализу при возникновении отклонений.
```

---

## 4. Конкретные предложения по улучшению

### 4.1. Добавить PFAD-запись
Создать отдельный раздел или файл `CS.DPF.001-PFAD.md` с архитектурными решениями.

### 4.2. Ввести L/A/D/E теги
Пометить все утверждения в разделах 1–8 как L, A, D или E. Это улучшит reviewability и упростит аудит.

### 4.3. Создать UTS (Unified Term Sheet)
Отдельный файл `CS.UTS.001-cncps-glossary.md` с терминами, plain/tech names, sense cells для разных контекстов.

### 4.4. Добавить evidence refs и PathId
Каждое числовое утверждение должно иметь ссылку на источник и уникальный PathId.

### 4.5. Добавить F-G-R таблицу
Для 10–15 ключевых claims добавить Formality / ClaimScope / Reliability.

### 4.6. Реализовать MVPK
Создать 4 view-файла:
- `CS.DPF.001-PlainView.md`
- `CS.DPF.001-TechCard.md` (основной файл)
- `CS.DPF.001-InteropCard.md`
- `CS.DPF.001-AssuranceLane.md`

### 4.7. Добавить Role–Method–Work раздел
Явно разделить роли, метод, capability, work plan и work.

### 4.8. Улучшить acceptance cases
Добавить входные данные, ожидаемые результаты и failure criteria для каждого acceptance case.

### 4.9. Добавить anti-patterns
К каждому из 8 паттернов добавить явный anti-pattern и почему он вреден.

### 4.10. Связать с SoTA
Добавить в каждый раздел ссылки на конкретные `CS.SOTA.*` записи.

---

## 5. Предлагаемая структура дополнений к CS.DPF.001

```
CS.DPF.001-cncps-feeding-model-principles-framework.md
├── Frontmatter (как сейчас)
├── Введение
├── Быстрый старт (как сейчас)
├── Архитектура паттернов (NEW)
│   ├── Таблица 8 паттернов
│   └── Карта связей между паттернами
├── PFAD (NEW)
├── Bounded Context + Glossary (NEW)
├── Разделы 1–8 (улучшенные L/A/D/E + evidence + anti-patterns)
├── Роли, методы и работа (NEW)
├── MVPK Views (NEW)
├── Acceptance Cases (улучшенные)
├── Relation Records (как сейчас + F-G-R)
├── Refresh Route (как сейчас)
├── Sources (как сейчас)
├── Integration Gate Record (улучшенное)
└── Change Log
```

---

## 6. Приоритеты и следующие шаги

### Быстрые победы (1–2 часа)
1. Добавить PFAD-раздел.
2. Пометить 1–2 раздела тегами L/A/D/E.
3. Добавить таблицу Role–Method–Work.

### Среднесрочные (4–8 часов)
4. Создать UTS для терминов CNCPS.
5. Добавить F-G-R таблицу для ключевых claims.
6. Расширить acceptance cases входными данными и failure criteria.

### Долгосрочные (12–20 часов)
7. Реализовать MVPK: 4 view-файла.
8. Добавить evidence refs и PathId для всех числовых утверждений.
9. Собрать пилотную обратную связь с ферм и обновить acceptance cases.

---

## 7. Связь с WP-94

Этот аудит — практическое применение WP-94 («Изучение FPF — разбор возможностей принципов»). Захваченные принципы:
- **DPF-AUTHORING** (`E.4.DPF`, `E.4.PFAD`, `C.30.AD`)
- **L/A/D/E routing** (`A.6.B`)
- **Role–Method–Work** (`A.15`)
- **Strict Distinction** (`A.7`)
- **Evidence Graph** (`A.10`)
- **F-G-R** (`B.3`)
- **MVPK** (`E.17`)
- **Bounded Contexts** (`A.1`)
- **Structural Information Adequacy** (`C.33`)

---

*Создано: 2026-07-12 в рамках WP-94. Статус: draft, требует ревью пилота.*
