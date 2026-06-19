---
type: fpf-study
pattern: A.2
title: "Role Taxonomy: роль — не человек и не часть"
domain: cattle-science
difficulty: beginner
reading_time: 20 min
created: 2026-06-19
---

# A.2 — Role Taxonomy

## 1. Зачем это читать

Если вы путаете «должность» с «работой», «человека» с «функцией» или «роль» со «структурой» — вы делаете категориальную ошибку. Когда ветеринар увольняется, `VeterinarianRole` не исчезает. Когда корова меняет группу, она остаётся той же коровой.

A.2 учит: **роль — это контекстуальная маска**, которую холон надевает на время. Поведение живёт в Method и Work, не в роли.

**FPF-тезис:** *«Существо говорит, что это такое. Роль говорит, кем оно является здесь и сейчас.»*

---

## 2. Две ключевые сущности

### 2.1 U.Role — «маска»

Роль — это схема возможностей и обязанностей внутри bounded context. У роли:
- нет структурных частей (не участвует в `partOf`),
- нет ресурсных дельт (не влечёт Work),
- есть локальное значение в контексте.

**Пример:** `CoolingCirculatorRole`, `VeterinarianRole`, `ConstraintSourceRole`.

### 2.2 U.RoleAssignment — «кто носит маску, где и когда»

```text
U.RoleAssignment {
  holder        : U.Holon,
  role          : U.Role,
  context       : U.BoundedContext,
  window?       : U.Window,
  justification?: U.Episteme,
  provenance?   : U.Method
}
```

Краткая форма: `Holder#Role:Context@Window`.

**Пример:** `Dr.Ivanov#VeterinarianRole:Farm_A@2026-06-19`.

---

## 3. Роль ≠ часть

Роли никогда не бывают частями холона. Если в диаграмме «Роль → part-of → Холон» — модель не проходит.

| Правильно | Неправильно |
|---|---|
| Корова играет `MilkingCowRole` | `MilkingCowRole` — часть коровы |
| Насос играет `CoolingCirculatorRole` | `CoolingCirculatorRole` — компонент насоса |

---

## 4. Роль ≠ поведение

Роль не делает работу. Система в роли делает работу по методу.

| Правильно | Неправильно |
|---|---|
| «Система в роли `VeterinarianRole` выполнила Work по протоколу» | «Роль ветеринара лечит коров» |
| «Насос в роли `CirculatorRole` имеет Method циркуляции» | «Роль циркулятора — крутить воду» |

---

## 5. Episteme может иметь только не-поведенческие роли

Документы, модели, протоколы не могут действовать. Но они могут играть роли вроде:
- `ReferenceRole` — используется как ссылка,
- `ConstraintSourceRole` — источник ограничений,
- `JustificationRole` — обоснование.

**Неправильно:** «Протокол требует вакцинации».
**Правильно:** «Протокол играет `ConstraintSourceRole`; система в роли `VeterinarianRole` выполняет Work вакцинации».

---

## 6. Локальность роли

Роль определена внутри `U.BoundedContext`. Один и тот же holder может играть разные роли в разных контекстах. Одно и то же имя роли может означать разное в разных контекстах.

**Пример:**
- `Pluto#Planet:Early20thCenturyAstronomy`
- `Pluto#DwarfPlanet:IAU_2006_Definition`

Противоречия нет — разные контексты.

---

## 7. Ролевая алгебра

Внутри контекста роли могут быть:
- `RoleS ≤ RoleG` — специализация,
- `RoleS ⊥ RoleG` — несовместимость,
- `RoleS ⊗ RoleG` — bundle (совместное исполнение).

**Пример несовместимости:** в одном и том же случае хирург и независимый аудитор не могут быть одним лицом.

---

## 8. Контрольный чеклист

- `CC-A2.1`: роль не является mereological part.
- `CC-A2.2`: поведенческие роли может играть только System; Episteme — только не-поведенческие роли.
- `CC-A2.3`: поведенческая роль должна быть связана хотя бы с одним Method.
- `CC-A2.4`: каждая роль context-indexed.
- `CC-A2.5`: у RoleAssignment есть window или traceable open-ended assignment time.
- `CC-A2.6`: несовместимые роли не пересекаются по времени у одного holder.
- `CC-A2.7`: `performedBy(Work)` ссылается на конкретную RoleAssignment.
- `CC-A2.8`: Method описан MethodDescription; Work — исполнение конкретной версии MethodDescription.
- `CC-A2.9`: claims о ролях anchor к SCR/RSCR.

---

## 9. Связи с другими паттернами

- **A.1 Holonic Foundation** — holder существует независимо от роли.
- **A.1.1 Bounded Context** — роль определена в контексте.
- **A.7 Strict Distinction** — роль ≠ поведение.
- **A.15 Role–Method–Work** — как роль связана с Method и Work.
- **A.14 Advanced Mereology** — роли вне partOf.

---

*Capture написан по FPF-Spec.md §A.2 для PACK-cattle-science.*
