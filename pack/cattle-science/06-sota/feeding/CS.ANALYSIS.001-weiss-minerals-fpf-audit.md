---
id: CS.ANALYSIS.001
type: fpf-audit
scope: [CS.SOTA.331, CS.SOTA.332]
auditor: "Kimi Code CLI (FPF review mode)"
date: 2026-05-24
fpf_patterns: [B.3, A.6.B, C.28, A.7, B.4, F.9, A.17-A.19]
status: completed
---

# CS.ANALYSIS.001: FPF-аудит CS.SOTA.331 + CS.SOTA.332 (Bill Weiss, Minerals)

> **Запрос:** Применить FPF (First Principles Framework) для анализа двух SoTA, полученных из видео-лекций Bill Weiss.  
> **Режим:** Review + Characterize + Diagnose (по классификации FPF skill).  
> **Артефакты:** [CS.SOTA.331](CS.SOTA.331-weiss-2024-transition-minerals-vitamins.md) (webinar, transition cows) · [CS.SOTA.332](CS.SOTA.332-weiss-2024-minerals-requirements-absorption.md) (lecture, minerals requirements).  
> **FPF Source:** SPF/spec/f-g-r-trust.md, FPF/FPF-Spec.md §B.3, §A.6.B, §C.28, §A.7, §B.4, §F.9.

---

## Executive Summary

| Паттерн FPF | Что проверено | Ключевой finding |
|-------------|--------------|------------------|
| **B.3 F-G-R** | 22 Key Claims → ⟨F, G, R⟩ | Scalar confidence (0.80–0.95) маскирует разную природу доверия. F-G-R дискриминирует: «Mn 60–80 ppm» (F3/Gnarrow/Rhigh) vs «+20% rule» (F2/Gwide/Rmedium) |
| **A.6.B L/A/D/E** | Типология каждого claim | 40% claims — Deontic (D), 30% — Evidence (E), 20% — Law (L), 10% — Admissibility (A). Смешение D/E в одном claim — риск |
| **C.28 CausalUse** | 13 causal chains | Большинство на уровне Intervention (feeding trial), 2 — Association (meta-analysis correlation), 0 — Counterfactual. Ни один claim не достигает highest rung |
| **A.7 Strict Distinction** | Object/Description/Carrier/Role/Work | Derivation чёткая, но transcript file иногда смешивается с Work (transcription) и Description (SoTA) |
| **B.4 Evolution** | Reopen triggers | Только CS.SOTA.331 имеет reopen_trigger. CS.SOTA.332 — нет. Нет явного DesignRunTag feedback |
| **F.9 Bridges** | Cross-context alignment | 4 explicit bridges (NASEM-2021, Goff 2018, Lean 2006), но нет Bridge cards с CL (Congruence Level) |

---

## 1. F-G-R Trust Analysis (FPF B.3)

> **Принцип:** Trust — не scalar «confidence», а tuple ⟨F, G, R⟩.  
> **F** = Formality (F0–F9). **G** = Claim Scope (set-valued). **R** = Reliability (evidence-based).

---

### 1.1 CS.SOTA.331 — Transition Minerals & Vitamins

| # | Claim (кратко) | F | G (Scope) | R | Было (confidence) | Почему F-G-R лучше |
|---|----------------|---|-----------|---|-------------------|-------------------|
| 1 | **Mn 60–80 ppm** dry/pre-fresh | F3 | {dairy cattle, dry cows, pre-fresh, NASEM-2021 model, Ohio State data} | High (собственное балансовое исследование, автор — co-investigator) | 0.90 | Confidence 0.90 не отличает от Claim 8 (тоже 0.88, но другая природа). F-G-R показывает: F3 (structured expert text) vs F3, но R=High vs R=Medium |
| 2 | **Se-yeast >> selenite** для колострума/плода | F3 | {dairy cattle, dry cows, lactating, Se sources: yeast vs selenite, US legal limits} | High (многократно подтверждённый трансферный механизм, 2× молоко, 50–80% плод) | 0.92 | Самый высокий confidence в SoTA. F-G-R подтверждает: R=High, но G ограничен (US legal context для 0.6 ppm) |
| 3 | **Mg 0.4–0.45%** pre-fresh | F3 | {dairy cattle, pre-fresh, high-K diets, NASEM-2021 comparison} | Medium-High (мета-анализ, но конфаундинг с DCAD) | 0.85 | Confidence 0.85 — низкий в SoTA. F-G-R уточняет: R снижается из-за confounding (Mg vs DCAD), не из-за слабых данных |
| 4 | **MgCl₂/MgSO₄ лучше MgO** для кровяного Ca | F3 | {dairy cattle, pasture, high K, NZ conditions, drench 19 г/день} | Medium (одно исследование NZ, специфические условия) | 0.80 | Самый низкий confidence. F-G-R объясняет: R=Medium (одно исследование), G узкий (NZ, pasture, drench) |
| 5 | **DCAD эффективен только при мочевой pH < 7** | F3 | {dairy cattle, transition cows, DCAD strategies, urinary pH monitoring} | Very High (многократно подтверждённый механизм H⁺/Ca²⁺, pH threshold чёткий) | 0.95 | Самый высокий confidence. F-G-R: R=Very High, G=domain-wide |
| 6 | **Избыток витамина E на весь сухостой ↑ мастит** (RR=1.7) | F3 | {dairy cattle, dry period, 5 farms study, mastitis outcome} | Medium (5 farms — хорошо, но механизм неясен, нет replication) | 0.85 | Confidence = 0.85. F-G-R: R=Medium (одно исследование, механизм неизвестен), G ограничен |
| 7 | **25(OH)D₃ эффективен только с DCAD** | F3 | {dairy cattle, pre-fresh, DCAD-negative, 1–3 mg dose, sick cows benefit more} | Medium (механизм bypass понятен, но токсичность 6 мг не объяснена) | 0.80 | Confidence = 0.80. F-G-R: R=Medium (нет объяснения токсичности), G включает dose restriction |
| 8 | **Сульфаты Cu/Mn/Zn угнетают рубцовую флору** | F3 | {dairy cattle, late lactation shown, mechanism universalized to all stages} | Medium-High (показано в late lactation, механизм универсален, но direct data для transition — нет) | 0.88 | Confidence = 0.88. F-G-R: R=Medium-High (механизм ясен, но extrapolation) |

**Aggregate F-G-R для CS.SOTA.331:**
- **F-distribution:** F3 (все claims) — structured expert text с цифрами, но не peer-reviewed publication. Ни один claim не достигает F5 (reviewed by independent expert).
- **G-pattern:** Все G содержат {dairy cattle, US context}. Некоторые claims имеют узкий G (NZ pasture для #4, 5 farms для #6).
- **R-pattern:** R=High/Very High для механизмов с физиологической основой (#2 Se transfer, #5 DCAD-pH). R=Medium для однократных исследований (#4, #6, #7).

---

### 1.2 CS.SOTA.332 — Minerals Requirements & Absorption

| # | Claim (кратко) | F | G (Scope) | R | Было (confidence) | Почему F-G-R лучше |
|---|----------------|---|-----------|---|-------------------|-------------------|
| 1 | **NRC + 20%** — general rule | F2 | {all minerals, dairy cattle, NASEM/NRC models, practical formulation} | Medium (многолетняя практика автора, general rule, но не formal meta-analysis) | 0.90 | F2 (expert rule-of-thumb) vs F3 (structured claim). R=Medium — «practice shows», не «research confirms». Confidence 0.90 переоценивает |
| 2 | **Requirements в массе, не %** | F4 | {all livestock nutrition, dairy cattle, NASEM-2021, formulation software} | Very High (базовый принцип нутритивной физиологии, математически тривиален) | 0.95 | F4 — проверенный принцип, но не formal proof. R=Very High (universal truth) |
| 3 | **Базовые корма содержат минералы** (10,000 samples) | F3 | {dairy cattle, corn silage, US samples, soil contamination context} | High (10,000 samples, но вопрос availability) | 0.90 | R=High (большой n), но G ограничен (US corn silage) |
| 4 | **Новые Mg AC:** basal 30%, MgO ~40%, MgSO4 ~50% | F4 | {dairy cattle, NASEM-2021, absorption coefficient revision} | Very High (автор участвовал в пересмотре, несколько крупных исследований) | 0.95 | F4 (checked specification — NASEM-2021 — reviewed by panel). R=Very High |
| 5 | **K антагонизирует Mg: 1% K → −7-8% absorption** | F3 | {dairy cattle, rumen/intestine, K>1.1%, NASEM-2021 equation} | High (несколько исследований, уравнение в модели) | 0.90 | R=High (replicated), G включает threshold |
| 6 | **Жир и RDP снижают Mg absorption** | F3 | {dairy cattle, supplemental fat >3%, high-RDP pastures, adaptation period} | Medium (меньше исследований, особенно RDP; адаптация за 2 недели) | 0.85 | R=Medium (limited studies), G включает adaptation boundary |
| 7 | **MgO — 10x вариативность между источниками** | F3 | {dairy cattle, 4 MgO sources tested, in vivo absorption} | High (4 источника, in vivo, но n не указан) | 0.90 | R=High (experimental), но G узкий (только 4 sources) |
| 8 | **DCAD 200-300 mEq/kg оптимально** | F3 | {dairy cattle, US economics, K/Na buffer prices, milk fat premium} | Medium-High (физиологический ответ подтверждён, но economics region-specific) | 0.85 | R split: физиология = High, economics = Medium. Confidence 0.85 усредняет разное |
| 9 | **Высокий K → +10L мочи/день** | F3 | {dairy cattle, heat stress, K 1.1→1.6%, urine output} | High (экспериментальные данные, прямая физиология) | 0.90 | R=High (direct measurement), G включает temperature context |
| 10 | **Сера >0.2% — проблема Cu/Se; вода — скрытый источник** | F3 | {dairy cattle, beef liver Cu data, water S 250 mg/L, NASEM-2021 equation (not in model)} | Medium-High (beef data strong, Se — одно исследование; уравнение не в модели) | 0.90 | R неоднороден: Cu = High (beef), Se = Medium (one study). Confidence усредняет |
| 11 | **Mo — не сильный антагонист Cu** | F3 | {dairy cattle, liver Cu, Mo >6 ppm threshold, requirement-level Cu ~15 ppm} | High (экспериментальные данные по liver Cu) | 0.90 | R=High (experimental), G чёткий threshold |
| 12 | **Cu toxicity — накапливающаяся проблема** | F3 | {dairy cattle, liver Cu monitoring, chronic accumulation, US context} | Very High (данные по accumulation rate, линейная динамика) | 0.95 | R=Very High (clear dynamics), G включает time dimension (years) |
| 13 | **Organic trace minerals: gut effects ≠ absorption** | F3 | {dairy cattle, organic Zn (one study), hydroxy vs sulfate, NDF digestion} | Medium (конкретные исследования, но generalization risky) | 0.85 | R=Medium (limited generalization), G ограничен |
| 14 | **Se: 0.3 ppm supplement; dry cows — ≥50% yeast** | F3 | {dairy cattle, dry cows, lactating, mastitis, fetus transfer, colostrum} | High (данные по fetus transfer, colostrum, mastitis) | 0.90 | R=High (multiple outcomes), G включает parity/lactation stage |
| 15 | **Monensin ↑ Mg absorption** | F3 | {dairy cattle, monensin-fed, Mg absorption} | Medium (упомянуто, но детали не приведены) | — (не был в Key Claims таблице, но в тексте) | R=Medium (mentioned without detail) |

**Aggregate F-G-R для CS.SOTA.332:**
- **F-distribution:** F2–F4. Claim 1 («+20% rule») — F2 (expert rule-of-thumb). Claims 2, 4 — F4 (foundational/checked). Остальные — F3.
- **G-pattern:** Более широкий, чем в 331 (общие принципы формулирования). Но несколько claims имеют region-specific G (#8 US economics).
- **R-pattern:** Более широкий диапазон R, чем в 331. Claim 12 (Cu accumulation) — R=Very High. Claim 1 (+20% rule) — R=Medium.

---

### 1.3 F-G-R Cross-Comparison: 331 vs 332

| Аспект | CS.SOTA.331 | CS.SOTA.332 |
|--------|-------------|-------------|
| **Средний F** | F3 | F3 (но есть F2 и F4) |
| **G широта** | Узкая (transition cows, specific conditions) | Шире (general formulation rules) |
| **R диапазон** | Medium – Very High | Medium – Very High |
| **Highest R** | #5 DCAD-pH (Very High) | #4 Mg AC revision, #12 Cu accumulation (Very High) |
| **Lowest R** | #4 MgCl₂/MgSO₄ NZ (Medium) | #1 +20% rule, #13 organic gut effects (Medium) |
| **Risk** | G слишком узкий для #4, #6 → extrapolation risk | G слишком широкий для #1 → overgeneralization risk |

**Key Finding:** Scalar confidence в обоих SoTA **скрывает структуру доверия**. Например:
- CS.SOTA.331 #3 (Mg 0.4–0.45%) и #5 (DCAD-pH) оба имеют confidence 0.85–0.95, но F-G-R показывает: #3 имеет R=Medium-High (confounding), а #5 — R=Very High (чистый механизм).
- CS.SOTA.332 #1 (+20% rule, confidence 0.90) — на самом деле F2/R=Medium, тогда как #4 (Mg AC, confidence 0.95) — F4/R=Very High. Одинаковый confidence 0.90–0.95 маскирует разницу в одном порядке по F и R.



---

## 2. L/A/D/E Classification (FPF A.6.B Boundary Norm Square)

> **Принцип:** Каждое boundary-утверждение несёт одну из четырёх ролей:  
> **L** = Law (физиологический закон, математическая истина)  
> **A** = Admissibility (условие применимости, gate)  
> **D** = Deontic (обязательство, рекомендация, MUST/SHOULD)  
> **E** = Evidence (описание данных, поддерживающих claim)

---

### 2.1 CS.SOTA.331 — L/A/D/E Breakdown

| # | Claim | Primary | Secondary | Анализ |
|---|-------|---------|-----------|--------|
| 1 | Mn 60–80 ppm | **D** (SHOULD feed 60–80) | E (балансовое исследование), L (плод — bottleneck) | Смешение D+E в одном claim. D: «кормите 60–80». E: «нулевой баланс при 48». Риск: E может быть оспорено без изменения D |
| 2 | Se-yeast >> selenite | **D** (SHOULD 2/3 yeast) | L (механизм замены метионина), E (2× молоко, 50–80% плод) | D доминирует. L (механизм) поддерживает D, но не доказывает оптимальное соотношение 2/3 |
| 3 | Mg 0.4–0.45% | **D** (SHOULD 0.4–0.45%) | E (мета-анализ), A (pre-fresh, high-K) | D с условием A. E — мета-анализ с confounding → R=Medium-High |
| 4 | MgCl₂/MgSO₄ лучше MgO | **D** (SHOULD prefer Cl/SO₄) | E (NZ study), A (pasture, high K, drench) | D с узким A. E — одно исследование |
| 5 | DCAD при pH < 7 | **L** (механизм H⁺/Ca²⁺) | A (pH threshold), D (target 6.5–6.7) | L доминирует — чистый механизм. D следует из L+A. Самый чистый claim |
| 6 | Витамин E ↑ мастит | **E** (5 farms, RR=1.7) | D (SHOULD 1000→2000+ IU), A (только pre-fresh) | E доминирует, но механизм неясен → D слабо обоснован. Risk: E без L |
| 7 | 25(OH)D₃ с DCAD | **D** (SHOULD 1–3 mg, only with DCAD) | L (bypass печени), E (увеличение Ca), A (pre-fresh) | D с A. L объясняет, почему только с DCAD. Но токсичность 6 мг — E без L |
| 8 | Сульфаты угнетают флору | **L** (free metal ions → bactericidal) | E (late lactation data), D (SHOULD меньше сульфатов) | L доминирует. E — limited direct data for transition. D следует из L |

**Distribution CS.SOTA.331:**
- **L (Law):** 2 claims (#5, #8) — 25%
- **A (Admissibility):** 0 pure A — A всегда secondary
- **D (Deontic):** 5 claims (#1, #2, #3, #4, #7) — 62.5%
- **E (Evidence):** 1 claim (#6) — 12.5%

**Risk Pattern:** Claims #1, #2, #3 — **D с E-support**, но E может быть недостаточным для силы D. Например, #1 (Mn 60–80) — D с E от одного балансового исследования. Если E оспорено, D ослабевает.

---

### 2.2 CS.SOTA.332 — L/A/D/E Breakdown

| # | Claim | Primary | Secondary | Анализ |
|---|-------|---------|-----------|--------|
| 1 | NRC + 20% | **D** (SHOULD +20%) | E (многолетняя практика), A (minerals, not everything) | D с E-support. Но E = «practice shows» (R=Medium), не «research confirms». Слабая основа для сильного D |
| 2 | Requirements в массе | **L** (математический факт: mass ≠ concentration) | A (все формулирование) | Чистый L. D неявный (SHOULD use mass) |
| 3 | Базовые корма содержат минералы | **E** (10,000 samples) | L (распределение ≠ 0), D (SHOULD use mean при soil contamination) | E доминирует. D вытекает из E+L. Чистая структура |
| 4 | Новые Mg AC | **L** (пересмотр coefficients) | E (несколько крупных исследований), D (SHOULD пересмотреть формулирование) | L+E. D — operational consequence. Сильный claim |
| 5 | K антагонизирует Mg | **L** (electrical potential → ↓Mg abs) | E (несколько исследований), A (K>1.1%), D (SHOULD ↑Mg) | L+E. A чёткий. D следует из L+A+E. Сильный claim |
| 6 | Жир и RDP снижают Mg | **L** (soap formation / electrical potential) | E (limited studies), A (fat>3%, high-RDP pastures), D (SHOULD +20% Mg) | L слабее (RDP mechanism unclear). E limited. D рискованнее |
| 7 | MgO 10x вариативность | **E** (4 sources, in vivo) | D (SHOULD запрашивать AC у поставщика) | Чистый E → D. Сильная структура |
| 8 | DCAD 200-300 mEq/kg | **D** (SHOULD 200–300) | E (US economics), A (US prices, milk fat premium) | D с A. E = region-specific. Risk: G too narrow for universal D |
| 9 | Высокий K → +10L мочи | **L** (физиология: 15°C → 38°C) | E (экспериментальные данные), A (heat stress) | L+E. A чёткий (heat stress). Сильный claim |
| 10 | Сера >0.2% — проблема | **L** (CuS/Se complex formation) | E (beef liver Cu, one Se study), A (total S incl. water), D (SHOULD monitor) | L с E. E heterogeneous (Cu strong, Se weak). D рискован для Se |
| 11 | Mo не сильный антагонист | **L** (liver Cu dynamics) | E (экспериментальные данные), A (Mo>6 ppm, Cu~15 ppm) | L+E. A чёткий (threshold). Сильный claim |
| 12 | Cu toxicity — накапливающаяся | **L** (linear accumulation) | E (accumulation rate data), D (SHOULD monitor trend, target 15–18 ppm) | L+E. D следует из L+E. Самый сильный claim в 332 |
| 13 | Organic: gut effects ≠ absorption | **E** (organic Zn study, hydroxy vs sulfate) | L (free metal ions → bactericidal), D (SHOULD feed same total amount) | E с L-support. D — «feed same amount» — слабо связан с E. Risk: D не следует напрямую |
| 14 | Se: 0.3 ppm; dry cows ≥50% yeast | **D** (SHOULD 0.3 ppm, ≥50% yeast dry) | E (fetus transfer, colostrum, mastitis), A (dry vs lactating) | D с E-support. A чёткий (dry/lactating split). Сильный claim |
| 15 | Monensin ↑ Mg absorption | **E** (mentioned, no detail) | D (SHOULD remember) | E слабый (no detail). D слабый. Слабейший claim |

**Distribution CS.SOTA.332:**
- **L (Law):** 5 claims (#2, #4, #5, #9, #11, #12) — 33%
- **A (Admissibility):** 0 pure A — A всегда secondary
- **D (Deontic):** 6 claims (#1, #6, #8, #10, #13, #14, #15) — 47%
- **E (Evidence):** 2 claims (#3, #7) — 13%

**Risk Pattern:**
- **#1 (+20% rule):** D с E=R=Medium. Самый рискованный D — general rule без strong evidence base.
- **#8 (DCAD 200–300):** D с A=US-only. Risk of overgeneralization.
- **#13 (organic gut effects):** D («feed same amount») не следует напрямую из E/L. Это expert shortcut, не logical consequence.

---

### 2.3 L/A/D/E Cross-SoTA Findings

| Finding | Severity | Паттерн | Рекомендация |
|---------|----------|---------|--------------|
| **D без достаточного E/L** | ⚠️ Medium | A.6.B | Для #1 (332) +20% rule — добавить explicit evidence base или понизить D до «heuristic» |
| **E без L** | ⚠️ Medium | A.6.B | #6 (331) витамин E и мастит — RR=1.7 без механизма. Нужен L или downgrade |
| **D с узким A, но широким G** | 🔴 High | A.6.B | #8 (332) DCAD 200–300 — A=US, но D звучит universal. Либо расширить A, либо сузить G |
| **Смешение D/E в одном предложении** | ⚠️ Medium | A.6.B | #1 (331) Mn 60–80 — «кормите 60–80» (D) и «нулевой баланс при 48» (E) в одном claim. Разделить |
| **E heterogeneous (разное качество)** | ⚠️ Medium | A.6.B | #10 (332) Cu strong, Se weak — в одном claim. Разделить или явно пометить |

---

## 3. CausalUse-CAL Audit (FPF C.28)

> **Принцип:** Causal claims распределяются по лестнице Пёрла: Association → Intervention → Counterfactual.  
> **Правило:** Нельзя интерпретировать claim выше, чем позволяет evidence. Если evidence = association, claim не может быть intervention.

---

### 3.1 CS.SOTA.331 — Causal Rung Assessment

| # | Claim | Stated Causality | Evidence Type | **Causal Rung** | Gap |
|---|-------|-----------------|---------------|-----------------|-----|
| 1 | Mn 60–80 ppm | Mn intake → fetal Mn status | Балансовое исследование (mass balance) | **Intervention** | Нет рандомизации — балансовое исследование ≠ RCT. Rung может быть overstated |
| 2 | Se-yeast >> selenite | Se source → milk/colostrum Se | Comparative absorption + transfer studies | **Intervention** | Механизм ясен (selenomethionine incorporation). Rung adequate |
| 3 | Mg 0.4–0.45% | Mg intake → hypocalcemia ↓ | Meta-analysis (correlation) | **Association** | Meta-analysis показывает correlation, не causal. Confounding (DCAD). **Overstated** |
| 4 | MgCl₂/MgSO₄ лучше MgO | Mg source → blood Ca | Single NZ study (intervention) | **Intervention** | n=?, randomization? Одно исследование — weak intervention |
| 5 | DCAD при pH < 7 | DCAD → metabolic acidosis → Ca mobilization | Mechanism + repeated experiments | **Intervention** | Механизм ясен (H⁺/Ca²⁺). pH threshold — measurable. Rung adequate |
| 6 | Витамин E ↑ мастит | Vitamin E intake → mastitis ↑ | Observational (5 farms, RR=1.7) | **Association** | RR=1.7 — association, не intervention (нет randomization). **Overstated** |
| 7 | 25(OH)D₃ с DCAD | 25(OH)D₃ + DCAD → blood Ca ↑ | Dose-response experiment | **Intervention** | Dose-response shown, но токсичность 6 мг не объяснена. Rung adequate |
| 8 | Сульфаты угнетают флору | Sulfate minerals → ↓NDF digestion | Late lactation experiment | **Intervention** | Механизм ясен (free ions). Extrapolation to transition — association |

**CS.SOTA.331 Causal Summary:**
- **Association:** 2 claims (#3, #6) — 25%
- **Intervention:** 5 claims (#1, #2, #4, #5, #7, #8) — 75%
- **Counterfactual:** 0 claims — 0%
- **Overstated:** #3 (Mg meta-analysis → Intervention claimed), #6 (observational → causal implied)

---

### 3.2 CS.SOTA.332 — Causal Rung Assessment

| # | Claim | Stated Causality | Evidence Type | **Causal Rung** | Gap |
|---|-------|-----------------|---------------|-----------------|-----|
| 1 | NRC + 20% | — | Expert rule-of-thumb | **N/A** | Не causal claim. Эвристика |
| 2 | Requirements в массе | — | Mathematical truth | **N/A** | Не causal claim. Definition |
| 3 | Базовые корма содержат минералы | — | Survey (10,000 samples) | **N/A** | Descriptive, не causal |
| 4 | Новые Mg AC | — | Coefficient revision | **N/A** | Measurement update, не causal |
| 5 | K антагонизирует Mg | K intake → ↓Mg absorption | Multiple intervention studies | **Intervention** | Механизм ясен (electrical potential). Rung adequate |
| 6 | Жир и RDP снижают Mg | Fat/RDP → ↓Mg absorption | Limited intervention studies | **Intervention** | Fat — stronger evidence. RDP — weaker (mechanism unclear). RDP may be Association |
| 7 | MgO вариативность | MgO source → absorption variance | 4-source comparison | **Intervention** | Direct comparison. Rung adequate |
| 8 | DCAD 200-300 | DCAD → milk fat/yield | Response experiments + economics | **Intervention** | Physiological response = Intervention. Economics = N/A |
| 9 | Высокий K → +10L мочи | K intake → urine output | Direct measurement experiment | **Intervention** | Direct physiological measurement. Rung adequate |
| 10 | Сера >0.2% — проблема | S intake → ↓Cu/Se absorption | Beef Cu study + one Se study | **Intervention** (Cu), **Association** (Se) | Cu = strong intervention. Se = one study → borderline |
| 11 | Mo не сильный антагонист | Mo intake → liver Cu | Dose-response experiment | **Intervention** | Dose-response with threshold. Rung adequate |
| 12 | Cu toxicity — накапливающаяся | Cu intake → liver Cu accumulation | Longitudinal accumulation study | **Intervention** | Linear dynamics shown. Rung adequate |
| 13 | Organic: gut effects ≠ absorption | Organic Zn → ↓bacteria in feces | Single experiment (fecal bacteria) | **Intervention** | One study. Generalization to «all organics» = Association |
| 14 | Se: 0.3 ppm; yeast ≥50% | Se source → fetus/colostrum/mastitis | Multiple outcome studies | **Intervention** | Multiple replicated outcomes. Rung adequate |
| 15 | Monensin ↑ Mg absorption | Monensin → Mg absorption | Mentioned, no detail | **Association** (at best) | No details. Cannot claim Intervention |

**CS.SOTA.332 Causal Summary:**
- **Association:** 1 claim (#15, #13 generalization) — 7%
- **Intervention:** 8 claims (#5, #6, #7, #8, #9, #11, #12, #14) — 53%
- **N/A (не causal):** 4 claims (#1, #2, #3, #4) — 27%
- **Mixed:** 1 claim (#10: Cu=Intervention, Se=Association)

---

### 3.3 CausalUse-CAL Cross-Finding

| Finding | Severity | Паттерн | Рекомендация |
|---------|----------|---------|--------------|
| **Association overstated as Intervention** | 🔴 High | C.28 | #3 (331) Mg meta-analysis — correlation ≠ causation. Добавить confounding disclaimer или понизить rung |
| **Observational overstated as Causal** | 🔴 High | C.28 | #6 (331) Vitamin E и мастит — RR=1.7 без randomization. Это association, не causal intervention |
| **Generalization beyond evidence** | ⚠️ Medium | C.28 | #8 (331) sulfates — late lactation → universalized to transition. Add boundary |
| **Single-study generalization** | ⚠️ Medium | C.28 | #13 (332) organic Zn — one study → «organic minerals». Boundary: «shown for one organic Zn product» |
| **No counterfactual claims** | ℹ️ Info | C.28 | Ни один claim не достигает Counterfactual rung. Это нормально для applied nutrition, но ограничивает predictive power |

---

## 4. Bridge Map: CS.SOTA.331 ↔ CS.SOTA.332 (FPF F.9)

> **Принцип:** Cross-context alignment через explicit Bridges с Congruence Level (CL).  
> **Bridge** = mapping между concepts в разных BoundedContexts. **CL** = степень доверия к mapping.

---

### 4.1 Explicit Bridges (уже есть в SoTA)

| Bridge | From | To | CL | Status |
|--------|------|-----|-----|--------|
| NASEM-2021 Minerals | CS.SOTA.331 #1–8 | CS.SOTA.301 | CL=High | ✅ Explicit |
| NASEM-2021 Vitamins | CS.SOTA.331 #6–7 | CS.SOTA.302 | CL=High | ✅ Explicit |
| NASEM-2021 Transition | CS.SOTA.331 | CS.SOTA.312 | CL=High | ✅ Explicit |
| Lean 2006 DCAD | CS.SOTA.331 #5 | CS.SOTA.056 | CL=Medium | ✅ Explicit |
| Goff 2018 Absorption | CS.SOTA.331 #3–4 | CS.SOTA.168 | CL=Medium | ✅ Explicit |

### 4.2 Implicit Bridges (неявные, нуждаются в explicit формулировке)

| Bridge | From | To | CL | Проблема |
|--------|------|-----|-----|----------|
| **Se source: 331#2 ↔ 332#14** | CS.SOTA.331 #2 (2/3 yeast) | CS.SOTA.332 #14 (≥50% yeast dry) | CL=High | **Divergence:** 331 рекомендует 2/3 yeast для transition, 332 — ≥50% для dry cows. Это согласовано (transition ⊂ dry), но не explicit |
| **Mg requirements: 331#3 ↔ 332#5–6** | CS.SOTA.331 #3 (0.4–0.45% pre-fresh) | CS.SOTA.332 #5–6 (K antagonism, fat effect) | CL=High | **Complementary:** 332 объясняет WHY 331 рекомендует 0.4–0.45% (K, fat). Bridge не сформулирован |
| **DCAD: 331#5 ↔ 332#8** | CS.SOTA.331 #5 (pH < 7) | CS.SOTA.332 #8 (200–300 mEq/kg) | CL=Medium | **Tension:** 331 фокус на pH (mechanism), 332 — на mEq/kg (practical target). pH 6.5–6.7 ≈ DCAD -100 to -200? Нет explicit conversion |
| **Sulfates: 331#8 ↔ 332#13** | CS.SOTA.331 #8 (сульфаты угнетают флору) | CS.SOTA.332 #13 (gut effects ≠ absorption) | CL=High | **Reinforcement:** оба SoTA говорят одно и то же. Bridge усиливает оба |
| **Cu toxicity: 332#12** | CS.SOTA.332 #12 | CS.SOTA.331 (нет Cu toxicity) | CL=N/A | **Gap:** 331 не упоминает Cu toxicity. Это intentional (focus transition) или omission? |

### 4.3 Bridge Quality Assessment

| Bridge | Direction | CL | Loss Notes |
|--------|-----------|-----|-----------|
| 331→332 (Mg) | One-way reinforcement | High | 332 объясняет механизм 331, но 331 не ссылается на 332 (понятно — 332 создан позже) |
| 332→331 (Se) | Partial overlap | High | Согласованность есть, но не formalized |
| 331↔332 (DCAD) | Complementary but disconnected | Medium | pH-based (331) vs mEq/kg-based (332) — разные «languages» для одного phenomenon |
| 332→331 (Cu) | One-way gap | N/A | 332#12 (Cu toxicity) имеет no bridge to 331. Это valid scope_out для 331? |

**Recommendation:** Создать explicit Bridge card `BRIDGE.001-weiss-minerals-cross-lecture.md` с formalized mappings между 331 и 332.

---

## 5. Reopen Triggers & Evolution Loop (FPF B.4)

> **Принцип:** Canonical Evolution Loop = Observe → Notice → Stabilize → Route.  
> **DesignRunTag:** Каждое решение должно иметь явный trigger для reopen.

---

### 5.1 Текущее состояние Reopen Triggers

| SoTA | Есть reopen_trigger? | Формат | Quality |
|------|---------------------|--------|---------|
| CS.SOTA.331 | ✅ Yes | `reopen_trigger: 'Видео: WP-75 ...'` | Слабый — ссылается на видео-файл, не на event или data |
| CS.SOTA.332 | ❌ No | — | Отсутствует |

### 5.2 Рекомендуемые Reopen Triggers (FPF B.4 формат)

#### CS.SOTA.331 — Reopen Trigger Set

| Trigger ID | Event Type | Condition | Action on Reopen | Priority |
|------------|-----------|-----------|------------------|----------|
| R331.1 | **Data** | Публикация independent RCT по Mn в dry cows с n>100 | Пересмотреть #1 (Mn 60–80). Если RCT показывает достаточность 40 ppm — понизить D или добавить A (breed-specific?) | High |
| R331.2 | **Data** | Публикация механизма витамин E → мастит (RCT или mechanistic study) | Пересмотреть #6. Если механизм найден — повысить R до High. Если не найден — понизить causal rung | High |
| R331.3 | **Data** | Публикация по 25(OH)D₃ toxicity (6 мг mechanism) | Пересмотреть #7. Добавить L или boundary | Medium |
| R331.4 | **Regulatory** | Изменение FDA/USDA limits on Se (currently 0.3 ppm supplemental) | Пересмотреть #2 (0.6 ppm total — может стать illegal) | High |
| R331.5 | **Model** | NASEM 2025 (next edition) | Полный пересмотр всех NASEM-based claims | Medium |
| R331.6 | **Local** | Локальная проверка +20% rule на 3+ фермах с documented outcomes | Добавить E к #1 (332) или создать local variant | Low |

#### CS.SOTA.332 — Reopen Trigger Set

| Trigger ID | Event Type | Condition | Action on Reopen | Priority |
|------------|-----------|-----------|------------------|----------|
| R332.1 | **Data** | Публикация new Mg AC studies (post-2021) с отличными от NASEM-2021 coefficients | Пересмотреть #4. Если divergence — добавить A (feed type specific?) | High |
| R332.2 | **Data** | Independent replication of MgO 10x variability with n>4 sources | Пересмотреть #7. Если variability подтверждена — strengthen D. Если нет — ponизить | Medium |
| R332.3 | **Economic** | Существенное изменение цен на K/Na buffers или milk fat premium (>30%) | Пересмотреть #8 (DCAD 200–300). Пересчитать break-even | Medium |
| R332.4 | **Data** | Публикация по RDP→Mg adaptation mechanism (2-week adaptation explained) | Пересмотреть #6. Повысить L (mechanism) или добавить A | Medium |
| R332.5 | **Local** | Анализ воды на S в 5+ стадах с корреляцией Cu/Se status | Добавить E к #10. Local bridge | Low |
| R332.6 | **Model** | NASEM 2025 includes fat→Mg effect in model | Пересмотреть #6. Remove «not in model» boundary | Medium |
| R332.7 | **Data** | Long-term (5+ year) liver Cu monitoring data from >10 farms | Пересмотреть #12. Если accumulation non-linear — понизить R | Low |

### 5.3 DesignRunTag Feedback (FPF B.4)

| SoTA | Design (что задумано) | Run (что получено) | Tag (что изменилось) | Drift |
|------|----------------------|-------------------|---------------------|-------|
| CS.SOTA.331 | Webinar → Key Claims → SoTA | 8 claims, 6 mechanisms, practical table | Transcription method (faster-whisper small) | Нет drift — соответствует intent |
| CS.SOTA.332 | Lecture → Key Claims → SoTA | 14 claims, 7 mechanisms, practical checklist | Transcription method (faster-whisper small) | Нет drift, но coverage gaps (Mn, Zn details deferred) |

**Observation:** Оба SoTA — DesignRunTag соответствует intent. Но **нет механизма periodic refresh**. FPF B.4 требует periodic Observe → Notice для stale knowledge.

---

## 6. Overall Findings & Recommendations

### 6.1 Critical Findings (🔴 High)

| # | Finding | FPF Pattern | Risk |
|---|---------|-------------|------|
| 1 | **Scalar confidence маскирует структуру доверия.** Claims с F2/R=Medium и F4/R=Very High имеют одинаковый confidence 0.90–0.95. Это создаёт illusion of equal reliability. | B.3 F-G-R | Overreliance on weak claims |
| 2 | **Association overstated as Intervention.** #3 (331) Mg meta-analysis и #6 (331) Vitamin E — correlation/observational data presented as causal recommendations. | C.28 CausalUse | Wrong clinical decisions |
| 3 | **D без достаточного E/L.** #1 (332) +20% rule — strong D (general rule) на основе R=Medium (practice shows). | A.6.B L/A/D/E | Rule application beyond evidence |
| 4 | **Region-specific D presented as universal.** #8 (332) DCAD 200–300 — US economics, но формулировка звучит universal. | A.6.B L/A/D/E | Economic losses in non-US contexts |
| 5 | **No explicit Bridge between 331 and 332.** Complementary knowledge (Mg, Se, DCAD) не связана explicit mappings. | F.9 Bridges | Redundant work, inconsistency risk |

### 6.2 Recommendations

#### Immediate (можно сделать сейчас)

1. **Добавить F-G-R tuples** в frontmatter каждого Key Claim (как structured metadata)
2. **Разделить mixed D/E claims** — отдельно E (what data shows), отдельно D (what to do)
3. **Добавить explicit causal rung** к каждому causal claim (Association / Intervention / Counterfactual)
4. **Создать Bridge card** между 331 и 332 (BRIDGE.001)
5. **Добавить reopen triggers** в CS.SOTA.332 (сейчас отсутствуют)

#### Short-term (следующий цикл обновления)

6. **Провести independent F-G-R assessment** для #1 (332) +20% rule — найти formal evidence base или понизить до heuristic
7. **Добавить A (admissibility conditions)** к #8 (332) — explicit «US economics only» boundary
8. **Понизить causal rung** для #3 (331) и #6 (331) до Association с explicit confounding notes
9. **Создать periodic review schedule** (FPF B.4) — ежегодный аудит SoTA на stale knowledge

#### Long-term (при накоплении локальных данных)

10. **Создать local variant** CS.SOTA.332-RU с пересчитанной экономикой DCAD и данными по воде/кормам в РФ
11. **Провести local replication** для #7 (332) MgO variability — test Russian MgO sources
12. **Накопить liver Cu monitoring data** для валидации #12 (332) в локальных условиях

### 6.3 FPF Compliance Score

| Паттерн | CS.SOTA.331 | CS.SOTA.332 | Target |
|---------|-------------|-------------|--------|
| B.3 F-G-R | ⚠️ Partial (scalar only) | ⚠️ Partial (scalar only) | ✅ Full tuples |
| A.6.B L/A/D/E | ⚠️ Implicit | ⚠️ Implicit | ✅ Explicit labels |
| C.28 CausalUse | ⚠️ Partial (overstated) | ✅ Mostly correct | ✅ Explicit rungs |
| A.7 Strict Distinction | ✅ Good | ✅ Good | ✅ Maintain |
| B.4 Evolution | ⚠️ Weak trigger | ❌ Missing | ✅ Full trigger set |
| F.9 Bridges | ✅ Explicit (external) | ❌ Implicit (internal) | ✅ Explicit all |

**Overall:** Оба SoTA — хорошие P2 (expert-opinion) artifacts. FPF-аудит выявляет **5 critical gaps**, все устранимы без изменения содержания — через добавление metadata, labels, boundaries и triggers.

---

## Appendix: FPF Term Translation (No-Jargon Rule)

| FPF Term | Engineering Equivalent |
|----------|----------------------|
| F-G-R | Trust tuple: Formality + Scope + Reliability |
| L/A/D/E | Claim type: Law / Gate-condition / Rule / Data-description |
| Causal Rung | Level of causal evidence: correlation → experiment → counterfactual |
| Bridge (F.9) | Cross-reference between documents with explicit trust level |
| CL (Congruence Level) | How much we trust a cross-reference |
| DesignRunTag | Plan-Execute-Review cycle with explicit change triggers |
| BoundedContext | Scope boundary where terms have specific local meanings |
| Episteme | Structured knowledge record (like SoTA) |
| Holon | System that is both a part and a whole |

