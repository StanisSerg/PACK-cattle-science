#!/bin/bash
#
# validate-chapter-sota.sh — Валидация chapter-based SoTA (NASEM/NRC book chapters)
#
# Использование:
#   bash scripts/validate-chapter-sota.sh <path-to-sota-file>
#   bash scripts/validate-chapter-sota.sh --last              # Последний созданный SoTA
#   bash scripts/validate-chapter-sota.sh --all               # Все chapter-based SoTA
#
# Проверяет соответствие шаблону SOTA-CHAPTER-EXPANDED-TEMPLATE.md v1.2

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Обязательные поля YAML для book chapter
REQUIRED_YAML=(
    "id:"
    "type:"
    "domain:"
    "area:"
    "year:"
    "authors:"
    "title:"
    "book_title:"
    "chapter_number:"
    "publisher:"
    "isbn:"
    "doi:"
    "pages:"
    "tags:"
    "related:"
)

# Обязательные секции для chapter-based SoTA (expanded format)
REQUIRED_SECTIONS=(
    "Аннотация"
    "КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ"
    "ВВЕДЕНИЕ"
    "МЕТОДОЛОГИЯ"
    "ИЛЛЮСТРАТИВНЫЕ РАСЧЁТЫ"
    "ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ"
    "КРИТИЧЕСКИЙ АНАЛИЗ"
    "FAQ"
    "ИСТОЧНИКИ"
    "ЖУРНАЛ ОБРАБОТКИ"
)

validate_file() {
    local file="$1"
    local filename=$(basename "$file")
    local ERRORS=0
    local WARNINGS=0
    local INFOS=0
    
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  📋 VALIDATE CHAPTER-SoTA: $filename${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ Файл не найден: $file${NC}"
        return 1
    fi
    
    # ── YAML frontmatter ──
    echo -e "\n${CYAN}── YAML Frontmatter ──${NC}"
    
    if ! head -1 "$file" | grep -q "^---"; then
        echo -e "${RED}❌ Отсутствует открывающий '---' для YAML${NC}"
        ERRORS=$((ERRORS + 1))
    else
        echo -e "${GREEN}✅ YAML frontmatter присутствует${NC}"
    fi
    
    for field in "${REQUIRED_YAML[@]}"; do
        if ! grep -q "^$field" "$file"; then
            echo -e "${RED}❌ Отсутствует обязательное поле YAML: $field${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
    
    # Проверка sota_edition
    if ! grep -q "sota_edition:" "$file"; then
        echo -e "${YELLOW}⚠️  Отсутствует sota_edition (рекомендуется)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Проверка freshness_window
    if ! grep -q "freshness_window:" "$file"; then
        echo -e "${YELLOW}⚠️  Отсутствует freshness_window (рекомендуется)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Структура разделов ──
    echo -e "\n${CYAN}── Структура разделов ──${NC}"
    
    local found_sections=0
    for section in "${REQUIRED_SECTIONS[@]}"; do
        if grep -qi "^## .*$section" "$file"; then
            found_sections=$((found_sections + 1))
        else
            echo -e "${RED}❌ Отсутствует раздел: $section${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
    echo -e "${GREEN}✅ Найдено разделов: $found_sections/${#REQUIRED_SECTIONS[@]}${NC}"
    
    # ─— Expanded-формат: физиологические разделы —─
    echo -e "\n${CYAN}── Expanded-формат (физиология + обоснования) ──${NC}"
    
    local phys_count=$(grep -c "Физиология и механизмы" "$file" 2>/dev/null || echo 0)
    local obos_count=$(grep -c "Обоснование" "$file" 2>/dev/null || echo 0)
    local evol_count=$(grep -c "Эволюция модели" "$file" 2>/dev/null || echo 0)
    local clinic_count=$(grep -c "Клинический контекст" "$file" 2>/dev/null || echo 0)
    
    echo -e "${GREEN}📊 Физиологических разделов: $phys_count${NC}"
    echo -e "${GREEN}📊 Блоков 'Обоснование': $obos_count${NC}"
    echo -e "${GREEN}📊 Таблиц эволюции модели: $evol_count${NC}"
    echo -e "${GREEN}📊 Клинических контекстов: $clinic_count${NC}"
    
    if [ "$phys_count" -lt 3 ]; then
        echo -e "${YELLOW}⚠️  Мало физиологических разделов (ожидается ≥3 для expanded)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if [ "$obos_count" -lt 5 ]; then
        echo -e "${YELLOW}⚠️  Мало блоков 'Обоснование' (ожидается ≥5 для expanded)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Key Claims ──
    echo -e "\n${CYAN}── Ключевые утверждения ──${NC}"
    
    local claim_headers=$(grep -c "^### Утверждение" "$file" 2>/dev/null || echo 0)
    if [ "$claim_headers" -ge 2 ]; then
        echo -e "${GREEN}✅ Key Claims: $claim_headers${NC}"
    else
        echo -e "${YELLOW}⚠️  Key Claims отсутствуют или менее 2${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Связи (related) ──
    echo -e "\n${CYAN}── Связи с другими SoTA ──${NC}"
    
    local related_count=$(grep -A 100 "^related:" "$file" | grep -cE "^\s*- id:" || true)
    if [ "$related_count" -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Нет связей с другими SoTA (related)${NC}"
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "${GREEN}✅ Связей: $related_count${NC}"
    fi
    
    # ── Медиа ──
    echo -e "\n${CYAN}── Медиа-инвентарь ──${NC}"
    
    local media_count=$(grep -c "!\[" "$file" 2>/dev/null || echo 0)
    if [ "$media_count" -eq 0 ]; then
        echo -e "${YELLOW}⚠️  Нет медиа-элементов (скриншотов/таблиц)${NC}"
        WARNINGS=$((WARNINGS + 1))
    else
        echo -e "${GREEN}✅ Медиа-элементов: $media_count${NC}"
    fi
    
    # ── Журнал обработки ──
    echo -e "\n${CYAN}── Журнал обработки ──${NC}"
    
    if ! grep -q "ЖУРНАЛ ОБРАБОТКИ" "$file"; then
        echo -e "${RED}❌ Отсутствует журнал обработки${NC}"
        ERRORS=$((ERRORS + 1))
    else
        echo -e "${GREEN}✅ Журнал обработки присутствует${NC}"
    fi
    
    # Проверка наличия Work Record
    if ! grep -q "Work Record" "$file"; then
        echo -e "${YELLOW}⚠️  Отсутствует Work Record в журнале${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Итог ──
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  📊 РЕЗУЛЬТАТ${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ SoTA полностью соответствует шаблону Expanded v1.2${NC}"
        return 0
    elif [ $ERRORS -eq 0 ]; then
        echo -e "${YELLOW}⚠️  SoTA соответствует с замечаниями ($WARNINGS warnings)${NC}"
        return 0
    else
        echo -e "${RED}❌ SoTA НЕ соответствует шаблону ($ERRORS errors, $WARNINGS warnings)${NC}"
        return 1
    fi
}

# ── Обработка аргументов ──
case "$1" in
    --last)
        echo -e "${BLUE}🔍 Поиск последнего созданного chapter-based SoTA...${NC}"
        file=$(find "$PACK_DIR"/06-sota -name "CS.SOTA.*-nasem-*.md" -type f -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)
        if [ -z "$file" ]; then
            echo -e "${RED}❌ Chapter-based SoTA не найдены${NC}"
            exit 1
        fi
        validate_file "$file"
        ;;
    
    --all)
        echo -e "${BLUE}=== Пакетная проверка всех chapter-based SoTA ===${NC}\n"
        FAILED=0
        for file in "$PACK_DIR"/06-sota/*/*-nasem-*.md "$PACK_DIR"/06-sota/*/*-nrc-*.md; do
            [ -f "$file" ] || continue
            if ! validate_file "$file"; then
                FAILED=$((FAILED + 1))
            fi
            echo ""
        done
        echo -e "${BLUE}=== Итог ===${NC}"
        echo "Не прошли валидацию: $FAILED"
        exit $FAILED
        ;;
    
    "")
        echo "Использование:"
        echo "  bash scripts/validate-chapter-sota.sh <path-to-file>"
        echo "  bash scripts/validate-chapter-sota.sh --last"
        echo "  bash scripts/validate-chapter-sota.sh --all"
        exit 1
        ;;
    
    *)
        validate_file "$1"
        ;;
esac
