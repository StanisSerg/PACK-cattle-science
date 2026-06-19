---
type: fpf-study
pattern: E.16
title: "Autonomy Budget & Guard Rails: автономия только в рамках бюджета"
domain: cattle-science
difficulty: intermediate
reading_time: 25 min
created: 2026-06-19
---

# E.16 — Autonomy Budget & Guard Rails: автономия только в рамках бюджета

## 1. Зачем это читать

Если на вашей ферме появляется робот, ИИ-советчик или автоматическая система, которая принимает решения без постоянного контроля человека, — вы уже в зоне E.16. Этот паттерн учит **делать любое заявление об автономии проверяемым, ограниченным и останавливаемым**.

**FPF-тезис:** *«Автономия — не право действовать без ограничений. Автономия — это выделенный бюджет с явными guard rails, ledger и процедурой override.»*

В животноводстве автономные системы становятся обычным делом: кормораздатчики, роботы-дояры, сенсоры отёла, ИИ-рекомендации по лечению. Без E.16 «автономность» превращается в чёрный ящик: система делает что-то, но никто не может сказать, в рамках какого разрешения и что делать при превышении лимита.

**Фермерский пример:**

> Ферма купила автономный кормораздатчик, который сам решает, сколько корма давать каждой группе. Через месяц оказалось, что он недокормил высокопродуктивных коров в жару, потому что «решение» основывалось на средних показателях. Никто не знал: какой у него бюджет решений, кто может его остановить, какие guard rails действуют.

E.16 требует: перед запуском автономной системы опубликовать `AutonomyBudgetDecl` — с scope, quota, guard, override protocol и ledger.

## 2. История одной ошибки

Ферма «Луговое» внедрила ИИ-сервис, который рекомендовал лечение мастита. Сервис работал «автономно» в том смысле, что генерировал рекомендации без участия ветеринара.

- **Бюджета не было.** Сколько рекомендаций в день? Какие риски допустимы? Неизвестно.
- **Guard rails отсутствовали.** Система предложила антибиотик корове с аллергией, потому что не проверяла историю.
- **Override было не ясно.** Ветеринар мог отменить рекомендацию, но эта отмена не фиксировалась; система продолжала учиться на отменённых случаях.
- **Ledger не вёлся.** Нельзя было аудиторски восстановить: сколько решений принято, сколько отменено, по каким причинам.

E.16 предлагает оформить автономию как **declared, versioned, auditable contract**:
- `AutonomyBudgetDecl` — что разрешено;
- `Aut-Guard policy` — при каких условиях;
- `OverrideProtocol` — кто и как останавливает;
- `AutonomyLedger` — журнал каждого решения.

## 3. RoC-Autonomy Budget & Enforcement — полное описание

> **Соответствие с FPF-Spec.** В реестре паттерн назван *Autonomy Budget & Guard Rails*. В спецификации FPF он развивается под именем *RoC-Autonomy Budget & Enforcement* — см. §E.16.

### 3.1 Условие применения

**Вопрос:** Когда E.16 обязателен?

**Ответ:** Всякий раз, когда `Role`, `Method` или `Service` заявляет об **автономном поведении** — то есть принимает решение или совершает действие без непрерывного подтверждения человеком в момент исполнения. Чисто рекомендательные системы, где каждое действие подтверждает человек, не подпадают.

**На ферме:**
| Система | Автономия? | Почему |
|---|---|---|
| Робот-дояр | Да | Совершает физические действия без подтверждения |
| Автокормушка | Да | Распределяет корм по своему алгоритму |
| Сенсор отёла с SMS-оповещением | Нет | Только уведомляет; решение принимает человек |
| ИИ-рекомендация лечения | Да, если назначает без ветеринара | Решение о лечении без подтверждения |
| Дашборд аналитики | Нет | Только отображает данные |

**Ключевой признак:** если система действует без immediate human confirmation — нужен `AutonomyBudgetDecl`.

### 3.2 AutonomyBudgetDecl — обязательный артефакт

**Вопрос:** Что должно быть в декларации?

**Ответ:**
- `id` и `version` — идентификация и edition pin;
- `scope` — `ClaimScope`, где бюджет действует;
- `budget` — typed quota: action tokens, decision tokens, risk bands, resource caps, time window;
- `AdmissibilityConditionsId` — политика guard rails;
- `overrideProtocolRef` — протокол SpeechActs для pause/resume/escalate;
- `telemetrySpecRef` — что записывать в ledger;
- `editionPins` — привязка к Role, Method, CHR refs.

**На ферме:**
```text
AutonomyBudgetDecl: AutoFeeder_v3_FarmA
  scope: FarmA.LactatingCows.HighYieldGroup
  budget:
    action_tokens: 48 dispenses/day
    decision_tokens: 24 ration_adjustments/day
    risk_bands: {BCS_deviation ≤ 0.25, MilkYield_drop ≤ 5%}
    resource_caps: {feed_inventory ≥ 2 days, energy ≥ baseline}
    time_window: 24h rolling
  AdmissibilityConditionsId: AutGuard_AutoFeeder_v3
  overrideProtocolRef: AutoFeeder_Override_Protocol_v1
  telemetrySpecRef: AutoFeeder_Telemetry_v2
  editionPins:
    RoleRef: AutoFeederRole_v2
    MethodDescRef: AutoFeeding_v3
    CHR refs: FeedAllocationCHR, BodyConditionCHR
```

**Ключевой признак:** бюджет — это не абстрактное «не навреди», а набор типизированных quota и условий.

### 3.3 Guarded enactment и ledger

**Вопрос:** Как система узнаёт, что ей можно действовать?

**Ответ:** Через **Green-Gate**: перед каждым действием проверяются:
- валидность `RoleAssignment`;
- остаток бюджета в текущем `Γ_time` окне;
- guard checks из `AdmissibilityConditionsId`.

Если любая проверка не проходит — действие **блокируется** (нет «soft warning»).

Каждое допущенное действие записывается в `AutonomyLedgerEntry`:
- `workId`, `performedBy: RoleAssignmentId`;
- `budgetId`, `version`, `time`;
- deltas по tokens, risk, resources;
- `guardVerdicts`;
- `pathIds` / `pathSliceIds` для parity/refresh.

**Ключевой признак:** без ledger entry автономное действие не считается admitted Work.

### 3.4 Override и Separation of Duties

**Вопрос:** Кто может остановить автономную систему?

**Ответ:** Любая роль, объявленная в `OverrideProtocolRef`, но **не та же `RoleAssignment`, которая потребляет бюджет**. Canonical SpeechActs:
- `PauseAutonomy(budgetId)` — немедленная остановка;
- `ResumeAutonomy(budgetId)` — возобновление после условий;
- `NarrowAutonomy(budgetId, Δscope)` — ужесточение лимитов;
- `Escalate(budgetId)` — передача supervisor.

**На ферме:**
> `HerdManagerRole` может вызвать `PauseAutonomy(AutoFeeder_v3_FarmA)`, если робот-дояр начинает доить корову с клиническим маститом. `HerdManagerRole` и `AutoFeederRole` — disjoint (SoD).

**Ключевой признак:** override — это Work (SpeechAct) с ledger entry и проверкой SoD.

### 3.5 Исчерпание бюджета

**Вопрос:** Что происходит, когда бюджет закончился?

**Ответ:**
- Блокировка дальнейших автономных действий в том же `Γ_time` окне;
- Эмиссия `DepletionNotice`;
- Либо `Escalate`, либо `Park` согласно политике;
- Возобновление только через `ResumeAutonomy` SpeechAct от допустимой роли после прохождения guard checks.

## 4. Почему смешивать / игнорировать — значит рисковать

Возьмём фразу: *«Наша система автономно управляет кормлением.»*

**Разложение по E.16:**

| Часть утверждения | Что это в FPF | Почему |
|---|---|---|
| «система» | `U.Service` / performer | Нужен `RoleAssignment` |
| «автономно управляет» | autonomy claim | Нужен `AutonomyBudgetDecl` |
| «кормлением» | `U.Work` / `U.Method` | Нужен MethodRef и WorkPlan |
| (скрытое) «безопасно» | guard claim | Нужен `AdmissibilityConditionsId` |

**Что плохого в смешивании:**

1. **Нетестируемость.** «Автономно» без бюджета нельзя проверить.
2. **Риск неконтролируемых действий.** Система может действовать вне remit.
3. **Растворение ответственности.** Если что-то пошло не так, непонятно, кто отвечал.
4. **Несравнимость.** Нельзя сравнить две автономные системы без опубликованных UTS-полей.

## 5. Как это выглядит на ферме: правильное применение

**Задача:** внедрить автономный кормораздатчик для высокопродуктивных коров.

**Было (смешанное / нечёткое):**
> «Робот сам решает, сколько корма давать, исходя из данных.»

**Стало (разложенное / ясное):**

**AutonomyBudgetDecl:**
> `id`: ABD-AutoFeeder-HY-FarmA
> `version`: 2026-06-19-v1
> `scope`: `FarmA.LactatingCows.HighYieldGroup`
> `budget`:
> - `action_tokens`: 48 dispenses/24h
> - `decision_tokens`: 2 ration_mix_changes/24h
> - `risk_bands`: `MilkYield_7d_drop ≤ 5%`; `BCS_change ≤ 0.1/14d`
> - `resource_caps`: `min_feed_inventory ≥ 48h`
> - `time_window`: 24h rolling
> `AdmissibilityConditionsId`: AG-AutoFeeder-HY-v1
> `overrideProtocolRef`: OP-AutoFeeder-HY-v1
> `telemetrySpecRef`: TL-AutoFeeder-HY-v1
> `editionPins`: `AutoFeederRole_v2`, `AutoFeedingMethod_v3`, `MilkYieldCHR`, `BCSCHR`

**Green-Gate example:**
> Перед каждой выдачей корма робот проверяет:
> 1. `RoleAssignment` активен.
> 2. `action_tokens > 0` в текущем 24h окне.
> 3. `MilkYield_7d_drop ≤ 5%` и `BCS_change ≤ 0.1/14d`.
> 4. `feed_inventory ≥ 48h`.
> Если хоть одно нарушено — выдача блокируется, отправляется `DepletionNotice` или `Escalate`.

**AutonomyLedgerEntry example:**
> `workId`: W-2026-0619-AF-003
> `performedBy`: `AutoFeederRole#Unit_07`
> `budgetId`: ABD-AutoFeeder-HY-FarmA
> `deltas`: action_tokens −1; decision_tokens 0; risk band within limit
> `guardVerdicts`: all pass
> `pathSliceId`: PS-HY-2026-06-19

**Override:**
> `HerdManagerRole#Ivanov` вызывает `PauseAutonomy(ABD-AutoFeeder-HY-FarmA)` при обнаружении неисправности. SoD: `HerdManagerRole ⊥ AutoFeederRole`.

**Что это даёт:**
- Любой аудитор видит, в рамках какого контракта действует робот.
- Превышение лимита останавливает систему, а не игнорируется.
- Ответственность за override чётко распределена.

## 6. Практическое применение: с чего начать

**Шаг 1.** Перечислите все системы на ферме, которые действуют без immediate human confirmation.

**Шаг 2.** Для каждой системы создайте `AutonomyBudgetDecl`: scope, budget (action/decision tokens, risk bands, resource caps, time window), AdmissibilityConditionsId, overrideProtocolRef, telemetrySpecRef, editionPins.

**Шаг 3.** Убедитесь, что Method steps, требующие автономии, декларируют `requiresAutonomyBudget`.

**Шаг 4.** Настройте ledger: каждое admitted Work должно создавать `AutonomyLedgerEntry`.

**Шаг 5.** Определите override SpeechActs и SoD: кто может pause/resume/escalate, и почему эта роль не совпадает с потребителем бюджета.

**Шаг 6.** Добавьте autonomy-поля в UTS rows для этой системы.

**Шаг 7.** Проведите drill: смоделируйте исчерпание бюджета и убедитесь, что система блокируется и эскалирует.

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Система называется «автономной», но нет `AutonomyBudgetDecl`? | Autonomy-by-label; E.16‑S1 нарушен. |
| Guard checks только предупреждают, но не блокируют? | Soft gates; E.16‑S2 нарушен. |
| Override может выполнить та же роль, что и потребитель бюджета? | SoD collapse; E.16‑S4 нарушен. |
| Ledger не привязан к `U.Work` или не содержит deltas? | Нет audit trail; E.16‑S3 нарушен. |
| Бюджет исчерпан, но система продолжает работать? | Depletion behavior не реализован; E.16‑S5 нарушен. |
| UTS row не содержит autonomy-полей? | Несравнимость; E.16‑S6 нарушен. |

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.2 Role Taxonomy | роли потребителя и overrider бюджета. |
| A.15 Role–Method–Work Alignment | Work и ledger entries. |
| A.21 Gate Profile | Green-Gate и gate checks. |
| C.9 Agency-CHR | измерение автономии и ответственности. |
| C.16 Measurement | типизация budget deltas через MM-CHR. |
| E.8 Pattern Authoring Discipline | шаблон оформления autonomy pattern. |
| E.10 LEX-BUNDLE | лексические правила: «автономно» — trigger word. |
| E.18 Transformation Flow Structure | scout/probe/commit partition при bounded specialization. |
| F.17 UTS | публикация autonomy-полей для parity/selection. |
| G.5/G.9/G.10 | method authoring, parity и shipping с учётом autonomy. |

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.16*
