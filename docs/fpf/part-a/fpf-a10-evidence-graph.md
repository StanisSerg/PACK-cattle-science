---
type: fpf-study
pattern: A.10
title: "Evidence Graph Referring: claims must carry carriers"
domain: cattle-science
difficulty: intermediate
reading_time: 30 min
created: 2026-06-19
---

# A.10 — Evidence Graph Referring: claims must carry carriers

## 1. Зачем это читать
«У нас есть исследование, что это работает» — фраза без доказательной цепочки. A.10 требует, чтобы каждый claim был привязан к carriers, external transformer, method trace, work trace и временному окну.

**FPF-тезис:** *«Claim без carrier — бесшумный. Dashboard без источника — не доказательство.»*

## 2. История одной ошибки
Ветеринар Анна утверждала, что корова здорова, потому что «есть исследование». Но исследование было опубликовано на другом типе коров, без указания метода отбора, а данные по этой ферме собирались вручную в разных таблицах. Когда аудитор попросил evidence path, оказалось, что связь между claim'ом «здорова» и carrier'ом не воспроизводится: неизвестно, кто измерял BHB, каким прибором и в каком окне после отёла.

## 3. Evidence Graph Referring: claims must carry carriers — полное описание

### 3.1 EPV-DAG
Evidence-Provenance DAG — это ациклический граф, отдельный от mereology. Узлы:

- `SymbolCarrier` — файлы, датасеты, лабораторные журналы, рисунки;
- `TransformerRole` — внешний transformer (A.12);
- `MethodDescription` — рецепт;
- `Observation` — датированное утверждение/результат;
- `s.Episteme` — знание.

Рёбра: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore`.

### 3.2 Два вида evidence
| Relation | Когда | Пример |
|---|---|---|
| `verifiedBy` | Формальное доказательство | Статический анализ, математическое доказательство |
| `validatedBy` | Эмпирическое доказательство | Полевые испытания, измерения, лабораторные тесты |

Обе заканчиваются в EPV-DAG, а не в part-whole graph.

### 3.3 SCR / RSCR
- **SCR** — Symbol Carrier Register: полный список carriers, использованных при агрегации `Γ_epist`.
- **RSCR** — Restricted SCR: адаптирован под bounded context с публикационными идентификаторами.

**Фермерский пример:**

```text
SCR for claim «Propylene glycol reduces ketosis»:
  - study: Gonzales_2022_dairy_cows.pdf
  - dataset: ketosis_trial_2022.csv
  - code: analysis_v3.R
  - lab notebook: farmA_lab_2022_Q3.md
```

### 3.4 Минимальный evidence path
Практический shortcut: ответьте на четыре вопроса:

1. **What carriers?** — какие файлы/данные/журналы?
2. **Which system?** — кто произвёл evidence?
3. **Which method?** — по какому протоколу?
4. **When?** — временное окно и freshness.

Если хоть один ответ пропущен — evidence недостаточно.

### 3.5 Reliance disposition
Когда источник выглядит авторитетно, но evidence path неполон:

| Disposition | Когда |
|---|---|
| `pass` | evidence relation текущая и bounded |
| `degrade` | источник поддерживает только более узкий claim |
| `abstain` | evidence недостаточно, но отказ преждевременен |
| `evidence-needed` | известно, какого evidence не хватает |
| `blocked-current-use` | unsupported claim — блокировать |

## 4. Почему смешивать / игнорировать — значит рисковать
Если пренебречь A.10, типичные риски на ферме:

| Что происходит | Почему это опасно |
|---|---|
| Решения принимаются на основе смешанных или устаревших данных | Невозможно отследить, что именно повлияло на результат |
| Роли и методы не разделены | Один и тот же человек или документ отвечает за несовместимые обязательства |
| Перенос знаний между контекстами без явного bridge | Рекомендации из одной традиции применяют к другой без учёта потерь |
| Отсутствие контрольного списка | Ошибки обнаруживаются слишком поздно, когда они уже стоят денег |

**Каскад:** нечёткое утверждение → неправильная интерпретация → некорректное решение → экономический убыток и снижение доверия к системе.

## 5. Как это выглядит на ферме: Фермерские примеры
### 5.1 Claim: «Корова #401 здорова»
- Carrier: vet record #2026-0619-401, BHB test strip photo
- External transformer: Vet_Maria#VeterinarianRole:FarmA
- Method: SOP_WellnessCheck_v2
- Work: 2026-06-19T08:15 examination
- Time window: 2026-06-19 08:15–08:35

### 5.2 Claim: «Молоко соответствует стандарту»
- Carrier: lab report #LAB-2026-044, sensor log tank #3
- External transformer: RegionalLab_C#AnalystRole
- Method: ISO_11866_SCC_method
- Work: sampling 2026-06-18T06:00

## 6. Практическое применение: с чего начать
**Шаг 1.** Выберите одно важное утверждение, на основе которого принимается решение (например, «стадо не в кетозе»).

**Шаг 2.** Для него найдите: claim, carrier, transformer, method, work, time window.

**Шаг 3.** Если какое-то звено отсутствует — либо откажитесь от claim'а, либо восстановите источник.

**Шаг 4.** Запишите evidence path в виде графа с ID каждого узла.

**Шаг 5.** Проверьте, что при удалении любого узла claim становится непроверяемым.

## 7. Проверь себя
| Вопрос | Если ответ «да» — проблема |
|---|---|
| `CC-A.10.1`: каждый published claim имеет путь в EPV-DAG. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.10.2`: `Γ_epist^synth` выдаёт SCR. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.10.3`: `Γ_epist^compile` выдаёт RSCR. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.10.4`: evidencing transformer external к оцениваемому holon. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.10.5`: design-time и run-time не смешаны в одном EPV-DAG. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.10.6`: provenance edges не используются как part-whole edges. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.10.7`: временное покрытие monotone и явно указано. | Контрольный критерий не выполнен — возможна структурная ошибка. |

## 8. Связь с другими паттернами
| Паттерн | Связь |
|---|---|
| A.12 External Transformer | external evidence producer. |
| A.3 Transformer Quartet | method/work traceability. |
| A.4 Temporal Duality | design/run scope separation. |
| A.7 Strict Distinction | claim vs carrier vs description. |
| B.3 Trust Framework | confidence penalties и assurance. |
| C.16 Measurement & Evidence | метрологические детали. |
---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §A.10*
