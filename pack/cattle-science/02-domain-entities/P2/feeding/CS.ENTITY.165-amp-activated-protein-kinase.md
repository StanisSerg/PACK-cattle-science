---
id: CS.ENTITY.165
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [ampk, energy-sensor, metabolic-regulation, catabolism, atp-regulation]
related:
  - id: CS.ENTITY.164
    type: related
    note: PGC-1α (downstream target)
  - id: CS.ENTITY.159
    type: related
    note: HSL (inhibition)
  - id: CS.ENTITY.161
    type: related
    note: FAS (inhibition)
---

# AMP-activated protein kinase

## Definition

**EN:** AMP-activated protein kinase (AMPK) is a heterotrimeric serine/threonine kinase that functions as a cellular energy sensor, activated by low energy status (high AMP/ATP ratio). It phosphorylates multiple substrates to switch off anabolic pathways (lipogenesis, gluconeogenesis) and switch on catabolic pathways (fatty acid oxidation, glycolysis). It is a master regulator of metabolic homeostasis and a therapeutic target for metabolic diseases.

**RU:** АМФ-активируемая протеинкиназа (АМФК) — гетеротримерная серин/треонинкиназа, функционирующая как клеточный датчик энергии, активируемый при низком энергетическом статусе (высокое соотношение АМФ/АТФ). Фосфорилирует множество субстратов для отключения анаболических путей (липогенез, глюконеогенез) и включения катаболических путей (окисление жирных кислот, гликолиз). Является главным регулятором метаболического гомеостаза и терапевтической мишенью при метаболических заболеваниях.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
AMPK is the master energy sensor that:
- Coordinates metabolic response to energy deficit
- Regulates lipolysis and fatty acid oxidation
- Controls gluconeogenesis and glucose uptake
- Links cellular energy status to whole-body metabolism

## Properties

### Structural Characteristics
| Property | Value |
|----------|-------|
| Structure | Heterotrimer (α, β, γ subunits) |
| Catalytic subunit | α (contains kinase domain) |
| Regulatory subunits | β (scaffold), γ (nucleotide binding) |
| Activation | Phosphorylation (Thr172) + AMP binding |

### Activation Mechanism
```
Low energy status → ATP consumption / AMP production
                            ↓
                    AMP binds γ subunit
                            ↓
            Allosteric activation + Promotion of Thr172 phosphorylation
                            ↓
                        Active AMPK
                            ↓
            Phosphorylation of downstream targets
```

### Key Upstream Kinases
- **LKB1**: Primary AMPK kinase (tumor suppressor)
- **CaMKKβ**: Calcium/calmodulin-dependent activation
- **TAK1**: Alternative activation pathway

## Physiological Role

### Anabolic Pathway Inhibition
| Target | Effect | Metabolic Consequence |
|--------|--------|----------------------|
| ACC1/ACC2 | Inhibition | ↓ Malonyl-CoA → ↑ CPT1 activity |
| HMGCR | Inhibition | ↓ Cholesterol synthesis |
| mTORC1 | Inhibition | ↓ Protein synthesis |
| SREBP-1c | Inhibition | ↓ Lipogenic gene expression |
| GS | Inhibition | ↓ Glycogen synthesis |

### Catabolic Pathway Activation
| Target | Effect | Metabolic Consequence |
|--------|--------|----------------------|
| PGC-1α | Activation | ↑ Mitochondrial biogenesis |
| TBC1D1 | Phosphorylation | ↑ GLUT4 translocation |
| PFK2 | Phosphorylation | ↑ Glycolysis |
| MCD | Activation | ↑ Malonyl-CoA degradation |

### In Dairy Cow Metabolism
- **Negative energy balance**: AMPK activated in liver and muscle
- **Fatty acid oxidation**: Promoted through ACC inhibition
- **Ketogenesis**: Enhanced hepatic ketone production
- **Glucose sparing**: Muscle glucose uptake promoted

## Clinical and Research Significance

### Metabolic Adaptation
```
NEB → Low ATP/High AMP → AMPK activation
                ↓
    ┌───────────┼───────────┐
    ↓           ↓           ↓
Lipolysis   Fatty acid   Glucose uptake
stimulated  oxidation    increased
    └───────────┴───────────┘
                ↓
        Adaptation to energy deficit
```

### Therapeutic Potential
- **Metformin**: Activates AMPK, used in metabolic syndrome
- **Exercise mimetic**: Potential for metabolic health
- **Transition cow support**: Nutritional modulation

## Measurement Methods

### Activity Assay
- **Principle**: Phosphorylation of SAMS peptide substrate
- **Sample**: Tissue homogenates
- **Detection**: Radioactive or fluorescent readout

### Phospho-specific Antibodies
- **pThr172-AMPK**: Active kinase detection (Western blot)
- **Downstream targets**: pACC, pRaptor as activity markers

### Gene Expression
- **qPCR**: AMPK subunit mRNA levels
- **Less informative**: Activity regulated post-translationally

## Related Entities

### Direct Targets
- CS.ENTITY.164: PGC-1α (activated by AMPK)
- CS.ENTITY.159: HSL (lipolysis regulation)
- CS.ENTITY.161: FAS (inhibited by AMPK)

### Metabolic Consequences
- CS.ENTITY.158: CPT1 (activated indirectly via ACC inhibition)
- CS.ENTITY.152: Mitochondria (biogenesis promoted)

### Energy Status
- CS.ENTITY.154: Acetyl-CoA (metabolite)
- CS.ENTITY.155: Pyruvate (glycolysis intermediate)

## Interpretations

### For Researchers
AMPK is the cellular fuel gauge:
- **Energy sensor**: Directly responds to AMP/ATP ratio
- **Master switch**: Coordinates anabolic/catabolic balance
- **Drug target**: Well-validated therapeutic target

### For Practitioners
Understanding AMPK explains:
- How cells sense and respond to energy deficit
- Mechanism of metformin action
- Why exercise improves metabolic health
- Potential nutritional interventions for transition cows

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Hardie DG, et al. The AMP-activated protein kinase—fuel gauge of the mammalian cell? Eur J Biochem. 1998;246:259-273.
3. Hardie DG. AMP-activated protein kinase: a cellular energy sensor with a key role in metabolic disorders. Endocrinology. 2014;155:2201-2209.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
