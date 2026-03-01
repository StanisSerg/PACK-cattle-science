# CS.ENTITY.001: 21-Day Pregnancy Rate

> Core reproductive metric linking biological performance to economic outcomes.

---

## Definition

**21-day pregnancy rate (21-d PR)** is the percentage of eligible non-pregnant cows that become pregnant over a 21-day period.

**Formula:**
```
21-d PR = Service Rate × Conception Rate (P/AI) × 100

Where:
- Service Rate = % of eligible cows receiving AI in 21 days
- Conception Rate (P/AI) = % of inseminated cows becoming pregnant
```

---

## Significance

### Biological Significance
- Measures efficiency of reproductive process
- Combines heat detection accuracy (service rate) and fertility (conception)
- Independent of voluntary waiting period (VWP)

### Economic Significance
- Primary driver of reproductive economic performance
- Each 1% improvement = $2-7/cow/year additional net return
- Determines optimal insemination eligibility period (IEP)

### Herd Structure Significance
- Determines calving interval
- Affects replacement rate
- Influences proportion of cows in each reproductive state

---

## Classification Scale

| Category | 21-d PR | Interpretation | Action Required |
|----------|---------|----------------|-----------------|
| **Low** | <20% | Poor performance | Immediate intervention |
| **Below average** | 20-24% | Below benchmark | Improvement needed |
| **Average** | 25-29% | Industry standard | Maintain with monitoring |
| **Above average** | 30-34% | Good performance | Maintain |
| **High** | ≥35% | Excellent performance | Benchmark for others |

### Historical Context (US Holstein herds)

| Period | Average 21-d PR | Top 25% | Top 10% |
|--------|-----------------|---------|---------|
| 2012 | 16% | 20% | 20% |
| 2016 | 18% | 24% | 26% |
| 2020 | 20% | 28% | 30% |

*Source: DRMS, 2024*

---

## Measurement

### Data Requirements

| Parameter | Source | Frequency |
|-----------|--------|-----------|
| Insemination dates | Breeding records | Real-time |
| Pregnancy check results | Vet records | 28-42 days post-AI |
| Eligible cow inventory | Herd software | Daily |

### Calculation Method

**Step 1: Define eligible cows**
- Cows past VWP (typically 50-70 DIM)
- Non-pregnant
- Not marked as "do not breed"

**Step 2: Track over 21-day periods**
- Rolling or fixed periods
- Account for seasonality

**Step 3: Calculate**
```
For each 21-day period:
  Eligible cows at start = E
  Cows receiving AI = A
  Cows becoming pregnant = P
  
  Service Rate = A / E × 100
  Conception Rate = P / A × 100
  21-d PR = P / E × 100
```

### Reporting

**Recommended:** 3-month rolling average  
**Minimum:** Monthly calculation  
**Presentation:** Percentage with trend arrow (▲ ▼ →)

---

## Influencing Factors

### Management Factors (Controllable)

| Factor | Impact on 21-d PR | Improvement Strategy |
|--------|-------------------|---------------------|
| Heat detection efficiency | Direct on Service Rate | Training, aids, activity monitors |
| AI technician skill | Direct on Conception Rate | Certification, supervision |
| Synchronization protocols | Direct on Service Rate | Systematic implementation |
| Semen handling | Direct on Conception Rate | Quality control, training |
| Transition cow management | Indirect via fertility | Metabolic monitoring |

### Biological Factors (Partially Controllable)

| Factor | Impact | Management Response |
|--------|--------|---------------------|
| Days in milk | Peak fertility 60-100 DIM | Optimize timing |
| Lactation number | 1st lactation lower fertility | Extra attention to heifers |
| Season/heat stress | Summer decline | Cooling, timing |
| Body condition score | BCS 3.0-3.5 optimal | Nutritional management |
| Metabolic disorders | Ketosis, mastitis reduce fertility | Prevention protocols |

### Genetic Factors (Selectable)

- Daughter pregnancy rate (DPR) in sire selection
- Fertility index inclusion in breeding decisions

---

## Economic Value

### Direct Value

| 21-d PR Level | Economic Status | Opportunity |
|---------------|-----------------|-------------|
| <20% | Significant loss | $50-100/cow/year potential gain |
| 20-24% | Below potential | $30-50/cow/year potential gain |
| 25-29% | Near optimal | $10-20/cow/year potential gain |
| 30-34% | Good | Maintain, benchmark |
| ≥35% | Excellent | Share practices |

### Value of Improvement

**Marginal value:** $2-7/cow/year per 1-percentage-point increase

**Example:**
- 500-cow herd
- Improving from 22% to 28% (6 points)
- Value: 500 × 6 × $5 = $15,000/year

---

## Related Concepts

| Concept | Relationship | Reference |
|---------|--------------|-----------|
| Days open | Outcome of 21-d PR | Lower 21-d PR → Higher days open |
| Calving interval | Outcome of 21-d PR | Target: 12.5-13.5 months |
| Insemination eligibility period | Optimized based on 21-d PR | CS.METHOD.003 |
| Semen type strategy | Decision depends on 21-d PR | CS.METHOD.003 |

---

## Failure Modes

| Mode | Detection | Prevention |
|------|-----------|------------|
| Overestimation | Compare calculated vs. actual calvings | Use confirmed pregnancies only |
| Seasonal blindness | Annual average masks variation | Report by season/quarter |
| Small sample error | High variability in small herds | Use 3-month rolling average |
| Eligibility errors | Cows counted incorrectly | Automated eligibility tracking |

---

## References

1. Ferguson, J.D., & Galligan, D.T. (1993). Reproductive performance in dairy herds. *Veterinary Clinics of North America: Food Animal Practice*, 9(2), 333-354.

2. Overton, M.W., & Cabrera, V.E. (2017). The Economic Impact of Reproductive Performance. *Veterinary Clinics of North America: Food Animal Practice*, 33(2), 325-342.

3. Lauber, M.R., Cabrera, V.E., & Fricke, P.M. (2025). An economic simulation model to assess the effect of the 21-day pregnancy rate... *Journal of Dairy Science*.

---

## Distinctions Applied

- **D.003 Input vs. Output:** 21-d PR is input parameter; days open, calving interval are outputs
- **D.005 Biological vs. Economic:** Biological metric with direct economic translation

---

*Entity defined: 2026-03-01*  
*Status: Active*  
*Review cycle: Annual*
