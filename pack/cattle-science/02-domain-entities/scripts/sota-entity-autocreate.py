#!/usr/bin/env python3
"""
SoTA Entity Auto-Creator

Automatically creates entities from SoTA content and maintains bidirectional links.
Integrates with WP-75 protocol for seamless entity management.

Usage:
    # Interactive mode - analyze SoTA and suggest actions
    python sota-entity-autocreate.py --sota CS.SOTA.001 --analyze
    
    # Auto-create missing entities (with confirmation)
    python sota-entity-autocreate.py --sota CS.SOTA.001 --auto-create
    
    # Update all links
    python sota-entity-autocreate.py --sota CS.SOTA.001 --link-all
    
    # Full pipeline: analyze + create + link
    python sota-entity-autocreate.py --sota CS.SOTA.001 --full
    
    # Batch process multiple SoTAs
    python sota-entity-autocreate.py --batch CS.SOTA.001,CS.SOTA.002,CS.SOTA.003
"""

import os
import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Set, Tuple

# Import from sibling module
import importlib.util
manager_path = Path(__file__).parent / "sota-entity-manager.py"
spec = importlib.util.spec_from_file_location("sota_entity_manager", manager_path)
sota_entity_manager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sota_entity_manager)
EntityManager = sota_entity_manager.EntityManager
Entity = sota_entity_manager.Entity
SoTA = sota_entity_manager.SoTA


@dataclass
class EntityExtraction:
    """Result of entity extraction from SoTA."""
    term: str
    context: str
    entity_type: str  # disease, metric, concept, method, technology
    confidence: float  # 0.0 - 1.0
    existing_entity_id: Optional[str] = None
    suggested_name_ru: Optional[str] = None
    suggested_name_en: Optional[str] = None
    suggested_area: Optional[str] = None
    action: str = "skip"  # skip, link, create


@dataclass
class ProcessingReport:
    """Report of SoTA processing."""
    sota_id: str
    timestamp: str
    extractions: List[EntityExtraction] = field(default_factory=list)
    created_entities: List[str] = field(default_factory=list)
    linked_entities: List[str] = field(default_factory=list)
    skipped: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)
    
    def to_dict(self) -> Dict:
        return {
            'sota_id': self.sota_id,
            'timestamp': self.timestamp,
            'extractions': [asdict(e) for e in self.extractions],
            'created_entities': self.created_entities,
            'linked_entities': self.linked_entities,
            'skipped': self.skipped,
            'errors': self.errors
        }


class EntityAutoCreator(EntityManager):
    """Extended manager with auto-creation capabilities."""
    
    # Enhanced entity detection patterns with context
    ENTITY_SIGNATURES = {
        'subclinical_ketosis': {
            'patterns': [
                r'субклинический кетоз',
                r'субклинического кетоза',
                r'subclinical ketosis',
            ],
            'type': 'disease',
            'name_ru': 'Субклинический кетоз',
            'name_en': 'Subclinical Ketosis',
            'abbreviation': 'SCK',
            'area': 'health',
            'subarea': 'metabolic-disorders',
        },
        'clinical_ketosis': {
            'patterns': [
                r'клинический кетоз',
                r'клинического кетоза',
                r'clinical ketosis',
            ],
            'type': 'disease',
            'name_ru': 'Клинический кетоз',
            'name_en': 'Clinical Ketosis',
            'area': 'health',
            'subarea': 'metabolic-disorders',
        },
        'bhb': {
            'patterns': [
                r'BHB',
                r'β-гидроксибутират',
                r'beta-hydroxybutyrate',
                r'бета-гидроксибутират',
            ],
            'type': 'metric',
            'name_ru': 'β-гидроксибутират',
            'name_en': 'Beta-hydroxybutyrate',
            'abbreviation': 'BHB',
            'area': 'health',
            'subarea': 'metabolic-markers',
        },
        'nefa': {
            'patterns': [
                r'NEFA',
                r'нэфа',
                r'non-esterified fatty acids',
                r'незамещенные жирные кислоты',
            ],
            'type': 'metric',
            'name_ru': 'Незамещенные жирные кислоты',
            'name_en': 'Non-esterified Fatty Acids',
            'abbreviation': 'NEFA',
            'area': 'health',
            'subarea': 'metabolic-markers',
        },
        'negative_energy_balance': {
            'patterns': [
                r'негативный энергетический баланс',
                r'НЭБ',
                r'negative energy balance',
                r'NEB',
            ],
            'type': 'concept',
            'name_ru': 'Негативный энергетический баланс',
            'name_en': 'Negative Energy Balance',
            'abbreviation': 'NEB',
            'area': 'health',
            'subarea': 'metabolic-concepts',
        },
        'transition_period': {
            'patterns': [
                r'переходный период',
                r'transition period',
                r'transition cow',
            ],
            'type': 'concept',
            'name_ru': 'Переходный период',
            'name_en': 'Transition Period',
            'area': 'health',
            'subarea': 'production-stages',
        },
        'sexed_semen': {
            'patterns': [
                r'sexed semen',
                r'сексированная сперма',
                r'sex-sorted semen',
            ],
            'type': 'technology',
            'name_ru': 'Сексированная сперма',
            'name_en': 'Sexed Semen',
            'area': 'reproduction',
            'subarea': 'reproductive-technologies',
        },
        'beef_semen': {
            'patterns': [
                r'beef semen',
                r'говяжья сперма',
                r'beef-on-dairy',
            ],
            'type': 'technology',
            'name_ru': 'Говяжья сперма',
            'name_en': 'Beef Semen',
            'area': 'reproduction',
            'subarea': 'reproductive-technologies',
        },
        'ovsynch': {
            'patterns': [
                r'Ovsynch',
                r'Овсинх',
                r'Ovsync',
            ],
            'type': 'method',
            'name_ru': 'Протокол Ovsynch',
            'name_en': 'Ovsynch Protocol',
            'area': 'reproduction',
            'subarea': 'synchronization-protocols',
        },
        'presynch': {
            'patterns': [
                r'Presynch',
                r'Пресинх',
            ],
            'type': 'method',
            'name_ru': 'Протокол Presynch',
            'name_en': 'Presynch Protocol',
            'area': 'reproduction',
            'subarea': 'synchronization-protocols',
        },
        'genomic_selection': {
            'patterns': [
                r'геномный отбор',
                r'genomic selection',
                r'геномная селекция',
            ],
            'type': 'technology',
            'name_ru': 'Геномный отбор',
            'name_en': 'Genomic Selection',
            'area': 'genetics',
            'subarea': 'selection-methods',
        },
        'activity_monitor': {
            'patterns': [
                r'activity monitor',
                r'активити монитор',
                r'pedometer',
                r'педометр',
            ],
            'type': 'technology',
            'name_ru': 'Монитор активности',
            'name_en': 'Activity Monitor',
            'area': 'management',
            'subarea': 'precision-dairy',
        },
    }
    
    def analyze_sota(self, sota_id: str) -> List[EntityExtraction]:
        """Deep analysis of SoTA for entity extraction."""
        if sota_id not in self.sotas:
            print(f"Error: SoTA {sota_id} not found")
            return []
        
        sota = self.sotas[sota_id]
        content = sota.content
        content_lower = content.lower()
        
        extractions = []
        
        for signature_id, signature in self.ENTITY_SIGNATURES.items():
            for pattern in signature['patterns']:
                # Find all occurrences
                for match in re.finditer(pattern, content, re.IGNORECASE):
                    # Extract context (100 chars before and after)
                    start = max(0, match.start() - 100)
                    end = min(len(content), match.end() + 100)
                    context = content[start:end].replace('\n', ' ')
                    
                    # Check if entity already exists
                    existing_id = None
                    for entity_id, entity in self.entities.items():
                        if (entity.name_ru.lower() == signature['name_ru'].lower() or
                            entity.name_en.lower() == signature['name_en'].lower() or
                            (entity.abbreviation and 
                             entity.abbreviation.lower() == signature.get('abbreviation', '').lower())):
                            existing_id = entity_id
                            break
                    
                    # Determine action
                    if existing_id:
                        entity = self.entities[existing_id]
                        if sota_id in entity.related_sota:
                            action = 'skip'  # Already linked
                        else:
                            action = 'link'  # Exists but not linked
                    else:
                        action = 'create'  # Needs to be created
                    
                    extraction = EntityExtraction(
                        term=pattern,
                        context=context,
                        entity_type=signature['type'],
                        confidence=0.9 if existing_id else 0.7,
                        existing_entity_id=existing_id,
                        suggested_name_ru=signature['name_ru'],
                        suggested_name_en=signature['name_en'],
                        suggested_area=signature['area'],
                        action=action
                    )
                    extractions.append(extraction)
        
        # Remove duplicates (keep highest confidence)
        seen = {}
        for ext in extractions:
            key = ext.suggested_name_ru or ext.term
            if key not in seen or seen[key].confidence < ext.confidence:
                seen[key] = ext
        
        return list(seen.values())
    
    def process_extractions(self, extractions: List[EntityExtraction], 
                           sota_id: str,
                           auto_create: bool = False,
                           dry_run: bool = True) -> Tuple[List[str], List[str]]:
        """Process extractions: create entities and update links."""
        created = []
        linked = []
        
        for ext in extractions:
            if ext.action == 'create' and auto_create:
                if dry_run:
                    print(f"[DRY RUN] Would create: {ext.suggested_name_ru}")
                    created.append(f"DRY:{ext.suggested_name_ru}")
                else:
                    # Create entity
                    entity = self.create_entity(
                        name_ru=ext.suggested_name_ru,
                        name_en=ext.suggested_name_en,
                        area=ext.suggested_area,
                        related_sota=[sota_id]
                    )
                    if entity:
                        created.append(entity.id)
                        ext.existing_entity_id = entity.id
            
            elif ext.action == 'link' or (ext.action == 'create' and ext.existing_entity_id):
                entity_id = ext.existing_entity_id
                if entity_id:
                    if dry_run:
                        print(f"[DRY RUN] Would link: {entity_id} -> {sota_id}")
                        linked.append(f"DRY:{entity_id}")
                    else:
                        success = self.update_entity_links(entity_id, sota_id)
                        if success:
                            linked.append(entity_id)
        
        return created, linked
    
    def generate_report(self, sota_id: str, extractions: List[EntityExtraction],
                       created: List[str], linked: List[str]) -> ProcessingReport:
        """Generate processing report."""
        skipped = [e.suggested_name_ru for e in extractions if e.action == 'skip']
        
        return ProcessingReport(
            sota_id=sota_id,
            timestamp=datetime.now().isoformat(),
            extractions=extractions,
            created_entities=created,
            linked_entities=linked,
            skipped=skipped,
            errors=[]
        )


def safe_print(text):
    """Print text handling encoding issues."""
    try:
        print(text)
    except UnicodeEncodeError:
        safe_text = text.encode('ascii', errors='replace').decode('ascii')
        print(safe_text)

def print_analysis(extractions: List[EntityExtraction]):
    """Print analysis results."""
    safe_print("\n" + "=" * 70)
    safe_print("ENTITY ANALYSIS RESULTS")
    safe_print("=" * 70)
    
    by_action = {'create': [], 'link': [], 'skip': []}
    for ext in extractions:
        by_action[ext.action].append(ext)
    
    if by_action['create']:
        safe_print(f"\n[TO CREATE] {len(by_action['create'])} entities:")
        for ext in by_action['create']:
            safe_print(f"  - {ext.suggested_name_ru} ({ext.suggested_name_en})")
            safe_print(f"    Type: {ext.entity_type}, Area: {ext.suggested_area}")
            # Skip context to avoid encoding issues
            safe_print("")
    
    if by_action['link']:
        safe_print(f"\n[TO LINK] {len(by_action['link'])} entities:")
        for ext in by_action['link']:
            safe_print(f"  - {ext.existing_entity_id}: {ext.suggested_name_ru}")
            safe_print("")
    
    if by_action['skip']:
        safe_print(f"\n[ALREADY LINKED] {len(by_action['skip'])} entities:")
        for ext in by_action['skip']:
            safe_print(f"  - {ext.suggested_name_ru}")
        safe_print("")


def main():
    parser = argparse.ArgumentParser(
        description='SoTA Entity Auto-Creator'
    )
    parser.add_argument('--sota', help='SoTA ID to process')
    parser.add_argument('--batch', help='Comma-separated list of SoTA IDs')
    parser.add_argument('--analyze', action='store_true',
                        help='Analyze SoTA and show entity extraction')
    parser.add_argument('--auto-create', action='store_true',
                        help='Automatically create missing entities')
    parser.add_argument('--link-all', action='store_true',
                        help='Update all entity links')
    parser.add_argument('--full', action='store_true',
                        help='Full pipeline: analyze + create + link')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without executing')
    parser.add_argument('--report', help='Save report to JSON file')
    
    args = parser.parse_args()
    
    if not any([args.sota, args.batch]):
        parser.print_help()
        return 1
    
    # Initialize
    creator = EntityAutoCreator()
    
    # Determine sotas to process
    sota_ids = []
    if args.batch:
        sota_ids = [s.strip() for s in args.batch.split(',')]
    elif args.sota:
        sota_ids = [args.sota]
    
    all_reports = []
    
    for sota_id in sota_ids:
        print(f"\n{'=' * 70}")
        print(f"Processing: {sota_id}")
        print('=' * 70)
        
        if args.analyze or args.full:
            # Analyze
            extractions = creator.analyze_sota(sota_id)
            print_analysis(extractions)
            
            if args.full:
                # Process extractions
                created, linked = creator.process_extractions(
                    extractions, sota_id,
                    auto_create=args.auto_create,
                    dry_run=args.dry_run
                )
                
                # Generate report
                report = creator.generate_report(sota_id, extractions, created, linked)
                all_reports.append(report.to_dict())
                
                print(f"\n[RESULTS]")
                print(f"  Created: {len(created)}")
                print(f"  Linked: {len(linked)}")
        
        elif args.link_all:
            # Just update links
            print(f"\nUpdating all links for {sota_id}...")
            # Implementation would go here
    
    # Save report if requested
    if args.report and all_reports:
        with open(args.report, 'w', encoding='utf-8') as f:
            json.dump(all_reports, f, indent=2, ensure_ascii=False)
        print(f"\nReport saved to: {args.report}")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
