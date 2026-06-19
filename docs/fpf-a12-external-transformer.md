---
type: fpf-study
pattern: A.12
title: "External Transformer & Reflexive Split: нет самодействия"
domain: cattle-science
difficulty: intermediate
reading_time: 25 min
created: 2026-06-19
---

# A.12 — External Transformer & Reflexive Split

## 1. Зачем это читать

«Система сконфигурировала себя сама», «датчик откалибровался», «документ обновил себя» — эти фразы скрывают причинность. В FPF любое изменение требует внешнего агента. Даже «самообучающиеся» системы моделируются через Reflexive Split.

**FPF-тезис:** *«Нет self-magic. Каждое изменение — следствие взаимодействия агента и объекта через границу.»*

---

## 2. Три элемента

Каждое преобразование — это:

1. **Agent** — `System#TransformerRole:Context`
2. **Target** — `U.Holon` под изменением
3. **Boundary** — `U.Boundary` с `U.Interaction`

**Ключевое неравенство:**

```text
holder(Agent) ≠ Target
```

---

## 3. Reflexive Split

Когда кажется, что система действует на себя, разделите её на две подсистемы:

| Роль | Что делает | Пример |
|---|---|---|
| **Regulator** | Контролирует/калибрует | CalibrationController |
| **Regulated** | Подвергается изменению | SensorSuite |

**Пример:** робот «калибрует себя» → внутри робота:

```text
CalibrationController#TransformerRole:RobotInternals
  → interacts across internal data bus
  → SensorSuite (target)
```

---

## 4. Фермерские примеры

### 4.1 Самокалибрующийся доильный зал

Naive: «Доильный зал откалибровал себя.»

FPF:

```text
Agent:    MilkingParlor_CalibrationModule#TransformerRole:ParlorInternals
Boundary: internal control bus
Target:   MilkingParlor_SensorSuite
Work:     calibration run 2026-06-19T04:00
```

### 4.2 Автоматическая кормушка

Naive: «Кормушка сама увеличила порцию.»

FPF:

```text
Agent:    Feeder_Controller#TransformerRole:FeederSystem
Boundary: CAN bus
Target:   Feeder_Dispenser
Work:     portion adjustment 2026-06-19T12:05
Evidence: feed log, weight sensor readings
```

### 4.3 Обновление SOP

Naive: «SOP обновился.»

FPF:

```text
Agent:    FarmManager_Anna#AuthorRole:FarmA_QA
Boundary: document control system
Target:   SOP_Ketosis_Treatment_v2 (symbol carrier)
Work:     revision 2026-06-18, approved by QA
```

---

## 5. No Self-Evidence

Агент, выполнивший Work, не может быть единственным источником evidence для его успеха. Evidence должен производить **независимый Observer**.

**Пример:**
- `CalibrationController` выполнил калибровку.
- Evidence: independent metrology lab report + sensor cross-check.

---

## 6. Контрольный чеклист

- `CC-A.12.1`: каждый `U.Work` приписан агенту, чей holder ≠ target.
- `CC-A.12.2`: «self-X» смоделирован через Reflexive Split.
- `CC-A.12.3`: граница и interaction между агентом и объектом явны.
- `CC-A.12.4`: при изменении episteme target — её symbol carrier.
- `CC-A.12.5`: evidence для transformation исходит от независимого Observer.

---

## 7. Связи

- **A.3 Transformer Quartet** — четыре якоря действия.
- **A.10 Evidence Graph Referring** — external evidence.
- **A.2 Role Taxonomy** — Role Assignment.
- **A.1 Holonic Foundation** — System vs Episteme.
- **B.2.5 Supervisor-Subsystem Feedback Loop** — детали Regulator–Regulated.

---

*Capture написан по FPF-Spec.md §A.12 для PACK-cattle-science.*
