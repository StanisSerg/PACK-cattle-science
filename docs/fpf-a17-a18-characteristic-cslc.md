---
type: fpf-study
pattern: A.17–A.18
title: "Characteristic & CSLC: измерять правильно"
domain: cattle-science
difficulty: advanced
reading_time: 50 min
created: 2026-06-19
---

# A.17–A.18 — Canonical Characteristic & Minimal CSLC

## 1. Зачем это читать

«Средний балл риска 3.2», «корова оценена как 4», «BHB = 1.4» — цифры ничего не значат без явного ответа: *измерение чего, по какой шкале, какой полярности*. A.17 фиксирует термин Characteristic. A.18 задаёт CSLC: Characteristic → Scale → Level → Coordinate.

**FPF-тезис:** *«Никаких голых чисел. Каждая координата несёт с собой Characteristic, Scale и Unit.»*

---

## 2. A.17 — Canonical Characteristic

**Characteristic** — единый термин для «что измеряем». Заменяет «axis», «dimension», «property», «feature», «metric».

### Arity

| Вид | Применяется к | Пример |
|---|---|---|
| **EntityCharacteristic** | Ровно одному bearer | Масса коровы, температура двигателя |
| **RelationCharacteristic** | Tuple из ≥2 bearers | Расстояние между коровами, coupling между модулями |

### Лексические запреты

В normative тексте запрещены: axis, dimension, metric, grade, property как синонимы. Используйте Characteristic, Scale, Level, Value, Coordinate, Score, ScoringMethod, Unit.

---

## 3. A.18 — CSLC clause

> **Exactly one Characteristic + exactly one Scale ⇒ one Coordinate, with an optional Level.**

| Элемент | Отвечает на | Пример |
|---|---|---|
| **Characteristic** | Что измеряем? | Body Weight |
| **Scale** | Как измеряем? | ratio scale, kg, 0..1500 |
| **Coordinate** | Что получилось? | 612 kg |
| **Level** | Именованный tier (опционально) | Good / Fair / Poor |

---

## 4. Scale types и допустимые операции

| Scale | Что можно | Чего нельзя |
|---|---|---|
| **Nominal** | проверять равенство | сравнивать порядок |
| **Ordinal** | ранжировать | усреднять, вычитать |
| **Interval** | +/- | говорить «в два раза больше» без true zero |
| **Ratio** | все арифметические операции | смешивать units |

### Polarity

Каждая ordered scale объявляет:

- `↑ better` — больше лучше (например, молочная продуктивность);
- `↓ better` — меньше лучше (например, соматические клетки);
- `targeted optimum` — оптимум вокруг целевого значения (например, pH рубца).

---

## 5. Фермерские примеры

### 5.1 Вес коровы

```text
Characteristic: BodyWeight
Scale: ratio, kg, 0..1500
Coordinate: 612 kg
```

Допустимо: «на 50 kg тяжелее», «средний вес группы 620 kg».

### 5.2 Оценка состояния коровы (BCS)

```text
Characteristic: BodyConditionScore
Scale: ordinal, levels {Thin, Moderate, Fat}
Coordinate: Moderate
```

Недопустимо: «средний BCS = 2.3» (если уровни не равноотстоящие).

### 5.3 Качество силоса

```text
Characteristic: SilageQuality
Scale: ordinal, levels {Poor, Fair, Good, Excellent}
Coordinate: Good
```

### 5.4 Расстояние до водопоя

```text
Characteristic: DistanceToWater
Scale: ratio, m
Coordinate: 250 m
RelationCharacteristic: applies to (pasture, waterPoint)
```

---

## 6. Составные scores

Нельзя складывать координаты разных Characteristics напрямую. Если нужен общий score — объявите явный `ScoringMethod` (𝒢) с:

- declared monotonicity;
- bounded output range;
- weights / formula;
- evidence.

```text
Composite: HerdHealthIndex
  inputs:
    - BHB (ratio, ↓ better)
    - SCC (ratio, ↓ better)
    - BCS (ordinal)
  ScoringMethod: weighted monotone map to 0..100
```

---

## 7. Контрольный чеклист

- `CC-A.17.1`: measured aspect назван `Characteristic`.
- `CC-A.17.2`: arity явна — entity или relation.
- `CC-A.18.1`: один metric template = один Characteristic + один Scale.
- `CC-A.18.2`: polarity объявлена для ordered scales.
- `CC-A.18.3`: unit и level ясны; unit не в имени Characteristic.
- `CC-A.18.4`: операции scale-appropriate.
- `CC-A.18.5`: нет голых чисел — каждая coordinate подписана.
- `CC-A.18.6`: cross-metric aggregation только через declared ScoringMethod.
- `CC-A.18.7`: Level используется осознанно или не используется.

---

## 8. Связи

- **A.17** — canonical term и arity.
- **A.18** — CSLC structure.
- **A.19 CharacteristicSpace** — пространство из Characteristics.
- **A.3.3 U.Dynamics** — state space как CharacteristicSpace.
- **C.16 Measurement & Evidence** — метрология и evidence.
- **G.3 CHR Authoring** — создание characteristic packs.
- **B.3 Trust Framework** — aggregation penalties.

---

*Capture написан по FPF-Spec.md §A.17–A.18 для PACK-cattle-science.*
