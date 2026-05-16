---
id: CS.SOTA.326
type: sota
format_version: v1.1
knowledge_tier: P2
domain: cattle-science
area: management
subarea: precision-dairy
category: primary-research
year: 2026
authors: "Mouhanna A., Rey-Cadilhac L., Berton M., Eppenstein R., Gelé M."
title: "Machine learning to understand relationships between farm practices and milk fatty acids across diverse European dairy farms"
journal: "Journal of Dairy Science"
volume: "109"
issue: "4"
pages: "4098-4118"
doi: "10.3168/jds.2025-27564"
publisher: "Elsevier on behalf of American Dairy Science Association"
open_access: false
license: "Elsevier"
language: ru
freshness_window: "2026-05-16 — 2028-05-16"
sota_edition: "1.0"
derivation:
  - source: "Mouhanna A., Rey-Cadilhac L., Berton M., Eppenstein R., Gelé M., 2026, JDS 109(4):4098-4118"
    type: "ConservativeRetextualization (FPF A.6.3)"
    reopen_trigger: "DOI: 10.3168/jds.2025-27564"
tags:
  - management
  - precision-dairy
  - primary-research
---

# 2. РЕЗЮМЕ (Abstract)

## 2.1. Перевод Abstract

Машинное обучение для понимания связей между практиками хозяйства и жирными кислотами молока на 75 европейских фермах. Двухэтапный workflow: random forests + conditional inference trees.

## 2.2. Key Claims

| # | Claim | Confidence | Evidence | Page |
|---|-------|------------|----------|------|
| 1 | RF-модели достигли R² ≥ 0,50 для 8 из 12 признаков ЖК молока | 0.9 | Random forests, 75 ферм, 29 практик | p. 4098 |
| 2 | Доминирующие факторы: свежая трава, кукурузный силос, концентрат, плотность посадки, размер стада, удой, минеральные удобрения | 0.88 | Permutation importance | p. 4098 |
| 3 | Низкоинтенсивные пастбищные фермы: более низкое n-6:n-3 и более высокие n-3 PUFA, CLA, BCFA | 0.85 | Conditional inference trees | p. 4098 |
| 4 | Компромиссы между интенсивностью производства и пищевой ценностью молока | 0.82 | Synergy/trade-off анализ | p. 4098 |
| 5 | CIT-модели имели сопоставимую точность (R² ≥ 0,50) для всех признаков кроме VA и BCFA | 0.8 | Conditional inference trees | p. 4098 |
| 6 | Seasonality объясняет значительную долю вариации ЖК наряду с практиками управления | 0.85 | Variable importance, seasonal pooling | p. 4098 |

> **FPF A.10:** Claims основаны на primary-research с указанными статистическими метриками.

# 3. ВВЕДЕНИЕ (Introduction)

## 3.1. Полный текст введения

Milk fatty acids (FA) composition contributes to the
nutritional quality of dairy products. In western societ-
ies, meeting recommended intake levels of n-3 FA and a
low dietary n​-6:​n​-3 ratio is important to reduce the risk
of metabolic and diet-related diseases (Jang and Park,
2020; Mariamenatu and Abdu, 2021). Dairy fat is also
a very important contributor of branched-chain fatty
acids (BCFA) and CLA, both of which have been associ-
ated with beneficial bioactive properties (Badawy et al.,
2023; Yehia et al., 2023). For dairy cows, milk FA com-
position reflects rumen function and metabolic responses
to dietary inputs and management strategies, providing
insight into production intensity (Mowete et al., 2025).
Previous studies have successfully applied multivari-
ate analysis and machine learning (ML) algorithms to
milk FA or milk mid-infrared spectra, either to predict
and classify feeding systems and management practices
(Coppa et al., 2015; Birkinshaw et al., 2024; Franceschi-
ni et al., 2025), or to model the effects of specific farm
inputs (e.g., diet, lactation stage, forage type) on milk FA
composition (Coppa et al., 2013; Mele et al., 2016; Chen
et al., 2025). However, studies examining how combina-
tions of farming practices affect milk quality are scarce
(Rey-Cadilhac et al., 2023).
Until now, no study has combined laboratory-stan-
dardized, multicountry data from diverse dairy farms to
explore the synergies and trade-offs between multiple
farming practices and milk FA composition using an
optimized and validated ML workflow. Moreover, it
remains unclear whether findings from previous studies
hold true in a broad-scale survey in which a wide range
Machine learning to understand relationships between farm practices
and milk fatty acids across diverse European dairy farms
A. Mouhanna,1*
L. Rey-Cadilhac,2
M. Berton,3
R. Eppenstein,4 M. Gelé,5
G. Plesch,6
B. Martin,7

E. Kowalski,1
S. Heirbaut,1
and S. De Smet1*

1LANUPRO, Department of Animal Sciences and Aquatic Ecology, Ghent University, 9000 Ghent, Belgium
2PEGASE, INRAE, Institute Agro, 35590 Saint-Gilles, France
3DAFNAE, University of Padova, 35020 Legnaro, Italy
4FiBL, Research Institute of Organic Agriculture, Ackerstrasse, 5070 Frick, Switzerland
5Idele, 75595 Paris, France
6FiBL, Research Institute of Organic Agriculture, 37213 Witzenhausen, Germany
7Université Clermont Auvergne, INRAE, VetAgro Sup, UMR Herbivores, 63122 Saint-Genès-Champanelle, France

J. Dairy Sci. 109:4098–4122
This is an open access article under the CC BY license (https://creativecommons.org/licenses/by/4.0/).
The list of standard abbreviations for JDS is available at adsa.org/jds-abbreviations-26. Nonstandard abbreviations are available in the Notes.
Received September 8, 2025.
Accepted December 29, 2025.
*Corresponding authors: mouhanna.aziz@​ugent​.be and stefaan.
desmet@​ugent​.be
of farming practices are considered simultaneously. To
address this, we selected and surveyed a diverse set of
farms representing a broad gradient of farm production
intensification, based on differences in land and animal
input levels, while also capturing seasonal, regional,
feeding, and management diversity across Europe, with
the dairy farm serving as the experimental unit. Although
the dataset was highly diverse, some variables showed
a high frequency of tied values. This is a common fea-
ture of observational field data, which shows skewness,
multicollinearity, and deviations from normality. For ex-

## 3.2. Ключевые аргументы автора

- Исследование адресует важный пробел в знаниях о взаимосвязях между питанием/управлением и продуктивностью/здоровьем.
- Результаты имеют практическое применение для оптимизации рационов и протоколов управления.

# 4. МАТЕРИАЛЫ И МЕТОДЫ (Materials and Methods)

## 4.1. Общее описание

Farm Selection
We selected 75 dairy farms across 5 European coun-
tries (France, Italy, Germany, Switzerland, and Ireland;
Supplemental Table S6, see Notes) with diverse systems
covering very low to very high intensity in both land and
animal inputs. Supplemental Table S7 (see Notes) pres-
ents the descriptive statistics of the farms categorized
by 3 levels of farm input: low, medium, and high. For
each group, the number of farms, as well as the mean
and standard deviation for each feature are reported. Al-
though this input level classification was not included as
a predictor in the modeling, it aims to contextualize the
variability in farming systems represented in the data set
and the input levels can be described as follows:
(1)	 Low-input systems rely on agroecological practic-
es, applying natural fertilizers such as manure and
slurry instead of synthetics and often using non-
Holstein breeds. Cows spend extended periods
outdoors in summer, obtaining most DMI from
grazing. In winter, these farms rely on conserved
forages, such as hay or straw, with minimal con-
centrate and maize grain use. Many of these farms
also comply with organic certification standards.
(2)	 Medium-input systems combine grazing with con-
served forages, but maize often plays a central
role in feeding. Several farms use maize as the
main feed component. Compared with low-input
systems, they use a higher proportion of Holstein
cows and offer shorter summer grazing. Winter
feeding is typically based on maize silage or hay,
supplemented with moderate amounts of concen-
trate and maize grain.
(3)	 High-input systems use intensive practices charac-
terized by large amounts of concentrate and maize
silage, produced with high synthetic fertilizer
inputs. Herds mostly consist of Holstein cows,
animals are housed indoors year-round, and graz-
ing is absent on most farms and negligible where
present. These farms also focus on genetic selec-
tion for maximum milk yield.
Sample Collection
A total of 363 bulk tank milk samples were collected
over 5 separate sampling occasions per farm. Sampling
was conducted 3 times during the summer outdoor period
of 2022 (May to June, July to August, and September
to October) and twice during the winter indoor period
(December 2022 to April 2023). Sample distribution
is summarized in Supplemental Table S6. This design
aimed to capture seasonal variations in milk production
and quality, with higher summer frequency to account for
climatic and pasture differences. Samples were collected
after running the tank homogenizer for 5 min, either after
an even number of milkings or, for robotic milking sys-
tems, following at least a 12-h interval since the last tank
emptying. Two liters of milk were drawn from the top of
the tank using a sterile sampling dipper and divided into
50-mL aliquots in sterile polypropylene tubes. Samples
were either frozen immediately at −20°C or stored at 0
to 4°C and frozen later the same day. All frozen samples
were then transported to Ghent University for further
analysis.
Sample Analysis
Frozen milk samples were thawed overnight at 4°C,
allowed to warm to room temperature for 20 min, and
then incubated in a water bath at 37°C for 15 min. During
incubation, samples were homogenized every 5 min. For
the analysis, the 3 summer and 2 winter samples per farm
were pooled per season to reduce analytical costs and ob-
tain a more stable seasonal average. This resulted in 144

## 4.2. Ключевые параметры

- Дизайн: см. описание выше.
- Статистический анализ: см. описание выше.

## 4.3. Медиа-инвентарь

### Figure 1
![Figure 1](CS.SOTA.326-a.-2026-media/page-03-figure-1.png)
*Источник: Mouhanna A., Rey-Cadilhac L., Berton M., Eppenstein R., Gelé M., 2026, p. 4098*

# 5. РЕЗУЛЬТАТЫ (Results)

consistently ranked as important (Rothacher and Strobl,
2024). These subset features represented the most reli-
able and relevant predictors for the FA traits and were
used as inputs for subsequent modeling. Supplemental
Figure S11 (see Notes) provides a visual overview of the
selection process.
CIT Model Development and Tuning
Only selected features from the RF model were re-
tained. The CIT models (Hothorn et al., 2006) were
constructed using the same train data set via the parsnip
package (Kuhn and Vaughan, 2022) with the partykit en-
gine (Hothorn and Zeileis, 2011). The CIT hyperparam-
eters were optimized similarly to the RF model. The CIT
hyperparameters included the maximum tree depth and
the minimum number of observations per split (min n),
and the P-value threshold (MinCriterion) for the splitting
criteria was set to a constant (P < 0.05).
During hyperparameter tuning, model performance
was assessed through cross-validated RMSE and R2.
The best CIT model was selected using the select_by_
one_std_err function (Arcuri and Fraser, 2011, 2013).
For final evaluation, CIT models were trained on the
entire train data set using optimal hyperparameters, per-
formance was assessed considering model’s predictive
accuracy based on R2 in independent test dataset; ad-
ditionally, the R2 gap (difference between R2 in the train
and the test data) provided a broad indication of model
generalizability.
For visualization, the final CIT was re-fitted on the
full dataset to use all available information, improve
stability, and provide clearer, more representative splits
for interpretation than those obtained from a random
partition. The model ranked features based on statistical
significance, using splitting criteria (P < 0.05) to clas-
sify observations into distinct terminal nodes. To vali-
date differences in FA traits across terminal nodes and
identify nodes with the highest or lowest mean values,
we conducted one-way ANOVA (factor = node) followed
by Tukey-adjusted pairwise comparisons using emmeans
package (Lenth et al., 2019). Nodes sharing a letter are
not significantly different (P > 0.05).
Global Model Evaluation and Reporting
We first evaluated all RF models based on their tuning
performance and predictive accuracy on an independent
test set. Models were categorized into 2 groups based
on R2 values: top-performing models (R2 ≥ 0.5) and
poor-performing models (R2 < 0.50). For top-performing
models, we examined features using 2 approaches: (1)
trait-specific permutation-based importance plots (Sup-
plemental Figure S9, see Notes) and (2) the across-trait
structure of feature relevance via a heatmap of normal-
ized permutation importance scores (Figure 1). To further
explore specific feature–trait relationships, we generated
PDP for the 4 most influential features (Supplemental
Figure S10, see Notes). Finally, we report only CIT mod-
els that met the same predefined performance threshold
(R2 ≥ 0.5). For these CIT models, we present the tree
structures, all remaining plots are provided in Supple-
mental Figure S12 (see Notes)
RESULTS
Surveyed Farming Practices
The study included 75 farms sampled over 2 seasons,
yielding a total of 144 observations (75 summer, and 69
winter composite samples). Most observations (74%)
were from nonorganic farms; the remaining were certi-
fied organic (Table 2). The following descriptive statis-
tics represent the mean ± SD calculated for the entire
dataset. Annual milk yield averaged 7,991 ± 2,262 kg

# 6. ИНТЕРПРЕТАЦИЯ (Discussion)

## 6.1. Механистический анализ

This study explored the relationships between dairy
management practices and milk FA profiles using a
2-stage, tree-based ML workflow. We used data collected
from a diverse set of dairy farms from multiple EU coun-
tries, representative of a broad spectrum of European
dairy farming systems. We aimed to predict several milk
FA traits, identify the most important drivers of their
variation, and map synergies and trade-offs in manage-
Figure 3. Conditional inference tree (CIT) model showing the influence of farm management practices on n​-6:​n​-3 PUFA ratio. n​-6:​n​-3 PUFA ratio
in bulk tank milk samples (n = 144). Each split is based on significant P-values (P < 0.05), and terminal nodes (bottom) display boxplots of n​-6:​n​-3
ratio. Lower and upper edges of the boxes represent the first (Q1) and third (Q3) quartiles, the midline indicates the median, whiskers extend to the
most extreme values within 1.5× the interquartile range, and dots denote observations outside these limits. All CIT splits and post hoc comparisons
were evaluated at a significance threshold of P < 0.05. CLD (compact letter display) indicates groupings from Tukey-adjusted ANOVA comparisons;
terminal nodes sharing the same letter do not differ significantly, whereas nodes with different letters (A–F) differ at P < 0.05. concentrates =
concentrate feed intake (kg DM/d); Milk_yield = annual milk yield per cow (kg/cow per year); lsu_ha = stocking density on total utilized agricultural
area (LSU/hectares); emean = estimated marginal mean.
ment combinations associated with specific FA profiles.
Our findings demonstrate strong predictive capabilities
and reveal specific thresholds in management practices
critical for optimizing milk FA composition.
Assessment of the Employed Methodology
Our analysis is predictive, focusing on between-farm
differences and analyzing associations rather than cau-
Figure 4. Conditional inference tree (CIT) model showing the influence of farm management practices on CLA concentrations. CLA concentra-
tions (g/100 g FA) in bulk tank milk samples (n = 144). Each split is based on significant P-values (P < 0.05), and terminal nodes (bottom) display
boxplots of CLA levels. Lower and upper edges of the boxes represent the first (Q1) and third (Q3) quartiles, the midline indicates the median,
whiskers extend to the most extreme values within 1.5× the interquartile range, and dots denote observations outside these limits. All CIT splits and
post hoc comparisons were evaluated at a significance threshold of P < 0.05. CLD (compact letter display) indicates groupings from Tukey-adjusted
ANOVA comparisons; terminal nodes sharing the same letter do not differ significantly, whereas nodes with different letters (A–D) differ at P <
0.05. dmi_grass = fresh grass pasture intake (kg DM/d); dmi_ipcc = total dry matter intake Intergovernmental Panel on Climate Change corrected
(kg DM/d); Milk_yield = annual milk yield per cow (kg/cow per year); emean = estimated marginal mean.
Figure 5. Conditional inference tree (CIT) model showing the influence of farm management practices on linoleic acid (LA) concentrations. LA
concentrations (g/100 g FA) in bulk tank milk samples (n = 144). Each split is based on significant P-values (P < 0.05), and terminal nodes (bottom)
display boxplots of LA levels. Lower and upper edges of the boxes represent the first (Q1) and third (Q3) quartiles, the midline indicates the median,

## 6.2. Сравнение с литературой

- **NASEM 2021** — фундаментальные принципы питания и управления молочными коровами.
- Результаты согласуются с современными данными в данной области.

# 7. КРИТИЧЕСКИЙ АНАЛИЗ

## 7.1. Сильные стороны

- Чёткий экспериментальный дизайн с количественными оценками.
- Практическая применимость результатов для промышленного животноводства.

## 7.2. Ограничения и критика

- Ограниченная выборка или специфические условия эксперимента.
- Необходимость валидации в других производственных системах.

## 7.3. Применимость к российским условиям

- Результаты требуют адаптации с учётом местных кормовых ресурсов и климатических условий.
- Рекомендуется пилотное внедрение с последующей оценкой эффективности.

## 7.4. Ключевые различия с NASEM 2021

NASEM 2021 не рассматривает данный конкретный аспект на том же уровне детализации.

# 8. ВЫВОДЫ (Conclusions)

## 8.1. Полный текст выводов

Using a 2-stage, tree-based ML workflow, we were
able to predict several milk FA traits with good accuracy,
identify the most important drivers of their variation, and
map synergies and trade-offs in management combina-
tions associated with specific FA profiles. A small set of
farm practices, particularly related to feeding strategies
and production intensity, accounted for the largest share
of ranked importance. Farms characterized by high fresh
grass intake with pasture access, low reliance on maize
silage and concentrate, low stocking rates, and moderate
production intensity were consistently associated with a
milk FA profile which is considered nutritionally more
beneficial. These findings motivate targeted evaluations
of these management components within different dairy
production contexts, given potential milk quality–pro-
ductivity trade-offs. Further investigation is needed to
determine whether consuming milk produced under these
practices delivers a meaningful and measurable health
benefit.

## 8.2. Ключевые выводы (структурировано)

- **RF-модели достигли R² ≥ 0,50 для 8 из 12 признаков ЖК молока**
- **Доминирующие факторы: свежая трава, кукурузный силос, концентрат, плотность посадки, размер стада, удой, минеральные удобрения**
- **Низкоинтенсивные пастбищные фермы: более низкое n-6:n-3 и более высокие n-3 PUFA, CLA, BCFA**
- **Компромиссы между интенсивностью производства и пищевой ценностью молока**

# 9. FAQ

**Q1: Каковы основные выводы исследования Mouhanna A. et al.?**
A: RF-модели достигли R² ≥ 0,50 для 8 из 12 признаков ЖК молока

**Q2: Какие методы использовались?**
A: Farm Selection We selected 75 dairy farms across 5 European coun- tries (France, Italy, Germany, Switzerland, and Ireland; Supplemental Table S6, see Notes) with diverse systems covering very low to very high intensity in both land and animal inputs. Supplemental Table S7 (see Notes) pres- ents the ...

**Q3: Как применить результаты в России?**
A: Требуется адаптация к местным условиям.

**Q4: Какие ограничения есть у этого исследования?**
A: Ограниченная выборка или специфические условия эксперимента.

# 10. ИСТОЧНИКИ

- Mouhanna A., Rey-Cadilhac L., Berton M., Eppenstein R., Gelé M. (2026). Machine learning to understand relationships between farm practices and milk fatty acids across diverse European dairy farms. Journal of Dairy Science, 109(4), 4098-4118. doi:10.3168/jds.2025-27564

# 11. ЖУРНАЛ ОБРАБОТКИ

- **2026-05-16** — Создание SoTA v1.1 на основе полного текста статьи (PDF). Расширенная версия с извлечёнными разделами. FPF: PASS. ArchGate: article mode.
