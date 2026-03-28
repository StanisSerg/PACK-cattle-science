---
id: CS.ENTITY.161
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [fas, fatty-acid-synthase, de-novo-lipogenesis, lipogenesis, adipose-tissue]
related:
  - id: CS.ENTITY.067
    type: related
    note: Triglycerides (end product)
  - id: CS.ENTITY.154
    type: related
    note: Acetyl-CoA (substrate)
  - id: CS.ENTITY.157
    type: related
    note: Citrate synthase (citrate shuttle)
---

# Fatty acid synthase

## Definition

**EN:** Fatty acid synthase (FAS, EC 2.3.1.85) is a multifunctional homodimeric enzyme complex that catalyzes the NADPH-dependent synthesis of palmitate (C16:0) from acetyl-CoA, malonyl-CoA, and NADPH through a series of condensation, reduction, and dehydration reactions. It is the primary enzyme of de novo lipogenesis and is highly regulated by nutritional and hormonal signals, particularly insulin.

**RU:** Синтаза жирных кислот (СЖК, EC 2.3.1.85) — многофункциональный гомодимерный ферментативный комплекс, катализирующий синтез пальмитата (C16:0) из ацетил-КоА, малонил-КоА и НАДФН через серию реакций конденсации, восстановления и дегидратации. Является основным ферментом de novo липогенеза и высоко регулируется нутритивными и гормональными сигналами, особенно инсулином.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
FAS is critical for:
- De novo fatty acid synthesis in adipose tissue
- Conversion of dietary carbohydrates to fat
- Insulin-sensitive lipogenic pathway
- Energy storage during positive energy balance

## Properties

### Enzymatic Characteristics
| Property | Value |
|----------|-------|
| EC Number | 2.3.1.85 |
| Gene | FASN |
| Molecular weight | ~270 kDa (monomer), homodimer active |
| Location | Cytosol |
| Products | Palmitate (C16:0) primarily |

### Multi-Enzyme Complex
FAS contains all activities required for fatty acid synthesis:
1. **Acetyltransferase (AT)** — loads acetyl-CoA
2. **Malonyltransferase (MT)** — loads malonyl-CoA
3. **Condensing enzyme (β-ketoacyl synthase, KS)**
4. **β-ketoacyl reductase (KR)** — uses NADPH
5. **β-hydroxyacyl dehydratase (DH)**
6. **Enoyl reductase (ER)** — uses NADPH
7. **β-hydroxyacyl thioesterase (TE)** — releases product

### Reaction Stoichiometry
```
Acetyl-CoA + 7 Malonyl-CoA + 14 NADPH + 14 H⁺ + 7 ATP
    → Palmitate + 7 CO₂ + 14 NADP⁺ + 8 CoA-SH + 7 ADP + 7 Pi
```

## Regulation

### Transcriptional Control
| Factor | Effect | Mechanism |
|--------|--------|-----------|
| Insulin | ↑↑↑ Upregulation | SREBP-1c activation |
| Glucose | ↑ Upregulation | ChREBP-mediated |
| Citrate | ↑ Upregulation | Allosteric + substrate |
| Palmitate | ↓ Feedback inhibition | Product inhibition |
| Palmitoyl-CoA | ↓ Feedback inhibition | Product inhibition |

### Post-translational
- **Phosphorylation**: AMPK-mediated inhibition during energy stress
- **Polymerization**: Active form is homodimer

## Physiological Role

### In Adipose Tissue
- **Primary site**: Major locus of de novo lipogenesis in ruminants
- **Ruminant limitation**: Less active than in monogastrics due to VFA absorption
- **Acetate utilization**: Converts acetate (from rumen) to fatty acids

### In Liver
- **Low activity**: Minimal de novo lipogenesis in bovine liver
- **Export function**: Any synthesis contributes to VLDL triglycerides

### In Mammary Gland
- **Lactation role**: Synthesis of medium-chain fatty acids (C4-C14)
- **Substrate**: Acetate and β-hydroxybutyrate
- **Regulation**: Upregulated during lactation

## Clinical and Research Significance

### Body Condition Score
```
Positive energy balance → Insulin ↑ → FAS activity ↑ → Fat deposition ↑
Negative energy balance → Insulin ↓ → FAS activity ↓ → Lipolysis dominates
```

### Research Applications
- **Adipose tissue biopsies**: FAS mRNA as lipogenic index
- **Nutritional studies**: Effects of energy source on lipogenesis
- **Genetic selection**: FASN gene polymorphisms and fat deposition

## Measurement Methods

### Activity Assay
- **Principle**: NADPH oxidation (A340) in coupled assay
- **Substrates**: Acetyl-CoA, malonyl-CoA, NADPH
- **Sample**: Tissue cytosolic fraction

### Gene Expression
- **qPCR**: FASN mRNA quantification
- **Tissue-specific**: Adipose vs. mammary expression

### Indirect Assessment
- **De novo fatty acids**: Fatty acid composition analysis
- **Isotope tracing**: ¹³C-acetate incorporation

## Related Entities

### Pathway Components
- CS.ENTITY.154: Acetyl-CoA (primer substrate)
- CS.ENTITY.067: Triglycerides (storage form)
- CS.ENTITY.157: Citrate synthase (citrate shuttle)

### Regulatory Factors
- CS.ENTITY.045: Insulin (major activator)
- CS.ENTITY.065: NEFA (feedback signal)

### Downstream Enzymes
- CS.ENTITY.160: Lipoprotein lipase (fatty acid uptake)
- CS.ENTITY.159: Hormone-sensitive lipase (opposing pathway)

## Interpretations

### For Researchers
FAS represents the committed step of de novo lipogenesis:
- **Highly regulated**: Integration of nutritional and hormonal signals
- **Ruminant adaptation**: Functions with acetate as primary substrate
- **Tissue-specific**: Adipose-dominant in cattle

### For Practitioners
Understanding FAS explains:
- Why body condition increases during late lactation/dry period
- Relationship between dietary energy and fat deposition
- Limitations of carbohydrate-driven fat synthesis in ruminants
- Importance of acetate as energy source

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Smith S, et al. Structural and functional organization of the animal fatty acid synthase. Prog Lipid Res. 2003;42:289-317.
3. Bernard L, et al. Lipid metabolism in ruminant adipose tissue. INRA Prod Anim. 2008;21:301-308.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
