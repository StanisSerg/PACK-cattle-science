#!/bin/bash
#
# Post-SoTA Creation Check
# Запускается после создания нового SoTA для проверки сущностей
#
# Usage:
#   ./scripts/post-sota-check.sh [sota_id]
#   ./scripts/post-sota-check.sh --last  # проверить последний созданный SoTA

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "═══════════════════════════════════════════════════════════════"
echo "  🔍 POST-SOTA ENTITY CHECK"
echo "═══════════════════════════════════════════════════════════════"

# Определяем SoTA для проверки
if [ "$1" == "--last" ]; then
    # Находим последний созданный SoTA
    SOTA_ID=$(find pack/cattle-science/06-sota -name "CS.SOTA.*.md" -type f -printf '%T@ %p\n' | sort -n | tail -1 | grep -oP 'CS\.SOTA\.\K\d+' || echo "")
    if [ -z "$SOTA_ID" ]; then
        echo "❌ SoTA файлы не найдены"
        exit 1
    fi
    echo "📄 Последний созданный SoTA: CS.SOTA.$SOTA_ID"
elif [ -n "$1" ]; then
    SOTA_ID="$1"
    # Убираем ведущие нули если есть
    SOTA_ID=$(echo "$SOTA_ID" | sed 's/^0*//')
    echo "📄 Проверка SoTA: CS.SOTA.$SOTA_ID"
else
    echo "Usage:"
    echo "  $0 <sota_id>     # Проверить конкретный SoTA"
    echo "  $0 --last        # Проверить последний созданный"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Шаг 1: Анализ сущностей в SoTA"
echo "═══════════════════════════════════════════════════════════════"
python3 scripts/analyze-sota-entities.py "$SOTA_ID"

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  Шаг 2: Проверка связей (DRY-RUN)"
echo "═══════════════════════════════════════════════════════════════"
python3 scripts/update-entity-links.py "$SOTA_ID" --dry-run

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  📋 РЕКОМЕНДАЦИИ"
echo "═══════════════════════════════════════════════════════════════"
echo ""
echo "1. Проверьте список найденных сущностей выше"
echo "2. Если нужно создать новые сущности, используйте шаблон:"
echo "   pack/cattle-science/02-domain-entities/00-entity-template.md"
echo ""
echo "3. Для автоматического обновления связей выполните:"
echo "   python3 scripts/update-entity-links.py $SOTA_ID"
echo ""
echo "4. После создания новых сущностей, обновите инвентарь:"
echo "   python3 scripts/reindex-entities.py"
echo ""
echo "5. Обновите интерпретации в файлах 02B*.md"
echo ""
echo "═══════════════════════════════════════════════════════════════"
