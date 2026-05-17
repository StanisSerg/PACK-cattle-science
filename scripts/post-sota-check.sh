#!/bin/bash
#
# Post-SoTA Creation Check v2.0
# Запускается после создания нового SoTA для комплексной проверки
#
# Usage:
#   ./scripts/post-sota-check.sh [sota_id]
#   ./scripts/post-sota-check.sh --last        # проверить последний созданный SoTA
#   ./scripts/post-sota-check.sh --full        # полная проверка со структурой, FPF и ArchGate

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR/.."

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

FULL_MODE=false
SOTA_ID=""

# Разбор аргументов
if [ "$1" == "--last" ]; then
    SOTA_ID=$(find pack/cattle-science/06-sota -name "CS.SOTA.*.md" -type f -printf '%T@ %p\n' | sort -n | tail -1 | grep -oP 'CS\.SOTA\.\K[0-9]+' || echo "")
    if [ -z "$SOTA_ID" ]; then
        echo -e "${RED}❌ SoTA файлы не найдены${NC}"
        exit 1
    fi
    echo -e "${BLUE}📄 Последний созданный SoTA: CS.SOTA.$SOTA_ID${NC}"
elif [ "$1" == "--full" ]; then
    FULL_MODE=true
    if [ -n "$2" ]; then
        SOTA_ID="$2"
        echo -e "${BLUE}📄 Полная проверка SoTA: CS.SOTA.$SOTA_ID${NC}"
    else
        SOTA_ID=$(find pack/cattle-science/06-sota -name "CS.SOTA.*.md" -type f -printf '%T@ %p\n' | sort -n | tail -1 | grep -oP 'CS\.SOTA\.\K[0-9]+' || echo "")
        if [ -z "$SOTA_ID" ]; then
            echo -e "${RED}❌ SoTA файлы не найдены${NC}"
            exit 1
        fi
        echo -e "${BLUE}📄 Полная проверка последнего SoTA: CS.SOTA.$SOTA_ID${NC}"
    fi
elif [ -n "$1" ]; then
    SOTA_ID="$1"
    # Убираем ведущие нули если есть
    SOTA_ID=$(echo "$SOTA_ID" | sed 's/^0*//')
    echo -e "${BLUE}📄 Проверка SoTA: CS.SOTA.$SOTA_ID${NC}"
else
    echo "Usage:"
    echo "  $0 <sota_id>       # Проверить конкретный SoTA (entities + links)"
    echo "  $0 --last          # Проверить последний созданный"
    echo "  $0 --full [id]     # Полная проверка: entities + structure + FPF + ArchGate"
    exit 1
fi

# Находим файл
SOTA_FILE=$(find pack/cattle-science/06-sota -name "CS.SOTA.${SOTA_ID}*.md" -type f | head -1)
if [ -z "$SOTA_FILE" ]; then
    echo -e "${RED}❌ Файл SoTA не найден для ID $SOTA_ID${NC}"
    exit 1
fi

echo ""
echo "═══════════════════════════════════════════════════════════════"
echo "  🔍 POST-SOTA CHECK v2.0"
echo "═══════════════════════════════════════════════════════════════"
echo ""

# ═══════════════════════════════════════════════════════════════
# Шаг 1: Структурная валидация (только в --full режиме)
# ═══════════════════════════════════════════════════════════════
if [ "$FULL_MODE" = true ]; then
    # Определяем тип SoTA: Chapter если есть book_title/chapter_number/isbn, иначе Article
    if head -30 "$SOTA_FILE" 2>/dev/null | grep -qE "book_title:|chapter_number:|isbn:"; then
        echo "═══════════════════════════════════════════════════════════════"
        echo "  Шаг 1: Структурная валидация (Chapter-SoTA)"
        echo "═══════════════════════════════════════════════════════════════"
        bash scripts/validate-chapter-sota.sh "$SOTA_FILE" || true
    else
        echo "═══════════════════════════════════════════════════════════════"
        echo "  Шаг 1: Структурная валидация (Article-SoTA v1.1)"
        echo "═══════════════════════════════════════════════════════════════"
        bash scripts/validate-article-sota.sh "$SOTA_FILE" || true
    fi
    echo ""
fi

# ═══════════════════════════════════════════════════════════════
# Шаг 2: Анализ сущностей
# ═══════════════════════════════════════════════════════════════
echo "═══════════════════════════════════════════════════════════════"
echo "  Шаг 2: Анализ сущностей в SoTA"
echo "═══════════════════════════════════════════════════════════════"
python3 scripts/analyze-sota-entities.py "$SOTA_ID" || true
echo ""

# ═══════════════════════════════════════════════════════════════
# Шаг 3: Проверка связей (DRY-RUN)
# ═══════════════════════════════════════════════════════════════
echo "═══════════════════════════════════════════════════════════════"
echo "  Шаг 3: Проверка связей (DRY-RUN)"
echo "═══════════════════════════════════════════════════════════════"
python3 scripts/update-entity-links.py "$SOTA_ID" --dry-run || true
echo ""

# ═══════════════════════════════════════════════════════════════
# Шаг 4: FPF-проверка (только в --full режиме)
# ═══════════════════════════════════════════════════════════════
if [ "$FULL_MODE" = true ]; then
    echo "═══════════════════════════════════════════════════════════════"
    echo "  Шаг 4: FPF-проверка соответствия"
    echo "═══════════════════════════════════════════════════════════════"
    bash scripts/check-fpf.sh "$SOTA_FILE" || true
    echo ""
fi

# ═══════════════════════════════════════════════════════════════
# Шаг 5: ArchGate-оценка (только в --full режиме)
# ═══════════════════════════════════════════════════════════════
if [ "$FULL_MODE" = true ]; then
    echo "═══════════════════════════════════════════════════════════════"
    echo "  Шаг 5: ArchGate-оценка качества"
    echo "═══════════════════════════════════════════════════════════════"
    bash scripts/check-archgate.sh "$SOTA_FILE" || true
    echo ""
fi

# ═══════════════════════════════════════════════════════════════
# Рекомендации
# ═══════════════════════════════════════════════════════════════
echo "═══════════════════════════════════════════════════════════════"
echo "  📋 РЕКОМЕНДАЦИИ"
echo "═══════════════════════════════════════════════════════════════"
echo ""
if [ "$FULL_MODE" = true ]; then
    echo "✅ Полная проверка завершена (structure + entities + FPF + ArchGate)"
    echo ""
    echo "Если все проверки пройдены:"
    echo "  git add -A && git commit -m 'feat(sota): CS.SOTA.$SOTA_ID — создан и проверен'"
    echo ""
else
    echo "✅ Базовая проверка завершена (entities + links)"
    echo ""
    echo "Для полной проверки со структурой, FPF и ArchGate:"
    echo "  bash scripts/post-sota-check.sh --full $SOTA_ID"
    echo ""
fi

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
