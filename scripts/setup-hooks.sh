#!/bin/bash
# setup-hooks.sh — Настройка git hooks для автоматического обновления индекса

echo "=== Настройка git hooks для PACK-cattle-science ==="
echo ""

# Проверяем, что мы в git-репозитории
if [ ! -d ".git" ]; then
    echo "Ошибка: Не найдена папка .git"
    echo "Запустите из корня репозитория PACK-cattle-science"
    exit 1
fi

# Настройка hooksPath
echo "Настройка core.hooksPath..."
git config core.hooksPath .githooks

# Проверка
if [ "$(git config core.hooksPath)" = ".githooks" ]; then
    echo "✅ Hooks настроены: .githooks"
else
    echo "❌ Ошибка настройки hooks"
    exit 1
fi

# Проверка наличия hook-файлов
if [ -f ".githooks/post-commit" ]; then
    echo "✅ Найден: post-commit hook"
else
    echo "⚠️  Не найден: post-commit hook"
fi

if [ -f ".githooks/pre-commit" ]; then
    echo "✅ Найден: pre-commit hook"
else
    echo "⚠️  Не найден: pre-commit hook"
fi

echo ""
echo "=== Готово ==="
echo ""
echo "Теперь при каждом коммите с новой SoTA:"
echo "  1. Автоматически обновится CS.MAP.001-sota-index.md"
echo "  2. Индекс добавится в тот же коммит"
echo ""
echo "Проверка работы:"
echo "  bash scripts/verify-sota-index.sh"
