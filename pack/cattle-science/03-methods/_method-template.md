---
# TEMPLATE: Method Card (Unified)
# Domain: cattle-science
# Version: 1.0
# Based on: SPF _method-card-template.md + CS.METHOD.001/002/005 practice
# Purpose: Unified template covering both Phase-based (005) and Numbered (002) algorithm styles
# Usage: Copy to CS.METHOD.NNN-name.md, replace all placeholders
---

```yaml
---
id: CS.METHOD.NNN
name: "Method Name in Russian"
status: draft | active | deprecated
summary: "One sentence (≤150 chars) describing this method for index and retrieval."
sota: current | deprecated-interpretation | hypothesis
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
related:
  produces:
    - CS.WP.XXX
  uses:
    - CS.ENTITY.XXX
  fails_with:
    - CS.FM.XXX
  requires_role:
    - CS.ROLE.XXX
  precedes:
    - CS.METHOD.YYY
  follows:
    - CS.METHOD.ZZZ
tags:
  - domain-tag
  - method-type
---
```

## [CS.METHOD.NNN] Method Name

### Definition

One to three sentences describing what this method is. Focus on what it does, not how to do it. Declarative, not procedural.

### Purpose

- Why does this method exist?
- What problem does it address?
- What does it enable?

### Inputs

| Input | Description | Required? | Source |
|-------|-------------|-----------|--------|
| Input 1 | What it is | Yes / No | Source |

### Outputs (Work Products)

| Output | Link | Description |
|--------|------|-------------|
| CS.WP.XXX | [Name](../04-work-products/CS.WP.XXX-name.md) | Brief description |

### Roles Involved

| Role | Responsibility in This Method |
|------|------------------------------|
| [Role](../02-domain-entities/02A-roles.md#role) | R/A/C/I — what they do |

### Related Methods

| Method | Relationship |
|--------|--------------|
| [CS.METHOD.YYY](./CS.METHOD.YYY-name.md) | precedes / follows / parallel / alternative / component_of |

### Key Distinctions

- **Distinction 1**: Why it matters here. Be specific to this method.
- **Distinction 2**: Contrasts or boundaries essential for correct application.

### Failure Modes

| Failure Mode | Link | Description |
|--------------|------|-------------|
| Failure 1 | [CS.FM.XXX](../05-failure-modes/CS.FM.XXX-name.md) | Brief description |

### Tools Commonly Used

| Tool | How Used |
|------|----------|
| Tool 1 | Brief note |

### SoTA Status

**Status**: `current` | `deprecated-interpretation` | `hypothesis`

**Basis:**
- **Author et al. Year** (CS.SOTA.XXX) — what evidence supports this method.

**Revision criterion:**
- What would change this status?

---

## Algorithm: Method Name Protocol

> **Choose ONE of the two styles below based on method type:**
>
> **Style A — Phase-based** (preferred for multi-stage methods, monitoring, prevention)
> - Use when method spans multiple time periods or contexts
> - Tables for actions, parameters, thresholds
> - Example: CS.METHOD.005 (Transition Calcium Monitoring)
>
> **Style B — Numbered** (preferred for treatment protocols, single-event methods)
> - Use when method is a linear or branching protocol
> - Checklists `[ ]` for executable actions
> - Example: CS.METHOD.002 (Hypocalcemia Diagnosis and Treatment)

---

### Style A: Phase-based Algorithm

```markdown
### Phase 1: Phase Name (time range or condition)

**Step 1.1: Sub-step name**

| Parameter | Value | Action |
|-----------|-------|--------|
| Condition | Threshold | What to do |

**Step 1.2: Sub-step name**

| Parameter | Value | Action |
|-----------|-------|--------|
| Condition | Threshold | What to do |

### Phase 2: Phase Name (time range or condition)

**Step 2.1: Sub-step name**

| Parameter | Value | Action |
|-----------|-------|--------|
| Condition | Threshold | What to do |

### Phase 3: Follow-up / Herd-level

| Metric | Target | Action if above target |
|--------|--------|------------------------|
| Metric 1 | Target value | Response |
```

---

### Style B: Numbered Algorithm

```markdown
### 1. DEFINITION

**Term:** Definition of the condition or object.

**Sub-type A:** Criteria
**Sub-type B:** Criteria

### 2. PURPOSE

- Goal 1
- Goal 2

### 3. INDICATIONS

#### Mandatory screening:
- [ ] Criterion 1
- [ ] Criterion 2

#### Additional screening:
- [ ] Criterion 3

### 4. DIAGNOSIS / ASSESSMENT

#### 4.1 Primary method

**Technique:**
1. Step 1
2. Step 2
3. Step 3

| Result | Interpretation | Action |
|--------|----------------|--------|
| Range A | Normal | Monitor |
| Range B | Abnormal | Treat |

#### 4.2 Extended diagnostics (optional)

- [ ] Test 1
- [ ] Test 2

### 5. TREATMENT / INTERVENTION

#### 5.1 Protocol for condition A

**Goal:** What to achieve

**Step 1: Immediate action**
- [ ] Action 1
  - *Alternative:* Action 1b
- [ ] Action 2

**Step 2: Supportive therapy**
- [ ] Action 3
- [ ] Action 4

**Step 3: Monitoring**
- [ ] Control 1
- [ ] Control 2

#### 5.2 Protocol for condition B

- [ ] Action 1
- [ ] Action 2

### 6. PREVENTION

#### 6.1 Dietary measures
- [ ] Measure 1
- [ ] Measure 2

#### 6.2 Management measures
- [ ] Measure 3

### 7. METABOLIC CASCADE (if applicable)

```
Condition A
      ↓
Consequence B
      ↓
Consequence C
      ↓
Consequence D
```

**Actions:**
- [ ] Monitor for B
- [ ] Prevent C

### 8. EFFECTIVENESS CRITERIA

**Successful intervention:**
- [ ] Criterion 1
- [ ] Criterion 2

**Need for correction:**
- [ ] Warning sign 1
- [ ] Warning sign 2
```

---

## Checklist Before Committing

- [ ] ID follows pattern `CS.METHOD.NNN`
- [ ] Definition is declarative (not "Step 1: ...")
- [ ] Outputs link to work product cards
- [ ] Failure modes are listed
- [ ] SoTA status and revision criterion specified
- [ ] Algorithm uses ONE consistent style (Phase-based OR Numbered)
- [ ] All tables have headers and consistent column order
- [ ] All checklists use `[ ]` / `[x]` syntax (Numbered style only)
- [ ] Related methods specify relationship type (precedes/follows/parallel/alternative)
- [ ] Added to `02C-methods-index.md`
- [ ] Added to `07-map/` (if applicable)
- [ ] Failure mode links resolve correctly
- [ ] Work product links resolve correctly

---

*Template: CS.METHOD Unified v1.0*
*Created: 2026-05-22 (WP-83 Methods PACK)*
*Source: SPF _method-card-template.md + CS.METHOD.001/002/005 synthesis*
