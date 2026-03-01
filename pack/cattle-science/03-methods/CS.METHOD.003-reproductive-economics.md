# CS.METHOD.003: Economic Evaluation of Reproductive Programs

> Method for determining optimal insemination eligibility period (IEP) and evaluating economic impact of reproductive decisions.

---

## Metadata

| Field | Value |
|-------|-------|
| **ID** | CS.METHOD.003 |
| **Domain** | cattle-science |
| **Area** | economics, reproduction |
| **Type** | Decision support method |
| **Status** | draft |
| **SoTA** | 2025-03-01 |
| **Sources** | [Lauber-2025], [Cabrera-2012], [Giordano-2012] |

---

## Purpose

Evaluate economic performance of dairy herd reproductive strategies to determine:
1. Optimal insemination eligibility period (IEP)
2. Most profitable semen type strategy
3. Economic value of improving 21-day pregnancy rate

---

## Key Parameters

### Input Parameters (Controllable)

| Parameter | Symbol | Range | Unit | Measurement |
|-----------|--------|-------|------|-------------|
| 21-day pregnancy rate | 21-d PR | 20-40 | % | (Service rate × P/AI) × 100 |
| Insemination eligibility period | IEP | 50-260 | days | From end of VWP |
| Semen type | — | Conv / Sexed+Beef | category | Strategic choice |
| Heifer survival rate | HSR | 75-90 | % | To first calving |
| Beef calf market value | — | 385-1,125 | $/calf | Market price |

### Output Parameters (Results)

| Parameter | Symbol | Unit | Interpretation |
|-----------|--------|------|----------------|
| Net return | NR | $/cow/year | Economic performance |
| Optimal IEP | — | days | IEP with maximum NR |
| Herd turnover rate | — | %/year | Replacement rate |
| Replacement sufficiency | — | yes/no | Can maintain herd size? |

### Reference Values: 21-day Pregnancy Rate

| Classification | 21-d PR | Interpretation |
|----------------|---------|----------------|
| Low | 20% | Poor performance, requires intervention |
| Below average | 25% | Below industry benchmark |
| Average | 30% | Industry standard (2020 US Holstein) |
| Above average | 35% | Good performance |
| High | 40% | Excellent performance |

---

## Method Steps

### Step 1: Assess Current Status

Measure or estimate current herd parameters:
- [ ] Calculate current 21-d PR from herd records
- [ ] Determine current semen usage (% conventional, % sexed, % beef)
- [ ] Estimate heifer survival rate
- [ ] Record current IEP policy

### Step 2: Define Scenarios

Define comparison scenarios:

**Scenario A: Conventional semen**
- All inseminations with conventional dairy semen
- Vary IEP: 80-170 days based on 21-d PR

**Scenario B: Sexed+Beef semen strategy**
- Nulliparous heifers: 75% sexed semen
- Primiparous/secondiparous: Sexed for 1st-2nd AI
- Remaining: Beef semen
- IEP: 200 days (typical optimal)

### Step 3: Calculate Economic Outcomes

For each scenario, calculate:

```
Net Return ($/cow/year) = 
    Milk Income
  + Calf Income (conventional or beef×dairy)
  - Semen Costs
  - Replacement Costs
  - Other Variable Costs
```

**Reference values (Lauber 2025):**
- Base NR (20% 21-d PR, conventional): baseline
- NR improvement (sexed+beef vs conventional): +$51/cow/year
- NR gain per 1% 21-d PR improvement: $2-7/cow/year

### Step 4: Determine Optimal IEP

Find IEP that maximizes NR while maintaining sufficient replacements:

| 21-d PR | Conventional Optimal IEP | Sexed+Beef Optimal IEP |
|---------|-------------------------|------------------------|
| 20% (Low) | 170 days | 200 days* |
| 25% (Below avg) | 150 days | 200 days* |
| 30% (Average) | 130 days | 200 days |
| 35% (Above avg) | 100 days | 200 days |
| 40% (High) | 80 days | 200 days |

*May require HSR ≥80% for sufficient replacements

### Step 5: Sensitivity Analysis

Test robustness of recommendation:
- [ ] Vary beef calf price (±$200)
- [ ] Vary heifer survival rate (±5%)
- [ ] Vary milk price (±10%)

### Step 6: Decision

Select strategy based on:
1. Maximum NR
2. Sufficient replacement availability
3. Risk tolerance (sensitivity results)

---

## Decision Algorithm

```
IF 21-d PR < 25% AND HSR < 80%:
    → Priority: Improve reproduction first
    → Consider conventional semen, longer IEP
    
ELSE IF 21-d PR ≥ 25% AND market conditions favorable:
    → Evaluate sexed+beef strategy
    → Optimal IEP = 200 days
    → Expected gain: $30-60/cow/year
    
ELSE IF maximizing genetic progress priority:
    → Use sexed semen for heifers and young cows
    → Beef semen for later lactations
    
ELSE:
    → Conservative: Conventional semen
    → Adjust IEP based on 21-d PR (80-170 days)
```

---

## Work Products

| Product | ID | Description |
|---------|-----|-------------|
| Reproduction Economic Assessment Report | CS.WP.003 | Full analysis with scenarios |
| IEP Recommendation Brief | CS.WP.003a | One-page decision support |
| Sensitivity Analysis Table | CS.WP.003b | Robustness testing results |

---

## Related Methods

| Method | Relationship |
|--------|--------------|
| CS.METHOD.001 | Protein norm calculation (feeding) |
| CS.METHOD.002 | Energy requirement assessment (feeding) |
| CS.METHOD.004 | Transition cow management (health) |

---

## Failure Modes

| Mode | Detection | Prevention |
|------|-----------|------------|
| Overestimating 21-d PR | Compare calculated vs. actual | Use 3-month rolling average |
| Ignoring replacement constraints | Monitor heifer inventory | Check HSR sufficiency |
| Static decision in dynamic market | Quarterly review | Update calf price assumptions |
| One-size-fits-all IEP | Herd-specific analysis | Calculate optimal, don't copy |

---

## References

1. Lauber, M.R., Cabrera, V.E., & Fricke, P.M. (2025). An economic simulation model to assess the effect of the 21-day pregnancy rate, semen type, and heifer survival rate on the optimal insemination eligibility period for lactating dairy cows. *Journal of Dairy Science*. https://doi.org/10.3168/jds.2025-27021

2. Cabrera, V.E. (2012). A simple formulation and solution to the replacement problem: A practical tool to assess the economic value of a cow. *Journal of Dairy Science*, 95(8), 4683-4693.

3. Giordano, J.O., et al. (2012). A daily herd Markov-chain model to study the reproductive and economic impact of reproductive programs. *Journal of Dairy Science*, 95(10), 6192-6207.

---

*Method created: 2026-03-01*  
*Based on: Lauber et al. (2025) analysis*  
*Review cycle: Annual or when major market changes occur*
