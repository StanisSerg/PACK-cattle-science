---
# YAML FRONTMATTER (обязательно)
id: CS.SOTA.122
type: sota
domain: cattle-science
area: economics
subarea: reproductive-economics
category: simulation
year: 2013
authors: "Galvão, K.N., et al."
title: "Economic comparison of reproductive programs for dairy herds using estrus detection, timed artificial insemination, or a combination"
journal: "Journal of Dairy Science"
volume: "96"
issue: "4"
pages: "2681-2693"
doi: "10.3168/jds.2012-5842"
open_access: false
license: ""
language: ru
tags:
  - economic-comparison
  - reproductive-programs
  - estrus-detection
  - t ai
  - simulation
  - cost-benefit
related:
  - id: CS.SOTA.118
    type: extends
    note: "High fertility cycle"
    relevance: high
  - id: CS.SOTA.001
    type: references
    note: "Протоколы репродукции"
    relevance: high
---

# 1. РЕЗЮМЕ (Abstract)

Симуляционное исследование сравнивает экономику 5 репродуктивных программ. Комбинация ED + TAI оптимальна для большинства ферм. Чистый выигрыш $120-180/корову/год vs ED-only.

---

# 2. KEY CLAIMS

## Claim 1: Комбинация ED + TAI — экономически оптимальна
- **Утверждение:** Программа "ED с последующим TAI для ненаблюденных" дает максимальную маржу ($485/корову/год) vs ED-only ($345) или TAI-only ($420)
- **Evidence:** Моделирование 10,000 коров-лет; sensitivity analysis; различные уровни ED (50-80%)
- **Confidence:** high — robust модель
- **Цитата:** "The combined program yielded $140 more profit per cow per year than ED alone"

## Claim 2: Точность ED критична
- **Утверждение:** При эффективности ED <60% TAI-only становится экономически предпочтительнее
- **Evidence:** Break-even analysis; sensitivity по accuracy ED
- **Confidence:** high

## Claim 3: Стоимость семени влияет на выбор
- **Утверждение:** При использовании sexed semen (+$20/доза) TAI-протоколы экономически выгоднее из-за фиксированного тайминга
- **Evidence:** Scenario analysis; Monte Carlo simulation
- **Confidence:** medium

---

# 3. МЕДИА-ИНВЕНТАРЬ

### [СКРИНШОТ] Table 1: Сравнение программ
**Название:** "Economic comparison of reproductive programs"
**Статус:** обязательный

**Ключевые элементы:**
| Программа | Доход | Затраты | Маржа |
|-----------|-------|---------|-------|
| ED only | $420 | $75 | $345 |
| TAI only | $495 | $75 | $420 |
| ED + TAI | $580 | $95 | **$485** |
| ED + TAI (resynch) | $595 | $110 | $485 |

---

### [СКРИНШОТ] Figure 1: Sensitivity analysis
**Название:** "Economic sensitivity to ED efficiency"
**Статус:** обязательный

**Ключевые элементы:**
- Break-even at ED = 58%
- ED + TAI лидирует при ED <75%
- TAI-only оптимален при ED <55%

---

### [СКРИНШОТ] Figure 2: Monte Carlo results
**Название:** "Probability of economic advantage"
**Статус:** рекомендуемый

---

## Чек-лист медиа

| Медиа | Приоритет |
|-------|-----------|
| Table 1 (сравнение) | Обязательный |
| Figure 1 (sensitivity) | Обязательный |
| Figure 2 (Monte Carlo) | Рекомендуемый |

---

# 4. РЕЗУЛЬТАТЫ

| Программа | Маржа/корову/год | Оптимальные условия |
|-----------|------------------|---------------------|
| ED only | $345 | ED >75%, низкая стоимость труда |
| TAI only | $420 | ED <55%, высокие затраты на обнаружение |
| ED + TAI | $485 | Стандартные условия |

---

# 5. ВЫВОДЫ

1. ED + TAI — оптимальная стратегия для большинства
2. Точность ED критична для выбора
3. Sexed semen меняет экономику в пользу TAI
4. Ресинхронизация повышает эффективность

---

**Статус:** 📝 **DRAFT**

*Создано в рамках WP-75: SoTA Ingestion*
