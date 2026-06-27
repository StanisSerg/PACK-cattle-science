---
type: fpf-study
pattern: E.16
title: "Autonomy Budget & Guard Rails: автономия только в рамках бюджета"
domain: cattle-science
difficulty: intermediate
reading_time: 30 min
created: 2026-06-27
fpf_context: ["E.16", "A.2", "A.15", "A.21", "C.9", "C.16", "E.8", "E.10", "E.18", "F.17"]
---

# E.16 — Autonomy Budget & Guard Rails: автономия только в рамках бюджета

> **Цель capture:** объяснить, как в FPF оформляется любое заявление об автономности, чтобы оно было проверяемым, ограниченным и останавливаемым.

---

## 1. Зачем это читать

Если на ферме появляется робот, ИИ-советчик или автоматическая система, которая принимает решения без постоянного контроля человека, — вы уже в зоне E.16. В животноводстве автономные системы становятся обычным делом: кормораздатчики, роботы-дояры, сенсоры отёла, ИИ-рекомендации по лечению. Без E.16 «автономность» превращается в чёрный ящик: система делает что-то, но никто не может сказать, в рамках какого разрешения и что делать при превышении лимита.

> **FPF-тезис:** *«Автономия — не право действовать без ограничений. Автономия — это выделенный бюджет с явными guard rails, ledger и процедурой override.»*

**Фермерский пример:**

> Ферма купила автономный кормораздатчик, который сам решает, сколько корма давать каждой группе. Через месяц оказалось, что он недокормил высокопродуктивных коров в жару, потому что «решение» основывалось на средних показателях. Никто не знал: какой у него бюджет решений, кто может его остановить, какие guard rails действуют.

---

## 2. История одной ошибки

Ферма «Луговое» внедрила ИИ-сервис, который рекомендовал лечение мастита. Сервис работал «автономно» в том смысле, что генерировал рекомендации без участия ветеринара.

- **Бюджета не было.** Сколько рекомендаций в день? Какие риски допустимы? Неизвестно.
- **Guard rails отсутствовали.** Система предложила антибиотик корове с аллергией, потому что не проверяла историю.
- **Override было не ясно.** Ветеринар мог отменить рекомендацию, но эта отмена не фиксировалась; система продолжала учиться на отменённых случаях.
- **Ledger не вёлся.** Нельзя было аудиторски восстановить, сколько решений принято, сколько отменено, по каким причинам.

E.16 предлагает оформить автономию как declared, versioned, auditable contract: `AutonomyBudgetDecl`, guard policy, `OverrideProtocol`, `AutonomyLedger`.

---

## 3. RoC-Autonomy Budget & Enforcement — полное описание

### 3.1 Определение

**Autonomy Budget & Guard Rails (E.16)** — это паттерн Rule-of-Constraints, который делает любое заявление об автономном поведении тестируемым и принудимым через опубликованный `AutonomyBudgetDecl`, guarded enactment, override SpeechActs с separation of duties и Work-anchored `AutonomyLedger`.

### 3.2 Почему это важно

Без явного бюджета «автономно» становится меткой, которую нельзя проверить. Системы действуют вне remit, ответственность растворяется, две автономные системы несравнимы. E.16 превращает автономию в измеримый контракт: сколько действий, в каких risk bands, какие ресурсы, кто останавливает, что записывается.

### 3.3 Условие применения

**Определение.** E.16 обязателен всякий раз, когда `Role`, `Method` или `Service` заявляет об **автономном поведении** — то есть принимает решение или совершает действие без непрерывного подтверждения человеком в момент исполнения. Чисто рекомендательные системы, где каждое действие подтверждает человек, не подпадают.

**Пояснение.** Автономность — это не свойство системы в целом, а свойство конкретного шага метода или роли. Если робот доит без подтверждения — это autonomy. Если дашборд только показывает данные — нет.

**Пример из животноводства.**

| Система | Автономия? | Почему |
|---|---|---|
| Робот-дояр | Да | Совершает физические действия без подтверждения |
| Автокормушка | Да | Распределяет корм по своему алгоритму |
| Сенсор отёла с SMS-оповещением | Нет | Только уведомляет; решение принимает человек |
| ИИ-рекомендация лечения | Да, если назначает без ветеринара | Решение о лечении без подтверждения |
| Дашборд аналитики | Нет | Только отображает данные |

**Ключевой признак.** Если система действует без immediate human confirmation — нужен `AutonomyBudgetDecl`.

### 3.4 AutonomyBudgetDecl — обязательный артефакт

**Определение.** `AutonomyBudgetDecl` — это named, versioned объект в том же `U.BoundedContext`, который декларирует: `scope` (`ClaimScope`), `budget` (action tokens, decision tokens, risk bands, resource caps, time window), `AdmissibilityConditionsId` (guard policy), `overrideProtocolRef`, `telemetrySpecRef` и `editionPins`.

**Пояснение.** Бюджет — это не абстрактное «не навреди», а набор типизированных quota и условий. Без публикации этого артефакта autonomy claim не считается admitted.

**Пример из животноводства.**

```text
AutonomyBudgetDecl: AutoFeeder_v3_FarmA
  scope: FarmA.LactatingCows.HighYieldGroup
  budget:
    action_tokens: 48 dispenses/day
    decision_tokens: 24 ration_adjustments/day
    risk_bands: {MilkYield_7d_drop ≤ 5%; BCS_change ≤ 0.1/14d}
    resource_caps: {feed_inventory ≥ 2 days; energy ≥ baseline}
    time_window: 24h rolling
  AdmissibilityConditionsId: AutGuard_AutoFeeder_v3
  overrideProtocolRef: AutoFeeder_Override_Protocol_v1
  telemetrySpecRef: AutoFeeder_Telemetry_v2
  editionPins:
    RoleRef: AutoFeederRole_v2
    MethodDescRef: AutoFeeding_v3
    CHR refs: MilkYieldCHR, BCSCHR
```

**Ключевой признак.** Бюджет содержит типизированные quota, risk bands, resource caps и time window.

### 3.5 Guarded enactment и AutonomyLedger

**Определение.** Перед каждым автономным действием выполняется **Green-Gate**: проверяются валидность `RoleAssignment`, остаток бюджета в текущем `Γ_time` окне и guard checks из `AdmissibilityConditionsId`. Каждое допущенное действие записывается в `AutonomyLedgerEntry`.

**Пояснение.** Если любая проверка не проходит, действие **блокируется** (нет «soft warning»). Ledger entry привязывается к `U.Work` и содержит deltas, guard verdicts, path ids.

**Пример из животноводства.**

> Перед каждой выдачей корма робот проверяет:
> 1. `RoleAssignment` активен.
> 2. `action_tokens > 0` в текущем 24h окне.
> 3. `MilkYield_7d_drop ≤ 5%` и `BCS_change ≤ 0.1/14d`.
> 4. `feed_inventory ≥ 48h`.
> Если хоть одно нарушено — выдача блокируется, отправляется `DepletionNotice` или `Escalate`.

```text
AutonomyLedgerEntry:
  workId: W-2026-0619-AF-003
  performedBy: AutoFeederRole#Unit_07
  budgetId: ABD-AutoFeeder-HY-FarmA
  deltas: action_tokens −1; decision_tokens 0; risk band within limit
  guardVerdicts: all pass
  pathSliceId: PS-HY-2026-06-19
```

**Ключевой признак.** Без ledger entry автономное действие не считается admitted Work.

### 3.6 Override и Separation of Duties

**Определение.** Override выполняет любая роль, объявленная в `OverrideProtocolRef`, но **не та же `RoleAssignment`, которая потребляет бюджет**. Canonical SpeechActs: `PauseAutonomy(budgetId)`, `ResumeAutonomy(budgetId)`, `NarrowAutonomy(budgetId, Δscope)`, `Escalate(budgetId)`.

**Пояснение.** Override — это Work (SpeechAct) с ledger entry и проверкой SoD. Это предотвращает ситуацию, когда система сама себя разрешает продолжать.

**Пример из животноводства.**

> `HerdManagerRole#Ivanov` вызывает `PauseAutonomy(AutoFeeder_v3_FarmA)`, если робот-дояр начинает доить корову с клиническим маститом. `HerdManagerRole` и `AutoFeederRole` — disjoint (SoD).

**Ключевой признак.** override — это SpeechAct с ledger entry; потребитель бюджета и overrider — разные роли.

### 3.7 Исчерпание бюджета

**Определение.** Когда бюджет исчерпан (нет tokens, превышен envelope, нарушен cap), дальнейшие автономные действия в том же `Γ_time` окне блокируются, эмитируется `DepletionNotice`, и либо `Escalate`, либо `Park` согласно политике. Возобновление — только через `ResumeAutonomy` SpeechAct от допустимой роли после прохождения guard checks.

**Пояснение.** Depletion behavior — не предупреждение, а hard stop. Это гарантирует, что система не действует вне объявленных лимитов.

**Пример из животноводства.**

> Если `decision_tokens` исчерпаны из-за частых изменений рациона, автокормушка переходит в режим ожидания и страница supervisor получает `DepletionNotice`. Раздатчик не возобновляет работу, пока `HerdManagerRole` не вызовет `ResumeAutonomy` и не подтвердит новые условия.

**Ключевой признак.** Исчерпание бюджета блокирует автономные шаги до governed resume.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Наша система автономно управляет кормлением.»*

**Разложение по E.16:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «система» | `U.Service` / performer | Нужен `RoleAssignment` |
| «автономно управляет» | autonomy claim | Нужен `AutonomyBudgetDecl` |
| «кормлением» | `U.Work` / `U.Method` | Нужен MethodRef и WorkPlan |
| (скрытое) «безопасно» | guard claim | Нужен `AdmissibilityConditionsId` |

**Основные риски смешивания:**

1. **Нетестируемость.** «Автономно» без бюджета нельзя проверить.
2. **Риск неконтролируемых действий.** Система может действовать вне remit.
3. **Растворение ответственности.** Если что-то пошло не так, непонятно, кто отвечал.
4. **Несравнимость.** Нельзя сравнить две автономные системы без опубликованных UTS-полей.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** внедрить автономный кормораздатчик для высокопродуктивных коров.

**Было (смешанное / нечёткое):**

> «Робот сам решает, сколько корма давать, исходя из данных.»

**Стало (разложенное / ясное):**

**AutonomyBudgetDecl:**

> `id`: ABD-AutoFeeder-HY-FarmA
> `version`: 2026-06-27-v1
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
> Если хоть одно нарушено — выдача блокируется.

**Override:**

> `HerdManagerRole#Ivanov` вызывает `PauseAutonomy(ABD-AutoFeeder-HY-FarmA)` при обнаружении неисправности. SoD: `HerdManagerRole ⊥ AutoFeederRole`.

**Результат:**

- Любой аудитор видит, в рамках какого контракта действует робот.
- Превышение лимита останавливает систему, а не игнорируется.
- Ответственность за override чётко распределена.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Перечислите все системы на ферме, которые действуют без immediate human confirmation.

**Шаг 2.** Для каждой системы создайте `AutonomyBudgetDecl`: scope, budget (action/decision tokens, risk bands, resource caps, time window), AdmissibilityConditionsId, overrideProtocolRef, telemetrySpecRef, editionPins.

**Шаг 3.** Убедитесь, что Method steps, требующие автономии, декларируют `requiresAutonomyBudget`.

**Шаг 4.** Настройте ledger: каждое admitted Work должно создавать `AutonomyLedgerEntry`.

**Шаг 5.** Определите override SpeechActs и SoD: кто может pause/resume/escalate, и почему эта роль не совпадает с потребителем бюджета.

**Шаг 6.** Добавьте autonomy-поля в UTS rows для этой системы.

**Шаг 7.** Проведите drill: смоделируйте исчерпание бюджета и убедитесь, что система блокируется и эскалирует.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Система называется «автономной», но нет `AutonomyBudgetDecl`? | Autonomy-by-label; E.16‑S1 нарушен. |
| Guard checks только предупреждают, но не блокируют? | Soft gates; E.16‑S2 нарушен. |
| Override может выполнить та же роль, что и потребитель бюджета? | SoD collapse; E.16‑S4 нарушен. |
| Ledger не привязан к `U.Work` или не содержит deltas? | Нет audit trail; E.16‑S3 нарушен. |
| Бюджет исчерпан, но система продолжает работать? | Depletion behavior не реализован; E.16‑S5 нарушен. |
| UTS row не содержит autonomy-полей? | Несравнимость; E.16‑S6 нарушен. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| A.2 Role Taxonomy | роли потребителя и overrider бюджета |
| A.15 Role–Method–Work Alignment | Work и ledger entries |
| A.21 Gate Profile | Green-Gate и gate checks |
| C.9 Agency-CHR | измерение автономии и ответственности |
| C.16 Measurement | типизация budget deltas через MM-CHR |
| E.8 Pattern Authoring Discipline | шаблон оформления autonomy pattern |
| E.10 LEX-BUNDLE | лексические правила: «автономно» — trigger word |
| E.18 Transformation Flow Structure | scout/probe/commit partition при bounded specialization |
| F.17 UTS | публикация autonomy-полей для parity/selection |
| G.5 / G.9 / G.10 | method authoring, parity и shipping с учётом autonomy |

---

## 9. Что запомнить

1. Автономия требует опубликованного `AutonomyBudgetDecl` в том же `U.BoundedContext`.
2. Guard checks — hard gates; depletion — hard stop.
3. Каждое admitted Work создаёт `AutonomyLedgerEntry`.
4. Override — SpeechAct с SoD; потребитель и overrider — разные роли.
5. UTS rows для автономных систем должны содержать autonomy-поля.

---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §E.16*
