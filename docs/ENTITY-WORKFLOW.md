# Workflow: Обновление сущностей после создания SoTA

## Быстрый старт

После создания нового SoTA:

```bash
./scripts/post-sota-check.sh --last
```

## Скрипты

### 1. Анализ сущностей

```bash
python3 scripts/analyze-sota-entities.py 252
```

### 2. Обновление связей

```bash
# Проверка
python3 scripts/update-entity-links.py 252 --dry-run

# Применение
python3 scripts/update-entity-links.py 252
```

### 3. Комплексная проверка

```bash
./scripts/post-sota-check.sh 252
```

## Workflow

1. Создать SoTA
2. Запустить `./scripts/post-sota-check.sh --last`
3. Проверить рекомендации
4. Обновить связи: `python3 scripts/update-entity-links.py <id>`
5. При необходимости создать новые сущности
6. Обновить инвентарь: `python3 scripts/reindex-entities.py`
7. Git commit && push
