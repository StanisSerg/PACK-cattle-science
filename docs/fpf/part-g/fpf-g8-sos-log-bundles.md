---
type: fpf-study
pattern: G.8
title: "SoS-LOG бандлы и лестницы зрелости: от бумажного журнала до ИИ-мониторинга"
domain: cattle-science
difficulty: intermediate
reading_time: 19 min
created: 2026-05-26
---

# G.8 — SoS-LOG бандлы и лестницы зрелости: от бумажного журнала до ИИ-мониторинга

## 1. Зачем это читать
Если вы когда-нибудь говорили: *«Наша программа здоровья стада на уровне 4 из 5»* — но не могли объяснить, что такое «уровень 4», кем он определён, на чём основан, и что нужно для «уровня 5» — вы использовали **нематериализованную зрелость**.

G.8 превращает разрозненные «программы», «чек-листы» и «уровни развития» в **проверяемые, цитируемые артефакты**:
- `SoS-LOGBundle@Context` — упаковка правил для селектора
- `AdmissibilityLedger@Context` — журнал решений в runtime
- `MethodFamily.MaturityCardDescription@Context` — лестница зрелости как poset (не скаляр!)

Этот паттерн — **иммунитет против «мы вроде как продвинутые»**.

## 2. История одной ошибки
Ферма «Надежда» заявила, что её «программа мониторинга здоровья стада» находится на «уровне 4 — цифровой мониторинг». Инвестор, проводивший due diligence, увидел цифру и поверил.

Аудит показал:
- «Уровень 4» был придуман самой фермой — нет UTS-идентификатора, нет определения.
- «Цифровой мониторинг» означал, что зоотехник раз в неделю вносил показания в Excel.
- Ни одно правило не было оформлено как `SoS-LOG.Rule` с tri-state семантикой.
- Не было `AdmissibilityLedger` — никто не мог проверить, какие методы были допущены, какие отвергнуты, почему.
- Не было ссылок на `PathId` (G.6) — решения не трассировались к доказательствам.

Инвестор принял решение на основе **пустого числа**. Ферма получила финансирование, которое не могла освоить, потому что «уровень 4» был фикцией.

G.8 требует:
1. Зрелость — это **ordinal/poset**, не скаляр. Нельзя сказать «4.2» или «выше среднего».
2. Каждая ступень (`MaturityRungId`) — UTS-регистрируемый идентификатор с объявленной `ReferencePlane`.
3. Переход между ступенями обосновывается через `PathId` (доказательства).
4. Правила (`SoSLogRuleId`) — tri-state: `pass` / `degrade(mode=...)` / `abstain`.
5. Решения записываются в `AdmissibilityLedger` с полным audit trail.

## 3. SoS-LOG бандлы и лестницы зрелости: от бумажного журнала до ИИ-мониторинга — полное описание
### 3.1 SoS-LOG.Rule — правило с тремя исходами
`SoS-LOG.Rule` — это исполняемая схема решения с три-state доменом:
- **pass** (допустить / admit) — метод проходит все пороги
- **degrade(mode=...)** (деградировать) — метод допустим с ограничениями; требуется указать режим
- **abstain** (воздержаться) — метод не допустим; требуется эскалация

**Ключевой момент:** `degrade` и `abstain` — не «почти pass». Это **разные исходы** с разными последствиями. Семантика правил управляется C.23; G.8 только упаковывает их ids.

**На ферме:**
- `Rule_001`: «Метод мониторинга BHB допустим, если есть тестер и протокол» → `pass`
- `Rule_002`: «Метод DCAD допустим, если есть анализ корма; если анализа нет — `degrade(mode=manual_estimate)`»
- `Rule_003`: «Метод генетического отбора для текущей задачи — `abstain` (горизонт не подходит)»

### 3.2 SoS-LOGBundle@Context — упаковка для селектора
`SoS-LOGBundle@Context` — это UTS-публикуемый объект, который связывает:
- `MethodFamilyId` (какое семейство методов)
- `SoSLogRuleId[]` (какие правила применять)
- `MaturityCardRef` (какая лестница зрелости)
- `AcceptanceClauseId[]?` (ссылки на acceptance thresholds из G.4)
- `EvidenceGraphId?` / `PathId[]?` (доказательства)
- `BridgeId/BridgeCardId?` / `CL/CL^k/CL^plane?` (переходы, если reuse)
- `PortfolioMode?` / `DominanceRegime?` (режимы из Default Governing Definition Index)

**Что bundle НЕ делает:**
- Не вводит новых legality правил
- Не встраивает numeric thresholds (они цитируются из G.4 по id)
- Не создаёт shadow specs

### 3.3 AdmissibilityLedger@Context — журнал runtime-решений
`AdmissibilityLedger` — это runtime-представление, которое записывает:
- `MethodFamilyId` + `SoSLogRuleId`
- `GuardDecision ∈ {pass | degrade | abstain}`
- `DegradeMode?` / `SoSLogBranchId[]?`
- `MaturityRungId?`
- `AcceptanceClauseId[]?`
- `EvidencePathRefs` (`PathId[]/PathSliceId[]`)
- `CrossingPins` (если reuse)

**На ферме:** каждое решение селектора о том, допустить ли метод, записывается в ledger с обоснованием. Через год можно проверить: почему метод X был отвергнут? Ответ: `PathId-123` + `Rule_007` + `abstain` по `AcceptanceClause_003`.

### 3.4 MethodFamily.MaturityCardDescription — лестница зрелости как poset
Лестница зрелости публикуется как отдельный, цитируемый артефакт:
- **Closed rungs** — UTS-регистрируемые идентификаторы ступеней
- **Scale kind = ordinal** — не cardinal, не ratio
- **Declared ReferencePlane** — в какой плоскости измеряется зрелость
- **Poset edges** — какие ступени предшествуют каким (частичный порядок)
- **Rung transition justifications** — каждый переход обоснован через `PathId`

**Ключевой момент:** зрелость — **не скаляр**. Нельзя сказать «мы на 73% зрелости». Можно сказать: «мы на ступени `Rung_003`, которая предшествует `Rung_005`, но несравнима с `Rung_004`».

**На ферме:**
- `Rung_001`: Бумажный журнал наблюдений
- `Rung_002`: Электронная таблица Excel с ручным вводом
- `Rung_003`: Автоматизированная система с датчиками, но без интеграции
- `Rung_004`: Интегрированная платформа с дашбордом и алертами
- `Rung_005`: ИИ-ассистированный мониторинг с предиктивной аналитикой

Переход `Rung_003 → Rung_004` требует: `PathId` доказательства, что интеграция работает; `AcceptanceClause` для порога сбоев; `Rule` для режима `degrade` при отказе сети.

### 3.5 Separation rule — разделение метод-специфики
Метод- или генератор-специфичные пины (QD, OEE, open-ended) НЕ находятся в core bundle. Они появляются только в `GPatternExtension` блоках, когда соответствующий extension активен.

**На ферме:** если вы используете QD-archive для мониторинга разнообразия показателей стада, edition pins (`DescriptorMapRef.edition`, `DistanceDefRef.edition`) появляются только через extension `QD_OEE_TelemetryPins`, а не в основном бандле.

## 4. Почему смешивать / игнорировать — значит рисковать
| Антипаттерн | Почему опасно | Как выглядит на ферме |
|---|---|---|
| **«Скалярная зрелость» (Scalar Maturity)** | Зрелость выражается числом или процентом, маскируя частичный порядок. | «Наша программа здоровья — 4.2 из 5» — без определения, что такое 4.2. |
| **«Пороги внутри правил» (Threshold Leak)** | Числовые пороги встроены в текст правила, а не цитируются из G.4. | «Если BHB > 1.2 — тревога» записано прямо в правиле, а не как `AcceptanceClause_007`. |
| **«Решение без следов» (Decision without Ledger)** | Admissibility decisions не записываются; невозможно провести аудит. | «Мы отказались от этого метода» — но почему, по какому правилу, с какими доказательствами? |
| **«Телеметрия без гигиены» (Telemetry Contamination)** | QD/OEE/illumination сигналы используются как dominance inputs без явных policy pins. | «Алгоритм выбрал DCAD, потому что illumination высокий» — но illumination не должен доминировать без политики. |
| **«Вечный бандл» (Eternal Bundle)** | Bundle публикуется без edition pins и RSCR wiring; изменения не отслеживаются. | «У нас есть программа здоровья» — но она 2018 года, а edition не pinned, и никто не знает, что изменилось. |

## 5. Как это выглядит на ферме: лестница зрелости для «программы здоровья стада"
**MethodFamily:** `HerdHealthProgram`
**Context:** `Farm_A_Transition_Barn_2026`

### 5.1 MaturityCardDescription (ordinal/poset)
```
MaturityCardRef: MAT-HHP-001
ReferencePlane: Farm_Operational_World
Scale: ordinal

Rungs (closed set):
  Rung_001: PaperBased
    - Описание: Бумажный журнал наблюдений, ручная запись
    - UTS.id: UTS-RUNG-001

  Rung_002: DigitalSpreadsheet
    - Описание: Excel/Google Sheets с ручным вводом
    - UTS.id: UTS-RUNG-002
    - Poset edge: Rung_001 ⊏ Rung_002

  Rung_003: SensorRaw
    - Описание: Датчики (активность, жвачка, температура) сырые данные, без интеграции
    - UTS.id: UTS-RUNG-003
    - Poset edge: Rung_002 ⊏ Rung_003

  Rung_004: IntegratedDashboard
    - Описание: Интегрированная платформа с дашбордом, алертами, отчётами
    - UTS.id: UTS-RUNG-004
    - Poset edge: Rung_003 ⊏ Rung_004

  Rung_005: AIPredictive
    - Описание: ИИ-ассистированный мониторинг с предиктивной аналитикой
    - UTS.id: UTS-RUNG-005
    - Poset edge: Rung_004 ⊏ Rung_005
```

**Примечание:** poset, не линейный порядок. Например, ферма может перейти `Rung_002 → Rung_004` (скипнув сырые датчики), если сразу внедряет интегрированную платформу. Но `Rung_005` требует `Rung_004`.

### 5.2 SoS-LOGBundle для Rung_004 (IntegratedDashboard)
```
SoS-LOGBundleRef: BUNDLE-HHP-FarmA-004
Edition: 2026-05-26

CG-FrameContext: Farm_A_Health_2026
describedEntity: ⟨HerdHealthProgram, Farm_Operational_World⟩
CNSpecRef.edition: CNS-HEALTH-001.2024
CGSpecRef.edition: CGS-HEALTH-001.2025

MethodFamilyId: HHP-001
RegistrationContext: Farm_A_Transition_Barn_2026

SoSLogRuleId:
  - RULE-HHP-001: pass если дашборд обновляется в реальном времени
  - RULE-HHP-002: degrade(mode=latency_4h) если задержка < 4 часов
  - RULE-HHP-003: abstain если нет резервного копирования

MaturityCardRef: MAT-HHP-001
MaturityRungId: Rung_004

AcceptanceClauseId:
  - ACC-001: uptime > 99.5%
  - ACC-002: false_positive_rate < 5%

EvidenceGraphId: EG-HHP-004-2026
PathId:
  - PATH-HHP-004-001 (обоснование перехода Rung_003→Rung_004)
  - PATH-HHP-004-002 (валидация uptime)

PortfolioMode: Standard
DominanceRegime: Pareto
```

### 5.3 AdmissibilityLedger (runtime snapshot)
```
⟨ MethodFamilyId: HHP-001
  SoSLogRuleId: RULE-HHP-001
  GuardDecision: pass
  MaturityRungId: Rung_004
  AcceptanceClauseId: [ACC-001, ACC-002]
  EvidencePathRefs: [PATH-HHP-004-001, PATH-HHP-004-002]
  PortfolioMode: Standard
  Edition: 2026-05-26 ⟩

⟨ MethodFamilyId: HHP-ALT-002 (конкурирующее семейство)
  SoSLogRuleId: RULE-HHP-003
  GuardDecision: abstain
  EvidencePathRefs: [PATH-HHP-ALT-003]
  Reason: резервное копирование не настроено ⟩
```

**Что это даёт:**
- Инвестор видит: «Rung_004 — это вот что, вот правила, вот доказательства».
- Аудитор видит: «ALT-002 отвергнут по RULE-HHP-003, вот PathId».
- Менеджер видит: «Для перехода на Rung_005 нужно пройти ACC-003, ACC-004, вот обоснования».

## 6. Практическое применение: с чего начать
**Шаг 1. Определите MethodFamily.**
Выберите одну программу/метод, который хотите «оценить зрелость» (например, программа воспроизводства).

**Шаг 2. Создайте closed rungs.**
Назовите 4–6 ступеней от «бумага» до «ИИ». Каждая — UTS-идентификатор. Не используйте числа 1–5 как скаляр — используйте имена (`PaperBased`, `DigitalSpreadsheet`, ...).

**Шаг 3. Объявите poset edges.**
Какие ступени обязательно предшествуют каким? Какие несравнимы? Нарисуйте граф.

**Шаг 4. Создайте SoS-LOG Rules.**
Для каждой ступени определите 2–3 правила tri-state. Не встраивайте пороги — цитируйте `AcceptanceClauseId` из G.4.

**Шаг 5. Соберите SoS-LOGBundle.**
Свяжите MethodFamily, Rules, MaturityCard, Acceptance, Evidence (PathId). Опубликуйте в UTS.

**Шаг 6. Запустите AdmissibilityLedger.**
Каждое runtime-решение записывайте: метод, правило, исход, доказательства. Это ваш аудит-след.

## 7. Проверь себя
| Вопрос | Если ответ «да» — проблема |
|---|---|
| Выражаете ли вы зрелость числом (1–5, 0–100%)? | Scalar Maturity |
| Встроены ли числовые пороги прямо в текст правил? | Threshold Leak |
| Можете ли вы через год объяснить, почему метод был отвергнут? | Decision without Ledger |
| Используете ли вы «сигналы системы» (QD, illumination) для выбора метода без явной политики? | Telemetry Contamination |
| Изменяли ли вы правила/лестницу без обновления edition и RSCR wiring? | Eternal Bundle |

## 8. Связь с другими паттернами
| Паттерн | Связь |
|---|---|
| G.Core | универсальные инварианты Part-G: tri-state guard, penalties→R_eff, P2W split, типизированные RSCR triggers. |
| C.23 (SoS-LOG) | семантика правил `pass/degrade/abstain`; G.8 только упаковывает их ids. |
| C.22 (TaskSignature) | сигнатуры задач, к которым привязываются бандлы. |
| G.4 (Acceptance) | thresholds и `AcceptanceClauseId`, которые бандл цитирует, не встраивает. |
| G.6 (Evidence Graph) | `PathId/PathSliceId` для обоснования rung transitions и решений. |
| G.5 (Method Dispatcher) | потребитель `SoS-LOGBundle` для registry/selection. |
| G.11 (Refresh Orchestration) | потребитель RSCR triggers при изменении bundle/ledger. |
| G.10 (Shipping Boundary) | бандл может пересекать границу публикации/shipping. |
| F.9 (BridgeCard) | если reuse across context, crossing pins подключаются через `G.8:Ext.BridgeReuseWiring`. |
| F.17 (UTS) | публикация bundle, ledger, maturity card как UTS rows. |
---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §G.8*
