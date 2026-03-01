# 01A. Bounded Context: Cattle Science

## Domain Definition

**Наука о содержании и кормлении крупного рогатого скота** — инженерная дисциплина, изучающая принципы, методы и нормы оптимального содержания молочного скота с целью максимизации продуктивности, здоровья и экономической эффективности.

## In Scope (Внутри границ)

### Core Areas

| Area | Description | Key Questions |
|------|-------------|---------------|
| **Feeding** | Nutrition, rations, feed supplements | What to feed? How much? When? |
| **Reproduction** | AI, estrus detection, dry period, calving | How to optimize reproductive performance? |
| **Economics** | Cost analysis, profitability models, decision support | What is the economic impact? |
| **Health Prevention** | Metabolic disorders, transition cow management | How to prevent disease? |

### Practitioners

- Dairy nutritionists
- Herd managers
- Reproduction specialists
- Agricultural economists
- Feed consultants

## Out of Scope (Вне границ)

| Area | Why Excluded | Where It Belongs |
|------|--------------|------------------|
| Therapeutic veterinary medicine | Treatment, not prevention | Veterinary medicine pack |
| Genetics and breeding | Selection, not management | Animal genetics pack |
| Farm construction | Infrastructure, not operations | Agricultural engineering pack |
| Milk processing | Post-harvest, not production | Dairy technology pack |
| Crop science | Feed production, not animal nutrition | Agronomy pack |

## Context Map

```
┌─────────────────────────────────────────┐
│         CATTLE SCIENCE (this pack)      │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐  │
│  │ Feeding │ │Repro    │ │Economics │  │
│  └────┬────┘ └────┬────┘ └────┬─────┘  │
│       └───────────┼───────────┘         │
│                   ↓                     │
│            ┌──────────┐                 │
│            │ Health   │                 │
│            │ Prevention│                │
│            └──────────┘                 │
└─────────────────────────────────────────┘
              ↕ Interfaces
┌─────────────────────────────────────────┐
│  VETERINARY    GENETICS    AGRONOMY     │
│  (adjacent    (adjacent   (adjacent    │
│   domains)      domains)    domains)    │
└─────────────────────────────────────────┘
```

## Key Interfaces

| Adjacent Domain | Interface | Nature |
|-----------------|-----------|--------|
| Veterinary medicine | Disease prevention protocols | CS provides risk factors; Vet provides treatment |
| Genetics | Selection criteria for feeding programs | Genetics provides potential; CS provides realization |
| Agronomy | Feed quality and availability | Agronomy provides inputs; CS specifies requirements |
| Economics (general) | Farm-level economic models | CS provides technical parameters |

## Language

**Primary language:** Russian (domain practice)
**Secondary:** English (scientific sources)

Key terms must be defined in both languages where scientific precision requires.

## Validation Criteria

A claim belongs in this pack if:
1. It relates to dairy cattle management (not other species)
2. It addresses feeding, reproduction, economics, or prevention
3. It is supported by scientific evidence or established practice
4. It is actionable by practitioners listed above

---

*Bounded context establishes what this pack is responsible for knowing.*
