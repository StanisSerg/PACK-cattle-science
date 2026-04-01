#!/bin/bash
# session-close.sh — Автоматическое закрытие сессии WP-75
#
# Выполняет:
# 1. Валидацию всех новых SoTA
# 2. Обновление индекса CS.MAP.001
# 3. Entity Integration (автосоздание сущностей)
# 4. Генерацию отчёта
#
# Использование:
#   bash scripts/session-close.sh                          # Интерактивный режим
#   bash scripts/session-close.sh --sota ID1,ID2,ID3       # Указать конкретные SoTA
#   bash scripts/session-close.sh --auto                   # Автоматический режим (без подтверждений)
#   bash scripts/session-close.sh --report                 # С генерацией отчёта

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PACK_DIR="$(dirname "$SCRIPT_DIR")/pack/cattle-science"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"

# Цвета
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

# Параметры
AUTO_MODE=false
GENERATE_REPORT=false
SPECIFIC_SOTAS=""

# Обработка аргументов
while [[ $# -gt 0 ]]; do
    case $1 in
        --sota)
            SPECIFIC_SOTAS="$2"
            shift 2
            ;;
        --auto)
            AUTO_MODE=true
            shift
            ;;
        --report)
            GENERATE_REPORT=true
            shift
            ;;
        --help)
            echo "Использование:"
            echo "  bash scripts/session-close.sh [опции]"
            echo ""
            echo "Опции:"
            echo "  --sota ID1,ID2    Обработать конкретные SoTA"
            echo "  --auto            Автоматический режим (без подтверждений)"
            echo "  --report          Сгенерировать отчёт"
            echo "  --help            Показать эту справку"
            exit 0
            ;;
        *)
            echo "Неизвестная опция: $1"
            exit 1
            ;;
    esac
done

echo -e "${CYAN}"
echo "╔════════════════════════════════════════════════════════════╗"
echo "║        WP-75 Session Close — Автоматическое закрытие       ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo -e "${NC}"

# Определение SoTA для обработки
if [ -n "$SPECIFIC_SOTAS" ]; then
    IFS=',' read -ra SOTA_IDS <<< "$SPECIFIC_SOTAS"
else
    # Найти все SoTA, созданные сегодня или недавно
    echo -e "${BLUE}Поиск недавно изменённых SoTA...${NC}"
    
    # Ищем SoTA, изменённые за последние 24 часа
    SOTA_FILES=$(find "$PACK_DIR/06-sota" -name "CS.SOTA.*.md" -mtime -1 2>/dev/null || true)
    
    # Или берём unstaged изменения
    if [ -z "$SOTA_FILES" ]; then
        SOTA_FILES=$(git -C "$ROOT_DIR" diff --name-only HEAD 2>/dev/null | grep "pack/cattle-science/06-sota/CS.SOTA.*\.md" || true)
    fi
    
    # Или предлагаем ввести вручную
    if [ -z "$SOTA_FILES" ]; then
        echo -e "${YELLOW}Не найдены недавно изменённые SoTA${NC}"
        echo "Введите ID SoTA через запятую (например: CS.SOTA.127,CS.SOTA.128):"
        read -r input
        IFS=',' read -ra SOTA_IDS <<< "$input"
    else
        SOTA_IDS=()
        for file in $SOTA_FILES; do
            id=$(basename "$file" | grep -oP 'CS\.SOTA\.\d+')
            if [ -n "$id" ]; then
                SOTA_IDS+=("$id")
            fi
        done
    fi
fi

if [ ${#SOTA_IDS[@]} -eq 0 ]; then
    echo -e "${RED}❌ Не найдены SoTA для обработки${NC}"
    exit 1
fi

echo -e "${BLUE}SoTA для обработки:${NC}"
for id in "${SOTA_IDS[@]}"; do
    echo "  - $id"
done
echo ""

if [ "$AUTO_MODE" = false ]; then
    echo -e "${YELLOW}Продолжить? (y/n)${NC}"
    read -r confirm
    if [ "$confirm" != "y" ]; then
        echo "Отменено"
        exit 0
    fi
fi

# Отчёт
REPORT_FILE=""
if [ "$GENERATE_REPORT" = true ]; then
    REPORT_FILE="$ROOT_DIR/process/ingestion/session-close-$(date +%Y-%m-%d-%H%M).md"
    mkdir -p "$(dirname "$REPORT_FILE")"
    
    cat > "$REPORT_FILE" << EOF
# Session Close Report: $(date +%Y-%m-%d)

**Время:** $(date +%H:%M)  
**Режим:** $([ "$AUTO_MODE" = true ] && echo "Автоматический" || echo "Интерактивный")

## Обработанные SoTA

| ID | Валидация | Индекс | Entities | Статус |
|----|-----------|--------|----------|--------|
EOF
fi

# Phase 1: Валидация
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Phase 1: Валидация SoTA по шаблону${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

VALIDATION_RESULTS=()
FAILED_VALIDATION=()

for id in "${SOTA_IDS[@]}"; do
    file=$(find "$PACK_DIR/06-sota" -name "$id*.md" 2>/dev/null | head -1)
    
    if [ -z "$file" ]; then
        echo -e "${RED}❌ Файл не найден: $id${NC}"
        FAILED_VALIDATION+=("$id")
        continue
    fi
    
    echo -e "${CYAN}Валидация: $id${NC}"
    
    if bash "$ROOT_DIR/scripts/validate-sota-template.sh" "$file" > /tmp/validate-$id.log 2>&1; then
        echo -e "${GREEN}  ✅ Валидация пройдена${NC}"
        VALIDATION_RESULTS+=("$id:PASS")
    else
        echo -e "${YELLOW}  ⚠️  Валидация с замечаниями${NC}"
        tail -10 /tmp/validate-$id.log | sed 's/^/    /'
        VALIDATION_RESULTS+=("$id:WARN")
    fi
done

# Phase 2: Обновление индекса
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Phase 2: Обновление индекса CS.MAP.001${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

INDEX_UPDATED=()

for id in "${SOTA_IDS[@]}"; do
    file=$(find "$PACK_DIR/06-sota" -name "$id*.md" 2>/dev/null | head -1)
    
    if [ -n "$file" ] && [ -f "$file" ]; then
        echo -e "${CYAN}Добавление в индекс: $id${NC}"
        
        if bash "$ROOT_DIR/scripts/add-sota-to-index.sh" "$file" > /tmp/index-$id.log 2>&1; then
            echo -e "${GREEN}  ✅ Добавлено в индекс${NC}"
            INDEX_UPDATED+=("$id")
        else
            echo -e "${YELLOW}  ⚠️  Уже в индексе или ошибка${NC}"
        fi
    fi
done

# Phase 3: Entity Integration
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Phase 3: Entity Integration${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

ENTITY_INTEGRATED=()

for id in "${SOTA_IDS[@]}"; do
    echo -e "${CYAN}Entity Integration: $id${NC}"
    
    if [ "$AUTO_MODE" = true ]; then
        # Автоматический режим с --yes
        if python3 "$PACK_DIR/02-domain-entities/scripts/wp75-entity-integration.py" \
            --sota "$id" --yes > /tmp/entity-$id.log 2>&1; then
            echo -e "${GREEN}  ✅ Entities созданы/связаны${NC}"
            ENTITY_INTEGRATED+=("$id")
        else
            echo -e "${YELLOW}  ⚠️  Ошибка Entity Integration${NC}"
            tail -5 /tmp/entity-$id.log | sed 's/^/    /'
        fi
    else
        # Интерактивный режим — показываем dry-run
        echo -e "${BLUE}  Предпросмотр изменений:${NC}"
        python3 "$PACK_DIR/02-domain-entities/scripts/wp75-entity-integration.py" \
            --sota "$id" --dry-run 2>&1 | head -30 | sed 's/^/    /'
        
        echo ""
        echo -e "${YELLOW}Выполнить Entity Integration для $id? (y/n)${NC}"
        read -r confirm
        
        if [ "$confirm" = "y" ]; then
            if python3 "$PACK_DIR/02-domain-entities/scripts/wp75-entity-integration.py" \
                --sota "$id" --yes > /tmp/entity-$id.log 2>&1; then
                echo -e "${GREEN}  ✅ Entities созданы/связаны${NC}"
                ENTITY_INTEGRATED+=("$id")
            else
                echo -e "${RED}  ❌ Ошибка${NC}"
            fi
        else
            echo -e "${YELLOW}  Пропущено${NC}"
        fi
    fi
done

# Phase 4: Git commit индекса
echo ""
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}  Phase 4: Git Commit${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════${NC}"
echo ""

if [ ${#INDEX_UPDATED[@]} -gt 0 ]; then
    echo -e "${CYAN}Добавление изменений в git...${NC}"
    
    git -C "$ROOT_DIR" add pack/cattle-science/07-map/CS.MAP.001-sota-index.md
    
    # Добавляем entity файлы
    git -C "$ROOT_DIR" add pack/cattle-science/02-domain-entities/ 2>/dev/null || true
    
    # Добавляем сами SoTA (если не закоммичены)
    for id in "${SOTA_IDS[@]}"; do
        git -C "$ROOT_DIR" add pack/cattle-science/06-sota/*/$id*.md 2>/dev/null || true
    done
    
    # Коммит
    commit_msg="WP-75: Session close - $(date +%Y-%m-%d)

Updated:
- CS.MAP.001: Added ${#INDEX_UPDATED[@]} SoTA(s)
- Entity Integration: ${#ENTITY_INTEGRATED[@]} SoTA(s)

SoTA processed:"

    for id in "${SOTA_IDS[@]}"; do
        commit_msg="$commit_msg
- $id"
    done
    
    if git -C "$ROOT_DIR" commit -m "$commit_msg" --quiet; then
        echo -e "${GREEN}✅ Изменения закоммичены${NC}"
    else
        echo -e "${YELLOW}⚠️  Нет изменений для коммита${NC}"
    fi
else
    echo -e "${YELLOW}Нет изменений для коммита${NC}"
fi

# Phase 5: Итоговый отчёт
echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}  ИТОГОВЫЙ ОТЧЁТ${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════${NC}"
echo ""

printf "%-40s %s\n" "Всего SoTA обработано:" "${#SOTA_IDS[@]}"
printf "%-40s %s\n" "Валидация пройдена:" "${#VALIDATION_RESULTS[@]}"
printf "%-40s %s\n" "Добавлено в индекс:" "${#INDEX_UPDATED[@]}"
printf "%-40s %s\n" "Entity Integration:" "${#ENTITY_INTEGRATED[@]}"
echo ""

if [ ${#FAILED_VALIDATION[@]} -gt 0 ]; then
    echo -e "${RED}⚠️  Требуют внимания:${NC}"
    for id in "${FAILED_VALIDATION[@]}"; do
        echo "  - $id"
    done
    echo ""
fi

# Обновление отчёта
if [ -n "$REPORT_FILE" ]; then
    for id in "${SOTA_IDS[@]}"; do
        val_status=$(echo "${VALIDATION_RESULTS[@]}" | grep "$id" | grep -o "PASS\|WARN\|FAIL" || echo "N/A")
        idx_status=$([[ " ${INDEX_UPDATED[@]} " =~ " $id " ]] && echo "✅" || echo "➖")
        ent_status=$([[ " ${ENTITY_INTEGRATED[@]} " =~ " $id " ]] && echo "✅" || echo "➖")
        
        echo "| $id | $val_status | $idx_status | $ent_status | Завершено |" >> "$REPORT_FILE"
    done
    
    cat >> "$REPORT_FILE" << EOF

## Итоги

- Валидация: ${#VALIDATION_RESULTS[@]}/${#SOTA_IDS[@]}
- Индекс: ${#INDEX_UPDATED[@]}/${#SOTA_IDS[@]}
- Entities: ${#ENTITY_INTEGRATED[@]}/${#SOTA_IDS[@]}

## Следующие шаги

1. Проверить git статус: \`git status\`
2. Запушить изменения: \`git push\`
3. Обновить WP-context в DS-strategy

---
*Отчёт сгенерирован автоматически*
EOF

    echo -e "${BLUE}Отчёт сохранён: $REPORT_FILE${NC}"
fi

echo -e "${GREEN}✅ Session Close завершён!${NC}"
echo ""
