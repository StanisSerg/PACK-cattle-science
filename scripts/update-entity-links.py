#!/usr/bin/env python3
"""
Entity Links Updater
Обновляет связи между SoTA и сущностями

Usage:
    python3 scripts/update-entity-links.py <sota_id> [--dry-run]
    python3 scripts/update-entity-links.py --all [--dry-run]
"""

import re
import yaml
import sys
import argparse
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent / "pack/cattle-science"
SOTA_DIR = BASE_DIR / "06-sota"
ENTITY_DIR = BASE_DIR / "02-domain-entities"

def load_entities():
    """Загружает сущности с их именами"""
    entities = {}
    for f in ENTITY_DIR.rglob("CS.ENTITY.*.md"):
        match = re.search(r'CS\.ENTITY\.(\d+)', f.name)
        if not match:
            continue
        eid = int(match.group(1))
        content = f.read_text(encoding='utf-8')
        
        # Парсим YAML
        meta = {}
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    meta = yaml.safe_load(parts[1])
                except:
                    pass
        
        # Собираем имена для поиска
        names = set()
        for key in ['name_ru', 'name_en', 'abbreviation']:
            if meta.get(key):
                names.add(str(meta[key]).lower())
        
        # Теги
        tags = set(str(t).lower() for t in meta.get('tags', []))
        
        entities[eid] = {
            'names': names,
            'tags': tags,
            'file': f,
            'content': content,
            'meta': meta
        }
    
    return entities

def find_sota_file(sota_id):
    """Находит файл SoTA по ID"""
    for cat in ['feeding', 'health', 'reproduction', 'economics', 'management']:
        cat_dir = SOTA_DIR / cat
        if not cat_dir.exists():
            continue
        for f in cat_dir.glob(f"CS.SOTA.{sota_id:03d}-*.md"):
            return f
    return None

def find_entities_in_sota(sota_path, entities):
    """Находит сущности, упомянутые в SoTA"""
    content = sota_path.read_text(encoding='utf-8').lower()
    
    found = []
    for eid, entity in entities.items():
        # Ищем по именам
        for name in entity['names']:
            if len(name) > 3 and name in content:
                found.append(eid)
                break
        else:
            # Ищем по тегам
            for tag in entity['tags']:
                if len(tag) > 3 and tag in content:
                    found.append(eid)
                    break
    
    return sorted(set(found))

def update_sota_links(sota_path, entity_ids, dry_run=False):
    """Обновляет связи в файле SoTA"""
    content = sota_path.read_text(encoding='utf-8')
    
    # Парсим YAML
    if not content.startswith('---'):
        print(f"  ⚠️  Нет YAML в {sota_path.name}")
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    try:
        meta = yaml.safe_load(parts[1])
    except:
        print(f"  ⚠️  Ошибка YAML в {sota_path.name}")
        return False
    
    # Получаем текущие связи
    current = set(meta.get('related_entities', []))
    new_ids = set(f"CS.ENTITY.{eid:03d}" for eid in entity_ids)
    
    # Проверяем, есть ли изменения
    to_add = new_ids - current
    if not to_add:
        print(f"  ✓ Нет новых связей для добавления")
        return False
    
    print(f"  ➕ Добавляем связи: {', '.join(sorted(to_add))}")
    
    if dry_run:
        return True
    
    # Обновляем YAML
    all_related = sorted(current | new_ids)
    meta['related_entities'] = all_related
    
    # Формируем новый YAML
    new_yaml = yaml.dump(meta, allow_unicode=True, sort_keys=False, default_flow_style=False)
    new_content = f"---\n{new_yaml}---{parts[2]}"
    
    sota_path.write_text(new_content, encoding='utf-8')
    return True

def update_entity_links(entity_path, sota_id, dry_run=False):
    """Обновляет связи в файле сущности"""
    content = entity_path.read_text(encoding='utf-8')
    
    # Парсим YAML
    if not content.startswith('---'):
        return False
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return False
    
    try:
        meta = yaml.safe_load(parts[1])
    except:
        return False
    
    # Получаем текущие связи
    current = set(meta.get('related_sota', []))
    new_sota = f"CS.SOTA.{sota_id:03d}"
    
    if new_sota in current:
        return False
    
    if dry_run:
        return True
    
    # Обновляем YAML
    all_related = sorted(current | {new_sota})
    meta['related_sota'] = all_related
    
    # Формируем новый YAML
    new_yaml = yaml.dump(meta, allow_unicode=True, sort_keys=False, default_flow_style=False)
    new_content = f"---\n{new_yaml}---{parts[2]}"
    
    entity_path.write_text(new_content, encoding='utf-8')
    return True

def process_sota(sota_id, entities, dry_run=False):
    """Обрабатывает один SoTA"""
    print(f"\n{'='*60}")
    print(f"📄 CS.SOTA.{sota_id:03d}")
    print('='*60)
    
    sota_path = find_sota_file(sota_id)
    if not sota_path:
        print(f"  ❌ Файл не найден")
        return
    
    # Находим сущности в SoTA
    found_ids = find_entities_in_sota(sota_path, entities)
    print(f"  🔍 Найдено сущностей: {len(found_ids)}")
    
    if not found_ids:
        return
    
    # Показываем какие
    for eid in found_ids[:10]:
        name = list(entities[eid]['names'])[0] if entities[eid]['names'] else 'Unknown'
        print(f"     CS.ENTITY.{eid:03d}: {name}")
    if len(found_ids) > 10:
        print(f"     ... и ещё {len(found_ids) - 10}")
    
    # Обновляем SoTA
    print(f"\n  📝 Обновление SoTA...")
    updated = update_sota_links(sota_path, found_ids, dry_run)
    if updated:
        print(f"     ✅ Связи обновлены" if not dry_run else "     [DRY-RUN] Связи будут обновлены")
    
    # Обновляем сущности
    print(f"\n  📝 Обновление сущностей...")
    updated_count = 0
    for eid in found_ids:
        if update_entity_links(entities[eid]['file'], sota_id, dry_run):
            updated_count += 1
    
    if updated_count > 0:
        print(f"     ✅ Обновлено {updated_count} сущностей" if not dry_run else f"     [DRY-RUN] Будет обновлено {updated_count} сущностей")

def main():
    parser = argparse.ArgumentParser(description='Update entity-SoTA links')
    parser.add_argument('sota_id', nargs='?', type=int, help='SoTA ID to process')
    parser.add_argument('--all', action='store_true', help='Process all SoTA')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')
    parser.add_argument('--recent', type=int, default=0, help='Process N most recent SoTA')
    
    args = parser.parse_args()
    
    if not args.sota_id and not args.all and not args.recent:
        parser.print_help()
        sys.exit(1)
    
    print("🔧 Entity Links Updater")
    if args.dry_run:
        print("[DRY-RUN MODE]")
    
    # Загружаем сущности
    entities = load_entities()
    print(f"Загружено сущностей: {len(entities)}")
    
    if args.sota_id:
        process_sota(args.sota_id, entities, args.dry_run)
    elif args.recent:
        # Находим последние N SoTA
        all_sota = []
        for cat in ['feeding', 'health', 'reproduction', 'economics', 'management']:
            cat_dir = SOTA_DIR / cat
            if not cat_dir.exists():
                continue
            for f in cat_dir.glob("CS.SOTA.*.md"):
                match = re.search(r'CS\.SOTA\.(\d+)', f.name)
                if match:
                    all_sota.append(int(match.group(1)))
        
        recent = sorted(set(all_sota))[-args.recent:]
        print(f"\nОбработка {len(recent)} последних SoTA...")
        for sota_id in recent:
            process_sota(sota_id, entities, args.dry_run)

if __name__ == "__main__":
    main()
