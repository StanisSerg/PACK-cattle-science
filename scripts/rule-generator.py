#!/usr/bin/env python3
"""
RULE Generator v1.0
Создаёт новые RULE-файлы из шаблона RULE-TEMPLATE.md

Usage:
  python rule-generator.py --id 005 --name "mastitis-detection" --category infectious
  python rule-generator.py --id 006 --name "hypocalcemia-protocol" --category metabolic --dl DL-003
"""

import argparse
import os
import re
from datetime import datetime
from pathlib import Path


def get_next_rule_id(rules_dir: str) -> int:
    """Находит следующий доступный ID для RULE"""
    rules_path = Path(rules_dir)
    existing_ids = []
    
    for f in rules_path.glob('RULE-*.md'):
        match = re.match(r'RULE-(\d+)', f.stem)
        if match:
            existing_ids.append(int(match.group(1)))
    
    if not existing_ids:
        return 1
    return max(existing_ids) + 1


def load_template(template_path: str) -> str:
    """Загружает шаблон RULE"""
    with open(template_path, 'r', encoding='utf-8') as f:
        return f.read()


def generate_rule(template: str, rule_id: str, name: str, category: str, 
                  dl_ref: str = None, author: str = "StanisSerg") -> str:
    """Генерирует RULE из шаблона"""
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Замены в шаблоне
    content = template
    
    # Frontmatter
    content = re.sub(r'rule_id: RULE-NNN', f'rule_id: {rule_id}', content)
    content = re.sub(r'dl_ref: DL-NNN', f'dl_ref: {dl_ref or "DL-NNN"}', content)
    content = re.sub(r'date_created: YYYY-MM-DD', f'date_created: {today}', content)
    content = re.sub(r'date_updated: YYYY-MM-DD', f'date_updated: {today}', content)
    content = re.sub(r'author: "Name"', f'author: {author}', content)
    content = re.sub(r'category: metabolic', f'category: {category}', content)
    content = re.sub(r'last_review: YYYY-MM-DD', f'last_review: {today}', content)
    
    # Рассчитываем next_review (+3 месяца)
    next_month = (datetime.now().month + 3) % 12 or 12
    next_year = datetime.now().year + (datetime.now().month + 3) // 13
    next_review = f"{next_year}-{next_month:02d}-{datetime.now().day:02d}"
    content = re.sub(r'next_review: YYYY-MM-DD', f'next_review: {next_review}', content)
    
    # Заголовок
    content = re.sub(r'# RULE-NNN: Rule-Name-Here', f'# {rule_id}: {name.replace("-", " ").title()}', content)
    
    # Maturity block
    content = re.sub(r'stage: conceptual', f'stage: conceptual', content)
    content = re.sub(r'status: применять, не переписывать', f'status: создать, наполнить, применить', content)
    
    # Change log
    content = re.sub(
        r'\| 1\.0 \| YYYY-MM-DD \| Создано \| \|',
        f'| 1.0 | {today} | Создано из шаблона | {author} |',
        content
    )
    
    return content


def main():
    parser = argparse.ArgumentParser(description='RULE Generator')
    parser.add_argument('--id', type=str, help='ID правила (например: 005). Если не указан — авто.')
    parser.add_argument('--name', type=str, required=True, help='Название правила (kebab-case)')
    parser.add_argument('--category', type=str, required=True, 
                        choices=['metabolic', 'reproductive', 'infectious', 'nutritional', 'management'],
                        help='Категория правила')
    parser.add_argument('--dl', type=str, help='Ссылка на Decision Layer (например: DL-003)')
    parser.add_argument('--author', type=str, default='StanisSerg', help='Автор правила')
    parser.add_argument('--dir', type=str, default='pack/rules', help='Директория для сохранения')
    parser.add_argument('--template', type=str, default='pack/rules/RULE-TEMPLATE.md', 
                        help='Путь к шаблону')
    
    args = parser.parse_args()
    
    # Определяем ID
    if args.id:
        rule_id = f"RULE-{args.id.zfill(3)}" if args.id.isdigit() else args.id
    else:
        next_num = get_next_rule_id(args.dir)
        rule_id = f"RULE-{next_num:03d}"
    
    # Проверяем существование файла
    output_path = Path(args.dir) / f"{rule_id}-{args.name}.md"
    if output_path.exists():
        print(f"✗ Ошибка: файл уже существует: {output_path}")
        sys.exit(1)
    
    # Загружаем шаблон
    if not Path(args.template).exists():
        print(f"✗ Ошибка: шаблон не найден: {args.template}")
        sys.exit(1)
    
    template = load_template(args.template)
    
    # Генерируем RULE
    content = generate_rule(template, rule_id, args.name, args.category, args.dl, args.author)
    
    # Сохраняем
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Создано: {output_path}")
    print(f"  ID: {rule_id}")
    print(f"  Name: {args.name}")
    print(f"  Category: {args.category}")
    print(f"\nСледующие шаги:")
    print(f"  1. Заполните hard/soft conditions в секции DECISION")
    print(f"  2. Опишите механизм в BECAUSE")
    print(f"  3. Создайте CASE и DL для валидации")
    print(f"  4. Запустите: python scripts/rule-validator.py {output_path}")


if __name__ == '__main__':
    import sys
    main()
