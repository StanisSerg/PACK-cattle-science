---
id: CS.ENTITY.162
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [srebp, transcription-factor, lipogenesis, cholesterol, insulin-signaling]
related:
  - id: CS.ENTITY.161
    type: related
    note: Fatty acid synthase (target gene)
  - id: CS.ENTITY.045
    type: related
    note: Insulin (activator)
  - id: CS.ENTITY.068
    type: related
    note: Phosphatidylcholines (membrane lipids)
---

# Sterol regulatory element-binding protein

## Definition

**EN:** Sterol regulatory element-binding proteins (SREBPs) are a family of transcription factors (SREBP-1a, SREBP-1c, SREBP-2) that regulate genes involved in lipid synthesis and uptake. SREBP-1c is the master regulator of insulin-stimulated lipogenesis, activating genes for fatty acid synthesis, while SREBP-2 primarily controls cholesterol metabolism. They are activated by low cellular sterol levels through a unique proteolytic cleavage mechanism in the ER-Golgi pathway.

**RU:** Белки, связывающие стеролрегуляторные элементы (SREBP) — семейство транскрипционных факторов (SREBP-1a, SREBP-1c, SREBP-2), регулирующих гены, вовлечённые в синтез и захват липидов. SREBP-1c является главным регулятором инсулин-стимулированного липогенеза, активируя гены синтеза жирных кислот, в то время как SREBP-2 в основном контролирует метаболизм холестерина. Они активируются при низком содержании клеточных стеролов через уникальный механизм протеолитического расщепления в пути ЭПР-Гольджи.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
SREBPs are master regulators of:
- Insulin-mediated lipogenic gene expression
- Coordination of lipid synthesis pathways
- Adaptation to nutritional status
- Integration of glucose and lipid metabolism

## Properties

### Family Members
| Isoform | Primary Function | Target Genes |
|---------|------------------|--------------|
| SREBP-1a | Potent activator | Lipogenic + cholesterogenic |
| SREBP-1c | Lipogenesis | FAS, ACC, SCD1, GPAT, LPL |
| SREBP-2 | Cholesterol synthesis | HMGCR, LDLR, SQLE |

### Structural Features
- **bHLH domain**: DNA binding and dimerization
- **Transmembrane domains**: ER anchoring (inactive form)
- **Regulatory domain**: Interaction with SREBP cleavage-activating protein (SCAP)

### Activation Mechanism
```
Low sterols → SCAP conformational change
                    ↓
            COPII vesicle transport to Golgi
                    ↓
            Sequential cleavage by S1P and S2P proteases
                    ↓
            Release of N-terminal bHLH domain
                    ↓
            Nuclear translocation → Gene activation
```

## Physiological Role

### In Lipogenesis
- **SREBP-1c activation**: Insulin → PI3K → Akt → SREBP-1c expression
- **Target genes**: 
  - ACLY (ATP-citrate lyase)
  - ACACA (acetyl-CoA carboxylase)
  - FASN (fatty acid synthase)
  - SCD (stearoyl-CoA desaturase)
  - GPAM (glycerol-3-phosphate acyltransferase)

### In Ruminant Metabolism
- **Acetate adaptation**: SREBP-1c responsive to acetate availability
- **Transition period**: Downregulation during negative energy balance
- **Adipose tissue**: Primary site of SREBP-1c-mediated lipogenesis

### Cross-talk with Other Pathways
- **LXR**: Liver X receptor activates SREBP-1c transcription
- **mTORC1**: Nutrient sensing and SREBP activation
- **AMPK**: Energy stress inhibits SREBP processing

## Clinical and Research Significance

### Metabolic Adaptation
| Physiological State | SREBP-1c Activity | Lipogenic Gene Expression |
|---------------------|-------------------|---------------------------|
| Fed/high insulin | High | High |
| Fasting/low insulin | Low | Low |
| NEB (early lactation) | Very low | Very low |
| Refeeding | Rapidly induced | Rapidly increased |

### Research Applications
- **Gene expression studies**: SREBP-1c mRNA as lipogenic index
- **Nutrigenomics**: Dietary effects on SREBP signaling
- **Metabolic disorders**: Dysregulation in fatty liver/ketosis

## Measurement Methods

### Gene Expression
- **qPCR**: SREBP-1c, SREBP-2 mRNA levels
- **Nuclear extracts**: Mature (active) SREBP protein
- **Target genes**: FASN, ACC as downstream markers

### Activity Assays
- **Reporter constructs**: SRE-luciferase assays
- **ChIP**: Chromatin immunoprecipitation of target promoters
- **Electrophoretic mobility shift**: DNA binding activity

## Related Entities

### Target Genes
- CS.ENTITY.161: Fatty acid synthase (FASN)
- CS.ENTITY.157: Citrate synthase (indirectly via metabolism)

### Regulatory Network
- CS.ENTITY.045: Insulin (primary activator of SREBP-1c)
- CS.ENTITY.068: Phosphatidylcholines (membrane component regulated by SREBP)

### Metabolic Integration
- CS.ENTITY.154: Acetyl-CoA (substrate for SREBP-driven synthesis)
- CS.ENTITY.067: Triglycerides (end product)

## Interpretations

### For Researchers
SREBPs are master transcriptional regulators of lipid metabolism:
- **Insulin sensitivity indicator**: SREBP-1c reflects tissue insulin responsiveness
- **Nutritional integration**: Coordinates multiple biosynthetic pathways
- **Therapeutic potential**: Target for metabolic disease intervention

### For Practitioners
Understanding SREBP explains:
- How insulin drives fat synthesis
- Why lipogenesis shuts down during energy deficit
- Mechanism of body condition recovery after calving
- Potential for nutritional modulation of gene expression

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Horton JD, et al. SREBPs: activators of the complete program of cholesterol and fatty acid synthesis. J Clin Invest. 2002;109:1125-1131.
3. Shimano H. SREBPs: physiology and pathophysiology of the SREBP family. FEBS J. 2009;276:616-621.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
