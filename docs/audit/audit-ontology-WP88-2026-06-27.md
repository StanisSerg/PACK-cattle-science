---
id: CS.AUDIT.001
type: audit
target: PACK-cattle-science ontology
wp: WP-88
date: 2026-06-27
status: draft
---

# Аудит онтологии PACK-cattle-science (WP-88)

## 1. Резюме

Проверил соответствие между `ontology.md` (корневая онтология Pack'а) и фактическими файлами в `pack/cattle-science/`. Нашёл серьёзный drift: метрики и структура в `ontology.md` отстают от реального состояния репозитория на несколько месяцев активной работы.

**Ключевые расхождения**

| Категория | Заявлено в `ontology.md` | Фактически в `pack/cattle-science/` |
|-----------|--------------------------|-------------------------------------|
| SoTA-документов | 29 | 330 файлов `CS.SOTA.*` + 9 посторонних файлов в `06-sota/` |
| Сущностей (Entities) | 1 | 214 формальных файлов `CS.ENTITY.*` + 1 шаблон |
| Методов (Methods) | 3 | 4 файла `CS.METHOD.*` + 1 шаблон |
| Рабочих продуктов (WP) | 3 | 2 файла `CS.WP.*` |
| Режимов отказа (FM) | 2 | 1 файл `CS.FM.*` + 1 шаблон |
| Карт/индексов (MAP) | 1 | 2 файла с одинаковым ID `CS.MAP.002` |

**Вердикт:** `ontology.md` не является достоверным источником истины. Его нужно либо синхронизировать с файлами, либо пересмотреть границы Pack'а.

---

## 2. Что проверял

- Скриптом обошёл все `.md`-файлы в `pack/cattle-science/`.
- Извлёк frontmatter (`id`, `title`, `area`) там, где он есть.
- Сравнил найденные ID с таблицами в `ontology.md` (разделы «Ключевые понятия», «Структура Pack'а», «Метрики Pack'а»).
- Дополнительно проверил дубликаты ID, отсутствующий frontmatter, файлы в неправильных директориях и битые ссылки между артефактами.

---

## 3. Найденные расхождения

### 3.1 SoTA — самый большой drift

`ontology.md` (строки 146–150) указывает:

| Диапазон | Тема | Количество |
|----------|------|------------|
| CS.SOTA.001–099 | Reproduction | 12 |
| CS.SOTA.010–019 | Feeding (NASEM) | 17 |

Фактическое распределение по 330 файлам `CS.SOTA.*`:

| Область (area) | Количество |
|----------------|------------|
| feeding | 185 |
| health | 86 |
| reproduction | 31 |
| management | 16 |
| economics | 9 |
| nutrition | 1 |
| — | 2 |

**Вывод:** Pack давно вышел за рамки заявленных 29 источников и двух областей. Области `health`, `economics` и `management` вообще не упомянуты в сводке SoTA.

#### Дубликаты ID среди SoTA

Один ID назначен двум разным источникам:

| ID | Файл 1 | Файл 2 |
|----|--------|--------|
| CS.SOTA.026 | `06-sota/health/CS.SOTA.026-aiello-1984.md` | `06-sota/management/CS.SOTA.026-reproductive-assessment-algorithm.md` |
| CS.SOTA.107 | `06-sota/health/CS.SOTA.107-venjakob-2017.md` | `06-sota/feeding/CS.SOTA.107-bach-2005.md` |
| CS.SOTA.108 | `06-sota/health/CS.SOTA.108-okkema-2023.md` | `06-sota/feeding/CS.SOTA.108-bell-2000.md` |
| CS.SOTA.333 | `06-sota/health/CS.SOTA.333-martins-2019.md` | `06-sota/feeding/CS.SOTA.333-tom-2026-heifer-growth-efficiency-feeding.md` |

#### Посторонние файлы в `06-sota/`

В папке SoTA лежат документы, которые не являются SoTA-статьями:

- `06-sota/ARCHGATE-ASSESSMENT.md`
- `06-sota/feeding/.CS.SOTA.294-295-FPF-review.md`
- `06-sota/feeding/.CS.SOTA.294-gap-analysis.md`
- `06-sota/feeding/CS.ANALYSIS.001-weiss-minerals-fpf-audit.md`
- `06-sota/feeding/CS.ANALYSIS.002-lectures-001-003-fpf-audit.md`
- `06-sota/feeding/CS.ANALYSIS.003-lectures-001-003-number-verification.md`
- `06-sota/feeding/CS.ANALYSIS.004-weiss-webinar-2-narrativization.md`
- `06-sota/feeding/CS.ANALYSIS.005-tom-heifer-discussion-narrativization.md`
- `06-sota/management/CS.SOTA.284-milking-data-2026.md`

Анализы и обзоры FPF стоит перенести в отдельную директорию (например, `07-map/`, `process/working/` или `docs/audit/`).

---

### 3.2 Сущности (Entities)

`ontology.md` упоминает только **CS.ENTITY.001** «21-day pregnancy rate». Фактически в `02-domain-entities/` находится 214 файлов `CS.ENTITY.001–214`, плюс шаблон `CS.ENTITY.XXX`.

**Проблемы:**

- 213 сущностей не отражены в корневой онтологии.
- Файлы разложены по подпапкам `P0/`, `P1/`, `P2/` (вероятно, приоритет/глубина), но в `ontology.md` эта структура не описана.
- Есть шаблон с placeholder-ID `CS.ENTITY.XXX` (`02-domain-entities/00-entity-template.md`).

#### Примеры сущностей, которые уже существуют, но не внесены в `ontology.md`

| ID | Название | Область |
|----|----------|---------|
| CS.ENTITY.002 | Subclinical ketosis | health |
| CS.ENTITY.004 | Rumen | feeding |
| CS.ENTITY.020 | Hypocalcemia | health |
| CS.ENTITY.030 | DMI | feeding |
| CS.ENTITY.053 | Machine learning | management |
| CS.ENTITY.111 | Herd turnover rate | economics |

---

### 3.3 Методы (Methods)

`ontology.md` заявляет:

| ID | Название в онтологии | Статус |
|----|----------------------|--------|
| CS.METHOD.003 | Reproductive economics | Active |
| CS.METHOD.004 | Cow value assessment | Active |
| CS.METHOD.005 | Transition health monitoring | Active |

Фактически в `03-methods/`:

| ID | Название в файле | Наличие |
|----|------------------|---------|
| CS.METHOD.001 | Протокол диагностики и лечения кетоза | ✅ |
| CS.METHOD.002 | Протокол диагностики и лечения гипокальцемии | ✅ |
| CS.METHOD.005 | Мониторинг кальция и профилактика гипокальцемии | ✅, но название не совпадает с онтологией |
| CS.METHOD.006 | Оценка кормления при выезде на ферму | ✅ |
| CS.METHOD.XXX | Шаблон метода | ⚠️ placeholder |

**Проблемы:**

- CS.METHOD.003 и CS.METHOD.004 объявлены в онтологии, но файлов нет.
- CS.METHOD.001 и CS.METHOD.002 присутствуют, но в онтологии не упомянуты.
- CS.METHOD.005 в онтологии называется «Transition health monitoring», а в файле — «Мониторинг кальция…». Нужно либо переименовать, либо разделить на два метода.

---

### 3.4 Рабочие продукты (WP)

`ontology.md` заявляет:

| ID | Название |
|----|----------|
| CS.WP.003 | Reproduction economic report |
| CS.WP.004 | Cow value report |
| CS.WP.005 | Program comparison |

Фактически в `04-work-products/`:

| ID | Название | Примечание |
|----|----------|------------|
| CS.WP.001 | Отчёт об оценке метаболического статуса стада | ✅, но нет frontmatter |
| CS.WP.002 | Отчёт о продуктивности | ✅, но нет frontmatter |

**Проблемы:**

- CS.WP.003–005 отсутствуют.
- CS.WP.001–002 существуют, но в `ontology.md` не упомянуты.
- У обоих WP-файлов отсутствует YAML frontmatter, поэтому скрипты не могут автоматически распознать их ID.

---

### 3.5 Режимы отказа (FM)

`ontology.md` заявляет:

| ID | Название |
|----|----------|
| CS.FM.001 | Overestimation of 21-d PR |
| CS.FM.002 | Ignoring replacement constraints |

Фактически в `05-failure-modes/`:

| ID | Название | Примечание |
|----|----------|------------|
| CS.FM.002 | Позднее выявление гипокальцемии | ✅, но title не совпадает с онтологией; frontmatter отсутствует |
| CS.FM.XXX | Шаблон FM | ⚠️ placeholder |

**Проблемы:**

- CS.FM.001 отсутствует.
- CS.FM.002 существует, но названо иначе, чем в `ontology.md`.
- У CS.FM.002 нет frontmatter.

---

### 3.6 Карты и индексы (MAP)

| ID | Файлы | Проблема |
|----|-------|----------|
| CS.MAP.001 | `07-map/CS.MAP.001-sota-index.md` + `07-map/sota-index/CS.MAP.001-*.md` | Один ID на несколько файлов |
| CS.MAP.002 | `07-map/CS.MAP.002-archgate-assessment.md` + `07-map/CS.MAP.002-sota-v1.1-index.md` | Прямой дубль ID |

---

### 3.7 Битые ссылки между артефактами

`CS.METHOD.001` ссылается на:

- `CS.WP.003` — не существует.
- `CS.FM.001` — не существует.
- `CS.ENTITY.001` — существует.

Это означает, что при работе по Pack'у метод указывает на артефакты, которых нет.

---

### 3.8 Отсутствующий frontmatter

Следующие важные файлы не имеют YAML frontmatter, поэтому автоматические lint-скрипты и KE-процессы не видят их как формальные артефакты:

- `04-work-products/CS.WP.001-metabolic-status-assessment-report.md`
- `04-work-products/CS.WP.002-productivity-performance-report.md`
- `05-failure-modes/CS.FM.002-late-hypocalcemia-detection.md`

---

## 4. Структурные находки

### 4.1 Структура `02-domain-entities/` не описана в `ontology.md`

Фактическая структура:

```
02-domain-entities/
├── P0/
│   ├── feeding/
│   ├── health/
│   ├── management/
│   └── reproduction/
├── P1/
│   ├── economics/
│   ├── feeding/
│   ├── genetics/
│   ├── health/
│   └── reproduction/
└── P2/
    ├── feeding/
    └── health/
```

В `ontology.md` упоминается только плоский список с одним файлом. Нужно либо зафиксировать структуру `P0/P1/P2`, либо отказаться от неё.

### 4.2 Противоречие с дорожной картой

`ontology.md` (строки 269–280) заявляет Phase 1 выполненной со «SoTA коллекция (29)». Фактически SoTA уже 330+. Это делает roadmap неактуальной.

---

## 5. Рекомендации

### 5.1 Быстрые исправления (можно сделать одним PR)

1. **Добавить frontmatter** в `CS.WP.001`, `CS.WP.002`, `CS.FM.002`.
2. **Разрешить дубли ID:**
   - CS.SOTA.026, 107, 108, 333 — переименовать один из конфликтующих файлов.
   - CS.MAP.002 — либо объединить, либо дать разные ID.
3. **Убрать placeholder-ID** из шаблонов (`CS.ENTITY.XXX`, `CS.FM.XXX`) или явно пометить их как шаблоны без реального ID.
4. **Перенести анализы и обзоры** из `06-sota/` в `process/working/` или `docs/audit/`.

### 5.2 Средние исправления (требуют решения пилота)

1. **Синхронизировать `ontology.md` с реальным состоянием:**
   - Обновить таблицы Entities, Methods, WP, FM.
   - Обновить метрики (SoTA 330+, Entities 214, Methods 4, WP 2, FM 1).
   - Обновить структуру Pack'а (добавить `P0/P1/P2`, области `health`, `economics`, `management`).
2. **Решить, какие методы и WP нужны:**
   - Либо создать недостающие CS.METHOD.003–004 и CS.WP.003–005.
   - Либо убрать их из `ontology.md` и методов, которые на них ссылаются.
3. **Привести названия в соответствие:**
   - CS.METHOD.005: уточнить, что это именно «кальциевый мониторинг».
   - CS.FM.002: либо переименовать файл, либо изменить описание в `ontology.md`.

### 5.3 Долгосрочные меры

1. **Автоматизировать lint:** добавить скрипт, который перед коммитом проверяет:
   - уникальность ID,
   - наличие frontmatter у всех `CS.*.md`,
   - соответствие между `ontology.md` и фактическими файлами.
2. **Внести в KE-процесс правило:** после добавления нового `CS.*.md` обновлять `ontology.md` или связанный индекс.
3. **Пересмотреть Roadmap:** Phase 1 фактически давно выполнен, Phase 2 частично выполнен. Нужна новая дорожная карта.

---

## 6. Следующий шаг

Рекомендую сначала решить принципиальный вопрос:

> **Сделать `ontology.md` авторитетным источником истины (и привести файлы к нему) или наоборот — перестроить `ontology.md` под фактическое содержимое Pack'а?**

После ответа я могу подготовить конкретный PR/набор правок.

---

## 7. Приложение: статистика по файлам

| Тип префикса | Количество файлов |
|--------------|-------------------|
| CS.SOTA.* | 330 |
| CS.ENTITY.* | 214 |
| CS.METHOD.* | 4 |
| CS.WP.* | 2 |
| CS.FM.* | 1 |
| CS.MAP.* | 2 |
| CS.ANALYSIS.* | 3 |
| CS.INT.MET.* | 1 |
| CS.ONTOLOGY.* | 1 |
| CS.ROLES.* | 1 |
| Прочее (README, шаблоны, индексы) | ~44 |

**Всего `.md`-файлов в `pack/cattle-science/`:** 603.


---

## 8. Применённые исправления (2026-06-27)

После выбора пилотом варианта «привести `ontology.md` к реальности» внесены изменения в `ontology.md`:

- **Версия:** 1.0 → 1.1, дата обновления 2026-06-27.
- **Структура Pack'а:** отражены реальные подпапки `P0/P1/P2` в `02-domain-entities/`, актуальные методы, WP, FM, MAP и области SoTA.
- **Таблицы понятий:**
  - Сущности — сводка по 214 файлам с разбивкой по уровням и областям.
  - Методы — 4 актуальных метода; CS.METHOD.003–004 помечены как запланированные.
  - WP — 2 актуальных продукта; помечено отсутствие frontmatter.
  - FM — 1 актуальный режим отказа; помечено отсутствие frontmatter.
  - SoTA — 330 файлов по областям.
- **Метрики:** обновлены до фактических значений; качество — добавлены ❌ на дубли, битые ссылки и отсутствующий frontmatter.
- **Roadmap:** Phase 1 отмечена выполненной с фактическими цифрами; Phase 2 переименована в Completeness (Q2–Q3) и дополнена техническим долгом.

Оставшиеся проблемы (дубли ID, отсутствующий frontmatter, битые ссылки, посторонние файлы) зафиксированы в `ontology.md` как технический долг Phase 2.
