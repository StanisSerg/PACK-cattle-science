# Entity Management Scripts

Скрипты для управления сущностями PACK-cattle-science.

## Скрипты

### 1. `reorganize-entities.py`

Реорганизация структуры сущностей из плоской в иерархическую.

**Использование:**
```bash
# Просмотр изменений
python scripts/reorganize-entities.py --dry-run

# Выполнение миграции
python scripts/reorganize-entities.py --execute
```

### 2. `sota-entity-manager.py`

Базовый менеджер для работы со связями SoTA-сущности.

**Возможности:**
- Загрузка всех сущностей и SoTA
- Извлечение упоминаний сущностей из SoTA
- Создание новых сущностей из шаблона
- Обновление двунаправленных связей

**Использование:**
```bash
# Извлечь сущности из SoTA
python scripts/sota-entity-manager.py --sota CS.SOTA.001 --extract

# Показать рекомендации
python scripts/sota-entity-manager.py --sota CS.SOTA.001 --suggest

# Обновить связи
python scripts/sota-entity-manager.py --sota CS.SOTA.001 --update-links

# Создать новую сущность
python scripts/sota-entity-manager.py --sota CS.SOTA.001 \
    --create-entity \
    --name-ru "Новая сущность" \
    --name-en "New Entity" \
    --area health \
    --subarea metabolic-disorders
```

### 3. `sota-entity-autocreate.py`

Продвинутый скрипт для автоматического создания сущностей.

**Возможности:**
- Глубокий анализ контента SoTA
- Распознавание сущностей по сигнатурам
- Автоматическое создание сущностей
- Генерация отчётов

**Использование:**
```bash
# Анализ SoTA
python scripts/sota-entity-autocreate.py --sota CS.SOTA.001 --analyze

# Полный процесс (анализ + создание + связывание)
python scripts/sota-entity-autocreate.py --sota CS.SOTA.001 --full --dry-run

# Пакетная обработка
python scripts/sota-entity-autocreate.py \
    --batch CS.SOTA.001,CS.SOTA.002,CS.SOTA.003 \
    --full \
    --report report.json
```

**Поддерживаемые типы сущностей:**
- Diseases (заболевания): кетоз, мастит, метрит, гипокальциемия
- Metrics (метрики): BHB, NEFA, глюкоза, инсулин
- Concepts (концепции): НЭБ, переходный период, открытый период
- Methods (методы): Ovsynch, Presynch, Double-Ovsynch
- Technologies (технологии): sexed semen, beef semen, геномный отбор

### 4. `wp75-entity-integration.py`

Интеграция с протоколом WP-75 (SoTA Ingestion).

**Назначение:**
Этот скрипт вызывается на фазе 3 (Закрытие) WP-75 после создания SoTA.

**Интеграция в WP-75:**
```
Phase 3: Закрытие (25 мин)
├── Подфаза 3.1: Оценка качества (10 мин)
├── Подфаза 3.2: Entity Integration (5 мин) ← НОВОЕ
│   └── python scripts/wp75-entity-integration.py --sota CS.SOTA.XXX
├── Подфаза 3.3: Финальная проверка индекса (5 мин)
└── Подфаза 3.4: Фиксация (5 мин)
```

**Использование:**
```bash
# Интеграция одного SoTA
python scripts/wp75-entity-integration.py --sota CS.SOTA.001

# Просмотр перед выполнением
python scripts/wp75-entity-integration.py --sota CS.SOTA.001 --dry-run

# Пакетная обработка после сессии WP-75
python scripts/wp75-entity-integration.py \
    --batch CS.SOTA.010,CS.SOTA.011,CS.SOTA.012 \
    --yes

# С генерацией отчёта
python scripts/wp75-entity-integration.py --sota CS.SOTA.001 --report integration-report.json
```

## Workflow: Создание нового SoTA с автосозданием сущностей

### Полный процесс

```bash
# 1. Создать SoTA по протоколу WP-75
# (см. PROTOCOLS/WP-75-sota-ingestion.md)

# 2. После завершения SoTA, запустить интеграцию
cd PACK-cattle-science/pack/cattle-science/02-domain-entities

# 2.1 Просмотр что будет сделано
python scripts/wp75-entity-integration.py --sota CS.SOTA.XXX --dry-run

# 2.2 Выполнение интеграции
python scripts/wp75-entity-integration.py --sota CS.SOTA.XXX --yes

# 3. Проверить созданные сущности
ls P0/*/CS.ENTITY.*.md  # или P1, P2

# 4. Обновить индекс SoTA (если не автоматически)
bash scripts/add-sota-to-index.sh ../06-sota/[area]/CS.SOTA.XXX-*.md

# 5. Git commit
git add -A
git commit -m "CS.SOTA.XXX: Add SoTA with auto-created entities"
```

## Структура связей

### SoTA → Entity (в YAML frontmatter SoTA)
```yaml
related:
  - id: CS.SOTA.002
    type: extends
    note: "Fricke 2023 развивает концепции"
```

### Entity → SoTA (в YAML frontmatter Entity)
```yaml
related_sota:
  - CS.SOTA.001
  - CS.SOTA.002
related_entities:
  - CS.ENTITY.003
  - CS.ENTITY.004
```

## Добавление новых сущностей для распознавания

Чтобы добавить распознавание новой сущности, отредактируйте:

**В `sota-entity-autocreate.py`:**
```python
ENTITY_SIGNATURES = {
    'your_entity_key': {
        'patterns': [
            r'паттерн на русском',
            r'english pattern',
        ],
        'type': 'concept',  # disease|metric|concept|method|technology
        'name_ru': 'Название на русском',
        'name_en': 'English Name',
        'abbreviation': 'ABBR',  # опционально
        'area': 'health',  # health|reproduction|feeding|genetics|management|economics
        'subarea': 'metabolic-disorders',
    },
}
```

## Требования

- Python 3.8+
- PyYAML: `pip install pyyaml`

## Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                    WP-75 Protocol                           │
│  Phase 1 → Phase 2 → Phase 3 → Entity Integration → Git     │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              wp75-entity-integration.py                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │   Extract   │→│   Analyze   │→│  Create/Link        │  │
│  │  entities   │  │   suggest   │  │  update bidirectional│  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              sota-entity-manager.py                         │
│  - Load entities/SoTAs                                      │
│  - Parse YAML frontmatter                                   │
│  - Create from template                                     │
│  - Update links                                             │
└─────────────────────────────────────────────────────────────┘
```

## История изменений

| Дата | Версия | Изменения |
|------|--------|-----------|
| 2026-03-28 | 1.0 | Создание системы автосоздания сущностей |
| 2026-03-28 | 1.1 | Интеграция с WP-75 |
