# Архитектура PACK-cattle-science

> **Версия:** 2.0  
> **Создан:** 2026-03-12  
> **Обновлён:** 2026-04-15  
> **Статус:** Активное развитие

---

## Философия архитектуры

PACK-cattle-science построен по многоуровневой архитектуре, отделяющей:
- **Фундаментальные знания** (Entities) от **практического применения** (Cases → Rules)
- **Теорию** (SoTA) от **методов** (Methods)
- **Общие принципы** от **конкретных ситуаций**
- **Описания** (Pack) от **исполнения** (Rule Engine)

Это позволяет:
- Быстро находить нужную информацию по ролям
- Стандартизировать практику через Methods
- Адаптировать знания под конкретные задачи через Cases
- Поддерживать актуальность без полной переработки
- Масштабировать научные знания в исполняемые правила

---

## Структура репозитория

```
PACK-cattle-science/
├── cases/                    # Сырые кейсы с фермы (Case Layer)
├── decisions/                # Decision Layer (что было решением)
├── docs/                     # Интеграция, workflow, guides
├── pack/
│   ├── cattle-science/       # Знания по SPF (Second Principles)
│   └── rules/                # Формализованные правила (RULE-XXX)
├── process/
│   ├── ingestion/            # Пайплайн добавления статей
│   │   ├── archive/          # Инвентарь PDF (файлы вне git)
│   │   └── new-articles/     # Входящие PDF для обработки
│   └── working/              # Временные файлы
├── rule_engine/              # Исполняемая система правил
└── scripts/                  # Автоматизация pack'а
```

---

## Структура `pack/cattle-science/`

```
pack/cattle-science/
├── 00-pack-manifest.md              # Входная точка, индекс
├── 01-domain-contract/              # Границы и различения
│   ├── 01A-bounded-context.md
│   ├── 01B-distinctions.md
│   └── 01C-ontology.md
│
├── 02-domain-entities/              # Сущности домена (P0 / P1 / P2)
│   ├── 00-entities-inventory.md
│   ├── 00-entity-template.md
│   ├── P0/                          # Приоритет 0: базовые (корова, молоко, рубец)
│   ├── P1/                          # Приоритет 1: производные
│   ├── P2/                          # Приоритет 2: специализированные
│   ├── 03-interpretations/          # Интерпретации сущностей
│   └── scripts/                     # Скрипты управления сущностями
│
├── 03-interpretations/              # Интерпретации домена
├── 03-methods/                      # Методы и SOP
├── 04-work-products/                # Шаблоны артефактов
├── 05-failure-modes/                # Типовые ошибки
├── 06-sota/                         # Научные источники
│   ├── economics/
│   ├── feeding/
│   ├── health/
│   ├── management/
│   └── reproduction/
├── 07-map/                          # Навигационные карты
├── PROTOCOLS/                       # Протоколы pack'а
└── TEMPLATES/                       # Шаблоны сущностей
```

---

## Корневые слои (вне `pack/`)

### `cases/` — Слой кейсов
**Назначение:** Сырые факты с фермы.  
**Формат:** `CASE-XXX-*.md` + `TEMPLATE-CASE.md`  
**Flow:** Кейс → Decision Layer → Rule

### `decisions/` — Decision Layer
**Назначение:** Запись того, что именно было решением в кейсе.  
**Формат:** `DL-XXX-*.md` + `TEMPLATE-DL.md`  
**Структура:** IF → THEN → BECAUSE → LIMITS

### `pack/rules/` — Исполняемые правила
**Назначение:** Формализованные правила для практики.  
**Формат:** `RULE-XXX-*.md` + `REGISTRY.md`  
**Структура:** IF → THEN → BECAUSE → LIMITS + Confidence + Escalation

### `rule_engine/` — Исполняемая система
**Назначение:** Python-скрипты, исполняющие правила над YAML-кейсами.  
**Состав:**
- `run_case.py` — главный движок
- `evaluate_case.py` — оценка prediction vs fact
- `models.py` — dataclasses
- `cases/` — YAML-кейсы для rule engine
- `rules/` — Python-модули правил (002, 003, ...)

### `scripts/` — Автоматизация
**Назначение:** Скрипты для поддержки pack'а.  
**Ключевые:**
- `validate-sota-template.sh` — валидация SoTA
- `rule-validator.py` / `rule-generator.py` — работа с правилами
- `reindex-sota.py` / `reindex-entities.py` — индексация
- `session-close.sh` — закрытие сессии ingestion

### `process/ingestion/` — Пайплайн статей
**Назначение:** Обработка PDF → SoTA.  
**Структура:**
- `new-articles/` — входящие PDF
- `archive/` — инвентарь обработанных (PDF хранятся вне git)
- `extract_pdf.py` — извлечение текста
- `sota-validator.py` — валидация

---

## Приоритеты сущностей (P0 / P1 / P2)

```
02-domain-entities/
├── P0/        # Базовые сущности (низкая волатильность)
│   ├── feeding/
│   ├── health/
│   ├── management/
│   └── reproduction/
├── P1/        # Производные сущности
│   ├── economics/
│   ├── feeding/
│   ├── genetics/
│   ├── health/
│   └── reproduction/
└── P2/        # Специализированные/продвинутые сущности
    ├── feeding/
    └── health/
```

**Принцип:** Приоритет = частота использования + стабильность. P0 меняются редко, P2 — чаще.

---

## Конвейер знаний: Case → DL → Rule → Engine

```
Ферма
  │
  ▼
cases/        ← Сырой факт (CASE-001)
  │
  ▼
decisions/    ← Что было решением (DL-001)
  │
  ▼
pack/rules/   ← Формализованное правило (RULE-001)
  │
  ▼
rule_engine/  ← Исполняемая логика (rule_001.py)
  │
  ▼
Рекомендация  ← Action + Prediction + Confidence
```

---

## Связи между уровнями

### Принцип зависимостей

```
Cases → Decisions → Rules → Rule Engine
  ↑         ↑          ↑
  └─────────┴──────────┘
        Зависят от
        pack/cattle-science/
              │
    Methods → SoTA → Entities
```

**Верхние уровни зависят от нижних, но не наоборот:**
- `01-domain-contract` не знает о `cases/`
- `06-sota/` ссылается на `02-domain-entities/`
- `03-methods/` реализует `06-sota/`
- `pack/rules/` использует `03-methods/` и `06-sota/`
- `rule_engine/` имплементирует `pack/rules/`

### Типы связей

| Тип | Описание | Пример |
|-----|----------|--------|
| `derived_from` | Кейс порождает решение | `DL-001` derived_from `CASE-001` |
| `formalizes` | Правило формализует решение | `RULE-001` formalizes `DL-001` |
| `implements` | Код реализует правило | `rule_002.py` implements `RULE-002` |
| `depends_on` | Зависит от знаний | `Methods` depends_on `SoTA` |
| `references` | Ссылается на сущность | `SoTA` references `P0 entity` |

---

## Поиск и навигация

### По ролям

| Роль | Начать с | Использовать |
|------|----------|--------------|
| **Фермер / Технолог** | `cases/` → `pack/rules/` | `FARM-CHECKLIST.md` для чеклистов |
| **Ветеринар** | `pack/rules/` (health) | `rule_engine/` для оценки кейса |
| **Репродуктолог** | `06-sota/reproduction/` | `03-methods/` для синхронизации |
| **Студент** | `02-domain-entities/P0/` | `06-sota/` для углубления |
| **Менеджер** | `00-pack-manifest.md` | `06-sota/economics/` для KPI |
| **Domain Engineer** | `CLAUDE.md` | `scripts/` + `process/ingestion/` |

### По задаче

| Задача | Путь |
|--------|------|
| Добавить статью | `process/ingestion/` → `06-sota/` |
| Создать правило из практики | `cases/` → `decisions/` → `pack/rules/` |
| Проверить нормы | `06-sota/feeding/` (NASEM) |
| Запустить оценку кейса | `rule_engine/run_case.py` |
| Понять физиологию | `02-domain-entities/P0/` |

---

## Процесс добавления нового контента

### Алгоритм принятия решения

```
Новый контент
    │
    ▼
Это фермерский кейс?
    ├── ДА → cases/ (CASE-XXX)
    │   ↓
    │   formalize → decisions/ (DL-XXX)
    │   ↓
    │   generalize → pack/rules/ (RULE-XXX)
    │   ↓
    │   implement → rule_engine/rules/ (rule_XXX.py)
    │
    └── НЕТ
        ↓
    Это научная статья?
        ├── ДА → process/ingestion/ → 06-sota/ (CS.SOTA.XXX)
        │   ↓
        │   integrate → 02-domain-entities/ (entities + links)
        │   ↓
        │   formalize → 03-methods/ или pack/rules/
        │
        └── НЕТ
            ↓
        Это сущность домена?
            ├── ДА → 02-domain-entities/P{N}/
            │
            └── НЕТ → Определить вручную
```

### Проверка перед созданием

- [ ] Правильный `type` в YAML
- [ ] Правильный ID по диапазону
- [ ] Правильная папка
- [ ] Ссылки на зависимости (related_entities, related SoTA)
- [ ] Обновление `00-pack-manifest.md` или `REGISTRY.md`

---

## Интеграция с FPF/SPF

### Соответствие шаблонам

| Аспект | FPF/SPF | PACK-cattle-science |
|--------|---------|---------------------|
| YAML frontmatter | ✅ | ✅ |
| Trust (F-G-R) | ✅ | ✅ |
| ID формат | DOMAIN.TYPE.XXX | CS.TYPE.XXX |
| Иерархия | Плоская | Многоуровневая + P0/P1/P2 |
| Связи | YAML relations | Хаб + вручную + `related_entities` |
| Исполнение | Документация | Rule Engine + Python |

### Расширения PACK

- Приоритетные уровни сущностей (P0/P1/P2)
- Полный конвейер `Case → DL → Rule → Engine`
- Исполняемые правила с валидацией и оценкой
- Интеграция SoTA в executable knowledge

---

## Версионирование

| Версия | Дата | Изменения |
|--------|------|-----------|
| 1.0 | 2026-03-12 | Базовая многоуровневая архитектура |
| 2.0 | 2026-04-15 | Синхронизация с реальной структурой: `cases/`, `decisions/`, `rule_engine/`, `pack/rules/`, P0/P1/P2 |

### Обновление архитектуры

При изменении архитектуры:
1. Обновить этот документ
2. Обновить `sota-ingestion-rules.md`
3. Обновить `00-pack-manifest.md`
4. Уведомить о breaking changes

---

*Архитектура PACK-cattle-science*  
*Версия: 2.0*  
*Обновлён: 2026-04-15*
