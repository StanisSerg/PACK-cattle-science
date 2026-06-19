---
type: fpf-study
pattern: A.12
title: "External Transformer & Reflexive Split: нет самодействия"
domain: cattle-science
difficulty: intermediate
reading_time: 25 min
created: 2026-06-19
---

# A.12 — External Transformer & Reflexive Split: нет самодействия

## 1. Зачем это читать
«Система сконфигурировала себя сама», «датчик откалибровался», «документ обновил себя» — эти фразы скрывают причинность. В FPF любое изменение требует внешнего агента. Даже «самообучающиеся» системы моделируются через Reflexive Split.

**FPF-тезис:** *«Нет self-magic. Каждое изменение — следствие взаимодействия агента и объекта через границу.»*

## 2. История одной ошибки
Доильный робот сам калибровал датчики и сам же фиксировал, что молоко соответствует норме. Когда молоко внезапно стало отклоняться по жиру, никто не заметил, что калибровка была внутренней: System проверял сам себя. Внешний transformer отсутствовал, поэтому отклонение было подавлено как «погрешность датчика».

## 3. External Transformer & Reflexive Split: нет самодействия — полное описание

### 3.1 Три элемента
Каждое преобразование — это:

1. **Agent** — `System#TransformerRole:Context`
2. **Target** — `U.Holon` под изменением
3. **Boundary** — `U.Boundary` с `U.Interaction`

**Ключевое неравенство:**

```text
holder(Agent) ≠ Target
```

### 3.2 Reflexive Split
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

### 3.3 No Self-Evidence
Агент, выполнивший Work, не может быть единственным источником evidence для его успеха. Evidence должен производить **независимый Observer**.

**Пример:**
- `CalibrationController` выполнил калибровку.
- Evidence: independent metrology lab report + sensor cross-check.

## 4. Почему смешивать / игнорировать — значит рисковать
Если пренебречь A.12, типичные риски на ферме:

| Что происходит | Почему это опасно |
|---|---|
| Решения принимаются на основе смешанных или устаревших данных | Невозможно отследить, что именно повлияло на результат |
| Роли и методы не разделены | Один и тот же человек или документ отвечает за несовместимые обязательства |
| Перенос знаний между контекстами без явного bridge | Рекомендации из одной традиции применяют к другой без учёта потерь |
| Отсутствие контрольного списка | Ошибки обнаруживаются слишком поздно, когда они уже стоят денег |

**Каскад:** нечёткое утверждение → неправильная интерпретация → некорректное решение → экономический убыток и снижение доверия к системе.

## 5. Как это выглядит на ферме: Фермерские примеры
### 5.1 Самокалибрующийся доильный зал
Naive: «Доильный зал откалибровал себя.»

FPF:

```text
Agent:    MilkingParlor_CalibrationModule#TransformerRole:ParlorInternals
Boundary: internal control bus
Target:   MilkingParlor_SensorSuite
Work:     calibration run 2026-06-19T04:00
```

### 5.2 Автоматическая кормушка
Naive: «Кормушка сама увеличила порцию.»

FPF:

```text
Agent:    Feeder_Controller#TransformerRole:FeederSystem
Boundary: CAN bus
Target:   Feeder_Dispenser
Work:     portion adjustment 2026-06-19T12:05
Evidence: feed log, weight sensor readings
```

### 5.3 Обновление SOP
Naive: «SOP обновился.»

FPF:

```text
Agent:    FarmManager_Anna#AuthorRole:FarmA_QA
Boundary: document control system
Target:   SOP_Ketosis_Treatment_v2 (symbol carrier)
Work:     revision 2026-06-18, approved by QA
```

## 6. Практическое применение: с чего начать
**Шаг 1.** Перечислите измерения и решения, от которых зависят деньги или здоровье животных.

**Шаг 2.** Для каждого определите: кто/что является System, а кто/что — External Transformer.

**Шаг 3.** Запретите одному и тому же System'у быть одновременно исполнителем и verifier'ом.

**Шаг 4.** Введите расписание внешней калибровки/аудита с ID Work.

**Шаг 5.** Документируйте reflexive split в SOP.

## 7. Проверь себя
| Вопрос | Если ответ «да» — проблема |
|---|---|
| `CC-A.12.1`: каждый `U.Work` приписан агенту, чей holder ≠ target. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.12.2`: «self-X» смоделирован через Reflexive Split. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.12.3`: граница и interaction между агентом и объектом явны. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.12.4`: при изменении episteme target — её symbol carrier. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.12.5`: evidence для transformation исходит от независимого Observer. | Контрольный критерий не выполнен — возможна структурная ошибка. |

## 8. Связь с другими паттернами
| Паттерн | Связь |
|---|---|
| A.3 Transformer Quartet | четыре якоря действия. |
| A.10 Evidence Graph Referring | external evidence. |
| A.2 Role Taxonomy | Role Assignment. |
| A.1 Holonic Foundation | System vs Episteme. |
| B.2.5 Supervisor-Subsystem Feedback Loop | детали Regulator–Regulated. |
---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §A.12*
