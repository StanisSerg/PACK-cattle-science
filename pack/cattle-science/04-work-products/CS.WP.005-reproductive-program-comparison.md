# Reproductive Program Comparison Report

## Metadata
```yaml
type: work_product
domain: cattle-science
area: reproductive-management
id: CS.WP.005
version: 1.0
status: template
method: CS.METHOD.005
sota: CS.SOTA.003
created: 2026-03-01
purpose: "Compare economic outcomes of TAI and ED reproductive programs"
```

---

## Purpose

Structured comparison of reproductive program alternatives to support farm management decisions on TAI vs estrus detection strategies.

---

## When to Use

- Evaluating current reproductive program performance
- Considering transition to TAI, ED, or combined approach
- Benchmarking against industry standards
- Justifying reproductive technology investments

---

## Required Inputs

### Farm-Specific Data

| Data Category | Specific Items | Source |
|---------------|----------------|--------|
| Current program | TAI %, ED %, protocols used | Farm records |
| Conception rates | TAI CR, ED CR by parity/lactation | DairyComp/DC305 |
| Estrus detection | Detection rate, accuracy | Activity monitors/visual |
| Economics | Milk price, feed cost, semen cost | Accounting records |
| Herd structure | Parity distribution, cull rate | Management software |

### Benchmark Data

| Benchmark | Typical Range | Source |
|-----------|---------------|--------|
| TAI CR (first) | 40-45% | Industry standard |
| TAI CR (second+) | 28-35% | Industry standard |
| ED CR | 25-35% | Farm-specific |
| ED rate | 40-60% | Activity monitors |

---

## Report Structure

### Section 1: Executive Summary

```markdown
## Executive Summary

**Farm:** [Name]
**Date:** [Date]
**Analyst:** [Name]

### Current Program
- Type: [100% TAI / TAI+ED / ED-only]
- Performance: [21-d PR: X%]
- Economics: [NV: $X/cow/year]

### Key Finding
[One-sentence conclusion: e.g., "Transitioning to 50% ED with 30% CR would increase NV by $X/cow/year"]

### Recommendation
[Specific actionable recommendation]
```

### Section 2: Program Definitions

| Program ID | Description | TAI CR1 | TAI CR2+ | ED CR | ED % |
|------------|-------------|---------|----------|-------|------|
| P1 | 100% TAI | 42% | 30% | - | 0% |
| P2 | TAI + low ED | 40% | 28% | 25% | 30% |
| P3 | TAI + med ED | 38% | 26% | 30% | 50% |
| P4 | TAI + high ED | 35% | 24% | 35% | 80% |
| P5 | [Custom] | [%] | [%] | [%] | [%] |

### Section 3: Economic Comparison

#### Net Value Results

| Program | NV ($/cow/yr) | vs P1 Δ | Rank |
|---------|---------------|---------|------|
| P1 (100% TAI) | $[value] | - | [rank] |
| P2 (TAI+low ED) | $[value] | $[Δ] | [rank] |
| P3 (TAI+med ED) | $[value] | $[Δ] | [rank] |
| P4 (TAI+high ED) | $[value] | $[Δ] | [rank] |

#### Component Breakdown

| Program | IOFC | Repro Cost | Replace Cost | Net |
|---------|------|------------|--------------|-----|
| P1 | $[X] | $[Y] | $[Z] | $[NV] |
| P2 | $[X] | $[Y] | $[Z] | $[NV] |
| P3 | $[X] | $[Y] | $[Z] | $[NV] |
| P4 | $[X] | $[Y] | $[Z] | $[NV] |

*IOFC = Income Over Feed Cost*

### Section 4: Reproductive Performance

| Program | 21-d PR | Days Open | Services/Conception | Cull Rate |
|---------|---------|-----------|---------------------|-----------|
| P1 | [%] | [days] | [X] | [%] |
| P2 | [%] | [days] | [X] | [%] |
| P3 | [%] | [days] | [X] | [%] |
| P4 | [%] | [days] | [X] | [%] |

### Section 5: Sensitivity Analysis

#### Key Sensitivities

| Parameter | Base Value | Low (-20%) | High (+20%) | Impact on Recommendation |
|-----------|------------|------------|-------------|--------------------------|
| TAI CR | [%] | [%] | [%] | [Stable/Changes] |
| ED CR | [%] | [%] | [%] | [Stable/Changes] |
| Milk price | $[X] | $[Y] | $[Z] | [Stable/Changes] |
| Semen cost | $[X] | $[Y] | $[Z] | [Stable/Changes] |

### Section 6: CR Trade-off Analysis

> "As ED proportion increases, TAI CR decreases"

| ED % | Expected TAI CR Impact | Net Effect on NV |
|------|------------------------|------------------|
| 30% | -2% first, -2% second+ | [Positive/Negative] |
| 50% | -4% first, -4% second+ | [Positive/Negative] |
| 80% | -7% first, -6% second+ | [Positive/Negative] |

### Section 7: Heifer Supply Integration

| Scenario | Current | With Adjustment | NV Impact |
|----------|---------|-----------------|-----------|
| Heifer surplus | [DIM cutoff] | [Adjusted] | $[Δ] |
| Heifer deficit | [DIM cutoff] | [Adjusted] | $[Δ] |
| Balanced | [DIM cutoff] | [No change] | $[Δ] |

### Section 8: Recommendations

#### Primary Recommendation

**Program:** [P1/P2/P3/P4/Custom]
**Expected NV:** $[X]/cow/year
**Implementation:** [Steps]

#### Implementation Timeline

| Phase | Action | Timeline | Responsible |
|-------|--------|----------|-------------|
| 1 | [Action] | [Weeks] | [Role] |
| 2 | [Action] | [Weeks] | [Role] |
| 3 | [Action] | [Weeks] | [Role] |

#### Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [L/M/H] | [L/M/H] | [Action] |
| [Risk 2] | [L/M/H] | [L/M/H] | [Action] |

---

## Quality Checklist

- [ ] All 4+ programs compared
- [ ] Farm-specific data used (not just defaults)
- [ ] Sensitivity analysis completed
- [ ] CR trade-off considered
- [ ] Heifer supply integrated
- [ ] Implementation plan provided
- [ ] Risks identified

---

## Example: Giordano 2012 Reference Results

| Program | ED CR | ED % | NV Rank | Key Insight |
|---------|-------|------|---------|-------------|
| 100% TAI | - | 0% | Lower | Baseline |
| TAI+ED | 25% | 30% | Lowest | Low ED CR not viable |
| TAI+ED | 30% | 50% | Moderate | Balanced approach |
| TAI+ED | 35% | 80% | **Highest** | High ED CR enables high ED % |

**Reference:** Giordano et al. (2012), Journal of Dairy Science 95:5442-5460

---

## Related Work Products

| WP | Relationship | When to Use Together |
|----|--------------|---------------------|
| CS.WP.003 | Economic evaluation | Compare methods |
| CS.WP.004 | Cow value assessment | Individual decisions |
| CS.WP.005 | This template | Program comparison |

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-01 | Initial template from Giordano 2012 |

---

*Part of PACK-cattle-science*  
*Repository: https://github.com/StanisSerg/PACK-cattle-science*
