---
id: CS.ENTITY.157
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [citrate-synthase, enzyme, tca-cycle, mitochondria, metabolic-regulation]
related:
  - id: CS.ENTITY.154
    type: related
    note: Acetyl-CoA (substrate)
  - id: CS.ENTITY.152
    type: related
    note: Mitochondria (location)
  - id: CS.ENTITY.155
    type: related
    note: Pyruvate (precursor)
  - id: CS.ENTITY.156
    type: related
    note: Lactate dehydrogenase (competing pathway)
---

# Citrate synthase

## Definition

**EN:** Citrate synthase (CS, EC 2.3.3.1) is a mitochondrial enzyme that catalyzes the first and rate-limiting step of the tricarboxylic acid (TCA) cycle, condensing acetyl-CoA with oxaloacetate to form citrate. It serves as a key regulatory point and marker of mitochondrial density and oxidative capacity in tissues.

**RU:** Цитратсинтаза (ЦС, EC 2.3.3.1) — митохондриальный фермент, катализирующий первую и лимитирующую стадию цикла трикарбоновых кислот (ЦТК), конденсацию ацетил-КоА с оксалоацетатом с образованием цитрата. Является ключевым регуляторным пунктом и маркером плотности митохондрий и окислительной способности тканей.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
Citrate synthase is discussed as:
- Marker of mitochondrial biogenesis and oxidative capacity
- Indicator of tissue metabolic adaptation during NEB
- Enzyme linking carbohydrate and lipid metabolism
- Target for understanding metabolic flexibility

## Properties

### Enzymatic Characteristics
| Property | Value |
|----------|-------|
| EC Number | 2.3.3.1 |
| Molecular weight | ~48-52 kDa (dimer) |
| Location | Mitochondrial matrix |
| Cofactors | None required |
| pH optimum | 7.8-8.2 |

### Reaction
```
Acetyl-CoA + Oxaloacetate + H₂O → Citrate + CoA-SH
```

### Regulation
- **Allosteric inhibitors**: ATP, NADH, succinyl-CoA
- **Substrate availability**: Acetyl-CoA and oxaloacetate concentrations
- **Post-translational**: Acetylation, phosphorylation
- **Transcriptional**: PGC-1α mediated upregulation during metabolic stress

## Physiological Role

### In Liver Metabolism
- **TCA cycle entry**: First committed step
- **Citrate export**: Precursor for cytosolic fatty acid synthesis
- **Metabolic signal**: High citrate inhibits glycolysis (allosteric regulation of PFK-1)

### In Adipose Tissue
- **Lipogenesis support**: Provides citrate for acetyl-CoA generation
- **Metabolic flexibility indicator**: Activity reflects oxidative vs. lipogenic capacity

### In Muscle
- **Oxidative capacity marker**: CS activity correlates with mitochondrial density
- **Exercise adaptation**: Upregulated with endurance training

## Clinical and Research Significance

### As Biomarker
| Application | Interpretation |
|-------------|----------------|
| Mitochondrial density | Activity proportional to mitochondrial content |
| Metabolic adaptation | Changes reflect tissue metabolic remodeling |
| NEB monitoring | Liver CS activity may indicate metabolic flexibility |

### Metabolic Disorders
- **Ketosis**: Altered CS activity reflects hepatic metabolic adaptation
- **Fatty liver**: Relationship between CS and lipid accumulation
- **Mitochondrial dysfunction**: Reduced activity in metabolic stress

## Measurement Methods

### Spectrophotometric Assay
- **Principle**: DTNB (Ellman's reagent) detects free CoA-SH
- **Sample**: Tissue homogenates
- **Unit**: μmol/min/mg protein

### Immunohistochemistry
- **Application**: Localization within tissues
- **Advantage**: Visual assessment of mitochondrial distribution

## Related Entities

### Metabolic Pathways
- CS.ENTITY.152: Mitochondria (location)
- CS.ENTITY.154: Acetyl-CoA (substrate)
- CS.ENTITY.155: Pyruvate → acetyl-CoA precursor
- CS.ENTITY.156: Lactate dehydrogenase (competing NADH utilization)

### Regulatory Networks
- CS.ENTITY.068: Phosphatidylcholines (membrane component)
- CS.ENTITY.069: Sphingomyelins (membrane component)

## Interpretations

### For Researchers
Citrate synthase serves as a reliable marker of mitochondrial oxidative capacity. In dairy cow metabolism studies, changes in CS activity can indicate:
- Tissue adaptation to negative energy balance
- Metabolic flexibility of different tissues
- Response to nutritional interventions

### For Practitioners
While not routinely measured in clinical practice, understanding CS function helps explain:
- Why liver metabolism changes during transition period
- Relationship between mitochondrial health and metabolic disorders
- Importance of supporting oxidative metabolism in fresh cows

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Srere PA. Citrate synthase. Methods Enzymol. 1969;13:3-11.
3. Gibala MJ, et al. Short-term sprint interval versus traditional endurance training. J Physiol. 2006;575:901-911.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
