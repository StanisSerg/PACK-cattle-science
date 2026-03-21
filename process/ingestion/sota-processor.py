#!/usr/bin/env python3
"""
SoTA Processor — Автоматическая обработка статей с валидацией

Использование:
    python sota-processor.py --next                    # Обработать следующую статью из W12
    python sota-processor.py --file article.pdf        # Обработать конкретный PDF
    python sota-processor.py --all                     # Обработать все из W12
    python sota-processor.py --validate-only CS.SOTA.XXX.md  # Только валидация

Цикл обработки:
    1. Извлечение текста из PDF
    2. Создание SoTA по шаблону
    3. Автоматическая валидация
    4. Фиксация метрик времени
    5. Перемещение PDF в archive/
"""

import sys
import time
import json
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional, List, Dict

# Импорт валидатора
from sota_validator import SoTAValidator, ValidationResult


@dataclass
class ProcessingMetrics:
    """Метрики обработки одной статьи"""
    filename: str
    sota_id: str
    start_time: str
    end_time: str
    duration_seconds: float
    is_valid: bool
    errors_count: int
    warnings_count: int


class SoTAProcessor:
    """Процессор автоматической обработки SoTA"""
    
    def __init__(self, verbose: bool = True):
        self.verbose = verbose
        self.validator = SoTAValidator(verbose=verbose)
        self.metrics: List[ProcessingMetrics] = []
        
        # Пути
        self.base_dir = Path(__file__).parent.parent.parent
        self.new_articles_dir = self.base_dir / "process" / "ingestion" / "new-articles"
        self.w12_dir = self.new_articles_dir / "W12"
        self.w13_dir = self.new_articles_dir / "W13"
        self.archive_dir = self.new_articles_dir / "archive"
        self.sota_dir = self.base_dir / "pack" / "cattle-science" / "06-sota"
        self.metrics_file = self.new_articles_dir / "processing-metrics.json"
        
        # Создаем директории если нужно
        self.archive_dir.mkdir(exist_ok=True)
    
    def get_next_pdf(self) -> Optional[Path]:
        """Получить следующий PDF из W12"""
        if not self.w12_dir.exists():
            return None
        
        pdfs = sorted(self.w12_dir.glob("*.pdf"))
        return pdfs[0] if pdfs else None
    
    def extract_text_from_pdf(self, pdf_path: Path) -> str:
        """Извлечь текст из PDF"""
        try:
            import fitz  # PyMuPDF
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            doc.close()
            return text
        except ImportError:
            print("[WARNING] PyMuPDF не установлен. Установите: pip install PyMuPDF")
            return ""
        except Exception as e:
            print(f"[ERROR] Не удалось извлечь текст из {pdf_path}: {e}")
            return ""
    
    def parse_article_info(self, text: str, filename: str) -> Dict:
        """Парсинг информации из текста статьи"""
        import re
        
        info = {
            "title": "",
            "authors": "",
            "year": "",
            "journal": "",
            "abstract": "",
            "keywords": []
        }
        
        # Извлечение из названия файла
        # Формат: Author - Year - Title.pdf
        file_match = re.match(r'(.+?)\s+-\s+(\d{4})\s+-\s+(.+)\.pdf', filename)
        if file_match:
            info["authors"] = file_match.group(1).strip()
            info["year"] = file_match.group(2)
            info["title"] = file_match.group(3).strip()
        
        # Извлечение из текста
        lines = text.split('\n')
        
        # Ищем ABSTRACT
        for i, line in enumerate(lines):
            if 'ABSTRACT' in line.upper():
                # Собираем следующие строки до пустой или заглавной
                abstract_lines = []
                for j in range(i+1, min(i+50, len(lines))):
                    next_line = lines[j].strip()
                    if next_line and not next_line.isupper():
                        abstract_lines.append(next_line)
                    elif next_line.isupper() and len(next_line) > 10:
                        break
                info["abstract"] = ' '.join(abstract_lines)[:500]
                break
        
        return info
    
    def determine_area(self, title: str, abstract: str) -> str:
        """Определить область (health/feeding/reproduction)"""
        text = (title + " " + abstract).lower()
        
        keywords_health = ['ketosis', 'ketone', 'liver', 'health', 'disease', 'metabolism', 
                          'immune', 'cortisol', 'inflammation', 'кетоз', 'печень', 'здоровье']
        keywords_feeding = ['feeding', 'nutrition', 'diet', 'rumen', 'fermentation', 
                           'protein', 'energy', 'кормление', 'питание']
        keywords_reproduction = ['reproduction', 'pregnancy', 'fertility', 'insemination',
                                'репродукция', 'стельность', 'фертильность']
        
        scores = {
            'health': sum(1 for k in keywords_health if k in text),
            'feeding': sum(1 for k in keywords_feeding if k in text),
            'reproduction': sum(1 for k in keywords_reproduction if k in text)
        }
        
        return max(scores, key=scores.get)
    
    def get_next_sota_id(self) -> str:
        """Получить следующий ID для SoTA"""
        existing = sorted(self.sota_dir.rglob("CS.SOTA.*.md"))
        if not existing:
            return "CS.SOTA.026"
        
        max_num = 25  # начальное значение
        for f in existing:
            match = re.search(r'CS\.SOTA\.(\d+)', f.name)
            if match:
                max_num = max(max_num, int(match.group(1)))
        
        return f"CS.SOTA.{max_num + 1:03d}"
    
    def create_sota_file(self, info: Dict, sota_id: str, area: str) -> Path:
        """Создать файл SoTA по шаблону"""
        # Определяем папку
        area_dir = self.sota_dir / area
        area_dir.mkdir(exist_ok=True)
        
        # Формируем имя файла
        author_short = info["authors"].split()[0].lower().replace(',', '')
        year = info["year"]
        filename = f"{sota_id}-{author_short}-{year}.md"
        filepath = area_dir / filename
        
        # Загружаем шаблон
        template_path = self.base_dir / "pack" / "cattle-science" / "TEMPLATES" / "SOTA-TEMPLATE.md"
        
        # Создаем базовую структуру (упрощенная версия)
        content = self._generate_sota_content(info, sota_id, area)
        
        filepath.write_text(content, encoding='utf-8')
        return filepath
    
    def _generate_sota_content(self, info: Dict, sota_id: str, area: str) -> str:
        """Генерация содержимого SoTA"""
        author_short = info["authors"].split()[0].replace(',', '')
        
        return f"""---
id: {sota_id}
type: sota
domain: cattle-science
area: {area}
subarea: 
subarea2: 
category: 
year: {info['year']}
authors: "{info['authors']}"
title: "{info['title']}"
journal: "{info['journal'] or 'TBD'}"
volume: ""
pages: ""
doi: ""
publisher: ""
open_access: false
license: ""
language: ru
tags:
  - 
related:
  - id: 
    type: 
    note: ""
    relevance: medium
---

# {sota_id}: {info['authors']} ({info['year']}) — {info['title']}

> **Уровень:**  
> **Формат:**  
> **Время изучения:**  
> **Применение:** 

---

## Резюме (Abstract)

**Контекст:** [Заполнить]  
**Цель:** [Заполнить]  
**Методы:** [Заполнить]  
**Результаты:** [Заполнить]  
**Выводы:** [Заполнить]

---

## 2. КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ (Key Claims)

### Утверждение 1: [Заголовок]
- **Утверждение:** 
- **Доказательства:** 
- **Уверенность:** 
- **Цитата:** ""

---

## 3. ВВЕДЕНИЕ (Introduction)

### 3.1. Полный текст введения [перевод]

{info['abstract'] or '[Заполнить из PDF]'}

---

## 4. МАТЕРИАЛЫ И МЕТОДЫ

### 4.1. Дизайн исследования

[Заполнить]

### 4.2. Медиа-инвентарь

[Описание графиков/таблиц]

---

## 5. РЕЗУЛЬТАТЫ

[Заполнить]

---

## 6. ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ

[Заполнить]

---

## 7. ВЫВОДЫ

[Заполнить]

---

## 8. КРИТИЧЕСКИЙ АНАЛИЗ

[Заполнить]

---

## 9. FAQ

[Заполнить]

---

## 10. ИНСТРУМЕНТЫ И ШАБЛОНЫ

[Заполнить]

---

## 11. ИСТОЧНИКИ

```
{info['authors']} ({info['year']}).
{info['title']}.
{info['journal'] or 'Journal TBD'}.
```

---

## 12. ЖУРНАЛ ОБРАБОТКИ

| Дата | Версия | Действие | Статус |
|------|--------|----------|--------|
| {datetime.now().strftime('%Y-%m-%d')} | 0.1 | Автоматическое создание | Черновик |

---

*SoTA создан: {datetime.now().strftime('%Y-%m-%d')}*  
*Версия: 0.1 (draft)*  
*Обработано в рамках: WP-75 (SoTA Ingestion)*
"""
    
    def process_article(self, pdf_path: Path, auto_fill: bool = False) -> Optional[ProcessingMetrics]:
        """
        Полный цикл обработки одной статьи
        
        Args:
            pdf_path: Путь к PDF файлу
            auto_fill: Попытаться автоматически заполнить из PDF
        """
        print(f"\n{'='*60}")
        print(f"Обработка: {pdf_path.name}")
        print(f"{'='*60}")
        
        start_time = time.time()
        start_time_str = datetime.now().isoformat()
        
        # 1. Извлечение текста (если auto_fill=True)
        text = ""
        info = {
            "title": "",
            "authors": "",
            "year": "",
            "journal": "",
            "abstract": ""
        }
        
        if auto_fill:
            print("[1/5] Извлечение текста из PDF...")
            text = self.extract_text_from_pdf(pdf_path)
            info = self.parse_article_info(text, pdf_path.name)
            print(f"  Найдено: {info['authors']}, {info['year']}, {info['title'][:50]}...")
        else:
            print("[1/5] Пропуск автоизвлечения (ручной режим)")
            # Базовая информация из имени файла
            import re
            file_match = re.match(r'(.+?)\s+-\s+(\d{4})\s+-\s+(.+)\.pdf', pdf_path.name)
            if file_match:
                info["authors"] = file_match.group(1).strip()
                info["year"] = file_match.group(2)
                info["title"] = file_match.group(3).strip()
        
        # 2. Определение области
        print("[2/5] Определение области...")
        area = self.determine_area(info["title"], info["abstract"])
        print(f"  Область: {area}")
        
        # 3. Получение ID
        print("[3/5] Получение ID...")
        sota_id = self.get_next_sota_id()
        print(f"  ID: {sota_id}")
        
        # 4. Создание файла
        print("[4/5] Создание SoTA файла...")
        sota_path = self.create_sota_file(info, sota_id, area)
        print(f"  Создан: {sota_path}")
        
        # 5. ВАЛИДАЦИЯ
        print("[5/5] Валидация по шаблону...")
        validation = self.validator.validate_file(sota_path)
        
        if validation.is_valid:
            print("  ✅ Валидация пройдена!")
        else:
            print(f"  ⚠️  Найдено ошибок: {len(validation.errors)}")
            for err in validation.errors[:3]:
                print(f"    - {err.section}: {err.message}")
        
        # 6. Перемещение PDF в архив
        archive_path = self.archive_dir / pdf_path.name
        pdf_path.rename(archive_path)
        print(f"  PDF перемещён в: {archive_path}")
        
        # 7. Фиксация метрик
        end_time = time.time()
        duration = end_time - start_time
        
        metrics = ProcessingMetrics(
            filename=pdf_path.name,
            sota_id=sota_id,
            start_time=start_time_str,
            end_time=datetime.now().isoformat(),
            duration_seconds=round(duration, 2),
            is_valid=validation.is_valid,
            errors_count=len(validation.errors),
            warnings_count=len(validation.warnings)
        )
        
        self.metrics.append(metrics)
        self._save_metrics()
        
        print(f"\n✅ Готово! Время: {duration:.1f} сек")
        print(f"   Файл: {sota_path}")
        print(f"   Валидация: {'OK' if validation.is_valid else 'FAIL'}")
        
        return metrics
    
    def _save_metrics(self):
        """Сохранить метрики в JSON"""
        data = [asdict(m) for m in self.metrics]
        self.metrics_file.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding='utf-8'
        )
    
    def process_all(self, auto_fill: bool = False):
        """Обработать все PDF из W12"""
        if not self.w12_dir.exists():
            print(f"❌ Директория W12 не найдена: {self.w12_dir}")
            return
        
        pdfs = sorted(self.w12_dir.glob("*.pdf"))
        print(f"Найдено {len(pdfs)} PDF в W12")
        
        for pdf in pdfs:
            self.process_article(pdf, auto_fill=auto_fill)
            print("\n" + "-"*60)
        
        # Итоговая статистика
        print(f"\n{'='*60}")
        print("ИТОГИ ОБРАБОТКИ")
        print(f"{'='*60}")
        print(f"Обработано: {len(self.metrics)}")
        print(f"Валидных: {sum(1 for m in self.metrics if m.is_valid)}")
        print(f"С ошибками: {sum(1 for m in self.metrics if not m.is_valid)}")
        print(f"Общее время: {sum(m.duration_seconds for m in self.metrics):.1f} сек")
        avg_time = sum(m.duration_seconds for m in self.metrics) / len(self.metrics) if self.metrics else 0
        print(f"Среднее время: {avg_time:.1f} сек")


def main():
    parser = argparse.ArgumentParser(
        description="Автоматическая обработка SoTA с валидацией",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры:
  python sota-processor.py --next                    # Следующая статья
  python sota-processor.py --all                     # Все из W12
  python sota-processor.py --all --auto-fill         # С автоизвлечением
  python sota-processor.py --validate-only CS.SOTA.026-aiello-1984.md
        """
    )
    parser.add_argument('--next', action='store_true', help='Обработать следующую статью из W12')
    parser.add_argument('--all', action='store_true', help='Обработать все из W12')
    parser.add_argument('--file', help='Обработать конкретный PDF')
    parser.add_argument('--auto-fill', action='store_true', help='Автоматически извлекать из PDF')
    parser.add_argument('--validate-only', help='Только валидировать существующий SoTA')
    parser.add_argument('--verbose', '-v', action='store_true', help='Подробный вывод')
    
    args = parser.parse_args()
    
    processor = SoTAProcessor(verbose=args.verbose)
    
    if args.validate_only:
        # Только валидация
        result = processor.validator.validate_file(Path(args.validate_only))
        print(f"\n{'='*60}")
        print(f"Валидация: {args.validate_only}")
        print(f"{'='*60}")
        print(f"Статус: {'✅ OK' if result.is_valid else '❌ FAIL'}")
        print(f"Секций найдено: {len(result.sections_found)}/13")
        if result.errors:
            print(f"\nОшибки ({len(result.errors)}):")
            for err in result.errors:
                print(f"  - [{err.severity}] {err.section}")
        if result.warnings:
            print(f"\nПредупреждения ({len(result.warnings)}):")
            for warn in result.warnings:
                print(f"  - {warn.message}")
        sys.exit(0 if result.is_valid else 1)
    
    elif args.next:
        # Следующая статья
        next_pdf = processor.get_next_pdf()
        if next_pdf:
            processor.process_article(next_pdf, auto_fill=args.auto_fill)
        else:
            print("✅ Нет статей для обработки в W12")
    
    elif args.all:
        # Все статьи
        processor.process_all(auto_fill=args.auto_fill)
    
    elif args.file:
        # Конкретный файл
        processor.process_article(Path(args.file), auto_fill=args.auto_fill)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
