---
id: CS.FPF.001
type: fpf-pattern-capture
fpf_pattern: A.15
fpf_title: "Role–Method–Work Alignment (Contextual Enactment)"
status: active
date: 2026-05-26
author: "Kimi Code CLI (FPF capture mode)"
domain: cattle-science
scope: [01-domain-contract, 03-methods, 04-work-products]
---

# CS.FPF.001: A.15 — Role–Method–Work Alignment в Cattle-Science

> **Паттерн:** A.15 (Kernel Architecture Cluster)  
> **Статус FPF:** Stable / Normative  
> **Цель capture:** Формализовать различение Role / Method / WorkPlan / Work для ветеринарно-зоотехнической практики на молочной ферме.

---

## 1. Суть паттерна (At a glance)

A.15 решает главную путаницу в операционной работе: команда спорит о «процессе», не различая:
- **Кто** отвечает (Role + Holder)
- **Как** должно делаться (MethodDescription)
- **Что запланировано** (WorkPlan)
- **Что реально сделано** (Work)

**FPF-тезис:** *Путаница Role/Method/Plan/Work — первоисточник ошибок проектирования, перерасхода бюджета и провалов.*

---

## 2. Core Entities — перевод на домен Cattle-Science

| FPF Entity | Инженерный эквивалент | Пример из фермы |
|---|---|---|
| **U.Role** | Должностная функция | `VeterinarianRole`, `NutritionistRole`, `MilkerRole` |
| **U.Holder** | Конкретный исполнитель | `Dr. Ivanov`, `Nutritionist Petrova`, `Operator Sidorov` |
| **U.BoundedContext** | Границы применимости | `Farm_A_Transition_Barn`, `Herd_Health_Program_2026` |
| **U.RoleAssignment** | Назначение | `Dr.Ivanov#VeterinarianRole:Farm_A` |
| **U.MethodDescription** | Протокол / SOP | `CS.METHOD.001` (кетоз — диагностика и лечение) |
| **U.Capability** | Компетенция холдера | «Владеет ультразвуковой диагностикой», «Сертифицирован по DCAD» |
| **U.WorkPlan** | План работ | «Обработка сухостойных 25–31 мая», «Вакцинация отельников — июнь» |
| **U.Work** | Фактическая работа | `Work_2026-05-26_#1847`: инъекция пропиленгликоля корове #2341, 08:15–08:22 |

---

## 3. Каскад типичных ошибок (Problem — FPF A.15:2)

| Ошибка | Пример из практики | Последствие |
|---|---|---|
| **Role-as-Part** | «Ветеринар» записан в органиграмме как подразделение, а не как роль с контекстом | Непонятно, кто именно принимает решение при смене врача |
| **Specification-as-Execution** | «У нас есть протокол кетоза» = «мы лечим кетоз правильно» | Paper compliance: протокол есть, а учёт фактических случаев — нет |
| **Capability-as-Work** | «Наш ветеринар умеет делать КТ» = «КТ сделана» | Смешение навыка и факта выполнения диагностики |
| **Work-without-Context** | «Вчера обработали 15 коров» — без ссылки на метод и роль | Невозможно аудит: что именно делали, по какому протоколу |
| **Ambiguous «process»** | «Процесс переходного периода» означает и план, и метод, и работу одновременно | Невозможно определить, где план, где выполнение |

---

## 4. Канонические связи (Canonical Relations)

```mermaid
graph TD
    subgraph Design-Time [Tᴰ — Мир потенциала]
        BC[Farm Context<br/>U.BoundedContext] -- defines --> R[VeterinarianRole<br/>U.Role]
        M[Ketosis Protocol<br/>U.Method] -- isDescribedBy --> MD[CS.METHOD.001<br/>U.MethodDescription]
        Cap[Ultrasound Skill<br/>U.Capability] -- supports --> M
        H[Dr. Ivanov<br/>U.System] --> RA[Dr.Ivanov#Vet:Farm_A<br/>U.RoleAssignment]
        R -- is the role in --> RA
        BC -- is the context for --> RA
        BC -- bindsCapability --> Cap
    end

    subgraph Run-Time [Tᴿ — Мир актуальности]
        W[Work_2026-05-26_#1847<br/>U.Work]<br/>ketosis treatment<br/>cow #2341, 08:15-08:22]
    end

    RA -- performedBy --> W
    W  -- isExecutionOf --> MD
```

**Полная трассируемость:**
`Work_#1847` → `isExecutionOf` → `CS.METHOD.001` → `isDescribedBy` → `KetosisTreatmentMethod` → `performedBy` → `Dr.Ivanov#VeterinarianRole:Farm_A`

---

## 5. Archetypal Grounding — двойная индустрия

| Аспект | Мануфактура (FPF archetype) | Cattle-Science (this capture) |
|---|---|---|
| **BoundedContext** | `FactoryFloor:Line_B` | `Farm_A:Transition_Barn` |
| **Role** | `WeldingRobotRole` | `ReproductionSpecialistRole` |
| **Holder** | `ABB_IRB_6700` | `Dr. Petrov` |
| **MethodDescription** | `Welding_WP-28A.pdf` | `CS.METHOD.005` (Ca monitoring) |
| **Capability** | `executeWeldingSeam(3F)` | `performTransrectalUS()`, `interpretNEFA()` |
| **Work** | `Weld_Job_#78345` (15:32–15:34, 1.2 kWh) | `Work_#1847` (08:15–08:22, cow #2341, 300 mL propylene glycol) |

**Key takeaway:** Сварка шасси и лечение кетоза имеют **идентичную причинно-следственную структуру** — разница только в доменной онтологии.

---

## 6. Применение к существующим артефактам PACK

### 6.1 CS.METHOD.001 (кетоз)

| Слой | Существующий артефакт | Статус по A.15 |
|---|---|---|
| U.MethodDescription | `CS.METHOD.001-ketosis-diagnosis-treatment.md` | ✅ Определён |
| U.Role | Неявный (`Veterinarian`) | ⚠️ Не формализован |
| U.WorkPlan | Нет отдельного файла | ❌ Отсутствует |
| U.Work | Нет журнала работ | ❌ Отсутствует |

**Рекомендация:** Для каждого CS.METHOD создать связанный WorkPlan-шаблон и Work-log формат.

### 6.2 CS.WP.001 (Metabolic Status Assessment Report)

- **Тип:** U.Episteme (отчёт как результат работы)
- **isOutputOf:** Work (обследование стада)
- **governedBy:** CS.METHOD.XXX (метод сбора и анализа данных)
- **performedBy:** RoleAssignment (`Nutritionist#HerdAssessment:Farm_A`)

**Рекомендация:** В отчёте явно указывать: кто выполнял работу, по какому методу, в каком контексте.

---

## 7. Bounded specialization scouting (A.15:4.3)

В применении к cattle-science: когда ветеринар + ИИ-система (например, предиктивная модель кетоза) работают в паре:

| Локальная роль | Ответственность |
|---|---|
| `UtilityOwnerRole` (ветеринар) | Определяет цель: «снизить клинический кетоз на 20%» |
| `AIScoutRole` (модель) | Перебирает коридоры решений: кормление, мониторинг, генетика |
| `AISpecialistProbeRole` (модель) | Тестирует один коридор: «прогнозная точность 85% при NEFA > 0.7» |
| `CommitAuthorityRole` (ветеринар) | Принимает решение: «внедряем NEFA-мониторинг» |

**CheckpointReturn** должен содержать:
- Целевая утилита: снижение кетоза 20%
- Протестированные подходы: NEFA-мониторинг, BHB-полоски, DCAD-оптимизация
- Эвиденс: точность, бюджет, риски
- Рекомендация: commit / continue probe / stop
- Триггер коммита: точность > 85% AND стоимость < $5/голову

---

## 8. Conformance Checklist (A.15:7)

| # | Проверка | Статус в PACK |
|---|----------|---------------|
| 1 | Различены U.Role, U.MethodDescription, U.WorkPlan, U.Work | ⚠️ Частично (методы есть, роли — нет) |
| 2 | Каждый U.Work имеет performedBy → U.RoleAssignment | ❌ Нет Work-log |
| 3 | Каждый U.Work имеет isExecutionOf → U.MethodDescription | ❌ Нет Work-log |
| 4 | U.Capability отделён от U.Work | ⚠️ Неявно |
| 5 | U.WorkPlan отделён от U.Work | ❌ Нет WorkPlan-ов |
| 6 | Briefing / dashboard не используется как execution authority | ⚠️ Требует аудита |

---

## 9. Немедленные действия (Minimum Sufficient Next Move)

1. **Создать роли:** Формализовать 3–5 ключевых ролей в `02-domain-entities/02A-roles.md`
2. **Создать WorkPlan-шаблон:** Для каждого CS.METHOD добавить связанный план
3. **Создать Work-log формат:** Минимальный: `timestamp, holder, role, method, target, duration, outcome`
4. **Аудит существующих отчётов:** Проверить CS.WP.001/002 на явное указание RoleAssignment

---

## 10. Relations to other FPF patterns

| Паттерн | Связь |
|---------|-------|
| A.7 Strict Distinction | A.15 — операционализация A.7 для enactment |
| A.2 Role Taxonomy | Поставщик U.Role, U.RoleAssignment |
| A.15.1 U.Work | Говорит о dated execution |
| A.15.2 U.WorkPlan | Говорит о планировании |
| B.3 F-G-R | Work outcomes служат evidence для capability conformance |
| B.5 ADI-Cycle | CheckpointReturn — это абдукция перед коммитом |

---

*Capture выполнен в рамках WP-1 (Саморазвитие — 1 FPF-принцип → capture в PACK).*  
*Session: 2026-05-26 · FPF Source: FPF/FPF-Spec.md §A.15*