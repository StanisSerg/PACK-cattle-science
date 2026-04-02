# Руководство по интеграции скриптов анализа сущностей

## Варианты интеграции

### Вариант 1: Git Hook (рекомендуется)

Автоматический запуск проверки после каждого коммита SoTA.

#### Установка:

```bash
# Включить использование локальных hooks
git config core.hooksPath .githooks

# Проверить
ls -la .githooks/
```

#### Результат:

После `git commit` с SoTA автоматически выводится:
```
═══════════════════════════════════════════════════════════════
  📝 Обнаружен новый SoTA
═══════════════════════════════════════════════════════════════

Запускаю проверку сущностей...

📚 Обнаружено существующих сущностей: 8
💡 Потенциальные новые сущности: 3

Следующие шаги:
  python3 scripts/update-entity-links.py 252
```

### Вариант 2: Ручной запуск (по необходимости)

Если hooks не настроены, запускать вручную:

```bash
# После создания каждого SoTA
./scripts/post-sota-check.sh --last

# Или для конкретного
./scripts/post-sota-check.sh 252
```

### Вариант 3: Интеграция в WP-75 Protocol

Протокол WP-75 обновлён — добавлена **Фаза 3.5**: Обновление связей сущностей.

```
Фаза 1: Подготовка
Фаза 2: Работа
Фаза 3: Закрытие
Фаза 3.5: Обновление связей ← НОВАЯ
Фаза 4: Публикация
```

**Чек-лист Фазы 3.5:**
- [ ] Запустить `./scripts/post-sota-check.sh --last`
- [ ] Проверить рекомендации скрипта
- [ ] Применить `update-entity-links.py` (если найдены сущности)
- [ ] Создать новые сущности (если рекомендовано score ≥ 2.0)
- [ ] Обновить индексы

### Вариант 4: IDE Integration

#### VS Code:

Добавить в `.vscode/tasks.json`:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Check SoTA Entities",
      "type": "shell",
      "command": "./scripts/post-sota-check.sh",
      "args": ["--last"],
      "group": "build",
      "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
      }
    },
    {
      "label": "Update Entity Links",
      "type": "shell",
      "command": "python3 scripts/update-entity-links.py",
      "args": ["${input:sotaId}"],
      "group": "build"
    }
  ],
  "inputs": [
    {
      "id": "sotaId",
      "type": "promptString",
      "description": "SoTA ID (e.g., 252)"
    }
  ]
}
```

#### Vim/Neovim:

Добавить в `.vimrc`:

```vim
" Check SoTA entities
command! SotaCheck :!./scripts/post-sota-check.sh --last

" Update entity links (asks for ID)
command! SotaLinks :execute '!python3 scripts/update-entity-links.py ' . input('SoTA ID: ')
```

### Вариант 5: Makefile

Создать `Makefile` в корне:

```makefile
.PHONY: sota-check sota-links reindex

# Проверить последний SoTA
sota-check:
	./scripts/post-sota-check.sh --last

# Обновить связи (usage: make sota-links ID=252)
sota-links:
	@python3 scripts/update-entity-links.py $(ID)

# Обновить все индексы
reindex:
	python3 scripts/reindex-sota.py
	python3 scripts/reindex-entities.py

# Полный цикл после создания SoTA
sota-complete: sota-check
	@echo "Run: make sota-links ID=<sota_id>"
```

Использование:
```bash
make sota-check     # Проверка
make sota-links ID=252   # Обновление связей
make reindex        # Обновление индексов
```

## Рекомендуемый workflow

### Для новых SoTA:

```bash
# 1. Создать SoTA по протоколу WP-75
# ... заполнение файла ...

# 2. Git add & commit
git add pack/cattle-science/06-sota/feeding/CS.SOTA.252-xxx.md
git commit -m "feat(sota): add CS.SOTA.252"

# 3. Автоматически запустится hook (или вручную):
./scripts/post-sota-check.sh --last

# 4. Обновить связи (если найдены сущности)
python3 scripts/update-entity-links.py 252

# 5. Обновить индексы
python3 scripts/reindex-sota.py
python3 scripts/reindex-entities.py

# 6. Добавить изменения связей
git add -A
git commit --amend -m "feat(sota): add CS.SOTA.252 with entity links"
```

## Частые вопросы

### Q: Hook не запускается
A: Проверьте:
```bash
# Права на выполнение
ls -la .githooks/post-commit

# Включены ли hooks
git config core.hooksPath
# Должно быть: .githooks

# Если нет:
git config core.hooksPath .githooks
```

### Q: Скрипт не находит сущность
A: Проверьте YAML сущности:
- Есть ли `name_ru` и `name_en`?
- Есть ли релевантные `tags`?
- Используется ли термин в SoTA?

### Q: Слишком много ложных срабатываний
A: Отредактируйте `scripts/analyze-sota-entities.py`:
- Добавьте термины в `stop_words`
- Увеличьте минимальный `score` для вывода

### Q: Как отключить hook временно?
A: 
```bash
git commit --no-verify -m "message"  # пропустить hooks
```

## См. также

- [WP-75 Protocol](../pack/cattle-science/PROTOCOLS/WP-75-sota-ingestion.md)
- [Entity Workflow](./ENTITY-WORKFLOW.md)
- [SoTA Template](../pack/cattle-science/TEMPLATES/SOTA-TEMPLATE.md)
