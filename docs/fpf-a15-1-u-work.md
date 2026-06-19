---
type: fpf-study
pattern: A.15.1
title: "U.Work: dated occurrence with resources and outcome"
domain: cattle-science
difficulty: intermediate
reading_time: 20 min
created: 2026-06-19
---

# A.15.1 — U.Work

## 1. Зачем это читать

Команды часто путают план, протокол и факт. `U.Work` — это единственное место, где фиксируется «что случилось на самом деле»: датированное событие с исполнителем, методом, параметрами, ресурсами и результатом.

**FPF-тезис:** *«Work = how it went this time.»*

---

## 2. Что такое U.Work

`U.Work` — это **4D occurrence holon**:

- датированный run-time enactment `U.Method`;
- performer через `U.RoleAssignment`;
- concrete parameter bindings;
- consumed/produced resources;
- affected referent и Δ (pre-state → post-state);
- executed within `U.System`/`U.SubSystem`.

---

## 3. Обязательные ссылки

Каждая `U.Work` **MUST** ссылаться на:

1. `enactsMethod → U.Method`
2. `methodDescriptionRef → U.MethodDescription` (если актуально)
3. `performedBy → U.RoleAssignment`
4. `executedWithin → U.System` или `U.SubSystem`
5. time window `[t_start, t_end]`
6. context

---

## 4. Различия в четырёх слотах

| Ты указываешь на… | Это | Литмус |
|---|---|---|
| Рецепт / SOP / код | **MethodDescription** | Это episteme? |
| Семантический способ | **Method** | Один и тот же способ в разных записях? |
| Назначение «кто есть что» | **RoleAssignment** | Можно переназначить? |
| Датированное событие с логами | **Work** | Произошло в (t₀,t₁)? |
| Изменение состояния | **Work.Δ** | pre → post на declared state-plane? |

---

## 5. Фермерские примеры

### 5.1 Инъекция корове

```text
Work: W-2026-0619-001
  method: AdministerPropyleneGlycol
  methodDescriptionRef: SOP_Ketosis_Treatment_v2
  performedBy: Vet_Maria#VeterinarianRole:FarmA_2026
  executedWithin: BarnA_MedicalBay
  window: 2026-06-19T08:15..08:20
  parameters: cowId=401, dose=1L, route=oral
  resources: propyleneGlycol 1L, syringe
  outcome: BHB pre=1.4, post=0.9 (18:00)
```

### 5.2 Доение

```text
Work: W-2026-0619-MR3-042
  method: MilkCow
  performedBy: MilkingRobot_3#MilkingRole:BarnB
  executedWithin: MilkingParlor_3
  window: 2026-06-19T05:12..05:18
  parameters: cowId=401, quarter=full
  resources: electricity 0.3 kWh, water 5L
  outcome: milk 28.4 kg, SCC 120k/ml
```

---

## 6. Work mereology

- `TemporalPartOf_work` — time-slice.
- `EpisodeOf_work` — продолжение после прерывания.
- `OperationalPartOf_work` — sub-run (например, разрез внутри операции).
- `ConcurrentPartOf_work` — параллельные sub-runs.

**Правило:** method composition ≠ proof of Work decomposition.

---

## 7. Контрольный чеклист

- `CC-A.15.1.1`: `U.Work` — run-time occurrence, не Method, не Plan.
- `CC-A.15.1.2`: есть `enactsMethod`, `methodDescriptionRef`, `performedBy`, `executedWithin`.
- `CC-A.15.1.3`: есть closed time window.
- `CC-A.15.1.4`: resources списаны на Work, а не на Plan.
- `CC-A.15.1.5`: retry / resumption / rework явно размечены.
- `CC-A.15.1.6`: effect Δ привязан к pre/post state на declared state-plane.

---

## 8. Связи

- **A.15 Role–Method–Work Alignment** — обзор пяти сущностей.
- **A.15.2 U.WorkPlan** — план vs факт.
- **A.3 Transformer Quartet** — Method/MethodDescription/Work.
- **A.12 External Transformer** — кто выполнил.
- **A.10 Evidence Graph Referring** — evidence из Work.
- **B.1 Γ** — агрегация resource deltas.

---

*Capture написан по FPF-Spec.md §A.15.1 для PACK-cattle-science.*
