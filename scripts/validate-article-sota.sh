#!/bin/bash
#
# validate-article-sota.sh — Валидация Article-SoTA v1.1 Expanded
#
# Использование:
#   bash scripts/validate-article-sota.sh <path-to-sota-file>
#   bash scripts/validate-article-sota.sh --last
#   bash scripts/validate-article-sota.sh --all

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Обязательные поля YAML для peer-reviewed article
REQUIRED_YAML_ARTICLE=(
    "id:"
    "type:"
    "format_version:"
    "knowledge_tier:"
    "domain:"
    "area:"
    "year:"
    "authors:"
    "title:"
    "journal:"
    "volume:"
    "pages:"
    "doi:"
    "tags:"
    "related:"
)

# Рекомендуемые поля для v1.1
RECOMMENDED_YAML_V11=(
    "freshness_window:"
    "sota_edition:"
    "derivation:"
)

# Проверить, содержит ли файл хотя бы один из паттернов
has_any_pattern() {
    local file="$1"
    shift
    for pat in "$@"; do
        if grep -qEi "$pat" "$file" 2>/dev/null; then
            return 0
        fi
    done
    return 1
}

validate_file() {
    local file="$1"
    local filename=$(basename "$file")
    local ERRORS=0
    local WARNINGS=0
    
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  📋 VALIDATE ARTICLE-SoTA v1.1: $filename${NC}"
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
    
    # Проверка format_version
    local format_ver=$(grep "^format_version:" "$file" 2>/dev/null | head -1 | sed 's/.*: *//')
    if [ -n "$format_ver" ]; then
        echo -e "${GREEN}✅ format_version: $format_ver${NC}"
    else
        echo -e "${YELLOW}⚠️  Отсутствует format_version (рекомендуется v1.1)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Проверяем, что это article, а не chapter
    local sota_type=$(grep "^type:" "$file" 2>/dev/null | head -1 | sed 's/.*: *//')
    if [ "$sota_type" == "sota" ] || [ "$sota_type" == "article" ]; then
        echo -e "${GREEN}✅ Тип: Article-SoTA${NC}"
    else
        echo -e "${YELLOW}⚠️  Тип не 'article' или 'sota' ($sota_type) — возможно, это Chapter-SoTA${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Обязательные поля для article
    for field in "${REQUIRED_YAML_ARTICLE[@]}"; do
        local key=$(echo "$field" | sed 's/://')
        if ! grep -q "^$field" "$file"; then
            echo -e "${RED}❌ Отсутствует обязательное поле YAML: $field${NC}"
            ERRORS=$((ERRORS + 1))
        fi
    done
    
    # НЕ требуем book fields для article
    for bookfield in "book_title:" "chapter_number:" "isbn:"; do
        if grep -q "^$bookfield" "$file"; then
            echo -e "${YELLOW}⚠️  Поле $bookfield присутствует (не требуется для Article-SoTA)${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
    
    # Рекомендуемые поля v1.1
    for field in "${RECOMMENDED_YAML_V11[@]}"; do
        if ! grep -q "^$field" "$file"; then
            echo -e "${YELLOW}⚠️  Отсутствует рекомендуемое поле: $field${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    done
    
    # Проверка freshness_window
    if ! grep -q "freshness_window:" "$file"; then
        echo -e "${YELLOW}⚠️  Отсутствует freshness_window${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # Проверка derivation
    if ! grep -q "derivation:" "$file"; then
        echo -e "${YELLOW}⚠️  Отсутствует derivation (reopen_trigger)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Структура разделов ──
    echo -e "\n${CYAN}── Структура разделов (Article v1.1) ──${NC}"
    
    local found_sections=0
    local total_sections=11
    
    # Аннотация
    if has_any_pattern "$file" "АННОТАЦ" "Аннотация"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Аннотация${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Введение
    if has_any_pattern "$file" "ВВЕДЕНИЕ" "Введение"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Введение${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Методология
    if has_any_pattern "$file" "МЕТОДОЛОГИЯ" "Методология"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Методология${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Результаты
    if has_any_pattern "$file" "РЕЗУЛЬТАТ" "Результаты"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Результаты${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Интерпретация
    if has_any_pattern "$file" "ИНТЕРПРЕТАЦ" "Интерпретация"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Интерпретация${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Критический анализ
    if has_any_pattern "$file" "КРИТИЧЕСКИЙ АНАЛИЗ" "Критический анализ"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Критический анализ${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Выводы
    if has_any_pattern "$file" "ВЫВОДЫ" "Выводы"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Выводы${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # FAQ
    if has_any_pattern "$file" "FAQ" "Часто задаваемые"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: FAQ${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Практическое применение
    if has_any_pattern "$file" "ПРАКТИЧЕСКОЕ" "Практическое применение"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Практическое применение${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Источники
    if has_any_pattern "$file" "ИСТОЧНИК" "Источники"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Источники${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    # Журнал обработки
    if has_any_pattern "$file" "ЖУРНАЛ" "Журнал обработки"; then
        found_sections=$((found_sections + 1))
    else
        echo -e "${RED}❌ Отсутствует раздел: Журнал обработки${NC}"; ERRORS=$((ERRORS + 1))
    fi
    
    echo -e "${GREEN}✅ Найдено разделов: $found_sections/$total_sections${NC}"
    
    # ── Key Claims ──
    echo -e "\n${CYAN}── Key Claims ──${NC}"
    
    local claim_patterns=0
    if grep -qEi "^### Claim [0-9]+" "$file" 2>/dev/null; then
        claim_patterns=$(grep -cEi "^### Claim [0-9]+" "$file" 2>/dev/null || echo 0)
    fi
    if grep -qEi "^\*\*Claim [0-9]+:\*\*" "$file" 2>/dev/null; then
        local claim_bold=$(grep -cEi "^\*\*Claim [0-9]+:\*\*" "$file" 2>/dev/null || echo 0)
        claim_patterns=$((claim_patterns + claim_bold))
    fi
    if grep -qEi "Key Claims" "$file" 2>/dev/null; then
        echo -e "${GREEN}✅ Раздел Key Claims присутствует${NC}"
    fi
    
    if [ "$claim_patterns" -ge 2 ]; then
        echo -e "${GREEN}✅ Key Claims: $claim_patterns найдено${NC}"
    else
        echo -e "${YELLOW}⚠️  Key Claims отсутствуют или менее 2 (найдено: $claim_patterns)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Медиа-инвентарь (Section 4.6) ──
    echo -e "\n${CYAN}── Медиа-инвентарь (v1.1) ──${NC}"
    
    if grep -qEi "Медиа-инвентарь" "$file"; then
        echo -e "${GREEN}✅ Медиа-инвентарь присутствует${NC}"
    else
        echo -e "${YELLOW}⚠️  Медиа-инвентарь отсутствует${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    local media_table=$(grep -c "|.*|.*|.*|.*|" "$file" 2>/dev/null || echo 0)
    if [ "$media_table" -ge 3 ]; then
        echo -e "${GREEN}✅ Таблицы с разделителями найдены ($media_table строк)${NC}"
    fi
    
    # ── Механистические интерпретации ──
    echo -e "\n${CYAN}── Механистические интерпретации ──${NC}"
    
    local mech_count=$(grep -cEi "механистическ(ая|ую|ие|ой)|механизм" "$file" 2>/dev/null || echo 0)
    if [ "$mech_count" -ge 3 ]; then
        echo -e "${GREEN}✅ Механистических блоков: $mech_count (≥3)${NC}"
    else
        echo -e "${YELLOW}⚠️  Мало механистических блоков ($mech_count, ожидается ≥3)${NC}"
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
    
    # ── Журнал обработки ──
    echo -e "\n${CYAN}── Журнал обработки ──${NC}"
    
    if ! grep -qEi "ЖУРНАЛ ОБРАБОТКИ|WorkPlan|Work Record" "$file"; then
        echo -e "${RED}❌ Отсутствует журнал обработки${NC}"
        ERRORS=$((ERRORS + 1))
    else
        echo -e "${GREEN}✅ Журнал обработки присутствует${NC}"
    fi
    
    # Проверка наличия WorkPlan и Work Record
    local has_workplan=0
    local has_workrecord=0
    if grep -qEi "WorkPlan|Work Plan" "$file"; then has_workplan=1; fi
    if grep -qEi "Work Record|WorkRecord" "$file"; then has_workrecord=1; fi
    
    if [ "$has_workplan" -eq 1 ] && [ "$has_workrecord" -eq 1 ]; then
        echo -e "${GREEN}✅ WorkPlan и Work Record присутствуют${NC}"
    else
        if [ "$has_workplan" -eq 0 ]; then
            echo -e "${YELLOW}⚠️  Отсутствует WorkPlan${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
        if [ "$has_workrecord" -eq 0 ]; then
            echo -e "${YELLOW}⚠️  Отсутствует Work Record${NC}"
            WARNINGS=$((WARNINGS + 1))
        fi
    fi
    
    # ── Навигация ──
    echo -e "\n${CYAN}── Навигация ──${NC}"
    
    if grep -qEi "Навигация|Navigation|\[.*Аннотация.*|.*Введение" "$file"; then
        echo -e "${GREEN}✅ Навигационная панель присутствует${NC}"
    else
        echo -e "${YELLOW}⚠️  Навигационная панель отсутствует${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Итог ──
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  📊 РЕЗУЛЬТАТ${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ SoTA полностью соответствует шаблону Article Expanded v1.1${NC}"
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
        echo -e "${BLUE}🔍 Поиск последнего созданного Article-SoTA...${NC}"
        file=$(find "$PACK_DIR"/06-sota -name "CS.SOTA.*.md" -type f -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)
        if [ -z "$file" ]; then
            echo -e "${RED}❌ SoTA файлы не найдены${NC}"
            exit 1
        fi
        validate_file "$file"
        ;;
    
    --all)
        echo -e "${BLUE}=== Пакетная проверка всех Article-SoTA ===${NC}\n"
        FAILED=0
        for file in "$PACK_DIR"/06-sota/*/*.md; do
            [ -f "$file" ] || continue
            # Проверяем, что это article (есть format_version: v1.1)
            if head -30 "$file" 2>/dev/null | grep -q "format_version:"; then
                if ! validate_file "$file"; then
                    FAILED=$((FAILED + 1))
                fi
                echo ""
            fi
        done
        echo -e "${BLUE}=== Итог ===${NC}"
        echo "Не прошли валидацию: $FAILED"
        exit $FAILED
        ;;
    
    "")
        echo "Использование:"
        echo "  bash scripts/validate-article-sota.sh <path-to-file>"
        echo "  bash scripts/validate-article-sota.sh --last"
        echo "  bash scripts/validate-article-sota.sh --all"
        exit 1
        ;;
    
    *)
        validate_file "$1"
        ;;
esac
