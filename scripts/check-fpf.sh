#!/bin/bash
#
# check-fpf.sh — Автоматическая проверка FPF-compliance для SoTA
#
# Использование:
#   bash scripts/check-fpf.sh <path-to-sota-file>
#   bash scripts/check-fpf.sh --last        # Последний созданный SoTA
#
# Проверяет:
#   A.7  Strict Distinction        — разделение модели и реальности
#   A.6.3 ConservativeRetextualization — reopen trigger (номера страниц)
#   A.10 Evidence Graph            — evidence anchors
#   Tone check                     — академический тон, без аналогий
#   AP-5 Conversational tone       — запрет разговорных конструкций

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

ERRORS=0
WARNINGS=0

check_file() {
    local file="$1"
    local filename=$(basename "$file")
    
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  🔍 FPF CHECK: $filename${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ Файл не найден: $file${NC}"
        return 1
    fi
    
    # ── A.7 Strict Distinction ──
    echo -e "\n${CYAN}── A.7 Strict Distinction (Модель ≠ Реальность) ──${NC}"
    
    # Запрещённые фразы (прямое приписывание модели реальности)
    local strict_errors=0
    
    while IFS= read -r line; do
        local ln=$(echo "$line" | cut -d: -f1)
        local txt=$(echo "$line" | cut -d: -f2-)
        echo -e "${RED}❌ Строка $ln: $txt${NC}"
        strict_errors=$((strict_errors + 1))
    done < <(grep -in "корова поглощает\|животное поглощает\|организм поглощает" "$file" | grep -v "модель предполагает" | grep -v "модель NASEM" | head -5)
    
    while IFS= read -r line; do
        local ln=$(echo "$line" | cut -d: -f1)
        local txt=$(echo "$line" | cut -d: -f2-)
        echo -e "${RED}❌ Строка $ln: $txt${NC}"
        strict_errors=$((strict_errors + 1))
    done < <(grep -in "корова синтезирует\|животное синтезирует" "$file" | grep -v "модель предполагает" | grep -v "модель NASEM" | head -5)
    
    if [ $strict_errors -eq 0 ]; then
        echo -e "${GREEN}✅ Запрещённые фразы (прямое приписывание) не обнаружены${NC}"
    else
        echo -e "${YELLOW}💡 Исправьте на: 'Модель NASEM 2021 предполагает, что...'${NC}"
        ERRORS=$((ERRORS + strict_errors))
    fi
    
    # ── A.6.3 ConservativeRetextualization — Reopen trigger ──
    echo -e "\n${CYAN}── A.6.3 ConservativeRetextualization (Reopen trigger) ──${NC}"
    
    local page_refs=$(grep -cE "\(NASEM 2021, p\. [0-9]+\)|NASEM 2021, p\. [0-9]+" "$file" 2>/dev/null)
    local eq_refs=$(grep -cE "Eq [0-9]+-[0-9]+|Equation [0-9]+-[0-9]+" "$file" 2>/dev/null)
    
    echo -e "${GREEN}📊 Ссылок на страницы NASEM 2021: $page_refs${NC}"
    echo -e "${GREEN}📊 Ссылок на уравнения (Eq X-Y): $eq_refs${NC}"
    
    if [ "$page_refs" -lt 5 ]; then
        echo -e "${YELLOW}⚠️  Мало страничных ссылок (рекомендуется ≥5 для reopen trigger)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    if [ "$eq_refs" -lt 3 ]; then
        echo -e "${YELLOW}⚠️  Мало ссылок на уравнения (рекомендуется ≥3)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── A.10 Evidence Graph — Evidence anchors ──
    echo -e "\n${CYAN}── A.10 Evidence Graph (Evidence anchors) ──${NC}"
    
    local evidence_anchors=$(grep -cE "\([A-Z][a-z]+( et al\.)?,? [0-9]{4}\)|NASEM 2021|NRC 2001|Goff|DeLuca|Gaucheron|Bijl" "$file" 2>/dev/null)
    echo -e "${GREEN}📊 Evidence anchors: $evidence_anchors${NC}"
    
    if [ "$evidence_anchors" -lt 10 ]; then
        echo -e "${YELLOW}⚠️  Мало evidence anchors (рекомендуется ≥10 для expanded)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Tone check — Аналогии и метафоры ──
    echo -e "\n${CYAN}── Tone check (AP-5: без аналогий и метафор) ──${NC}"
    
    local tone_errors=0
    
    # Аналогии из бытовой сферы
    local analogies=("пекарня" "хозяин симбиотической" "чёрный ящик" "духовка" "мука" "печь" "завод" "фабрика")
    for analogy in "${analogies[@]}"; do
        if grep -qi "$analogy" "$file"; then
            local ln=$(grep -in "$analogy" "$file" | head -1 | cut -d: -f1)
            echo -e "${RED}❌ Строка $ln: найдена аналогия '$analogy'${NC}"
            tone_errors=$((tone_errors + 1))
        fi
    done
    
    # Разговорные вопросы в заголовках (исключая FAQ, лекции и Q1/Q2...)
    local colloquial_qs=$(grep -inE "^#{1,4} .*Зачем.*\?|^#{1,4} .*Почему.*\?|^#{1,4} .*Как.*\?" "$file" 2>/dev/null | grep -ivE "Q[0-9]+:|FAQ|Лекци|Вопросы для обсуждения|чек-лист|практическое|упражнение" | head -5)
    local cq_count=0
    if [ -n "$colloquial_qs" ]; then
        while IFS= read -r line; do
            local ln=$(echo "$line" | cut -d: -f1)
            local txt=$(echo "$line" | cut -d: -f2-)
            echo -e "${RED}❌ Строка $ln: разговорный вопрос в заголовке '$txt'${NC}"
            cq_count=$((cq_count + 1))
        done <<< "$colloquial_qs"
        tone_errors=$((tone_errors + cq_count))
    fi
    
    # Эмоциональные оценки без метрик (исключая лекционные цитаты и FAQ)
    local emotional=$(grep -inE "просто |всего лишь |такая низкая |такой высокий |очень дорогой |очень дешёвый |выгодный |невыгодный" "$file" 2>/dev/null | grep -ivE "Лекци|FAQ|цитата|пример фразы|ключевые сообщения|чек-лист" | head -5)
    if [ -n "$emotional" ]; then
        while IFS= read -r line; do
            local ln=$(echo "$line" | cut -d: -f1)
            local txt=$(echo "$line" | cut -d: -f2-)
            echo -e "${RED}❌ Строка $ln: эмоциональная оценка '$txt'${NC}"
            tone_errors=$((tone_errors + 1))
        done <<< "$emotional"
    fi
    
    # Метафоры
    local metaphors=("узкое место" "слабое звено" "бутылочное горлышко")
    for metaphor in "${metaphors[@]}"; do
        if grep -qi "$metaphor" "$file"; then
            local ln=$(grep -in "$metaphor" "$file" | head -1 | cut -d: -f1)
            echo -e "${RED}❌ Строка $ln: найдена метафора '$metaphor'${NC}"
            tone_errors=$((tone_errors + 1))
        fi
    done
    
    if [ $tone_errors -eq 0 ]; then
        echo -e "${GREEN}✅ Аналогий, метафор и разговорных конструкций не обнаружено${NC}"
    else
        ERRORS=$((ERRORS + tone_errors))
    fi
    
    # ── A.6.Q Quality Term Precision ──
    echo -e "\n${CYAN}── A.6.Q Quality Term Precision ──${NC}"
    
    local vague_terms=$(grep -inE "высокая абсорбция|низкая абсорбция|хорошая|плохая|сильная|слабая" "$file" | grep -v "#" | grep -vi "R²\|RMSE\|CCC\|AC =\|mg/\|г/кг" | head -5)
    local vague_count=0
    if [ -n "$vague_terms" ]; then
        while IFS= read -r line; do
            local ln=$(echo "$line" | cut -d: -f1)
            local txt=$(echo "$line" | cut -d: -f2-)
            echo -e "${YELLOW}⚠️  Строка $ln: расплывчатый термин '$txt'${NC}"
            vague_count=$((vague_count + 1))
        done <<< "$vague_terms"
        WARNINGS=$((WARNINGS + vague_count))
    fi
    
    # FPF A.6.Q: качественные оценки уверенности в Key Claims без числовой шкалы
    local conf_vague=$(grep -inE "\*\*Уверенность:\*\* (высокая|средняя|низкая|средне-высокая|средняя-высокая)" "$file" | head -5)
    if [ -n "$conf_vague" ]; then
        while IFS= read -r line; do
            local ln=$(echo "$line" | cut -d: -f1)
            local txt=$(echo "$line" | cut -d: -f2-)
            echo -e "${RED}❌ Строка $ln: качественная оценка уверенности '$txt' — требуется числовая шкала (0,0–1,0) с обоснованием${NC}"
            vague_count=$((vague_count + 1))
        done <<< "$conf_vague"
        ERRORS=$((ERRORS + vague_count))
    fi
    
    if [ "$vague_count" -eq 0 ]; then
        echo -e "${GREEN}✅ Расплывчатых терминов без метрик не обнаружено${NC}"
    fi
    
    # ── A.6.P Relation Precision ──
    echo -e "\n${CYAN}── A.6.P Relation Precision ──${NC}"
    
    local imprecise=$(grep -inE "[A-Za-z]+ важен для [A-Za-z]+|[A-Za-z]+ нужен для [A-Za-z]+|[A-Za-z]+ необходим для [A-Za-z]+" "$file" | grep -v "#" | grep -v "модель" | head -5)
    local imprecise_count=0
    if [ -n "$imprecise" ]; then
        while IFS= read -r line; do
            local ln=$(echo "$line" | cut -d: -f1)
            local txt=$(echo "$line" | cut -d: -f2-)
            echo -e "${YELLOW}⚠️  Строка $ln: неточное отношение '$txt' — уточните количественно${NC}"
            imprecise_count=$((imprecise_count + 1))
        done <<< "$imprecise"
        WARNINGS=$((WARNINGS + imprecise_count))
    else
        echo -e "${GREEN}✅ Неточных отношений не обнаружено${NC}"
    fi
    
    # ── FPF-разметка границ модели ──
    echo -e "\n${CYAN}── FPF A.7: Разметка границ модели ──${NC}"
    
    local fpf_markers=$(grep -c "FPF A\.7" "$file" 2>/dev/null)
    local outside_markers=$(grep -c "\[вне NASEM" "$file" 2>/dev/null)
    
    echo -e "${GREEN}📊 FPF-маркеров (A.7, A.6.3, A.10): $fpf_markers${NC}"
    echo -e "${GREEN}📊 Пометок [вне NASEM]: $outside_markers${NC}"
    
    if [ "$fpf_markers" -lt 2 ]; then
        echo -e "${YELLOW}⚠️  Мало явных FPF-маркеров (рекомендуется ≥2)${NC}"
        WARNINGS=$((WARNINGS + 1))
    fi
    
    # ── Итог ──
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  📊 FPF РЕЗУЛЬТАТ${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
        echo -e "${GREEN}✅ SoTA полностью соответствует FPF${NC}"
        return 0
    elif [ $ERRORS -eq 0 ]; then
        echo -e "${YELLOW}⚠️  FPF-соответствие с замечаниями ($WARNINGS warnings)${NC}"
        return 0
    else
        echo -e "${RED}❌ FPF-нарушения: $ERRORS errors, $WARNINGS warnings${NC}"
        return 1
    fi
}

# ── Обработка аргументов ──
case "$1" in
    --last)
        file=$(find "$PACK_DIR"/06-sota -name "CS.SOTA.*-nasem-*.md" -type f -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)
        if [ -z "$file" ]; then
            echo -e "${RED}❌ SoTA не найдены${NC}"
            exit 1
        fi
        check_file "$file"
        ;;
    
    "")
        echo "Использование:"
        echo "  bash scripts/check-fpf.sh <path-to-file>"
        echo "  bash scripts/check-fpf.sh --last"
        exit 1
        ;;
    
    *)
        check_file "$1"
        ;;
esac
