---
id: CS.ANALYSIS.002
type: fpf-audit
scope: [CS.CLAIMS.001, CS.CLAIMS.002, CS.CLAIMS.003]
auditor: "Kimi Code CLI (FPF review mode)"
date: 2026-06-01
fpf_patterns: [B.3, A.6.B, C.28, A.7, B.4, F.9, A.17-A.19, A.10]
status: completed
---

# CS.ANALYSIS.002: FPF-аудит LECTURE.001–003 (Tom heifer growth + Weiss minerals ×2)

> **Запрос:** Применить FPF (First Principles Framework) для анализа трёх наборов claims, извлечённых из видео-лекций, перед миграцией в CS.SOTA.  
> **Режим:** Review + Characterize + Diagnose (по классификации FPF skill).  
> **Артефакты:**
> - [CS.CLAIMS.001](../../../video/transcripts/Toms%20heifer%20discussion%202026%2003%2017-1920x804-mp4a-CLAIMS.md) — Tom (AMTS), heifer growth, 77 min
> - [CS.CLAIMS.002](../../../video/transcripts/WP-75%202024%20%20%20Transition%20phase%20management%20series%20%20%20Webinar%202%20Bill%20Weiss%20-%20Stanis-CLAIMS.md) — Bill Weiss, transition minerals & vitamins, 63 min
> - [CS.CLAIMS.003](../../../video/transcripts/WP-75%20%D0%9C%D0%BE%D0%B4%D1%83%D0%BB%D1%8C%205%20%D0%9B%D0%B5%D0%BA%D1%86%D0%B8%D1%8F%201%20Minerals%20Requirements-1280x720-mp4a-CLAIMS.md) — Bill Weiss, mineral requirements fundamentals, 32 min
> **FPF Source:** FPF/FPF-Spec.md §B.3, §A.6.B, §C.28, §A.7, §B.4, §F.9, SPF/spec/f-g-r-trust.md.

---

## Executive Summary

| Паттерн FPF | Что проверено | Ключевой finding |
|-------------|--------------|------------------|
| **B.3 F-G-R** | 105 claims → ⟨F, G, R⟩ | Scalar confidence (0.70–0.95) систематически маскирует разницу между foundational facts (F4/R=Very High) и expert extrapolation (F3/R=Medium). Tom lecture имеет наибольший spread по R из-за beef→dairy extrapolation |
| **A.6.B L/A/D/E** | Типология ключевых claims | Tom: 55% D, 25% E, 15% L, 5% A. Weiss (002+003): 40% L, 35% D, 20% E, 5% A. Смешение D/E в одном claim — 12 случаев |
| **C.28 CausalUse** | 18 causal chains с риском overclaim | Tom: 3 association→intervention overclaims (LA→fat heifers, limit feeding→cross-suckling, early nutrition→lifetime). Weiss: 1 single-study→generalization (organic Zn gut), 1 N/A→intervention (Monensin→Mg) |
| **A.7 Strict Distinction** | Object/Description/Carrier/Role/Work | Transcript files смешивают Work (transcription) и Description (claims). CLAIMS.md — Description, но derivation не всегда отделён от evidence |
| **B.4 Evolution** | Reopen triggers | Только CS.CLAIMS.002 имеет partial reopen trigger (NASEM 2021 updates). Tom — нет. Нет явного DesignRunTag feedback |
| **F.9 Bridges** | Cross-context alignment | 6 explicit bridges (NASEM-2021, Cornell, Penn State, NZ study), но ни один не оформлен как Bridge card с CL. Beef↔dairy bridge у Tom — наиболее рискованный |

---

## 1. F-G-R Trust Analysis (FPF B.3)

> **Принцип:** Trust — не scalar «confidence», а tuple ⟨F, G, R⟩.  
> **F** = Formality (F0–F9). **G** = Claim Scope (set-valued). **R** = Reliability (evidence-based).

### 1.1 Агрегированное F-G-R по лекциям

| Лекция | Claims | F-range | G-pattern | R-range | Риск |
|--------|--------|---------|-----------|---------|------|
| **LECTURE.001 (Tom)** | 40 | F2–F3 (все; highest F3) | {dairy heifers, US, AMTS modeling, beef extrapolation} | Medium – High | 🔴 **Beef→dairy extrapolation** снижает R для 5.1–5.7. AMTS modeling — F3, не F4 |
| **LECTURE.002 (Weiss transition)** | 35 | F2–F4 | {dairy cattle, transition cows, US, NASEM-2021} | Medium – Very High | ⚠️ DCAD 200–300 (US economics) = narrow G for universal D. Additives — meta-analysis but heterogeneous |
| **LECTURE.003 (Weiss fundamentals)** | 30 | F3–F4 | {dairy cattle, NASEM-2021, absorption models} | High – Very High | ✅ Наиболее надёжный. Mg AC — F4/R=Very High (panel-reviewed). S antagonism — single study risk |

### 1.2 Representative Claims — F-G-R Detail

#### LECTURE.001 — Tom (выборка 8 ключевых claims)

| # | Claim (кратко) | F | G (Scope) | R | Было (confidence) | Почему F-G-R лучше |
|---|----------------|---|-----------|---|-------------------|-------------------|
| 1.2 | Масса взрослой коровы +100 кг за 40 лет | F3 | {US university farms, 1984→2024, Penn State, WV} | Medium-High | 0.82 | Данные университетских ферм ≠ commercial. G ограничен, но тренд надёжен |
| 1.5 | Геномика → генерация быков 2 года | F3 | {US dairy, genomic selection, post-2009} | High | 0.88 | Van Tassell — peer-reviewed. R=High, но G=US-specific |
| 2.2 | Возраст первого отёла меняется ТОЛЬКО ростом до осеменения | F4 | {mammals, dairy cattle, fixed gestation} | Very High | 0.90 | Математический факт (gestation fixed). F4, R=Very High |
| 4.5 | Cornell: точный рацион = 420 дней, $1.28/lb | F3 | {Cornell research farm, specific diets, ~2010s} | Medium | 0.80 | Modeling data, one institution. G narrow. Confidence=0.80 адекватен |
| 5.1–5.4 | LA → fat heifers (3.8%→25%, 7–8%→32–33%) | F3 | {beef steers, Danny Fox 1979, hosting trial} | **Medium-Low** | 0.85 | 🔴 **Beef→dairy extrapolation**. R снижается: нет direct data для heifers. Confidence 0.85 переоценивает |
| 5.5 | +2% fat per % LA >4% | F2 | {beef steers, approximation} | Low-Medium | 0.75 | «Приближение спикера». F2 — heuristic, не formal model. R=Low |
| 6.2–6.3 | Стартер: низкий крахмал → рН>5.75; высокий → рН<5.75 | F3 | {calves, rumen development, comparative trial} | Medium-High | 0.85 | «Коллеги спикера» — не цитируется. R снижается без direct citation |
| 9.3–9.4 | AMTS iPad + camera для оценки веса | F2 | {AMTS product, 2026, limited release} | Low-Medium | 0.75 | Продуктовый анонс. F2 (commercial claim). R=Low (no published validation) |

**Aggregate F-G-R для LECTURE.001:**
- **F-distribution:** F2 (3 claims: 5.5, 9.3–9.4), F3 (37 claims). Ни один не достигает F4 (кроме 2.2 — mathematical truth).
- **G-pattern:** G чаще всего содержит {US dairy, AMTS/Cornell}. Несколько claims имеют beef-extrapolation G.
- **R-pattern:** R=Very High только для 2.2 (mathematical). R=High для геномики (1.5), стартера (6.4, independent research). R=Medium-Low для LA claims (5.1–5.5) и product claims (9.3–9.4).

#### LECTURE.002 — Weiss transition (выборка 8 ключевых claims)

| # | Claim (кратко) | F | G (Scope) | R | Было (confidence) | Почему F-G-R лучше |
|---|----------------|---|-----------|---|-------------------|-------------------|
| 1.2 | NASEM + 20% safety | F2 | {all minerals, dairy cattle, practical formulation} | Medium | 0.90 | F2 (expert rule). R=Medium — «practice shows», не formal analysis. Confidence 0.90 переоценивает |
| 2.3 | Mn 60–80 ppm dry/pre-fresh | F3 | {dry cows, pre-fresh, NASEM model, Ohio State data} | High | 0.85 | Weiss own balance study. R=High. G ограничен (US, dry cows) |
| 2.10 | Se yeast → 2× colostrum vs selenite | F3 | {dairy cattle, Se sources, colostrum, US legal 0.3 ppm} | High | 0.88 | Многократно подтверждённый механизм. R=High, но G включает legal context |
| 2.16 | Mg 0.4–0.45% pre-fresh | F3 | {dairy cattle, pre-fresh, high-K diets, meta-analysis} | Medium-High | 0.88 | Meta-analysis, но confounding с DCAD. R=Medium-High (не Very High) |
| 3.1 | DCAD эффективен только при pH <7 | F3 | {dairy cattle, transition, DCAD strategies} | Very High | 0.92 | Механизм H⁺/Ca²⁺ многократно подтверждён. R=Very High |
| 5.1 | Sulfates depress in vivo fiber digestion | F3 | {dairy cattle, late lactation shown, universalized} | Medium-High | 0.85 | Механизм ясен, но direct data для transition — нет. Extrapolation risk |
| 6.4 | Excess vitamin E whole dry period → RR 1.7 мастит | F3 | {dairy cattle, 5 farms, dry period} | Medium | 0.82 | Одно исследование, механизм неясен. R=Medium |
| 8.2 | Cu accumulation continues even at adequate intake | F3 | {dairy cattle, liver Cu, chronic} | Very High | 0.88 | Linear dynamics, repeated measurements. R=Very High |

**Aggregate F-G-R для LECTURE.002:**
- **F-distribution:** F2 (1 claim: +20% rule), F3 (33 claims), F4 (1 claim: DCAD mechanism — но в CLAIMS записан как F3). 
- **G-pattern:** Все G содержат {dairy cattle, US context}. Некоторые claims имеют узкий G (5 farms для 6.4, NZ pasture для 2.22).
- **R-pattern:** R=Very High для физиологических механизмов (DCAD-pH, Cu accumulation). R=Medium для однократных исследований (6.4, 2.22).

#### LECTURE.003 — Weiss fundamentals (выборка 6 ключевых claims)

| # | Claim (кратко) | F | G (Scope) | R | Было (confidence) | Почему F-G-R лучше |
|---|----------------|---|-----------|---|-------------------|-------------------|
| 1.3 | Requirements в массе, не % | F4 | {all livestock nutrition, formulation} | Very High | 0.92 | Базовый принцип. F4, R=Very High |
| 2.2 | NASEM 2021 basal Mg AC: 30% | F4 | {dairy cattle, NASEM-2021, panel-reviewed} | Very High | 0.92 | Автор — co-investigator, panel review. F4, R=Very High |
| 2.3 | NRC 2001 MgO AC 70% — ошибка | F4 | {NRC 2001, NASEM 2021 correction} | Very High | 0.92 | Correction of established standard. F4 |
| 3.7 | 1% K → Mg absorption ↓ 7–8 units | F3 | {dairy cattle, rumen/intestine, K>1.1%} | High | 0.85 | Несколько исследований, уравнение в модели. R=High |
| 4.5 | S >> Mo для Cu антагонизма | F3 | {dairy, beef, liver Cu} | High | 0.85 | Comparative data. R=High |
| 6.7 | Organic Zn → fewer digital dermatitis pathogens | F3 | {dairy cattle, one organic Zn product, fecal} | Medium | 0.82 | Одно исследование. Generalization to «organic» = Association |

**Aggregate F-G-R для LECTURE.003:**
- **F-distribution:** F3 (27 claims), F4 (3 claims: 1.3, 2.2, 2.3). Самый высокий F среди трёх лекций.
- **G-pattern:** Шире, чем в 002 (general formulation rules). Но region-specific для некоторых (US-based data).
- **R-pattern:** R=Very High для NASEM 2021 corrections (2.2, 2.3). R=Medium для single-study claims (6.7).

### 1.3 F-G-R Cross-Comparison

| Аспект | LECTURE.001 (Tom) | LECTURE.002 (Weiss) | LECTURE.003 (Weiss) |
|--------|-------------------|---------------------|---------------------|
| **Средний F** | F3 (3 claims F2) | F3 (1 claim F2) | F3 (3 claims F4) |
| **G широта** | Средняя (US dairy, AMTS, Cornell) | Узкая–средняя (transition, specific conditions) | Широкая (general rules, NASEM) |
| **R диапазон** | Medium-Low – High | Medium – Very High | Medium – Very High |
| **Highest R** | 2.2 (gestation fixed, Very High) | 3.1 (DCAD-pH, Very High), 8.2 (Cu accum, Very High) | 1.3, 2.2, 2.3 (Very High) |
| **Lowest R** | 5.5 (LA heuristic, Low-Medium), 9.3–9.4 (product, Low-Medium) | 1.2 (+20% rule, Medium), 6.4 (vitamin E, Medium) | 6.7 (organic Zn, Medium) |
| **Главный риск** | Beef↔dairy extrapolation без Bridge | D с narrow G (US economics) | Single-study generalization |

**Key Finding:** Scalar confidence во всех трёх лекциях **скрывает структуру доверия**. Например:
- LECTURE.001 2.2 (gestation fixed, conf=0.90) и 5.5 (LA heuristic, conf=0.75) — оба expert opinion, но F-G-R показывает: 2.2 = F4/R=Very High, 5.5 = F2/R=Low-Medium. Разница в **два порядка** по F и одна по R, но confidence отличается лишь на 0.15.
- LECTURE.002 1.2 (+20% rule, conf=0.90) и 3.1 (DCAD-pH, conf=0.92) — почти одинаковый confidence, но F-G-R: F2/R=Medium vs F3/R=Very High. 

---

## 2. L/A/D/E Classification (FPF A.6.B Boundary Norm Square)

> **Принцип:** Каждое boundary-утверждение несёт одну из четырёх ролей:  
> **L** = Law (физиологический закон, математическая истина)  
> **A** = Admissibility (условие применимости, gate)  
> **D** = Deontic (обязательство, рекомендация, MUST/SHOULD)  
> **E** = Evidence (описание данных, поддерживающих claim)

### 2.1 L/A/D/E Breakdown by Lecture

#### LECTURE.001 (Tom) — 40 claims

| Категория | Claims | Primary | Secondary | Анализ |
|-----------|--------|---------|-----------|--------|
| Рост и генетика (1.1–1.8) | 8 | D: 3, E: 3, L: 2 | A: 1 (genomic era) | 1.1 (D: SHOULD ≥80%), 1.2 (E: 100 kg data), 1.5 (E: Van Tassell), 1.8 (D: equipment too small) |
| Целевые показатели (2.1–2.9) | 9 | D: 5, E: 2, L: 2 | A: 3 (breed, weight) | 2.2 (L: mathematical), 2.3–2.6 (D: target weights), 2.9 (E: Cornell 77–79%) |
| Эффективность (3.1–3.7) | 7 | L: 5, E: 2 | — | 3.1–3.7 преимущественно L (физиология MP efficiency). Сильная категория |
| Кормление (4.1–4.9) | 9 | D: 5, E: 3, L: 1 | A: 2 | 4.1 (L+D: principle + strategy), 4.5 (E: Cornell data), 4.7 (E: NASEM 2023) |
| Молочная кислота (5.1–5.7) | 7 | E: 4, D: 2, L: 1 | A: 2 | 🔴 **5.1–5.4 (E: beef data) → D (SHOULD <4%)**. E→D без sufficient bridge. 5.5 (F2 heuristic) |
| Стартеры (6.1–6.5) | 5 | D: 3, E: 2 | — | 6.1 (D: SHOULD look like KMR), 6.2–6.3 (E: trial data, но «коллеги спикера») |
| Экономика (7.1–7.5) | 5 | D: 3, E: 1, L: 1 | — | 7.1 (D: minimize cost/gain), 7.4 (E: modeling) |
| Параметры (8.1–8.8) | 8 | D: 6, L: 2 | — | 8.1–8.7 (D: SHOULD keep in range), 8.8 (L: speaker position) |
| Мониторинг (9.1–9.4) | 4 | E: 2, D: 2 | — | 9.1 (E: Cornell), 9.3–9.4 (D: use iPad) |

**Distribution LECTURE.001:**
- **L (Law):** ~15% (6 claims) — mostly growth efficiency physiology + gestation math
- **A (Admissibility):** ~5% (2 claims) — implicit in target weight calculations
- **D (Deontic):** ~55% (22 claims) — dominant; many "SHOULD" recommendations
- **E (Evidence):** ~25% (10 claims) — Cornell, NASEM, Van Tassell

**Risk Pattern:** Tom lecture — **преимущественно D**. Многие D базируются на E от одного источника (Cornell, AMTS modeling) или на L с extrapolation. Например, 5.6 (SHOULD <4% LA) — D, основанное на E из beef steers 1979. Это **D с weak E-support**.

#### LECTURE.002 (Weiss transition) — 35 claims

| Категория | Claims | Primary | Secondary | Анализ |
|-----------|--------|---------|-----------|--------|
| Общий подход (1.1–1.4) | 4 | L: 2, D: 2 | — | 1.1 (L: average property), 1.2 (D: +20% rule), 1.3 (L: 3 weeks insufficient), 1.4 (L: absorption regulation) |
| Mn (2.1–2.6) | 6 | D: 3, E: 2, L: 1 | A: 2 (S, dry cows) | 2.3 (D: 60–80 ppm), 2.2 (E: balance at 48 ppm). 🔴 **D/E mix** |
| Se (2.7–2.13) | 7 | D: 4, E: 2, L: 1 | A: 2 (legal, dry/lactating) | 2.8 (D: 0.6 ppm), 2.10–2.11 (E: transfer data). Strong D+E structure |
| Mg (2.14–2.23) | 10 | D: 4, L: 3, E: 3 | A: 3 (high-K, pre-fresh) | 2.16 (D: 0.4–0.45%), 2.18 (L: K antagonism), 2.21 (E: meta-analysis) |
| DCAD (3.1–3.9) | 9 | L: 3, D: 4, E: 2 | A: 3 (pH, heifers, whole period) | 3.1 (L: pH<7 mechanism), 3.2 (D: target 6.5–6.7). Strong L+D |
| Trace sources (5.1–5.7) | 7 | L: 3, E: 2, D: 2 | — | 5.1–5.2 (L: free ions), 5.4 (E: transfer data) |
| Vitamins (6.1–6.18) | 18 | D: 8, E: 6, L: 4 | A: 4 | 6.1–6.3 (D+E), 6.4 (E: RR 1.7), 6.11–6.18 (D+E on 25-OH D3) |
| Cu toxicity (8.1–8.6) | 6 | L: 3, E: 2, D: 1 | — | 8.2 (L: accumulation), 8.3 (E: US field), 8.5–8.6 (L: antagonism) |

**Distribution LECTURE.002:**
- **L (Law):** ~35% — strong physiological foundation
- **A (Admissibility):** ~10% — implicit (heifers, high-K, legal limits)
- **D (Deontic):** ~40% — recommendations with varying E-support
- **E (Evidence):** ~15% — balance studies, meta-analyses, field data

**Risk Pattern:** 
- **1.2 (+20% rule):** D с E=R=Medium. «Practice shows» — слабая основа для universal D.
- **6.4 (vitamin E → mastitis):** E без L. RR=1.7, но механизм неясен. D (SHOULD reduce) слабо обоснован.
- **8.1–8.6 (Cu toxicity):** Strong L+E. D минимален (monitor) — безопасная структура.

#### LECTURE.003 (Weiss fundamentals) — 30 claims

| Категория | Claims | Primary | Secondary | Анализ |
|-----------|--------|---------|-----------|--------|
| Модель (1.1–1.5) | 5 | L: 3, D: 1, E: 1 | — | 1.1 (L: average property), 1.3 (L: mass not %), 1.2 (D: +20%) |
| Mg AC (2.1–2.8) | 8 | L: 5, E: 3 | — | 2.1–2.6 (L: coefficient corrections), 2.8 (E: monensin effect). Strong L |
| DCAD/K (3.1–3.9) | 9 | L: 4, E: 3, D: 2 | A: 1 | 3.1 (L: equation), 3.7 (L: K antagonism), 3.3 (D: 200–300) |
| Sulfur (4.1–4.8) | 8 | L: 4, E: 3, D: 1 | A: 1 | 4.1 (L: multiple effects), 4.4–4.6 (E: beef data), 4.5 (L: S>>Mo) |
| Trace (5.1–5.8) | 8 | E: 4, L: 2, D: 2 | — | 5.3 (E: 10,000 samples), 5.5 (L: soil contamination) |
| Organic (6.1–6.11) | 11 | E: 5, D: 3, L: 3 | — | 6.1 (D: ask for data), 6.5–6.6 (E: liver Cu), 6.9 (L: free ions) |
| Cu toxicity (7.1–7.6) | 6 | L: 3, E: 2, D: 1 | — | 7.1 (E: norm), 7.2 (L: accumulation), 7.6 (L: S>>Mo) |

**Distribution LECTURE.003:**
- **L (Law):** ~45% — highest among three lectures
- **A (Admissibility):** ~5%
- **D (Deontic):** ~25% — lowest; more descriptive
- **E (Evidence):** ~25% — feed database, studies

**Risk Pattern:** 
- **3.3 (DCAD 200–300):** D с A=US economics. G too narrow for universal D.
- **6.7 (organic Zn):** E с generalization risk. Single study → «organic minerals».

### 2.2 L/A/D/E Cross-Lecture Findings

| Finding | Лекции | Severity | Паттерн | Рекомендация |
|---------|--------|----------|---------|--------------|
| **D без достаточного E/L** | 002 #1.2 (+20%), 001 #5.6 (LA<4%) | 🔴 High | A.6.B | Добавить explicit evidence base или понизить D до «heuristic» |
| **E без L** | 002 #6.4 (vitamin E, mastitis) | ⚠️ Medium | A.6.B | Добавить mechanistic hypothesis или down-grade causal claim |
| **D с узким A, но широким G** | 002 #3.2 (DCAD target), 003 #3.3 (DCAD 200–300) | ⚠️ Medium | A.6.B | Расширить A (US-only) или сузить G |
| **Смешение D/E в одном claim** | 001 #5.1–5.4, 002 #2.3, 003 #6.10 | ⚠️ Medium | A.6.B | Разделить на D-claim и E-claim |
| **E heterogeneous** | 002 #4.3 (S: Cu strong, Se weak) | ⚠️ Medium | A.6.B | Разделить Cu и Se claims |
| **L доминирует — strong** | 003 #2.1–2.6 (Mg AC), 002 #3.1 (DCAD-pH) | ✅ Good | A.6.B | Сохранить структуру при миграции в CS.SOTA |

---

## 3. CausalUse-CAL Audit (FPF C.28)

> **Принцип:** Causal claims распределяются по лестнице Пёрла: Association → Intervention → Counterfactual.  
> **Правило:** Нельзя интерпретировать claim выше, чем позволяет evidence.

### 3.1 Risky Causal Claims by Lecture

#### LECTURE.001 — Causal Rung Assessment (selected)

| # | Claim | Stated Causality | Evidence Type | **Causal Rung** | Gap |
|---|-------|-----------------|---------------|-----------------|-----|
| 1.5 | Геномика → 2 года генерации | Genomic selection → generation interval | Observational trend + breeding program data | **Intervention** | Нет RCT, но breeding program — natural experiment. Rung adequate |
| 4.7 | Limit feeding → cross-suckling | Feed restriction → behavioral change | NASEM 2023 publication | **Intervention** | Если RCT — adequate. Если observational — borderline |
| 5.1–5.4 | LA intake → fat heifers | LA → adipose deposition | Beef steer trial (Fox 1979) | **Association** (for dairy heifers) | 🔴 **Beef data → dairy claim**. Overstated as Intervention for heifers |
| 5.5 | +2% fat per % LA >4% | LA dose → fat % | Speaker approximation | **Heuristic** | Не causal. F2 heuristic |
| 6.5 | Early nutrition → lifetime performance | Calf starter → feedlot performance | Dairy beef/long-fed data | **Association** | «Long-fed calves» — correlation, не proven intervention |

**LECTURE.001 Causal Summary:**
- **Association:** 2 claims (5.1–5.4 for dairy heifers, 6.5) — 40%
- **Intervention:** 2 claims (1.5, 4.7 — if RCT) — 40%
- **Heuristic:** 1 claim (5.5) — 20%
- **Overstated:** 5.1–5.4 (beef→dairy without Bridge), 6.5 (correlation→causation)

#### LECTURE.002 — Causal Rung Assessment (selected)

| # | Claim | Stated Causality | Evidence Type | **Causal Rung** | Gap |
|---|-------|-----------------|---------------|-----------------|-----|
| 2.3 | Mn 60–80 ppm → adequate status | Mn intake → zero balance | Balance study (Weiss) | **Intervention** | Mass balance ≠ RCT, но direct measurement. Adequate |
| 2.10–2.11 | Se yeast → 2× colostrum/fetus | Se source → transfer efficiency | Comparative absorption studies | **Intervention** | Mechanism ясен (selenomethionine). Rung adequate |
| 3.1 | DCAD → hypocalcemia ↓ (via pH) | DCAD → metabolic acidosis → Ca mobilization | Mechanism + repeated experiments | **Intervention** | Very strong. Rung adequate |
| 5.1 | Sulfates → ↓NDF digestion | Sulfate minerals → fiber digestion | Late lactation experiment | **Intervention** (for late lactation), **Association** (transition) | 🔴 **Extrapolation to transition** without direct data |
| 6.4 | Vitamin E excess → mastitis ↑ | Vitamin E intake → mastitis risk | Observational (5 farms, RR=1.7) | **Association** | 🔴 **Observational → causal**. No randomization, mechanism unclear |
| 6.14–6.18 | 25-OH D3 → blood Ca ↑ | D3 metabolite → Ca mobilization | Dose-response experiments | **Intervention** | Adequate, но toxicity at 6 mg — unexplained |

**LECTURE.002 Causal Summary:**
- **Association:** 2 claims (5.1 transition extrapolation, 6.4) — 18%
- **Intervention:** 7 claims — 64%
- **N/A:** 2 claims — 18%
- **Overstated:** 6.4 (observational → causal), 5.1 (late lactation → universal)

#### LECTURE.003 — Causal Rung Assessment (selected)

| # | Claim | Stated Causality | Evidence Type | **Causal Rung** | Gap |
|---|-------|-----------------|---------------|-----------------|-----|
| 2.2–2.3 | Basal Mg AC 30% (not 16%) | Measurement update | Coefficient revision panel | **N/A** | Measurement, не causal |
| 3.7 | 1% K → Mg absorption ↓ 7–8% | K intake → Mg absorption | Multiple intervention studies | **Intervention** | Mechanism ясен (electrical potential). Rung adequate |
| 4.4–4.5 | S intake → ↓liver Cu | S intake → Cu status | Beef controlled study | **Intervention** (beef), **Association** (dairy) | Beef→dairy bridge needed |
| 4.6 | S → ↓Se absorption | S intake → Se absorption | One experiment | **Association** | 🔴 **One study → causal**. Rung overstated |
| 6.7 | Organic Zn → ↓pathogens | Organic Zn → fecal bacteria | Single experiment | **Intervention** (for that product), **Association** (all organic) | 🔴 **Single product → all organic** |

**LECTURE.003 Causal Summary:**
- **Association:** 2 claims (4.6, 6.7 generalization) — 22%
- **Intervention:** 5 claims — 56%
- **N/A:** 2 claims — 22%
- **Overstated:** 4.6 (one study), 6.7 (single product)

### 3.2 CausalUse-CAL Cross-Finding

| Finding | Лекции | Severity | Паттерн | Рекомендация |
|---------|--------|----------|---------|--------------|
| **Beef↔dairy extrapolation без Bridge** | 001 #5.1–5.4, 003 #4.4–4.5 | 🔴 High | C.28 | Создать explicit Bridge card с CL (Congruence Level) и loss notes |
| **Observational overstated as Causal** | 002 #6.4 (vitamin E) | 🔴 High | C.28 | Понизить rung до Association или добавить «mechanism hypothesized» |
| **Single-study generalization** | 003 #4.6 (S→Se), 003 #6.7 (organic Zn) | ⚠️ Medium | C.28 | Добавить boundary: «shown in one study» |
| **Extrapolation beyond direct data** | 002 #5.1 (late lactation → transition) | ⚠️ Medium | C.28 | Добавить explicit scope restriction |
| **Heuristic presented as Law** | 001 #5.5 (+2% fat per % LA) | ⚠️ Medium | C.28 | Понизить до heuristic / rule-of-thumb |
| **No counterfactual claims** | All three | ℹ️ Info | C.28 | Нормально для applied nutrition, но ограничивает predictive power |

---

## 4. Cross-Lecture FPF Analysis

### 4.1 Concordance (F.9 Bridges — без Bridge cards)

| Claim | LECTURE.002 | LECTURE.003 | Concordance Level | FPF Assessment |
|-------|-------------|-------------|-------------------|----------------|
| **S >> Mo для Cu** | 8.6 (S>>Mo) | 4.5 (S>>Mo) | ✅ Strong | Одинаковый источник (Weiss), одинаковый E. Но нет Bridge card с CL |
| **Organic Cu under antagonism ~2×** | 5.5 (~2×) | 6.5 (~2×) | ✅ Strong | Одинаковые liver Cu assay данные |
| **Organic ≠ all same** | 5.7 (ask for data) | 6.1 (ask for data) | ✅ Strong | Идентичный D |
| **Mg 0.4–0.45% pre-fresh** | 2.16 (0.4–0.45%) | — (003 has 0.12–0.15% NASEM) | ✅ Resolved | **Не конфликт**: 002 = dietary recommendation с antagonism; 003 = NASEM absorbed requirement. Different levels of analysis |
| **K → Mg absorption ↓7–8%** | 2.18 (-7–8%) | 3.7 (-7–8%) | ✅ Strong | Идентичные данные, идентичное L |
| **DCAD equation** | 3.1 (implicit) | 3.1 (explicit) | ✅ Strong | Формула стандартна |
| **+20% safety factor** | 1.2 (+20%) | 1.2 (+20%) | ⚠️ Medium | Одинаковый D, но одинаково weak E. Не усиливает друг друга |

### 4.2 Conflict & Resolution

| Conflict | Лекция A | Лекция B | Статус | Resolution |
|----------|----------|----------|--------|------------|
| **Mg requirement: 0.12–0.15% vs 0.4–0.45%** | 003 #2.14 (NASEM absorbed) | 002 #2.16 (practical dietary) | ✅ **Resolved** | Different analysis levels. 003 = model requirement (absorbed). 002 = dietary recommendation with K antagonism + safety. Not a true conflict |
| **DCAD for heifers** | 002 #3.5 (should NOT feed) | — (001 has no DCAD) | ✅ **Resolved** | 002 explicit: heifers more sensitive. No contradiction with 001 |
| **LA and fat heifers** | 001 #5.1–5.7 (LA→fat) | 002/003 (no LA coverage) | ⚠️ **Gap** | No source covers LA for transition cows or heifers. Tom's claim is unique but extrapolated |

### 4.3 Gaps (A.7 — Strict Distinction: what is NOT covered)

| Gap | Почему важно | Рекомендация |
|-----|--------------|--------------|
| **Antioxidant nutrition for bred heifers** | 001 covers heifer growth, 002/003 cover transition cows. Bred heifers (between) — mineral/vitamin needs unclear | Создать CS.ANALYSIS.003: «Bred heifer nutrition gap» |
| **Lactic acid mechanism in dairy (not beef)** | 001 extrapolates beef→dairy. No direct dairy data on LA→fat in heifers | Пометить как «requires peer-review validation» |
| **Organic mineral absorption coefficients** | 003 #6.2: «no company has true AC». 002/003 use relative availability, not true absorption | Создать CS.CORE: «Trace mineral AC — known unknowns» |
| **Regional adaptation of +20% rule** | 002 #1.2: universal +20%. 003 #5.8: «use local data if available». Tension between universal D and local E | Создать Bridge: «NASEM +20% ↔ local forage data» |
| **Water S as hidden source** | 002 #4.4, 003 #4.3: 250 mg/L = +0.1% dietary. But no systematic survey of water S in different regions | Добавить в CS.METHOD: water testing protocol |

---

## 5. Strict Distinction & Evolution Audit (A.7, B.4)

### 5.1 A.7 Strict Distinction

| Аспект | Статус | Finding |
|--------|--------|---------|
| **Object ≠ Description** | ✅ | Claims описывают Object (cattle, diets, minerals). Description = CLAIMS.md files |
| **Description ≠ Carrier** | ⚠️ | Transcript files = Carrier (video → text). CLAIMS.md = Description. Но LECTURE-v2.md смешивает Work (transcription notes) и Description (structured claims) |
| **Role ≠ Work** | ✅ | Speaker = Role (expert). Transcription = Work. Claims = Description of speaker's enacted role |
| **Work evidence** | ⚠️ | Нет separate Work record для transcription process. No timestamps for extraction work |
| **Derivation separation** | ⚠️ | В CLAIMS.md derivation (speaker said) не всегда отделён от evidence (Cornell data). FPF A.10 требует explicit evidenceRef |

### 5.2 B.4 Evolution (Reopen Triggers)

| Лекция | Reopen trigger | Статус |
|--------|---------------|--------|
| **LECTURE.001** | NASEM 2021 Ch.19 Young Calf update; new heifer nutrition research | ❌ Не указан в CLAIMS.md |
| **LECTURE.002** | NASEM 2021 revision; new DCAD meta-analysis; 25-OH D3 regulatory changes | ⚠️ Частично (NASEM 2021 mentioned, но не как reopen trigger) |
| **LECTURE.003** | NASEM 2021 revision; new Mg AC studies; K antagonism research | ⚠️ Частично (NASEM 2021 updates implicit) |

**Рекомендация:** Добавить `reopen_trigger` в YAML frontmatter каждого CLAIMS.md перед миграцией в CS.SOTA.

---

## 6. Recommendations перед миграцией в CS.SOTA

### 6.1 Обязательные (MUST)

| # | Действие | FPF Pattern | Приоритет |
|---|----------|-------------|-----------|
| 1 | **Создать Bridge card** для beef↔dairy extrapolation (LA→fat heifers, 001 #5.1–5.7) с CL=Medium и loss notes | F.9 | 🔴 Critical |
| 2 | **Понизить causal rung** для 002 #6.4 (vitamin E → mastitis) с Intervention до Association | C.28 | 🔴 Critical |
| 3 | **Разделить D и E** в 001 #5.1–5.4: D (SHOULD <4% LA) и E (beef steer data 1979) — separate claims | A.6.B | 🔴 Critical |
| 4 | **Добавить reopen_trigger** в YAML frontmatter всех трёх CLAIMS.md | B.4 | ⚠️ High |
| 5 | **Пересмотреть confidence** для 001 #5.5 (0.75 → более низкий или F2-marked) и 001 #9.3–9.4 (0.75 → product claim) | B.3 | ⚠️ High |

### 6.2 Рекомендуемые (SHOULD)

| # | Действие | FPF Pattern | Приоритет |
|---|----------|-------------|-----------|
| 6 | **Создать Bridge card** для NASEM +20% ↔ local forage data (002 #1.2 vs 003 #5.8) | F.9 | ⚠️ High |
| 7 | **Добавить explicit G (Scope)** к каждому Key Claim при миграции в CS.SOTA | B.3 | ⚠️ High |
| 8 | **Разделить heterogeneous E** в 002 #4.3 (Cu strong, Se weak) на separate claims | A.6.B | ⚠️ High |
| 9 | **Создать explicit evidenceRef** для каждого claim (Cornell → Van Amburgh PhD, etc.) | A.10 | ⚠️ Medium |
| 10 | **Добавить Work record** для transcription + extraction process | A.15 | ⚠️ Medium |

### 6.3 Желательные (MAY)

| # | Действие | FPF Pattern | Приоритет |
|---|----------|-------------|-----------|
| 11 | **Создать CS.ANALYSIS.003**: «Bred heifer nutrition gap» — анализ gap между 001 (growth) и 002 (transition) | B.2 (MHT) | ℹ️ Low |
| 12 | **Создать CS.CORE**: «Trace mineral AC — known unknowns» — каталог неопределённостей | A.11 | ℹ️ Low |
| 13 | **Проверить DesignRunTag feedback** после первого использования CS.SOTA в formulation | B.4 | ℹ️ Low |

---

## Appendix A: F-G-R Quick Reference

| F | Описание | Примеры из аудита |
|---|----------|-------------------|
| F2 | Expert rule-of-thumb, heuristic | +20% rule (002), iPad product (001), LA approximation (001) |
| F3 | Structured expert text с цифрами | Большинство claims во всех трёх лекциях |
| F4 | Foundational principle, checked specification | Requirements in mass (003), Mg AC 30% (003), gestation fixed (001) |

| R | Описание | Примеры |
|---|----------|---------|
| Low-Medium | Single source, product claim, heuristic | LA approximation (001), iPad camera (001) |
| Medium | One study, modeling data, practice-based | Cornell data (001), +20% rule (002), organic Zn (003) |
| Medium-High | Multiple studies, strong mechanism | Mn balance (002), Se transfer (002), Mg with K (003) |
| High | Repeated experiments, panel review | NASEM 2021 Mg AC (003), DCAD mechanism (002) |
| Very High | Universal mechanism, mathematical truth | Gestation fixed (001), mass≠concentration (003), Cu accumulation (002) |

---

> **Конец документа CS.ANALYSIS.002**
> *FPF Audit для LECTURE.001–003 | PACK-cattle-science | 2026-06-01*
