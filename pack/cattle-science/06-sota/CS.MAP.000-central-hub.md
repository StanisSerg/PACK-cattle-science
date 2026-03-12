---
id: CS.MAP.000
type: map
subtype: central-hub
domain: cattle-science
status: current
created: 2026-03-12
updated: 2026-03-12
tags: [navigation, index, hub, cattle-science, feeding, reproduction, health]
---

# CS.MAP.000: Центральная навигация PACK-cattle-science

> **Назначение:** Единая точка входа во все знания PACK-cattle-science. Навигация по доменам, темам, связям между сущностями.

---

## Быстрый доступ по ролям

| Роль | Что искать | Куда идти |
|------|------------|-----------|
| **Технолог** | Рационы, нормы, чек-листы | [Feeding](#feeding-питание) → [Применение](#применение-applications) |
| **Ветеринар** | Метаболизм, болезни, профилактика | [Health](#health-здоровье) + [Feeding/Transition](#chapter-13-transition) |
| **Репродуктолог** | Циклы, осеменение, бесплодие | [Reproduction](#reproduction-репродукция) |
| **Менеджер** | Экономика, KPI, риски | [Cross-domain](#cross-domain-междоменные-связи) → [Экономика](#экономика) |
| **Студент** | База, физиология, системы | [Core](#core-сущности) → [NASEM](#nasem-reference-standard) |

---

## Структура знаний

### 1. Core (Ядро) — Фундаментальные сущности

> Базовые концепции, на которых строятся все остальные знания.

| ID | Сущность | Описание | Ключевые связи |
|----|----------|----------|----------------|
| CS.CORE.001 | [Корова](./core/CS.CORE.001-cow.md) | Физиология, фазы жизни, типы | Все домены |
| CS.CORE.002 | [Молоко](./core/CS.CORE.002-milk.md) | Состав, синтез, факторы | Feeding, Health |
| CS.CORE.003 | [Рубец](./core/CS.CORE.003-rumen.md) | Микробиом, ферментация, VFA | Feeding |
| CS.CORE.004 | [Метаболизм](./core/CS.CORE.004-metabolism.md) | Энергия, протеин, минералы | Feeding, Health |
| CS.CORE.005 | [Репродуктивная система](./core/CS.CORE.005-reproductive-system.md) | Анатомия, цикл, гормоны | Reproduction |
| CS.CORE.006 | [Иммунитет](./core/CS.CORE.006-immunity.md) | Защита, воспаление, стресс | Health, Feeding |

**Статус:** ✅ Готово (6 из 6)

---

### 2. Feeding (Питание) — Полный индекс

#### 2.1 NASEM Reference Standard

| Chapter | Название | Ключевые темы | Статус |
|---------|----------|---------------|--------|
| [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) | Energy | NEL, NEM, ME, TDN→NEL | ✅ Готово |
| [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) | Protein | MP, RDP/RUP, Lys/Met | ✅ Готово |
| [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) | Minerals | Ca, P, Mg, DCAD, микро | ✅ Готово |
| 010-07 | Vitamins | A, D, E, B12, β-каротин | 📝 TODO |
| 010-08 | Water | Потребление, качество | 📝 TODO |
| [010-09](./feeding/CS.SOTA.010-09-feed-intake.md) | Feed Intake | DMI, уравнения, факторы | ✅ Готово |
| 010-10 | Forages | Силос, сено, качество | 📝 TODO |
| 010-11 | Reproduction Nutrition | Питание и репродукция | 📝 TODO |
| 010-12 | Heifers | Выращивание нетелей | 📝 TODO |
| [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) | Transition Period | DCAD, кальций, метаболизм | ✅ Готово |
| [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) | BCS | Оценка упитанности | ✅ Готово |
| 010-15 | Fatty Acids | Жиры, защищённые жиры | 📝 TODO |
| 010-16 | Amino Acids | Углублённый анализ АК | 📝 TODO |
| 010-17 | Feed Additives | Добавки, премиксы | 📝 TODO |
| 010-18 | Environment | Температура, стресс | 📝 TODO |

#### 2.2 Другие SoTA по питанию

| ID | Название | Источник | Тема |
|----|----------|----------|------|
| CS.SOTA.001 | [Kolver 2018](./CS.SOTA.001-kolver-nutrition.md) | Kolver et al. | Высокая продуктивность |
| CS.SOTA.002 | [Lean 2019](./CS.SOTA.002-lean-nutrition.md) | Lean et al. | Метаболические заболевания |

---

### 3. Reproduction (Репродукция) — Структура

> **Внимание:** Этот домен требует наполнения

#### 3.1 Запланированные SoTA

| ID | Название | Источник | Ключевые темы | Статус |
|----|----------|----------|---------------|--------|
| [CS.SOTA.020-01](./reproduction/CS.SOTA.020-01-estrous-cycle.md) | Estrous Cycle | NASEM Ch.11 + Various | Эструальный цикл, гормоны | ✅ Готово |
| [CS.SOTA.020-02](./reproduction/CS.SOTA.020-02-synchronization.md) | Synchronization | Pursley et al. | Синхронизация циклов, TAI | ✅ Готово |
| CS.SOTA.020-03 | AI Techniques | NASEM | Техника осеменения | 📝 TODO |
| CS.SOTA.020-04 | Infertility | Various | Бесплодие, диагностика | 📝 TODO |
| CS.SOTA.020-05 | Postpartum | NASEM Ch.11 | Восстановление после отёла | 📝 TODO |
| CS.SOTA.020-06 | Heat Detection | Various | Обнаружение охоты | 📝 TODO |

#### 3.2 Связи с Feeding

| Тема | Feeding | Reproduction | Связь |
|------|---------|--------------|-------|
| Переходный период | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) | 020-05 | Метаболизм → цикл |
| BCS | [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) | 020-04 | Упитанность → концепция |
| Энергия | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) | 020-01 | НЭБ → ановуляция |
| Минералы | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) | 020-02 | Se, Zn → фертильность |

---

### 4. Health (Здоровье) — Структура

> **Внимание:** Этот домен требует наполнения

#### 4.1 Запланированные SoTA

| ID | Название | Тема | Статус |
|----|----------|------|--------|
| CS.SOTA.030-01 | Metabolic Disorders | Кетоз, гипокальция, ацидоз | 📝 TODO |
| CS.SOTA.030-02 | Mastitis | Маститы, профилактика | 📝 TODO |
| CS.SOTA.030-03 | Lameness | Хромота, копыта | 📝 TODO |
| CS.SOTA.030-04 | Transition Diseases | Метриты, ретенция | 📝 TODO |
| CS.SOTA.030-05 | Immunonutrition | Питание и иммунитет | 📝 TODO |

#### 4.2 Связи с Feeding

| Тема | Feeding | Health | Связь |
|------|---------|--------|-------|
| Гипокальция | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md), [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) | 030-01 | DCAD → профилактика |
| Кетоз | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md), [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) | 030-01 | NEB → кетоз |
| Мастит | [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) | 030-02 | Se, Zn, Vit E → иммунитет |
| Хромота | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) | 030-03 | Ca, P, Zn → копыта |

---

### 5. Cross-domain (Междоменные связи)

#### 5.1 По фазам лактации

| Фаза | DIM | Feeding | Reproduction | Health | Приоритет |
|------|-----|---------|--------------|--------|-----------|
| **Transition** | -21 to +21 | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) | 020-05 | 030-01, 030-04 | 🔴 Критично |
| **Early** | 0-100 | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md), [010-09](./feeding/CS.SOTA.010-09-feed-intake.md) | — | 030-01 | 🔴 Критично |
| **Breeding** | 60-120 | [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) | 020-01, 020-03 | — | 🟡 Важно |
| **Mid** | 100-200 | [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) | 020-04 | — | 🟢 Стандарт |
| **Late** | 200-305 | [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) | — | — | 🟡 Важно |
| **Dry** | -60 to 0 | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) | — | 030-01 | 🔴 Критично |

#### 5.2 По нутриентам

| Нутриент | Feeding | Reproduction | Health | Механизм |
|----------|---------|--------------|--------|----------|
| **Energy (NEL)** | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) | Цикл, концепция | Кетоз | НЭБ → метаболизм |
| **Protein (MP)** | [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) | Фертильность | Мастит | Иммуноглобулины |
| **Ca** | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md), [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) | Партурition | Гипокальция | Мышечная функция |
| **Se, Zn, Vit E** | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) | Концепция | Мастит, иммунитет | Антиоксиданты |

---

## Навигация по задачам

### Я составляю рацион для...

| Ситуация | Куда идти |
|----------|-----------|
| Дойная 30 DIM, 35 кг молока | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) + [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) + [010-09](./feeding/CS.SOTA.010-09-feed-intake.md) |
| Сухостойная -14 DIM | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) + [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) |
| Нетель 12 месяцев | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) (ME для нетелей) + [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) |
| Корова после метрита | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) + Health/030-04 |

### У меня проблема с...

| Проблема | Куда идти |
|----------|-----------|
| Кетоз | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) + [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) + Health/030-01 |
| Низкая концепция | [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) + Reproduction/020-04 |
| Маститы | [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) (Se, Zn) + [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) + Health/030-02 |
| Гипокальция | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) + [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md) |
| Низкий DMI | [010-09](./feeding/CS.SOTA.010-09-feed-intake.md) |

---

## Экономика

### ROI по доменам

| Домен | Инвестиция | Возврат | ROI | Приоритет |
|-------|------------|---------|-----|-----------|
| **Transition (DCAD)** | $15-20/корову | $40-80/корову | 200-400% | 🔴 Высокий |
| **Amino Acids** | $0.15/день | $0.50-0.80/день | 300-500% | 🟡 Средний |
| **BCS Management** | $0 (оценка) | $50-100/корову | ∞ | 🔴 Высокий |
| **Reproduction** | Разное | Предотвращение холостых | 400-800% | 🔴 Высокий |

---

## Методы (Methods)

### Расчётные

| ID | Метод | Описание | Использует |
|----|-------|----------|------------|
| CS.METHOD.001 | Расчёт MP | Требование метаболического протеина | [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) |
| CS.METHOD.002 | Расчёт NEL | Требование чистой энергии лактации | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) |
| CS.METHOD.003 | Расчёт ME нетелей | Требование для молодняка | [010-04](./feeding/CS.SOTA.010-04-nasem-energy.md) |
| CS.METHOD.004 | Расчёт DCAD | Баланс катионов-анионов | [010-06](./feeding/CS.SOTA.010-06-nasem-minerals.md), [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) |
| CS.METHOD.005 | Мониторинг метаболитов | NEFA, BHBA, Ca | [010-13](./feeding/CS.SOTA.010-13-nasem-transition-period.md) |
| CS.METHOD.006 | Оценка RDP:RUP | Анализ протеина | [010-05](./feeding/CS.SOTA.010-05-nasem-protein.md) |
| CS.METHOD.007 | DMI prediction | Прогноз потребления | [010-09](./feeding/CS.SOTA.010-09-feed-intake.md) |
| CS.METHOD.008 | BCS scoring | Оценка упитанности | [010-14](./feeding/CS.SOTA.010-14-body-condition-score.md) |

### Практические

| ID | Метод | Описание | Применение |
|----|-------|----------|------------|
| CS.METHOD.009 | pH мочи | Контроль DCAD | Transition |
| CS.METHOD.010 | Кетостик | BHBA в моче/крови | Health |
| CS.METHOD.011 | Оценка свежих | Ежедневный осмотр | Transition/Health |

---

## Обновления и версии

### История изменений

| Дата | Версия | Изменения |
|------|--------|-----------|
| 2026-03-12 | 1.0 | Создание центрального хаба, 6 NASEM SoTA готовы |
| 2026-03-12 | 1.1 | Добавлены 6 Core сущностей, 2 Reproduction SoTA |
| 2026-03-12 | 1.2 | Созданы methods/ и applications/, архитектура 1.0 |

### План развития

| Приоритет | Задача | Срок |
|-----------|--------|------|
| 🔴 Высокий | Создать Core сущности (6 шт.) | 1-2 недели |
| 🔴 Высокий | Дописать оставшиеся NASEM главы (9 шт.) | 2-3 недели |
| 🟡 Средний | Создать Reproduction SoTA (6 шт.) | 2-3 недели |
| 🟡 Средний | Создать Health SoTA (5 шт.) | 2 недели |
| 🟢 Низкий | Визуальная карта связей (Mermaid) | По запросу |

---

## Как внести вклад

### Добавить новый SoTA

1. Создать файл по шаблону `process/nasem-sota-template.md`
2. Обновить этот хаб (раздел соответствующего домена)
3. Добавить связи в раздел Cross-domain
4. Обновить историю изменений

### Исправить ошибку

1. Найти SoTA в соответствующем разделе
2. Внести правки
3. Обновить `updated` в frontmatter
4. Добавить запись в историю изменений

---

*Центральный хуб PACK-cattle-science*  
*Создан: 2026-03-12*  
*Всего SoTA: 6 готовых, 20+ запланировано*  
*Статус: Активное развитие*
