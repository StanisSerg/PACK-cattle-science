---
type: fpf-study
pattern: A.19
title: "CharacteristicSpace & Dynamics Hook: пространство состояний"
domain: cattle-science
difficulty: advanced
reading_time: 60 min
created: 2026-06-19
---

# A.19 — CharacteristicSpace & Dynamics Hook

## 1. Зачем это читать

Если вы строите модель коровы, стада, фермы или кормового рациона, вам нужно объявить, по каким измерениям эта система меняется. A.19 требует явного `CharacteristicSpace`: набор слотов `(Characteristic, Scale)`, в котором движется модель.

**FPF-тезис:** *«Состояние — это не «параметры». Это координата в объявленном CharacteristicSpace.»*

---

## 2. U.CharacteristicSpace

CharacteristicSpace — конечное произведение slot value sets:

```text
CS = ∏ ValueSet(slot_i)
slot_i = (Characteristic_i, Scale_i)
```

Каждый slot:

- связывает ровно один `Characteristic` с ровно одним `Scale`;
- имеет стабильный identifier (basis);
- сохраняет arity (entity vs relation);
- объявляет `admissible_domain` и missingness semantics.

---

## 3. Dynamics hook

`U.Dynamics.stateSpace` **SHALL** указывать на declared `CharacteristicSpace`. Это typing requirement: все состояния и траектории модели лежат в этом пространстве.

Сам закон динамики (time base, transition law) — в **A.3.3 U.Dynamics**. A.19 задаёт только контейнер состояний.

---

## 4. Операции над пространствами

| Оператор | Что делает | Пример |
|---|---|---|
| **Sub / Projection** | Выбросить часть слотов | Модель здоровья без экономических слотов |
| **Emb / Embedding** | Вложить одно пространство в другое | Перевести кг в фунты через NormalizationMethod |
| **Prod / Product** | Объединить два пространства | Здоровье ⊗ экономика ⊗ погода |
| **Quot / Quotient** | Факторизация по ≡_UNM | Сравнение после нормализации |

**Cross-context:** любое embedding/compare через контекст требует Alignment Bridge (F.9) с CL.

---

## 5. Два режима сравнимости

### 5.1 Coordinatewise (`≼_coord`)

Допустимо только если:

- одно и то же `CharacteristicSpace` (same slots, same definitions);
- identical scale metadata (type, unit, polarity);
- same state-definition criteria.

### 5.2 Normalization-based (`≼_normalization`)

Если состояния в разных пространствах:

1. Применить declared `NormalizationMethodInstance` (A.19.UNM).
2. Сравнить в общем пространстве через `≼_coord`.

> Никогда не сравнивайте raw coordinates напрямую.

---

## 6. Optional overlays

Пространство по умолчанию — просто Cartesian product. Дополнительная структура объявляется явно:

- **order overlay** — product order для dominance/Pareto reasoning;
- **topology** — для continuity/limits;
- **metric / distance** — для distance-based acceptance.

Если используется distance overlay, acceptance predicates должны быть non-expansive (Lipschitz ≤ 1) или объявить margin.

---

## 7. Фермерский пример: пространство здоровья стада

```text
CharacteristicSpace: HerdHealth_CS_v1
  slots:
    - (BHB, ratio, mmol/L, ↓ better)
    - (SCC, ratio, cells/ml, ↓ better)
    - (BodyWeight, ratio, kg)
    - (LamenessScore, ordinal, {None, Mild, Severe}, ↓ better)
    - (DistanceToWater, relation, m)

state: Cow#401@2026-06-19T08:00 =
  (BHB=1.1, SCC=180k, BodyWeight=612, LamenessScore=None, DistanceToWater=250)
```

Checklist для состояния `Healthy`:

```text
BHB < 1.2 AND SCC < 200k AND LamenessScore = None
```

---

## 8. Контрольный чеклист

- `CC-A.19.1`: space объявлен через basis слотов `(Characteristic, Scale)`.
- `CC-A.19.2`: каждый slot привязан ровно к одному Characteristic и одному Scale.
- `CC-A.19.3`: meaning slot не меняется ретроактивно; версионируется.
- `CC-A.19.4`: relation Characteristics сохраняют arity.
- `CC-A.19.5`: внутри space нет скрытых normalizations/aggregations.
- `CC-A.19.6`: `U.Dynamics.stateSpace` ссылается на declared space.
- `CC-A.19.7`: cross-context compare использует Bridge + CL.
- `CC-A.19.8`: equality/joins — на invariant forms (quotient/NormalizationFix), не на raw coordinates.
- `CC-A.19.9`: distance overlay non-expansive или с margin.

---

## 9. Связи

- **A.17 Characteristic** — vocabulary.
- **A.18 CSLC** — scale/coordinate discipline.
- **A.3.3 U.Dynamics** — dynamic laws over CharacteristicSpace.
- **A.2.5 RoleStateGraph** — state certification via checklist.
- **A.19.UNM** — normalization methods.
- **F.9 Bridges** — cross-context mappings.
- **B.3 Trust Framework** — Φ(CL) penalties.

---

*Capture написан по FPF-Spec.md §A.19 для PACK-cattle-science.*
