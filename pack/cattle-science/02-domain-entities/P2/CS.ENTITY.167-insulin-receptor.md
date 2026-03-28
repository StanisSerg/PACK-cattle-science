---
id: CS.ENTITY.167
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: metabolic-regulation
tags: [insulin-receptor, tyrosine-kinase, glucose-uptake, insulin-signaling, metabolic-regulation]
related:
  - id: CS.ENTITY.045
    type: related
    note: Insulin (ligand)
  - id: CS.ENTITY.166
    type: related
    note: mTOR (downstream pathway)
  - id: CS.ENTITY.162
    type: related
    note: SREBP-1c (downstream target)
---

# Insulin receptor

## Definition

**EN:** The insulin receptor (INSR) is a transmembrane receptor tyrosine kinase that mediates the cellular effects of insulin, including glucose uptake, glycogen synthesis, lipogenesis, and protein synthesis. It is a heterotetrameric protein (α2β2) with extracellular α subunits that bind insulin and transmembrane β subunits with intrinsic tyrosine kinase activity. Upon insulin binding, it autophosphorylates and activates downstream signaling cascades including PI3K/Akt and MAPK pathways.

**RU:** Рецептор инсулина (INSR) — трансмембранный рецептор с тирозинкиназной активностью, медиирующий клеточные эффекты инсулина, включая захват глюкозы, синтез гликогена, липогенез и синтез белков. Является гетеротетрамерным белком (α2β2) с экстраклеточными α-субъединицами, связывающими инсулин, и трансмембранными β-субъединицами с внутренней тирозинкиназной активностью. При связывании инсулина аутофосфорилируется и активирует нисходящие сигнальные каскады, включая пути PI3K/Akt и MAPK.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
Insulin receptor is the gateway for:
- Glucose homeostasis regulation
- Metabolic adaptation to feeding/fasting
- Tissue-specific insulin sensitivity
- Pathophysiology of insulin resistance

## Properties

### Structural Characteristics
| Feature | Description |
|---------|-------------|
| Structure | Heterotetramer (α2β2) |
| α subunits | 135 kDa, extracellular, insulin binding |
| β subunits | 95 kDa, transmembrane, kinase domain |
| Gene | INSR (chromosome location varies by species) |
| Isoforms | INSR-A (fetal), INSR-B (adult, metabolic) |

### Activation Mechanism
```
Insulin binding → α subunit conformational change
                        ↓
            Transmembrane signal transmission
                        ↓
            β subunit autophosphorylation (Tyr residues)
                        ↓
            Tyrosine kinase activation
                        ↓
            Phosphorylation of IRS proteins
                        ↓
            PI3K/Akt and MAPK pathway activation
```

### Signaling Pathways
| Pathway | Key Components | Metabolic Effects |
|---------|----------------|-------------------|
| PI3K/Akt | IRS → PI3K → PIP3 → PDK1 → Akt | Glucose uptake, glycogen synthesis, lipogenesis |
| MAPK | Shc → Grb2 → SOS → Ras → Raf → MEK → ERK | Growth, proliferation |
| CAP/Cbl | Cbl → C3G → TC10 | GLUT4 translocation (alternative) |

## Physiological Role

### In Glucose Homeostasis
- **Glucose uptake**: GLUT4 translocation to membrane
- **Glycogen synthesis**: GSK3 inhibition, glycogen synthase activation
- **Gluconeogenesis suppression**: FOXO1 inhibition

### In Lipid Metabolism
- **Lipogenesis**: SREBP-1c activation, FAS/ACC induction
- **Lipolysis inhibition**: HSL phosphorylation/inhibition
- **VLDL clearance**: LPL induction

### In Protein Metabolism
- **Protein synthesis**: mTORC1 activation via Akt/TSC
- **Protein degradation**: Autophagy suppression

### In Dairy Cows
- **Transition period**: Insulin sensitivity changes dramatically
- **Negative energy balance**: Insulin resistance develops
- **Lactation**: Prioritizes glucose for mammary gland
- **Body condition**: Insulin drives fat storage

## Clinical and Research Significance

### Insulin Resistance
```
Chronic NEB → Elevated NEFA → Lipid accumulation in muscle/liver
                                    ↓
                    Serine phosphorylation of IRS-1
                                    ↓
                        Impaired PI3K activation
                                    ↓
                    Reduced glucose uptake + Metabolic dysregulation
```

### Research Applications
- **Glucose tolerance tests**: Assess insulin sensitivity
- **Tissue biopsies**: Receptor expression and phosphorylation
- **Transition studies**: Dynamics of insulin resistance

## Measurement Methods

### Receptor Binding Assay
- **Principle**: Radiolabeled insulin binding
- **Sample**: Membrane preparations
- **Output**: Receptor number and affinity

### Tyrosine Kinase Activity
- **Principle**: Phosphorylation of synthetic substrate
- **Sample**: Immunoprecipitated receptor
- **Unit**: pmol phosphate/min/mg protein

### Western Blot
- **Total INSR**: Expression levels
- **Phospho-Tyr**: Activation state
- **IRS proteins**: Downstream signaling

### Functional Assessment
- **Hyperinsulinemic-euglycemic clamp**: Gold standard for sensitivity
- **Glucose tolerance test**: Clinical assessment
- **HOMA-IR**: Surrogate insulin resistance index

## Related Entities

### Ligand and Signaling
- CS.ENTITY.045: Insulin (ligand)
- CS.ENTITY.166: mTOR (downstream target)
- CS.ENTITY.162: SREBP-1c (lipogenic target)

### Metabolic Effects
- CS.ENTITY.159: HSL (inhibited via insulin)
- CS.ENTITY.161: FAS (induced via insulin)
- CS.ENTITY.160: Lipoprotein lipase (induced)

### Opposing Signals
- CS.ENTITY.165: AMPK (opposes insulin signaling)
- CS.ENTITY.046: Glucagon (counter-regulatory)

## Interpretations

### For Researchers
Insulin receptor is the metabolic control gateway:
- **Signal integration**: Nutritional status sensor
- **Tissue-specific**: Different sensitivity in different tissues
- **Disease relevance**: Central to metabolic disorders

### For Practitioners
Understanding insulin receptor explains:
- Why insulin resistance develops in early lactation
- Importance of body condition management
- Glucose dynamics in transition cows
- Potential for insulin-sensitizing interventions

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Kahn CR. Insulin action, diabetogenes, and the cause of type II diabetes. Diabetes. 1994;43:1066-1084.
3. White MF. IRS proteins and the common path to diabetes. Am J Physiol. 2002;283:E413-E422.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
