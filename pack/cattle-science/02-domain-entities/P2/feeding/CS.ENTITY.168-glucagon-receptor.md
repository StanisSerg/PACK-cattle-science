---
id: CS.ENTITY.168
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: metabolic-regulation
tags:
- glucagon-receptor
- gpcr
- gluconeogenesis
- glycogenolysis
- catabolism
related:
- id: CS.ENTITY.046
  type: related
  note: Glucagon (ligand)
- id: CS.ENTITY.167
  type: related
  note: Insulin receptor (opposing pathway)
- id: CS.ENTITY.165
  type: related
  note: AMPK (convergent catabolic signaling)
related_sota:
- CS.SOTA.336
- CS.SOTA.338
- CS.SOTA.339
---

# Glucagon receptor

## Definition

**EN:** The glucagon receptor (GCGR) is a class B G-protein coupled receptor (GPCR) that mediates the catabolic effects of glucagon, primarily in the liver. Upon glucagon binding, it activates adenylyl cyclase via Gs protein, increasing cAMP and activating PKA, which promotes glycogenolysis, gluconeogenesis, and ketogenesis while inhibiting glycogen synthesis and lipogenesis. It is essential for maintaining glucose homeostasis during fasting and metabolic stress.

**RU:** Рецептор глюкагона (GCGR) — G-белок-сопряжённый рецептор класса B, медиирующий катаболические эффекты глюкагона, преимущественно в печени. При связывании глюкагона активирует аденилатциклазу через Gs-белок, увеличивая cAMP и активируя ПКА, что стимулирует гликогенолиз, глюконеогенез и кетогенез при одновременном ингибировании синтеза гликогена и липогенеза. Необходим для поддержания глюкозного гомеостаза при голодании и метаболическом стрессе.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
Glucagon receptor is essential for:
- Counter-regulatory response to hypoglycemia
- Hepatic glucose production during fasting
- Ketogenesis during negative energy balance
- Opposition to insulin action

## Properties

### Structural Characteristics
| Feature | Description |
|---------|-------------|
| Family | Class B GPCR (secretin receptor family) |
| Gene | GCGR |
| Structure | 7-transmembrane domain receptor |
| Coupling | Primarily Gs (stimulatory) |
| Second messenger | cAMP |

### Signaling Cascade
```
Glucagon binding → Receptor conformational change
                        ↓
                Gs protein activation
                        ↓
                Adenylyl cyclase stimulation
                        ↓
                cAMP production ↑
                        ↓
                PKA activation
                        ↓
        Phosphorylation of metabolic enzymes
```

### PKA Targets in Liver
| Target | Phosphorylation Effect | Metabolic Outcome |
|--------|------------------------|-------------------|
| Glycogen phosphorylase kinase | Activation | Glycogenolysis ↑ |
| Glycogen synthase | Inhibition | Glycogen synthesis ↓ |
| PFK-2/FBPase-2 | Inhibition | Gluconeogenesis ↑ |
| Hormone-sensitive lipase | Activation | Lipolysis ↑ (adipose) |
| CREB | Activation | Gene transcription |

## Physiological Role

### In Hepatic Glucose Production
- **Glycogenolysis**: Rapid glucose release (minutes)
- **Gluconeogenesis**: Sustained glucose synthesis (hours)
- **Substrates**: Lactate, amino acids, glycerol

### In Lipid Metabolism
- **Lipolysis**: HSL activation in adipose tissue
- **Ketogenesis**: Acetyl-CoA diversion to ketone bodies
- **Fatty acid oxidation**: Promotes hepatic β-oxidation

### In Protein Metabolism
- **Amino acid uptake**: Enhanced for gluconeogenesis
- **Ureagenesis**: Increased nitrogen excretion

### In Dairy Cows
- **Negative energy balance**: Elevated glucagon supports metabolism
- **Transition period**: Critical for glucose homeostasis
- **Ketogenesis**: Drives hepatic ketone production
- **Gluconeogenic demand**: Supports high lactose synthesis

## Clinical and Research Significance

### Glucagon-Insulin Ratio
```
Fed state: Insulin ↑↑, Glucagon ↓ → Anabolism
Fasting/NEB: Insulin ↓, Glucagon ↑↑ → Catabolism

Glucagon/Insulin ratio determines:
- Hepatic glucose output
- Ketogenic capacity
- Lipolytic rate
```

### Research Applications
- **Glucagon challenge tests**: Assess glycogen stores
- **Receptor antagonists**: Potential therapeutic targets
- **Transition studies**: Glucagon dynamics around calving

## Measurement Methods

### Receptor Binding
- **Principle**: Radiolabeled glucagon binding
- **Sample**: Liver membrane preparations
- **Challenge**: High non-specific binding

### Functional Assays
- **cAMP production**: Cell-based assays
- **Glycogenolysis**: Isolated hepatocytes
- **Gluconeogenesis**: Substrate conversion assays

### Gene Expression
- **qPCR**: GCGR mRNA levels
- **Tissue distribution**: Primarily liver

## Related Entities

### Ligand and Signaling
- CS.ENTITY.046: Glucagon (ligand)
- CS.ENTITY.167: Insulin receptor (opposing pathway)
- CS.ENTITY.165: AMPK (convergent catabolic effects)

### Metabolic Effects
- CS.ENTITY.159: HSL (activated via cAMP)
- CS.ENTITY.050: β-hydroxybutyrate (ketogenesis product)
- CS.ENTITY.155: Pyruvate (gluconeogenic substrate)

### Hormonal Network
- CS.ENTITY.045: Insulin (counter-regulatory hormone)
- CS.ENTITY.047: Cortisol (synergistic catabolic)

## Interpretations

### For Researchers
Glucagon receptor mediates the fasting/starvation response:
- **Counter-regulatory**: Opposes insulin action
- **Metabolic flexibility**: Switches fuel sources
- **Stress adaptation**: Critical for survival during energy deficit

### For Practitioners
Understanding glucagon receptor explains:
- How liver produces glucose during fasting
- Mechanism of ketogenesis in early lactation
- Why hypoglycemia triggers stress responses
- Hormonal basis of metabolic adaptation

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Jiang G, Zhang BB. Glucagon and regulation of glucose metabolism. Annu Rev Physiol. 2003;65:207-227.
3. Drucker DJ. The glucagon-like peptides. Diabetes. 1998;47:159-169.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
