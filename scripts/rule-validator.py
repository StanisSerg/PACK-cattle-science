#!/usr/bin/env python3
"""
RULE Validator v1.0
Проверяет RULE-файлы на соответствие шаблону RULE-TEMPLATE.md

Usage:
  python rule-validator.py RULE-001-ketosis-threshold.md
  python rule-validator.py --all  # проверить все RULE в pack/rules/
  python rule-validator.py --fix  # авто-исправление где возможно
"""

import re
import sys
import os
import argparse
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Tuple, Optional


@dataclass
class ValidationResult:
    """Результат валидации одного RULE"""
    rule_id: str
    filepath: str
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    passed: List[str] = field(default_factory=list)
    
    @property
    def is_valid(self) -> bool:
        return len(self.errors) == 0
    
    def report(self) -> str:
        lines = [f"\n{'='*60}", f"RULE: {self.rule_id}", f"File: {self.filepath}", f"{'='*60}"]
        
        if self.passed:
            lines.append(f"\n✓ Passed ({len(self.passed)}):")
            for p in self.passed:
                lines.append(f"  ✓ {p}")
        
        if self.warnings:
            lines.append(f"\n⚠ Warnings ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"  ⚠ {w}")
        
        if self.errors:
            lines.append(f"\n✗ Errors ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"  ✗ {e}")
        
        lines.append(f"\n{'='*60}")
        lines.append(f"Status: {'VALID' if self.is_valid else 'INVALID'}")
        lines.append(f"{'='*60}\n")
        
        return "\n".join(lines)


class RuleValidator:
    """Валидатор RULE-файлов"""
    
    # Обязательные поля в frontmatter
    REQUIRED_FRONTMATTER = [
        "rule_id",
        "dl_ref",
        "case_refs",
        "date_created",
        "date_updated",
        "author",
        "category",
        "tags",
        "rule_version",
        "rule_maturity",
        "status",
        "trend",
        "metrics_enabled",
        "confidence",
    ]
    
    # Обязательные секции в теле документа
    REQUIRED_SECTIONS = [
        ("DECISION", "Trigger Conditions"),
        ("STATE MACHINE", "State Definitions"),
        ("ACTION PROTOCOL", None),
        ("BECAUSE", "Научное обоснование"),
        ("LIMITS", "Hard Limits"),
        ("VALIDATION", "Current Evidence Base"),
        ("RULE METRICS", "Outcome Registration"),
        ("CHANGE LOG", None),
        ("ROBUSTNESS ANALYSIS", "Known Limitations"),
        ("Execution Framework", "Phase 1"),
    ]
    
    # Допустимые значения для enum полей
    VALID_MATURITY = ["conceptual", "pilot-ready", "pilot-active", "production", "deprecated"]
    VALID_STATUS = ["conceptual", "testing", "stable", "degraded", "deprecated"]
    VALID_TREND = ["improving", "stable", "degrading"]
    VALID_CONFIDENCE = ["low", "medium", "high"]
    VALID_CATEGORIES = [
        "metabolic", "reproductive", "infectious", 
        "nutritional", "management", "genetic", "welfare"
    ]
    
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.content = ""
        self.frontmatter = {}
        self.body = ""
        
    def load(self) -> bool:
        """Загружает файл"""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except Exception as e:
            return False
    
    def parse_frontmatter(self) -> bool:
        """Парсит YAML frontmatter"""
        pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
        match = re.match(pattern, self.content, re.DOTALL)
        
        if not match:
            return False
        
        fm_text = match.group(1)
        self.body = match.group(2)
        
        # Простой парсинг YAML (ключ: значение)
        for line in fm_text.split('\n'):
            line = line.strip()
            if ':' in line and not line.startswith('#'):
                key, value = line.split(':', 1)
                key = key.strip()
                # Убираем комментарии после значения
                value = value.split('#')[0].strip()
                value = value.strip().strip('"').strip("'")
                self.frontmatter[key] = value
        
        return True
    
    def validate_frontmatter(self, result: ValidationResult):
        """Валидирует frontmatter"""
        if not self.parse_frontmatter():
            result.errors.append("Frontmatter не найден или некорректен (должен быть между ---)")
            return
        
        # Проверяем обязательные поля
        for field in self.REQUIRED_FRONTMATTER:
            if field not in self.frontmatter:
                result.errors.append(f"Отсутствует обязательное поле: {field}")
            else:
                result.passed.append(f"Frontmatter поле: {field}")
        
        # Проверяем формат rule_id
        if 'rule_id' in self.frontmatter:
            if not re.match(r'^RULE-\d+$', self.frontmatter['rule_id']):
                result.errors.append(f"rule_id должен быть формата RULE-NNN, получено: {self.frontmatter['rule_id']}")
        
        # Проверяем enum значения
        if 'rule_maturity' in self.frontmatter:
            if self.frontmatter['rule_maturity'] not in self.VALID_MATURITY:
                result.errors.append(f"rule_maturity должен быть одним из: {', '.join(self.VALID_MATURITY)}")
        
        if 'status' in self.frontmatter:
            if self.frontmatter['status'] not in self.VALID_STATUS:
                result.errors.append(f"status должен быть одним из: {', '.join(self.VALID_STATUS)}")
        
        if 'trend' in self.frontmatter:
            if self.frontmatter['trend'] not in self.VALID_TREND:
                result.errors.append(f"trend должен быть одним из: {', '.join(self.VALID_TREND)}")
        
        if 'confidence' in self.frontmatter:
            if self.frontmatter['confidence'] not in self.VALID_CONFIDENCE:
                result.errors.append(f"confidence должен быть одним из: {', '.join(self.VALID_CONFIDENCE)}")
        
        if 'category' in self.frontmatter:
            if self.frontmatter['category'] not in self.VALID_CATEGORIES:
                result.warnings.append(f"category нестандартный: {self.frontmatter['category']}")
    
    def validate_sections(self, result: ValidationResult):
        """Валидирует наличие обязательных секций"""
        for section, subsection in self.REQUIRED_SECTIONS:
            pattern = rf'##\s*{re.escape(section)}'
            if not re.search(pattern, self.body, re.IGNORECASE):
                result.errors.append(f"Отсутствует секция: {section}")
            else:
                result.passed.append(f"Секция: {section}")
                
                # Если есть subsection — проверяем и её
                if subsection:
                    # Ищем subsection внутри section
                    section_pattern = rf'##\s*{re.escape(section)}.*?(?=##|\Z)'
                    section_match = re.search(section_pattern, self.body, re.IGNORECASE | re.DOTALL)
                    if section_match:
                        section_content = section_match.group(0)
                        if subsection not in section_content:
                            result.warnings.append(f"В секции {section} нет подсекции {subsection}")
    
    def validate_structure(self, result: ValidationResult):
        """Валидирует структурные элементы"""
        # Проверяем наличие State Machine диаграммы
        if "INITIAL" not in self.body and "state" not in self.body.lower():
            result.warnings.append("Возможно отсутствует State Machine диаграмма")
        
        # Проверяем наличие таблиц
        table_count = len(re.findall(r'\|.*\|.*\|', self.body))
        if table_count < 3:
            result.warnings.append(f"Мало таблиц ({table_count}), ожидается минимум 3")
        else:
            result.passed.append(f"Таблиц: {table_count}")
        
        # Проверяем наличие YAML блоков
        yaml_blocks = len(re.findall(r'```yaml', self.body))
        if yaml_blocks < 3:
            result.warnings.append(f"Мало YAML блоков ({yaml_blocks}), ожидается минимум 3")
        else:
            result.passed.append(f"YAML блоков: {yaml_blocks}")
        
        # Проверяем System Loop
        if "CASE → PREDICTION → DECISION" not in self.body:
            result.errors.append("Отсутствует System Loop (CASE → PREDICTION → ...)")
        else:
            result.passed.append("System Loop присутствует")
        
        # Проверяем Execution Framework
        if "Phase 1" not in self.body or "Phase 2" not in self.body:
            result.errors.append("Отсутствует Execution Framework (Phase 1, Phase 2...)")
        else:
            result.passed.append("Execution Framework присутствует")
        
        # Проверяем Root Cause с Priority
        if "P1" not in self.body or "P2" not in self.body:
            result.warnings.append("Возможно отсутствуют Root Cause Priority (P1/P2/P3)")
        else:
            result.passed.append("Root Cause Priority присутствует")
    
    def validate(self) -> ValidationResult:
        """Полная валидация"""
        result = ValidationResult(
            rule_id=self.frontmatter.get('rule_id', 'UNKNOWN'),
            filepath=self.filepath
        )
        
        if not self.load():
            result.errors.append(f"Не удалось загрузить файл: {self.filepath}")
            return result
        
        self.validate_frontmatter(result)
        self.validate_sections(result)
        self.validate_structure(result)
        
        return result


def main():
    parser = argparse.ArgumentParser(description='RULE Validator')
    parser.add_argument('file', nargs='?', help='Путь к RULE-файлу')
    parser.add_argument('--all', action='store_true', help='Проверить все RULE в pack/rules/')
    parser.add_argument('--dir', default='pack/rules', help='Директория с RULE (по умолчанию: pack/rules)')
    
    args = parser.parse_args()
    
    if args.all:
        # Находим все RULE-файлы
        rules_dir = Path(args.dir)
        if not rules_dir.exists():
            print(f"Директория не найдена: {rules_dir}")
            sys.exit(1)
        
        rule_files = list(rules_dir.glob('RULE-*.md'))
        
        if not rule_files:
            print(f"RULE-файлы не найдены в {rules_dir}")
            sys.exit(1)
        
        print(f"Найдено {len(rule_files)} RULE-файлов")
        
        all_valid = True
        for rule_file in sorted(rule_files):
            # Пропускаем TEMPLATE и REGISTRY
            if 'TEMPLATE' in rule_file.name or 'REGISTRY' in rule_file.name:
                continue
                
            validator = RuleValidator(str(rule_file))
            result = validator.validate()
            print(result.report())
            
            if not result.is_valid:
                all_valid = False
        
        sys.exit(0 if all_valid else 1)
    
    elif args.file:
        validator = RuleValidator(args.file)
        result = validator.validate()
        print(result.report())
        sys.exit(0 if result.is_valid else 1)
    
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
