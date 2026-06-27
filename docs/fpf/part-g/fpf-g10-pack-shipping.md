---
type: fpf-study
pattern: G.10
title: "SoTA Pack Shipping: публикация упаковки без подмены семантики"
domain: cattle-science
difficulty: advanced
reading_time: 26 min
created: 2026-06-27
fpf_context: ["G.10", "G.Core", "G.5", "G.9", "G.11", "G.12"]
---

# G.10 — SoTA Pack Shipping: публикация упаковки без подмены семантики

> **Цель capture:** объяснить, как паттерн G.10 определяет единственную shipping surface для Part G — SoTA-Pack(Core) — и как сделать shipped pack selector-ready, audit-citable и refreshable.

---

## 1. Зачем это читать

В скотоводстве результаты работы — SoTA-упаковки, отчёты parity, evidence graphs, dashboard slices — часто передаются между командами, публикуются для фермеров или отправляются в внешние системы. Без явного shipping boundary «передача» превращается в ad-hoc export, который может подменить семантику, потерять edition pins или скрыть crossings. G.10 фиксирует, что именно должно быть в shipped pack.

> **FPF-тезис:** *«Shipping — это не формат файла, а citation surface с обязательными pins, paths и MOO-disclosure.»*

**Фермерский пример:**

> Фермер получает «пакет рекомендаций» по профилактике кетоза. В пакете должны быть не только итоговые советы, но и ссылки на CG-Spec, ComparatorSet, BridgeCards, EvidenceGraph paths, selector outcomes и telemetry pins. Без этого фермер не сможет проверить, почему выбран именно этот метод, и не сможет обновить пакет, когда изменится evidence.

---

## 2. История одной ошибки

Консалтинговая фирма отправила фермеру PDF-отчёт с рекомендациями по управлению метаболическим риском. PDF содержал красивые графики, но не включал ссылки на использованные CG-Spec, BridgeCards и ParityReport. Через полгода вышло новое исследование, изменившее порог BHB. Фермер не мог понять, какие части отчёта нужно пересмотреть, потому что shipping surface не содержала PathSliceId и RSCR hooks. G.10 требует, чтобы pack нёс эти pins.

---

## 3. SoTA Pack Shipping — полное описание

### 3.1 Определение

**SoTA-Pack(Core)** — это pack-governed shipping surface, который цитирует все upstream артефакты по stable ids/refs и exposes минимальные pins, необходимые для: (a) потребления через selection, (b) аудита через path citations и crossing bundles, (c) refresh через typed RSCR triggers.

### 3.2 Почему это важно

Naive shipping либо превращает формат файла в governing spec, либо теряет edition/policy pins, либо скрывает crossings. SoTA-Pack(Core) предотвращает это, делая pack conceptual object'ом с явными ссылками. Он не задаёт формат файла; он задаёт, что должно быть цитируемым.

### 3.3 SoTA-Pack(Core) object model

**Определение.** SoTA-Pack(Core) — это объект, содержащий PackId(UTS), publicationScopeId, CG-FrameContext, entityOfConcern, CNSpecRef.edition, CGSpecRef.edition, PortfolioRosterId, cited payload pack ids, PathIds, PathSliceIds, AuditPins, CrossingBundleIds, TelemetryPinIds и MOOManifestId.

**Пояснение.** Pack цитирует upstream артефакты (harvest pack, CHR pack, CAL pack, evidence graph, bridge calibration, SoS-LOG bundle, parity report, dashboard slice) без дублирования их семантики. AuditPins содержит edition pins, policy ids, UTS/Path pins и crossing pins.

**Пример из животноводства.**

```text
SoTA-Pack(Core) PACK-001:
  - PackId(UTS): PACK-001
  - publicationScopeId: public_farmA_ketosis_2026
  - CGFrameContext: ketosis_prevention_FarmA
  - CNSpecRef.edition: 1.2
  - CGSpecRef.edition: 1.0
  - PortfolioRosterId: PR-001
  - SoTAHarvestPackId: HARVEST-001
  - CHRPackId: CHR-001
  - CALPackId: CAL-001
  - EvidenceGraphId: EG-001
  - BridgeCalibrationTableId: BCT-001
  - ParityReportId: PR-001
  - PathIds: [P-001, P-002]
  - PathSliceIds: [PS-001, PS-002]
  - CrossingBundleIds: [CB-001]
  - TelemetryPinIds: [TP-001]
  - MOOManifestId: MOO-001
```

**Ключевой признак.** Pack цитирует upstream ids и expose'ит AuditPins, PathIds, CrossingBundleIds и TelemetryPinIds.

### 3.4 PortfolioRoster@Context

**Определение.** PortfolioRoster@Context — это selector-facing roster token внутри shipped pack, который содержит metadata о selector outcomes (setResultFamily, handoffKind, derivedViewKind, basePaletteRef, shortlistId), но не переопинирует selection semantics.

**Пояснение.** PortfolioRoster позволяет потребителю pack понять, какой вид результата он видит: palette, front, archive, shortlist, ranked shortlist. Roster не является publication face kind; он — metadata внутри shipping form.

**Пример из животноводства.**

```text
PortfolioRoster PR-001:
  - selectorOutcomeKind: SetResultOutcome
  - setResultFamily: ParetoShortlist
  - sourceSetFamily: MethodFamilyPool
  - derivedViewKind: TraditionFront
  - basePaletteRef: PALETTE-001
  - shortlistId: SL-001
```

**Ключевой признак.** PortfolioRoster использует controlled tokens и cited ids; не вводит новых semantics.

### 3.5 MOOManifest

**Определение.** MOOManifest (Method-of-Obtaining-Output Manifest) — это disclosure, который перечисляет mechanism/policy/edition ids, использованные для получения shipped outcomes.

**Пояснение.** MOOManifest отвечает на вопрос: «Какие механизмы и политики произвели этот результат?» Он не раскрывает формат, а раскрывает provenance.

**Пример из животноводства.**

```text
MOO-001:
  - selectorMethodRef: G.5-SELECT-001
  - dominanceRegimeRef: CC-G5.28
  - parityHarnessRef: PR-001
  - bridgeCalibrationRef: BCT-001
  - policyPins: [POL-001, POL-002]
```

**Ключевой признак.** MOOManifest содержит ids механизмов и политик, а не narrative explanation.

### 3.6 CrossingBundle exposure

**Определение.** Для каждого GateCrossing, relevant к shipped artefacts, pack должен expose CrossingBundleIds; missing/non-conformant bundles вызывают fail-fast.

**Пояснение.** CrossingBundle (E.18) содержит pins, необходимые для проверки cross-context reuse. G.10 не проверяет crossing semantics; он требует, чтобы bundles были видны.

**Пример из животноводства.** Если pack включает сравнение Lab_BHB и Milk_Ketone_Test, CrossingBundle CB-001 должен содержать BridgeCard BC-001, CL, Φ(CL) policy id и UTSRowId.

**Ключевой признак.** CrossingBundleIds присутствуют в pack для всех asserted crossings.

### 3.7 Telemetry pins for refresh

**Определение.** Pack должен emit PathSlice-keyed telemetry pins с policy-id и active edition pins, чтобы G.11 мог планировать slice-scoped refresh.

**Пояснение.** Telemetry не превращается в dominance; она служит для refresh planning. Каждый telemetry pin содержит RSCRTriggerKindId, scope и payload pins.

**Пример из животноводства.**

```text
TelemetryPin TP-001:
  - triggerKindId: RSCRTriggerKindId.EditionPinChange
  - scope: PS-001
  - payloadPins: {DHCMethodRef.edition=2.1, policy-id=POL-003}
```

**Ключевой признак.** Telemetry pins keyed by PathSliceId и несут policy/edition payload.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Мы отправили фермеру PDF с рекомендациями.»*

**Разложение по G.10:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «PDF» | serialization / publication form | Формат не является governing spec |
| «рекомендации» | selector outcome / CAL actions | Требуют citation surface |
| «фермеру» | consumer | Потребитель pack |

**Основные риски смешивания:**

1. **Format-as-spec.** PDF становится «pack», теряются pins и provenance.
2. **Hidden edition drift.** Без edition pins нельзя понять, какая редакция CG-Spec использовалась.
3. **Refresh orphaning.** Без PathSliceId обновление требует полного пересбора.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** публикация pack для фермера по управлению метаболическим риском.

**Было (смешанное / нечёткое):**
> «Отправим фермеру PDF с рекомендациями.»

**Стало (разложенное / ясное):**

**SoTA-Pack(Core) PACK-001:**
> PackId = PACK-001
> PortfolioRosterId = PR-001
> CGSpecRef.edition = 1.0, CNSpecRef.edition = 1.2
> PathIds = [P-001, P-002]
> CrossingBundleIds = [CB-001]
> TelemetryPinIds = [TP-001]
> MOOManifestId = MOO-001

**PortfolioRoster PR-001:**
> setResultFamily = ParetoShortlist
> sourceSetFamily = MethodFamilyPool
> shortlistId = SL-001

**MOOManifest MOO-001:**
> selector = G.5-SELECT-001, parity = PR-001, bridge = BCT-001.

**Результат:**
- Pack можно проверить, обновить и повторно использовать.
- Формат PDF является одной из publication forms, но не governing spec.
- Фермер получает не только советы, но и адреса для аудита.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Соберите все upstream artefact ids и проверьте required pins.

**Шаг 2.** Составьте SoTA-Pack(Core) с CG-FrameContext, entityOfConcern, spec refs.

**Шаг 3.** Создайте PortfolioRoster@Context с корректными set-result metadata.

**Шаг 4.** Добавьте PathIds, CrossingBundleIds, AuditPins и TelemetryPinIds.

**Шаг 5.** Сформируйте MOOManifestId и опубликуйте pack в UTS.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Pack представлен только как файл без conceptual object? | Format-as-spec; теряются pins. |
| Отсутствуют PathIds / PathSliceIds? | Refresh будет глобальным и неуправляемым. |
| CrossingBundleIds не exposed? | Cross-context reuse не аудитоспособен. |
| MOOManifestId отсутствует? | Непонятно, как был получен результат. |
| Telemetry pins не keyed by PathSliceId? | G.11 не может планировать slice-scoped refresh. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| G.5 Method Dispatcher | предоставляет selector outcomes для PortfolioRoster |
| G.9 Parity Harness | предоставляет ParityReportId |
| G.7 Bridge Calibration | предоставляет BridgeCalibrationTableId и CrossingBundle |
| G.11 Telemetry Refresh | потребляет TelemetryPinIds |
| G.Core | определяет shipping boundary и universal invariants |

---

## 9. Что запомнить

1. SoTA-Pack(Core) — это conceptual shipping surface, а не файл.
2. Pack цитирует upstream artefact ids и expose'ит AuditPins, PathIds, CrossingBundleIds.
3. PortfolioRoster@Context описывает selector outcome shape без переопределения semantics.
4. MOOManifest раскрывает mechanism/policy/edition ids, использованные для получения outcomes.
5. Telemetry pins делают pack refreshable через G.11.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.10*
