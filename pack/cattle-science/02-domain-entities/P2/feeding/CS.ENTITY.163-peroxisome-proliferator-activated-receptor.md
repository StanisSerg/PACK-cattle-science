---
id: CS.ENTITY.163
type: entity
priority: P2
domain: cattle-science
area: feeding
subarea: lipid-metabolism
tags:
- ppar
- transcription-factor
- fatty-acid-oxidation
- adipogenesis
- metabolic-regulation
related:
- id: CS.ENTITY.158
  type: related
  note: CPT1 (target gene)
- id: CS.ENTITY.159
  type: related
  note: HSL (lipolysis regulator)
- id: CS.ENTITY.152
  type: related
  note: Mitochondria (PPARα targets)
related_sota:
- CS.SOTA.257
- CS.SOTA.282
---

# Peroxisome proliferator-activated receptor

## Definition

**EN:** Peroxisome proliferator-activated receptors (PPARs) are a family of nuclear hormone receptors (PPARα, PPARδ/β, PPARγ) that function as ligand-activated transcription factors regulating genes involved in lipid metabolism, energy homeostasis, and inflammation. PPARα activates fatty acid oxidation genes in liver and muscle; PPARγ promotes adipogenesis and lipid storage; PPARδ/β regulates oxidative metabolism broadly. They are activated by fatty acids and their derivatives.

**RU:** Рецепторы, пролиферирующие пероксисомы (PPAR) — семейство ядерных рецепторов гормонов (PPARα, PPARδ/β, PPARγ), функционирующих как лиганд-активируемые транскрипционные факторы, регулирующие гены, вовлечённые в метаболизм липидов, энергетический гомеостаз и воспаление. PPARα активирует гены окисления жирных кислот в печени и мышцах; PPARγ стимулирует адипогенез и липидное депо; PPARδ/β регулирует окислительный метаболизм широко. Активируются жирными кислотами и их производными.

## SoTA Context

### Source
- **McFadden et al., 2017** (CS.SOTA.039) — comprehensive review of lipid metabolism in dairy cows

### Relevance
PPARs are master regulators of:
- Fatty acid oxidation capacity (PPARα)
- Adipose tissue development and function (PPARγ)
- Metabolic adaptation to energy status
- Inflammatory responses in metabolic tissues

## Properties

### Family Members
| Isoform | Primary Tissue | Main Function | Ligands |
|---------|----------------|---------------|---------|
| PPARα | Liver, muscle, heart | Fatty acid oxidation | Fatty acids, fibrates |
| PPARδ/β | Ubiquitous | Oxidative metabolism | Fatty acids |
| PPARγ | Adipose, macrophages | Adipogenesis, storage | Fatty acids, thiazolidinediones |

### Structural Features
- **DNA-binding domain (DBD)**: Zinc finger structure for DNA recognition
- **Ligand-binding domain (LBD)**: Binds fatty acids and drugs
- **AF-2 domain**: Transactivation function

### Mechanism of Action
```
Fatty acid ligand → Binding to PPAR LBD
                        ↓
            Conformational change + RXR heterodimerization
                        ↓
            Binding to PPAR response elements (PPREs)
                        ↓
            Recruitment of coactivators (SRC-1, PGC-1α)
                        ↓
            Transcriptional activation of target genes
```

## Physiological Role

### PPARα in Liver
**Target genes for fatty acid oxidation:**
- CPT1A, CPT2 (mitochondrial transport)
- ACOX1 (peroxisomal oxidation)
- HMGCS2 (ketogenesis)
- FABP1 (fatty acid binding)

**Role in NEB:**
- Upregulated during fasting/negative energy balance
- Promotes hepatic fatty acid oxidation
- Supports ketogenesis for extrahepatic fuel

### PPARγ in Adipose Tissue
**Functions:**
- Adipocyte differentiation (adipogenesis)
- Lipid storage and glucose uptake
- Adipokine production (adiponectin)
- Insulin sensitization

**In dairy cows:**
- Critical for adipose tissue development
- Regulated by energy status
- Target for understanding body condition dynamics

### PPARδ/β
- **Broad expression**: All metabolically active tissues
- **Function**: Enhances oxidative capacity
- **Potential**: Exercise mimetic effects

## Clinical and Research Significance

### Metabolic Adaptation
| Condition | PPARα | PPARγ | Net Effect |
|-----------|-------|-------|------------|
| Fasting/NEB | ↑↑ Up | ↓ Down | Oxidation favored |
| Refeeding | ↓ Down | ↑↑ Up | Storage favored |
| Exercise | ↑ Up | Neutral | Enhanced oxidation |

### Research Applications
- **Gene expression**: PPAR target genes as metabolic indices
- **Nutritional studies**: Effects of fatty acid supplements
- **Transition cow physiology**: PPAR dynamics around calving

## Measurement Methods

### Gene Expression
- **qPCR**: PPARα, PPARγ, PPARδ mRNA
- **Target genes**: CPT1, ACOX, CD36 as activity markers

### Protein Analysis
- **Western blot**: PPAR protein levels
- **Nuclear extracts**: Active receptor fraction

### Functional Assays
- **Reporter gene assays**: PPRE-driven transcription
- **ChIP-seq**: Genome-wide binding sites

## Related Entities

### Target Genes
- CS.ENTITY.158: CPT1 (PPARα target)
- CS.ENTITY.159: HSL (regulated in adipose)
- CS.ENTITY.152: Mitochondria (PPARα enhances biogenesis)

### Ligands/Activators
- CS.ENTITY.065: NEFA (endogenous ligands)
- CS.ENTITY.067: Triglycerides (source of ligands)

### Co-regulators
- CS.ENTITY.164: PGC-1α (major PPAR coactivator)

## Interpretations

### For Researchers
PPARs are nutrient sensors that coordinate metabolic adaptation:
- **Fatty acid receptors**: Respond to lipid-derived signals
- **Tissue-specific**: Different isoforms in different tissues
- **Integration**: Link nutritional status to gene expression

### For Practitioners
Understanding PPARs explains:
- How tissues adapt to changing energy availability
- Why fatty acids can regulate their own metabolism
- Potential for dietary modulation of gene expression
- Mechanisms of metabolic flexibility

## References

1. McFadden JW, et al. (2017) — See CS.SOTA.039
2. Evans RM, et al. PPARs and the complex journey to obesity. Nat Med. 2004;10:355-361.
3. Lemberger T, et al. Peroxisome proliferator-activated receptors. Annu Rev Cell Dev Biol. 1996;12:335-363.

---

*Last updated: 2026-03-28*
*Entity type: P2 (SoTA-specific from McFadden 2017)*
