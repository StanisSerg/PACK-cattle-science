# CS.SOTA.005: Galvão et al. (2013) - Economic Comparison of Reproductive Programs

---

## Article Metadata

| Field | Value |
|-------|-------|
| **Authors** | Galvão, K.N., Federico, P., De Vries, A., Schuenemann, G.M. |
| **Year** | 2013 |
| **Title** | Economic comparison of reproductive programs for dairy herds using estrus detection, timed artificial insemination, or a combination |
| **Journal** | Journal of Dairy Science, 96:2681-2693 |
| **DOI** | https://doi.org/10.3168/jds.2012-5982 |
| **Type** | Economic simulation (stochastic dynamic Monte-Carlo) |

---

## SoTA Status

| Aspect | Status | Date |
|--------|--------|------|
| **Currency** | Current | 2026-03-01 |
| **Evidence Level** | Medium-High | Validated simulation, extensive scenarios |
| **Relevance** | High | Core decision for reproductive management |
| **Confidence** | Medium-High | Model-based, not field trial |

**Overall Status:** Current (with simulation caveat)

---

## Key Claims

### Claim 1: Combining TAI and ED Increases Profits vs. Either Alone
> "Adding TAI to ED would increase overall profit/cow per year by $46.8 to $74.7 with 40% ED, and by $8.9 to $30.5 with 60% ED. Adding ED to TAI would increase profit/cow per year by $64.2 to $99.4 with 85% compliance and by $31.8 to $59.7 with 95% compliance."

**Evidence:** Monte-Carlo simulation, 1,000 cow herd, steady-state analysis (3,000d + 2,000d)

**Confidence:** Medium-High (model-dependent)

**Practical Implication:** Synergistic effect of combining both approaches — not either/or decision

**Value Range:** +$8.9 to +$99.4/cow/year depending on baseline performance

---

### Claim 2: High-Performance Single Systems Match Combined Systems
> "ED60 with 95% accuracy or TAI with 95% compliance were as profitable as or more profitable than TAI-ED with low ED, accuracy, or compliance."

**Evidence:** Scenario comparison across ED rates (40%, 60%), accuracy (85%, 95%), compliance (85%, 95%)

**Confidence:** High (within model assumptions)

**Practical Implication:** If you can execute one system excellently, don't add complexity of second system

**Threshold:** ED ≥60% with ≥95% accuracy OR TAI with ≥95% compliance

---

### Claim 3: ED40 Outperforms Low-Compliance TAI
> "The ED40 models resulted in greater profits than the TAI-85 model but lower profits than the TAI-95 model."

**Confidence:** High

**Practical Implication:** Poor compliance with TAI is worse than moderate ED

**Implication for management:** TAI investment requires compliance commitment

---

### Claim 4: ED60 Outperforms Even High-Compliance TAI
> "Both ED60 models resulted in greater profits than the TAI-95 model."

**Confidence:** High

**Practical Implication:** Excellent estrus detection remains gold standard economically

**Caveat:** ED60 with 95% accuracy is difficult to achieve in practice

---

## Methodology Assessment

### Approach
- **Type:** Stochastic dynamic Monte-Carlo simulation
- **Herd size:** 1,000 cows (maintained constant)
- **Time horizon:** 3,000d to steady state + 2,000d analysis
- **Scenarios evaluated:**
  - ED only: 40% or 60% detection rate, 85% or 95% accuracy
  - TAI only: Presynch-Ovsynch first AI, Ovsynch resync at 32d; 85% or 95% compliance
  - TAI-ED combined: Presynch-Ovsynch first AI, then ED; resync open cows at 32d
- **Economic factors:** Milk price ($0.33 vs $0.44/kg), all incomes and costs included
- **Biological parameters:** CR 33.9% first service, -2.6% per subsequent; abortion 11.3%; no AI after 366 DIM; cull open at 450 DIM

### Strengths
1. Comprehensive economic modeling (all costs and incomes)
2. Extensive sensitivity analysis (ED rate, accuracy, compliance, milk price)
3. Validated simulation approach (used in prior studies)
4. Practical scenario range (40-60% ED achievable; 85-95% compliance realistic)

### Limitations
1. **Simulation, not field trial:** Results are model predictions
2. **Fixed parameters:** CR, abortion rate static (not herd-specific)
3. **Immediate replacement:** Assumes no replacement cost/lag
4. **No health interactions:** Transition health not modeled
5. **Static prices:** No year-to-year variation

### Validation Status
- Model structure: Based on established dairy simulation models
- Parameters: Industry-standard values (USDA 2009, etc.)
- **Field validation:** Not performed; use as decision support, not prediction

---

## Revision Criterion

**Trigger for review:**
- Field trial with >20 herds comparing these programs with different results
- Major technology shift (automated ED systems, sexed semen cost reduction)
- Significant change in milk/beef price ratios
- New synchronization protocols with different compliance profiles

**Review date:** 2027-03-01 (annual) or earlier if trigger event

---

## Related SoTA Entries

| Entry | Relationship |
|-------|--------------|
| CS.SOTA.001 (Lauber 2025) | Builds on this model; adds semen type and IEP optimization |
| CS.SOTA.004 (Bruinjé 2024) | Health factors affecting reproductive performance (not in this model) |

---

## Application Notes

### When to Use This Source
- Deciding between ED, TAI, or combined approach
- Justifying investment in ED training or synchronization protocols
- Setting performance targets (ED rate, accuracy, compliance)
- Evaluating current program against benchmarks

### When to Supplement
- Herd-specific economics (use current prices, costs)
- Health-challenged herds (Bruinjé 2024)
- Sexed/beef semen strategies (Lauber 2025)
- Genetic considerations (not addressed)

### When to Be Cautious
- Herds with ED <40% or accuracy <85% (outside tested range)
- TAI compliance <85% (worse than any modeled scenario)
- Grazing or seasonal systems (model assumptions may not hold)
- Very large or small herds (1,000 cow baseline)

---

## Distinctions Applied

| Distinction | Application |
|-------------|-------------|
| D.003 Input vs. Output | Program choice (input) → Profit (output) |
| D.005 Biological vs. Economic | Biological parameters fixed; economic optimization |
| D.007 Model vs. Reality | Simulation estimates; validate with herd data |
| D.008 Strategy vs. Tactics | Strategic program choice; tactical execution (accuracy, compliance) |

---

## Pack Integration

| Element | Integration |
|---------|-------------|
| Method | CS.METHOD.006-reproductive-program-selection |
| Work Product | CS.WP.006-reproductive-program-economic-analysis |
| Entity | CS.ENTITY.003-reproductive-program-efficiency |
| Thresholds | ED≥60% + accuracy≥95% OR TAI compliance≥95% |

---

*SoTA annotation created: 2026-03-01*  
*Analyst: Claude (AI assistant)*  
*Next review: 2027-03-01*
