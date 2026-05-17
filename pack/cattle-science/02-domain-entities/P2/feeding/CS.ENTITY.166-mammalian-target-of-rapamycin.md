---
id: CS.ENTITY.166
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: metabolic-regulation
tags:
- mtor
- mtorc1
- protein-synthesis
- anabolism
- nutrient-sensing
- growth
related:
- id: CS.ENTITY.165
  type: related
  note: AMPK (opposing regulator)
- id: CS.ENTITY.045
  type: related
  note: Insulin (activator)
- id: CS.ENTITY.164
  type: related
  note: PGC-1α (regulated by mTOR)
related_sota:
- CS.SOTA.263
- CS.SOTA.269
- CS.SOTA.270
- CS.SOTA.272
- CS.SOTA.281
- CS.SOTA.319
- CS.SOTA.327
---

# mTOR (Mammalian target of rapamycin)

## Definition

**EN:** Mammalian target of rapamycin (mTOR) is a serine/threonine kinase that functions as a central nutrient and growth factor sensor, regulating cell growth, protein synthesis, and anabolism in response to amino acids, growth factors, and energy status. It exists in two complexes: mTORC1 (nutrient/energy sensing, rapamycin-sensitive) and mTORC2 (cell survival, rapamycin-insensitive). mTORC1 promotes anabolic processes when nutrients are abundant and is inhibited during energy deficit.

**RU:** Млекопитающая мишень рапамицина (mTOR) — серин/треонинкиназа, функционирующая как центральный датчик нутриентов и факторов роста, регулирующий рост клеток, синтез белков и анаболизм в ответ на аминокислоты, факторы роста и энергетический статус. Существует в двух комплексах: mTORC1 (датчик нутриентов/энергии, чувствителен к рапамицину) и mTORC2 (выживание клеток, нечувствителен к рапамицину). mTORC1 стимулирует анаболические процессы при избытке нутриентов и ингибируется при энергетическом дефиците.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
mTOR is the master anabolic regulator that:
- Controls protein synthesis in response to nutrition
- Regulates cell growth and proliferation
- Integrates amino acid, energy, and growth factor signals
- Opposes AMPK during energy surplus

## Properties

### mTOR Complexes
| Complex | Components | Primary Function | Rapamycin Sensitivity |
|---------|------------|------------------|----------------------|
| mTORC1 | mTOR, Raptor, mLST8, PRAS40, DEPTOR | Anabolism, growth | Sensitive |
| mTORC2 | mTOR, Rictor, mSIN1, mLST8, PROTOR | Survival, metabolism | Insensitive |

### Activation Requirements (mTORC1)
```
Amino acids (especially leucine)
            ↓
    Rag GTPases activation
            ↓
    Lysosomal recruitment of mTORC1
            ↓
    Growth factors (insulin/IGF-1)
            ↓
    PI3K → Akt → TSC1/2 inhibition → Rheb-GTP
            ↓
    Full mTORC1 activation
```

### Key Downstream Targets
| Target | Function | Effect of mTORC1 |
|--------|----------|------------------|
| S6K1 | Ribosomal protein S6 kinase | ↑ Protein synthesis |
| 4E-BP1 | Translation initiation | ↑ Translation |
| ULK1 | Autophagy initiation | ↓ Autophagy |
| Lipin-1 | Lipid metabolism | Regulation |
| PGC-1α | Mitochondrial biogenesis | Inhibition |

## Physiological Role

### In Protein Synthesis
- **Translation initiation**: Phosphorylates 4E-BP1, releasing eIF4E
- **Ribosome biogenesis**: Activates S6K1, promotes rRNA synthesis
- **Amino acid sensing**: Direct response to leucine, arginine

### In Growth and Development
- **Cell proliferation**: Promotes cell cycle progression
- **Tissue growth**: Muscle protein accretion
- **Fetal development**: Critical for embryonic growth

### In Metabolic Regulation
- **Lipogenesis**: Coordinates with SREBP-1c
- **Autophagy suppression**: Prevents protein degradation
- **Mitochondrial function**: Regulates PGC-1α

### In Dairy Cows
- **Lactation**: Milk protein synthesis regulation
- **Transition period**: Downregulated during NEB
- **Muscle metabolism**: Protein balance during energy deficit
- **Mammary gland**: Amino acid utilization for milk production

## Clinical and Research Significance

### Nutrient Signaling
```
Fed state → Amino acids ↑ + Insulin ↑ → mTORC1 activation
                                    ↓
                        Protein synthesis ↑ + Growth ↑

Fasting/NEB → Amino acids ↓ + AMPK activation → mTORC1 inhibition
                                            ↓
                                Autophagy ↑ + Catabolism ↑
```

### Research Applications
- **Milk protein**: Regulation of mammary protein synthesis
- **Muscle metabolism**: Protein accretion vs. atrophy
- **Transition nutrition**: Amino acid requirements

## Measurement Methods

### Activity Markers
- **Phospho-S6K1 (Thr389)**: Direct mTORC1 target
- **Phospho-4E-BP1 (Thr37/46)**: Translation initiation
- **Phospho-S6 (Ser235/236)**: Downstream readout

### Western Blot
- **Sample**: Tissue homogenates
- **Antibodies**: Phospho-specific for activity assessment

### Gene Expression
- **Limited utility**: mTOR regulated post-translationally
- **Downstream genes**: S6K1, 4E-BP1 expression

## Related Entities

### Opposing Regulators
- CS.ENTITY.165: AMPK (inhibits mTORC1)
- CS.ENTITY.045: Insulin (activates mTORC1 via Akt)

### Downstream Targets
- CS.ENTITY.164: PGC-1α (inhibited by mTORC1)

### Metabolic Integration
- CS.ENTITY.161: FAS (lipogenesis coordination)
- CS.ENTITY.162: SREBP-1c (coordinated regulation)

## Interpretations

### For Researchers
mTOR is the anabolic master switch:
- **Nutrient integration**: Amino acid, energy, growth factor sensing
- **Growth control**: Cell size and proliferation
- **Therapeutic target**: Rapamycin and analogs

### For Practitioners
Understanding mTOR explains:
- Importance of amino acids for milk production
- Why protein intake matters during transition
- Muscle loss during negative energy balance
- Potential for leucine supplementation

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Laplante M, Sabatini DM. mTOR signaling in growth control and disease. Cell. 2012;149:274-293.
3. Saxton RA, Sabatini DM. mTOR signaling in growth, metabolism, and disease. Cell. 2017;168:960-976.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
