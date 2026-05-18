---
id: CS.METHOD.005
name: "Оценка уровня кальция и профилактика гипокальцемии в переходный период"
status: active
summary: "Системный мониторинг кальция и метаболических маркеров у коров в переходный период (3 недели до — 3 недели после отёла) с целью раннего выявления риска гипокальцемии и применения превентивных мер."
sota: current
created: 2026-05-18
last_updated: 2026-05-18
related:
  produces:
    - CS.WP.002
    - CS.WP.005
  uses:
    - CS.ENTITY.103
    - CS.ENTITY.104
    - CS.ENTITY.041
    - CS.ENTITY.098
  fails_with:
    - CS.FM.002
  requires_role:
    - CS.ROLE.001
    - CS.ROLE.005
  precedes:
    - CS.METHOD.002
  follows: []
tags:
  - transition-period
  - calcium
  - hypocalcemia
  - monitoring
  - prevention
  - metabolic-health
  - subclinical
---

## [CS.METHOD.005] Оценка уровня кальция и профилактика гипокальцемии в переходный период

### Definition

Систематический метод оценки метаболического статуса коров в переходный период с фокусом на динамику кальция, выявление субклинических нарушений и применение превентивных мер до развития клинической гипокальцемии.

Метод охватывает период с 21 дня до отёла (dry-off / close-up) по 21 день после отёла (fresh cow), интегрируя лабораторную диагностику, поведенческие маркеры и управленческие решения.

### Purpose

- **Раннее выявление** субклинической гипокальцемии (SCH) до появления клинических признаков
- **Стратификация риска** — определение групп коров с высоким/низким риском по фенотипам Graef 2025
- **Превентивное вмешательство** — применение DCAD, витамина D, перорального Ca до кризиса
- **Снижение каскадных потерь** — предотвращение вторичных осложнений (DAb, мастит, метрит, ketosis)
- **Оптимизация репродуктивных показателей** — минимизация влияния метаболического стресса на фертильность

### Inputs

| Input | Description | Required? | Source |
|-------|-------------|-----------|--------|
| tCa (1 DIM) | Общий кальций крови в 1-й день после отёла | Yes | Лаборатория / портативный анализатор |
| tCa (5 DIM) | Общий кальций крови в 5-й день после отёла | Yes | Лаборатория / портативный анализатор |
| iCa (опционально) | Ионизированный кальций (более точный маркер) | No | Лаборатория |
| BCS при отёле | Оценка упитанности по 5-балльной шкале | Yes | Зоотехник / визуальная оценка |
| Парность | Примипара / мультипара | Yes | Учётная система |
| Молочная продуктивность | Ожидаемый удой (M305, пиковый) | Yes | Учётная система |
| История заболеваний | Перенесённые гипокальцемия, DAb, мастит | Yes | Ветеринарные записи |
| pH мочи | Контроль эффективности анионных солей | No (при DCAD) | Тест-полоски |
| FTIR-данные (опционально) | Предиктивные маркеры из анализа молока | No | Лаборатория молока |
| Hp / SAA (опционально) | Воспалительные маркеры для уточнения прогноза | No | Лаборатория |

### Outputs (Work Products)

| Output | Link | Description |
|--------|------|-------------|
| CS.WP.002 | [Отчёт о продуктивности и метаболическом статусе](../04-work-products/CS.WP.002-productivity-performance-report.md) | Групповой отчёт по стаду: доли фенотипов SCH, динамика tCa |
| CS.WP.005 | [Оценка риска здоровье-фертильность](../04-work-products/CS.WP.005-health-fertility-risk-assessment.md) | Индивидуальная карта риска с рекомендациями по менеджменту |

### Roles Involved

| Role | Responsibility in This Method |
|------|------------------------------|
| [Veterinarian (Ветеринар)](../02-domain-entities/02A-roles.md#veterinarian) | R/A — назначение протокола мониторинга, интерпретация результатов, корректировка профилактики |
| [Herd Manager (Заведующий стадом)](../02-domain-entities/02A-roles.md#herd-manager) | A — организация отбора проб, контроль графика, принятие управленческих решений |
| [Dairy Nutritionist (Нутрициолог)](../02-domain-entities/02A-roles.md#dairy-nutritionist) | C — корректировка DCAD, рационов close-up / fresh cow |
| [Breeding Manager](../02-domain-entities/02A-roles.md#breeding-manager) | I — учёт связи метаболического статуса с репродуктивными показателями |

### Related Methods

| Method | Relationship |
|--------|-------------|
| [CS.METHOD.002](./CS.METHOD.002-hypocalcemia-diagnosis-treatment.md) | follows — при выявлении клинической гипокальцемии переход к протоколу лечения |
| [CS.METHOD.001](./CS.METHOD.001-ketosis-diagnosis-treatment.md) | parallel — часто сопутствующий метаболический нарушение, совместный мониторинг |
| [CS.METHOD.003](./CS.METHOD.003-reproductive-program-evaluation.md) | precedes — репродуктивные показатели зависят от метаболического статуса в transition |
| [CS.METHOD.020](../02-domain-entities/02C-methods-index.md#csmethod020) | alternative — более широкий мониторинг переходного периода (NEFA, BHB, BCS) |

### Key Distinctions

- **tCa vs iCa:** Общий кальций (tCa) включает белок-связанную фракцию и доступен в большинстве лабораторий. Ионизированный кальций (iCa) — биологически активная фракция, более точен, но требует специального оборудования. Пороги SCH различаются.
- **SCH vs клиническая гипокальцемия:** Субклиническая форма (tCa ≤2.0 mmol/L) не имеет видимых признаков, но ассоциирована с осложнениями. Клиническая форма (tCa <1.95 mmol/L + paresis/recumbency) — неотложное состояние.
- **Профилактика vs лечение:** Профилактика — меры до отёла (DCAD, витамин D, Ca-болюсы). Лечение — медицинское вмешательство при диагностированном нарушении.
- **NC vs tSCH vs dSCH vs pSCH:** Четыре фенотипа по динамике tCa (1 DIM / 5 DIM), определяющие тактику менеджмента.

### Failure Modes

| Failure Mode | Link | Description |
|--------------|------|-------------|
| Позднее выявление | [CS.FM.002](../05-failure-modes/CS.FM.002-late-hypocalcemia-detection.md) | Мониторинг начинается после появления клинических признаков или вообще отсутствует |
| Неправильные пороги | [CS.FM.003](../05-failure-modes/CS.FM.003-incorrect-calcium-thresholds.md) | Использование устаревших или невалидированных для породы/региона порогов tCa |
| Игнорирование SCH | [CS.FM.004](../05-failure-modes/CS.FM.004-sch-ignored.md) | Отсутствие действий при выявлении субклинической формы («не болеет, значит не лечим») |
| Неконтролируемый DCAD | [CS.FM.005](../05-failure-modes/CS.FM.005-uncontrolled-dcad.md) | Применение анионных солей без контроля pH мочи → ацидоз или недостаточный эффект |
| Фрагментарный мониторинг | [CS.FM.006](../05-failure-modes/CS.FM.006-fragmented-monitoring.md) | Измерение tCa только в 1 DIM без динамики в 5 DIM — упущенные фенотипы dSCH/pSCH |

### Tools Commonly Used

| Tool | How Used |
|------|---------|
| Портативный анализатор Ca (i-STAT, VetScan) | Экспресс-диагностика tCa / iCa в хозяйстве, результат за 2 минуты |
| Precision Xtra / Nova Vet | Портативный BHB + tCa (комбинированный скрининг) |
| FTIR-анализатор молока | Предиктивная модель риска SCH (Lin 2025, AUROC 0.70–0.76) |
| Тест-полоски pH мочи | Контроль эффективности DCAD (цель pH 6.0–6.5) |
| RumiWatch / CowManager | Мониторинг жвачки и активности — косвенные маркеры метаболического стресса |
| CRM / учётная система | Регистрация DIM, парности, истории, продуктивности |

### SoTA Status

**Status:** `current`

**Basis:**
- **Graef et al. 2025** (CS.SOTA.066) — фенотипирование SCH по динамике tCa (1 DIM / 5 DIM), 4 фенотипа (NC, tSCH, dSCH, pSCH), ассоциация с воспалительными маркерами.
- **Lin et al. 2025** (CS.SOTA.067) — FTIR + ML для предикции SCH, AUROC 0.70–0.76.
- **Bruinjé et al. 2024** (CS.SOTA.020) — связь послеродового здоровья с эндокринной сигнализацией и репродуктивными показателями.
- **Bradford et al. 2023** (CS.SOTA.053) — HPA-ось и иммуносупрессия в transition period.
- **NASEM 2021** (CS.SOTA.300–312) — нутриционные требования и DCAD-протоколы.

**Revision criterion:**
- Появление новых предиктивных моделей с AUROC >0.85
- Валидация фенотипов Graef 2025 на независимых популяциях (Jersey, crossbreed, различные регионы)
- Изменение рекомендаций NASEM по порогам Ca

---

## Algorithm: Transition Calcium Monitoring Protocol

### Phase 1: Risk Stratification (Pre-calving, -21 to 0 DIM)

**Step 1.1: Identify high-risk cows**

| Risk Factor | Weight | Action |
|-------------|--------|--------|
| Multiparous (≥2 lactations) | High | Mandatory monitoring |
| Previous hypocalcemia / SCH | High | Mandatory monitoring + aggressive prevention |
| BCS >3.75 or <3.0 at dry-off | High | Nutritional correction + monitoring |
| Expected peak milk >45 kg | Medium | Standard monitoring |
| Seasonal risk (winter housing) | Medium | Increase prevention intensity |

**Step 1.2: Implement prevention measures**

| Measure | Timing | Target | Control |
|---------|--------|--------|---------|
| DCAD adjustment | -21 to 0 DIM | 0–150 mEq/kg | pH urine 6.0–6.5 |
| Vitamin D₃ or 25-OH-D₃ | -10 to -7 DIM | 10–20M IU D₃ or 3–5 mg 25-OH-D₃ | None (dose-based) |
| Oral Ca supplementation | -2 to +2 DIM | 50–100 g Ca/day | None (protocol-based) |
| Ca bolus at calving | 0 DIM (immediately after) | 1 bolus (≈43 g Ca) | Observation for 4h |

### Phase 2: Active Monitoring (Post-calving, 1–7 DIM)

**Step 2.1: Sample collection schedule**

| Day | Sample | Priority |
|-----|--------|----------|
| 1 DIM | tCa + iCa (if available) | **Mandatory** |
| 3 DIM | Visual assessment + behavior | Standard |
| 5 DIM | tCa + Hp/SAA (optional) | **Mandatory** |
| 7 DIM | tCa (for dSCH/pSCH follow-up) | Conditional |

**Step 2.2: Phenotype classification (Graef 2025)**

| Phenotype | tCa 1 DIM | tCa 5 DIM | Risk | Action |
|-----------|-----------|-----------|------|--------|
| **NC** | >1.95 | >2.32 | Low | Standard monitoring, no extra prevention |
| **tSCH** | ≤1.95 | >2.32 | Medium | Monitor at 7 DIM, consider oral Ca |
| **dSCH** | >1.95 | ≤2.32 | High | Oral Ca 50–100 g/day × 5–7 days, monitor inflammation |
| **pSCH** | ≤1.95 | ≤2.32 | Very High | IV Ca at calving, oral Ca 100 g/day × 7–10 days, intensive monitoring |

### Phase 3: Intervention & Follow-up (5–21 DIM)

**Step 3.1: Phenotype-specific response**

See [CS.METHOD.002](./CS.METHOD.002-hypocalcemia-diagnosis-treatment.md) for clinical treatment protocols.

**Step 3.2: Reproductive impact tracking**

- Link metabolic status to first service conception rate (FSCR)
- Cows with pSCH: delay first AI by 7–14 days if condition not stabilized
- Track days open by phenotypic group

### Phase 4: Herd-level Analysis (Monthly / Quarterly)

**Step 4.1: Aggregate metrics**

| Metric | Target | Action if above target |
|--------|--------|------------------------|
| SCH prevalence (all phenotypes) | <30% | Review DCAD protocol, nutritionist consultation |
| pSCH prevalence | <8% | Aggressive prevention review, vet consultation |
| Clinical hypocalcemia incidence | <2% | Emergency protocol review |
| Average tCa 1 DIM | >2.0 mmol/L | Nutrition / management review |

**Step 4.2: Continuous improvement loop**

1. Collect data → 2. Classify phenotypes → 3. Apply prevention → 4. Measure outcomes → 5. Adjust thresholds/prevention → return to 1.

---

## Checklist Before Committing

- [x] ID follows pattern `CS.METHOD.NNN`
- [x] Definition is declarative
- [x] Outputs link to work product cards
- [x] Failure modes are listed
- [x] SoTA status and revision criterion specified
- [x] Added to `02C-methods-index.md`
- [x] Added to `07-map/` (if applicable)

---

*Created: 2026-05-18 (WP-83 Methods PACK)*
*Last updated: 2026-05-18*
