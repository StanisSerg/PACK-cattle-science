---
type: fpf-study
pattern: A.6
title: "Signature Stack & Boundary Discipline: разложить контракт на слои"
domain: cattle-science
difficulty: advanced
reading_time: 45 min
created: 2026-06-19
---

# A.6 — Signature Stack & Boundary Discipline

## 1. Зачем это читать

Контракты, API, протоколы, SLA, SOP — всё это «граничные утверждения». В одном предложении часто смешаны законы, требования, обещания и ожидаемые эффекты. A.6 учит раскладывать такие тексты на четыре квадранта, чтобы каждый отвечал за своё.

**FPF-тезис:** *«Не смешивайте «есть», «можно», «должен» и «проверено» в одном абзаце.»*

---

## 2. Стек граничных слоёв

| Слой | Что там | Стабильность | Пример для фермы |
|---|---|---|---|
| **Signature (L)** | Законы и определения | Высокая | «Корова — млекопитающее; масса измеряется в кг» |
| **Mechanism (A)** | Admissibility gates, entry conditions | Средняя | «Допуск к обработке: BHB > 1.2 mmol/L» |
| **Norms/Commitments (D)** | Обязательства агентов | Средняя | «Ветеринар обязан проверить температуру до инъекции» |
| **Evidence/Carriers (E)** | Эффекты и доказательства | Низкая | «Температура 38.5 °C зафиксирована логгером #7» |

Чем выше слой, тем стабильнее. Механизмы и форматы evidence меняются чаще, чем определения.

---

## 3. Boundary Norm Square (L/A/D/E)

Каждое граничное утверждение — ровно в одном квадранте:

|  | In-description | In-work |
|---|---|---|
| **Truth (is/iff)** | **L** Laws & Definitions | **E** Effects/Evidence |
| **Governance (must/may)** | **A** Admissibility | **D** Deontics/Commitments |

**Пример разложения:**

> «Обработка от клещей допускается только после отрицательного теста на мастит, и фермер обязан записать температуру.»

- **L**: «Обработка от клещей» — определение процедуры.
- **A**: «только после отрицательного теста» — admissibility gate.
- **D**: «фермер обязан записать температуру» — duty.
- **E**: запись температуры — evidence carrier.

---

## 4. Типичные ошибки

| Ошибка | Почему плохо | Ремонт |
|---|---|---|
| Gate predicate записан как закон | Нельзя менять gate, не меняя «закон» | Перенести в Mechanism (A) |
| «Должен» смешан с «если» | Duty vs admissibility | Разделить D и A |
| Эффект без carrier | Непроверяемо | Привязать к evidence (E) |
| Signature тянет за собой implementation | Реализацию нельзя менять | Вынести в lower layer |

---

## 5. Фермерский пример: SLA на молоко

```text
Boundary package: MilkQuality_SLA_v3

L-claims:
  L-1: MilkFat ≥ 3.4% (definition)
  L-2: SomaticCellCount < 200k/ml (definition)

A-claims:
  A-1: milk accepted only if L-1 and L-2 hold (admissibility gate)

D-claims:
  D-1: dairy lab must sample each batch (duty)
  D-2: farm must cool milk to 4°C within 2h (duty)

E-claims:
  E-1: lab report with timestamp, sampler, method (evidence)
  E-2: cooling log from tank sensor (evidence)
```

---

## 6. Контрольный чеклист

- `CC-A.6.1`: каждое утверждение разложено на L/A/D/E.
- `CC-A.6.2`: один claim — один квадрант; смешанные предложения атомизированы.
- `CC-A.6.3`: A-* gates не записаны как L-* законы.
- `CC-A.6.4`: D-* duties привязаны к ролям/агентам.
- `CC-A.6.5`: E-* claims привязаны к carriers и measurement conditions.
- `CC-A.6.6`: публикационные face (MVPK) ссылаются на claim ID, а не переписывают их.

---

## 7. Связи

- **A.6.B Boundary Norm Square** — четыре квадранта.
- **A.6.P Relational Precision Restoration** — ремонт расплывчатых отношений.
- **A.6.0 U.Signature** — формальное объявление Signature.
- **A.6.1 U.Mechanism** — механизмы с admissibility conditions.
- **A.7 Strict Distinction** — EntityOfConcern vs Description vs Carrier.
- **A.2.8 Commitment** — deontic claims.
- **A.10 Evidence Graph Referring** — evidence carriers.

---

*Capture написан по FPF-Spec.md §A.6 для PACK-cattle-science.*
