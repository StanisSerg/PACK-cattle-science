---
type: fpf-study
pattern: A.15.2
title: "U.WorkPlan: намерение, а не факт"
domain: cattle-science
difficulty: intermediate
reading_time: 20 min
created: 2026-06-19
---

# A.15.2 — U.WorkPlan: намерение, а не факт

## 1. Зачем это читать
«Обработать коров в понедельник» — это ещё не «обработали». `U.WorkPlan` — первый-class episteme для intended work. Без него невозможно отслеживать отклонения: schedule variance, cost variance, scope variance.

**FPF-тезис:** *«Plan = when, by whom in intent, under which constraints. Work = how it went this time.»*

## 2. История одной ошибки
Фермер планировал сухостойный период по протоколу, но фактические значения записывал в ту же строку таблицы, перезаписывая план. Когда удой после отёла оказался ниже ожидаемого, никто не мог сказать, в чём отклонение: план был завышен, факт недобран или метод применён не по плану.

## 3. U.WorkPlan: намерение, а не факт — полное описание

### 3.1 Что такое U.WorkPlan
`U.WorkPlan` — это `U.Episteme`, который декларирует intended `U.Work` occurrences:

- horizon и cadence;
- planned windows;
- dependencies;
- intended performers как role kinds или proposed `U.RoleAssignment`;
- resource budgets/reservations;
- acceptance targets;
- baseline для variance.

### 3.2 PlanItem
Каждый элемент плана содержит:

1. Target Method + MethodDescription
2. Planned window
3. Role requirements (kinds, не люди)
4. Capability thresholds
5. Resource budgets и reservations
6. Dependencies
7. Acceptance targets
8. Location/asset constraints

**Важно:** в WorkPlan **нет** logs, actuals, concrete launch values.

### 3.3 Различия
| Если вы говорите… | Это | Почему |
|---|---|---|
| «Расписание операций на завтра» | **WorkPlan** | Календарь intended runs |
| «Workflow доения» | **MethodDescription + Method** | Рецепт, не календарь |
| «Процесс уже выполнился в 10:00» | **Work** | Dated occurrence |
| «План назначает Марию» | **WorkPlan** с intended RoleAssignment | Assignment проверяется на момент Work |
| «Бюджет смены B» | **WorkPlan** (planned ledger) | Actuals — в Work |

### 3.4 Fulfilment и Variance
Когда Work произошло:

- **fulfil** — `plannedAs → PlanItem`;
- **partially fulfil** — несколько Work на один PlanItem или наоборот;
- **deviate** — другой метод, окно, performer, параметр;
- **unplanned** — emergency Work, должен быть явно помечен.

**Виды variance:**

| Variance | Что сравниваем |
|---|---|
| Schedule (Δt) | planned vs actual window |
| Cost (Δc) | budget vs actual resources |
| Scope | planned vs actual Method/MethodDescription |
| Quality | acceptance verdict vs target |
| Assignment | intended vs actual RoleAssignment |

### 3.5 Фермерский пример: план обработки
```text
WorkPlan: FarmA_TreatmentPlan_Week25
  PlanItem TI-001:
    targetMethod: AdministerPropyleneGlycol
    methodDescriptionRef: SOP_Ketosis_Treatment_v2
    plannedWindow: 2026-06-23T08:00..10:00
    roleRequirements: VeterinarianRole
    resourceBudget: propyleneGlycol 20L, syringes 20
    dependencies: BHB screening completed
    acceptanceTarget: BHB < 1.2 mmol/L within 12h
```

После выполнения:

```text
Work W-2026-0623-011 plannedAs TI-001
  variance: schedule +15 min, resources -1 syringe
```

## 4. Почему смешивать / игнорировать — значит рисковать
Если пренебречь A.15.2, типичные риски на ферме:

| Что происходит | Почему это опасно |
|---|---|
| Решения принимаются на основе смешанных или устаревших данных | Невозможно отследить, что именно повлияло на результат |
| Роли и методы не разделены | Один и тот же человек или документ отвечает за несовместимые обязательства |
| Перенос знаний между контекстами без явного bridge | Рекомендации из одной традиции применяют к другой без учёта потерь |
| Отсутствие контрольного списка | Ошибки обнаруживаются слишком поздно, когда они уже стоят денег |

**Каскад:** нечёткое утверждение → неправильная интерпретация → некорректное решение → экономический убыток и снижение доверия к системе.

## 5. Как это выглядит на ферме: правильное применение
**Задача:** разделить WorkPlan и WorkExecution для кормления сухостойных коров.

**Было:**
> «Сухостой: сено 5 кг, концентрат 1 кг.» — одна строка для плана и факта.

**Стало:**
> WorkPlan ID: `WP-0619-DryGroup`
> Planned inputs: сено 5.0 кг, концентрат 1.0 кг, минералы 150 г
> Planned role: `FeederRole:DryCows`
> Planned method: `DryCowDiet_v4`
>
> WorkExecution ID: `WE-0620-DryGroup`
> Actual inputs: сено 4.8 кг, концентрат 1.2 кг
> Variance: -0.2 кг сена, +0.2 кг концентрата
> Fulfilment status: partial

Разделение позволяет анализировать отклонения, а не просто констатировать факт.

## 6. Практическое применение: с чего начать
**Шаг 1.** Найдите таблицы, где план и факт хранятся в одной ячейке.

**Шаг 2.** Создайте отдельные сущности WorkPlan и WorkExecution с одинаковой структурой полей.

**Шаг 3.** Добавьте поля variance и fulfilment status.

**Шаг 4.** Запретите редактировать WorkPlan после начала исполнения.

**Шаг 5.** Еженедельно анализируйте variance по ролям и методам.

## 7. Проверь себя
| Вопрос | Если ответ «да» — проблема |
|---|---|
| `CC-A.15.2.1`: WorkPlan именует intended Work, не performed work. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.15.2.2`: каждый reliance-bearing PlanItem содержит target Method, window, role requirement, budget, dependencies, acceptance target. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.15.2.3`: intended RoleAssignment не считается valid для интервала Work автоматически. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.15.2.4`: actual costs/resources — в Work. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.15.2.5`: PlanItem decomposition не навязывает ту же форму Work. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.15.2.6`: cross-context планирование объявляет bridges. | Контрольный критерий не выполнен — возможна структурная ошибка. |

## 8. Связь с другими паттернами
| Паттерн | Связь |
|---|---|
| A.15.1 U.Work | факт vs намерение. |
| A.15 Role–Method–Work Alignment | обзор. |
| A.3 Transformer Quartet | Method/MethodDescription. |
| A.2 Role Taxonomy | role kinds. |
| A.10 Evidence Graph Referring | evidence для acceptance. |
| B.1 Γ | агрегация ресурсов. |
---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §A.15.2*
