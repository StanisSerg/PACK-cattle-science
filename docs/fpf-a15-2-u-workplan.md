---
type: fpf-study
pattern: A.15.2
title: "U.WorkPlan: намерение, а не факт"
domain: cattle-science
difficulty: intermediate
reading_time: 20 min
created: 2026-06-19
---

# A.15.2 — U.WorkPlan

## 1. Зачем это читать

«Обработать коров в понедельник» — это ещё не «обработали». `U.WorkPlan` — первый-class episteme для intended work. Без него невозможно отслеживать отклонения: schedule variance, cost variance, scope variance.

**FPF-тезис:** *«Plan = when, by whom in intent, under which constraints. Work = how it went this time.»*

---

## 2. Что такое U.WorkPlan

`U.WorkPlan` — это `U.Episteme`, который декларирует intended `U.Work` occurrences:

- horizon и cadence;
- planned windows;
- dependencies;
- intended performers как role kinds или proposed `U.RoleAssignment`;
- resource budgets/reservations;
- acceptance targets;
- baseline для variance.

---

## 3. PlanItem

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

---

## 4. Различия

| Если вы говорите… | Это | Почему |
|---|---|---|
| «Расписание операций на завтра» | **WorkPlan** | Календарь intended runs |
| «Workflow доения» | **MethodDescription + Method** | Рецепт, не календарь |
| «Процесс уже выполнился в 10:00» | **Work** | Dated occurrence |
| «План назначает Марию» | **WorkPlan** с intended RoleAssignment | Assignment проверяется на момент Work |
| «Бюджет смены B» | **WorkPlan** (planned ledger) | Actuals — в Work |

---

## 5. Fulfilment и Variance

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

---

## 6. Фермерский пример: план обработки

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

---

## 7. Контрольный чеклист

- `CC-A.15.2.1`: WorkPlan именует intended Work, не performed work.
- `CC-A.15.2.2`: каждый reliance-bearing PlanItem содержит target Method, window, role requirement, budget, dependencies, acceptance target.
- `CC-A.15.2.3`: intended RoleAssignment не считается valid для интервала Work автоматически.
- `CC-A.15.2.4`: actual costs/resources — в Work.
- `CC-A.15.2.5`: PlanItem decomposition не навязывает ту же форму Work.
- `CC-A.15.2.6`: cross-context планирование объявляет bridges.

---

## 8. Связи

- **A.15.1 U.Work** — факт vs намерение.
- **A.15 Role–Method–Work Alignment** — обзор.
- **A.3 Transformer Quartet** — Method/MethodDescription.
- **A.2 Role Taxonomy** — role kinds.
- **A.10 Evidence Graph Referring** — evidence для acceptance.
- **B.1 Γ** — агрегация ресурсов.

---

*Capture написан по FPF-Spec.md §A.15.2 для PACK-cattle-science.*
