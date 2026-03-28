#!/bin/bash
# extract-entity-mentions.sh — Авто-извлечение упоминаний сущностей в SoTA

SOTA_DIR="pack/cattle-science/06-sota"
ENTITY_DIR="pack/cattle-science/02-domain-entities"
OUTPUT_DIR="process/ingestion/entity-mentions"

mkdir -p "$OUTPUT_DIR"

# Список сущностей для поиска (названия из файлов)
declare -A ENTITIES
ENTITIES["BHB"]="CS.ENTITY.007"
ENTITIES["beta-hydroxybutyrate"]="CS.ENTITY.007"
ENTITIES["ВНВК"]="CS.ENTITY.007"
ENTITIES["NEFA"]="CS.ENTITY.008"
ENTITIES["non-esterified fatty acids"]="CS.ENTITY.008"
ENTITIES["glucose"]="CS.ENTITY.009"
ENTITIES["глюкоза"]="CS.ENTITY.009"
ENTITIES["propionate"]="CS.ENTITY.010"
ENTITIES["пропионат"]="CS.ENTITY.010"
ENTITIES["glycerol"]="CS.ENTITY.078"
ENTITIES["глицерол"]="CS.ENTITY.078"

echo "=== Извлечение упоминаний сущностей ==="
echo "SoTA директория: $SOTA_DIR"
echo ""

# Для каждой сущности ищем упоминания
for term in "${!ENTITIES[@]}"; do
    entity_id="${ENTITIES[$term]}"
    output_file="$OUTPUT_DIR/${entity_id}-mentions.json"
    
    echo "Поиск: $term -> $entity_id"
    
    # Ищем в SoTA файлах
    find "$SOTA_DIR" -name "CS.SOTA.*.md" -exec grep -l -i "$term" {} \; | while read -r sota_file; do
        sota_id=$(basename "$sota_file" | sed 's/CS.SOTA.//' | sed 's/-.*//')
        
        # Извлекаем контекст (2 строки до и после)
        grep -i -B2 -A2 "$term" "$sota_file" | head -20
        
        echo "---"
    done > "$output_file.tmp"
    
    if [ -s "$output_file.tmp" ]; then
        echo "  Найдено упоминаний: $(wc -l < "$output_file.tmp")"
        mv "$output_file.tmp" "$output_file"
    else
        echo "  Упоминаний не найдено"
        rm -f "$output_file.tmp"
    fi
done

echo ""
echo "=== Готово ==="
echo "Результаты в: $OUTPUT_DIR/"
