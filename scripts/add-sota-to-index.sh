#!/bin/bash
# add-sota-to-index.sh — Автоматическое добавление SoTA в индекс
#
# Использование:
#   bash scripts/add-sota-to-index.sh <path-to-sota-file>
#   Пример: bash scripts/add-sota-to-index.sh pack/cattle-science/06-sota/health/CS.SOTA.060-capel-2021.md

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"
INDEX_FILE="$PACK_DIR/07-map/CS.MAP.001-sota-index.md"

# Цвета для вывода
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Проверка аргументов
if [ $# -eq 0 ]; then
    echo -e "${RED}Ошибка: Укажите путь к SoTA-файлу${NC}"
    echo "Использование: bash scripts/add-sota-to-index.sh <path-to-sota-file>"
    exit 1
fi

SOTA_FILE="$1"

if [ ! -f "$SOTA_FILE" ]; then
    echo -e "${RED}Ошибка: Файл не найден: $SOTA_FILE${NC}"
    exit 1
fi

echo -e "${BLUE}=== Добавление SoTA в индекс ===${NC}"
echo "Файл: $SOTA_FILE"
echo ""

# Извлечение метаданных из YAML frontmatter
extract_yaml() {
    local key="$1"
    grep -m 1 "^$key:" "$SOTA_FILE" | sed 's/^[^:]*: //' | sed 's/^"//;s/"$//' | sed "s/^'//;s/'$//"
}

ID=$(extract_yaml "id")
AUTHORS=$(extract_yaml "authors")
YEAR=$(extract_yaml "year")
TITLE=$(extract_yaml "title")
CATEGORY=$(extract_yaml "category")
AREA=$(extract_yaml "area")

# Извлечение фамилии первого автора
FIRST_AUTHOR=$(echo "$AUTHORS" | sed 's/,.*//' | sed 's/ .*//')

# Определение раздела в индексе по area
case "$AREA" in
    reproduction)
        SECTION="Репродуктивный менеджмент"
        FOLDER="reproduction"
        ;;
    feeding)
        SECTION="Кормление и метаболизм"
        FOLDER="feeding"
        ;;
    health)
        SECTION="Здоровье и метаболизм"
        FOLDER="health"
        ;;
    economics)
        SECTION="Экономика"
        FOLDER="economics"
        ;;
    management)
        SECTION="Менеджмент"
        FOLDER="management"
        ;;
    *)
        SECTION="Здоровье и метаболизм"
        FOLDER="health"
        ;;
esac

echo -e "${BLUE}Извлечённые метаданные:${NC}"
echo "  ID: $ID"
echo "  Автор: $FIRST_AUTHOR"
echo "  Год: $YEAR"
echo "  Раздел: $SECTION"
echo "  Папка: $FOLDER"
echo ""

# Проверка, есть ли уже в индексе
if grep -q "$ID" "$INDEX_FILE"; then
    echo -e "${YELLOW}⚠️  SoTA $ID уже присутствует в индексе${NC}"
    echo "Пропуск добавления."
    exit 0
fi

# Формирование строк для таблиц
# 1. Для "Полного списка SoTA"
# Формат: | CS.SOTA.XXX | Author | Year | Type | Tags | Key result |

# Извлечение первого тега для краткости
FIRST_TAG=$(grep -A 20 "^tags:" "$SOTA_FILE" | grep "^- " | head -1 | sed 's/^- //' | sed 's/^#//' || echo "general")

# Краткое название (первые 3-4 слова из title)
SHORT_TITLE=$(echo "$TITLE" | cut -d' ' -f1-4 | sed 's/ $//')

# Строка для полного списка
FULL_LIST_ROW="| $ID | $FIRST_AUTHOR | $YEAR | $CATEGORY | \`#$FIRST_TAG\` | $SHORT_TITLE... |"

# 2. Для "По структуре папок"
# Формат: | CS.SOTA.XXX-author-year.md | XXX | Description |
FILENAME=$(basename "$SOTA_FILE")
DESCRIPTION=$(echo "$SHORT_TITLE" | sed 's/"//g')
FOLDER_ROW="| $FILENAME | ${ID##*.} | $DESCRIPTION |"

echo -e "${BLUE}Строки для добавления:${NC}"
echo "  [Полный список]: $FULL_LIST_ROW"
echo "  [По структуре]:  $FOLDER_ROW"
echo ""

# Добавление в "Полный список SoTA"
echo -e "${BLUE}Добавление в 'Полный список SoTA'...${NC}"

# Найти строку с заголовком раздела и добавить после неё
SECTION_PATTERN="### $SECTION"
if grep -q "$SECTION_PATTERN" "$INDEX_FILE"; then
    # Найти последнюю строку таблицы в этом разделе
    # Используем awk для точного позиционирования
    awk -v section="$SECTION" -v row="$FULL_LIST_ROW" '
        BEGIN { in_section = 0; table_end = 0 }
        /^### / { in_section = 0 }
        $0 ~ "^### " section { in_section = 1 }
        in_section && /^\|.*\|.*\|/ && !/^\|.*---.*\|/ { last_table_row = NR }
        in_section && /^$/ && last_table_row > 0 { 
            if (!printed) {
                print row
                printed = 1
            }
        }
        { print }
    ' "$INDEX_FILE" > "$INDEX_FILE.tmp" && mv "$INDEX_FILE.tmp" "$INDEX_FILE"
    echo -e "${GREEN}✅ Добавлено в полный список${NC}"
else
    echo -e "${YELLOW}⚠️  Раздел '$SECTION' не найден в индексе${NC}"
fi

# Добавление в "По структуре папок"
echo -e "${BLUE}Добавление в 'По структуре папок'...${NC}"

FOLDER_PATTERN="### \`$FOLDER/\`"
if grep -q "$FOLDER_PATTERN" "$INDEX_FILE"; then
    awk -v folder="$FOLDER" -v row="$FOLDER_ROW" '
        BEGIN { in_folder = 0 }
        /^### / && /\`.*\`/ { in_folder = 0 }
        $0 ~ "^### \\`" folder "/\\`" { in_folder = 1 }
        in_folder && /^\|.*\|.*\|.*\|/ && !/^\|.*---.*\|/ { last_table_row = NR }
        in_folder && /^$/ && last_table_row > 0 {
            if (!printed) {
                print row
                printed = 1
            }
        }
        { print }
    ' "$INDEX_FILE" > "$INDEX_FILE.tmp" && mv "$INDEX_FILE.tmp" "$INDEX_FILE"
    echo -e "${GREEN}✅ Добавлено в структуру папок${NC}"
else
    echo -e "${YELLOW}⚠️  Папка '$FOLDER' не найдена в индексе${NC}"
fi

# Обновление счётчиков
echo -e "${BLUE}Обновление счётчиков...${NC}"

# Подсчёт нового количества файлов
NEW_TOTAL=$(find "$PACK_DIR/06-sota" -name "CS.SOTA.*.md" | wc -l)
NEW_FOLDER_COUNT=$(find "$PACK_DIR/06-sota/$FOLDER" -name "CS.SOTA.*.md" 2>/dev/null | wc -l || echo "0")

# Обновление общего счётчика
sed -i "s/Всего SoTA:\*\* [0-9]\+/Всего SoTA:** $NEW_TOTAL/" "$INDEX_FILE"

# Обновление счётчика папки
sed -i "s/\`$FOLDER\/\` — [0-9]\+/\`$FOLDER\/\` — $NEW_FOLDER_COUNT/" "$INDEX_FILE"

# Обновление даты
TODAY=$(date +%Y-%m-%d)
sed -i "s/Последнее обновление: [0-9]\{4\}-[0-9]\{2\}-[0-9]\{2\}/Последнее обновление: $TODAY/" "$INDEX_FILE"

echo -e "${GREEN}✅ Счётчики обновлены:${NC}"
echo "  Всего SoTA: $NEW_TOTAL"
echo "  $FOLDER/: $NEW_FOLDER_COUNT"
echo "  Дата: $TODAY"
echo ""

# Проверка
echo -e "${BLUE}Проверка...${NC}"
if grep -q "$ID" "$INDEX_FILE"; then
    echo -e "${GREEN}✅ SoTA $ID успешно добавлена в индекс${NC}"
else
    echo -e "${RED}❌ Ошибка: SoTA $ID не найдена в индексе после добавления${NC}"
    exit 1
fi

echo ""
echo -e "${GREEN}=== Готово ===${NC}"
echo "Не забудьте закоммитить изменения:"
echo "  git add 07-map/CS.MAP.001-sota-index.md"
echo "  git commit -m \"index: add $ID to CS.MAP.001\""
