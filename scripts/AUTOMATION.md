# Автоматизация WP-75 (SoTA Ingestion)

Автоматизированный workflow для создания SoTA с валидацией, индексацией и интеграцией сущностей.

---

## 🔄 Полный Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│  1. Создание SoTA (ручное/AI)                                       │
│     └── pack/cattle-science/06-sota/[area]/CS.SOTA.XXX-*.md         │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  2. Git Commit                                                      │
│     └── git add . && git commit -m "CS.SOTA.XXX: ..."               │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  3. Post-Commit Hook (автоматически)                                │
│     ├── ✅ Валидация по шаблону                                     │
│     ├── ✅ Обновление CS.MAP.001 (индекс)                          │
│     └── ✅ Amend commit с индексом                                  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│  4. Session Close (по окончании сессии)                             │
│     ├── Проверка всех новых SoTA                                    │
│     ├── Обновление индекса                                          │
│     ├── Entity Integration (создание связей)                        │
│     └── Git commit финальных изменений                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📋 Установка

### 1. Настройка Git Hooks

```bash
cd PACK-cattle-science
git config core.hooksPath .githooks
chmod +x .githooks/post-commit
```

### 2. Проверка скриптов

```bash
# Сделать исполняемыми
chmod +x scripts/validate-sota-template.sh
chmod +x scripts/session-close.sh
chmod +x scripts/add-sota-to-index.sh
chmod +x scripts/verify-sota-index.sh
```

---

## 🚀 Использование

### Вариант A: Автоматический (рекомендуется)

```bash
# 1. Создаёте SoTA (вручную или через AI)
# 2. Коммитите
git add pack/cattle-science/06-sota/feeding/CS.SOTA.139-example-2024.md
git commit -m "CS.SOTA.139: Example study on feeding strategies"

# 3. Hook автоматически:
#    - Провалидирует SoTA
#    - Добавит в индекс
#    - Сделает amend commit

# 4. По окончании сессии запускаете session-close
bash scripts/session-close.sh
```

### Вариант B: Ручной контроль

```bash
# Валидация конкретного SoTA
bash scripts/validate-sota-template.sh pack/cattle-science/06-sota/feeding/CS.SOTA.139-*.md

# Добавление в индекс
bash scripts/add-sota-to-index.sh pack/cattle-science/06-sota/feeding/CS.SOTA.139-*.md

# Entity Integration
cd pack/cattle-science/02-domain-entities
python scripts/wp75-entity-integration.py --sota CS.SOTA.139 --yes
```

### Вариант C: Пакетная обработка

```bash
# Закрытие сессии с конкретными SoTA
bash scripts/session-close.sh --sota CS.SOTA.139,CS.SOTA.140,CS.SOTA.141

# Автоматический режим (без подтверждений)
bash scripts/session-close.sh --auto

# С генерацией отчёта
bash scripts/session-close.sh --report
```

---

## 🧪 Скрипты

### `validate-sota-template.sh`

Проверяет SoTA на соответствие шаблону v1.4.

**Проверки:**
- ✅ Имя файла (CS.SOTA.XXX-author-year.md)
- ✅ YAML frontmatter (все обязательные поля)
- ✅ Структура разделов (14 разделов)
- ✅ Key Claims (минимум 2, с Evidence/Confidence)
- ✅ Медиа-инвентарь ([СКРИНШОТ])
- ✅ Журнал обработки
- ✅ Связи (related)

**Использование:**
```bash
bash scripts/validate-sota-template.sh <file>           # Один файл
bash scripts/validate-sota-template.sh --all            # Все SoTA
bash scripts/validate-sota-template.sh --batch ID1,ID2  # Пакетно
```

### `session-close.sh`

Полный цикл закрытия сессии.

**Фазы:**
1. Валидация всех новых SoTA
2. Обновление индекса CS.MAP.001
3. Entity Integration (автосоздание сущностей)
4. Git commit

**Использование:**
```bash
bash scripts/session-close.sh              # Интерактивный
bash scripts/session-close.sh --auto       # Автоматический
bash scripts/session-close.sh --report     # С отчётом
```

### `add-sota-to-index.sh`

Добавляет SoTA в CS.MAP.001.

**Действия:**
- Извлекает метаданные из YAML
- Добавляет в таблицу "Полный список"
- Добавляет в таблицу "По структуре папок"
- Обновляет счётчики и дату

### `verify-sota-index.sh`

Проверяет консистентность индекса.

```bash
bash scripts/verify-sota-index.sh        # Проверка
bash scripts/verify-sota-index.sh --fix  # Исправление
```

---

## 📊 Структура SoTA (Шаблон v1.4)

```markdown
---
# 1. YAML FRONTMATTER
id: CS.SOTA.XXX
type: sota
domain: cattle-science
area: [reproduction|feeding|health|economics|management]
year: YYYY
authors: "..."
title: "..."
journal: "..."
doi: "..."
tags: [...]
related: [...]
---

# 2. РЕЗЮМЕ
# 3. KEY CLAIMS (2+ с Evidence/Confidence)
# 4. ВВЕДЕНИЕ
# 5. МАТЕРИАЛЫ И МЕТОДЫ
# 6. РЕЗУЛЬТАТЫ
# 7. ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ
# 8. МАТЕРИАЛЫ ДЛЯ ЛЕКЦИЙ
# 9. ВЫВОДЫ
# 10. КРИТИЧЕСКИЙ АНАЛИЗ
# 11. REVISION CRITERION
# 12. FAQ
# 13. ИНСТРУМЕНТЫ И ШАБЛОНЫ
# 14. ИСТОЧНИКИ
# 15. ЖУРНАЛ ОБРАБОТКИ
```

---

## ⚠️ Troubleshooting

### Hook не срабатывает

```bash
# Проверить путь к hooks
git config core.hooksPath  # должен быть: .githooks

# Проверить права
ls -la .githooks/post-commit  # должен быть executable

# Переустановить
git config core.hooksPath .githooks
chmod +x .githooks/post-commit
```

### Entity Integration не работает

```bash
# Проверить Python
python3 --version

# Проверить зависимости
cd pack/cattle-science/02-domain-entities
python3 scripts/wp75-entity-integration.py --help
```

### Индекс не обновляется

```bash
# Ручная проверка
bash scripts/verify-sota-index.sh

# Ручное добавление
bash scripts/add-sota-to-index.sh <path-to-file>
```

---

## 📈 Архитектура

```
┌─────────────────────────────────────────────────────────────┐
│                     Git Hook: post-commit                   │
│  ┌─────────────────┐  ┌─────────────────┐                   │
│  │   Validation    │→│  Index Update   │                   │
│  │  (template.sh)  │  │ (add-to-index)  │                   │
│  └─────────────────┘  └─────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                 Session Close (manual)                      │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │
│  │  Validate   │→│ Index Check │→│ Entity Integration  │  │
│  │   (all)     │  │  (verify)   │  │  (wp75-*.py)        │  │
│  └─────────────┘  └─────────────┘  └─────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Git Commit + Push                        │
└─────────────────────────────────────────────────────────────┘
```

---

## 📝 Лог изменений

| Дата | Версия | Изменения |
|------|--------|-----------|
| 2026-04-01 | 1.0 | Создание системы автоматизации |
| | | Валидация шаблона |
| | | Автоматическое обновление индекса |
| | | Session Close скрипт |

---

*PACK-cattle-science | Exocortex-V2*
