#!/bin/bash
#
# check-archgate.sh — ArchGate-оценка качества SoTA
#
# Использование:
#   bash scripts/check-archgate.sh <path-to-sota-file>
#   bash scripts/check-archgate.sh --last
#
# Оценивает 7 характеристик (ЭМОГССБ):
#   Э — Эффективность (практическая применимость)
#   М — Модифицируемость (легкость обновления)
#   О — Основательность (доказательная база)
#   Г — Глубина (механистическое обоснование)
#   С — Структурированность (логика изложения)
#   С — Сопровождаемость (журнал, связи, версионирование)
#   Б — Безопасность (FPF-разметка, границы модели)
#
# Формат: чеклист с баллами 0–10, без агрегирования (conjunctive screening)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
MAGENTA='\033[0;35m'
NC='\033[0m'

ERRORS=0

# Хелпер для безопасного подсчёта совпадений
safe_count() {
    local pattern="$1"
    local file="$2"
    local count
    count=$(grep -cE "$pattern" "$file" 2>/dev/null) || count=0
    echo "$count"
}

calculate_score() {
    local value=$1
    local max=$2
    echo $(( value * 10 / max ))
}

assess_file() {
    local file="$1"
    local filename=$(basename "$file")
    
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  🏛️  ARCHGATE ASSESSMENT: $filename${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ ! -f "$file" ]; then
        echo -e "${RED}❌ Файл не найден: $file${NC}"
        return 1
    fi
    
    local total_lines=$(wc -l < "$file")
    local word_count=$(wc -w < "$file")
    
    # ── Э — Эффективность (практическая применимость) ──
    echo -e "\n${CYAN}── Э — Эффективность (практическая применимость) ──${NC}"
    
    local has_algorithm=$(safe_count "Алгоритм" "$file")
    local has_errors=$(safe_count "Типичные ошибки" "$file")
    local has_edge_cases=$(safe_count "пограничные сценарии|пограничные случаи" "$file")
    local has_examples=$(safe_count "Расчёт требований|Пример|Иллюстративный" "$file")
    local has_russian=$(safe_count "российским условиям|России|российских" "$file")
    
    local eff_score=0
    [ "$has_algorithm" -gt 0 ] && eff_score=$((eff_score + 2))
    [ "$has_errors" -gt 0 ] && eff_score=$((eff_score + 2))
    [ "$has_edge_cases" -gt 0 ] && eff_score=$((eff_score + 2))
    [ "$has_examples" -gt 0 ] && eff_score=$((eff_score + 2))
    [ "$has_russian" -gt 0 ] && eff_score=$((eff_score + 2))
    
    echo -e "  Алгоритм:           $has_algorithm  (+2 при >0)"
    echo -e "  Типичные ошибки:    $has_errors  (+2 при >0)"
    echo -e "  Пограничные случаи: $has_edge_cases  (+2 при >0)"
    echo -e "  Примеры расчётов:   $has_examples  (+2 при >0)"
    echo -e "  Адаптация к России: $has_russian  (+2 при >0)"
    
    local eff_final=$(calculate_score $eff_score 10)
    if [ "$eff_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Эффективность: $eff_final/10${NC}"
    elif [ "$eff_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Эффективность: $eff_final/10${NC}"
    else
        echo -e "  ${RED}❌ Эффективность: $eff_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── М — Модифицируемость (легкость обновления) ──
    echo -e "\n${CYAN}── М — Модифицируемость ──${NC}"
    
    local has_workplan=$(safe_count "WorkPlan" "$file")
    local has_workrecord=$(safe_count "Work Record" "$file")
    local has_freshness=$(safe_count "freshness_window" "$file")
    local has_version=$(safe_count "sota_edition" "$file")
    local has_criteria=$(safe_count "Критерии пересмотра|Критерий готовности" "$file")
    
    local mod_score=0
    [ "$has_workplan" -gt 0 ] && mod_score=$((mod_score + 2))
    [ "$has_workrecord" -gt 0 ] && mod_score=$((mod_score + 2))
    [ "$has_freshness" -gt 0 ] && mod_score=$((mod_score + 2))
    [ "$has_version" -gt 0 ] && mod_score=$((mod_score + 2))
    [ "$has_criteria" -gt 0 ] && mod_score=$((mod_score + 2))
    
    echo -e "  WorkPlan:           $has_workplan  (+2)"
    echo -e "  Work Record:        $has_workrecord  (+2)"
    echo -e "  Freshness window:   $has_freshness  (+2)"
    echo -e "  Версионирование:    $has_version  (+2)"
    echo -e "  Критерии пересмотра: $has_criteria  (+2)"
    
    local mod_final=$(calculate_score $mod_score 10)
    if [ "$mod_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Модифицируемость: $mod_final/10${NC}"
    elif [ "$mod_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Модифицируемость: $mod_final/10${NC}"
    else
        echo -e "  ${RED}❌ Модифицируемость: $mod_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── О — Основательность (доказательная база) ──
    echo -e "\n${CYAN}── О — Основательность ──${NC}"
    
    local has_page_refs=$(safe_count "p\. [0-9]+" "$file")
    local has_eq_refs=$(safe_count "Eq [0-9]+-[0-9]+" "$file")
    local has_table_refs=$(safe_count "Table [0-9]+-[0-9]+" "$file")
    local has_external_refs=$(safe_count "вне NASEM" "$file")
    local has_stats=$(safe_count "R²|RMSE|CCC|CV =|P [<>]" "$file")
    
    local ev_score=0
    [ "$has_page_refs" -ge 5 ] && ev_score=$((ev_score + 2)) || ev_score=$((ev_score + has_page_refs * 2 / 5))
    [ "$has_eq_refs" -ge 5 ] && ev_score=$((ev_score + 2)) || ev_score=$((ev_score + has_eq_refs * 2 / 5))
    [ "$has_table_refs" -ge 2 ] && ev_score=$((ev_score + 2)) || ev_score=$((ev_score + has_table_refs))
    [ "$has_external_refs" -ge 2 ] && ev_score=$((ev_score + 2)) || ev_score=$((ev_score + has_external_refs))
    [ "$has_stats" -ge 3 ] && ev_score=$((ev_score + 2)) || ev_score=$((ev_score + has_stats * 2 / 3))
    
    echo -e "  Ссылки на страницы: $has_page_refs  (+2 при ≥5)"
    echo -e "  Ссылки на уравнения: $has_eq_refs  (+2 при ≥5)"
    echo -e "  Ссылки на таблицы:  $has_table_refs  (+2 при ≥2)"
    echo -e "  Внешние источники:  $has_external_refs  (+2 при ≥2)"
    echo -e "  Статистические метрики: $has_stats  (+2 при ≥3)"
    
    local ev_final=$(calculate_score $ev_score 10)
    if [ "$ev_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Основательность: $ev_final/10${NC}"
    elif [ "$ev_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Основательность: $ev_final/10${NC}"
    else
        echo -e "  ${RED}❌ Основательность: $ev_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── Г — Глубина (механистическое обоснование) ──
    echo -e "\n${CYAN}── Г — Глубина ──${NC}"
    
    local phys_sections=$(safe_count "Физиология и механизмы" "$file")
    local obos_blocks=$(safe_count "Обоснование" "$file")
    local mech_blocks=$(safe_count "Механизм" "$file")
    local evolution_tables=$(safe_count "Эволюция модели" "$file")
    local has_physiology_context=$(safe_count "физиологическая|биохимическая|молекулярная" "$file")
    
    local deep_score=0
    [ "$phys_sections" -ge 3 ] && deep_score=$((deep_score + 2)) || deep_score=$((deep_score + phys_sections * 2 / 3))
    [ "$obos_blocks" -ge 5 ] && deep_score=$((deep_score + 2)) || deep_score=$((deep_score + obos_blocks * 2 / 5))
    [ "$mech_blocks" -ge 3 ] && deep_score=$((deep_score + 2)) || deep_score=$((deep_score + mech_blocks * 2 / 3))
    [ "$evolution_tables" -ge 2 ] && deep_score=$((deep_score + 2)) || deep_score=$((deep_score + evolution_tables))
    [ "$has_physiology_context" -ge 5 ] && deep_score=$((deep_score + 2)) || deep_score=$((deep_score + has_physiology_context * 2 / 5))
    
    echo -e "  Физиологических разделов: $phys_sections  (+2 при ≥3)"
    echo -e "  Блоков 'Обоснование':     $obos_blocks  (+2 при ≥5)"
    echo -e "  Блоков 'Механизм':        $mech_blocks  (+2 при ≥3)"
    echo -e "  Таблиц эволюции:          $evolution_tables  (+2 при ≥2)"
    echo -e "  Физиологического контекста: $has_physiology_context  (+2 при ≥5)"
    
    local deep_final=$(calculate_score $deep_score 10)
    if [ "$deep_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Глубина: $deep_final/10${NC}"
    elif [ "$deep_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Глубина: $deep_final/10${NC}"
    else
        echo -e "  ${RED}❌ Глубина: $deep_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── С — Структурированность ──
    echo -e "\n${CYAN}── С — Структурированность ──${NC}"
    
    local h2_count=$(safe_count "^## " "$file")
    local h3_count=$(safe_count "^### " "$file")
    local h4_count=$(safe_count "^#### " "$file")
    local has_toc_links=$(safe_count "Место главы в системе книги|Архитектура" "$file")
    local has_summary=$(safe_count "Аннотация|Ключевые обновления" "$file")
    
    local struct_score=0
    [ "$h2_count" -ge 8 ] && struct_score=$((struct_score + 2)) || struct_score=$((struct_score + h2_count * 2 / 8))
    [ "$h3_count" -ge 10 ] && struct_score=$((struct_score + 2)) || struct_score=$((struct_score + h3_count * 2 / 10))
    [ "$h4_count" -ge 10 ] && struct_score=$((struct_score + 2)) || struct_score=$((struct_score + h4_count * 2 / 10))
    [ "$has_toc_links" -gt 0 ] && struct_score=$((struct_score + 2))
    [ "$has_summary" -gt 0 ] && struct_score=$((struct_score + 2))
    
    echo -e "  H2-заголовков:    $h2_count  (+2 при ≥8)"
    echo -e "  H3-заголовков:    $h3_count  (+2 при ≥10)"
    echo -e "  H4-заголовков:    $h4_count  (+2 при ≥10)"
    echo -e "  Навигация (TOC):  $has_toc_links  (+2)"
    echo -e "  Аннотация/сводка: $has_summary  (+2)"
    
    local struct_final=$(calculate_score $struct_score 10)
    if [ "$struct_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Структурированность: $struct_final/10${NC}"
    elif [ "$struct_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Структурированность: $struct_final/10${NC}"
    else
        echo -e "  ${RED}❌ Структурированность: $struct_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── С — Сопровождаемость ──
    echo -e "\n${CYAN}── С — Сопровождаемость ──${NC}"
    
    local has_git=$(safe_count "Коммит|commit" "$file")
    local has_author=$(safe_count "Автор|Author" "$file")
    local has_date=$(safe_count "Дата|date:" "$file")
    local has_related=$(grep -A 100 "^related:" "$file" | grep -cE "^\s*- id:" || true)
    local has_next_steps=$(safe_count "Следующие шаги|Следующий ID" "$file")
    
    local sup_score=0
    [ "$has_git" -gt 0 ] && sup_score=$((sup_score + 2))
    [ "$has_author" -gt 0 ] && sup_score=$((sup_score + 2))
    [ "$has_date" -gt 0 ] && sup_score=$((sup_score + 2))
    [ "$has_related" -ge 2 ] && sup_score=$((sup_score + 2)) || sup_score=$((sup_score + has_related))
    [ "$has_next_steps" -gt 0 ] && sup_score=$((sup_score + 2))
    
    echo -e "  Git-ссылки:       $has_git  (+2)"
    echo -e "  Авторы:           $has_author  (+2)"
    echo -e "  Даты:             $has_date  (+2)"
    echo -e "  Связи (related):  $has_related  (+2 при ≥2)"
    echo -e "  Следующие шаги:   $has_next_steps  (+2)"
    
    local sup_final=$(calculate_score $sup_score 10)
    if [ "$sup_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Сопровождаемость: $sup_final/10${NC}"
    elif [ "$sup_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Сопровождаемость: $sup_final/10${NC}"
    else
        echo -e "  ${RED}❌ Сопровождаемость: $sup_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── Б — Безопасность (FPF-разметка) ──
    echo -e "\n${CYAN}── Б — Безопасность (FPF-разметка) ──${NC}"
    
    local fpf_markers=$(safe_count "FPF A\." "$file")
    local outside_markers=$(safe_count "\[вне NASEM" "$file")
    local model_markers=$(safe_count "модель предполагает|Модель NASEM" "$file")
    local has_limitations=$(safe_count "Ограничения|Ограничения и критика" "$file")
    local has_distinction=$(safe_count "Модель ≠ Реальность|Strict Distinction" "$file")
    
    local safe_score=0
    [ "$fpf_markers" -ge 3 ] && safe_score=$((safe_score + 2)) || safe_score=$((safe_score + fpf_markers * 2 / 3))
    [ "$outside_markers" -ge 2 ] && safe_score=$((safe_score + 2)) || safe_score=$((safe_score + outside_markers))
    [ "$model_markers" -ge 5 ] && safe_score=$((safe_score + 2)) || safe_score=$((safe_score + model_markers * 2 / 5))
    [ "$has_limitations" -gt 0 ] && safe_score=$((safe_score + 2))
    [ "$has_distinction" -gt 0 ] && safe_score=$((safe_score + 2))
    
    echo -e "  FPF-маркеров:           $fpf_markers  (+2 при ≥3)"
    echo -e "  [вне NASEM] пометок:    $outside_markers  (+2 при ≥2)"
    echo -e "  'Модель предполагает':  $model_markers  (+2 при ≥5)"
    echo -e "  Раздел ограничений:     $has_limitations  (+2)"
    echo -e "  Strict Distinction:     $has_distinction  (+2)"
    
    local safe_final=$(calculate_score $safe_score 10)
    if [ "$safe_final" -ge 8 ]; then
        echo -e "  ${GREEN}✅ Безопасность: $safe_final/10${NC}"
    elif [ "$safe_final" -ge 6 ]; then
        echo -e "  ${YELLOW}⚠️  Безопасность: $safe_final/10${NC}"
    else
        echo -e "  ${RED}❌ Безопасность: $safe_final/10 (ниже порога 6)${NC}"
        ERRORS=$((ERRORS + 1))
    fi
    
    # ── Итог ──
    echo -e "\n${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    echo -e "${BLUE}  📊 ARCHGATE РЕЗУЛЬТАТ${NC}"
    echo -e "${BLUE}═══════════════════════════════════════════════════════════════${NC}"
    
    if [ $ERRORS -eq 0 ]; then
        echo -e "${GREEN}✅ Все 7 характеристик ≥6 — SoTA проходит conjunctive screening${NC}"
        echo -e "${GREEN}✅ Рекомендация: принять${NC}"
        return 0
    else
        echo -e "${RED}❌ $ERRORS характеристик ниже порога 6${NC}"
        echo -e "${YELLOW}⚠️  Рекомендация: доработать перед принятием${NC}"
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
        assess_file "$file"
        ;;
    
    "")
        echo "Использование:"
        echo "  bash scripts/check-archgate.sh <path-to-file>"
        echo "  bash scripts/check-archgate.sh --last"
        exit 1
        ;;
    
    *)
        assess_file "$1"
        ;;
esac
