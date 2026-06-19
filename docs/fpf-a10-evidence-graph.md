---
type: fpf-study
pattern: A.10
title: "Evidence Graph Referring: claims must carry carriers"
domain: cattle-science
difficulty: intermediate
reading_time: 30 min
created: 2026-06-19
---

# A.10 — Evidence Graph Referring

## 1. Зачем это читать

«У нас есть исследование, что это работает» — фраза без доказательной цепочки. A.10 требует, чтобы каждый claim был привязан к carriers, external transformer, method trace, work trace и временному окну.

**FPF-тезис:** *«Claim без carrier — бесшумный. Dashboard без источника — не доказательство.»*

---

## 2. EPV-DAG

Evidence-Provenance DAG — это ациклический граф, отдельный от mereology. Узлы:

- `SymbolCarrier` — файлы, датасеты, лабораторные журналы, рисунки;
- `TransformerRole` — внешний transformer (A.12);
- `MethodDescription` — рецепт;
- `Observation` — датированное утверждение/результат;
- `s.Episteme` — знание.

Рёбра: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore`.

---

## 3. Два вида evidence

| Relation | Когда | Пример |
|---|---|---|
| `verifiedBy` | Формальное доказательство | Статический анализ, математическое доказательство |
| `validatedBy` | Эмпирическое доказательство | Полевые испытания, измерения, лабораторные тесты |

Обе заканчиваются в EPV-DAG, а не в part-whole graph.

---

## 4. SCR / RSCR

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

---

## 5. Минимальный evidence path

Практический shortcut: ответьте на четыре вопроса:

1. **What carriers?** — какие файлы/данные/журналы?
2. **Which system?** — кто произвёл evidence?
3. **Which method?** — по какому протоколу?
4. **When?** — временное окно и freshness.

Если хоть один ответ пропущен — evidence недостаточно.

---

## 6. Фермерские примеры

### 6.1 Claim: «Корова #401 здорова»

- Carrier: vet record #2026-0619-401, BHB test strip photo
- External transformer: Vet_Maria#VeterinarianRole:FarmA
- Method: SOP_WellnessCheck_v2
- Work: 2026-06-19T08:15 examination
- Time window: 2026-06-19 08:15–08:35

### 6.2 Claim: «Молоко соответствует стандарту»

- Carrier: lab report #LAB-2026-044, sensor log tank #3
- External transformer: RegionalLab_C#AnalystRole
- Method: ISO_11866_SCC_method
- Work: sampling 2026-06-18T06:00

---

## 7. Reliance disposition

Когда источник выглядит авторитетно, но evidence path неполон:

| Disposition | Когда |
|---|---|
| `pass` | evidence relation текущая и bounded |
| `degrade` | источник поддерживает только более узкий claim |
| `abstain` | evidence недостаточно, но отказ преждевременен |
| `evidence-needed` | известно, какого evidence не хватает |
| `blocked-current-use` | unsupported claim — блокировать |

---

## 8. Контрольный чеклист

- `CC-A.10.1`: каждый published claim имеет путь в EPV-DAG.
- `CC-A.10.2`: `Γ_epist^synth` выдаёт SCR.
- `CC-A.10.3`: `Γ_epist^compile` выдаёт RSCR.
- `CC-A.10.4`: evidencing transformer external к оцениваемому holon.
- `CC-A.10.5`: design-time и run-time не смешаны в одном EPV-DAG.
- `CC-A.10.6`: provenance edges не используются как part-whole edges.
- `CC-A.10.7`: временное покрытие monotone и явно указано.

---

## 9. Связи

- **A.12 External Transformer** — external evidence producer.
- **A.3 Transformer Quartet** — method/work traceability.
- **A.4 Temporal Duality** — design/run scope separation.
- **A.7 Strict Distinction** — claim vs carrier vs description.
- **B.3 Trust Framework** — confidence penalties и assurance.
- **C.16 Measurement & Evidence** — метрологические детали.

---

*Capture написан по FPF-Spec.md §A.10 для PACK-cattle-science.*
