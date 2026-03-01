# Pack Manifest: CS (Cattle Science)

## Metadata

| Field | Value |
|-------|-------|
| **Pack ID** | CS |
| **Full Name** | Наука о содержании и кормлении КРС |
| **Domain** | Cattle husbandry, dairy science |
| **Version** | 0.1.0 |
| **Status** | Draft |
| **Created** | 2026-03-01 |

## Scope

### In Scope
- Feeding science (nutrition, rations, supplements)
- Reproduction management (AI, dry period, calving)
- Economic evaluation (costs, profitability, models)
- Health prevention (metabolic disorders)

### Out of Scope
- Therapeutic veterinary medicine
- Genetics and breeding
- Farm construction and engineering
- Milk processing technology

## Key Entities (Preview)

### Methods

| ID | Description | Source |
|----|-------------|--------|
| CS.METHOD.001 | Protein norm calculation | — |
| CS.METHOD.002 | Energy requirement assessment | — |
| CS.METHOD.003 | Reproductive program evaluation | CS.SOTA.001, CS.SOTA.005 |
| CS.METHOD.004 | Economic simulation modeling | CS.SOTA.001-003, CS.SOTA.005 |
| CS.METHOD.005 | Transition health monitoring | CS.SOTA.004 |
| CS.METHOD.006 | Reproductive program selection | CS.SOTA.005 |

### Domain Entities

| ID | Description | Key Metrics |
|----|-------------|-------------|
| CS.ENTITY.001 | 21-day pregnancy rate | %, target ≥30% |
| CS.ENTITY.002 | Postpartum health syndrome | NEFA, Ca, BHB, haptoglobin |
| CS.ENTITY.003 | Reproductive program efficiency | ED rate, accuracy, compliance |

### Work Products

| ID | Description | Application |
|----|-------------|-------------|
| CS.WP.003 | Reproduction economic report | IEP optimization |
| CS.WP.005 | Health-fertility risk assessment | Transition cow management |
| CS.WP.006 | Reproductive program economic analysis | Program selection |

## Upstream Dependencies

- SPF (Second Principles Framework)
- FPF (First Principles Framework)
- Peer-reviewed scientific literature

## Downstream Consumers

- Course: "Feeding and Management of Dairy Cattle" (planned)
- Personal consulting practice
- Future: DS tools for reproductive decision support

## Index

| Section | File |
|---------|------|
| Bounded Context | [01-domain-contract/01A-bounded-context.md](01-domain-contract/01A-bounded-context.md) |
| Distinctions | [01-domain-contract/01B-distinctions.md](01-domain-contract/01B-distinctions.md) |
| Domain Entities | [02-domain-entities/](02-domain-entities/) |
| Methods | [03-methods/](03-methods/) |
| Work Products | [04-work-products/](04-work-products/) |
| Failure Modes | [05-failure-modes/](05-failure-modes/) |
| SoTA | [06-sota/](06-sota/) |
| Map | [07-map/](07-map/) |

---

*This manifest is the entry point to the pack. Start here for navigation.*
