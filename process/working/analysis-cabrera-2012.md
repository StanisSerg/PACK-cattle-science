# Analysis: Cabrera (2012)

> Stage 06: Analysis and Formalization

---

## Source Information

**Full Citation:** Cabrera, V.E. (2012). A simple formulation and solution to the replacement problem: A practical tool to assess the economic cow value, the value of a new pregnancy, and the cost of a pregnancy loss. *Journal of Dairy Science*, 95(8), 4683-4698.

**Article Type:** Methodological / Decision support tool

**Confidence Level:** High (foundational, widely cited)

---

## 1. Key Parameters Extracted

### Cow Value Examples (Average Second-Lactation Cow)

| Scenario | MIM | Status | Value | Unit |
|----------|-----|--------|-------|------|
| Nonpregnant | 1 | Open | $897 | $/cow |
| Nonpregnant | 8 | Open | $68 | $/cow |
| Just pregnant | 3 | Pregnant | $889 | $/cow |
| Just pregnant | 8 | Pregnant | $298 | $/cow |

### Pregnancy Loss Value (Cow Pregnant in MIM = 5)

| Loss Timing | Value of Loss | Interpretation |
|-------------|---------------|----------------|
| First month of pregnancy | $221 | Early loss cost |
| Ninth month of pregnancy | $897 | Late loss cost (≈ cow value) |

### Key Sensitivity Parameters

| Parameter | Value | Impact |
|-----------|-------|--------|
| Genetic gain effect on cow value | -$211 | Per 1% expected genetic gain of replacement |
| High production premium (120%) | 1.52-6.48× | Cow value multiplier for high producers |

### Model Specifications

| Parameter | Value | Description |
|-----------|-------|-------------|
| MIM for pregnancy check | 9 | Month in milk for status evaluation |
| Lactations modeled | 1-9 | Parity range |
| Algorithm | Markov chain | Forward expected value calculation |

---

## 2. Key Findings

1. **Pregnant cows should be kept**
   - Cow value higher when pregnant vs. open at same MIM
   - Evidence: $889 (pregnant MIM=3) vs. implied lower value for open
   - Implication: Default policy = keep pregnant cows

2. **Cow value decreases dramatically in late lactation if open**
   - Nonpregnant cow: $897 (MIM=1) → $68 (MIM=8)
   - Evidence: 93% value loss by MIM=8 if not pregnant
   - Implication: Late open cows are strong cull candidates

3. **Pregnancy loss cost increases with gestation stage**
   - Early loss (month 1): $221
   - Late loss (month 9): $897
   - Evidence: Late loss equals cow value
   - Implication: Protect pregnant cows, especially late-term

4. **Expected production relative to herd average is critical**
   - 120% production cow: 1.52-6.48× cow value
   - Evidence: Multiplier depends on MIM and pregnancy status
   - Implication: High producers have substantially higher value

5. **Genetic gain of replacement affects current cow value**
   - Effect: -$211 per 1% genetic gain of replacement
   - Evidence: Sensitivity analysis
   - Implication: Rapid genetic progress increases cull pressure

---

## 3. Methodology Assessment

### Approach
- **Type:** Markov chain algorithm
- **Innovation:** Simpler than dynamic programming, more practical
- **Calculation:** Forward expected value (not backward optimization)

### Strengths
1. User-friendly vs. complex DP models
2. Practical for day-to-day farmer decisions
3. Includes farmer assessment of expected performance
4. Includes genetic gain consideration
5. Single model calculates both replacement policies AND herd statistics

### Limitations
1. **Predefined policy required:** Markov simulates, doesn't optimize
2. **Simplification:** Less theoretically "optimal" than DP
3. **Assumptions:** Requires estimates of future production

### Validation
- Results consistent with prior DP studies (Groenendaal et al. 2004)
- Widely adopted in later research (Lauber 2025, Giordano 2012)

---

## 4. Distinctions Applied

| Distinction | Application |
|-------------|-------------|
| D.003 Input vs. Output | MIM, pregnancy status (inputs) → Cow value (output) |
| D.005 Biological vs. Economic | Production potential vs. economic value |
| D.007 Model vs. Reality | Markov simulation vs. actual farm decisions |

---

## 5. Knowledge Candidates

### Candidate 1: Method
- **Name:** Economic cow value assessment
- **Type:** Decision support method
- **ID:** CS.METHOD.004-cow-value-assessment
- **Key parameters:** MIM, pregnancy status, expected production, genetic gain
- **Output:** Cow value, pregnancy value, pregnancy loss cost

### Candidate 2: Norm
- **Parameter:** Pregnancy status threshold
- **Value:** Pregnant cows should be kept (default)
- **Exception:** Late pregnancy + very low production + high genetic gain

### Candidate 3: Work Product
- **Name:** Cow value assessment report
- **ID:** CS.WP.004-cow-value-report
- **Contents:** Individual cow values, cull/keep recommendations

---

## 6. SoTA Assessment

| Aspect | Status | Rationale |
|--------|--------|-----------|
| **Currency** | Historical (2012) | Superseded by later models BUT foundational |
| **Evidence type** | Methodological | Well-validated approach |
| **Relevance** | High | Still used, cited in 2025 research |
| **Confidence** | High | Widely adopted, consistent with DP |

**Overall Status:** Foundational / Classic

**Note:** While specific numbers may be dated (2012 economics), the method remains valid. Current applications should update economic parameters.

---

## 7. Pack Integration

### Files to Create/Update

1. **03-methods/CS.METHOD.004-cow-value-assessment.md**
   - Simplified Markov method
   - Cow value calculation
   - Pregnancy loss valuation

2. **06-sota/CS.SOTA.002-cabrera-2012-cow-value.md**
   - Foundational method annotation
   - Historical significance
   - Current applicability notes

3. **04-work-products/CS.WP.004-cow-value-report.md**
   - Individual cow assessment template

### Relationship to Lauber 2025

| Aspect | Cabrera 2012 | Lauber 2025 |
|--------|--------------|-------------|
| Focus | Individual cow value | Herd-level optimization |
| Method | Markov (simplified) | Markov (extended) |
| Scale | Single cow | 1,000-cow herd |
| Use | Practical tool | Research simulation |
| Status | Foundation | Extension |

**Connection:** Lauber 2025 builds on Cabrera 2012 methodology

---

## Next Steps

1. [x] Extract parameters from PDF
2. [x] Identify key findings
3. [x] Assess methodology
4. [ ] Create CS.METHOD.004
5. [ ] Create CS.SOTA.002
6. [ ] Create CS.WP.004
7. [ ] Update ingestion log → "analyzed"

---

*Analysis completed: 2026-03-01*
*Analyst: Claude (AI assistant)*
*Status: Ready for Stage 07*
