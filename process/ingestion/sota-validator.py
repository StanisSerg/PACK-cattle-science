#!/usr/bin/env python3
"""
SoTA Validator — Проверка соответствия SoTA файлов шаблону

Использование:
    python sota-validator.py [file.md]          # Проверить один файл
    python sota-validator.py --all              # Проверить все SoTA
    python sota-validator.py --dir health/      # Проверить папку

Выход:
    - JSON отчёт с ошибками
    - Код возврата 0 = все OK, 1 = есть ошибки
"""

import sys
import re
import json
import argparse
from pathlib import Path
from dataclasses import dataclass, asdict
from typing import List, Optional


@dataclass
class ValidationError:
    file: str
    section: str
    severity: str  # error, warning, info
    message: str
    line: Optional[int] = None


@dataclass
class ValidationResult:
    file: str
    is_valid: bool
    errors: List[ValidationError]
    warnings: List[ValidationError]
    sections_found: List[str]
    sections_missing: List[str]


class SoTAValidator:
    """Валидатор SoTA файлов"""
    
    # Обязательные секции из шаблона SOTA-TEMPLATE.md
    REQUIRED_SECTIONS = [
        "YAML FRONTMATTER",
        "Резюме (Abstract)",
        "КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ",
        "ВВЕДЕНИЕ",
        "МАТЕРИАЛЫ И МЕТОДЫ",
        "РЕЗУЛЬТАТЫ",
        "ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ",
        "ВЫВОДЫ",
        "КРИТИЧЕСКИЙ АНАЛИЗ",
        "FAQ",
        "ИНСТРУМЕНТЫ И ШАБЛОНЫ",
        "ИСТОЧНИКИ",
        "ЖУРНАЛ ОБРАБОТКИ"
    ]
    
    # Обязательные поля YAML
    REQUIRED_YAML_FIELDS = [
        "id",
        "type",
        "domain",
        "area",
        "year",
        "authors",
        "title",
        "journal",
        "tags"
    ]
    
    # Опциональные но рекомендуемые поля
    RECOMMENDED_YAML_FIELDS = [
        "subarea",
        "subarea2",
        "category",
        "volume",
        "pages",
        "doi",
        "related"
    ]
    
    # Паттерны для поиска секций (гибкие — с или без нумерации)
    SECTION_PATTERNS = {
        "YAML FRONTMATTER": r"^---\s*\n",
        "Резюме (Abstract)": r"## \d*\.?\s*Резюме",
        "КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ": r"## \d*\.?\s*КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ",
        "ВВЕДЕНИЕ": r"## \d*\.?\s*ВВЕДЕНИЕ",
        "МАТЕРИАЛЫ И МЕТОДЫ": r"## \d*\.?\s*МАТЕРИАЛЫ И МЕТОДЫ",
        "РЕЗУЛЬТАТЫ": r"## \d*\.?\s*РЕЗУЛЬТАТЫ",
        "ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ": r"## \d*\.?\s*ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ",
        "ВЫВОДЫ": r"## \d*\.?\s*ВЫВОДЫ",
        "КРИТИЧЕСКИЙ АНАЛИЗ": r"## \d*\.?\s*КРИТИЧЕСКИЙ АНАЛИЗ",
        "FAQ": r"## \d*\.?\s*FAQ",
        "ИНСТРУМЕНТЫ И ШАБЛОНЫ": r"## \d*\.?\s*ИНСТРУМЕНТЫ",
        "ИСТОЧНИКИ": r"## \d*\.?\s*ИСТОЧНИКИ",
        "ЖУРНАЛ ОБРАБОТКИ": r"## \d*\.?\s*ЖУРНАЛ ОБРАБОТКИ"
    }
    
    # Обязательные подсекции
    REQUIRED_SUBSECTIONS = {
        "Медиа-инвентарь": r"### \d*\.?\d*\.?\s*Медиа-инвентарь|Медиа-инвентарь"
    }
    
    # Минимальное количество медиа-элементов
    MIN_MEDIA_ITEMS = 2
    
    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.errors: List[ValidationError] = []
        self.warnings: List[ValidationError] = []
    
    def validate_file(self, filepath: Path) -> ValidationResult:
        """Проверить один SoTA файл"""
        self.errors = []
        self.warnings = []
        
        if not filepath.exists():
            self.errors.append(ValidationError(
                file=str(filepath),
                section="general",
                severity="error",
                message=f"Файл не найден: {filepath}"
            ))
            return self._build_result(filepath)
        
        content = filepath.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Проверка YAML frontmatter
        self._validate_yaml(content, filepath)
        
        # Проверка секций
        sections_found, sections_missing = self._validate_sections(content, filepath)
        
        # Проверка подсекций
        self._validate_subsections(content, filepath)
        
        # Проверка структуры утверждений
        self._validate_claims(content, filepath)
        
        # Проверка связей
        self._validate_related(content, filepath)
        
        # Проверка именования файла
        self._validate_filename(filepath)
        
        return self._build_result(filepath, sections_found, sections_missing)
    
    def _validate_yaml(self, content: str, filepath: Path):
        """Проверка YAML frontmatter"""
        yaml_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
        
        if not yaml_match:
            self.errors.append(ValidationError(
                file=str(filepath),
                section="YAML FRONTMATTER",
                severity="error",
                message="Отсутствует YAML frontmatter (должен начинаться с ---)"
            ))
            return
        
        yaml_content = yaml_match.group(1)
        
        # Проверка обязательных полей
        for field in self.REQUIRED_YAML_FIELDS:
            if f"{field}:" not in yaml_content:
                self.errors.append(ValidationError(
                    file=str(filepath),
                    section="YAML FRONTMATTER",
                    severity="error",
                    message=f"Отсутствует обязательное поле: {field}"
                ))
        
        # Проверка рекомендуемых полей
        for field in self.RECOMMENDED_YAML_FIELDS:
            if f"{field}:" not in yaml_content:
                self.warnings.append(ValidationError(
                    file=str(filepath),
                    section="YAML FRONTMATTER",
                    severity="warning",
                    message=f"Отсутствует рекомендуемое поле: {field}"
                ))
        
        # Проверка формата id
        id_match = re.search(r'id:\s*(CS\.SOTA\.\d+)', yaml_content)
        if id_match:
            soTA_id = id_match.group(1)
            expected_pattern = r'CS\.SOTA\.\d{3}'
            if not re.match(expected_pattern, soTA_id):
                self.warnings.append(ValidationError(
                    file=str(filepath),
                    section="YAML FRONTMATTER",
                    severity="warning",
                    message=f"ID '{soTA_id}' не соответствует формату CS.SOTA.XXX (три цифры)"
                ))
        
        # Проверка year
        year_match = re.search(r'year:\s*(\d{4})', yaml_content)
        if not year_match:
            self.errors.append(ValidationError(
                file=str(filepath),
                section="YAML FRONTMATTER",
                severity="error",
                message="Поле year должно быть в формате YYYY"
            ))
    
    def _validate_sections(self, content: str, filepath: Path) -> tuple:
        """Проверка наличия секций"""
        sections_found = []
        sections_missing = []
        
        for section, pattern in self.SECTION_PATTERNS.items():
            if re.search(pattern, content, re.MULTILINE):
                sections_found.append(section)
            else:
                sections_missing.append(section)
                self.errors.append(ValidationError(
                    file=str(filepath),
                    section=section,
                    severity="error",
                    message=f"Отсутствует обязательная секция: {section}"
                ))
        
        return sections_found, sections_missing
    
    def _validate_subsections(self, content: str, filepath: Path):
        """Проверка обязательных подсекций"""
        for subsection, pattern in self.REQUIRED_SUBSECTIONS.items():
            if not re.search(pattern, content, re.MULTILINE):
                self.warnings.append(ValidationError(
                    file=str(filepath),
                    section="Подсекции",
                    severity="warning",
                    message=f"Отсутствует подсекция: {subsection}"
                ))
        
        # Проверка количества медиа-элементов
        media_items = re.findall(r'\*\*\[СКРИНШОТ\]\*\*', content)
        if len(media_items) < self.MIN_MEDIA_ITEMS:
            self.warnings.append(ValidationError(
                file=str(filepath),
                section="Медиа-инвентарь",
                severity="warning",
                message=f"Медиа-инвентарь неполный: найдено {len(media_items)} элементов, рекомендуется минимум {self.MIN_MEDIA_ITEMS}"
            ))
        
        # Проверка наличия комментариев лектора
        lecturer_comments_media = re.findall(r'\*\*Комментарий лектора:\*\*', content)
        if len(lecturer_comments_media) < len(media_items):
            self.warnings.append(ValidationError(
                file=str(filepath),
                section="Медиа-инвентарь",
                severity="warning",
                message=f"Не все медиа-элементы имеют комментарии лектора: {len(lecturer_comments_media)}/{len(media_items)}"
            ))
        
        # Проверка соответствия медиа-инвентаря и результатов
        # Ищем ссылки типа "**Соответствует:** Figure X" в разделе Результаты
        results_section = re.search(
            r'## \d*\.?\s*РЕЗУЛЬТАТЫ.*?(?=## \d*\.?\s*ПРАКТИЧЕСКОЕ|\Z)',
            content,
            re.DOTALL
        )
        if results_section:
            results_content = results_section.group(0)
            # Подсчитываем сколько медиа-элементов упомянуто в результатах
            media_referenced = 0
            for i in range(1, len(media_items) + 1):
                if re.search(rf'Figure {i}|Table {i}|\[СКРИНШОТ\].*?{i}', results_content):
                    media_referenced += 1
            
            if media_referenced < len(media_items):
                self.warnings.append(ValidationError(
                    file=str(filepath),
                    section="РЕЗУЛЬТАТЫ",
                    severity="warning",
                    message=f"Не все медиа-элементы описаны в разделе Результаты: {media_referenced}/{len(media_items)}"
                ))
    
    def _validate_claims(self, content: str, filepath: Path):
        """Проверка структуры ключевых утверждений"""
        claims_section = re.search(
            r'## 2\. КЛЮЧЕВЫЕ УТВЕРЖДЕНИEMA.*?\n(.*?)(?=## 3\.|## 3\. |\Z)',
            content,
            re.DOTALL
        )
        
        if claims_section:
            claims_content = claims_section.group(1)
            
            # Проверка наличия утверждений
            claim_patterns = re.findall(r'### Утверждение \d+:', claims_content)
            if len(claim_patterns) < 2:
                self.warnings.append(ValidationError(
                    file=str(filepath),
                    section="КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ",
                    severity="warning",
                    message=f"Найдено только {len(claim_patterns)} утверждений, рекомендуется 3-5"
                ))
            
            # Проверка структуры каждого утверждения
            required_claim_fields = ["Утверждение:", "Доказательства:", "Уверенность:"]
            for field in required_claim_fields:
                if field not in claims_content:
                    self.warnings.append(ValidationError(
                        file=str(filepath),
                        section="КЛЮЧЕВЫЕ УТВЕРЖДЕНИЯ",
                        severity="warning",
                        message=f"Утверждения должны содержать поле: {field}"
                    ))
    
    def _validate_related(self, content: str, filepath: Path):
        """Проверка связанных SoTA"""
        if 'related:' in content:
            related_count = len(re.findall(r'- id:', content))
            if related_count < 2:
                self.warnings.append(ValidationError(
                    file=str(filepath),
                    section="YAML FRONTMATTER",
                    severity="warning",
                    message=f"Рекомендуется добавить 3-5 связанных SoTA (найдено: {related_count})"
                ))
    
    def _validate_filename(self, filepath: Path):
        """Проверка имени файла"""
        filename = filepath.name
        expected_pattern = r'CS\.SOTA\.\d{3}-[a-z]+-\d{4}\.md'
        
        if not re.match(expected_pattern, filename):
            self.warnings.append(ValidationError(
                file=str(filepath),
                section="general",
                severity="warning",
                message=f"Имя файла '{filename}' не соответствует шаблону CS.SOTA.XXX-author-year.md"
            ))
    
    def _build_result(
        self,
        filepath: Path,
        sections_found: Optional[List[str]] = None,
        sections_missing: Optional[List[str]] = None
    ) -> ValidationResult:
        """Сборка результата валидации"""
        return ValidationResult(
            file=str(filepath),
            is_valid=len(self.errors) == 0,
            errors=self.errors.copy(),
            warnings=self.warnings.copy(),
            sections_found=sections_found or [],
            sections_missing=sections_missing or []
        )
    
    def validate_directory(self, directory: Path) -> List[ValidationResult]:
        """Проверить все SoTA файлы в директории"""
        results = []
        
        for md_file in directory.rglob("CS.SOTA.*.md"):
            if self.verbose:
                print(f"Проверка: {md_file}")
            result = self.validate_file(md_file)
            results.append(result)
        
        return results


def print_report(result: ValidationResult, verbose: bool = False):
    """Печать отчёта о валидации"""
    status = "[OK]" if result.is_valid else "[FAIL]"
    print(f"\n{status} {result.file}")
    
    if result.sections_missing:
        print(f"  Отсутствуют секции: {', '.join(result.sections_missing[:3])}")
    
    if result.errors:
        print(f"  Ошибок: {len(result.errors)}")
        if verbose:
            for err in result.errors[:5]:
                print(f"    - [{err.severity}] {err.section}: {err.message}")
    
    if result.warnings:
        print(f"  Предупреждений: {len(result.warnings)}")
        if verbose:
            for warn in result.warnings[:3]:
                print(f"    - {warn.message}")


def main():
    parser = argparse.ArgumentParser(
        description="Валидатор SoTA файлов",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры:
  python sota-validator.py CS.SOTA.026-aiello-1984.md
  python sota-validator.py --all
  python sota-validator.py --dir health/ --verbose
        """
    )
    parser.add_argument('file', nargs='?', help='Путь к SoTA файлу')
    parser.add_argument('--all', action='store_true', help='Проверить все SoTA')
    parser.add_argument('--dir', help='Проверить директорию')
    parser.add_argument('--verbose', '-v', action='store_true', help='Подробный вывод')
    parser.add_argument('--json', help='Сохранить отчёт в JSON файл')
    
    args = parser.parse_args()
    
    validator = SoTAValidator(verbose=args.verbose)
    results = []
    
    # Определяем что проверять
    if args.file:
        result = validator.validate_file(Path(args.file))
        results.append(result)
        print_report(result, args.verbose)
    
    elif args.all:
        # Поиск от корня PACK-cattle-science
        base_dir = Path(__file__).parent.parent.parent
        sota_dir = base_dir / "pack" / "cattle-science" / "06-sota"
        
        if not sota_dir.exists():
            print(f"[ERROR] Директория SoTA не найдена: {sota_dir}")
            sys.exit(1)
        
        print(f"Проверка всех SoTA в {sota_dir}...")
        results = validator.validate_directory(sota_dir)
        
        for result in results:
            print_report(result, args.verbose)
    
    elif args.dir:
        dir_path = Path(args.dir)
        results = validator.validate_directory(dir_path)
        
        for result in results:
            print_report(result, args.verbose)
    
    else:
        parser.print_help()
        sys.exit(1)
    
    # Статистика
    total = len(results)
    valid = sum(1 for r in results if r.is_valid)
    total_errors = sum(len(r.errors) for r in results)
    total_warnings = sum(len(r.warnings) for r in results)
    
    print(f"\n{'='*50}")
    print(f"Итого: {valid}/{total} файлов валидны")
    print(f"Ошибок: {total_errors}, Предупреждений: {total_warnings}")
    
    # JSON отчёт
    if args.json:
        report = {
            "summary": {
                "total_files": total,
                "valid_files": valid,
                "total_errors": total_errors,
                "total_warnings": total_warnings
            },
            "results": [asdict(r) for r in results]
        }
        
        with open(args.json, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
        print(f"Отчёт сохранён: {args.json}")
    
    # Код возврата
    sys.exit(0 if valid == total else 1)


if __name__ == "__main__":
    main()
