# CS.SOTA.002: Cabrera (2012) - Economic Cow Value Assessment

---

## Article Metadata

| Field | Value |
|-------|-------|
| **Author** | Cabrera, V.E. |
| **Year** | 2012 |
| **Title** | A simple formulation and solution to the replacement problem: A practical tool to assess the economic cow value, the value of a new pregnancy, and the cost of a pregnancy loss |
| **Journal** | Journal of Dairy Science |
| **Volume/Issue** | 95(8) |
| **Pages** | 4683-4698 |
| **DOI** | http://dx.doi.org/10.3168/jds.2011-5214 |
| **Type** | Methodological / Decision support tool |

---

## SoTA Status

| Aspect | Status | Date |
|--------|--------|------|
| **Currency** | Foundational / Classic | 2026-03-01 |
| **Evidence Level** | High (methodological) | Validated approach |
| **Relevance** | High | Still cited and used |
| **Confidence** | High | Widely adopted |

**Overall Status:** Foundational (Classic)

**Note:** Method remains valid; specific economic values require updating.

---

## Key Claims

### Claim 1: Simplified Markov Chain Can Replace Complex Dynamic Programming
> "The proven hypothesis of this study was that all the above requirements could be achieved by using a Markov chain algorithm."

**Evidence:** Results consistent with prior DP studies (Groenendaal et al. 2004)

**Confidence:** High

**Practical Implication:** Farmers can use practical tools without complex optimization software.

---

### Claim 2: Pregnant Cows Have Higher Economic Value
> "The cow value indicated pregnant cows should be kept."

**Evidence:** Comparative values at same MIM (pregnant vs. open)

**Confidence:** High

**Practical Implication:** Default replacement policy = keep pregnant cows.

---

### Claim 3: Open Cow Value Declines Dramatically in Late Lactation
> Nonpregnant cow: $897 (MIM=1) → $68 (MIM=8)

**Evidence:** Direct calculation

**Confidence:** High

**Practical Implication:** Late open cows are strong cull candidates.

**Value:** 93% value loss by MIM=8 if not pregnant (2012$)

---

### Claim 4: Pregnancy Loss Cost Increases with Gestation
> Early loss (month 1): $221; Late loss (month 9): $897

**Evidence:** Stage-dependent valuation

**Confidence:** High

**Practical Implication:** Protect pregnant cows, especially late-term; late abortion costs ≈ cow value.

---

### Claim 5: Expected Production and Genetic Gain Significantly Affect Value
> "A 120% expected milk production... determined between 1.52 and 6.48 times the cow value"
> "The cow value decreased by $211 for every 1 percentage point of expected genetic gain of the replacement"

**Evidence:** Sensitivity analysis

**Confidence:** Medium-High

**Practical Implication:** Individual cow assessment must include production potential and genetic context.

---

## Methodology Assessment

### Approach
- **Type:** Markov chain algorithm
- **Innovation:** Simplification of complex DP models
- **Calculation:** Forward expected value

### Strengths
1. User-friendly (practical adoption)
2. Single model for replacement policies AND herd statistics
3. Includes farmer assessment of expected performance
4. Includes genetic gain consideration
5. Results consistent with complex DP

### Limitations
1. **Predefined policy:** Markov simulates, doesn't optimize
2. **Simplification:** Less theoretically "optimal" than DP
3. **Requires estimates:** Future production, genetic gain
4. **Static:** Point-in-time calculation

### Validation
- Consistent with Groenendaal et al. (2004) DP results
- Widely cited and adopted
- Foundation for Lauber (2025) and Giordano (2012)

---

## Historical Significance

### Context (2012)
- Problem: DP models too complex for practical use
- Solution: Simplified Markov approach
- Impact: Enabled practical decision support tools

### Legacy
- Cited in 2025 research (Lauber)
- Foundation for herd-level models
- Still used in Extension programs

### Current Applicability
| Aspect | Status | Action Needed |
|--------|--------|---------------|
| Method | Valid | None |
| Economic values | Outdated | Update to current prices |
| Software tools | Superseded | Use modern implementations |

---

## Revision Criterion

**Trigger for review:**
- New methodology demonstrating significant improvement over Markov approach
- Substantial change in dairy economics structure

**Note:** As foundational work, unlikely to be "revised" but may be superseded by extensions.

---

## Related SoTA Entries

| Entry | Relationship |
|-------|--------------|
| CS.SOTA.001 (Lauber 2025) | Extension to herd-level optimization |
| CS.SOTA.003 (Giordano 2012) | Concurrent Markov model development |

---

## Application Notes

### When to Use This Source
- Understanding cow value fundamentals
- Developing simple decision support tools
- Teaching replacement economics
- Historical context for modern methods

### When to Supplement
- Current economic parameters (update required)
- Herd-level optimization (see Lauber 2025)
- Individual farm data for calibration

### When to Be Cautious
- Using 2012 economic values without updating
- Applying to very different production systems
- Ignoring later methodological improvements

---

## Distinctions Applied

- **D.003 Input vs. Output:** MIM, pregnancy, production (inputs) → Cow value (output)
- **D.005 Biological vs. Economic:** Production potential vs. economic value
- **D.007 Model vs. Reality:** Markov simulation vs. actual farm decisions

---

## Pack Integration

| Element | Integration |
|---------|-------------|
| Method | CS.METHOD.004-cow-value-assessment (primary source) |
| Work Product | CS.WP.004-cow-value-report (application) |
| Foundation for | CS.METHOD.003 (Lauber 2025 extension) |

---

*SoTA annotation created: 2026-03-01*  
*Status: Foundational (Classic)*  
*Next review: Upon significant methodological advancement*
