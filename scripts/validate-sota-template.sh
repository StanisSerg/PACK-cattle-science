#!/bin/bash
# validate-sota-template.sh — Валидация SoTA по шаблону
#
# Использование:
#   bash scripts/validate-sota-template.sh <path-to-sota-file>
#   bash scripts/validate-sota-template.sh --all              # Проверить все SoTA
#   bash scripts/validate-sota-template.sh --batch ID1,ID2    # Пакетная проверка

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Обязательные разделы (по шаблону v1.4)
REQUIRED_SECTIONS=(
    "РЕЗЮМЕ"
    "ВВЕДЕНИЕ"
    "МАТЕРИАЛЫ И МЕТОДЫ"
    "РЕЗУЛЬТАТЫ"
    "ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ"
    "МАТЕРИАЛЫ ДЛЯ ЛЕКЦИЙ"
    "ВЫВОДЫ"
    "КРИТИЧЕСКИЙ АНАЛИЗ"
    "FAQ"
    "ИНСТРУМЕНТЫ"
    "ИСТОЧНИКИ"
    "ЖУРНАЛ ОБРАБОТКИ"
)

# Обязательные поля YAML
REQUIRED_YAML=(
    "id:"
    "type:"
    "domain:"
    "area:"
    "year:"
    "authors:"
    "title:"
    "journal:"
    "doi:"
    "tags:"
    "related:"
)

validate_file() {
    local file="$1"
    local filename=$(basename "$file")
    local ERRORS=0
    local WARNINGS=0
    
    echo -e "${BLUE}=== Валидация: $filename ===${NC}"
    
    # Проверка существования файла
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ Файл не найден: $file${NC}"
        return 1
    fi
    
    # Проверка имени файла
    if [[ ! "$filename" =~ ^CS\.SOTA\.[0-9]+-[a-z]+-[0-9]{4}\.md$ ]]; then
        echo -e "${YELLOW}⚠️  Имя файла не соответствует шаблону CS.SOTA.XXX-author-year.md${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Проверка YAML frontmatter
    echo -e "\n${BLUE}Проверка YAML frontmatter...${NC}"
    
    # Проверка наличия --- в начале
    if ! head -1 "$file" | grep -q "^---"; then
        echo -e "${RED}❌ Отсутствует открывающий '---' для YAML${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    for field in "${REQUIRED_YAML[@]}"; do
        if ! grep -q "^$field" "$file"; then
            echo -e "${RED}❌ Отсутствует обязательное поле YAML: $field${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
    
    # Проверка структуры разделов
    echo -e "\n${BLUE}Проверка структуры разделов...${NC}"
    
    local found_sections=0
    for section in "${REQUIRED_SECTIONS[@]}"; do
        if grep -qi "^#.*$section" "$file"; then
            found_sections=$((found_sections + 1))
        else
            echo -e "${RED}❌ Отсутствует раздел: $section${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
    
    echo -e "${GREEN}✅ Найдено разделов: $found_sections/${#REQUIRED_SECTIONS[@]}${NC}"
    
    # Проверка Key Claims (опционально — не входит в обязательные разделы v1.4)
    echo -e "\n${BLUE}Проверка Key Claims...${NC}"
    
    local claim_count=$(grep -c "^## Claim" "$file" 2>/dev/null || true)
    if [ "$claim_count" -ge 2 ]; then
        echo -e "${GREEN}✅ Key Claims: $claim_count${NC}"
        if ! grep -q "Evidence:" "$file"; then
            echo -e "${YELLOW}⚠️  Отсутствуют поля Evidence в Key Claims${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
        if ! grep -q "Confidence:" "$file"; then
            echo -e "${YELLOW}⚠️  Отсутствуют поля Confidence в Key Claims${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    else
        echo -e "${YELLOW}⚠️  Key Claims отсутствуют или менее 2 (опционально для v1.4)${NC}"
    fi
    
    # Проверка журнала обработки
    echo -e "\n${BLUE}Проверка журнала обработки...${NC}"
    
    if ! grep -q "ЖУРНАЛ ОБРАБОТКИ" "$file"; then
        echo -e "${RED}❌ Отсутствует журнал обработки${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # Проверка связей (related)
    echo -e "\n${BLUE}Проверка связей...${NC}"
    
    local related_count=$(grep -A 100 "^related:" "$file" | grep -c "^- id:" || true)
    if [ "$related_count" -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Нет связей с другими SoTA (related)${NC}"
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "${GREEN}✅ Связей: $related_count${NC}"
    fi
    
    # Проверка медиа-инвентаря
    echo -e "\n${BLUE}Проверка медиа-инвентаря...${NC}"
    
    local screenshot_count=$(grep -c "\[СКРИНШОТ\]" "$file" 2>/dev/null || true)
    if [ "$screenshot_count" -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Нет медиа-элементов ([СКРИНШОТ])${NC}"
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "${GREEN}✅ Медиа-элементов: $screenshot_count${NC}"
    fi
    
    # Итог
    echo -e "\n${BLUE}=== Результат ===${NC}"
    if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ SoTA полностью соответствует шаблону${NC}"
        return 0
    elif [ $ERRORS -eq 0 ]; then
        echo -e "${YELLOW}⚠️  SoTA соответствует с замечаниями ($WARNINGS warnings)${NC}"
        return 0
    else
        echo -e "${RED}❌ SoTA НЕ соответствует шаблону ($ERRORS errors, $WARNINGS warnings)${NC}"
        return 1
    fi
}

# Обработка аргументов
case "$1" in
    --all)
        echo -e "${BLUE}=== Пакетная проверка всех SoTA ===${NC}\n"
        FAILED=0
        for file in "$PACK_DIR"/06-sota/*/*.md; do
            if [ -f "$file" ]; then
                if ! validate_file "$file"; then
                    FAILED=$((FAILED + 1))
                fi
                echo ""
            fi
        done
        echo -e "\n${BLUE}=== Итог пакетной проверки ===${NC}"
        echo "Не прошли валидацию: $FAILED"
        exit $FAILED
        ;;
    
    --batch)
        if [ -z "$2" ]; then
            echo "Укажите ID через запятую: --batch CS.SOTA.001,CS.SOTA.002"
            exit 1
        fi
        IFS=',' read -ra IDS <<< "$2"
        FAILED=0
        for id in "${IDS[@]}"; do
            # Найти файл по ID
            file=$(find "$PACK_DIR"/06-sota -name "$id*.md" 2>/dev/null | head -1)
            if [ -n "$file" ]; then
                if ! validate_file "$file"; then
                    FAILED=$((FAILED + 1))
                fi
            else
                echo -e "${RED}❌ Файл не найден для $id${NC}"
                FAILED=$((FAILED + 1))
            fi
            echo ""
        done
        exit $FAILED
        ;;
    
    "")
        echo "Использование:"
        echo "  bash scripts/validate-sota-template.sh <path-to-file>"
        echo "  bash scripts/validate-sota-template.sh --all"
        echo "  bash scripts/validate-sota-template.sh --batch ID1,ID2,ID3"
        exit 1
        ;;
    
    *)
        validate_file "$1"
        exit $?
        ;;
esac
