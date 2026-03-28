---
id: CS.ENTITY.153
type: entity
priority: P2
domain: cattle-science
area: health
subarea: cellular-biology
subarea2: organelles
fpf-type: U.System
name:
  ru: Пероксисомы
  en: Peroxisomes
abbreviation: PXS
definition:
  ru: Одномембранные органеллы, сайт пероксисомального β-окисления жирных кислот и детоксикации реактивных кислородных видов
  en: Single-membrane organelles, site of peroxisomal β-oxidation of fatty acids and detoxification of reactive oxygen species
source-sota:
  - id: CS.SOTA.026
    note: Drackley 1991 - hepatic fatty acid oxidation pathways
    relevance: high
  - id: CS.SOTA.039
    note: McFadden 2017 - very long chain fatty acid metabolism
    relevance: medium
related-entities:
  - id: CS.ENTITY.003
    relationship: located-in
    note: Hepatic peroxisomes
  - id: CS.ENTITY.097
    relationship: regulated-by
    note: PPAR-α activation
  - id: CS.ENTITY.152
    relationship: cooperates-with
    note: Mitochondrial-peroxisomal interplay
measurement:
  method: Enzymatic markers (catalase, acyl-CoA oxidase)
  unit: activity units
  normal-range: unknown
---

# CS.ENTITY.153: Peroxisomes (Пероксисомы)

## Определение

Пероксисомы — одномембранные органеллы клеток эукариот, содержащие ферменты для окисления жирных кислот (особенно очень длинноцепочечных) и детоксикации реактивных кислородных видов.

## Структура

### Мембрана
- Однослойная липидная билипидная мембрана
- Содержит транспортные белки
- Обмен метаболитами с цитоплазмой

### Матрикс
- Ферменты β-окисления
- Каталаза (детоксикация H₂O₂)
- Ферменты биосинтеза эфирных липидов

## Функции

### Пероксисомальное β-окисление
- Субстрат: очень длинноцепочечные жирные кислоты (>C22)
- Продукт: ацетил-КоА (транспортируется в митохондрии)
- Отличие от митохондриального: не производит АТФ напрямую

### Детоксикация
- Разложение H₂O₂ каталазой
- Нейтрализация токсичных соединений
- Регуляция окислительного стресса

### Биосинтез
- Эфирные фосфолипиды (плазмалогены)
- Желчные кислоты (предшественники)

## Регуляция

### PPAR-α
- Основной регулятор биогенеза
- Индукция при голодании, диабете
- Увеличение числа и размера пероксисом

### Физиологические стимулы
- Высокий уровень жирных кислот
- Гиполипидемические препараты (фибраты)
- Переходный период (адаптация)

## Роль в transition period

### Адаптация
- Увеличение активности при липомобилизации
- Компенсация перегрузки митохондрий
- Альтернативный путь окисления

### Маркеры
- Каталаза — общий маркер
- Ацил-КоА оксидаза — специфичный маркер β-окисления

## Связанные сущности

| Сущность | Связь | Описание |
|----------|-------|----------|
| CS.ENTITY.003 | Локализация | Печень |
| CS.ENTITY.152 | Кооперация | Митохондрии |
| CS.ENTITY.097 | Регуляция | PPAR-α |
| CS.ENTITY.074 | Субстрат | Жирные кислоты |

## Источники

- Drackley et al. (1991) — пути окисления жирных кислот в печени (CS.SOTA.026)
- McFadden et al. (2017) — метаболизм очень длинноцепочечных жирных кислот (CS.SOTA.039)

---

*Создан: 2026-03-28*  
*Приоритет: P2*  
*Статус: Активен*
