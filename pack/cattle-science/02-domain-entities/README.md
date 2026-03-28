# 02-domain-entities

Domain entities for cattle science PACK — structured knowledge base of research entities.

## Structure

```
02-domain-entities/
├── P0/                    # Priority 0: Core foundational entities
│   ├── reproduction/      # Reproductive biology (20 entities)
│   ├── feeding/           # Nutrition and feeding (12 entities)
│   ├── health/            # Health and disease (24 entities)
│   └── management/        # Farm management (1 entity)
├── P1/                    # Priority 1: Important applied entities
│   ├── reproduction/      # (20 entities)
│   ├── feeding/           # (28 entities)
│   ├── health/            # (27 entities)
│   ├── economics/         # Economic analysis (16 entities)
│   └── genetics/          # Genetics and breeding (1 entity)
├── P2/                    # Priority 2: Specialized/advanced entities
│   ├── feeding/           # (34 entities)
│   └── health/            # (3 entities)
└── scripts/               # Maintenance scripts
    └── reorganize-entities.py
```

## Statistics

- **Total entities:** 186
- **P0 (Core):** 57 entities
- **P1 (Important):** 92 entities
- **P2 (Specialized):** 37 entities

## Entity Schema

Each entity follows the PACK entity schema:

```yaml
---
id: DP.ENTITY.XXX
title: Entity Title
priority: P0|P1|P2
area: reproduction|feeding|health|management|economics|genetics
subarea: optional_subarea
type: concept|method|metric|factor|condition
---
```

## Reorganization History

**2026-03-28:** Migrated from flat P0/P1/P2 structure to hierarchical P{priority}/{area}/ structure.

- **Reason:** Scalability — flat structure limited to ~200 entities, hierarchical supports 2000+
- **Script:** `scripts/reorganize-entities.py`
- **Result:** 11 area directories created, 186 entities reorganized

## Usage

### Finding Entities

```bash
# By area
grep -r "area: reproduction" P0/ P1/ P2/ --include="*.md"

# By type
grep -r "type: metric" P0/ P1/ P2/ --include="*.md"

# By priority
ls P0/reproduction/*.md
```

### Adding New Entities

1. Determine priority (P0/P1/P2) and area
2. Create file in appropriate directory: `P{priority}/{area}/DP.ENTITY.XXX.md`
3. Follow entity schema template

## Maintenance

Use the reorganization script for structural changes:

```bash
# Preview changes
python scripts/reorganize-entities.py --dry-run

# Execute migration
python scripts/reorganize-entities.py
```
