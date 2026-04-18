---
type: sota-synthesis-pack
cg_frame: PACK-cattle-science-decision-layer
domain: dairy-cattle-management
version: 0.1.0-draft
status: draft
g2_conformance: partial
---

# SoTA Synthesis Pack@CG-Frame: Decision Layer for Dairy Herd Management

> **CG-Frame:** Decision support in transition-cow health, metabolic screening, and group-level productivity management.
> **Pattern:** G.2 — SoTA Harvester & Synthesis (FPF)
> **Status:** Draft / Phase-1 seed. Explicit gaps marked `TBD`.

---

## 0. Scope Declaration (G.2:4.3 — Step 1)

```yaml
CG-FrameContext:
  primary_focus: "Transition-period decision support for dairy cattle (DIM -60 to +60)"
  secondary_focus: "Group-level productivity monitoring and metabolic risk screening"
  describedEntity:
    - GroundingHolon: "Holstein-Friesian dairy cow, commercial herd"
    - ReferencePlane: "Russian commercial dairy enterprise (ОАО МТК pilot)"
    - SecondaryPlane: "NASEM 2021 nutrient requirements, NRC 2001 baseline"

Tradition[] (initial set):
  - T1: Threshold-Based Expert Rules (veterinary protocols, clinical thresholds)
  - T2: Group-First Management (herd-level aggregation, group deviation models)
  - T3: Enterprise Data & Predictive Analytics (MilkBot curves, M305, farm data)
  - T4: NRC/NASEM Nutrition Standards (normative feeding requirements, energy/protein norms)

FamilyCoverageFloorK: 3
  # NOTE: Currently 4 Traditions declared. Need ≥3 distinct U.BoundedContext entries.
```

---

## G.2a — CorpusLedger

> Ledger of candidate sources with Context and triage status.

| LedgerId | Source | Type | Tradition | Context | Year | Triage | Rationale / Notes |
|----------|--------|------|-----------|---------|------|--------|-------------------|
| CS.SOTA.001 | Bruinjé 2024 | research-article | T1 / T4 | metabolic, reproduction | 2024 | **include** | Transition health, evidence-backed thresholds |
| CS.SOTA.002 | Galvão 2013 | research-article | T1 | metabolic | 2013 | **include** | Subclinical ketosis screening protocols |
| CS.SOTA.003–007 | NASEM 2021 chapters | book-chapter | T4 | feeding, nutrition | 2021 | **include** | Nutrient requirement standards, energy/protein norms |
| CS.SOTA.??? | MilkBot (Bo70) | method-family | T3 | productivity, lactation curves | 2015+ | **include** | Lactation curve fitting, M305 prediction |
| CS.ENTERPRISE.001 | ОАО МТК dataset | enterprise-data | T3 | herd-management, metabolic | 2024–2025 | **include** | 206 head, M305 avg 7901 kg, 31% metabolic risk |
| CS.SOTA.??? | Oetzel 2011 / McArt 2013 | review / research | T1 | metabolic | 2011 / 2013 | **park** | Classic hypocalcemia/ketosis protocols; need freshness check |
| CS.SOTA.??? | Precision Livestock Farming (PLF) reviews | review | T2 | monitoring, IoT | 2020+ | **park** | Group-level sensor monitoring; not yet integrated |

**Triage gaps (TBD):**
- [ ] Add FlowRecord tracing for `CS.SOTA.???` entries (currently missing explicit screening trail).
- [ ] Park/retire rationale for excluded sources (e.g., genetic selection papers, treatment protocols).

---

## G.2b — ClaimSheets[Tradition]

> Typed Claim Sheets per Tradition. **Preserved disjoint by default.** Cross-Tradition fusion only via BridgeMatrix + GammaEpistSynthId.

---

### ClaimSheet T1: Threshold-Based Expert Rules

```yaml
ClaimSheetId: CS.CLAIM.T1-THRESHOLD
Tradition: Threshold-Based Expert Rules (clinical veterinary protocols)
HomeContext: individual-cow transition management
DescribedEntity: Holstein cow, DIM 0–14, postpartum metabolic screening
EvidenceAnchors:
  - CS.SOTA.002 (Galvão 2013): BHB threshold for SCK detection
  - CS.SOTA.001 (Bruinjé 2024): transition health thresholds
  - Clinical protocols: Ca < 1.5 mmol/L → acute hypocalcemia emergency
FreshnessWindow: "2013–2024; Bruinjé 2024 considered current backbone"
RiskTrustCues:
  - BHB threshold 1.2 mmol/L: medium confidence (population-dependent)
  - Ca threshold 1.5 mmol/L: high confidence (clinical consensus)
KeyClaims:
  - K1: "BHB ≥ 1.2 mmol/L at DIM 3–14 indicates subclinical ketosis (SCK)"
  - K2: "Ca < 1.5 mmol/L in fresh cow → emergency IV calcium (override all rules)"
  - K3: "Urine pH 6.0–6.5 in close-up indicates adequate DCAD balance"
ValidityRegion:
  - Herd size: any
  - Breed: Holstein-Friesian (calibrated); Jersey/other → TBD
  - Geography: temperate climate; heat stress → see T2/T3
FailureModes:
  - FM1: False positive SCK (BHB 1.2–1.4 without metabolic deficit) → over-treatment
  - FM2: Missed hypocalcemia (subclinical, Ca 1.5–2.0) → delayed intervention
```

---

### ClaimSheet T2: Group-First Management

```yaml
ClaimSheetId: CS.CLAIM.T2-GROUP
Tradition: Group-First Management (herd-level aggregation models)
HomeContext: herd-level management, group deviation monitoring
DescribedEntity: Commercial dairy herd (≥100 head), lactating group
EvidenceAnchors:
  - CS.ENTERPRISE.001 (ОАО МТК): group deviation patterns, 206 head
  - PACK-cattle-science internal: group_models.py v1.0
FreshnessWindow: "2025; enterprise data current as of 2025-04"
RiskTrustCues:
  - Group average M305: high confidence (enterprise-backed)
  - Group deviation model: low confidence (v1.0, conceptual)
KeyClaims:
  - K1: "Group-level metabolic risk screening is more actionable than individual thresholds for large herds"
  - K2: "Deviation from group mean (BHB, DMI) predicts transition failure earlier than absolute thresholds"
ValidityRegion:
  - Herd size: ≥100 head (group statistics meaningful)
  - Data quality: requires DIM, BHB, DMI for ≥80% of cows
FailureModes:
  - FM1: Small groups (<50) → group mean unstable → false signals
  - FM2: Heterogeneous groups (mixed DIM, parity) → confounded deviation
```

---

### ClaimSheet T3: Enterprise Data & Predictive Analytics

```yaml
ClaimSheetId: CS.CLAIM.T3-PREDICTIVE
Tradition: Enterprise Data & Predictive Analytics (MilkBot, M305, herd data)
HomeContext: commercial enterprise data analysis, predictive productivity modeling
DescribedEntity: Lactating Holstein cow / herd, Russian commercial farm
EvidenceAnchors:
  - CS.ENTERPRISE.001 (ОАО МТК): 206 head, avg M305 7901 kg, 60 cows in metabolic risk
  - MilkBot (Bo70): a=54.5, b=33, c=5, d=0.0025 (extracted from Пример 3.csv)
  - CS.WP.002 / CS.WP.003: productivity and metabolism reports
FreshnessWindow: "2024–2025; MilkBot curve parameters pinned to Пример 3.csv edition"
RiskTrustCues:
  - M305 average: high confidence (enterprise data)
  - MilkBot curve fit: medium confidence (single herd extraction; needs cross-validation)
  - Metabolic risk 31%: medium confidence (depends on BHB sampling frequency)
KeyClaims:
  - K1: "Herd-level MilkBot curve (a=54.5, b=33, c=5, d=0.0025) characterizes lactation shape for this enterprise"
  - K2: "31% of cows in metabolic risk (BHB + Ca combined) indicates suboptimal transition management"
  - K3: "Absence of DIM < 35 data blocks early ketosis screening (critical data gap)"
ValidityRegion:
  - Enterprise: ОАО МТК (206 head, tied housing, TMR feeding)
  - Breed: Holstein-Friesian
  - Season: data collected 2024–2025 (winter-spring bias possible)
FailureModes:
  - FM1: Missing DIM < 35 data → early lactation underrepresented
  - FM2: Single-enterprise fit → overfitting to local conditions
  - FM3: No causal model; correlations only
```

---

### ClaimSheet T4: NRC/NASEM Nutrition Standards

```yaml
ClaimSheetId: CS.CLAIM.T4-NUTRITION
Tradition: NRC/NASEM Nutrition Standards (normative requirement models)
HomeContext: ration formulation, energy/protein requirement calculation
DescribedEntity: Holstein cow by parity and DIM, US/EU reference populations
EvidenceAnchors:
  - CS.SOTA.003–007 (NASEM 2021): energy requirements, protein norms
  - NRC 2001: baseline nutrient requirements
FreshnessWindow: "NASEM 2021 current; NRC 2001 legacy backbone"
RiskTrustCues:
  - NASEM energy requirements: high confidence (consensus standard)
  - Direct applicability to Russian conditions: medium confidence (feed composition differs)
KeyClaims:
  - K1: "NASEM 2021 energy requirements provide normative baseline for ration evaluation"
  - K2: "Prepartum DCAD manipulation (urine pH target 6.0–6.5) reduces hypocalcemia incidence"
ValidityRegion:
  - Geography: primarily US/EU calibrated; Russian feed tables need cross-calibration
  - Breed: Holstein-Friesian
  - Production level: high-input systems (≥8000 kg M305)
FailureModes:
  - FM1: Direct translation without local feed analysis → systematic error
  - FM2: NASEM assumes TMR; pasture-based systems → different norms
```

---

## G.2c — OperatorAndObjectInventory

> Candidate CHR terms and CAL operator stubs for downstream authoring.
> **All entries are stubs unless explicitly marked lawful.**

| InventoryId | Term / Operator | Kind | Proposed CHR Type | Owner (TBD) | Status | Notes |
|-------------|-----------------|------|-------------------|-------------|--------|-------|
| INV-001 | BHB (beta-hydroxybutyrate) | characteristic | Concentration (mmol/L) | T1 / T3 | stub | Threshold 1.2; population-dependent |
| INV-002 | Ca (total calcium) | characteristic | Concentration (mmol/L) | T1 | stub | Emergency < 1.5; subclinical 1.5–2.0 |
| INV-003 | DIM (days in milk) | coordinate | Integer days | T1–T4 | stub | Temporal anchor for all rules |
| INV-004 | DMI (dry matter intake) | characteristic | Mass (kg/day) | T1 / T4 | stub | Ratio DMI_actual/DMI_norm used in RULE-001 |
| INV-005 | M305 (305-day milk yield) | characteristic | Mass (kg) | T3 | stub | Herd avg 7901 kg (ОАО МТК) |
| INV-006 | MilkBot curve parameters | operator-family | Lactation model | T3 | stub | a=54.5, b=33, c=5, d=0.0025 |
| INV-007 | Group mean deviation | operator | Ratio / Z-score | T2 | stub | Group-level aggregation; threshold TBD |
| INV-008 | NEL (net energy lactation) | characteristic | Energy (Mcal/kg) | T4 | stub | NASEM 2021 normative |
| INV-009 | DCAD (dietary cation-anion difference) | characteristic | mEq/kg | T4 | stub | Prepartum manipulation target |
| INV-010 | BCS (body condition score) | characteristic | Ordinal 1–5 | T1 / T4 | stub | Visual / ultrasound assessment |

**TBD:** Legality discipline (A.17–A.19 / C.16) for each stub; threshold semantics deferred to G.4 (CAL).

---

## G.2d — BridgeMatrix

> Alignment / divergence surface across Tradition × Tradition.

| From \ To | T1 Threshold | T2 Group-First | T3 Predictive | T4 Nutrition |
|-----------|--------------|----------------|---------------|--------------|
| **T1 Threshold** | — | ⚠️ Scale conflict: individual vs group | ⚠️ Temporal: thresholds static, MilkBot dynamic | ✅ Compatible: thresholds inform ration adjustments |
| **T2 Group-First** | ⚠️ Scale conflict | — | ✅ Complementary: group mean + individual deviation | ⚠️ Context: nutrition norms assume individual intake, not group statistics |
| **T3 Predictive** | ⚠️ Temporal / causal | ✅ Complementary | — | ⚠️ Feed-to-yield gap: NASEM norms vs actual M305 |
| **T4 Nutrition** | ✅ Compatible | ⚠️ Context | ⚠️ Feed-to-yield gap | — |

**Explicit Loss Notes:**
- **T1 ↔ T2 (Scale):** T1 thresholds (BHB ≥1.2) apply to individual cows; T2 group deviation applies to herd mean. A cow with BHB 1.1 may be "normal" by T1 but "group outlier" by T2 if group mean is 0.8. **Loss:** T1 misses early group-level signals; T2 may flag healthy individuals in high-risk groups.
- **T1 ↔ T3 (Temporal):** T1 uses single-point BHB; T3 uses MilkBot curve trajectory. A cow with BHB 1.0 at DIM 7 but declining M305 may be at risk by T3 but not flagged by T1. **Loss:** T1 lacks trajectory information.
- **T3 ↔ T4 (Feed-to-yield):** NASEM predicts required intake for target M305; actual M305 (T3) may diverge due to management, not nutrition. **Loss:** attributing yield gap to nutrition vs non-nutritional factors.

**Crossings:**
- No explicit `GammaEpistSynthId` records emitted yet (no fusion/substitution asserted). BridgeMatrix records parallel divergent claims only.

---

## G.2e — MicroExamples

> Worked micro-examples for load-bearing claims.

### ME-001: BHB Threshold + Group Deviation Conflict

```yaml
MicroExampleId: ME-001
ClaimSheetRefs: [CS.CLAIM.T1-THRESHOLD, CS.CLAIM.T2-GROUP]
DescribedEntity: Holstein cow, DIM 5, herd size 206 (ОАО МТК)
Context: Postpartum metabolic screening
Substrate:
  - Cow A: BHB = 1.1 mmol/L (T1: NOT_TRIGGERED)
  - Group mean BHB (DIM 3–14): 0.8 mmol/L, σ = 0.15
  - Cow A deviation: +2.0σ (T2: flagged as outlier)
Outcome:
  - T1: No intervention
  - T2: Recommend monitoring / early re-check
AssuranceTag: VA (validity argument)
A10Anchors: [CS.ENTERPRISE.001, CS.CLAIM.T2-GROUP.K2]
LossNote: "T1 optimizes for clinical action; T2 optimizes for early signal. No single 'correct' answer without declared decision frame (G.5)."
```

### ME-002: MilkBot Curve + NASEM Norm Gap

```yaml
MicroExampleId: ME-002
ClaimSheetRefs: [CS.CLAIM.T3-PREDICTIVE, CS.CLAIM.T4-NUTRITION]
DescribedEntity: Holstein cow, parity 2, DIM 60, M305 target 8500 kg
Context: Ration evaluation vs actual production
Substrate:
  - NASEM 2021: Required NEL = 1.75 Mcal/kg for target M305 8500 kg
  - Actual DMI: 22 kg/day; actual M305 trajectory (MilkBot): falling below predicted
  - Group avg M305 (ОАО МТК): 7901 kg (below target)
Outcome:
  - T4: Ration is adequate by normative standard
  - T3: Actual production lower than predicted; possible non-nutritional cause (management, disease, genetics)
AssuranceTag: LA (legality argument — NASEM norms lawful, but attribution requires additional evidence)
A10Anchors: [CS.SOTA.003–007, CS.ENTERPRISE.001]
LossNote: "Attribution gap: NASEM predicts 'what should be' under ideal conditions; MilkBot describes 'what is'. Bridge requires explicit causal model (not yet in pack)."
```

**TBD:** Add ≥2 more micro-examples on heterogeneous substrates (e.g., Jersey breed, pasture-based system, smallholder <50 head).

---

## G.2f — UTSProposals

> Draft Name Cards + MDS for public ids.

| ProposalId | Proposed Name | Kind | Scope | Status |
|------------|---------------|------|-------|--------|
| UTS-TBD-001 | `CS.ENTITY.BHB-THRESHOLD-TRANSITION` | Name Card | BHB threshold for SCK, DIM 3–14 | draft |
| UTS-TBD-002 | `CS.METHOD.GROUP-DEVIATION-METABOLIC` | Name Card | Group-first metabolic deviation | draft |
| UTS-TBD-003 | `CS.PACK.MILKBOT-ENTERPRISE-v1` | MDS | MilkBot params for ОАО МТК | draft |

**TBD:** MDS content, alias docking, concept-set linkage.

---

## G.2g — describedEntity Map

> Mapping key terms to GroundingHolon + ReferencePlane.

| Term / ClaimFamily | GroundingHolon | ReferencePlane | ClaimSheetId | EvidenceAnchors |
|--------------------|----------------|----------------|--------------|-----------------|
| BHB ≥ 1.2 (SCK) | Holstein cow, DIM 3–14, individual | Clinical veterinary practice | CS.CLAIM.T1-THRESHOLD | CS.SOTA.002, CS.SOTA.001 |
| Group deviation (BHB) | Holstein herd, ≥100 head, lactating group | Enterprise management (ОАО МТК) | CS.CLAIM.T2-GROUP | CS.ENTERPRISE.001 |
| MilkBot curve | Holstein cow, parity 2+, lactation curve | ОАО МТК dataset | CS.CLAIM.T3-PREDICTIVE | CS.ENTERPRISE.001 |
| NEL requirement | Holstein cow, target M305 ≥8000 kg | NASEM 2021 reference population | CS.CLAIM.T4-NUTRITION | CS.SOTA.003–007 |
| Ca < 1.5 emergency | Holstein cow, DIM 0–3, fresh | Clinical emergency protocol | CS.CLAIM.T1-THRESHOLD | Clinical consensus (TBD: A.10 anchor) |

---

## G.2h — PRISMA Flow Record

> Screening / eligibility trail.

```yaml
FlowRecordId: CS.FLOW.G2-001
HarvestPolicyRef: TBD (no explicit policy pinned yet)
InclusionCriteriaId: TBD
ScreeningRubricId: TBD

Stages:
  1. Identification:
     - Seed sources: PACK-cattle-science existing SoTA (Bruinjé, Galvão, NASEM)
     - Expansion: citation chaining → TBD (not performed)
     - Enterprise data: provided by farm veterinarian (ОАО МТК)
  2. Screening:
     - Excluded: genetics, treatment protocols, construction (per domain contract)
     - Included: metabolic, feeding, reproduction, management
  3. Eligibility:
     - Post-2015 preference: partially met (Galvão 2013 is pre-2015; kept as backbone)
     - Language: Russian / English
  4. Included:
     - SoTA annotations: 5+ (per WORKPLAN Phase A)
     - Enterprise datasets: 1 (ОАО МТК)
     - Method families: MilkBot

Gaps:
  - No formal PRISMA diagram
  - No explicit inclusion/exclusion rubric
  - Citation chaining incomplete
```

---

## G.2i — SoSIndicatorFamilies

> Indicators as variants with Acceptance branches.

| FamilyId | Indicator Family | Variants | Acceptance Branches | Notes |
|----------|------------------|----------|---------------------|-------|
| IND-FAM-001 | Metabolic Risk Indicator | V1: BHB single-point (threshold 1.2) | Branch-A: clinical_action; Branch-B: monitor | T1-owned |
| IND-FAM-001 | Metabolic Risk Indicator | V2: BHB group-deviation (+2σ) | Branch-A: early_signal; Branch-B: false_positive_risk | T2-owned |
| IND-FAM-001 | Metabolic Risk Indicator | V3: Combined BHB + Ca + DMI ratio | Branch-A: multi-factor_alert; Branch-B: incomplete_data | T1/T3 hybrid |
| IND-FAM-002 | Productivity Indicator | V1: M305 (actual) | Branch-A: target_met; Branch-B: below_target | T3-owned |
| IND-FAM-002 | Productivity Indicator | V2: MilkBot predicted M305 | Branch-A: trajectory_ok; Branch-B: declining | T3-owned |
| IND-FAM-003 | Nutrition Adequacy | V1: DMI_actual / DMI_NASEM | Branch-A: adequate; Branch-B: deficit | T4-owned |

**Anti-pattern check:** No single scalar "herd health score" asserted. Families remain set-returning.

---

## G.2j — MethodFamilyCards

| CardId | Method Family | Signature | Validity Region | Failure Modes | Wiring Stubs for G.5 |
|--------|---------------|-----------|-----------------|---------------|----------------------|
| MF-001 | Threshold-Based Screening | `f(cow_params) → {TRIGGERED, GRAY_ZONE, NOT_TRIGGERED}` | Individual cow, DIM-specific | FM1: population drift; FM2: false positive | Eligibility: DIM ∈ window; Assurance: medium |
| MF-002 | Group-First Evaluation | `f(herd_params) → {OUTLIER, NORMAL, INSUFFICIENT_DATA}` | Herd ≥100 head, homogeneous groups | FM1: small groups; FM2: confounded groups | Eligibility: n≥20 per group; Assurance: low |
| MF-003 | MilkBot Curve Fitting | `f(DIM, yield_records) → {a, b, c, d}` | Lactating cow, ≥5 yield records | FM1: early lactation underfit; FM2: outliers | Eligibility: DIM ≥ 5; Assurance: medium |
| MF-004 | NASEM Ration Evaluation | `f(ration_composition, cow_params) → {adequate, deficit, excess}` | TMR-fed, high-production Holstein | FM1: non-TMR systems; FM2: local feed tables | Eligibility: feed analysis available; Assurance: high |

---

## G.2k — GeneratorFamilyCards

| CardId | Generator Family | Validity Region | Transfer Hooks |
|--------|------------------|-----------------|----------------|
| GEN-001 | `generate_enterprise_reports.py` | ОАО МТК data format | CSV input → markdown output; extensible to other farms via `enterprise_loader.py` |
| GEN-002 | `run_group_case.py` / `evaluate_group_case.py` | Group-model v1.0 | YAML case → decision → evaluation; batch mode TBD |

---

## G.2l — Annexes

### Annex A: Data Gaps & Blockers (informative)

| Gap | Impact | Proposed Resolution |
|-----|--------|---------------------|
| DIM < 35 missing in enterprise data | Blocks early ketosis screening | Request expanded dataset from ОАО МТК |
| No cross-herd validation | T3 overfitting risk | Partner with 2nd farm for external validation |
| No explicit causal model (T3↔T4) | Attribution ambiguity | Add structural model or CAL workflow (G.4) |
| No PLF sensor data (T2) | Group-first lacks real-time signal | Park until sensor integration available |

### Annex B: G.2-F (GammaEpistSynthesis) Status

> `GammaEpistSynthId[]`: **None emitted.**
>
> No cross-Tradition fusion/substitution asserted in this draft. All crossings recorded as parallel divergent claims in BridgeMatrix only.
>
> If future work asserts (e.g.) "group deviation replaces individual BHB threshold", MUST emit `GammaEpistSynthId` with provenance union + alignment refs.

---

## SoTAPaletteDescription

```yaml
SoTAPaletteDescriptionId: CS.PALETTE.DL-v0.1
SoTA_SetId: CS.SET.DL-TRANSITION-HEALTH

Bindings:
  SoTA_Set@CG-Frame: "Transition-period decision support: metabolic screening + productivity monitoring"
  ClaimSheetIds: [CS.CLAIM.T1-THRESHOLD, CS.CLAIM.T2-GROUP, CS.CLAIM.T3-PREDICTIVE, CS.CLAIM.T4-NUTRITION]
  OperatorAndObjectInventoryId: INV-001..INV-010
  BridgeMatrixId: CS.BRIDGE.DL-v0.1
  MicroExampleIds: [ME-001, ME-002]
  MethodFamilyCardIds: [MF-001, MF-002, MF-003, MF-004]
  GeneratorFamilyCardIds: [GEN-001, GEN-002]
  SoSIndicatorFamilyIds: [IND-FAM-001, IND-FAM-002, IND-FAM-003]
  DescribedEntityMapId: CS.DEMAP.DL-v0.1
  FlowRecordId: CS.FLOW.G2-001

ConsumableSurfaces:
  - G.3 handoff: "CHR stubs for BHB, Ca, DIM, DMI, M305, MilkBot params, group deviation"
  - G.4 handoff: "Acceptance branch scaffolding for IND-FAM-001/002/003; threshold semantics TBD"
  - G.5 handoff: "MethodFamily cards with eligibility predicates; portfolio set-return discipline"
```

---

## Conformance Checklist (CC-G2) — Self-Assessment

| CheckId | Status | Notes |
|---------|--------|-------|
| CC-G2-CoreRef | ⚠️ partial | G.Core linkage manifest present; some pins TBD |
| CC-G2-Pluralism-1 | ✅ pass | 4 Traditions declared; ≥3 BoundedContexts (metabolic, feeding, management) |
| CC-G2-Ledger-1 | ⚠️ partial | CorpusLedger exists; explicit triage rationale incomplete |
| CC-G2-FlowRecord-1 | ❌ gap | FlowRecord seeded but lacks formal rubric and PRISMA diagram |
| CC-G2-ClaimSheets-1 | ✅ pass | 4 ClaimSheets, disjoint by default, evidence anchors declared |
| CC-G2-Palette-1 | ✅ pass | SoTA_Set and SoTAPaletteDescription exported |
| CC-G2-describedEntityMap-1 | ✅ pass | Map exists, ties claims to holons/planes |
| CC-G2-Alignment-1 | ✅ pass | BridgeMatrix records divergence; no silent fusion |
| CC-G2-GammaSynth-1 | ✅ pass | No fusion asserted; explicitly stated |
| CC-G2-Inventory-1 | ✅ pass | OperatorAndObjectInventory present |
| CC-G2-Inventory-2 | ✅ pass | All entries marked stubs; no shadow CHR/CAL |
| CC-G2-MicroExamples-1 | ⚠️ partial | 2 micro-examples; need ≥2 more on heterogeneous substrates |
| CC-G2-UTS-1 | ⚠️ partial | Proposals drafted; no public ids minted yet |
| CC-G2-Families-1 | ✅ pass | Indicators represented as families/variants with branches |
| CC-G2-HandOff-1 | ⚠️ partial | Hand-off manifests described; not yet wired to G.3/G.4/G.5 |
| CC-G2-CoverageGate-1 | ⚠️ partial | k=3 declared; not yet enforced as automated gate |
| CC-G2-RSCR-1 | ❌ gap | RSCRTriggerKindIds not yet wired to automated refresh |

---

## Next Steps (to reach G.2 conformance)

1. **Pin FlowRecord:** Add explicit `HarvestPolicyRef`, `InclusionCriteriaId`, `ScreeningRubricId`.
2. **Complete CorpusLedger:** Expand citation chaining; add 2–3 competing PLF sources for T2.
3. **Add MicroExamples:** ≥2 more on heterogeneous substrates (Jersey, pasture, smallholder).
4. **Mint UTS ids:** Publish Name Cards for key terms (BHB-threshold-transition, group-deviation-metabolic).
5. **Wire RSCR:** Add typed trigger causes for edition/policy changes.
6. **Hand-off to G.3/G.4/G.5:** Produce explicit `CHR-handoff`, `CAL-handoff`, `Registry-handoff` manifests.

---

*Pack-local ids pinned. Created: 2026-04-18 (G.2 synthesis draft).*
*Owner: PACK-cattle-science / WP-93 (Decision Layer).*
