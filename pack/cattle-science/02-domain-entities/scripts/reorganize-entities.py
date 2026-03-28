#!/usr/bin/env python3
"""
Reorganize entities from flat structure to hierarchical by area.

Usage:
    python reorganize-entities.py [--dry-run] [--verbose]

Options:
    --dry-run   Show what would be done without making changes
    --verbose   Show detailed output
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path
from collections import defaultdict

# Configuration
BASE_DIR = Path(__file__).parent.parent
SCRIPT_DIR = Path(__file__).parent

# Area mapping for P0/P1 entities
AREA_MAPPING = {
    'reproduction': ['reproduction', 'breeding', 'fertility', 'insemination', 'pregnancy', 'ovulation', 'estrus', 'cycle'],
    'feeding': ['feeding', 'nutrition', 'metabolism', 'lipid', 'glucose', 'energy', 'rumen', 'diet'],
    'health': ['health', 'disease', 'disorder', 'ketosis', 'hypocalcemia', 'mastitis', 'metritis', 'liver', 'immune', 'inflammation'],
    'management': ['management', 'housing', 'milking', 'culling', 'longevity', 'turnover'],
    'economics': ['economics', 'efficiency', 'profit', 'cost', 'income'],
    'behavior': ['behavior', 'rumination', 'activity', 'welfare', 'stress'],
    'technology': ['technology', 'machine-learning', 'ai', 'ftir', 'metabolomics', 'precision', 'digital'],
    'genetics': ['genetics', 'selection', 'breeding-value', 'genomic']
}

# Special mapping for P2 (molecular entities)
P2_AREA_MAPPING = {
    'lipids': ['lipid', 'ceramide', 'sphingo', 'phosphatidyl', 'cardiolipin', 'glyceride', 'cholesterol'],
    'metabolites': ['metabolite', 'glucose', 'bhb', 'nefa', 'amino-acid', 'carnitine', 'choline'],
    'enzymes': ['enzyme', 'lipase', 'synthase', 'transferase', 'phosphatase', 'kinase', 'dehydrogenase'],
    'proteins': ['protein', 'receptor', 'perilipin', 'adipophilin', 'tip47', 'cgi-58'],
    'signaling': ['signaling', 'calcium', 'serca', 'ryanodine', 'ip3', 'receptor'],
    'organelles': ['organelle', 'mitochondria', 'peroxisome', 'lysosome']
}


def extract_yaml_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            return parts[1].strip()
    return None


def parse_yaml_simple(yaml_content):
    """Simple YAML parser for basic key-value pairs."""
    data = {}
    if not yaml_content:
        return data
    
    current_key = None
    current_list = []
    in_list = False
    
    for line in yaml_content.split('\n'):
        line = line.rstrip()
        
        # Skip empty lines and comments
        if not line or line.startswith('#'):
            continue
        
        # Check for list items
        if line.strip().startswith('- '):
            if in_list and current_key:
                current_list.append(line.strip()[2:].strip())
            continue
        
        # Check for key-value pairs
        if ':' in line and not line.strip().startswith('-'):
            # Save previous list if exists
            if in_list and current_key and current_list:
                data[current_key] = current_list
                current_list = []
            
            in_list = False
            key, value = line.split(':', 1)
            key = key.strip()
            value = value.strip()
            
            # Check if next lines will be a list
            if not value:
                current_key = key
                in_list = True
                current_list = []
            else:
                # Remove quotes if present
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                elif value.startswith("'") and value.endswith("'"):
                    value = value[1:-1]
                data[key] = value
    
    # Save last list if exists
    if in_list and current_key and current_list:
        data[current_key] = current_list
    
    return data


def detect_area_from_content(content, yaml_data, priority):
    """Detect area from YAML data or content."""
    # Try YAML fields first
    for field in ['area', 'subarea', 'domain', 'tags']:
        if field in yaml_data:
            value = yaml_data[field]
            if isinstance(value, str):
                value = value.lower()
                # Check against mapping
                if priority == 'P2':
                    mapping = P2_AREA_MAPPING
                else:
                    mapping = AREA_MAPPING
                
                for area, keywords in mapping.items():
                    for keyword in keywords:
                        if keyword in value:
                            return area
            elif isinstance(value, list):
                for item in value:
                    item = item.lower()
                    if priority == 'P2':
                        mapping = P2_AREA_MAPPING
                    else:
                        mapping = AREA_MAPPING
                    
                    for area, keywords in mapping.items():
                        for keyword in keywords:
                            if keyword in item:
                                return area
    
    # Try content analysis
    content_lower = content.lower()
    
    if priority == 'P2':
        mapping = P2_AREA_MAPPING
    else:
        mapping = AREA_MAPPING
    
    for area, keywords in mapping.items():
        for keyword in keywords:
            if keyword in content_lower:
                return area
    
    # Default fallback
    return 'general'


def get_entity_info(file_path):
    """Extract entity information from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        yaml_content = extract_yaml_frontmatter(content)
        yaml_data = parse_yaml_simple(yaml_content) if yaml_content else {}
        
        # Determine priority from path
        priority = 'P0'
        if '/P1/' in str(file_path):
            priority = 'P1'
        elif '/P2/' in str(file_path):
            priority = 'P2'
        
        # Detect area
        area = detect_area_from_content(content, yaml_data, priority)
        
        return {
            'file_path': file_path,
            'file_name': file_path.name,
            'priority': priority,
            'area': area,
            'yaml_data': yaml_data,
            'entity_id': yaml_data.get('id', 'UNKNOWN')
        }
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None


def create_migration_plan(entities_dir, dry_run=False, verbose=False):
    """Create migration plan for all entities."""
    plan = defaultdict(list)
    errors = []
    
    # Scan all priority directories
    for priority in ['P0', 'P1', 'P2']:
        priority_dir = entities_dir / priority
        if not priority_dir.exists():
            continue
        
        if verbose:
            print(f"\nScanning {priority}/...")
        
        for md_file in priority_dir.glob('*.md'):
            if md_file.name == 'README.md':
                continue
            
            info = get_entity_info(md_file)
            if info:
                plan[priority].append(info)
            else:
                errors.append(f"Failed to parse: {md_file}")
    
    return plan, errors


def execute_migration(plan, entities_dir, dry_run=False, verbose=False):
    """Execute the migration plan."""
    stats = {
        'moved': 0,
        'created_dirs': 0,
        'errors': 0,
        'by_area': defaultdict(int)
    }
    
    for priority, entities in plan.items():
        if verbose:
            print(f"\n{'='*60}")
            print(f"Processing {priority}: {len(entities)} entities")
            print(f"{'='*60}")
        
        # Group by area
        by_area = defaultdict(list)
        for entity in entities:
            by_area[entity['area']].append(entity)
        
        for area, area_entities in by_area.items():
            # Create target directory
            target_dir = entities_dir / priority / area
            
            if not dry_run:
                target_dir.mkdir(parents=True, exist_ok=True)
            
            stats['created_dirs'] += 1
            
            if verbose:
                print(f"\n  {area}/ ({len(area_entities)} entities)")
            
            for entity in area_entities:
                source = entity['file_path']
                target = target_dir / entity['file_name']
                
                if verbose:
                    print(f"    {entity['file_name']} → {priority}/{area}/")
                
                if not dry_run:
                    try:
                        shutil.move(str(source), str(target))
                        stats['moved'] += 1
                        stats['by_area'][f"{priority}/{area}"] += 1
                    except Exception as e:
                        print(f"ERROR moving {source}: {e}")
                        stats['errors'] += 1
                else:
                    stats['moved'] += 1
                    stats['by_area'][f"{priority}/{area}"] += 1
    
    return stats


def generate_summary(plan, stats, dry_run=False):
    """Generate migration summary."""
    print("\n" + "="*60)
    print("MIGRATION SUMMARY")
    print("="*60)
    
    mode = "DRY RUN (no changes made)" if dry_run else "EXECUTED"
    print(f"\nMode: {mode}")
    
    # Count entities by priority
    total_entities = sum(len(entities) for entities in plan.values())
    print(f"\nTotal entities: {total_entities}")
    
    for priority in ['P0', 'P1', 'P2']:
        if priority in plan:
            count = len(plan[priority])
            print(f"  {priority}: {count} entities")
    
    print(f"\nDirectories created: {stats['created_dirs']}")
    print(f"Files moved: {stats['moved']}")
    print(f"Errors: {stats['errors']}")
    
    print("\nDistribution by area:")
    for area, count in sorted(stats['by_area'].items()):
        print(f"  {area}: {count}")
    
    if not dry_run and stats['errors'] == 0:
        print("\n[OK] Migration completed successfully!")
        print("\nNext steps:")
        print("1. Review the new structure")
        print("2. Update any hardcoded paths")
        print("3. Run: git add -A && git commit -m 'Reorganize entities by area'")
    elif dry_run:
        print("\n[NOTE] This was a dry run. No changes were made.")
        print("To execute migration, run without --dry-run")


def create_readme_for_area(area_dir, area_name, entities):
    """Create README.md for each area directory."""
    readme_content = f"""# {area_name.title()} Entities

## Overview

This directory contains {len(entities)} entities related to {area_name}.

## Entities

| ID | Name | Priority |
|----|------|----------|
"""
    
    for entity in sorted(entities, key=lambda x: x['entity_id']):
        name = entity['yaml_data'].get('name', entity['file_name'])
        if isinstance(name, dict):
            name = name.get('en', name.get('ru', 'Unknown'))
        readme_content += f"| {entity['entity_id']} | {name} | {entity['priority']} |\n"
    
    readme_content += f"""
## Related Areas

- See other areas in ../
- Cross-area relationships: ../../03-interpretations/

---

*Auto-generated by reorganize-entities.py*
"""
    
    return readme_content


def main():
    parser = argparse.ArgumentParser(
        description='Reorganize entities from flat to hierarchical structure'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without making changes'
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed output'
    )
    parser.add_argument(
        '--create-readmes',
        action='store_true',
        help='Create README.md for each area directory'
    )
    
    args = parser.parse_args()
    
    entities_dir = BASE_DIR
    
    print("="*60)
    print("ENTITY REORGANIZATION SCRIPT")
    print("="*60)
    print(f"\nBase directory: {entities_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    
    # Create migration plan
    print("\nCreating migration plan...")
    plan, errors = create_migration_plan(entities_dir, args.dry_run, args.verbose)
    
    if errors:
        print("\n⚠️  Errors encountered:")
        for error in errors:
            print(f"  - {error}")
    
    if not plan:
        print("\n❌ No entities found!")
        return 1
    
    # Show plan summary
    print(f"\nMigration plan created:")
    for priority, entities in plan.items():
        print(f"  {priority}: {len(entities)} entities")
    
    # Confirm if not dry-run
    if not args.dry_run:
        print("\n" + "="*60)
        response = input("Proceed with migration? [y/N]: ")
        if response.lower() != 'y':
            print("Migration cancelled.")
            return 0
    
    # Execute migration
    print("\nExecuting migration...")
    stats = execute_migration(plan, entities_dir, args.dry_run, args.verbose)
    
    # Create READMEs if requested
    if args.create_readmes and not args.dry_run:
        print("\nCreating README files...")
        for priority, entities in plan.items():
            by_area = defaultdict(list)
            for entity in entities:
                by_area[entity['area']].append(entity)
            
            for area, area_entities in by_area.items():
                area_dir = entities_dir / priority / area
                readme_path = area_dir / 'README.md'
                readme_content = create_readme_for_area(area_dir, area, area_entities)
                
                with open(readme_path, 'w', encoding='utf-8') as f:
                    f.write(readme_content)
                
                if args.verbose:
                    print(f"  Created {priority}/{area}/README.md")
    
    # Generate summary
    generate_summary(plan, stats, args.dry_run)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
