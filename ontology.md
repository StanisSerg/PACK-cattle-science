---
id: CS.ONTOLOGY.ROOT
type: ontology
domain: cattle-science
version: 1.1
created: 2026-03-12
updated: 2026-06-27
language: ru
---

# Онтология PACK-cattle-science (Root)

> Корневая онтология Pack'а "Наука о содержании и кормлении молочного крупного рогатого скота".

---

## Идентификация Pack'а

| Атрибут | Значение |
|---------|----------|
| **ID** | PACK-cattle-science |
| **Название** | Наука о содержании и кормлении молочного КРС |
| **Английское название** | Dairy Cattle Science |
| **Версия** | 1.0.0 |
| **Создан** | 2026-03-01 |
| **Обновлён** | 2026-06-27 |
| **Владелец** | Stanis Serg |
| **Тип** | Domain Pack (L2) |

---

## Позиционирование в иерархии

```
FPF (Level 1) — First Principles Framework
    ↓ upstream
SPF (Level 2) — Second Principles Framework
    ↓ downstream
PACK-cattle-science (L2) — Domain Pack
    ↓ downstream
DS-cattle-course (L3) — Surface (курс)
```

### Связь с upstream

| Upstream | Элемент | Связь |
|----------|---------|-------|
| FPF | A.1 Bounded Context | Структура области |
| FPF | A.3 Method | Типология методов |
| FPF | A.7 Strict Distinction | Различения |
| FPF | Part G SoTA Kit | Работа с источниками |
| SPF | pack-template/ | Структура Pack'а |
| SPF | process/ | Процесс создания |

### Downstream

| Downstream | Тип | Связь |
|------------|-----|-------|
| DS-cattle-course | Surface (курс) | Обучение на основе Pack'а |
| Exocortex-V2 | Personal IWE | Использование знаний |

---

## Структура Pack'а

```
PACK-cattle-science/
├── README.md
├── CLAUDE.md
├── REPO-TYPE.md
├── ontology.md                    ← Этот файл
├── pack/cattle-science/
│   ├── 00-pack-manifest.md
│   ├── 01-domain-contract/
│   │   ├── 01A-bounded-context.md
│   │   ├── 01B-distinctions.md
│   │   ├── 01C-ontology.md        ← Детальная онтология
│   │   └── 01D-domain-principles.md
│   ├── 02-domain-entities/        ← Доменные сущности
│   │   ├── P0/                    ← Базовый уровень
│   │   │   ├── feeding/
│   │   │   ├── health/
│   │   │   ├── management/
│   │   │   └── reproduction/
│   │   ├── P1/                    ← Промежуточный уровень
│   │   │   ├── economics/
│   │   │   ├── feeding/
│   │   │   ├── genetics/
│   │   │   ├── health/
│   │   │   └── reproduction/
│   │   ├── P2/                    ← Углублённый уровень
│   │   │   ├── feeding/
│   │   │   └── health/
│   │   ├── 00-entities-inventory.md
│   │   ├── 02A-roles.md
│   │   ├── 02B-entity-interpretations-spec.md
│   │   └── 02C-methods-index.md
│   ├── 03-methods/
│   │   ├── CS.METHOD.001-ketosis-diagnosis-treatment.md
│   │   ├── CS.METHOD.002-hypocalcemia-diagnosis-treatment.md
│   │   ├── CS.METHOD.005-calcium-monitoring-hypocalcemia-prevention.md
│   │   ├── CS.METHOD.006-farm-visit-feeding-assessment.md
│   │   └── _method-template.md
│   ├── 04-work-products/
│   │   ├── CS.WP.001-metabolic-status-assessment-report.md
│   │   ├── CS.WP.002-productivity-performance-report.md
│   │   └── README.md
│   ├── 05-failure-modes/
│   │   ├── CS.FM.002-late-hypocalcemia-detection.md
│   │   └── _failure-mode-template.md
│   ├── 06-sota/                   ← State of the Art
│   │   ├── economics/
│   │   ├── feeding/
│   │   ├── health/
│   │   ├── management/
│   │   ├── reproduction/
│   │   ├── ARCHGATE-ASSESSMENT.md
│   │   └── CS.ANALYSIS.*          ← Временно; требует переноса
│   └── 07-map/
│       ├── CS.MAP.001-sota-index.md
│       ├── CS.MAP.002-archgate-assessment.md
│       └── CS.MAP.002-sota-v1.1-index.md
└── process/
    ├── ingestion/
    └── working/
```

---

## Ключевые понятия (Top Level)

### Сущности (Entities)

Формальных файлов `CS.ENTITY.*`: **214** (+1 шаблон). Полный инвентарь см. в `pack/cattle-science/02-domain-entities/00-entities-inventory.md`.

| Уровень | Области | Количество | Примеры |
|---------|---------|------------|---------|
| P0 | feeding, health, management, reproduction | 58 | CS.ENTITY.001 21-day pregnancy rate, CS.ENTITY.002 Subclinical ketosis, CS.ENTITY.004 Rumen |
| P1 | economics, feeding, genetics, health, reproduction | 128 | CS.ENTITY.111 Herd turnover rate, CS.ENTITY.143 Genetic selection, CS.ENTITY.053 Machine learning |
| P2 | feeding, health | 28 | CS.ENTITY.151 Ceramides, CS.ENTITY.152 Mitochondria, CS.ENTITY.187 Metabolome |

### Методы (Methods)

| ID | Название | Описание | Статус |
|----|----------|----------|--------|
| CS.METHOD.001 | Ketosis diagnosis & treatment | Протокол раннего выявления и лечения кетоза | Active |
| CS.METHOD.002 | Hypocalcemia diagnosis & treatment | Протокол диагностики и лечения гипокальцемии | Active |
| CS.METHOD.005 | Calcium monitoring & hypocalcemia prevention | Мониторинг кальция и профилактика гипокальцемии в переходный период | Active |
| CS.METHOD.006 | Farm-visit feeding assessment | Оценка кормления при выезде на ферму | Active |

> **Примечание:** `CS.METHOD.003` и `CS.METHOD.004` объявлены в roadmap, но файлов пока нет.

### Рабочие продукты (Work Products)

| ID | Название | Описание | Статус |
|----|----------|----------|--------|
| CS.WP.001 | Metabolic status assessment report | Отчёт об оценке метаболического статуса стада | Active |
| CS.WP.002 | Productivity & performance report | Отчёт о продуктивности | Active |

> **Примечание:** `CS.WP.001` и `CS.WP.002` требуют добавления YAML frontmatter.

### Режимы отказа (Failure Modes)

| ID | Название | Описание | Статус |
|----|----------|----------|--------|
| CS.FM.002 | Late hypocalcemia detection | Позднее выявление гипокальцемии | Active |

> **Примечание:** `CS.FM.002` требует добавления YAML frontmatter. `CS.FM.001` объявлен в roadmap, но файла пока нет.

### SoTA (State of the Art)

Формальных файлов `CS.SOTA.*`: **330**.

| Область | Количество | Примечание |
|---------|------------|------------|
| feeding | 185 | Включая NASEM-материалы и практические статьи |
| health | 86 | Метаболические заболевания, иммунитет, переходный период |
| reproduction | 31 | Репродуктивные программы, фертильность, менеджмент |
| management | 16 | Алгоритмы оценки и управленческие практики |
| economics | 9 | Экономика замены, репродуктивных программ, эффективности |
| nutrition | 1 | Пересекающаяся область |
| — | 2 | Требует классификации area |

> **Технический долг SoTA:** 4 дубли ID, 9 посторонних файлов в `06-sota/` (анализы, обзоры, hidden-файлы).

---

## Пространство имён (Namespace)

### Префиксы

| Префикс | Значение | Пример |
|---------|----------|--------|
| CS. | Cattle-Science (домен) | CS.METHOD.001 |
| CS.ENTITY. | Сущности | CS.ENTITY.001 |
| CS.METHOD. | Методы | CS.METHOD.001 |
| CS.WP. | Work Products | CS.WP.001 |
| CS.FM. | Failure Modes | CS.FM.002 |
| CS.SOTA. | State of the Art | CS.SOTA.001 |
| CS.MAP. | Карты/индексы | CS.MAP.001 |
| CS.ROLES. | Роли | CS.ROLES.001 |
| CS.TOOLS. | Инструменты | CS.TOOLS.001 |

### Диапазоны ID

| Тип | Диапазон | Описание |
|-----|----------|----------|
| Сущности | 001-999 | Доменные сущности |
| Методы | 001-599 | По категориям (001-099 кормление, 100-199 репродукция и т.д.) |
| Work Products | 001-999 | Рабочие продукты |
| Failure Modes | 001-999 | Режимы отказа |
| SoTA | 001-999 | По подпапкам (reproduction/, feeding/, health/) |
| Роли | 001-999 | Роли в области |
| Инструменты | 001-999 | Инструменты и ПО |

---

## Ключевые различения (Hard Distinctions)

### Внутренние различения домена

Детальные различения домена описаны в двух файлах:

- `pack/cattle-science/01-domain-contract/01C-ontology.md` — §4 «Различения» (5 hard distinctions: Conception/Pregnancy, Service Rate/Conception Rate, Method/Tool, Lactating/Dry, Clinical/Subclinical).
- `pack/cattle-science/01-domain-contract/01B-distinctions.md` — расширенный реестр hard distinctions (D.001–D.008), включая Norm/Recommendation, Input/Output, Individual/Herd, Biological Potential/Economic Optimum, Acute/Chronic, Model/Reality, Justified Decision/Opinion.

В корневой `ontology.md` различия не дублируются, чтобы избежать рассинхронизации.

### Различения FPF/SPF в контексте

| FPF Различение | Применение | Статус |
|----------------|------------|--------|
| Role ≠ Actor | Роли vs исполнители | Применяется |
| Method ≠ Tool | Методы vs инструменты | Применяется |
| Work Product ≠ Description | Продукт vs описание | Применяется |
| System ≠ Episteme | Система vs область знания | Применяется |

---

## Процессы и гейты

### Процесс развития Pack'а

```
1. Domain Selection (SPF 01)
   ↓
2. Bounded Context (SPF 02)
   ↓
3. Distinctions Work (SPF 03)
   ↓
4. Entities Identification (SPF 04)
   ↓
5. Information Ingestion (SPF 05) ← SoTA ingestion
   ↓
6. Analysis & Formalization (SPF 06)
   ↓
7. Method & Product Extraction (SPF 07)
   ↓
8. Failure Modes Extraction (SPF 08)
   ↓
9. SoTA Annotation (SPF 09)
   ↓
10. Map Maintenance (SPF 10)
   ↓
11. Review & Evolution (SPF 11)
```

### Гейты (Lint)

| Гейт | Проверка | Когда |
|------|----------|-------|
| Structure Lint | Соответствие pack-template | Перед commit |
| ID Lint | Корректность идентификаторов | Перед commit |
| Content Lint | Отсутствие дидактики в Pack | Перед commit |
| Distinction Lint | Соблюдение Hard Distinctions | Перед commit |

---

## Метрики Pack'а

### Текущее состояние (2026-06-27)

| Метрика | Значение | Цель |
|---------|----------|------|
| SoTA документов | 330 | 500+ |
| Сущностей | 214 | 300+ |
| Методов (Active) | 4 | 20+ |
| Work Products | 2 | 10+ |
| Failure Modes | 1 | 10+ |
| Карт/индексов | 2 | 5+ |
| Полнота по SPF | 85% | 100% |

### Качество

| Метрика | Статус |
|---------|--------|
| Структура соответствует SPF | 🟡 85% — появились подпапки P0/P1/P2, требуется обновление lint |
| Все ID уникальны | ❌ 4 дубля среди SoTA, 1 дубль CS.MAP.002 |
| Все ссылки валидны | ❌ CS.METHOD.001 ссылается на CS.WP.003 и CS.FM.001, которых нет |
| Нет дидактики в Pack | ✅ |
| Frontmatter у всех CS.*.md | ❌ Отсутствует у CS.WP.001, CS.WP.002, CS.FM.002 |

---

## Дорожная карта (Roadmap)

### Phase 1: Foundation (Q1 2026) ✅ Выполнено
- [x] Структура Pack'а
- [x] Базовые методы (4)
- [x] Базовые WP (2)
- [x] SoTA коллекция (330)
- [x] Сущности (214)
- [x] Failure modes (1)

### Phase 2: Completeness (Q2–Q3 2026) 🔄 В процессе
- [ ] Исправить ID-дубли (CS.SOTA.026, 107, 108, 333; CS.MAP.002)
- [ ] Добавить frontmatter в CS.WP.001, CS.WP.002, CS.FM.002
- [ ] Создать недостающие методы (CS.METHOD.003–004, 007–010)
- [ ] Создать недостающие WP (CS.WP.003–005)
- [ ] Создать недостающие FM (CS.FM.001)
- [ ] Перенести анализы и обзоры из `06-sota/` в `process/working/` или `docs/audit/`
- [ ] Дополнить сущности до 250+ и зафиксировать P0/P1/P2 в `01C-ontology.md`

### Phase 3: Depth (Q4 2026) ⏳ Запланировано
- [ ] Глубокая проработка всех категорий
- [ ] Интеграция с другими Pack'ами
- [ ] Валидация практикой
- [ ] Автоматический lint ontology drift перед коммитом

---

## Связи с внешними системами

### Upstream

| Система | Тип связи | Частота обновления |
|---------|-----------|-------------------|
| FPF | Нормативная | По мере выхода версий |
| SPF | Нормативная | По мере выхода версий |

### Downstream

| Система | Тип связи | Контракт |
|---------|-----------|----------|
| DS-cattle-course | Использование | Pack → Course |
| Exocortex-V2 | Использование | Pack → IWE |

### Peer (соседние Pack'и)

| Pack | Связь | Статус |
|------|-------|--------|
| PACK-personal | Методы обучения | Planned |
| PACK-ecosystem | Экосистема | Planned |

---

## Контакты и поддержка

| Роль | Контакт | Ответственность |
|------|---------|-----------------|
| Владелец Pack'а | Stanis Serg | Стратегия, приоритеты |
| Knowledge Engineer | Kimi Code | Интеграция, lint, формализация |
| Domain Expert | TBD | Предметная экспертиза |

---

*Создано: 2026-03-12*  
*Версия: 1.1*  
*Статус: Активное развитие*  
*Соответствие SPF: 85%*
