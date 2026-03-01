# Ingestion Log: PACK-cattle-science

> Process artifact, NOT pack content. Information sources for analysis.

---

## Entry 001: Lauber et al. (2025)

**Material:** An economic simulation model to assess the effect of the 21-day pregnancy rate, semen type, and heifer management on the economic performance of dairy farms

**Authors:** Lauber et al.

**Year:** 2025

**Source Type:** Peer-reviewed research (simulation study)

**Date Ingested:** 2026-03-01

**Relevance:** 
- Directly addresses reproductive economics (core CS domain)
- Provides quantitative thresholds for decision-making
- Connects biological parameters (pregnancy rate) to economic outcomes

**Relevance Test:**
- [x] Within bounded context? YES (reproduction economics)
- [x] Relates to identified entities? YES (reproduction, economics)
- [x] Can be analyzed through distinctions? YES (D.003 Input/Output, D.005 Biological/Economic)

**Status:** analyzed

**Initial Notes:**
- Focus on 21-day pregnancy rate as key economic driver
- Compares semen types (conventional vs sexed vs beef)
- Heifer management strategies
- Simulation-based (not field trial)

**Priority:** High (recent, comprehensive, actionable)

---

## Entry 002: Cabrera (2012)

**Material:** A simple formulation and solution to the replacement problem: A practical tool to assess the economic value of a cow

**Author:** Cabrera, V.E.

**Year:** 2012

**Source Type:** Peer-reviewed research (decision support tool)

**Date Ingested:** 2026-03-01

**Relevance:** 
- Foundational economic model for cow replacement decisions
- Directly used in Lauber 2025 (cited as base model)
- Core CS domain (economics, decision support)

**Relevance Test:**
- [x] Within bounded context? YES (economics, replacement decisions)
- [x] Relates to identified entities? YES (cow value, replacement)
- [x] Can be analyzed through distinctions? YES (D.005 Biological/Economic)

**Status:** analyzed

**Initial Notes:**
- Simple formulation for replacement problem
- Practical tool for economic value assessment
- Foundation for later Markov models
- High citation value (used in Lauber 2025, Giordano 2012)

---

## Entry 003: Giordano et al. (2012)

**Material:** A daily herd Markov-chain model to study the reproductive and economic impact of reproductive programs

**Authors:** Giordano, J.O., et al.

**Year:** 2012

**Source Type:** Peer-reviewed research (simulation model)

**Date Ingested:** 2026-03-01

**Relevance:** 
- Concurrent development with Cabrera 2012 (similar methodology)
- Daily (vs monthly) Markov chain granularity
- Herd-level reproductive impact assessment
- Core CS domain (reproduction, economics, modeling)

**Relevance Test:**
- [x] Within bounded context? YES (reproduction, herd dynamics)
- [x] Relates to identified entities? YES (herd structure, reproduction)
- [x] Can be analyzed through distinctions? YES (D.004 Individual/Herd, D.007 Model/Reality)

**Status:** pending-analysis

**Initial Notes:**
- Daily Markov chain (higher granularity than Cabrera)
- Focus on herd-level reproductive programs impact
- Concurrent with Cabrera 2012 (both 2012, both Markov)
- Complementary: Cabrera = individual cow, Giordano = herd dynamics
- Cited in Lauber 2025

---

*Ingestion log maintained during Stage 05. Cleared after Stage 06 completion.*
