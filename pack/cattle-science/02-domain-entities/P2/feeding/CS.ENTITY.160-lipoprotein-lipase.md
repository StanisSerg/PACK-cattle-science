---
id: CS.ENTITY.160
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [lpl, lipoprotein-lipase, triglyceride-hydrolysis, chylomicron, vldl]
related:
  - id: CS.ENTITY.065
    type: related
    note: NEFA (product of LPL action)
  - id: CS.ENTITY.067
    type: related
    note: Triglycerides (substrate)
  - id: CS.ENTITY.152
    type: related
    note: Tissue fatty acid uptake
---

# Lipoprotein lipase

## Definition

**EN:** Lipoprotein lipase (LPL, EC 3.1.1.34) is an extracellular enzyme anchored to the luminal surface of capillary endothelial cells that hydrolyzes triglycerides in circulating lipoproteins (chylomicrons and VLDL) to release free fatty acids for uptake by adjacent tissues. It is the primary determinant of tissue-specific fatty acid uptake and plays a critical role in lipid partitioning between milk synthesis, adipose storage, and muscle oxidation.

**RU:** Липопротеинлипаза (ЛПЛ, EC 3.1.1.34) — экстраклеточный фермент, закреплённый на просветной поверхности эндотелиальных клеток капилляров, гидролизующий триглицериды в циркулирующих липопротеинах (хиломикронах и ЛПОНП) с высвобождением свободных жирных кислот для захвата прилегающими тканями. Является основным определяющим фактором тканеспецифического захвата жирных кислот и играет критическую роль в распределении липидов между синтезом молока, жировым депо и окислением в мышцах.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
LPL is essential for:
- Tissue-specific fatty acid partitioning
- Milk fat synthesis (mammary LPL)
- Adipose tissue lipid storage
- Muscle fatty acid oxidation
- VLDL clearance from circulation

## Properties

### Enzymatic Characteristics
| Property | Value |
|----------|-------|
| EC Number | 3.1.1.34 |
| Gene | LPL |
| Molecular weight | ~55 kDa (homodimer) |
| Location | Capillary endothelium (luminal surface) |
| Cofactor | ApoC-II (essential activator) |
| pH optimum | 8.0-8.5 |

### Synthesis and Transport
```
Adipocyte/Muscle/Mammary cell → Synthesize LPL
                    ↓
            Secretion to extracellular space
                    ↓
            Binding to heparan sulfate proteoglycans
                    ↓
            Translocation to capillary lumen
```

### Reaction
```
Triglyceride (in lipoprotein) + H₂O → Diglyceride + NEFA
                    ↓
         Diglyceride + H₂O → Monoglyceride + NEFA
                    ↓
         Monoglyceride + H₂O → Glycerol + NEFA
```

## Tissue-Specific Expression and Function

### Mammary Gland
| Aspect | Characteristics |
|--------|-----------------|
| Expression | Very high during lactation |
| Function | Supply fatty acids for milk triglycerides |
| Regulation | Upregulated by prolactin, insulin |
| Importance | Critical for milk fat production |

### Adipose Tissue
| Aspect | Characteristics |
|--------|-----------------|
| Expression | High in fed state, suppressed in lactation |
| Function | Storage of dietary fatty acids |
| Regulation | Insulin-stimulated, fasting-inhibited |
| Adaptation | Downregulated during NEB |

### Skeletal Muscle
| Aspect | Characteristics |
|--------|-----------------|
| Expression | Moderate, exercise-inducible |
| Function | Fatty acid oxidation for energy |
| Regulation | Upregulated by training, fasting |
| Isoform | Similar to other tissues |

## Physiological Role

### In Lactating Dairy Cows
- **Milk fat synthesis**: Mammary LPL provides ~50% of milk fatty acids
- **Adipose sparing**: Downregulation prevents storage competition
- **VLDL clearance**: Hepatic lipid export processing

### Regulation by Physiological State
| State | Adipose LPL | Mammary LPL | Net Effect |
|-------|-------------|-------------|------------|
| Dry period | High | Low | Storage favored |
| Early lactation | Low | Very high | Milk synthesis favored |
| Late lactation | Increasing | Decreasing | Gradual shift |

## Clinical and Research Significance

### Milk Production
- **LPL activity**: Correlates with milk fat content
- **Nutritional effects**: Dietary fat supplementation responses
- **Genetic variation**: LPL polymorphisms and milk composition

### Metabolic Disorders
- **Fatty liver**: Impaired VLDL export → substrate limitation for LPL
- **Ketosis**: Altered LPL activity in different tissues
- **Negative energy balance**: Tissue-specific LPL adaptation

## Measurement Methods

### Activity Assay
- **Principle**: Hydrolysis of radiolabeled triolein in emulsion
- **Sample**: Tissue homogenates (heparin-releasable)
- **Unit**: mU/g tissue or mU/mg protein

### Gene Expression
- **qPCR**: LPL mRNA in different tissues
- **Tissue comparison**: Relative expression levels

### Plasma Markers
- **Post-heparin LPL**: Systemic LPL activity
- **Triglyceride clearance**: Functional assessment

## Related Entities

### Substrates and Products
- CS.ENTITY.067: Triglycerides (substrate)
- CS.ENTITY.065: NEFA (product)
- CS.ENTITY.066: Glycerol (product)

### Lipoproteins
- CS.ENTITY.070: Chylomicrons (substrate)
- CS.ENTITY.069: VLDL (substrate)

### Tissue Uptake
- CS.ENTITY.152: Mitochondria (oxidation)
- CS.ENTITY.158: CPT (mitochondrial entry)

## Interpretations

### For Researchers
LPL is the gatekeeper of tissue fatty acid uptake:
- **Tissue-specific**: Different regulation in mammary vs. adipose
- **Physiological adaptation**: Dramatic changes around parturition
- **Nutritional responses**: Modifiable by diet composition

### For Practitioners
Understanding LPL explains:
- Why milk fat responds to dietary fat supplements
- Competition between body condition and milk production
- Importance of transition period nutrition
- Individual variation in milk composition

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Cryer A. Tissue lipoprotein lipase activity and its action in lipoprotein metabolism. Int J Biochem. 1981;13:525-541.
3. Nielsen MO, et al. Lactation-dependent changes in tissue lipoprotein lipase activity in dairy cows. J Dairy Sci. 2003;86:3287-3296.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
