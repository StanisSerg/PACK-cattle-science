---
id: CS.ENTITY.151
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
subarea2: molecular-lipids
fpf-type: U.Characteristic
name:
  ru: Керамиды
  en: Ceramides
abbreviation: Cer
definition:
  ru: Класс сфинголипидов, состоящих из сфингозина и жирной кислоты, ключевые компоненты клеточных мембран и сигнальные молекулы
  en: Class of sphingolipids consisting of sphingosine and fatty acid, key components of cell membranes and signaling molecules
source-sota:
  - id: CS.SOTA.039
    note: McFadden 2017 - lipidomics of liver in transition period
    relevance: high
related-entities:
  - id: CS.ENTITY.069
    relationship: is-a
    note: Sphingomyelins precursor/product
  - id: CS.ENTITY.003
    relationship: found-in
    note: Liver lipidome
measurement:
  method: LC-MS/MS metabolomics
  unit: μmol/L
  normal-range: unknown
---

# CS.ENTITY.151: Ceramides (Керамиды)

## Определение

Керамиды — класс сфинголипидов, состоящих из сфингозина и жирной кислоты. Являются ключевыми компонентами клеточных мембран и играют роль сигнальных молекул в регуляции клеточного цикла, дифференцировки и апоптоза.

## Физиологическая роль

### Структурная функция
- Основной компонент липидных рафт мембран
- Поддержание барьерной функции мембран
- Регуляция флюидности мембран

### Сигнальная функция
- Регуляция клеточного цикла
- Индукция апоптоза при стрессе
- Модуляция инсулиновой сигнализации

## Метаболизм

### Синтез (де novo)
```
Пальмитоил-КоА + Серин → 3-кетосфинганин → Сфинганин → Керамиды
```

### Распад
- Керамидаза → сфингозин + жирная кислота
- Фосфорилирование → церамид-1-фосфат

## Клиническое значение

### В transition period
- Изменение профиля керамидов в печени
- Связь с инсулинорезистентностью
- Маркер метаболического стресса

### Диагностика
- Метод: таргетная метаболомика (LC-MS/MS)
- Биоматериал: биопсия печени, плазма крови

## Связанные сущности

| Сущность | Связь | Описание |
|----------|-------|----------|
| CS.ENTITY.069 | Предшественник | Сфингомиелины |
| CS.ENTITY.003 | Локализация | Печень |
| CS.ENTITY.070 | Метаболизм | Желчные кислоты |

## Источники

- McFadden et al. (2017) — липидомика печени в переходный период (CS.SOTA.039)

---

*Создан: 2026-03-28*  
*Приоритет: P2*  
*Статус: Активен*
