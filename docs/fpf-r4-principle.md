# Принцип R4 — CL Routing (FPF)

> **Источник:** FPF-Spec.md, раздел C.23 (Method-SoS-LOG), строка 36862  
> **Тип:** Правило исполняемого слоя логики выбора методов  
> **Статус:** Normative

---

## Суть R4

**R4 — CL routing.** Любое повторное использование через Context/plane **обязано** ссылаться на **Bridge ids** (с примечаниями о потерях). Применять **Φ(CL)** и (если плоскости различаются) **Φ_plane**, которые являются **монотонными, ограниченными, таблично-закреплёнными**; **публиковать policy-ids** в SCR; **штрафы идут только в `R_eff`**; **F/G инвариантны**.

---

## Что это означает на человеческом

Когда два метода (или две Tradition) говорят разное, система не должна:
1. Молча выбрать одно и игнорировать другое
2. Усреднить ответы
3. Сказать «всё нормально» без объяснения

Вместо этого система должна:
1. **Знать**, что они из разных контекстов
2. **Знать**, насколько они совместимы (CL — Congruence Level)
3. **Применить штраф** к доверию (R_eff = R_base × Φ(CL))
4. **Сохранить** суть каждого метода (F/G не меняются)

---

## Где в FPF находится R4

В FPF есть несколько принципов с меткой **R4**:

| R4 | Где в FPF | Суть |
|----|-----------|------|
| **C.23 R4 — CL routing** | Раздел C.23 (Method-SoS-LOG) | Любое cross-Context/plane reuse **обязано** ссылаться на Bridge ids с loss notes. Применять Φ(CL) и Φ_plane; policy-ids публикуются в SCR; штрафы идут только в `R_eff`; **F/G инвариантны**. |
| **F.12 R4 — Bridge rule** | Раздел F.12 (KD-CAL) | Если Clause, Work и Measure живут в разных Contexts — применять declared Bridges с kind, CL и loss notes. |
| **F.18 R4 — Local-Sense** | Раздел F.18 (UTS Naming) | Имя должно разрешаться в Local-Sense внутри своего Context. |

Для работы с BridgeMatrix в G.2 наиболее релевантен **C.23 R4 — CL routing**.

---

## Применение R4 к BridgeMatrix (PACK-cattle-science)

Сейчас в `G2-SoTA-Synthesis-Pack.md` BridgeMatrix записывает *что* расходится (scale conflict, temporal gap, feed-to-yield gap), но не фиксирует **Bridge ids**, **CL-уровни**, **Φ-политики** и **маршрут штрафов**. R4 требует это явно закрепить.

### Crossing 1: T1 ↔ T2 (Пороги vs Групповое управление)

```yaml
BridgeId: CS.BRIDGE.T1-T2-SCALE-001
Kind: scale_mismatch
Crossing: T1 (individual threshold) → T2 (group deviation)

CL (Congruence Level):
  - scope_CL: 1  # Понятия "BHB" совпадают, но масштаб применения различен
  - kind_CL: 2   # Характеристика та же, но оператор разный (individual vs group_mean)

Φ(CL) policy:
  PolicyId: CS.POLICY.PHI-T1T2-v1
  Table:
    - CL=1 → Φ(CL)=0.85
    - CL=2 → Φ(CL)=0.70
  Monotone: true
  Bounded: [0.5, 1.0]

Φ_plane:
  # ReferencePlane одинаковая (enterprise data), поэтому Φ_plane не применяется
  PolicyId: null

Loss notes:
  - "T1 оптимизирован для клинического действия (recall individual); T2 — для раннего группового сигнала. Пересечение масштабов ведёт к потере точности на уровне индивидуума при групповой агрегации."

R_eff routing:
  - R_base (T1): 0.75 (medium confidence)
  - R_base (T2): 0.55 (low confidence — group model v1.0 conceptual)
  - R_eff_T1→T2: R_base_T1 * Φ(CL=1) = 0.75 * 0.85 = 0.638
  - R_eff_T2→T1: R_base_T2 * Φ(CL=2) = 0.55 * 0.70 = 0.385

F/G invariant check:
  - F (ClaimScope): не изменён; T1 и T2 остаются disjoint ClaimSheets
  - G (Coverage): не изменён; групповое покрытие ≠ индивидуальное покрытие
```

### Crossing 2: T1 ↔ T3 (Точечный порог vs Траектория MilkBot)

```yaml
BridgeId: CS.BRIDGE.T1-T3-TEMPORAL-001
Kind: temporal_mismatch
Crossing: T1 (single-point BHB) → T3 (MilkBot trajectory)

CL:
  - scope_CL: 2  # BHB как характеристика общая, но temporal window различается
  - kind_CL: 3   # Разные виды измерения: point vs curve derivative

Φ(CL) policy:
  PolicyId: CS.POLICY.PHI-T1T3-v1
  Table:
    - CL=2 → Φ(CL)=0.75
    - CL=3 → Φ(CL)=0.55
  Monotone: true
  Bounded: [0.4, 1.0]

Loss notes:
  - "T1 использует единичное измерение BHB; T3 использует динамику M305 как прокси. Потеря: T1 не видит траектории; T3 не видит острого метаболического кризиса."

R_eff routing:
  - R_base_T1: 0.75
  - R_base_T3: 0.60 (MilkBot curve — medium confidence)
  - R_eff_T1→T3: 0.75 * 0.75 = 0.563
  - R_eff_T3→T1: 0.60 * 0.55 = 0.330

F/G invariant check:
  - F: не изменён; point measurement ≠ trajectory model
  - G: не изменён; coverage разных DIM-окон не смешивается
```

### Crossing 3: T3 ↔ T4 (MilkBot vs NASEM нормы)

```yaml
BridgeId: CS.BRIDGE.T3-T4-ATTRIBUTION-001
Kind: attribution_gap
Crossing: T3 (actual yield / predictive) → T4 (normative requirement)

CL:
  - scope_CL: 2  # "Продуктивность" общая область
  - kind_CL: 3   # Predictive/descriptive vs Normative/prescriptive
  - plane_CL: 2  # Разные ReferencePlane: actual farm vs NASEM reference population

Φ(CL) policy:
  PolicyId: CS.POLICY.PHI-T3T4-v1
  Table:
    - CL=2 → Φ(CL)=0.70
    - CL=3 → Φ(CL)=0.50

Φ_plane policy:
  PolicyId: CS.POLICY.PHI-PLANE-FARM-NASEM-v1
  Table:
    - plane_CL=2 → Φ_plane=0.80
  Monotone: true
  Bounded: [0.6, 1.0]

Loss notes:
  - "T3 описывает 'что есть' (фактическая M305, MilkBot-кривая). T4 предписывает 'что должно быть' (NASEM нормы). Потеря: разрыв 'кормление–продуктивность' невозможно закрыть без причинной модели."

R_eff routing:
  - R_base_T3: 0.60
  - R_base_T4: 0.85 (NASEM high confidence)
  - R_eff_T3→T4: 0.60 * Φ(CL=2) * Φ_plane(2) = 0.60 * 0.70 * 0.80 = 0.336
  - R_eff_T4→T3: 0.85 * Φ(CL=3) * Φ_plane(2) = 0.85 * 0.50 * 0.80 = 0.340

F/G invariant check:
  - F: не изменён; descriptive ≠ prescriptive
  - G: не изменён; farm-level coverage ≠ reference-population coverage
```

---

## Что нужно добавить в G.2-пакет для соответствия R4

1. **BridgeMatrix** дополнить колонками: `BridgeId`, `CL`, `Φ(CL) policy-id`, `Φ_plane policy-id`, `R_eff`.
2. **SCR visibility:** добавить раздел `SCR-visibility` (Selector Conformance Report), где перечислены все policy-ids и их таблицы Φ.
3. **Проверка инвариантности F/G:** для каждого crossing явно записать, что F (ClaimScope) и G (Coverage) не были перезаписаны.

---

*Создано: 2026-04-18 в ходе сессии применения FPF к PACK-cattle-science.*
