# Git Hooks для PACK-cattle-science

## Автоматическое обновление индекса SoTA

### Установка hooks

```bash
# Указать git использовать hooks из этой папки
git config core.hooksPath .githooks

# Сделать hooks исполняемыми (Unix/Mac)
chmod +x .githooks/post-commit
chmod +x .githooks/pre-commit
```

### Как это работает

#### post-commit hook
- **Срабатывает:** После каждого коммита
- **Действие:** 
  1. Проверяет, добавлены ли новые SoTA-файлы
  2. Автоматически запускает `scripts/add-sota-to-index.sh`
  3. Добавляет обновлённый индекс в коммит (amend)

#### pre-commit hook
- **Срабатывает:** Перед каждым коммитом
- **Действие:**
  1. Проверяет, есть ли новые SoTA-файлы в staged
  2. Предупреждает, если индекс не обновлён
  3. Запускает `verify-sota-index.sh` для проверки

### Ручное обновление (если hooks не настроены)

```bash
# Добавить конкретную SoTA в индекс
bash scripts/add-sota-to-index.sh pack/cattle-science/06-sota/health/CS.SOTA.060-capel-2021.md

# Проверить индекс
bash scripts/verify-sota-index.sh
```

### Отключение hooks

```bash
# Вернуться к стандартным hooks
git config --unset core.hooksPath
```

### Windows

На Windows hooks могут не работать напрямую. Используйте:
- Git Bash
- WSL
- Или ручное обновление через `scripts/add-sota-to-index.sh`
