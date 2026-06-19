---
type: fpf-study
pattern: A.3
title: "Transformer Quartet: who acts, by what recipe, with what result"
domain: cattle-science
difficulty: intermediate
reading_time: 25 min
created: 2026-06-19
---

# A.3 — Transformer Constitution (Quartet)

## 1. Зачем это читать

Когда фермер говорит «насос качает воду» или «ветеринар вылечил корову», он смешивает четыре разные вещи. FPF требует их разделять, иначе невозможно отследить причинность, ответственность и аудит.

**FPF-тезис:** *«Нет самодействия. Каждое изменение — это System-in-Role, MethodDescription, Method и Work.»*

---

## 2. Четыре якоря

| Якорь | Что это | Жизненный пример |
|---|---|---|
| **System bearing TransformerRole** | Система, которая действует | Ветеринар, дояр, робот, насос, скрипт |
| **MethodDescription** | Рецепт/описание в **Tᴰ** | SOP «Лечение кетоза», протокол сухостоя, чертёж насоса |
| **Method** | Семантический способ действия | «Ввести 1 л пропиленгликоля», «откачать 1000 л воды» |
| **Work** | Датированное событие в **Tᴿ** | 2026-06-19 08:15 — введено 1 л препарата корове №401 |

**Безопасная формула:**

```text
MethodDescription → describes → Method → executedAs → Work
```

---

## 3. Role Assignment

Кто действует, где и в какой роли:

```text
U.RoleAssignment(
  holder  : U.System,
  role    : U.TransformerRole,
  context : U.BoundedContext,
  timespan?: Interval
)
```

**Фермерский пример:**
- `Vet_Maria#VeterinarianRole:FarmA_2026` лечит корову.
- `MilkingRobot_3#MilkingRole:BarnB` доит стадо.
- `FertiliserSpreadController#ApplicatorRole:FieldC` распределяет удобрения.

Роль локальна и привязана ко времени. Один и тот же человек может быть ветеринаром утром и консультантом вечером — но в разных контекстах.

---

## 4. Типичные ошибки

| Ошибка | Почему это не так | Правильно |
|---|---|---|
| «Система настроилась сама» | Self-magic: нет внешнего агента | Разделить Regulator и Regulated (A.12) |
| «Протокол лечит» | MethodDescription ≠ Work | Протокол описывает Method; лечение — Work |
| «У нас есть SOP — значит, работа выполнена» | MethodDescription ≠ Work | Проверить журнал Work |
| «Ветеринар — это роль» | Человек ≠ роль | Human `Maria` bears `VeterinarianRole` |

---

## 5. Пример: лечение кетоза

```text
System bearing TransformerRole:
  Vet_Maria#VeterinarianRole:FarmA_2026

MethodDescription (Tᴰ):
  SOP_Ketosis_Treatment_v2.md

Method:
  AdministerPropyleneGlycol(1L, oral, BHB<1.2)

Work (Tᴿ):
  2026-06-19T08:15, Cow#401,
  performer = Vet_Maria#VeterinarianRole:FarmA_2026,
  enactsMethod = AdministerPropyleneGlycol,
  methodDescriptionRef = SOP_Ketosis_Treatment_v2,
  resources = {propylene glycol 1L, syringe},
  outcome = BHB 0.9 mmol/L at 18:00
```

---

## 6. Контрольный чеклист

- `CC-A.3.1`: каждое преобразование сопровождается `U.RoleAssignment`.
- `CC-A.3.2`: `holder` роли TransformerRole не совпадает с объектом изменения (A.12).
- `CC-A.3.3`: `MethodDescription` живёт в Tᴰ; `Work` — в Tᴿ.
- `CC-A.3.4`: каждый `Work` ссылается на `Method` и `MethodDescription` версии.
- `CC-A.3.5`: отклонения от рецепта зафиксированы как `policy override` или `exception path`.
- `CC-A.3.6`: ресурсы списаны именно на `Work`, а не на роль или описание.

---

## 7. Связи

- **A.2 Role Taxonomy** — роль как маска.
- **A.4 Temporal Duality** — Tᴰ/Tᴿ разделение.
- **A.12 External Transformer** — запрет self-magic.
- **A.15 Role–Method–Work Alignment** — пять сущностей под словом «процесс».
- **A.10 Evidence Graph Referring** — Work как якорь для evidence.

---

*Capture написан по FPF-Spec.md §A.3 для PACK-cattle-science.*
