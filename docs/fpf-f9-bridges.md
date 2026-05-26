---
type: fpf-study
pattern: F.9
title: "Bridges: как переносить знания из одного мира в другой, не разрушая их"
domain: cattle-science
difficulty: medium
reading_time: 15 min
created: 2026-05-26
---

# F.9 — Alignment & Bridge across Contexts

## 1. Зачем это читать

Если вы когда-нибудь говорили *«в NASEM-2021 написано то же самое»* — вы построили мост. Но спросите себя: **какой именно мост?** Полностью эквивалентный? Частично перекрывающийся? Названный одинаково, но означающий другое?

В мире науки о кормлении это случается постоянно:
- NASEM-2021 говорит «требование» в массе элементов, а европейские системы — в %
- «DCAD» у Weiss (механизм, pH) и «DCAD» у формулировщика (практическая цель, mEq/kg) — разные вещи
- Исследование в Новой Зеландии (pasture, high K) и исследование в США (TMR, controlled) — одинаковые термины, разные контексты

F.9 говорит: *«Мосты нужны не для того, чтобы доказать, что всё одинаково. Мосты нужны для того, чтобы явно записать, что теряется при переходе»*.

---

## 2. История одной ошибки

Представьте зоотехника, который читает:

- **SoTA 1 (Weiss, webinar):** «Mg 0.4–0.45% pre-fresh для снижения гипокальциемии»
- **SoTA 2 (NASEM-2021):** «Mg requirement = 0.16% от сухого вещества»

Зоотехник думает: «Weiss говорит 0.4%, NASEM говорит 0.16%. Кто-то неправ».

Но это **не противоречие**. Это **разные контексты**:
- Weiss: практическая рекомендация для **pre-fresh коров** на **high-K рационах** с учётом антагонизма K
- NASEM: **базовое требование** для **средней дойной коровы** без учёта антагонистов

Проблема не в цифрах. Проблема в **отсутствии моста** между двумя контекстами. Если бы был explicit Bridge:

> «Weiss 0.4% pre-fresh → NASEM 0.16% base: **Broader-than** (Weiss включает safety margin + K antagonism). CL = Medium. Loss: K context, stage specificity, source variability.»

— зоотехник понял бы: 0.4% не заменяет 0.16%, а **дополняет** её для конкретных условий.

F.9 предотвращает «string-equals fallacy»: одинаковое написание ≠ одинаковое значение.

---

## 3. Что такое Bridge

Bridge — это **явно объявленный перевод** между двумя локальными смыслами (SenseCells) из разных контекстов.

Каждый Bridge **обязан** содержать:
1. **Два SenseCell'а:** что связываем (с контекстами)
2. **Bridge kind:** какая связь (эквивалентность, перекрытие, включение, объяснение)
3. **Direction:** симметрично или однонаправленно
4. **CL (Congruence Level):** насколько смысл переносится без потерь
5. **Loss Notes:** что именно теряется при переходе

### 3.1 Виды Bridges

**Substitution Bridges** (сохраняют senseFamily — можно подставлять):

| Вид | Что означает | Пример |
|---|---|---|
| **Equivalence** | Почти тождество | NASEM-2021 Mg req ↔ NRC-2001 Mg req (CL=High, minor editorial differences) |
| **Narrower-than / Broader-than** | Одно включает другое | «Weiss pre-fresh Mg» ⊃ «NASEM base Mg» — Weiss broader |
| **Partial-overlap** | Пересечение, но ни одно не включает другое | «DCAD у Weiss» ∩ «DCAD у формулировщика» — overlap, но не identity |
| **Disjoint** | Явное различие | «Мг требование в %» vs «Мг требование в массе» — disjoint until explicit conversion |

**Interpretation Bridges** (cross-senseFamily — только объяснение, не подстановка):

| Вид | Что означает | Пример |
|---|---|---|
| **Design-spec → Run-trace** | Концепция ↔ её run-time проявление | «NASEM model» → «фактический рацион на ферме А» |
| **Measure-of / Evidence-for** | Измерение ↔ то, что оно измеряет | «BHB в крови» → «кетозный статус» |
| **Policy-implies** | Правило ↔ поведение, которое оно ограничивает | «Se limit 0.3 ppm» → «максимальная доза premix» |

### 3.2 CL — Congruence Level

CL = насколько безопасно переносить смысл.

| CL | Название | Что позволено | Пример |
|---|---|---|---|
| **CL3** | Verified equivalence | Полная подстановка | «NASEM-2021 Mg req = NRC-2001 Mg req» (verified by committee) |
| **CL2** | Validated mapping | Подстановка с оговорками | «Weiss pre-fresh Mg ⊃ NASEM base Mg» (validated by mechanism) |
| **CL1** | Plausible mapping | Только именование, не подстановка | «DCAD у Weiss ≈ DCAD у формулировщика» ( plausible, но разные «языки») |
| **CL0** | Tentative guess | Только ориентация, никакой подстановки | «Возможно, NZ pasture data применимо к US TMR» (guess) |

**Ключевое правило:** Низкий CL **штрафует** aggregate trust (R_eff), но **не оправдывает** подстановки.

---

## 4. Каскад типичных ошибок

| Ошибка | Симптом | Пример |
|---|---|---|
| **String-equals fallacy** | Одинаковое написание = одинаковое значение | «DCAD» у Weiss и у формулировщика |
| **Scope creep** | Naming convenience растянута до assignment | «У них работает MgCl₂, значит, и у нас будет» (NZ pasture ≠ US TMR) |
| **Direction amnesia** | Асимметричное отношение treated as symmetric | «Weiss ⊃ NASEM» → «заменяем NASEM на Weiss» (unsafe!) |
| **Loss blindness** | Различия не записаны | «Просто пересчитай % в массу» — без записи о потере precision |
| **DesignRunTag jumping** | Design artifact substituted for run-time | «NASEM говорит 0.16%» → «наша корова получает 0.16%» (model ≠ reality) |

---

## 5. Как это выглядит на ферме: Bridge cards

**Bridge Card 1: Mg requirements**

```
Bridge ID: BRIDGE.001
From: CS.SOTA.332 #4 (Weiss) — «Mg basal 30%, MgO ~40%, MgSO4 ~50%»
To: CS.SOTA.301 (NASEM-2021) — «Mg AC: basal 30%, oxide 40%, sulfate 50%»
Kind: Equivalence
Direction: Symmetric
CL: High (CL3)
Loss Notes: «Weiss — verbal description, NASEM — formal specification. Values match, provenance differs.»
```

**Bridge Card 2: DCAD — pH vs mEq/kg**

```
Bridge ID: BRIDGE.002
From: CS.SOTA.331 #5 (Weiss) — «DCAD effective if urinary pH < 7»
To: CS.SOTA.332 #8 (Weiss) — «DCAD optimal 200–300 mEq/kg»
Kind: Partial-overlap
Direction: Symmetric (but disconnected languages)
CL: Medium (CL1)
Loss Notes: «331 — mechanism language (pH). 332 — practical target (mEq/kg). No explicit conversion formula published. pH 6.5–6.7 ≈ mEq/kg -100 to -200? Unverified.»
```

**Bridge Card 3: Se yeast — transition vs dry cows**

```
Bridge ID: BRIDGE.003
From: CS.SOTA.331 #2 — «2/3 yeast for transition»
To: CS.SOTA.332 #14 — «≥50% yeast for dry cows»
Kind: Narrower-than (331 ⊂ 332)
Direction: 331 → 332 (safe), 332 → 331 (unsafe without check)
CL: High (CL2)
Loss Notes: «Transition cows ⊂ dry cows. 331 narrower scope. Safe to apply 332 to transition if 50% ≥ 2/3.»
```

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Найдите два источника в вашем PACK с «похожими» claim'ами.

**Шаг 2.** Задайте вопросы:
- Это действительно одно и то же? (Equivalence — редкость)
- Одно включает другое? (Narrower/Broader)
- Есть пересечение, но не тождество? (Partial-overlap)
- Это вообще разные вещи? (Disjoint)

**Шаг 3.** Определите CL:
- CL3: проверено комитетом или формальным доказательством
- CL2: механизм объясняет связь
- CL1: похоже, но не проверено
- CL0: догадка

**Шаг 4.** Запишите Loss Notes. Что теряется при переходе?
- Единицы измерения?
- Контекст (страна, сезон, порода)?
- Методология (observational vs RCT)?

**Шаг 5.** Создайте Bridge card. Не полагайтесь на память.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Используете ли вы термины из разных источников как взаимозаменяемые? | String-equals fallacy |
| Переносите ли результаты с NZ pasture на US TMR без оговорок? | Scope creep |
| Считаете ли вы отношение «Weiss ⊃ NASEM» симметричным? | Direction amnesia |
| Записываете ли вы, что теряется при переходе между источниками? | Loss blindness |
| Подменяете ли вы модель (NASEM) реальностью (фактический рацион)? | DesignRunTag jumping |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---------|-------|
| A.1.1 BoundedContext | Bridge связывает два BoundedContext'а |
| B.3 F-G-R | CL штрафует R при агрегации |
| A.6.9 RPR-XCTX | Repairing cross-context «same/equivalent/align» |
| C.26 Cross-Context Transport | Bridges — семантическая основа для transport |
| E.17 MVPK | Bridge card — один из видов MVPK publication |

---

*Capture создан в рамках WP-1 (Саморазвитие — изучение FPF).*
*FPF Source: FPF/FPF-Spec.md §F.9*