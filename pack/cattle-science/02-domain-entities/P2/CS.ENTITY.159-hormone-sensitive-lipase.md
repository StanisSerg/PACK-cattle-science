---
id: CS.ENTITY.159
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags: [hsl, hormone-sensitive-lipase, lipolysis, adipose-tissue, fat-mobilization]
related:
  - id: CS.ENTITY.065
    type: related
    note: Non-esterified fatty acids (NEFA) - product
  - id: CS.ENTITY.066
    type: related
    note: Glycerol (product)
  - id: CS.ENTITY.152
    type: related
    note: Mitochondria (fatty acid oxidation)
---

# Hormone-sensitive lipase

## Definition

**EN:** Hormone-sensitive lipase (HSL, EC 3.1.1.79) is the rate-limiting enzyme of lipolysis in adipose tissue, catalyzing the hydrolysis of triglycerides to diglycerides and subsequently to monoglycerides and free fatty acids. It is the primary regulatory point for hormone-controlled fat mobilization, activated by catecholamines via cAMP/PKA pathway and inhibited by insulin.

**RU:** Гормон-чувствительная липаза (ГЧЛ, EC 3.1.1.79) — лимитирующий фермент липолиза в жировой ткани, катализирующий гидролиз триглицеридов до диглицеридов и затем до моноглицеридов и свободных жирных кислот. Является основным регуляторным пунктом гормон-контролируемой мобилизации жира, активируется катехоламинами через путь cAMP/ПКА и ингибируется инсулином.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
HSL is central to:
- Adipose tissue lipolysis regulation
- NEFA mobilization during negative energy balance
- Hormonal control of energy homeostasis
- Metabolic adaptation in transition dairy cows

## Properties

### Enzymatic Characteristics
| Property | Value |
|----------|-------|
| EC Number | 3.1.1.79 |
| Gene | LIPE |
| Molecular weight | ~84 kDa |
| Location | Adipocyte lipid droplet surface |
| pH optimum | 7.0-7.4 |

### Substrate Specificity
1. **Primary**: Triglycerides → Diglycerides + NEFA
2. **Secondary**: Diglycerides → Monoglycerides + NEFA
3. **Minor**: Cholesteryl esters, retinyl esters

### Regulation Mechanism
```
Catecholamines → β-adrenergic receptor → Gs protein
                                    ↓
                              Adenylyl cyclase activation
                                    ↓
                              cAMP ↑ → PKA activation
                                    ↓
                         HSL phosphorylation (Ser563, Ser659, Ser660)
                                    ↓
                         Translocation to lipid droplet + Activation
```

## Physiological Role

### In Adipose Tissue
- **Lipolysis control**: Rate-limiting step of fat mobilization
- **Basal lipolysis**: Maintains minimal NEFA release
- **Stimulated lipolysis**: Dramatic increase during fasting/NEB

### Hormonal Regulation
| Hormone | Mechanism | Effect on HSL |
|---------|-----------|---------------|
| Epinephrine | cAMP/PKA | Activation |
| Norepinephrine | cAMP/PKA | Activation |
| Insulin | PDE3B/cAMP↓ | Inhibition |
| Glucocorticoids | GR-mediated | Permissive for catecholamines |

### In Dairy Cows
- **Transition period**: Dramatic activation due to negative energy balance
- **Ketosis risk**: Excessive HSL activity → high NEFA → ketogenesis
- **Adipose adaptation**: Downregulation with chronic stimulation

## Clinical and Research Significance

### NEFA Mobilization
```
HSL Activity → NEFA Release → Hepatic Uptake →
    ├─→ β-oxidation → Energy (beneficial)
    ├─→ Re-esterification → VLDL (neutral)
    └─→ Ketogenesis → Ketosis (pathological if excessive)
```

### Research Applications
- **Adipose tissue biopsies**: HSL activity/mRNA as lipolytic index
- **Plasma NEFA**: Indirect marker of HSL activity
- **Pharmacological targets**: Beta-agonist effects on lipolysis

## Measurement Methods

### Activity Assay
- **Principle**: Hydrolysis of radiolabeled triglyceride substrate
- **Sample**: Adipose tissue homogenates
- **Unit**: nmol/min/mg protein

### Gene Expression
- **qPCR**: HSL (LIPE) mRNA quantification
- **Regulatory assessment**: Phosphorylation state (Western blot)

### Indirect Markers
- **Plasma NEFA**: Systemic lipolytic rate
- **Glycerol**: More specific lipolysis marker (not reutilized)

## Related Entities

### Lipolysis Cascade
- CS.ENTITY.065: Non-esterified fatty acids (NEFA) - product
- CS.ENTITY.066: Glycerol - product
- CS.ENTITY.067: Triglycerides (triacylglycerols) - substrate

### Metabolic Fate
- CS.ENTITY.152: Mitochondria (fatty acid oxidation)
- CS.ENTITY.050: β-hydroxybutyrate (ketogenesis product)
- CS.ENTITY.158: CPT (fatty acid transport)

### Regulatory Hormones
- CS.ENTITY.045: Insulin (inhibitor)
- CS.ENTITY.046: Glucagon (indirect activator)

## Interpretations

### For Researchers
HSL represents the critical control point for adipose tissue lipolysis:
- **Rate-limiting**: Determines overall fat mobilization rate
- **Hormonal integration**: Receives multiple endocrine signals
- **Adaptive changes**: Chronic stimulation alters expression and sensitivity

### For Practitioners
Understanding HSL explains:
- Why NEFA increases dramatically after calving
- Role of stress (catecholamines) in metabolic disorders
- Why insulin therapy can suppress excessive lipolysis
- Importance of body condition management

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Holm C, et al. Hormone-sensitive lipase. Ann NY Acad Sci. 2000;892:178-187.
3. Duncan RE, et al. Regulation of lipolysis in adipocytes. Annu Rev Nutr. 2007;27:79-101.
4. Drackley JK. ADSA Foundation Scholar Award. J Dairy Sci. 1999;82:2259-2273.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
