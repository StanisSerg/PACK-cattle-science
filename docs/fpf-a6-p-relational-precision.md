---
type: fpf-study
pattern: A.6.P
title: "Relational Precision Restoration: когда «связан с» недостаточно"
domain: cattle-science
difficulty: advanced
reading_time: 50 min
created: 2026-06-19
---

# A.6.P — Relational Precision Restoration (RPR)

## 1. Зачем это читать

«Эта ферма связана с кооперативом», «корова зависит от кормовой базы», «данные привязаны к сезону». Все эти фразы скрывают вид отношения, участников, направление, область действия и время. A.6.P учит восстанавливать скрытую структуру, прежде чем полагаться на такие утверждения.

**FPF-тезис:** *«Зонтичные глаголы — это не отношения. Это триггеры для ремонта.»*

---

## 2. Когда применять

Используйте A.6.P, когда в тексте встречаются:

- «связан с», «зависит от», «влияет на», «основан на»;
- «синхронизирован», «привязан», «поддерживается»;
- «тот же», «эквивалентен», «соответствует»;
- метонимические или местоименные конечные точки («это», «здесь», «у них»);
- отношения, используемые для gate, assurance, cross-context reuse.

---

## 3. Рецепт RPR

```text
1. Восстановить head kind — что за вещь стоит за словом.
2. Определить конечные точки и их facets/kinds.
3. Выбрать стабильный lens (n-ary relation, base relation, bridge, span).
4. Заменить зонтичный глагол на явный RelationKind token.
5. Сделать слоты явными: scope, Γ_time, viewpoint, witnesses.
6. Разложить на L/A/D/E (A.6.B).
```

---

## 4. Фермерские примеры

### 4.1 «Ферма связана с переработчиком»

| Шаг | Ремонт |
|---|---|
| head kind | supply contract / milk delivery relation |
| endpoints | FarmA, DairyProcessorB |
| relation kind | `deliversMilkTo` |
| slots | volume (L/day), quality spec, pickup window, bridge to processor context |
| qualifiers | effective window, price formula, penalties |

Правильно:

```text
deliversMilkTo(
  supplier = FarmA,
  receiver = DairyProcessorB,
  productSpec = MilkQuality_SLA_v3,
  volumeSlot = 1200 L/day,
  Γ_time = 2026-01-01..2026-12-31,
  bridge = FarmContext→DairyContext(B-001, CL=low)
)
```

### 4.2 «Данные привязаны к сезону»

| Шаг | Ремонт |
|---|---|
| head kind | measurement series |
| relation kind | `validForSeason` или `sampledInSeason` |
| slots | datasetRef, seasonRef, weather window, grazing regime |

Правильно:

```text
validForSeason(
  dataset = PastureYield_2026,
  season  = GrazingSeason_2026_North,
  Γ_time  = 2026-05-01..2026-10-15,
  witnesses = {satelliteimagery#12, fieldlog#45}
)
```

---

## 5. Candidate-Set Note

Если конечная точка неоднозначна, запишите:

```text
CandidateSetNote:
  triggerSpan: "у них"
  role: endpointRef(p2)
  candidates:
    - Coop_DairyNorth
    - Processor_B
    - RegionalLab_C
  selected: Processor_B
  why: contract reference #2026-044
  consequence: use deliversMilkTo, add contractRef slot
```

---

## 6. Контрольный чеклист

- `CC-A.6P.1`: зонтичный глагол заменён на явный `RelationKind` token.
- `CC-A.6P.2`: все participant/qualifier slots явны (`SlotKind`, `ValueKind`, `RefKind`).
- `CC-A.6P.3`: метонимические или местоименные endpoints восстановлены.
- `CC-A.6P.4`: scope, `Γ_time`, viewpoint и witnesses указаны, если нужны для решения.
- `CC-A.6P.5`: cross-context relation использует Bridge + CL (F.9).
- `CC-A.6P.6`: semantic change class явна (`retarget`, `revise`, `rescope`, `retime`, `refreshWitnesses`).

---

## 7. Связи

- **A.6 Signature Stack** — L/A/D/E раскладка.
- **A.6.B Boundary Norm Square** — классификация claims.
- **A.6.6 Structured Witnessed Base Declaration** — для basedness/anchored.
- **A.6.5 Relation Slot Discipline** — SlotKind/ValueKind/RefKind.
- **A.10 Evidence Graph Referring** — witnesses.
- **F.9 Bridges** — cross-context relations.
- **F.18 Naming** — mint-or-reuse RelationKind tokens.

---

*Capture написан по FPF-Spec.md §A.6.P для PACK-cattle-science.*
