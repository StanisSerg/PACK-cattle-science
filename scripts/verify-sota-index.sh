#!/bin/bash
# verify-sota-index.sh — Проверка соответствия индекса и фактических файлов
#
# Использование:
#   bash scripts/verify-sota-index.sh              # Проверка
#   bash scripts/verify-sota-index.sh --fix        # Предложить исправления

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"
SOTA_DIR="$PACK_DIR/06-sota"
INDEX_FILE="$PACK_DIR/07-map/CS.MAP.001-sota-index.md"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "=== Проверка индекса SoTA ==="
echo ""

# Подсчёт файлов по папкам
declare -A FOLDER_COUNTS
declare -A INDEX_COUNTS

for folder in reproduction feeding health economics management; do
    if [ -d "$SOTA_DIR/$folder" ]; then
        count=$(find "$SOTA_DIR/$folder" -name "CS.SOTA.*.md" | wc -l)
        FOLDER_COUNTS[$folder]=$count
    else
        FOLDER_COUNTS[$folder]=0
    fi
done

# Подсчёт в индексе
echo "Проверка счётчиков в индексе..."
echo ""

# Извлечение счётчиков из индекса
INDEX_TOTAL=$(grep -oP 'Всего SoTA:\*\* \K[0-9]+' "$INDEX_FILE" 2>/dev/null || echo "0")

echo "📊 Сравнение счётчиков:"
echo ""
printf "%-15s %-10s %-10s %-10s\n" "Папка" "Факт" "Индекс" "Статус"
echo "-------------------------------------------"

# Проверка каждой папки
for folder in reproduction feeding health economics management; do
    actual=${FOLDER_COUNTS[$folder]:-0}
    
    # Поиск в индексе
    index_count=$(grep -oP "\`$folder/\` — \K[0-9]+" "$INDEX_FILE" 2>/dev/null || echo "0")
    
    if [ "$actual" -eq "$index_count" ]; then
        status="${GREEN}OK${NC}"
    else
        status="${RED}FAIL${NC}"
    fi
    
    printf "%-15s %-10s %-10s %-10b\n" "$folder/" "$actual" "$index_count" "$status"
done

echo ""

# Проверка общего количества
TOTAL_ACTUAL=$(find "$SOTA_DIR" -name "CS.SOTA.*.md" | wc -l)

echo "📈 Общее количество:"
echo "  Фактически:  $TOTAL_ACTUAL файлов"
echo "  В индексе:   $INDEX_TOTAL файлов"

if [ "$TOTAL_ACTUAL" -eq "$INDEX_TOTAL" ]; then
    echo -e "  Статус:      ${GREEN}OK${NC}"
else
    echo -e "  Статус:      ${RED}FAIL (разница: $((TOTAL_ACTUAL - INDEX_TOTAL)))${NC}"
fi

echo ""

# Поиск файлов, отсутствующих в индексе
echo "🔍 Проверка наличия файлов в индексе..."
echo ""

MISSING=0
while IFS= read -r file; do
    filename=$(basename "$file")
    id=$(echo "$filename" | grep -oP 'CS\.SOTA\.\d+')
    
    if ! grep -q "$id" "$INDEX_FILE"; then
        echo -e "${RED}MISSING:${NC} $filename"
        MISSING=$((MISSING + 1))
    fi
done < <(find "$SOTA_DIR" -name "CS.SOTA.*.md")

if [ $MISSING -eq 0 ]; then
    echo -e "${GREEN}OK: Все файлы в индексе${NC}"
else
    echo ""
    echo -e "${RED}Найдено $MISSING файлов без индекса${NC}"
fi

echo ""

# Поиск ID в индексе, отсутствующих как файлы
echo "🔍 Проверка висячих ссылок..."
echo ""

ORPHAN=0
for id in $(grep -oP 'CS\.SOTA\.\d+' "$INDEX_FILE" | sort -u); do
    if ! find "$SOTA_DIR" -name "$id*.md" | grep -q .; then
        echo -e "${YELLOW}ORPHAN:${NC} $id (нет файла)"
        ORPHAN=$((ORPHAN + 1))
    fi
done

if [ $ORPHAN -eq 0 ]; then
    echo -e "${GREEN}OK: Нет висячих ссылок${NC}"
else
    echo ""
    echo -e "${YELLOW}Найдено $ORPHAN висячих ссылок${NC}"
fi

echo ""
echo "=== Проверка завершена ==="

# Выход с ошибкой, если есть проблемы
if [ $MISSING -gt 0 ] || [ $ORPHAN -gt 0 ] || [ "$TOTAL_ACTUAL" -ne "$INDEX_TOTAL" ]; then
    exit 1
fi

exit 0
