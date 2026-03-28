---
id: CS.ENTITY.158
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [cpt, carnitine-palmitoyltransferase, beta-oxidation, fatty-acid-transport, mitochondria]
related:
  - id: CS.ENTITY.152
    type: related
    note: Mitochondria (target organelle)
  - id: CS.ENTITY.154
    type: related
    note: Acetyl-CoA (end product)
  - id: CS.ENTITY.157
    type: related
    note: Citrate synthase (TCA cycle)
---

# Carnitine palmitoyltransferase

## Definition

**EN:** Carnitine palmitoyltransferase (CPT) is a mitochondrial enzyme system comprising CPT1 (outer mitochondrial membrane) and CPT2 (inner mitochondrial membrane) that catalyzes the rate-limiting transport of long-chain fatty acids into mitochondria for β-oxidation. CPT1 converts fatty acyl-CoA to fatty acylcarnitine, which is then translocated and converted back by CPT2.

**RU:** Карнитинпальмитоилтрансфераза (КПТ) — митохондриальная ферментативная система, включающая КПТ1 (внешняя мембрана) и КПТ2 (внутренняя мембрана), катализирующая лимитирующий транспорт длинноцепочечных жирных кислот в митохондрии для β-окисления. КПТ1 превращает жироацил-КоА в жироацилкарнитин, который затем транслоцируется и обратно превращается КПТ2.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
CPT system is critical for:
- Regulation of fatty acid oxidation rates
- Metabolic adaptation during negative energy balance
- Hepatic lipid metabolism and ketogenesis
- Muscle energy substrate selection

## Properties

### CPT1 (Regulatory Isoform)
| Property | Value |
|----------|-------|
| Location | Outer mitochondrial membrane |
| Isoforms | CPT1A (liver), CPT1B (muscle), CPT1C (brain) |
| Inhibitor | Malonyl-CoA (potent, physiological) |
| Km for carnitine | 0.5-1.0 mM |

### CPT2 (Catalytic Isoform)
| Property | Value |
|----------|-------|
| Location | Inner mitochondrial membrane (matrix side) |
| Function | Regenerates fatty acyl-CoA from acylcarnitine |
| Cofactors | CoA-SH |

### Reaction Sequence
```
Fatty acyl-CoA + Carnitine →[CPT1]→ Fatty acylcarnitine + CoA-SH
                    ↓ (carnitine-acylcarnitine translocase)
Fatty acylcarnitine + CoA-SH →[CPT2]→ Fatty acyl-CoA + Carnitine
```

## Physiological Role

### In Liver During NEB
- **Fatty acid oxidation**: Primary pathway for energy production
- **Ketogenesis**: Supplies acetyl-CoA for ketone body synthesis
- **Malonyl-CoA regulation**: Insulin/glucagon control via ACC products

### In Skeletal Muscle
- **Exercise fuel**: Enables fatty acid oxidation during prolonged activity
- **Metabolic flexibility**: Switches between glucose and fatty acid utilization
- **CPT1B isoform**: Muscle-specific regulation

### In Adipose Tissue
- **Limited expression**: Low CPT activity in bovine adipose
- **Lipogenic focus**: Preferentially uses glucose for fatty acid synthesis

## Clinical and Research Significance

### Malonyl-CoA Regulation
| Condition | Malonyl-CoA | CPT1 Activity | Outcome |
|-----------|-------------|---------------|---------|
| Fed state | High | Inhibited | Lipogenesis favored |
| Fasting | Low | Active | β-oxidation favored |
| NEB (early) | Low | Highly active | Rapid fat mobilization |

### Research Applications
- **Metabolic flexibility assessment**: CPT1 activity as indicator
- **Nutritional interventions**: Effects of fatty acid supplements
- **Transition cow studies**: Adaptation to lactation demands

## Measurement Methods

### Enzymatic Assay
- **Principle**: Radiolabeled palmitoyl-CoA conversion
- **Sample**: Tissue mitochondria or homogenates
- **Sensitivity**: Requires specialized equipment

### Gene Expression
- **qPCR**: CPT1A, CPT1B, CPT2 mRNA levels
- **Tissue-specific**: Different isoforms in liver vs. muscle

### Metabolite Proxies
- **Plasma acylcarnitines**: Indirect marker of CPT activity
- **β-hydroxybutyrate**: End product of CPT-dependent oxidation

## Related Entities

### Enzyme Systems
- CS.ENTITY.152: Mitochondria (location)
- CS.ENTITY.157: Citrate synthase (TCA cycle partner)
- CS.ENTITY.156: Lactate dehydrogenase (alternative pathway)

### Metabolic Products
- CS.ENTITY.154: Acetyl-CoA (oxidation product)
- CS.ENTITY.050: β-hydroxybutyrate (ketogenesis product)

### Regulatory Molecules
- CS.ENTITY.068: Phosphatidylcholines (membrane lipids)

## Interpretations

### For Researchers
CPT system represents a critical regulatory node in lipid metabolism:
- **Rate-limiting step**: Controls overall β-oxidation flux
- **Insulin sensitivity indicator**: Malonyl-CoA sensitivity reflects metabolic health
- **Therapeutic target**: Potential for metabolic disease intervention

### For Practitioners
Understanding CPT function explains:
- Why fatty acid oxidation increases dramatically in early lactation
- Relationship between energy balance and ketone production
- Importance of gradual transition to high-energy diets

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. McGarry JD, Brown NF. The mitochondrial carnitine palmitoyltransferase system. Eur J Biochem. 1997;244:1-14.
3. Essen-Gustavsson B, et al. Carnitine in skeletal muscle and blood plasma in dairy cows. J Dairy Sci. 1988;71:2462-2466.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
