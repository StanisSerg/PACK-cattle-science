#!/usr/bin/env python3
"""
SoTA Index Regenerator
Перегенерирует шардированные индексы на основе YAML frontmatter в SoTA файлах
"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent / "pack/cattle-science"
SOTA_DIR = BASE_DIR / "06-sota"
MAP_DIR = BASE_DIR / "07-map"
SHARD_DIR = MAP_DIR / "sota-index"

# Категории в порядке приоритета
CATEGORIES = ["reproduction", "feeding", "health", "economics", "management"]

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

def parse_sota_files():
    """Парсит все SoTA файлы и возвращает структурированные данные"""
    sota_data = defaultdict(list)
    
    for category in CATEGORIES:
        category_dir = SOTA_DIR / category
        if not category_dir.exists():
            continue
            
        for md_file in sorted(category_dir.glob("*.md")):
            content = md_file.read_text(encoding='utf-8')
            meta = extract_yaml_frontmatter(content)
            
            if not meta:
                print(f"⚠️  Нет YAML в {md_file.name}")
                continue
                
            sota_id = meta.get('id', '')
            if not sota_id:
                print(f"⚠️  Нет ID в {md_file.name}")
                continue
            
            # Извлекаем ключевой результат из раздела КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ или РЕЗЮМЕ
            key_result = extract_key_result(content)
            
            sota_info = {
                'id': sota_id,
                'number': int(re.search(r'\d+', sota_id).group()) if re.search(r'\d+', sota_id) else 0,
                'authors': meta.get('authors', 'Unknown'),
                'year': meta.get('year', 'N/A'),
                'type': meta.get('category', meta.get('type', 'unknown')),
                'priority': meta.get('priority', 'P2'),
                'tags': meta.get('tags', []),
                'title': meta.get('title', ''),
                'key_result': key_result,
                'area': meta.get('area', category),
                'filename': md_file.name
            }
            
            sota_data[category].append(sota_info)
    
    # Сортируем по номеру в каждой категории
    for category in sota_data:
        sota_data[category].sort(key=lambda x: x['number'])
    
    return sota_data

def extract_key_result(content):
    """Извлекает первое ключевое утверждение или резюме"""
    # Ищем в ключевых утверждениях
    key_claim_match = re.search(r'##?\s*КЛЮЧЕВЫЕ\s*УТВЕРЖДЕНИЯ.*?\*\*(.+?)\*\*', content, re.DOTALL | re.IGNORECASE)
    if key_claim_match:
        return key_claim_match.group(1).strip()[:100] + "..."
    
    # Ищем в резюме
    summary_match = re.search(r'##?\s*РЕЗЮМЕ.*?(?:\n|^)(.+?)(?:\n##|\Z)', content, re.DOTALL | re.IGNORECASE)
    if summary_match:
        return summary_match.group(1).strip()[:100] + "..."
    
    return "См. файл для деталей"

def get_author_short(authors_str):
    """Получает короткое имя первого автора"""
    if not authors_str:
        return "Unknown"
    first_author = authors_str.split(',')[0].strip()
    # Убираем инициалы для краткости
    last_name = first_author.split()[-1] if ' ' in first_author else first_author
    return last_name

def generate_shard(category, sota_list):
    """Генерирует содержимое шард-файла"""
    lines = [
        f"# CS.MAP.001-{category}: SoTA Index — {get_category_title(category)}",
        "",
        f"> Шард индекса: {category} ({len(sota_list)} SoTA)",
        ">",
        "> **Мастер-индекс:** [CS.MAP.001-sota-index.md](../CS.MAP.001-sota-index.md)",
        "",
        "---",
        "",
        "## Статистика",
        "",
        "| Метрика | Значение |",
        "|---------|----------|"
    ]
    
    # Счетчики
    p0_count = sum(1 for s in sota_list if s['priority'] == 'P0')
    p1_count = sum(1 for s in sota_list if s['priority'] == 'P1')
    p2_count = sum(1 for s in sota_list if s['priority'] == 'P2')
    p3_count = sum(1 for s in sota_list if s['priority'] == 'P3')
    
    type_counts = defaultdict(int)
    for s in sota_list:
        type_counts[s['type']] += 1
    
    lines.extend([
        f"| Всего SoTA | {len(sota_list)} |",
        f"| P0 (Фундаментальные) | {p0_count} |",
        f"| P1 (Критически важные) | {p1_count} |",
        f"| P2 (Важные) | {p2_count} |",
        f"| P3 (Дополнительные) | {p3_count} |"
    ])
    
    # Добавляем типы
    for t, count in sorted(type_counts.items()):
        lines.append(f"| {t.capitalize()} | {count} |")
    
    lines.extend([
        "",
        "---",
        "",
        "## Полный список",
        "",
        "| ID | Статья | Год | Приоритет | Тип | Теги | Ключевой результат |",
        "|----|--------|-----|-----------|-----|------|-------------------|"
    ])
    
    # Список SoTA
    for s in sota_list:
        author_short = get_author_short(s['authors'])
        tags_str = ', '.join(s['tags'][:3]) if s['tags'] else '-'
        key_res = s['key_result'][:60] + "..." if len(s['key_result']) > 60 else s['key_result']
        key_res = key_res.replace('|', '\\|')  # Экранируем pipe
        
        lines.append(
            f"| [{s['id']}](../../06-sota/{category}/{s['filename']}) | "
            f"{author_short} et al. | "
            f"{s['year']} | "
            f"{s['priority']} | "
            f"{s['type']} | "
            f"`{tags_str}` | "
            f"{key_res} |"
        )
    
    lines.extend([
        "",
        "---",
        "",
        "## Структура папки",
        "",
        f"```",
        f"06-sota/{category}/",
        f"```",
        "",
        "---",
        "",
        f"*Шард обновлён: {datetime.now().strftime('%Y-%m-%d')}*",
        f"*Автоматическая генерация: {len(sota_list)} SoTA*"
    ])
    
    return '\n'.join(lines)

def get_category_title(category):
    """Возвращает русское название категории"""
    titles = {
        'reproduction': 'Репродуктивный менеджмент',
        'feeding': 'Кормление и метаболизм',
        'health': 'Здоровье и метаболизм',
        'economics': 'Экономика',
        'management': 'Менеджмент'
    }
    return titles.get(category, category.capitalize())

def generate_master_index(sota_data):
    """Генерирует мастер-индекс"""
    total = sum(len(lst) for lst in sota_data.values())
    
    lines = [
        "# CS.MAP.001: SoTA Index — Научные источники",
        "",
        "> Карта научно-обоснованных знаний в PACK-cattle-science",
        ">",
        "> **Версия:** 3.0 (Sharded — Auto-generated)",
        f"> **Всего SoTA:** {total}",
        f"> **Последнее обновление:** {datetime.now().strftime('%Y-%m-%d')}",
        "",
        "---",
        "",
        "## Быстрая навигация (шарды)",
        "",
        "| Область | SoTA | Шард | Описание |",
        "|---------|------|------|----------|"
    ]
    
    descriptions = {
        'reproduction': 'Репродуктивный менеджмент, TAI, синхронизация',
        'feeding': 'Кормление, метаболизм, переходный период',
        'health': 'Здоровье, кетоз, иммунитет, печень',
        'economics': 'Экономика, моделирование, оптимизация',
        'management': 'Менеджмент, алгоритмы, оценка'
    }
    
    for cat in CATEGORIES:
        count = len(sota_data.get(cat, []))
        lines.append(
            f"| {get_category_emoji(cat)} **{cat}** | {count} | "
            f"[Перейти →](./sota-index/CS.MAP.001-{cat}.md) | {descriptions.get(cat, '')} |"
        )
    
    lines.extend([
        f"| **ИТОГО** | **{total}** | | |",
        "",
        "---",
        "",
        "## Статистика по категориям",
        ""
    ])
    
    # Гистограмма
    max_count = max(len(sota_data.get(cat, [])) for cat in CATEGORIES) if sota_data else 0
    lines.append("```")
    lines.append(f"Всего SoTA: {total}")
    for cat in CATEGORIES:
        count = len(sota_data.get(cat, []))
        bar_len = int(40 * count / max_count) if max_count > 0 else 0
        bar = "█" * bar_len
        percent = int(100 * count / total) if total > 0 else 0
        lines.append(f"├── {cat:13} {count:3} {bar} ({percent}%)")
    lines.append("```")
    
    # По приоритетам
    lines.extend([
        "",
        "## Статистика по уровням",
        "",
        "| Уровень | Количество | Описание |",
        "|---------|------------|----------|"
    ])
    
    p0 = sum(1 for cat in CATEGORIES for s in sota_data.get(cat, []) if s['priority'] == 'P0')
    p1 = sum(1 for cat in CATEGORIES for s in sota_data.get(cat, []) if s['priority'] == 'P1')
    p2 = sum(1 for cat in CATEGORIES for s in sota_data.get(cat, []) if s['priority'] == 'P2')
    p3 = sum(1 for cat in CATEGORIES for s in sota_data.get(cat, []) if s['priority'] == 'P3')
    
    lines.extend([
        f"| **P0** — Фундаментальные | {p0} | Определяют парадигму |",
        f"| **P1** — Критически важные | {p1} | Meta-analysis, крупные обзоры |",
        f"| **P2** — Важные | {p2} | Эксперименты, уточняющие исследования |",
        f"| **P3** — Дополнительные | {p3} | Вспомогательные материалы |",
        "",
        "---",
        "",
        "## Поиск",
        "",
        "- **По ID:** Ctrl+F → `CS.SOTA.XXX`",
        "- **По автору:** Перейти в шард категории",
        "- **По тегу:** Перейти в соответствующий шард",
        "- **По теме:** См. разделы \"По темам\" в шардах",
        "",
        "---",
        "",
        "## Полный список (компактный)"
    ])
    
    # Компактные списки по категориям
    for cat in CATEGORIES:
        sota_list = sota_data.get(cat, [])
        if not sota_list:
            continue
        ids = [f"`{s['id']}`" for s in sota_list]
        lines.extend([
            "",
            f"### {cat.capitalize()} ({len(sota_list)})",
            ' '.join(ids)
        ])
    
    lines.extend([
        "",
        "---",
        "",
        "## Структура папок",
        "",
        "```",
        "06-sota/"
    ])
    for cat in CATEGORIES:
        count = len(sota_data.get(cat, []))
        lines.append(f"├── {cat:13}/     # {count} SoTA")
    lines.append("```")
    
    lines.extend([
        "",
        "---",
        "",
        "## Обновление индекса",
        "",
        "Автоматически через:",
        "```bash",
        "python3 scripts/reindex-sota.py",
        "```",
        "",
        "---",
        "",
        f"*Версия 3.0 — Обновлено: {datetime.now().strftime('%Y-%m-%d')}*",
        f"*Автоматический подсчёт: {total} SoTA*"
    ])
    
    return '\n'.join(lines)

def get_category_emoji(category):
    """Возвращает эмодзи для категории"""
    emojis = {
        'reproduction': '🧬',
        'feeding': '🌾',
        'health': '🏥',
        'economics': '💰',
        'management': '📊'
    }
    return emojis.get(category, '📄')

def main():
    print("🔍 Парсинг SoTA файлов...")
    sota_data = parse_sota_files()
    
    total = sum(len(lst) for lst in sota_data.values())
    print(f"✅ Найдено {total} SoTA файлов")
    
    # Создаем директории если нужно
    MAP_DIR.mkdir(parents=True, exist_ok=True)
    SHARD_DIR.mkdir(parents=True, exist_ok=True)
    
    # Генерируем шарды
    print("\n📝 Генерация шардов:")
    for cat in CATEGORIES:
        sota_list = sota_data.get(cat, [])
        if sota_list:
            shard_content = generate_shard(cat, sota_list)
            shard_path = SHARD_DIR / f"CS.MAP.001-{cat}.md"
            shard_path.write_text(shard_content, encoding='utf-8')
            print(f"  ✅ {cat}: {len(sota_list)} SoTA → {shard_path.name}")
        else:
            print(f"  ⚠️  {cat}: нет файлов")
    
    # Генерируем мастер-индекс
    print("\n📝 Генерация мастер-индекса...")
    master_content = generate_master_index(sota_data)
    master_path = MAP_DIR / "CS.MAP.001-sota-index.md"
    master_path.write_text(master_content, encoding='utf-8')
    print(f"  ✅ Мастер-индекс: {total} SoTA → {master_path.name}")
    
    print("\n✨ Реиндексация завершена!")
    print(f"\n📊 Итого: {total} SoTA в {len(CATEGORIES)} категориях")
    for cat in CATEGORIES:
        count = len(sota_data.get(cat, []))
        print(f"   {cat:12}: {count:3} файлов")

if __name__ == "__main__":
    main()
