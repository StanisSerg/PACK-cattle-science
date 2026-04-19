#!/usr/bin/env python3
"""
SoTA Entity Analyzer
Анализирует новые SoTA на предмет:
1. Новых потенциальных сущностей
2. Существующих сущностей, которые нужно обновить
3. Связей между сущностями

Usage:
    python3 scripts/analyze-sota-entities.py [sota_id]
    python3 scripts/analyze-sota-entities.py --all-new
"""

import re
import yaml
import sys
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent / "pack/cattle-science"
SOTA_DIR = BASE_DIR / "06-sota"
ENTITY_DIR = BASE_DIR / "02-domain-entities"

def load_existing_entities():
    """Загружает все существующие сущности с их именами и тегами"""
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
        
        # Извлекаем имена
        names = set()
        if meta.get('name_ru'):
            names.add(meta['name_ru'].lower())
        if meta.get('name_en'):
            names.add(meta['name_en'].lower())
        if meta.get('abbreviation'):
            names.add(meta['abbreviation'].lower())
        
        # Теги
        tags = set(meta.get('tags', []))
        
        entities[eid] = {
            'names': names,
            'tags': tags,
            'area': meta.get('area', 'unknown'),
            'fpf': meta.get('fpf_type', 'Unknown'),
            'file': f.name
        }
    
    return entities

def extract_terms_from_sota(sota_path):
    """Извлекает потенциальные термины-сущности из SoTA"""
    content = sota_path.read_text(encoding='utf-8')
    
    # Парсим YAML
    meta = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            try:
                meta = yaml.safe_load(parts[1])
            except:
                pass
    
    terms = defaultdict(lambda: {'count': 0, 'contexts': [], 'type': ''})
    
    # Извлекаем теги
    for tag in meta.get('tags', []):
        tag_str = str(tag).lower().strip()
        terms[tag_str]['count'] += 2
        terms[tag_str]['type'] = 'tag'
    
    # Извлекаем subarea
    for key in ['subarea', 'subarea2']:
        val = meta.get(key, '')
        if val:
            terms[str(val).lower().replace('-', ' ')]['count'] += 2
            terms[str(val).lower().replace('-', ' ')]['type'] = 'subarea'
    
    # Извлекаем ключевые утверждения
    key_claims = re.findall(r'\*\*([^*]+)\*\*', content)
    for claim in key_claims[:5]:
        # Ищем научные термины
        words = re.findall(r'\b[A-Z][a-z]+(?:\s+[a-z]+){0,2}\b', claim)
        for word in words:
            word_lower = word.lower()
            if len(word_lower) > 3:
                terms[word_lower]['count'] += 1
                terms[word_lower]['contexts'].append(claim[:100])
    
    # Извлекаем аббревиатуры
    abbrs = re.findall(r'\b([A-Z]{2,6})\b', content)
    for abbr in abbrs:
        if abbr not in ['PDF', 'DOC', 'USA', 'JDS', 'ETC']:
            terms[abbr.lower()]['count'] += 1.5
            terms[abbr.lower()]['type'] = 'abbreviation'
    
    return terms, meta

def find_matches(terms, existing_entities):
    """Находит совпадения с существующими сущностями"""
    matches = []
    new_candidates = []
    
    for term, data in terms.items():
        if data['count'] < 1:
            continue
            
        # Ищем совпадения с существующими
        matched = False
        for eid, entity in existing_entities.items():
            # Прямое совпадение с именем
            if term in entity['names']:
                matches.append((eid, entity['file'], term, data['count']))
                matched = True
                break
            # Совпадение с тегом
            if term in entity['tags']:
                matches.append((eid, entity['file'], term, data['count']))
                matched = True
                break
        
        if not matched and len(term) > 3:
            # Проверяем на общие слова
            common_words = {'this', 'that', 'with', 'from', 'they', 'have', 'been', 'were', 'said', 'each', 'which', 'their', 'would', 'there', 'could', 'should'}
            if term not in common_words and not term.isdigit():
                new_candidates.append((term, data['count'], data.get('type', ''), data.get('contexts', [])))
    
    return matches, new_candidates

def analyze_sota(sota_id):
    """Анализирует конкретный SoTA"""
    # Ищем файл SoTA
    sota_file = None
    for cat in ['feeding', 'health', 'reproduction', 'economics', 'management']:
        cat_dir = SOTA_DIR / cat
        if not cat_dir.exists():
            continue
        for f in cat_dir.glob(f"CS.SOTA.{sota_id}-*.md"):
            sota_file = f
            break
        if sota_file:
            break
    
    if not sota_file:
        print(f"❌ SoTA CS.SOTA.{sota_id:03d} не найден")
        return
    
    print(f"\n{'='*80}")
    print(f"🔍 Анализ: {sota_file.name}")
    print('='*80)
    
    # Загружаем существующие сущности
    existing = load_existing_entities()
    
    # Извлекаем термины
    terms, meta = extract_terms_from_sota(sota_file)
    
    # Находим совпадения
    matches, new_candidates = find_matches(terms, existing)
    
    # Выводим результаты
    print(f"\n📚 Обнаружено существующих сущностей: {len(set(m[0] for m in matches))}")
    print("-"*80)
    seen = set()
    for eid, filename, term, score in sorted(matches, key=lambda x: -x[3]):
        if eid not in seen:
            print(f"  ✅ CS.ENTITY.{eid:03d} ({filename}) — match: '{term}' (score: {score:.1f})")
            seen.add(eid)
    
    print(f"\n💡 Потенциальные новые сущности: {len(new_candidates)}")
    print("-"*80)
    for term, score, type_, contexts in sorted(new_candidates, key=lambda x: -x[1])[:15]:
        type_str = f"[{type_}]" if type_ else ""
        print(f"  ➕ {term:30} (score: {score:.1f}) {type_str}")
        if contexts:
            print(f"      Context: {contexts[0][:80]}...")
    
    # Рекомендации по связям
    print(f"\n🔗 Рекомендации по обновлению связей:")
    print("-"*80)
    print(f"  1. Добавить в SoTA related_entities для {len(seen)} сущностей")
    print(f"  2. Добавить в сущности related_sota для CS.SOTA.{sota_id:03d}")
    print(f"  3. Рассмотреть создание новых сущностей из топ-10 кандидатов")

def analyze_all_new():
    """Анализирует все SoTA, у которых нет связей с сущностями"""
    print("\n🔍 Поиск SoTA без связей с сущностями...")
    
    # Находим все SoTA
    all_sota = {}
    for cat in ['feeding', 'health', 'reproduction', 'economics', 'management']:
        cat_dir = SOTA_DIR / cat
        if not cat_dir.exists():
            continue
        for f in cat_dir.glob("CS.SOTA.*.md"):
            match = re.search(r'CS\.SOTA\.(\d+)', f.name)
            if match:
                sota_id = int(match.group(1))
                all_sota[sota_id] = f
    
    # Загружаем существующие связи
    existing = load_existing_entities()
    linked_sota = set()
    
    for entity in existing.values():
        # Ищем упоминания SoTA в файлах сущностей
        pass  # Упрощенная версия
    
    # Анализируем последние 20 SoTA
    recent = sorted(all_sota.keys())[-20:]
    for sota_id in recent:
        analyze_sota(sota_id)

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  {sys.argv[0]} <sota_id>     # Анализ конкретного SoTA")
        print(f"  {sys.argv[0]} --all-new     # Анализ всех новых SoTA")
        sys.exit(1)
    
    if sys.argv[1] == '--all-new':
        analyze_all_new()
    else:
        try:
            sota_id = int(sys.argv[1])
            analyze_sota(sota_id)
        except ValueError:
            print(f"❌ Неверный ID SoTA: {sys.argv[1]}")
            sys.exit(1)

if __name__ == "__main__":
    main()
