#!/usr/bin/env python3
"""
SoTA-Entity Manager

Automates entity creation and bidirectional link updates when creating new SoTA.

Features:
- Extract entities mentioned in SoTA content
- Auto-create missing entities from template
- Update bidirectional links (SoTA <-> Entity)
- Maintain relationship consistency

Usage:
    python sota-entity-manager.py --sota CS.SOTA.001 --extract
    python sota-entity-manager.py --sota CS.SOTA.001 --create-entities
    python sota-entity-manager.py --sota CS.SOTA.001 --update-links
    python sota-entity-manager.py --sota CS.SOTA.001 --full-process
"""

import os
import re
import sys
import argparse
import yaml
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Tuple, Set

# Configuration
PACK_ROOT = Path(__file__).resolve().parent.parent.parent
SOTA_DIR = PACK_ROOT / "06-sota"
ENTITIES_DIR = PACK_ROOT / "02-domain-entities"
TEMPLATE_FILE = ENTITIES_DIR / "00-entity-template.md"

# Entity patterns for extraction
ENTITY_PATTERNS = {
    'diseases': [
        r'кетоз', r'кетоза', r'кетозу', r'кетозом',
        r'мастит', r'мастита', r'маститу',
        r'метрит', r'метрита', r'метриту',
        r'гипокальциеми', r'гипокальцемия',
        r'жировой гепатоз', r'жирового гепатоза',
        r'субклинический кетоз', r'субклинического кетоза',
        r'клинический кетоз',
    ],
    'metrics': [
        r'BHB', r'β-гидроксибутират', r'beta-hydroxybutyrate',
        r'NEFA', r'нэфа', r'non-esterified fatty acids',
        r'глюкоза', r'glucose',
        r'инсулин', r'insulin',
        r'кортизол', r'cortisol',
        r'прогестерон', r'progesterone',
        r'пролактин', r'prolactin',
        r'IGF-1', r'ИГФ-1',
    ],
    'concepts': [
        r'негативный энергетический баланс', r'НЭБ', r'negative energy balance',
        r'переходный период', r'transition period',
        r'сухостойный период', r'dry period',
        r'раннее послеродовой период', r'early postpartum',
        r'открытый период', r'open period',
        r'21-дневная стельность', r'21-day pregnancy',
        r'коэффициент оплодотворяемости', r'conception rate',
        r'сервис период', r'service period',
    ],
    'methods': [
        r'Ovsynch', r'Овсинх',
        r'Presynch', r'Пресинх',
        r'Double-Ovsynch', r'Дабл-Овсинх',
        r'CoSynch', r'КоСинх',
        r'экспресс-тест', r'rapid test',
        r'УЗИ', r'ultrasound',
        r'тест-полоски', r'test strips',
    ],
    'technologies': [
        r'sexed semen', r'сексированная сперма',
        r'beef semen', r'говяжья сперма',
        r'эмбрио-трансфер', r'embryo transfer',
        r'витрофертлизация', r'IVF',
        r'геномный отбор', r'genomic selection',
    ]
}

# Known entity mappings (name -> entity_id)
KNOWN_ENTITIES = {
    # Diseases
    'кетоз': 'CS.ENTITY.018',
    'клинический кетоз': 'CS.ENTITY.018',
    'субклинический кетоз': 'CS.ENTITY.002',
    'субклинического кетоза': 'CS.ENTITY.002',
    'мастит': 'CS.ENTITY.XXX',  # Need to check actual ID
    'метрит': 'CS.ENTITY.XXX',
    'гипокальциемия': 'CS.ENTITY.XXX',
    'жировой гепатоз': 'CS.ENTITY.XXX',
    
    # Metrics
    'bhb': 'CS.ENTITY.007',
    'β-гидроксибутират': 'CS.ENTITY.007',
    'nefa': 'CS.ENTITY.008',
    'глюкоза': 'CS.ENTITY.009',
    'инсулин': 'CS.ENTITY.015',
    'кортизол': 'CS.ENTITY.017',
    'прогестерон': 'CS.ENTITY.040',
    
    # Concepts
    'негативный энергетический баланс': 'CS.ENTITY.XXX',
    'нэб': 'CS.ENTITY.XXX',
    'переходный период': 'CS.ENTITY.XXX',
    
    # Body parts/tissues
    'печень': 'CS.ENTITY.003',
    'жировая ткань': 'CS.ENTITY.005',
    'молоко': 'CS.ENTITY.006',
}


@dataclass
class Entity:
    """Represents a domain entity."""
    id: str
    name_ru: str
    name_en: str
    area: str
    subarea: Optional[str] = None
    abbreviation: Optional[str] = None
    related_sota: List[str] = field(default_factory=list)
    related_entities: List[str] = field(default_factory=list)
    yaml_data: Dict = field(default_factory=dict)
    content: str = ""
    file_path: Optional[Path] = None
    
    @property
    def filename(self) -> str:
        return f"{self.id}-{self.name_ru.lower().replace(' ', '-').replace('_', '-')}.md"


@dataclass
class SoTA:
    """Represents a State of the Art document."""
    id: str
    title: str
    authors: str
    year: int
    area: str
    subarea: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    related: List[Dict] = field(default_factory=list)
    yaml_data: Dict = field(default_factory=dict)
    content: str = ""
    file_path: Optional[Path] = None


class EntityManager:
    """Manages entities and their relationships with SoTA."""
    
    def __init__(self, pack_root: Path = PACK_ROOT):
        self.pack_root = pack_root
        self.sota_dir = pack_root / "06-sota"
        self.entities_dir = pack_root / "02-domain-entities"
        self.template_file = self.entities_dir / "00-entity-template.md"
        
        self.entities: Dict[str, Entity] = {}
        self.sotas: Dict[str, SoTA] = {}
        self.entity_name_map: Dict[str, str] = {}  # name -> id
        
        self._load_all()
    
    def _load_all(self):
        """Load all entities and SoTAs."""
        self._load_entities()
        self._load_sotas()
    
    def _load_entities(self):
        """Load all entities from directory."""
        for priority in ['P0', 'P1', 'P2']:
            priority_dir = self.entities_dir / priority
            if not priority_dir.exists():
                continue
                
            for area_dir in priority_dir.iterdir():
                if not area_dir.is_dir():
                    continue
                    
                for entity_file in area_dir.glob('CS.ENTITY.*.md'):
                    try:
                        content = entity_file.read_text(encoding='utf-8')
                        yaml_data = self._parse_yaml(content)
                        
                        entity = Entity(
                            id=yaml_data.get('id', ''),
                            name_ru=yaml_data.get('name_ru', ''),
                            name_en=yaml_data.get('name_en', ''),
                            area=yaml_data.get('area', ''),
                            subarea=yaml_data.get('subarea'),
                            abbreviation=yaml_data.get('abbreviation'),
                            related_sota=yaml_data.get('related_sota', []),
                            related_entities=yaml_data.get('related_entities', []),
                            yaml_data=yaml_data,
                            content=content,
                            file_path=entity_file
                        )
                        
                        if entity.id:
                            self.entities[entity.id] = entity
                            # Map names to IDs
                            self.entity_name_map[entity.name_ru.lower()] = entity.id
                            self.entity_name_map[entity.name_en.lower()] = entity.id
                            if entity.abbreviation:
                                self.entity_name_map[entity.abbreviation.lower()] = entity.id
                    except Exception as e:
                        print(f"Warning: Could not load entity {entity_file}: {e}")
        
        print(f"Loaded {len(self.entities)} entities")
    
    def _load_sotas(self):
        """Load all SoTAs from directory."""
        for area_dir in self.sota_dir.iterdir():
            if not area_dir.is_dir():
                continue
                
            for sota_file in area_dir.glob('CS.SOTA.*.md'):
                try:
                    content = sota_file.read_text(encoding='utf-8')
                    yaml_data = self._parse_yaml(content)
                    
                    sota = SoTA(
                        id=yaml_data.get('id', ''),
                        title=yaml_data.get('title', ''),
                        authors=yaml_data.get('authors', ''),
                        year=yaml_data.get('year', 0),
                        area=yaml_data.get('area', ''),
                        subarea=yaml_data.get('subarea'),
                        tags=yaml_data.get('tags', []),
                        related=yaml_data.get('related', []),
                        yaml_data=yaml_data,
                        content=content,
                        file_path=sota_file
                    )
                    
                    if sota.id:
                        self.sotas[sota.id] = sota
                except Exception as e:
                    print(f"Warning: Could not load SoTA {sota_file}: {e}")
        
        print(f"Loaded {len(self.sotas)} SoTAs")
    
    def _parse_yaml(self, content: str) -> Dict:
        """Parse YAML frontmatter from markdown."""
        if not content.startswith('---'):
            return {}
        
        try:
            end = content.find('---', 3)
            if end == -1:
                return {}
            
            yaml_content = content[3:end].strip()
            return yaml.safe_load(yaml_content) or {}
        except Exception as e:
            print(f"Warning: YAML parse error: {e}")
            return {}
    
    def get_next_entity_id(self) -> str:
        """Get next available entity ID."""
        max_num = 0
        for entity_id in self.entities.keys():
            match = re.match(r'CS\.ENTITY\.(\d+)', entity_id)
            if match:
                max_num = max(max_num, int(match.group(1)))
        
        return f"CS.ENTITY.{max_num + 1:03d}"
    
    def extract_entities_from_sota(self, sota_id: str) -> List[Dict]:
        """Extract entity mentions from SoTA content."""
        if sota_id not in self.sotas:
            print(f"Error: SoTA {sota_id} not found")
            return []
        
        sota = self.sotas[sota_id]
        content_lower = sota.content.lower()
        
        found_entities = []
        
        # Check known entities
        for name, entity_id in KNOWN_ENTITIES.items():
            if name.lower() in content_lower:
                status = "exists" if entity_id in self.entities else "missing"
                found_entities.append({
                    'name': name,
                    'entity_id': entity_id,
                    'status': status,
                    'type': 'known'
                })
        
        # Check patterns for potential new entities
        for category, patterns in ENTITY_PATTERNS.items():
            for pattern in patterns:
                if pattern.lower() in content_lower:
                    # Check if already in found
                    if not any(f['name'].lower() == pattern.lower() for f in found_entities):
                        found_entities.append({
                            'name': pattern,
                            'entity_id': None,
                            'status': 'potential',
                            'type': category
                        })
        
        return found_entities
    
    def create_entity(self, name_ru: str, name_en: str, area: str, 
                      subarea: Optional[str] = None, 
                      abbreviation: Optional[str] = None,
                      related_sota: List[str] = None) -> Optional[Entity]:
        """Create a new entity from template."""
        if not self.template_file.exists():
            print(f"Error: Template file not found: {self.template_file}")
            return None
        
        entity_id = self.get_next_entity_id()
        
        # Read template
        template_content = self.template_file.read_text(encoding='utf-8')
        
        # Replace placeholders
        entity_content = template_content
        entity_content = entity_content.replace('CS.ENTITY.XXX', entity_id)
        entity_content = entity_content.replace('[Название на русском]', name_ru)
        entity_content = entity_content.replace('[Название на английском]', name_en)
        entity_content = entity_content.replace('health | reproduction | feeding | economics | genetics', area)
        
        if subarea:
            entity_content = entity_content.replace('[уточнение подобласти]', subarea)
        
        if abbreviation:
            entity_content = entity_content.replace('[Аббревиатура, если есть]', abbreviation)
        else:
            entity_content = entity_content.replace('[Аббревиатура, если есть]', '')
        
        # Add related SoTA
        if related_sota:
            sota_list = '\n'.join([f'  - {s}' for s in related_sota])
            entity_content = entity_content.replace('  - CS.SOTA.XXX', sota_list)
        
        # Determine priority based on area
        priority = self._determine_priority(area, subarea)
        
        # Create file path
        area_folder = self._get_area_folder(area)
        target_dir = self.entities_dir / priority / area_folder
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename
        safe_name = name_ru.lower().replace(' ', '-').replace('_', '-')
        safe_name = re.sub(r'[^\w\-]', '', safe_name)
        filename = f"{entity_id}-{safe_name}.md"
        file_path = target_dir / filename
        
        # Write file
        file_path.write_text(entity_content, encoding='utf-8')
        
        # Create entity object
        entity = Entity(
            id=entity_id,
            name_ru=name_ru,
            name_en=name_en,
            area=area,
            subarea=subarea,
            abbreviation=abbreviation,
            related_sota=related_sota or [],
            yaml_data={
                'id': entity_id,
                'name_ru': name_ru,
                'name_en': name_en,
                'area': area,
                'subarea': subarea,
                'abbreviation': abbreviation,
                'related_sota': related_sota or []
            },
            content=entity_content,
            file_path=file_path
        )
        
        # Add to cache
        self.entities[entity_id] = entity
        self.entity_name_map[name_ru.lower()] = entity_id
        self.entity_name_map[name_en.lower()] = entity_id
        if abbreviation:
            self.entity_name_map[abbreviation.lower()] = entity_id
        
        print(f"Created entity: {entity_id} -> {file_path}")
        return entity
    
    def _determine_priority(self, area: str, subarea: Optional[str]) -> str:
        """Determine priority folder for entity."""
        # Core entities go to P0
        core_areas = ['health', 'reproduction', 'feeding']
        if area in core_areas and subarea in ['metabolic-disorders', 'fertility', 'nutrition']:
            return 'P0'
        
        # Important applied entities go to P1
        if area in core_areas:
            return 'P1'
        
        # Specialized/advanced go to P2
        return 'P2'
    
    def _get_area_folder(self, area: str) -> str:
        """Map area to folder name."""
        area_map = {
            'reproduction': 'reproduction',
            'feeding': 'feeding',
            'health': 'health',
            'management': 'management',
            'economics': 'economics',
            'genetics': 'genetics',
        }
        return area_map.get(area, area)
    
    def update_entity_links(self, entity_id: str, sota_id: str) -> bool:
        """Add SoTA link to entity (bidirectional)."""
        if entity_id not in self.entities:
            print(f"Error: Entity {entity_id} not found")
            return False
        
        entity = self.entities[entity_id]
        
        # Check if already linked
        if sota_id in entity.related_sota:
            print(f"Entity {entity_id} already linked to {sota_id}")
            return True
        
        # Add link
        entity.related_sota.append(sota_id)
        
        # Update YAML in content
        if entity.file_path:
            try:
                content = entity.file_path.read_text(encoding='utf-8')
                yaml_data = self._parse_yaml(content)
                yaml_data['related_sota'] = entity.related_sota
                
                # Reconstruct YAML frontmatter
                new_yaml = yaml.dump(yaml_data, allow_unicode=True, sort_keys=False)
                
                # Replace old frontmatter
                end = content.find('---', 3)
                new_content = f"---\n{new_yaml}---{content[end+3:]}"
                
                entity.file_path.write_text(new_content, encoding='utf-8')
                print(f"Updated entity {entity_id} with link to {sota_id}")
                return True
            except Exception as e:
                print(f"Error updating entity {entity_id}: {e}")
                return False
        
        return False
    
    def get_entity_suggestions(self, sota_id: str) -> List[Dict]:
        """Get entity suggestions for a SoTA."""
        extracted = self.extract_entities_from_sota(sota_id)
        
        suggestions = []
        for item in extracted:
            if item['status'] == 'missing':
                suggestions.append({
                    'action': 'create',
                    'name': item['name'],
                    'reason': f"Entity mentioned in SoTA but does not exist"
                })
            elif item['status'] == 'exists':
                entity = self.entities.get(item['entity_id'])
                if entity and sota_id not in entity.related_sota:
                    suggestions.append({
                        'action': 'link',
                        'entity_id': item['entity_id'],
                        'name': entity.name_ru,
                        'reason': f"Entity exists but not linked to {sota_id}"
                    })
        
        return suggestions
    
    def process_sota(self, sota_id: str, dry_run: bool = True) -> Dict:
        """Full processing of a SoTA: extract, suggest, create, link."""
        results = {
            'sota_id': sota_id,
            'extracted': [],
            'created': [],
            'linked': [],
            'errors': []
        }
        
        if sota_id not in self.sotas:
            results['errors'].append(f"SoTA {sota_id} not found")
            return results
        
        # Extract entities
        extracted = self.extract_entities_from_sota(sota_id)
        results['extracted'] = extracted
        
        if dry_run:
            print(f"\n[DRY RUN] Processing {sota_id}")
            print(f"Found {len(extracted)} entity mentions:")
            for item in extracted:
                print(f"  - {item['name']} ({item['status']})")
            return results
        
        # Create missing entities
        for item in extracted:
            if item['status'] == 'missing' and item['entity_id'] is None:
                # This is a potential new entity
                print(f"\nPotential new entity: {item['name']}")
                # In real implementation, would prompt for details
                # For now, just log
                results['created'].append({
                    'name': item['name'],
                    'status': 'skipped (needs manual input)'
                })
        
        # Link existing entities
        for item in extracted:
            if item['status'] == 'exists':
                success = self.update_entity_links(item['entity_id'], sota_id)
                if success:
                    results['linked'].append(item['entity_id'])
        
        return results


def main():
    parser = argparse.ArgumentParser(
        description='SoTA-Entity Manager - Automate entity creation and link updates'
    )
    parser.add_argument('--sota', required=True, help='SoTA ID (e.g., CS.SOTA.001)')
    parser.add_argument('--extract', action='store_true', 
                        help='Extract entity mentions from SoTA')
    parser.add_argument('--suggest', action='store_true',
                        help='Suggest actions for SoTA')
    parser.add_argument('--create-entity', action='store_true',
                        help='Create a new entity (interactive)')
    parser.add_argument('--update-links', action='store_true',
                        help='Update bidirectional links')
    parser.add_argument('--full-process', action='store_true',
                        help='Full processing: extract, suggest, create, link')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without executing')
    parser.add_argument('--name-ru', help='Entity name in Russian (for --create-entity)')
    parser.add_argument('--name-en', help='Entity name in English (for --create-entity)')
    parser.add_argument('--area', help='Entity area (for --create-entity)')
    parser.add_argument('--subarea', help='Entity subarea (for --create-entity)')
    
    args = parser.parse_args()
    
    # Initialize manager
    manager = EntityManager()
    
    if args.extract:
        print(f"\nExtracting entities from {args.sota}...")
        entities = manager.extract_entities_from_sota(args.sota)
        
        print(f"\nFound {len(entities)} mentions:")
        print("-" * 60)
        
        for item in entities:
            status_icon = "[OK]" if item['status'] == 'exists' else "[NEW]"
            print(f"{status_icon} {item['name']}")
            if item['entity_id']:
                print(f"    ID: {item['entity_id']}")
            print(f"    Type: {item['type']}")
            print()
    
    elif args.suggest:
        print(f"\nSuggestions for {args.sota}:")
        print("-" * 60)
        
        suggestions = manager.get_entity_suggestions(args.sota)
        
        for sug in suggestions:
            if sug['action'] == 'create':
                print(f"[CREATE] {sug['name']}")
                print(f"    Reason: {sug['reason']}")
            elif sug['action'] == 'link':
                print(f"[LINK] {sug['entity_id']} - {sug['name']}")
                print(f"    Reason: {sug['reason']}")
            print()
    
    elif args.create_entity:
        if not all([args.name_ru, args.name_en, args.area]):
            print("Error: --name-ru, --name-en, and --area are required for entity creation")
            return 1
        
        entity = manager.create_entity(
            name_ru=args.name_ru,
            name_en=args.name_en,
            area=args.area,
            subarea=args.subarea,
            related_sota=[args.sota] if args.sota else []
        )
        
        if entity:
            print(f"\nSuccessfully created: {entity.id}")
            print(f"Location: {entity.file_path}")
    
    elif args.update_links:
        print(f"\nUpdating links for {args.sota}...")
        
        entities = manager.extract_entities_from_sota(args.sota)
        linked_count = 0
        
        for item in entities:
            if item['status'] == 'exists' and item['entity_id']:
                if not args.dry_run:
                    success = manager.update_entity_links(item['entity_id'], args.sota)
                    if success:
                        linked_count += 1
                else:
                    print(f"[DRY RUN] Would link {item['entity_id']} to {args.sota}")
                    linked_count += 1
        
        print(f"\nLinked {linked_count} entities to {args.sota}")
    
    elif args.full_process:
        results = manager.process_sota(args.sota, dry_run=args.dry_run)
        
        print("\n" + "=" * 60)
        print("PROCESSING RESULTS")
        print("=" * 60)
        print(f"SoTA: {results['sota_id']}")
        print(f"Extracted mentions: {len(results['extracted'])}")
        print(f"Created entities: {len(results['created'])}")
        print(f"Linked entities: {len(results['linked'])}")
        
        if results['errors']:
            print(f"\nErrors:")
            for error in results['errors']:
                print(f"  - {error}")
    
    else:
        parser.print_help()
    
    return 0


# Wrapper for safe printing
def safe_print(text):
    """Print text handling encoding issues."""
    try:
        print(text)
    except UnicodeEncodeError:
        # Fallback: encode to ASCII with replacements
        safe_text = text.encode('ascii', errors='replace').decode('ascii')
        print(safe_text)

if __name__ == '__main__':
    sys.exit(main())
