# Herd-Level Reproductive Program Simulation

## Metadata
```yaml
type: method
domain: cattle-science
area: reproductive-management
subarea: decision-support
id: CS.METHOD.005
version: 1.0
status: draft
sources: ["Giordano-2012"]
created: 2026-03-01
author: "Giordano et al. (2012)"
```

---

## Purpose

Simulate and compare economic outcomes of different reproductive programs combining timed artificial insemination (TAI) and estrus detection (ED) at herd level using daily Markov chain methodology.

---

## When to Use

- **Decision context:** Choosing between TAI-only, ED-only, or combined programs
- **Data availability:** Conception rates for TAI and ED, estrus detection rates
- **Scale:** Herd-level economic comparison
- **Time horizon:** Long-term steady-state projections

---

## Required Inputs

### Program Parameters

| Parameter | Symbol | Unit | Typical Range | Source |
|-----------|--------|------|---------------|--------|
| TAI conception rate (first service) | CR_TAI1 | % | 35-45 | Farm records / literature |
| TAI conception rate (second+) | CR_TAI2+ | % | 25-35 | Farm records / literature |
| ED conception rate | CR_ED | % | 25-35 | Farm records / literature |
| ED proportion | P_ED | % | 0-80 | Management decision |
| Voluntary waiting period | VWP | days | 50-70 | Management decision |

### Economic Parameters

| Parameter | Symbol | Unit | Notes |
|-----------|--------|------|-------|
| Milk price | P_milk | $/kg | Market rate |
| Feed cost | C_feed | $/cow/day | Lactation stage dependent |
| Semen cost | C_semen | $/dose | TAI vs conventional |
| Hormone cost | C_hormone | $/protocol | Ovsynch costs |
| Cull cow value | V_cull | $ | Market dependent |
| Heifer cost | C_heifer | $ | Replacement cost |

### Herd Parameters

| Parameter | Symbol | Unit | Typical Value |
|-----------|--------|------|---------------|
| Herd size | N | cows | 100-1000+ |
| Average parity | - | lactation | 2.5 |
| Baseline cull rate | - | %/year | 25-35 |

---

## Methodology

### Step 1: Define Cow States

Each cow is characterized by:
- **Parity:** 1, 2, 3+ (or specific lactation number)
- **DIM:** Days in milk (1 to 999)
- **Pregnancy status:** Open, pregnant (by DIM of conception), or dry
- **Reproductive program:** TAI or ED eligible

**Total states:** ~600,000 combinations (Giordano 2012)

### Step 2: Define Transition Probabilities

**Daily transitions for open cows:**

| From State | To State | Probability | Condition |
|------------|----------|-------------|-----------|
| Open, DIM < VWP | Open, DIM+1 | 1.0 | Waiting period |
| Open, DIM ≥ VWP, TAI | Pregnant | CR_TAI / 100 | Insemination day |
| Open, DIM ≥ VWP, TAI | Open, DIM+1 | 1 - CR_TAI/100 | Not pregnant |
| Open, DIM ≥ VWP, ED | Pregnant | P_ED × CR_ED/100 | Detected & conceived |
| Open, DIM ≥ VWP, ED | Open, DIM+1 | 1 - above | Not pregnant or not detected |

### Step 3: Define Replacement Rules

**Mandatory culling:**
- DIM > cutoff (e.g., 400-500 days open)
- Low milk production (< threshold)
- Death/illness (fixed probability)

**Voluntary culling:**
- Based on economic threshold (optional)

### Step 4: Simulate Replacement Herd

- Track heifer inventory
- Match supply to demand
- Adjust culling policy if surplus/deficit

### Step 5: Calculate Steady-State Distribution

**Iterative solution:**
1. Initialize herd distribution
2. Apply daily transitions for all cows
3. Add replacements for culled cows
4. Repeat until distribution stabilizes
5. Calculate annual averages

### Step 6: Calculate Net Value

```
NV = Income_over_feed_cost - Reproductive_costs - Replacement_costs

Where:
- Income_over_feed_cost = Σ(Milk_revenue - Feed_cost) for all cows
- Reproductive_costs = Semen + Hormones + Labor
- Replacement_costs = Heifer_cost - Cull_value
```

---

## Key Relationships

### CR Trade-off

> "As the proportion of cows receiving AI after ED increased, the CR of cows receiving TAI decreased"

**Interpretation:** Resource competition or management attention effect

| ED Proportion | Expected TAI CR Impact |
|---------------|------------------------|
| 0% (100% TAI) | Baseline (42% first, 30% second+) |
| 30% | Slight decrease |
| 50% | Moderate decrease |
| 80% | Significant decrease |

### Optimal Program Selection

| ED CR | Recommended ED Proportion | Expected NV Rank |
|-------|---------------------------|------------------|
| 25% | Low (≤30%) or none | Lower |
| 30% | Moderate (30-50%) | Moderate |
| 35% | High (50-80%) | Highest |

---

## Outputs

### Primary Output

| Metric | Description | Use |
|--------|-------------|-----|
| Net Value (NV) | $/cow/year | Program comparison |

### Secondary Outputs

| Metric | Description |
|--------|-------------|
| 21-day pregnancy rate | Herd-level reproductive efficiency |
| Days open | Average interval |
| Cull rate | Annual replacement rate |
| Heifer surplus/deficit | Inventory balance |
| Program cost | $/cow/year reproductive expenses |

### Comparison Table Format

| Program | TAI CR | ED CR | ED % | NV ($/cow/yr) | 21-d PR | Rank |
|---------|--------|-------|------|---------------|---------|------|
| 100% TAI | 42/30 | - | 0% | [value] | [value] | [rank] |
| TAI+ED low | 40/28 | 25% | 30% | [value] | [value] | [rank] |
| TAI+ED med | 38/26 | 30% | 50% | [value] | [value] | [rank] |
| TAI+ED high | 35/24 | 35% | 80% | [value] | [value] | [rank] |

---

## Validation

### Internal Consistency Checks

| Check | Expected Result |
|-------|-----------------|
| Total probability | Sum of transitions from any state = 1.0 |
| Herd size | Stable at target N |
| Cull rate | Matches replacement rate |
| Pregnancy rate | Consistent with CR and service rate |

### External Validation

| Source | Comparison |
|--------|------------|
| Field data | Compare simulated vs actual 21-d PR |
| Literature | Compare NV to other studies |
| Expert opinion | Review program rankings |

---

## Limitations and Considerations

### Model Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Steady-state assumption | Ignores transitional dynamics | Use for long-term planning only |
| Fixed CR values | Ignores individual variation | Sensitivity analysis on CR |
| Predefined policies | Not true optimization | Compare wide range of programs |
| Computational complexity | ~600,000 states | Efficient matrix operations |

### Practical Considerations

| Factor | Recommendation |
|--------|----------------|
| ED accuracy | Invest in training before increasing ED proportion |
| Resource allocation | Balance ED effort vs TAI protocol compliance |
| Heifer supply | Adjust culling policy to match replacement availability |
| Economic update | Update prices/costs annually |

---

## Related Methods

| Method | Relationship | When to Use |
|--------|--------------|-------------|
| CS.METHOD.004 (Cabrera 2012) | Simpler, monthly | Quick individual cow assessment |
| CS.METHOD.003 (Lauber 2025) | Economic update | Current economic conditions |
| CS.METHOD.005 (this) | Higher granularity | Detailed program comparison |

---

## References

1. Giordano, J.O., Kalantari, A.S., Fricke, P.M., Wiltbank, M.C., & Cabrera, V.E. (2012). A daily herd Markov-chain model to study the reproductive and economic impact of reproductive programs combining timed artificial insemination and estrus detection. *Journal of Dairy Science*, 95(10), 5442-5460.

---

## Change Log

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-01 | Initial creation from Giordano 2012 analysis |

---

*Part of PACK-cattle-science*  
*Repository: https://github.com/StanisSerg/PACK-cattle-science*
