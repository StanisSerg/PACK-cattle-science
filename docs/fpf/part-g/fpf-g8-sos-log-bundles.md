---
type: fpf-study
pattern: G.8
title: "SoS-LOG Bundles: упаковка правил и лестниц зрелости"
domain: cattle-science
difficulty: advanced
reading_time: 26 min
created: 2026-06-27
fpf_context: ["G.8", "C.23", "G.4", "G.5", "G.6", "G.Core"]
---

# G.8 — SoS-LOG Bundles: упаковка правил и лестниц зрелости

> **Цель capture:** объяснить, как паттерн G.8 упаковывает SoS-LOG правила, лестницы зрелости и admissibility traces в selector-facing bundle, не вводя пороги в правила и не смешивая трихотомию guard с другими статусами.

---

## 1. Зачем это читать

В скотоводстве семейства методов конкурируют внутри одного CG-Frame: разные протоколы профилактики кетоза, разные системы мониторинга, разные подходы к кормлению. SoS-LOG правила (C.23) помогают принимать tri-state решения о допустимости методов, а лестницы зрелости показывают, насколько метод готов к применению. G.8 упаковывает эти артефакты в UTS-citable bundle, который может потреблять G.5.

> **FPF-тезис:** *«Правила и лестницы зрелости публикуются как отдельный bundle; пороги и acceptance остаются в CAL.»*

**Фермерский пример:**

> Фермер оценивает, можно ли внедрить новую систему мониторинга BHB. SoS-LOG bundle содержит правила: «pass — если есть validation study на целевой породе», «degrade — если validation есть, но на другой породе», «abstain — если validation отсутствует». Лестница зрелости показывает, что система находится на rung «validated_in_lab», а не «field_proven». Пороги применимости (например, BHB ≥ 1,2) живут в CAL, а не в LOG.

---

## 2. История одной ошибки

Хозяйство внедрило программу мониторинга, которая объявила метод «зрелым», когда у него был только лабораторный validation. В правилах программы был статус «почти готов», который не соответствовал ни pass, ни degrade, ни abstain. Когда метод начал давать ложные результаты в полевых условиях, никто не мог объяснить, почему он был допущен. Если бы использовался G.8 bundle с tri-state guard и maturity ladder, статус был бы явным, а пороги — в CAL.

---

## 3. SoS-LOG Bundles — полное описание

### 3.1 Определение

**SoS-LOG Bundle** — это selector-facing, UTS-citable упаковочный объект, который связывает SoS-LOG rule ids (C.23), maturity ladder card, Acceptance clause ids (G.4), EvidenceGraph paths (G.6) и refresh hooks (G.11). Bundle не содержит порогов и не переопределяет rule semantics.

### 3.2 Почему это важно

Правила и лестницы зрелости часто разбросаны по документам, дашбордам и чек-листам. G.8 собирает их в один bundle, делает их citable и гарантирует, что thresholds остаются в CAL. Это позволяет G.5 dispatch'ить методы на основании явных admissibility traces.

### 3.3 SoS-LOG.Rule

**Определение.** SoS-LOG.Rule — это идентификатор правила, задающего tri-state decision schema {pass | degrade(mode) | abstain} для пары (TaskSignature, MethodFamily).

**Пояснение.** Семантика правил определяется C.23. G.8 только упаковывает rule ids и binding pins. Это предотвращает shadow spec: правила не переопределяются локально.

**Пример из животноводства.**

```text
RULE-001: «IF validation_study_on_target_breed THEN pass"
RULE-002: «IF validation_study_exists BUT NOT target_breed THEN degrade(mode = adapt_thresholds)"
RULE-003: «IF NO validation_study THEN abstain"
```

**Ключевой признак.** SoS-LOG.Rule — это id, ссылающийся на C.23; семантика не раскрывается в bundle.

### 3.4 SoS-LOGBundle@Context

**Определение.** SoS-LOGBundle@Context — это UTS-публикуемый объект, содержащий CG-FrameContext, MethodFamilyId, RegistrationContext, SoSLogRuleId[], MaturityCardRef, AcceptanceClauseId[], EvidenceGraphId/PathId и опциональные crossing/telemetry pins.

**Пояснение.** Bundle связывает правила, acceptance, evidence и maturity в одном месте. Он не вводит новых legality gates и не содержит numeric thresholds.

**Пример из животноводства.**

```text
BUNDLE-001:
  - CGFrameContext: ketosis_prevention_FarmA
  - MethodFamilyId: {MF-001, MF-002}
  - SoSLogRuleId: [RULE-001, RULE-002, RULE-003]
  - MaturityCardRef: MC-001
  - AcceptanceClauseId: [AC-001, AC-002]
  - EvidenceGraphId: EG-001
```

**Ключевой признак.** Bundle содержит ids, а не семантику; thresholds ссылаются на G.4.

### 3.5 AdmissibilityLedger@Context

**Определение.** AdmissibilityLedger@Context — это run-time ledger, который фиксирует outcomes guard-решений (pass/degrade/abstain), cited evidence paths, branch tokens и policy pins.

**Пояснение.** Ledger делает admissibility traceable. Каждая строка связывает MethodFamily, SoSLogRule, guard decision, MaturityRungId, AcceptanceClauseId и PathId/PathSliceId.

**Пример из животноводства.**

```text
AL-001:
  - MethodFamilyId: MF-001 (propylene_glycol_protocol)
  - SoSLogRuleId: RULE-001
  - GuardDecision: pass
  - MaturityRungId: field_proven
  - AcceptanceClauseId: AC-001
  - PathId: P-001
```

**Ключевой признак.** AdmissibilityLedger содержит guard outcomes с PathId/PathSliceId и policy pins.

### 3.6 Maturity ladder

**Определение.** Maturity ladder — это ordinal/poset лестница зрелости, опубликованная как отдельный UTS-артефакт, с closed rungs и declared ReferencePlane.

**Пояснение.** Maturity ladder не содержит thresholds. Она показывает, на какой ступени находится метод: conceptual, lab_validated, field_pilot, field_proven. Переходы между ступенями обосновываются evidence paths.

**Пример из животноводства.**

| MaturityRungId | Label | Evidence requirement |
|---|---|---|
| MR-1 | conceptual | claim exists |
| MR-2 | lab_validated | validation study |
| MR-3 | field_pilot | pilot on target farm type |
| MR-4 | field_proven | multi-farm field study |

**Ключевой признак.** Maturity ladder — ordinal/poset, без thresholds, с closed UTS-registered rungs.

### 3.7 No thresholds in LOG

**Определение.** Числовые пороги, maturity floors и acceptance gates не должны быть встроены в SoS-LOG rules или ladder rungs; они живут в G.4 Acceptance.

**Пояснение.** Это разделение предотвращает смешение LOG-семантики (допустимость) и CAL-семантики (пороги). Rule говорит «метод допустим, если есть validation»; CAL говорит «применяй, если BHB ≥ 1,2».

**Пример из животноводства.** Правило «pass — если validation study on target breed» не содержит порога BHB. Порог BHB ≥ 1,2 находится в AC-001.

**Ключевой признак.** В bundle и ladder не встречаются числовые значения типа «≥ 1,2»; они ссылаются на AcceptanceClauseId.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Метод зрелый, если он прошёл пилот и BHB снижается на 0,3.»*

**Разложение по G.8:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «метод зрелый» | MaturityRungId | Относится к лестнице зрелости |
| «прошёл пилот» | SoS-LOG rule condition | Условие допустимости |
| «BHB снижается на 0,3» | Acceptance threshold (G.4) | Числовой порог не в LOG |

**Основные риски смешивания:**

1. **Threshold leak.** Числовые пороги оказываются в rule text, их сложно изменить.
2. **Мaturity становится scalar.** «Зрелость» превращается в число, а не ordinal/poset.
3. **Auditability brittle.** Нет явной связи между rule outcome и evidence path.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** оценка готовности нового метода профилактики кетоза.

**Было (смешанное / нечёткое):**
> «Метод зрелый, потому что в пилоте BHB снизился.»

**Стало (разложенное / ясное):**

**SoS-LOG bundle BUNDLE-001:**
> MethodFamilyId: MF-004 (new metabolic bolus)
> SoSLogRuleId: [RULE-001, RULE-002, RULE-003]
> MaturityCardRef: MC-001
> AcceptanceClauseId: [AC-005, AC-006]
> EvidenceGraphId: EG-002

**Maturity ladder MC-001:**
> MR-2: lab_validated (current)
> MR-3: field_pilot (target)

**AdmissibilityLedger AL-002:**
> MF-004, RULE-002, degrade(mode = field_pilot_required), MaturityRungId MR-2, PathId P-003.

**CAL thresholds:**
> AC-005: IF BHB ≥ 1.2 THEN consider method.
> AC-006: IF BHB_reduction ≥ 0.3 THEN acceptable efficacy.

**Результат:**
- LOG-решение (degrade) отделено от CAL-порогов.
- Зрелость явна и отслеживается.
- Аудитор видит evidence path для каждого статуса.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Определите MethodFamilyId и TaskSignature для вашего CG-Frame.

**Шаг 2.** Соберите SoSLogRuleId из C.23, не переопределяя их семантику.

**Шаг 3.** Создайте MaturityCard с closed rungs и declared ReferencePlane.

**Шаг 4.** Ссылайтесь на AcceptanceClauseId из G.4, не встраивая пороги в bundle.

**Шаг 5.** Настройте AdmissibilityLedger, фиксируя guard outcomes и PathId.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| В SoS-LOG rule есть числовые пороги? | Пороги должны быть в CAL acceptance clauses. |
| Maturity ladder имеет незарегистрированные rungs? | Лестница должна иметь closed UTS-registered rungs. |
| AdmissibilityLedger не ссылается на PathId? | Outcome не проверяем. |
| Введён статус вроде «почти pass»? | Нарушена трихотомия guard. |
| Bundle переопределяет rule semantics? | Нарушено no-shadow-specs; нужно цитировать C.23. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| C.23 | определяет семантику SoS-LOG rules |
| G.4 CAL Authoring | предоставляет AcceptanceClauseId и thresholds |
| G.5 Method Dispatcher | потребляет bundle и ledger для dispatch |
| G.6 Evidence Graph | предоставляет PathId/PathSliceId для ledger |
| G.Core | гарантирует tri-state guard и set-return semantics |

---

## 9. Что запомнить

1. G.8 упаковывает SoS-LOG rules, maturity ladder и admissibility traces.
2. Правила не содержат порогов; пороги живут в CAL.
3. Maturity ladder — ordinal/poset с closed UTS-registered rungs.
4. AdmissibilityLedger фиксирует guard outcomes с evidence paths.
5. Bundle — selector-facing артефакт, не заменяющий C.23 или G.4.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.8*
