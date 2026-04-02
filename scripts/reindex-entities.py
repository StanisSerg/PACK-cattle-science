#!/usr/bin/env python3
"""
Entity Inventory Regenerator
Перегенерирует инвентарь сущностей на основе YAML frontmatter в entity-файлах
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

BASE_DIR = Path("/root/IWE/PACK-cattle-science/pack/cattle-science")
ENTITY_DIR = BASE_DIR / "02-domain-entities"
SOTA_DIR = BASE_DIR / "06-sota"

PRIORITY_LEVELS = ["P0", "P1", "P2"]

def extract_yaml_frontmatter(content):
    """Извлекает YAML frontmatter из markdown файла"""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                return yaml.safe_load(parts[1])
            except yaml.YAMLError:
                return None
    return None

def parse_entity_files():
    """Парсит все entity файлы и возвращает структурированные данные"""
    entity_data = defaultdict(lambda: defaultdict(list))
    stats = {
        'total': 0,
        'by_priority': defaultdict(int),
        'by_area': defaultdict(int),
        'by_fpf_type': defaultdict(int),
        'orphaned_sota_refs': []
    }
    
    # Получаем существующие SoTA для проверки
    existing_sota = set()
    if SOTA_DIR.exists():
        for sota_file in SOTA_DIR.rglob("CS.SOTA.*.md"):
            match = re.search(r'CS\.SOTA\.(\d+)', sota_file.name)
            if match:
                existing_sota.add(int(match.group(1)))
    
    for priority in PRIORITY_LEVELS:
        priority_dir = ENTITY_DIR / priority
        if not priority_dir.exists():
            continue
            
        for md_file in priority_dir.rglob("*.md"):
            if not md_file.name.startswith("CS.ENTITY."):
                continue
                
            content = md_file.read_text(encoding='utf-8')
            meta = extract_yaml_frontmatter(content)
            
            if not meta:
                print(f"⚠️  Нет YAML в {md_file.name}")
                continue
                
            entity_id = meta.get('id', '')
            if not entity_id:
                print(f"⚠️  Нет ID в {md_file.name}")
                continue
            
            # Проверяем ссылки на SoTA
            related_sota = meta.get('related_sota', [])
            for sota_ref in related_sota:
                match = re.search(r'(\d+)', str(sota_ref))
                if match:
                    sota_num = int(match.group(1))
                    if sota_num not in existing_sota:
                        stats['orphaned_sota_refs'].append((entity_id, sota_num))
            
            area = meta.get('area', 'unknown')
            fpf_type = meta.get('fpf_type', 'Unknown')
            
            entity_info = {
                'id': entity_id,
                'number': int(re.search(r'\d+', entity_id).group()) if re.search(r'\d+', entity_id) else 0,
                'name_ru': meta.get('name_ru', 'Unknown'),
                'name_en': meta.get('name_en', 'Unknown'),
                'abbreviation': meta.get('abbreviation', ''),
                'fpf_type': fpf_type,
                'area': area,
                'subarea': meta.get('subarea', ''),
                'priority': priority,
                'related_sota': related_sota,
                'related_entities': meta.get('related_entities', []),
                'tags': meta.get('tags', []),
                'filename': md_file.name,
                'path': str(md_file.relative_to(ENTITY_DIR))
            }
            
            entity_data[priority][area].append(entity_info)
            stats['total'] += 1
            stats['by_priority'][priority] += 1
            stats['by_area'][area] += 1
            stats['by_fpf_type'][fpf_type] += 1
    
    # Сортируем
    for priority in entity_data:
        for area in entity_data[priority]:
            entity_data[priority][area].sort(key=lambda x: x['number'])
    
    return entity_data, stats

def generate_inventory(entity_data, stats):
    """Генерирует инвентарь сущностей"""
    lines = [
        "# Инвентарь сущностей PACK-cattle-science",
        "",
        f"> Полный каталог entities из всех SoTA ({stats['total']} файлов)",
        ">",
        f"> **Дата создания:** {datetime.now().strftime('%Y-%m-%d')}",
        f"> **Всего сущностей:** {stats['total']}",
        "> **Статус:** Активный",
        "",
        "---",
        "",
        "## Сводка",
        "",
        "| Категория | Количество | Процент |",
        "|-----------|-----------|---------|",
        f"| **Всего сущностей** | **{stats['total']}** | 100% |"
    ]
    
    for p in PRIORITY_LEVELS:
        count = stats['by_priority'].get(p, 0)
        percent = int(100 * count / stats['total']) if stats['total'] > 0 else 0
        desc = {'P0': 'Fundamental', 'P1': 'Important', 'P2': 'Specific'}[p]
        lines.append(f"| **{p} ({desc})** | {count} | {percent}% |")
    
    lines.extend([
        "",
        "### По типам FPF",
        "",
        "| Тип | Количество | Описание |",
        "|-----|-----------|----------|"
    ])
    
    fpf_descriptions = {
        'U.Characteristic': 'Измеримые характеристики',
        'U.Episteme': 'Понятия/состояния',
        'U.System': 'Биологические системы',
        'U.Method': 'Методы/процедуры',
        'U.Role': 'Роли'
    }
    
    for fpf_type, count in sorted(stats['by_fpf_type'].items(), key=lambda x: -x[1]):
        desc = fpf_descriptions.get(fpf_type, '')
        lines.append(f"| **{fpf_type}** | {count} | {desc} |")
    
    lines.extend([
        "",
        "### По областям",
        "",
        "| Область | Упоминания |",
        "|---------|-----------|"
    ])
    
    for area, count in sorted(stats['by_area'].items(), key=lambda x: -x[1]):
        lines.append(f"| {area} | {count} |")
    
    # P0 Entities
    lines.extend([
        "",
        "---",
        "",
        f"## P0 — Fundamental Entities ({stats['by_priority'].get('P0', 0)} шт)",
        "",
        "Встречаются в 5+ SoTA. Критические для понимания дисциплины.",
        ""
    ])
    
    for area in sorted(entity_data.get('P0', {}).keys()):
        entities = entity_data['P0'][area]
        if not entities:
            continue
            
        lines.extend([
            f"### {area.capitalize()}",
            "",
            "| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |",
            "|-----|---------------|-----------------|-------|-----|"
        ])
        
        for e in entities:
            abbr = e['abbreviation'] or '—'
            lines.append(
                f"| **{e['id']}** | {e['name_ru']} | {e['name_en']} | {abbr} | {e['fpf_type']} |"
            )
        lines.append("")
    
    # P1 Entities
    lines.extend([
        "",
        "---",
        "",
        f"## P1 — Important Entities ({stats['by_priority'].get('P1', 0)} шт)",
        "",
        "Расширенные понятия, важные для специализации.",
        ""
    ])
    
    for area in sorted(entity_data.get('P1', {}).keys()):
        entities = entity_data['P1'][area]
        if not entities:
            continue
            
        lines.extend([
            f"### {area.capitalize()}",
            "",
            "| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |",
            "|-----|---------------|-----------------|-------|-----|"
        ])
        
        for e in entities:
            abbr = e['abbreviation'] or '—'
            lines.append(
                f"| **{e['id']}** | {e['name_ru']} | {e['name_en']} | {abbr} | {e['fpf_type']} |"
            )
        lines.append("")
    
    # P2 Entities
    lines.extend([
        "",
        "---",
        "",
        f"## P2 — Specific Entities ({stats['by_priority'].get('P2', 0)} шт)",
        "",
        "Детальные/молекулярные сущности.",
        ""
    ])
    
    for area in sorted(entity_data.get('P2', {}).keys()):
        entities = entity_data['P2'][area]
        if not entities:
            continue
            
        lines.extend([
            f"### {area.capitalize()}",
            "",
            "| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |",
            "|-----|---------------|-----------------|-------|-----|"
        ])
        
        for e in entities:
            abbr = e['abbreviation'] or '—'
            lines.append(
                f"| **{e['id']}** | {e['name_ru']} | {e['name_en']} | {abbr} | {e['fpf_type']} |"
            )
        lines.append("")
    
    # Orphaned references
    if stats['orphaned_sota_refs']:
        lines.extend([
            "",
            "---",
            "",
            "## ⚠️ Проблемы",
            "",
            "### Ссылки на несуществующие SoTA",
            "",
            "| Entity | Несуществующий SoTA |",
            "|--------|---------------------|"
        ])
        for entity_id, sota_num in sorted(set(stats['orphaned_sota_refs'])):
            lines.append(f"| {entity_id} | CS.SOTA.{sota_num:03d} |")
    
    lines.extend([
        "",
        "---",
        "",
        f"*Сгенерировано: {datetime.now().strftime('%Y-%m-%d')}*",
        "*Автоматическое обновление через: `python3 scripts/reindex-entities.py`"
    ])
    
    return '\n'.join(lines)

def main():
    print("🔍 Парсинг entity файлов...")
    entity_data, stats = parse_entity_files()
    
    print(f"✅ Найдено {stats['total']} entity файлов")
    print(f"   P0: {stats['by_priority'].get('P0', 0)}")
    print(f"   P1: {stats['by_priority'].get('P1', 0)}")
    print(f"   P2: {stats['by_priority'].get('P2', 0)}")
    
    if stats['orphaned_sota_refs']:
        print(f"\n⚠️  Найдено {len(stats['orphaned_sota_refs'])} ссылок на несуществующие SoTA")
    
    # Генерируем инвентарь
    print("\n📝 Генерация инвентаря...")
    inventory_content = generate_inventory(entity_data, stats)
    inventory_path = ENTITY_DIR / "00-entities-inventory.md"
    inventory_path.write_text(inventory_content, encoding='utf-8')
    print(f"  ✅ Инвентарь обновлён: {inventory_path}")
    
    print("\n✨ Реиндексация сущностей завершена!")

if __name__ == "__main__":
    main()
