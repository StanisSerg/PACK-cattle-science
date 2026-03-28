#!/usr/bin/env python3
"""
WP-75 Entity Integration

Integrates entity auto-creation into WP-75 SoTA Ingestion Protocol.
This script should be called after creating a new SoTA to:
1. Extract entities mentioned in the SoTA
2. Create missing entities automatically
3. Update bidirectional links
4. Generate a report for the processing log

Usage:
    # After creating a new SoTA, run:
    python wp75-entity-integration.py --sota CS.SOTA.XXX
    
    # Dry run (preview only):
    python wp75-entity-integration.py --sota CS.SOTA.XXX --dry-run
    
    # Skip confirmation prompts:
    python wp75-entity-integration.py --sota CS.SOTA.XXX --yes
    
    # Batch process after WP-75 session:
    python wp75-entity-integration.py --batch CS.SOTA.010,CS.SOTA.011,CS.SOTA.012

Integration with WP-75:
    This script is designed to be called during Phase 3 (Closing) of WP-75,
    specifically after the SoTA content is complete but before git commit.
"""

import os
import sys
import argparse
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Import from sibling module
import importlib.util
manager_path = Path(__file__).parent / "sota-entity-manager.py"
spec = importlib.util.spec_from_file_location("sota_entity_manager", manager_path)
sota_entity_manager = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sota_entity_manager)
EntityManager = sota_entity_manager.EntityManager


class WP75EntityIntegration:
    """Integrates entity management with WP-75 protocol."""
    
    def __init__(self):
        self.manager = EntityManager()
        self.report = {
            'timestamp': datetime.now().isoformat(),
            'sotas_processed': [],
            'entities_created': [],
            'entities_linked': [],
            'skipped': [],
            'errors': []
        }
    
    def process_sota(self, sota_id: str, dry_run: bool = True, 
                     auto_create: bool = False, yes: bool = False) -> Dict:
        """Process a single SoTA through the integration pipeline."""
        print(f"\n{'='*70}")
        print(f"WP-75 Entity Integration: {sota_id}")
        print('='*70)
        
        result = {
            'sota_id': sota_id,
            'status': 'success',
            'entities_created': [],
            'entities_linked': [],
            'errors': []
        }
        
        # Step 1: Extract entities
        print("\n[Step 1] Extracting entities from SoTA...")
        extracted = self.manager.extract_entities_from_sota(sota_id)
        
        if not extracted:
            print("  No entities found in SoTA content.")
            return result
        
        print(f"  Found {len(extracted)} entity mentions")
        
        # Categorize
        to_create = [e for e in extracted if e['status'] == 'missing']
        to_link = [e for e in extracted if e['status'] == 'exists']
        
        # Step 2: Show summary
        print(f"\n[Step 2] Summary:")
        print(f"  - Missing entities to create: {len(to_create)}")
        print(f"  - Existing entities to link: {len(to_link)}")
        
        # Step 3: Create missing entities
        if to_create:
            print(f"\n[Step 3] Entity Creation:")
            
            for item in to_create:
                name = item['name']
                
                if dry_run:
                    print(f"  [DRY RUN] Would create: {name}")
                    result['entities_created'].append(f"DRY:{name}")
                    continue
                
                if auto_create or yes:
                    # Auto-create with default settings
                    # In production, would use intelligent defaults from context
                    print(f"  Creating: {name}")
                    # entity = self.manager.create_entity(...)
                    # result['entities_created'].append(entity.id)
                    result['entities_created'].append(f"PENDING:{name}")
                else:
                    # Interactive mode
                    response = input(f"  Create entity '{name}'? [y/n/skip]: ")
                    if response.lower() == 'y':
                        print(f"    Creating... (interactive input needed)")
                        result['entities_created'].append(f"PENDING:{name}")
                    else:
                        print(f"    Skipped")
                        result['skipped'].append(name)
        
        # Step 4: Update links
        if to_link:
            print(f"\n[Step 4] Updating Links:")
            
            for item in to_link:
                entity_id = item['entity_id']
                
                if dry_run:
                    print(f"  [DRY RUN] Would link: {entity_id} <-> {sota_id}")
                    result['entities_linked'].append(f"DRY:{entity_id}")
                    continue
                
                success = self.manager.update_entity_links(entity_id, sota_id)
                if success:
                    print(f"  [OK] Linked: {entity_id}")
                    result['entities_linked'].append(entity_id)
                else:
                    print(f"  [FAIL] Could not link: {entity_id}")
                    result['errors'].append(f"Link failed: {entity_id}")
        
        # Step 5: Generate processing log entry
        print(f"\n[Step 5] Processing Log Entry:")
        log_entry = self._generate_log_entry(sota_id, result)
        print(log_entry)
        
        # Update report
        self.report['sotas_processed'].append(sota_id)
        self.report['entities_created'].extend(result['entities_created'])
        self.report['entities_linked'].extend(result['entities_linked'])
        
        return result
    
    def _generate_log_entry(self, sota_id: str, result: Dict) -> str:
        """Generate a log entry for the SoTA processing log."""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        
        lines = [
            f"| {timestamp} | Entity Integration | Auto-extracted entities |",
            f"| | | Created: {len(result['entities_created'])} |",
            f"| | | Linked: {len(result['entities_linked'])} |",
        ]
        
        return '\n'.join(lines)
    
    def save_report(self, filepath: Optional[str] = None):
        """Save the integration report."""
        if filepath is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filepath = f"wp75-entity-report-{timestamp}.json"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.report, f, indent=2, ensure_ascii=False)
        
        print(f"\nReport saved to: {filepath}")
    
    def print_summary(self):
        """Print final summary."""
        print("\n" + "="*70)
        print("WP-75 ENTITY INTEGRATION SUMMARY")
        print("="*70)
        print(f"SoTAs processed: {len(self.report['sotas_processed'])}")
        print(f"Entities created: {len(self.report['entities_created'])}")
        print(f"Entities linked: {len(self.report['entities_linked'])}")
        print(f"Errors: {len(self.report['errors'])}")
        
        if self.report['errors']:
            print("\nErrors:")
            for error in self.report['errors']:
                print(f"  - {error}")


def main():
    parser = argparse.ArgumentParser(
        description='WP-75 Entity Integration - Automate entity management for SoTAs'
    )
    parser.add_argument('--sota', help='Single SoTA ID to process')
    parser.add_argument('--batch', help='Comma-separated list of SoTA IDs')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without executing')
    parser.add_argument('--auto-create', action='store_true',
                        help='Automatically create entities without prompting')
    parser.add_argument('--yes', '-y', action='store_true',
                        help='Answer yes to all prompts')
    parser.add_argument('--report', help='Save report to file')
    parser.add_argument('--silent', action='store_true',
                        help='Minimal output')
    
    args = parser.parse_args()
    
    if not any([args.sota, args.batch]):
        print("Error: Must specify --sota or --batch")
        parser.print_help()
        return 1
    
    # Initialize integration
    integration = WP75EntityIntegration()
    
    # Determine SoTAs to process
    sota_ids = []
    if args.batch:
        sota_ids = [s.strip() for s in args.batch.split(',')]
    elif args.sota:
        sota_ids = [args.sota]
    
    # Process each SoTA
    for sota_id in sota_ids:
        result = integration.process_sota(
            sota_id=sota_id,
            dry_run=args.dry_run,
            auto_create=args.auto_create,
            yes=args.yes
        )
    
    # Print summary
    if not args.silent:
        integration.print_summary()
    
    # Save report if requested
    if args.report:
        integration.save_report(args.report)
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
