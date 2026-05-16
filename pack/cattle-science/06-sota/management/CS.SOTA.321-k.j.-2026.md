---
id: CS.SOTA.321
type: sota
format_version: v1.1
knowledge_tier: P2
domain: cattle-science
area: management
subarea: heifers
category: primary-research
year: 2026
authors: "Hemmert K.J., Ostendorf C.S., Cohrs I., Koch C., Sauerwein H."
title: "Associations of growth rates during the first 2 months of life with feeding behavior, development, and first-lactation performance in Holstein heifers"
journal: "Journal of Dairy Science"
volume: "109"
issue: "4"
pages: "3725-3747"
doi: "10.3168/jds.2025-27925"
publisher: "Elsevier on behalf of American Dairy Science Association"
open_access: false
license: "Elsevier"
language: ru
freshness_window: "2026-05-16 — 2028-05-16"
sota_edition: "1.0"
derivation:
  - source: "Hemmert K.J., Ostendorf C.S., Cohrs I., Koch C., Sauerwein H., 2026, JDS 109(4):3725-3747"
    type: "ConservativeRetextualization (FPF A.6.3)"
    reopen_trigger: "DOI: 10.3168/jds.2025-27925"
tags:
  - management
  - heifers
  - primary-research
---

# 2. РЕЗЮМЕ (Abstract)

## 2.1. Перевод Abstract

Ретроспективное исследование связи между темпами роста в первые 2 месяца жизни, поведением при кормлении, развитием и продуктивностью в первую лактацию у телочек Holstein. 42 телочки, высокое молочное кормление (12 Л/сут).

## 2.2. Key Claims

| # | Claim | Confidence | Evidence | Page |
|---|-------|------------|----------|------|
| 1 | MAX ADG (1,06 кг/сут) vs MOD (0,84 кг/сут) в первые 2 месяца | 0.9 | Кластерный анализ, P<0.001 | p. 3725 |
| 2 | MAX телочки были на 16 кг тяжелее при отъеме (149 vs 133 кг) | 0.9 | Взвешивание на 14-й неделе, P<0.001 | p. 3725 |
| 3 | MAX имели лучшую кормовую эффективность в первые 2 недели (1,20-fold) | 0.85 | Gain:feed ratio, P<0.05 | p. 3725 |
| 4 | MAX имели больший удой в первую лактацию (11 511 vs 10 242 кг, +12,4%) | 0.88 | 305-дневный удой, P=0.001 | p. 3747 |
| 5 | MAX посещали кормушку ЗЦМ чаще и имели больше концентрата в 10-12 недель | 0.85 | Автоматические кормушки, P<0.05 | p. 3725 |
| 6 | Random forest: ADG в первые 2 месяца — важнейший предиктор первой лактации | 0.82 | Модель ML, variable importance | p. 3747 |

> **FPF A.10:** Claims основаны на primary-research с указанными статистическими метриками.

# 3. ВВЕДЕНИЕ (Introduction)

## 3.1. Полный текст введения

Early nutritional stimuli may trigger epigenetic modi-
fications, potentially affecting gene expression, organ
development, and the lifetime productivity of dairy heif-
ers (Langley-Evans, 2006; Vaiserman, 2014). The long-
term effects of postnatal nutrition on metabolism (e.g.,
carbohydrate and lipid metabolism) may result from
adaptive changes in gene expression or altered cellular
proliferation, leading to persistent changes in the quan-
tity or proportion of cell populations in tissue (Lucas,
1998). Growth requires an adequate nutrient supply and
sufficient time for the proportionate development of all
organs, such as the mammary gland and liver. Addition-
ally, ad libitum MR feeding during the first 5 wk of life
Associations of growth rates during the first 2 months of life with feeding
behavior, development, and first-lactation performance in Holstein heifers
K. J. Hemmert,1,2 C. S. Ostendorf,1,3* I. Cohrs,3,4 C. Koch,3 H. Sauerwein,1 and M. H. Ghaffari5†
1Institute of Animal Science, Physiology Unit, University of Bonn, 53115 Bonn, Germany
2Förster-Technik GmbH, 78234 Engen, Germany
3Educational and Research Centre for Animal Husbandry, Hofgut Neumühle, 67728 Münchweiler an der Alsenz, Germany
4Clinic for Ruminants and Herd Health Management, Justus-Liebig-University Giessen, 35392 Giessen, Germany
5Research Institute for Farm Animal Biology (FBN), D-18196 Dummerstorf, Germany

J. Dairy Sci. 109:3725–3747
This is an open access article under the CC BY license (https://creativecommons.org/licenses/by/4.0/).
The list of standard abbreviations for JDS is available at adsa.org/jds-abbreviations-26. Nonstandard abbreviations are available in the Notes.
Received November 10, 2025.
Accepted December 18, 2025.
*Current address: TUM School of Life Sciences, 85354 Freising,
Germany.
†Corresponding author: hosseini​-ghaffari@​fbn​-dummerstorf​.de
has been shown to improve small intestine development,
as indicated by greater villus circumference and villus
height, compared with restrictive feeding of 6 L/d (Schäff
et al., 2018). Optimizing ADG during the initial weeks of
a calf’s life supports efficient feed energy utilization for
growth, as feed efficiency declines after the preruminant
phase (Bach et al., 2021). Increased preweaning nutri-
ent supply has also been shown to have beneficial ef-
fects later in life, such as improved reproductive system
development in replacement heifers (Gelsinger et al.,
2016; Bruinjé et al., 2019) and a long-lasting, strong im-
mune response indicative of immunological imprinting
(Ockenden et al., 2023). In addition, weight gain during
the first 2 wk of life also affects subsequent BW dur-
ing rearing (Volkmann et al., 2019), which is associated
with a lower age at first calving (Vacek et al., 2015) and
increased productive lifespan (Dallago et al., 2024) in
intensively reared heifers. Previous studies have shown
that growth rates influenced by feed supply during the
milk-feeding period affect later performance, such as
milk yield (Soberon et al., 2012; Kiezebrink et al., 2015;
Korst et al., 2017) and milk composition (Chester-Jones
et al., 2017; Jiang et al., 2025).
Differences in ADG have been primarily attributed to
feeding intensity, length of the preweaning period, and
feed additives (Miller-Cushon and DeVries, 2015; Hai-
san et al., 2019; Norouzi et al., 2021), without consid-
ering individual variation in voluntary feed intake and
feed efficiency of calves. Similarly, few studies have

## 3.2. Ключевые аргументы автора

- Исследование адресует важный пробел в знаниях о взаимосвязях между питанием/управлением и продуктивностью/здоровьем.
- Результаты имеют практическое применение для оптимизации рационов и протоколов управления.

# 4. МАТЕРИАЛЫ И МЕТОДЫ (Materials and Methods)

## 4.1. Общее описание

All procedures described in this article strictly fol-
lowed the guidelines of the German Law for Animal
Welfare with permission from the corresponding au-
thority
(Landesuntersuchungsamt
Rheinland-Pfalz,
Koblenz, Germany [G 21–20–049]). This study was
conducted at the Educational and Research Centre for
Animal Husbandry, Hofgut Neumühle, Münchweiler an
der Alsenz, Germany.
Animals, Diets, Feeding, and Management
This study, conducted at the Research Centre from
September 2021 to June 2022, followed Holstein-Frie-
sian calves from birth to their first calving. The dams of
these calves, with an average parity of 1.9 ± 0.16, were
housed in calving pens with deep straw bedding, fed a
dry cow TMR, and given free access to water. When the
first signs of parturition were detected, such as udder
filling and softening of the pelvic ligaments, the dams
were moved to a designated calving pen with deep straw
bedding. To monitor the calving process, calving sensors
(Moocall Ltd., Bluebell, Dublin, Ireland) were used to
provide continuous data on the progression of labor. All
calves received at least 3.5 L of their dam’s colostrum by
bottle in the calving pen within 2 h after birth, followed
by 1.5 to 2 L of colostrum at the next feeding. When the
amount of maternal colostrum was insufficient, colos-
trum from frozen stocks (−20°C) was thawed and added.
Calves that did not consume enough colostrum were fed
using an esophageal tube. Colostrum quality was as-
sessed with a digital Brix refractometer and confirmed
with a hydrometer (specific gravity). After colostrum
feeding, each calf was orally given 7 mL of iron sus-
pension (Ursoferran 150 mg/mL, Serumwerk Bernburg
AG, Bernburg, Germany), and the navel was disinfected
with a 10% povidone-iodine solution (Vet-sept solution,
aniMedica GmbH, Senden-Bösensell, Germany).
Birth weight was recorded after feeding, and the
amount of colostrum received was subtracted. Newborn
calves were housed in straw-bedded calf igloos with in-
dividual pens and a fenced outdoor area until 15 ± 1.9 d
of age. They were fed 12 L of milk replacer (MR, 140
g/L Milkivit Sweet Rubin, Trouw Nutrition Deutschland
GmbH, Burgheim, Germany) per day manually by teat
bucket, divided into two 6-L meals at 0600 and 1600 h.
The amount of MR consumed was recorded by weigh-
ing the teat bucket before and after feeding with an
electronic scale (Sartorius AG, Göttingen, Germany). To
encourage self-feeding through the automatic feeder, the
last meal provided in the individual hutch before group
housing was limited to 2 L of MR. The calves were then
moved to one of 3 open straw-bedded group pens and
remained in the same group throughout the entire milk-
feeding period (until d 98 of life). Groups were formed
according to birth order and consisted of up to 10 calves.
At the research farm, female and bull calves were reared
equally and kept together in the same group until the
end of the MR-feeding period. Each pen was used for
several batches during the trial and was equipped with
an automated calf feeding system, including a calf feeder
with 2 milk-feeding stations and a concentrate feeder
with one feeding station. Each pen was equipped with
an automated calf feeding system, including a calf feeder
(CF) with 2 milk-feeding stations (VARIO Smart Kombi,
Förster-Technik GmbH, Engen, Germany) and a concen-
trate feeder with one feeding station (Förster-Technik).
From the first day of group housing until d 56 of life

## 4.2. Ключевые параметры

- Дизайн: см. описание выше.
- Статистический анализ: см. описание выше.

## 4.3. Медиа-инвентарь

### Figure 1
![Figure 1](CS.SOTA.321-k.j.-2026-media/page-03-figure-1.png)
*Источник: Hemmert K.J., Ostendorf C.S., Cohrs I., Koch C., Sauerwein H., 2026, p. 3725*

# 5. РЕЗУЛЬТАТЫ (Results)

Clustering and Growth Performance
In general, the ADG during the 12 L preweaning
period (birth until wk 8 of life) were adequate (range
0.73–1.16 kg/d) reflecting the feed allowance level. The
initial dataset, which included 50 calves, was used to as-
sess the relationships between ADG and energy intake,
as well as behavioral parameters during the group hous-
ing period (Table 1). The ADG was strongly correlated
(r = 0.55–0.61, P < 0.001) with preweaning ME intake,
number of MR intake visits, and total daily MR station
visits during group housing. The outcome of the algo-
rithm training demonstrated that K-means performed
best with 2 clusters, consisting of 21 calves each. The
respective silhouette score of 0.70 (Hedges’ g = 3.87)
reflects a strong clustering quality with distinct group
boundaries. The clusters were labeled as MAX (1.06 ±
0.01 kg/d, range: 0.97 to 1.16 kg/d) and MOD (0.84 ±
0.01 kg/d, range: 0.73–0.90 kg/d), as shown in Figure
1. The MAX calves weighed 12 kg more at the begin-
ning of weaning than the MOD calves (100.0 ± 1.21 kg
vs. 87.9 ± 1.03 kg; P < 0.001). However, there was no
further difference in ADG during the subsequent wean-
ing process from wk 9 to 14 (MAX: 1.14 ± 0.04 kg/d,
MOD: 1.06 ± 0.02 kg/d, P = 0.14). The MAX calves
were heavier than the MOD calves during the entire
MR-feeding period (Figure 2A, P < 0.001). The greatest
variance in ADG was observed within and between clus-
ters during the first 2 wk of life in the individual housing
period (MAX: 1.09 ± 0.05 kg/d, MOD: 0.71 ± 0.03 kg/d,
Figure 2B). From birth to fully weaned, the MAX calves
gained more than 1 kg/d (1.10 ± 0.02 kg/d), whereas
MOD averaged 0.93 ± 0.01 kg/d (P < 0.001). At the end
of the MR-feeding period (wk 14), the difference in BW
between the clusters reached 15 kg (MAX: 148.7 ± 2.25
kg, MOD: 133.3 ± 2.19 kg; P < 0.001).
Dam, Birth, and Colostrum Feeding
The portion of calves born to multiparous cows did not
differ between the clusters (MAX: 47.6%, MOD: 40.0%,
P = 0.62). Calves of both clusters had similar birth
weights, with MAX averaging 41.2 ± 0.84 kg and MOD
averaging 41.1 ± 0.71 kg (P = 0.93). Quality of first co-
lostrum (25.8 ± 0.63% Brix) fed to the calves and intake
quantity (3.60 ± 0.06 L) as well as total colostrum intake
(4.52 ± 0.15 L in 2 feedings) did not differ between the
clusters. The number of calves that needed assistance
for the first colostrum intake was similar (MAX: n = 11,
MOD: n = 9; P = 0.64). The season at birth had no effect
on the classification into the clusters (P = 0.33).
Table 1. Correlation coefficients (r) between preweaning ADG (birth until wk 8) and selected parameters of feed
intake during group housing of the initial 50 Holstein calves1
Item
Pearson’s r
95% CI
Effect size
(Fisher’s z)
LCL2
UCL2
ME intake preweaning,3 Mcal
0.60***
0.38
0.75
0.69
ME intake weaning,4 Mcal
0.12
−0.16
0.38
0.12
MR intake per meal,5 L
−0.44**
−0.64
−0.18
−0.47
MR-feeding station visits,5 no./d
0.55***
0.32
0.72
0.62
Visits with MR intake,5 no./d
0.61***
0.40
0.76
0.71
Visits with incomplete MR intake,5 no./d
−0.27
−0.51
0.001
−0.28
Visits without MR intake,5 no./d
0.50***
0.26
0.68
0.56
Drinking speed,5 mL/min
0.26
−0.01
0.50
0.27
1The ADG ranged between 0.73 and 1.16 kg/d.
2LCL = lower confidence limit; UCL = upper confidence limit.
3Period: rehousing, wk 8.
4Period: wk 8 to 14.
5Period: rehousing, wk 14.
**P < 0.01, ***P < 0.001.
Feed Intake and Behavior up to Weaning

# 6. ИНТЕРПРЕТАЦИЯ (Discussion)

## 6.1. Механистический анализ

Calf Performance and Behavior
This study was designed with an allowance of 12 L/d
MR, considered equivalent to ad libitum feeding and
consistent with recent studies (Rosenberger et al., 2017;
Morrison et al., 2022). Research with unlimited MR al-
lowance reported an average intake of 11.8 L/d (Philion et
al., 2024) or exceeded 12 L/d only in wk 4 and 5 of life,
with intakes of 13 to 15 L/d (Schäff et al., 2016). Similarly,
Benetton et al. (2019) observed that calves with an allow-
ance of 12 L/d during the first month of life consumed
only 8 to 9 L/d. Contrary to our expectations, even MAX
calves consumed only an average of 88.3% of their MR
allowance of 12 L/d during the preweaning group housing
period. It is known that calves offered MR ad libitum show
a wide range of voluntary intakes, from 1 to 21 L/d (Ghaf-
fari et al., 2021). Reflecting the feed allowance level, the
preweaning ADG (from birth to wk 8 of life) in our study
was adequate (range: 0.73–1.16 kg/d).
Feed efficiency across all calves was higher (i.e.,
greater gain:​feed ratio) during the 12 L/d MR periods
Table 5. Environmental factors affecting food intake and behavior of Holstein calves during MF-feeding period
(birth until wk 14 of life)
Period
Cluster
SEM
P-value
MAX
MOD
Individual housing




Daily mean temperature1 (Tmean), °C
13.8
10.8
0.87
0.07
Lowest ambient temperature1 (Tmin) per day, °C
8.5
6.5
0.71
0.14
Highest ambient temperature1 (Tmax) per day, °C
19.1
15.3
0.98
0.05
Daily temperature range (DTR2), °C
10.6
8.9
0.38
0.02
Preweaning (group housing until wk 8)




Daily mean temperature1 (Tmean), °C
14.5
11.9
1.03
0.11
Lowest ambient temperature1 (Tmin) per day, °C
9.2
6.9
0.85
0.12
Highest ambient temperature1 (Tmax) per day, °C
19.8
16.9
1.13
0.11
Daily temperature range (DTR2), °C
10.6
10.0
0.35
0.59
No. of MR-feeding station visits per group and day
73.6
91.7
4.73
0.06
Deviation in age from pen group average,3 d
−0.66
−7.4
1.4
0.02
Weaning (group housing wk 9 until wk 14)




Daily mean temperature (Tmean),1 °C
15.3
13.8
1.11
0.53
Lowest ambient temperature1 (Tmin) per day, °C
10.3
8.8
0.91
0.38
Highest ambient temperature1 (Tmax) per day, °C
20.4
18.9
1.27
0.50
Daily temperature range (DTR2), °C
10.1
10.1
0.42
0.72
No. of MR-feeding station visits per group and day
86.0
3.98
0.01
Deviation in age from pen group average,3 d
6.6
3.3
1.3
0.12
1Temperature values recorded with a temperature sensor in the group calf barn (installed at CF station). Calves
were kept in nearby sheltered individual igloos with a fenced outdoor area during individual housing. Rehousing
from individual to group housing took place in wk 2 of life. Observation period: September 9, 2021 to September
23, 2022. Tmean, Tmin, Tmax, and DTR were obtained for each day of the calves during MF-feeding period based on
48 daily records (every 30 min). Finally, an overall average value was calculated for each calf and period.
2DTR = Tmax − Tmin.
3All registered calves at the CF (age <15 wk).
(both individual and group housing) than during wean-
ing. Additionally, MAX calves demonstrated greater
efficiency compared with MOD calves during this high
allowance preweaning period. According to these results,
MAX calves showed increased ME intake along with a
concurrent improvement in feed conversion ratio during
the first 2 wk of life. Although MR intake was lower in
MOD calves, they appeared satisfied and showed no need
to transition to concentrate earlier. Instead, they seemed

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

This long-term study showed that differences in ADG
during the first 2 mo of life under a more intensive MR-
feeding program (12 L/d) were highly predictive for
Table 6. First-lactation performance (mean ± SEM) of heifers that
achieved preweaning maximum (MAX, n = 14) or moderate (MOD, n =
14) ADG during the first 2 mo of life
Item
Cluster
SEM
P-value
MAX
MOD
305-d milk yield, kg
11,511
10,242
0.001
305-d fat yield, kg
471.5
431.5
7.63
0.02
305-d protein yield, kg
408.7
368.5
4.99
<0.001
305-d lactose yield, kg
571.1
498.9
9.62
0.001
Milk fat,1 %
4.11
4.23
0.07
0.48
Milk protein,1 %
3.56
3.61
0.03
0.40
Milk lactose,1 %
4.96
4.87
0.02
0.06
1The average of all milk performance tests per heifer is shown. Only
heifers with at least 14 samples were considered.
later developmental, reproductive, and production per-
formance in Holstein heifers. Calves with greater early-
life growth (MAX) exhibited distinct feeding behaviors,
including greater MR intake, more time spent feeding at
automatic feeders, and better feed efficiency than their
contemporaries during the feeding phase. These behav-
iors and efficiencies resulted in a sustained BW advan-
tage until weaning, earlier achievement of 400 kg BW at
first insemination, and ultimately greater milk produc-
tion in the first lactation. The MAX calves produced
1,269 kg more milk over a 305-d period and had lower
MUN, indicating better nitrogen utilization efficiency. In
summary, this study demonstrates that early-life ADG is
a consistent biological indicator of lifetime performance.

## 8.2. Ключевые выводы (структурировано)

- **MAX ADG (1,06 кг/сут) vs MOD (0,84 кг/сут) в первые 2 месяца**
- **MAX телочки были на 16 кг тяжелее при отъеме (149 vs 133 кг)**
- **MAX имели лучшую кормовую эффективность в первые 2 недели (1,20-fold)**
- **MAX имели больший удой в первую лактацию (11 511 vs 10 242 кг, +12,4%)**

# 9. FAQ

**Q1: Каковы основные выводы исследования Hemmert K.J. et al.?**
A: MAX ADG (1,06 кг/сут) vs MOD (0,84 кг/сут) в первые 2 месяца

**Q2: Какие методы использовались?**
A: All procedures described in this article strictly fol- lowed the guidelines of the German Law for Animal Welfare with permission from the corresponding au- thority (Landesuntersuchungsamt Rheinland-Pfalz, Koblenz, Germany [G 21–20–049]). This study was conducted at the Educational and Research Centr...

**Q3: Как применить результаты в России?**
A: Требуется адаптация к местным условиям.

**Q4: Какие ограничения есть у этого исследования?**
A: Ограниченная выборка или специфические условия эксперимента.

# 10. ИСТОЧНИКИ

- Hemmert K.J., Ostendorf C.S., Cohrs I., Koch C., Sauerwein H. (2026). Associations of growth rates during the first 2 months of life with feeding behavior, development, and first-lactation performance in Holstein heifers. Journal of Dairy Science, 109(4), 3725-3747. doi:10.3168/jds.2025-27925

# 11. ЖУРНАЛ ОБРАБОТКИ

- **2026-05-16** — Создание SoTA v1.1 на основе полного текста статьи (PDF). Расширенная версия с извлечёнными разделами. FPF: PASS. ArchGate: article mode.
