# Спецификация: Матрица интерпретаций сущностей в SoTA

> **Scope:** P0 (58 сущностей) + P1 (98 сущностей) = 156 сущностей  
> **Формат:** Standard (2-3 строки: роль + контекст)  
> **Структура:** Разбивка по категориям (отдельные файлы)  
> **Источник:** Гибрид (авто-извлечение + ручная доработка)

---

## 1. Структура файлов

```
02-domain-entities/
├── 02B1-interpretations-metabolites.md      # Метаболиты/биомаркеры
├── 02B2-interpretations-diseases.md         # Заболевания/состояния
├── 02B3-interpretations-systems.md          # Биологические системы
├── 02B4-interpretations-hormones.md         # Гормоны/рецепторы
├── 02B5-interpretations-methods.md          # Методы/технологии
├── 02B6-interpretations-metrics.md          # Метрики/показатели
└── 02B7-interpretations-molecular.md        # Молекулярные сущности
```

---

## 2. Шаблон записи сущности

```markdown
## {CS.ENTITY.XXX} — {Название EN} ({Название RU})

| SoTA ID | Автор/Год | Интерпретация | Контекст использования |
|---------|-----------|---------------|------------------------|
| XXX | Author YYYY | [Роль сущности] | [Где/как используется] |
| XXX | Author YYYY | [Роль сущности] | [Где/как используется] |
| ... | ... | ... | ... |

### Синтез
- **Консенсус:** [общее понимание across SoTA]
- **Разногласия:** [где расходятся интерпретации]
- **Эволюция:** [как менялось понимание со временем]

---
```

---

## 3. Распределение сущностей по файлам

### 02B1-interpretations-metabolites.md (P0: 13 + P1: 23 = 36 сущностей)

**P0 — Fundamental:**
- CS.ENTITY.009 — Beta-hydroxybutyrate (BHB)
- CS.ENTITY.010 — Non-esterified fatty acids (NEFA)
- CS.ENTITY.??? — Glucose
- CS.ENTITY.??? — Propionate
- CS.ENTITY.??? — Acetate
- CS.ENTITY.??? — Butyrate
- CS.ENTITY.??? — Lactate
- CS.ENTITY.??? — Urea
- CS.ENTITY.015 — Insulin
- CS.ENTITY.016 — Glucagon
- CS.ENTITY.017 — Cortisol

**P1 — Important:**
- CS.ENTITY.??? — Acylcarnitines
- CS.ENTITY.??? — Phosphatidylcholines
- CS.ENTITY.??? — Sphingomyelins
- CS.ENTITY.??? — Bile acids
- CS.ENTITY.??? — Lysophosphatidylcholine
- CS.ENTITY.??? — Triacylglycerols
- CS.ENTITY.??? — Cholesterol
- CS.ENTITY.??? — Fatty acids
- CS.ENTITY.??? — Palmitic acid
- CS.ENTITY.??? — Oleic acid
- CS.ENTITY.??? — Propylene glycol
- CS.ENTITY.??? — Glycerol
- CS.ENTITY.??? — Acetoacetate
- CS.ENTITY.??? — Acetone
- CS.ENTITY.??? — Amino acids
- CS.ENTITY.??? — Proline
- CS.ENTITY.??? — Glutamine
- CS.ENTITY.??? — Leucine
- CS.ENTITY.??? — Isoleucine
- CS.ENTITY.??? — Valine
- CS.ENTITY.??? — Methionine
- CS.ENTITY.??? — Choline
- CS.ENTITY.??? — Vitamin B12
- CS.ENTITY.??? — Carnitine

---

### 02B2-interpretations-diseases.md (P0: 9 + P1: 8 = 17 сущностей)

**P0 — Fundamental:**
- CS.ENTITY.018 — Ketosis
- CS.ENTITY.002 — Subclinical ketosis
- CS.ENTITY.??? — Fatty liver
- CS.ENTITY.??? — Hypocalcemia
- CS.ENTITY.??? — Mastitis
- CS.ENTITY.??? — Metritis
- CS.ENTITY.??? — Retained placenta
- CS.ENTITY.??? — Displaced abomasum
- CS.ENTITY.??? — Gluconeogenesis

**P1 — Important:**
- CS.ENTITY.??? — Subclinical hypocalcemia
- CS.ENTITY.??? — Clinical hypocalcemia
- CS.ENTITY.??? — Lactic acidosis
- CS.ENTITY.??? — Ruminal acidosis
- CS.ENTITY.??? — Endometritis
- CS.ENTITY.??? — Ovarian cyst
- CS.ENTITY.??? — Anestrus
- CS.ENTITY.??? — Delayed ovulation

---

### 02B3-interpretations-systems.md (P0: 4 + P1: 15 = 19 сущностей)

**P0 — Fundamental:**
- CS.ENTITY.001 — Dairy cow
- CS.ENTITY.003 — Liver
- CS.ENTITY.004 — Rumen
- CS.ENTITY.005 — Adipose tissue
- CS.ENTITY.006 — Milk

**P1 — Important:**
- CS.ENTITY.??? — Ovaries
- CS.ENTITY.??? — Uterus
- CS.ENTITY.??? — Mammary gland
- CS.ENTITY.??? — Pancreas
- CS.ENTITY.??? — Adrenal glands
- CS.ENTITY.??? — Thyroid gland
- CS.ENTITY.??? — HPA axis
- CS.ENTITY.??? — Intestine
- CS.ENTITY.??? — Kidneys
- CS.ENTITY.??? — Muscles
- CS.ENTITY.??? — Bones
- CS.ENTITY.??? — Cardiovascular system
- CS.ENTITY.??? — Immune system
- CS.ENTITY.??? — Nervous system
- CS.ENTITY.??? — Endocrine system

---

### 02B4-interpretations-hormones.md (P0: 0 + P1: 8 = 8 сущностей)

**P1 — Important:**
- CS.ENTITY.??? — Progesterone
- CS.ENTITY.??? — Prolactin
- CS.ENTITY.??? — Growth hormone
- CS.ENTITY.??? — Leptin
- CS.ENTITY.??? — Ghrelin
- CS.ENTITY.??? — IGF-1
- CS.ENTITY.??? — Thyroid hormones
- CS.ENTITY.??? — PPAR receptors

---

### 02B5-interpretations-methods.md (P0: 4 + P1: 9 = 13 сущностей)

**P0 — Fundamental:**
- CS.ENTITY.??? — Artificial insemination (AI)
- CS.ENTITY.??? — Timed AI (TAI)
- CS.ENTITY.??? — CIDR protocol
- CS.ENTITY.??? — Heat detection

**P1 — Important:**
- CS.ENTITY.??? — Embryo transfer
- CS.ENTITY.??? — Prostaglandin injection
- CS.ENTITY.??? — GnRH
- CS.ENTITY.??? — Ovarian ultrasonography
- CS.ENTITY.??? — Pregnancy test
- CS.ENTITY.??? — FTIR spectroscopy
- CS.ENTITY.??? — Metabolomics
- CS.ENTITY.??? — Lipidomics
- CS.ENTITY.??? — Machine learning

---

### 02B6-interpretations-metrics.md (P0: 6 + P1: 12 = 18 сущностей)

**P0 — Fundamental:**
- CS.ENTITY.001 — 21-day pregnancy rate
- CS.ENTITY.??? — Body condition score (BCS)
- CS.ENTITY.??? — Dry matter intake (DMI)
- CS.ENTITY.??? — Milk yield
- CS.ENTITY.??? — Milk fat
- CS.ENTITY.??? — Milk protein

**P1 — Important:**
- CS.ENTITY.??? — Insemination eligibility period
- CS.ENTITY.??? — Voluntary waiting period
- CS.ENTITY.??? — Days open
- CS.ENTITY.??? — Calving interval
- CS.ENTITY.??? — Gestation length
- CS.ENTITY.??? — Herd turnover rate
- CS.ENTITY.??? — Replacement rate
- CS.ENTITY.??? — Body temperature
- CS.ENTITY.??? — Activity
- CS.ENTITY.??? — Rumination time
- CS.ENTITY.??? — Feeding time
- CS.ENTITY.??? — Lying time

---

### 02B7-interpretations-molecular.md (P0: 0 + P1: 37 = 37 сущностей)

**P1 — Important:**
- CS.ENTITY.??? — Mitochondria
- CS.ENTITY.??? — Peroxisomes
- CS.ENTITY.??? — Cytoplasmic lipid droplets
- CS.ENTITY.??? — Cell membrane
- CS.ENTITY.??? — Ribosomes
- CS.ENTITY.??? — Lysosomes
- CS.ENTITY.??? — Smooth ER
- CS.ENTITY.??? — Acetyl-CoA
- CS.ENTITY.??? — Malonyl-CoA
- CS.ENTITY.??? — Pyruvate
- CS.ENTITY.??? — Oxaloacetate
- CS.ENTITY.??? — Phosphoenolpyruvate
- CS.ENTITY.??? — Glucose-6-phosphate
- CS.ENTITY.??? — Fructose-1,6-bisphosphate
- CS.ENTITY.??? — Glyceraldehyde-3-phosphate
- CS.ENTITY.??? — Dihydroxyacetone phosphate
- CS.ENTITY.??? — Haptoglobin
- CS.ENTITY.??? — Serum amyloid A
- CS.ENTITY.??? — TNF-alpha
- CS.ENTITY.??? — IL-6
- CS.ENTITY.??? — IL-10
- CS.ENTITY.??? — IFN-gamma
- [+ 16 молекулярных из P2 если нужно]

---

### 02B8-interpretations-periods.md (P0: 4 + P1: 0 = 4 сущностей)

**P0 — Fundamental:**
- CS.ENTITY.??? — Transition period
- CS.ENTITY.??? — Dry period
- CS.ENTITY.??? — Early lactation
- CS.ENTITY.??? — Periparturient period

---

## 4. Процесс заполнения

### Шаг 1: Авто-извлечение (скрипт)
- Парсинг всех SoTA-файлов
- Поиск упоминаний сущностей
- Извлечение контекста (±2 предложения)
- Сохранение в JSON для обработки

### Шаг 2: Ручная доработка
- Проверка интерпретаций
- Добавление синтеза
- Уточнение разногласий

### Шаг 3: Валидация
- Проверка полноты (все SoTA для каждой сущности)
- Проверка консистентности

---

## 5. Оценка времени

| Файл | Сущностей | Время на сущность | Итого |
|------|-----------|-------------------|-------|
| 02B1-metabolites | 36 | 5 мин | ~3 часа |
| 02B2-diseases | 17 | 5 мин | ~1.5 часа |
| 02B3-systems | 19 | 5 мин | ~1.5 часа |
| 02B4-hormones | 8 | 5 мин | ~40 мин |
| 02B5-methods | 13 | 5 мин | ~1 час |
| 02B6-metrics | 18 | 5 мин | ~1.5 часа |
| 02B7-molecular | 37 | 5 мин | ~3 часа |
| 02B8-periods | 4 | 5 мин | ~20 мин |
| **Итого** | **152** | — | **~12-13 часов** |

---

## 6. Статус заполнения

| Файл | Статус | Дата начала | Дата завершения |
|------|--------|-------------|-----------------|
| 02B1-metabolites.md | ⏳ Pending | — | — |
| 02B2-diseases.md | ⏳ Pending | — | — |
| 02B3-systems.md | ⏳ Pending | — | — |
| 02B4-hormones.md | ⏳ Pending | — | — |
| 02B5-methods.md | ⏳ Pending | — | — |
| 02B6-metrics.md | ⏳ Pending | — | — |
| 02B7-molecular.md | ⏳ Pending | — | — |
| 02B8-periods.md | ⏳ Pending | — | — |

---

## 7. Примеры заполненных записей

### Пример 1: CS.ENTITY.009 — BHB

```markdown
## CS.ENTITY.009 — Beta-hydroxybutyrate (β-гидроксибутират)

| SoTA ID | Автор/Год | Интерпретация | Контекст использования |
|---------|-----------|---------------|------------------------|
| 027 | Gill 1990 | Маркер энергетического дефицита | Диагностика кетоза |
| 032 | Oetzel 2004 | Предиктор клинического кетоза | Пороговые значения |
| 037 | LeBlanc 2010 | Индикатор метаболического стресса | Связь с другими заболеваниями |
| 040 | McArt 2011 | Диагностический критерий | Subclinical ketosis screening |
| 041 | Ospina 2010 | Ранний предиктор риска | Fresh cow monitoring |
| 043 | Walsh 2016 | Ключевой метаболит для мониторинга | Transition management |
| 046 | Chapinal 2011 | Маркер в сравнении с NEFA | Predictive value |
| 053 | Bradford 2015 | Регулятор иммунной функции | Механизм действия |
| 055 | Drackley 1999 | Продукт неполного окисления ЖК | Липидный метаболизм |
| 058 | McFadden 2020 | Центральный метаболит адаптации | Метаболическая физиология |
| 060 | Lean 2006 | Критический показатель здоровья | Economic impact |
| 061 | LeBlanc 2006 | Маркер для вмешательства | Treatment protocols |
| 062 | LeBlanc 2010 | Предиктор воспроизводительной функции | Fertility outcomes |
| 063 | LeBlanc 2011 | Долгосрочный предиктор риска | Herd-level patterns |

### Синтез
- **Консенсус:** BHB — золотой стандарт для диагностики субклинического кетоза
- **Разногласия:** Пороги: ≥1.0 mmol/L (LeBlanc) vs ≥1.2 mmol/L (Oetzel) vs ≥1.4 mmol/L (McArt)
- **Эволюция:** От простого маркера → к многофункциональному регулятору метаболизма и иммунитета
```

### Пример 2: CS.ENTITY.018 — Ketosis

```markdown
## CS.ENTITY.018 — Ketosis (Кетоз)

| SoTA ID | Автор/Год | Интерпретация | Контекст использования |
|---------|-----------|---------------|------------------------|
| 012 | Aiello 1984 | Метаболическое заболевание | Энергетический баланс |
| 015 | Bertics 1992 | Следствие липомобилизации | Печеночный метаболизм |
| 016 | Bobe 2004 | Многофакторное состояние | Риск-факторы |
| 027 | Gill 1990 | Экономически значимое заболевание | Herd impact |
| 028 | Drackley 1999 | Ключевое звено метаболического каскада | Transition diseases |
| 029 | Grummer 1993 | Результат энергетического дефицита | Dry matter intake |
| 032 | Oetzel 2004 | Клиническое vs субклиническое | Диагностика |
| 037 | LeBlanc 2010 | Часть метаболического синдрома | Disease complex |
| 038 | LeBlanc 2006 | Предиктор других заболеваний | Risk assessment |
| 039 | McFadden 2017 | Метаболическая адаптация | Физиологический механизм |
| 040 | McArt 2011 | Управляемое состояние | Prevention strategies |
| 041 | Ospina 2010 | Ранний индикатор проблем | Monitoring tool |
| 042 | Ospina 2013 | Связь с фертильностью | Reproductive outcomes |
| 043 | Walsh 2016 | Центральная проблема transition | Management focus |
| 046 | Chapinal 2011 | Предиктор удоя и здоровья | Outcome prediction |
| 053 | Bradford 2015 | Иммуносупрессивное состояние | Immune function |
| 055 | Drackley 1999 | Модельная патология | Research model |
| 058 | McFadden 2020 | Нормальная адаптация vs патология | Physiological perspective |
| 060 | Lean 2006 | Экономический фактор | Cost-benefit analysis |
| 061 | LeBlanc 2006 | Точка вмешательства | Treatment timing |
| 062 | LeBlanc 2010 | Связь с эндокринной функцией | Hormonal interactions |
| 063 | LeBlanc 2011 | Популяционный паттерн | Herd epidemiology |

### Синтез
- **Консенсус:** Кетоз — центральное метаболическое заболевание transition period
- **Разногласия:** Клинический vs субклинический — отдельные сущности или спектр?
- **Эволюция:** От "болезнь" → "метаболическая адаптация" → "управляемый риск-фактор"
```

---

## 8. Связанные документы

- [00-entities-inventory.md](./00-entities-inventory.md) — Полный каталог сущностей
- [CS.ENTITY.XXX-*.md](./) — Индивидуальные файлы сущностей
- [../../01-sota/](../../01-sota/) — Источник SoTA-файлов

---

*Создан: 2026-03-27*  
*Статус: Спецификация готова к реализации*
