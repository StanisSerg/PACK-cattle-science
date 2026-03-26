#!/usr/bin/env python3
"""
Скрипт для анализа SoTA файлов на соответствие шаблону.
Генерирует отчёт в формате Markdown.
"""

import os
import re
import glob
from pathlib import Path
from datetime import datetime

def extract_yaml_frontmatter(content):
    """Извлекает YAML frontmatter из файла."""
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if match:
        return match.group(1)
    return None

def check_yaml_fields(yaml_content):
    """Проверяет наличие обязательных полей в YAML."""
    required = ['id', 'type', 'authors', 'title', 'year', 'tags']
    found = []
    for field in required:
        if field in yaml_content:
            found.append(field)
    return found, len(found) == len(required)

def check_section(content, section_patterns, min_lines=0):
    """Проверяет наличие раздела по паттернам."""
    for pattern in section_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            start = match.end()
            # Находим конец раздела (следующий заголовок уровня 1 или 2)
            end_match = re.search(r'\n#{1,2}\s+', content[start:])
            if end_match:
                section_content = content[start:start + end_match.start()]
            else:
                section_content = content[start:]
            
            lines = [l for l in section_content.split('\n') if l.strip()]
            if len(lines) >= min_lines:
                return True, len(lines)
            return True, len(lines)
    return False, 0

def count_faq_questions(content):
    """Считает количество вопросов в FAQ."""
    # Ищем вопросы в формате Q1, В1, ### Q, **Вопрос и т.д.
    patterns = [
        r'(?:^|\n)(?:Q|В)\s*\d+[:\.]',
        r'(?:^|\n)###?\s*(?:Q|В|Вопрос)',
        r'(?:^|\n)\*\*(?:Вопрос|Q)',
        r'(?:^|\n)####?\s*В\d+',
    ]
    count = 0
    for pattern in patterns:
        matches = re.findall(pattern, content, re.IGNORECASE)
        count += len(matches)
    return max(count, 0)

def has_journal_section(content):
    """Проверяет наличие журнала обработки."""
    patterns = [
        r'#{1,3}\s*ЖУРНАЛ\s*ОБРАБОТКИ',
        r'#{1,3}\s*Журнал\s*обработки',
        r'#{1,3}\s*14\.\s*ЖУРНАЛ',
        r'\|\s*Дата\s*\|\s*Версия\s*\|',
    ]
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def has_screenshots(content):
    """Проверяет наличие скриншотов/медиа-инвентаря."""
    patterns = [
        r'\[СКРИНШОТ\]',
        r'\[Скриншот\]',
        r'Figure\s*\d+',
        r'Table\s*\d+',
        r'Рисунок\s*\d+',
        r'Таблица\s*\d+',
    ]
    for pattern in patterns:
        if re.search(pattern, content, re.IGNORECASE):
            return True
    return False

def has_related_sota(content):
    """Проверяет наличие связей с другими SoTA."""
    patterns = [
        r'related:\s*\n',
        r'CS\.SOTA\.\d+',
        r'id:\s*CS\.SOTA\.\d+',
    ]
    count = 0
    for pattern in patterns:
        matches = re.findall(pattern, content)
        count += len(matches)
    return count > 1  # Больше 1, т.к. свой ID тоже считается

def analyze_sota_file(filepath):
    """Анализирует один SoTA файл."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {
            'file': os.path.basename(filepath),
            'error': str(e),
            'score': 0
        }
    
    result = {
        'file': os.path.basename(filepath),
        'filepath': filepath,
        'score': 0,
        'problems': [],
        'details': {}
    }
    
    # 1. YAML frontmatter
    yaml_content = extract_yaml_frontmatter(content)
    if yaml_content:
        fields, yaml_ok = check_yaml_fields(yaml_content)
        result['details']['yaml'] = fields
        if yaml_ok:
            result['score'] += 1
        else:
            result['problems'].append(f"YAML неполный: {fields}")
    else:
        result['problems'].append("Нет YAML frontmatter")
        result['details']['yaml'] = []
    
    # 2. Abstract / Резюме
    abstract_patterns = [
        r'#{1,3}\s*Резюме\s*\(Abstract\)',
        r'#{1,3}\s*Аннотация',
        r'#{1,3}\s*Abstract',
        r'##\s*Резюме',
    ]
    has_abstract, _ = check_section(content, abstract_patterns, min_lines=3)
    if has_abstract:
        result['score'] += 1
    else:
        result['problems'].append("Нет Abstract/Резюме")
    result['details']['abstract'] = has_abstract
    
    # 3. Key Claims / Ключевые утверждения
    key_claims_patterns = [
        r'#{1,3}\s*2\.?\s*KEY\s*CLAIMS',
        r'#{1,3}\s*2\.?\s*КЛЮЧЕВЫЕ\s*УТВЕРЖДЕНИЯ',
        r'#{1,3}\s*Ключевые\s*утверждения',
    ]
    has_key_claims, _ = check_section(content, key_claims_patterns, min_lines=3)
    if has_key_claims:
        result['score'] += 1
    else:
        result['problems'].append("Нет Key Claims")
    result['details']['key_claims'] = has_key_claims
    
    # 4. Introduction / Введение (проверяем объём)
    intro_patterns = [
        r'#{1,3}\s*3\.?\s*Введение',
        r'#{1,3}\s*3\.?\s*Introduction',
        r'#{1,3}\s*Введение\s*\(Introduction\)',
    ]
    has_intro, intro_lines = check_section(content, intro_patterns, min_lines=10)
    if has_intro and intro_lines >= 10:
        result['score'] += 1
    elif has_intro:
        result['problems'].append(f"Introduction короткий ({intro_lines} строк)")
    else:
        result['problems'].append("Нет Introduction")
    result['details']['intro_lines'] = intro_lines
    
    # 5. Methods / Методы
    methods_patterns = [
        r'#{1,3}\s*4\.?\s*Материалы\s*и\s*методы',
        r'#{1,3}\s*4\.?\s*Methods',
        r'#{1,3}\s*МЕТОДЫ',
    ]
    has_methods, methods_lines = check_section(content, methods_patterns, min_lines=5)
    if has_methods and methods_lines >= 5:
        result['score'] += 1
    elif has_methods:
        result['problems'].append(f"Methods короткий ({methods_lines} строк)")
    else:
        result['problems'].append("Нет Methods")
    result['details']['methods_lines'] = methods_lines
    
    # 6. Results / Результаты
    results_patterns = [
        r'#{1,3}\s*5\.?\s*Результаты',
        r'#{1,3}\s*5\.?\s*Results',
        r'#{1,3}\s*РЕЗУЛЬТАТЫ',
    ]
    has_results, results_lines = check_section(content, results_patterns, min_lines=10)
    if has_results and results_lines >= 10:
        result['score'] += 1
    else:
        result['problems'].append(f"Нет Results или короткий ({results_lines} строк)")
    result['details']['results_lines'] = results_lines
    
    # 7. Practical Application
    practical_patterns = [
        r'#{1,3}\s*6\.?\s*Практическое\s*применение',
        r'#{1,3}\s*6\.?\s*Practical',
        r'#{1,3}\s*ПРАКТИЧЕСКОЕ\s*ПРИМЕНЕНИЕ',
    ]
    has_practical, _ = check_section(content, practical_patterns, min_lines=3)
    if has_practical:
        result['score'] += 1
    else:
        result['problems'].append("Нет Practical Application")
    result['details']['practical'] = has_practical
    
    # 8. Conclusions / Выводы
    conclusions_patterns = [
        r'#{1,3}\s*8\.?\s*Выводы',
        r'#{1,3}\s*8\.?\s*Conclusions',
        r'#{1,3}\s*ВЫВОДЫ',
    ]
    has_conclusions, _ = check_section(content, conclusions_patterns, min_lines=3)
    if has_conclusions:
        result['score'] += 1
    else:
        result['problems'].append("Нет Conclusions")
    result['details']['conclusions'] = has_conclusions
    
    # 9. FAQ (≥3 вопроса)
    faq_patterns = [
        r'#{1,3}\s*11\.?\s*FAQ',
        r'#{1,3}\s*11\.?\s*Вопросы',
        r'#{1,3}\s*FAQ',
    ]
    has_faq_section, _ = check_section(content, faq_patterns, min_lines=3)
    faq_count = count_faq_questions(content)
    if has_faq_section and faq_count >= 3:
        result['score'] += 1
    elif has_faq_section:
        result['problems'].append(f"FAQ слишком короткий ({faq_count} вопросов)")
    else:
        result['problems'].append("Нет FAQ")
    result['details']['faq_count'] = faq_count
    
    # 10. Journal / Журнал обработки
    has_journal = has_journal_section(content)
    if has_journal:
        result['score'] += 1
    else:
        result['problems'].append("Нет Журнала обработки")
    result['details']['journal'] = has_journal
    
    # Дополнительные критерии для высоких оценок
    # Скриншоты/медиа
    has_media = has_screenshots(content)
    result['details']['screenshots'] = has_media
    
    # Связи с другими SoTA
    has_related = has_related_sota(content)
    result['details']['related_sota'] = has_related
    
    # Полный перевод Introduction (проверяем по объёму)
    full_intro = intro_lines > 20
    result['details']['full_intro'] = full_intro
    
    return result

def calculate_final_score(result):
    """Рассчитывает итоговую оценку 1-9."""
    base_score = result['score']  # 0-9 базовых разделов
    
    # Дополнительные факторы для оценок 7-9
    has_media = result['details'].get('screenshots', False)
    has_related = result['details'].get('related_sota', False)
    full_intro = result['details'].get('full_intro', False)
    faq_count = result['details'].get('faq_count', 0)
    
    # Преобразуем в шкалу 1-9
    if base_score <= 1:
        return 1  # Только YAML
    elif base_score <= 2:
        return 2  # + Abstract
    elif base_score <= 3:
        return 3  # + Key Claims
    elif base_score <= 4:
        return 4  # + Introduction
    elif base_score <= 6:
        return 5  # + Methods, Results
    elif base_score <= 7:
        return 6  # + Practical
    elif base_score <= 8:
        # Проверяем полноту для 7-9
        if full_intro and faq_count >= 5:
            if has_media and has_related:
                return 9
            elif has_media:
                return 8
            else:
                return 7
        else:
            return 6
    else:  # base_score == 9
        if has_media and has_related:
            return 9
        elif has_media:
            return 8
        else:
            return 7

def main():
    # Находим все SoTA файлы
    base_path = "PACK-cattle-science/pack/cattle-science/06-sota"
    sota_files = []
    
    for subdir in ['reproduction', 'feeding', 'health', 'economics', 'management']:
        pattern = os.path.join(base_path, subdir, "*.md")
        sota_files.extend(glob.glob(pattern))
    
    results = []
    for filepath in sorted(sota_files):
        result = analyze_sota_file(filepath)
        result['final_score'] = calculate_final_score(result)
        results.append(result)
    
    # Сортируем по score (возрастание)
    results.sort(key=lambda x: (x['final_score'], x['file']))
    
    # Генерируем отчёт
    report_lines = [
        "# SoTA Compliance Audit Report",
        "",
        f"**Дата генерации:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**Всего файлов:** {len(results)}",
        "",
        "## Результаты аудита",
        "",
        "| ID | Файл | Score | Проблемы | Приоритет |",
        "|----|------|-------|----------|-----------|",
    ]
    
    for i, r in enumerate(results, 1):
        filename = r['file']
        score = r['final_score']
        
        # Определяем приоритет
        if score <= 3:
            priority = "🔴 Критический"
        elif score <= 5:
            priority = "🟡 Высокий"
        elif score <= 7:
            priority = "🟢 Средний"
        else:
            priority = "✅ Низкий"
        
        # Формируем список проблем
        if r.get('error'):
            problems = f"ОШИБКА: {r['error']}"
        elif r['problems']:
            problems = '; '.join(r['problems'][:3])  # Первые 3 проблемы
            if len(r['problems']) > 3:
                problems += f" (+{len(r['problems']) - 3} ещё)"
        else:
            problems = "—"
        
        # ID из YAML или из имени файла
        file_id = r.get('details', {}).get('yaml', [])
        if file_id and isinstance(file_id, list) and len(file_id) > 0:
            file_id = file_id[0] if isinstance(file_id[0], str) else filename[:15]
        else:
            file_id = filename[:15]
        
        report_lines.append(f"| {i} | {filename} | {score}/9 | {problems} | {priority} |")
    
    # Добавляем сводку
    report_lines.extend([
        "",
        "## Сводка",
        "",
    ])
    
    score_distribution = {}
    for r in results:
        s = r['final_score']
        score_distribution[s] = score_distribution.get(s, 0) + 1
    
    for score in range(1, 10):
        count = score_distribution.get(score, 0)
        pct = count / len(results) * 100 if results else 0
        bar = "█" * int(pct / 5)
        report_lines.append(f"- **Score {score}/9:** {count} файлов ({pct:.1f}%) {bar}")
    
    report_lines.extend([
        "",
        "## Критерии оценки",
        "",
        "| Score | Описание |",
        "|-------|----------|",
        "| 1/9 | Только YAML |",
        "| 2/9 | + Abstract |",
        "| 3/9 | + Key Claims |",
        "| 4/9 | + Introduction (>10 строк) |",
        "| 5/9 | + Methods (>5 строк) |",
        "| 6/9 | + Results (>10 строк), Practical Application, Conclusions |",
        "| 7/9 | + полный перевод Introduction, FAQ (≥3 вопроса) |",
        "| 8/9 | + скриншоты, лекционные материалы |",
        "| 9/9 | + полная интеграция с другими SoTA |",
        "",
        "---",
        "*Отчёт сгенерирован автоматически*",
    ])
    
    # Сохраняем отчёт
    output_path = "PACK-cattle-science/process/ingestion/sota-audit-report.md"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"Отчёт сохранён: {output_path}")
    print(f"Всего проанализировано файлов: {len(results)}")

if __name__ == "__main__":
    main()
