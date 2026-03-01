# CS.METHOD.004: Economic Cow Value Assessment

> Simplified Markov-chain method for calculating economic value of individual cows.

---

## Metadata

| Field | Value |
|-------|-------|
| **ID** | CS.METHOD.004 |
| **Domain** | cattle-science |
| **Area** | economics, decision-support |
| **Type** | Assessment method |
| **Status** | active |
| **SoTA** | 2012-08-01 (foundational) |
| **Sources** | [Cabrera-2012] |

---

## Purpose

Calculate economic value of individual cows to support replacement decisions:
1. Should this cow be kept or culled?
2. What is the value of a new pregnancy?
3. What is the cost of a pregnancy loss?

---

## Key Parameters

### Input Parameters

| Parameter | Symbol | Unit | How to Determine |
|-----------|--------|------|------------------|
| Month in milk | MIM | months | Days since calving ÷ 30.4 |
| Pregnancy status | PREG | yes/no | Pregnancy check records |
| Month of pregnancy | MOP | months | If pregnant, gestation month |
| Expected production | EP | % of herd avg | Historical data, lactation curves |
| Genetic gain of replacement | GG | % | Sire selection, breeding goals |

### Output Parameters

| Parameter | Symbol | Unit | Interpretation |
|-----------|--------|------|----------------|
| Cow value | CV | $/cow | Economic value if kept |
| Pregnancy value | PV | $/pregnancy | Additional value from pregnancy |
| Pregnancy loss cost | PLC | $/loss | Economic cost of abortion |

---

## Method Steps

### Step 1: Gather Cow Data

Collect for target cow:
- [ ] Current MIM
- [ ] Pregnancy status (yes/no)
- [ ] If pregnant: month of pregnancy (1-9)
- [ ] Expected production (% of herd average)
- [ ] Parity (lactation number)

### Step 2: Calculate Base Cow Value

**Reference values (update for current economics):**

| Scenario | MIM | Status | Base CV (2012$) | Adjustment Method |
|----------|-----|--------|-----------------|-------------------|
| Open | 1 | Nonpregnant | $897 | Scale to current milk price |
| Open | 8 | Nonpregnant | $68 | Scale to current milk price |
| Pregnant | 3 | Pregnant | $889 | Scale to current milk price |
| Pregnant | 8 | Pregnant | $298 | Scale to current milk price |

**Scaling formula:**
```
Current CV = Base CV × (Current milk price / $18 per cwt) × (Current replacement cost / $1200)
```

*(Note: $18/cwt and $1200 are approximate 2012 reference values)*

### Step 3: Adjust for Expected Production

| Expected Production | Multiplier | Example |
|---------------------|------------|---------|
| 80% (poor) | 0.5-0.8 | Below-average cow |
| 100% (average) | 1.0 | Baseline |
| 120% (good) | 1.5-6.5 | High producer |

**Formula:**
```
Adjusted CV = Base CV × Production Multiplier
```

*Higher multipliers for pregnant cows in later lactations*

### Step 4: Adjust for Genetic Gain

```
GG Adjustment = -$211 × (GG% / 1%)

Where:
- GG% = Expected genetic improvement of replacement (%)
- $211 = 2012 value (scale to current)
```

**Current scaling:**
```
Current GG Adjustment = -$211 × (Current replacement cost / $1200) × (GG% / 1%)
```

### Step 5: Calculate Final Cow Value

```
CV = (Base CV × Production Multiplier) + GG Adjustment
```

### Step 6: Calculate Pregnancy Value (if open)

Compare CV(pregnant) - CV(open) at same MIM:

| MIM | Pregnancy Value (2012$) | Current$ Estimate |
|-----|------------------------|-------------------|
| 3 | $889 - $897 ≈ -$8 | Near zero early |
| Later | Increasing | Higher value |

**Rule of thumb:** Pregnancy adds $200-800 depending on timing

### Step 7: Calculate Pregnancy Loss Cost (if pregnant)

| Loss Timing | PLC (2012$) | Interpretation |
|-------------|-------------|----------------|
| Month 1 | $221 | Early loss |
| Month 9 | $897 | Late loss (≈ cow value) |

**Current scaling:**
```
Current PLC = PLC(2012) × (Current replacement cost / $1200)
```

### Step 8: Decision

| Comparison | Decision |
|------------|----------|
| CV(cow) > Replacement cost | Keep cow |
| CV(cow) < Replacement cost | Cull cow |
| Pregnant cow | Default = keep (higher value) |

---

## Decision Rules

### Rule 1: Pregnant Cows
```
IF pregnant:
    → Default decision = KEEP
    → Exception: Very late lactation + very low production + high genetic gain
```

### Rule 2: Open Cows
```
IF MIM < 5 AND EP > 100%:
    → Breed and keep
    
ELSE IF MIM 5-7 AND EP > 110%:
    → Breed and keep
    
ELSE IF MIM > 7 AND open:
    → Strong cull candidate
    → Calculate CV vs. replacement cost
    
ELSE IF EP < 80%:
    → Cull candidate regardless of MIM
```

### Rule 3: High Genetic Gain Context
```
IF GG > 2% per year:
    → Increase cull pressure on low producers
    → CV decreases by ~$400+ per cow
```

---

## Work Products

| Product | ID | Description |
|---------|-----|-------------|
| Individual Cow Value Report | CS.WP.004 | Per-cow assessment |
| Cull/Keep Recommendation List | CS.WP.004a | Herd-level decisions |
| Pregnancy Loss Risk Assessment | CS.WP.004b | Protect high-value pregnancies |

---

## Related Methods

| Method | Relationship |
|--------|--------------|
| CS.METHOD.003 | Extension to herd-level optimization |
| CS.METHOD.005 | Transition cow management (affects EP) |

---

## Historical Context

### 2012 Reference Economics
| Parameter | Value | Current Update Needed |
|-----------|-------|----------------------|
| Milk price | ~$18/cwt | Update to current |
| Replacement cost | ~$1,200 | Update to current |
| Cow values | 2012$ | Scale by inflation |

### Validation
- Results consistent with dynamic programming (Groenendaal et al. 2004)
- Widely adopted in research (Lauber 2025, Giordano 2012)
- Foundation for later herd-level models

---

## Failure Modes

| Mode | Detection | Prevention |
|------|-----------|------------|
| Outdated economics | CV seems unrealistic | Update prices quarterly |
| Overestimating EP | Actual < expected | Use 3-lactation average |
| Ignoring genetic gain | Slow genetic progress | Include GG in calculation |
| Static decision | Not recalculating | Review monthly for open cows |

---

## References

1. Cabrera, V.E. (2012). A simple formulation and solution to the replacement problem. *Journal of Dairy Science*, 95(8), 4683-4698.

2. Groenendaal, H., et al. (2004). An economic spreadsheet model to evaluate costs. *Journal of Dairy Science*, 87(7), 2146-2157.

---

*Method created: 2026-03-01*  
*Based on: Cabrera (2012)*  
*Note: Economic parameters require regular updating*
