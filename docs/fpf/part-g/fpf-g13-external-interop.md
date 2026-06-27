---
type: fpf-study
pattern: G.13
title: "External Interop Hooks: внешние индексы как управляемые входы SoTA"
domain: cattle-science
difficulty: advanced
reading_time: 26 min
created: 2026-06-27
fpf_context: ["G.13", "G.Core", "G.2", "G.3", "G.12", "G.10"]
---

# G.13 — External Interop Hooks: внешние индексы как управляемые входы SoTA

> **Цель capture:** объяснить, как паттерн G.13 позволяет подключать внешние научные индексы и репозитории к Part G pipeline, сохраняя FPF-инварианты и делая interop refreshable.

---

## 1. Зачем это читать

В скотоводстве внешние источники — PubMed, реестры данных, claim graphs, отраслевые базы знаний — играют важную роль при создании SoTA-упаковок. Без явного interop kit авторы либо копируют внешние сигналы как «факты», либо строят ad-hoc маппинги, которые скрывают edition drift и cross-context reuse. G.13 превращает внешние источники в управляемые входы с edition pins, mapping policies и typed RSCR triggers.

> **FPF-тезис:** *«Внешние индексы — это источники, а не управляющие нормы; их нужно регистрировать, типизировать и связывать с evidence.»*

**Фермерский пример:**

> Консультант хочет дополнить SoTA-упаковку по кетозу результатами из внешнего claim graph (например, OpenAlex- или ORKG-подобного индекса). G.13 требует зарегистрировать ExternalIndexCard с edition, создать ClaimMapperCard с MappingPolicyRef и опубликовать InteropSurface@Context. Только после этого внешние claim'ы могут стать входами для G.2 harvesting или G.12 dashboards.

---

## 2. История одной ошибки

Хозяйство использовало внешний сервис, который «автоматически» подбирал исследования по кетозу и превращал их в рекомендации. Со временем внешний индекс изменил алгоритм ранжирования, и в выдачу попали статьи по овцам и козам, а не по дойным коровам. Поскольку интеграция не была типизирована и не имела edition pins, команда долго не замечала drift. G.13 мог бы потребовать ExternalIndexCard и ClaimMapperCard, которые фиксируют scope и mapping policy.

---

## 3. External Interop Hooks — полное описание

### 3.1 Определение

**External Interop Hooks** — это conceptual interop kit, который регистрирует внешние источники через ExternalIndexCard@Context, описывает их mapping через ClaimMapperCard@Context, типизирует производные признаки через SoSFeatureTransform@Context и публикует InteropSurface@Context с edition-aware RSCR triggers.

### 3.2 Почему это важно

Внешние источники ценны широтой охвата, но они часто несут скрытые предположения: о шкалах, о популяциях, о методах. G.13 не запрещает их использовать, но требует явно зафиксировать: какой источник, какая редакция, какая политика mapping, какие потери при переносе. Это предотвращает подмену внешних сигналов на evidence и делает interop refreshable.

### 3.3 ExternalIndexCard@Context

**Определение.** ExternalIndexCard@Context — это регистрация внешнего источника и его snapshot, включающая ExternalIndexId, ProviderName, ExternalIndexType, CoverageScope, ExternalEdition, FreshnessWindow и entityOfConcern anchor.

**Пояснение.** ExternalIndexCard создаёт стабильный, citable «source card». Downstream артефакты цитируют ExternalIndexRef.edition, а не произвольные snapshot labels.

**Пример из животноводства.**

```text
EIC-001: ExternalIndexCard@Context
  - ExternalIndexId: PUBMED-KETOSIS
  - ProviderName: NCBI PubMed
  - ExternalIndexType: scholarly_article_index
  - CoverageScope: dairy cattle ketosis, 2015–2025
  - ExternalEdition: 2026-06-01
  - entityOfConcern: dairy cows, transition period
```

**Ключевой признак.** ExternalIndexCard имеет ExternalEdition и ExternalIndexRef.edition; downstream цитирует edition.

### 3.4 ClaimMapperCard@Context

**Определение.** ClaimMapperCard@Context — это conceptual mapping recipe, который описывает, как внешние claim'ы превращаются в FPF-native artefacts (ClaimSheets, BridgeHints, SoSFeatureSet, UTSProposals).

**Пояснение.** ClaimMapperCard не является shadow legality gate. Он ссылается на governing definitions (A.19, G.0, G.3, G.4) и публикует pins для audit/refresh. Cross-plane/context reuse требует crossing bundles.

**Пример из животноводства.**

```text
CMC-001: ClaimMapperCard@Context
  - MapperId: PUBMED-TO-FPF-001
  - ExternalIndexId: EIC-001
  - MappingPolicyRef: POL-MAP-001
  - Targets: ClaimSheet, BridgeHints
  - PlaneMapRef: PM-001 (if needed)
  - ScaleEmbeddingSpecRef: SES-001 (if embedding used)
```

**Ключевой признак.** ClaimMapperCard содержит ExternalIndexId, MappingPolicyRef, Targets и optional PlaneMap/ScaleEmbeddingSpec refs.

### 3.5 SoSFeatureTransform@Context

**Определение.** SoSFeatureTransform@Context — декларация того, как внешние сигналы превращаются в CHR-typed SoS features для DHC/dashboard или SoS-LOG rule evaluation.

**Пояснение.** Transform не вводит новых comparators или legality gates. Он только типизирует и фиксирует provenance. Любая агрегация должна быть scale-legal.

**Пример из животноводства.**

```text
SFT-001: SoSFeatureTransform@Context
  - Inputs: ClaimSheetId [CS-001, CS-002]
  - SoSFeatureSetId: SFS-001
  - FeatureTypingRefs: {CharacteristicId=CH-001, ScaleId=SC-001}
  - ReferencePlane: world
  - EvidenceGraphId: EG-001
```

**Ключевой признак.** SoSFeatureTransform содержит CHR typing refs и evidence hooks.

### 3.6 ScaleEmbeddingSpec@Context

**Определение.** ScaleEmbeddingSpec@Context — это optional spec, который задаёт ограничения на representation/space alignment, используемый в mapping recipe.

**Пояснение.** Когда interop использует embedding-based alignment (например, текстовые сходства), Spec делает эти преобразования явно constrained и edition-pinned. Он не определяет, что «достаточно похоже».

**Пример из животноводства.**

```text
SES-001: ScaleEmbeddingSpec@Context
  - IntendedUse: concept_neighborhood_for_ketosis
  - AllowedTransformFamily: cosine_similarity_over_sentence_embedding
  - ProhibitedCoercions: ordinal arithmetic, threshold assignment
```

**Ключевой признак.** ScaleEmbeddingSpec определяет allowed transforms и prohibited coercions.

### 3.7 InteropSurface@Context

**Определение.** InteropSurface@Context — это published summary того, какие interop публикации/records существуют, как они pinned и как связаны с upstream artefacts.

**Пояснение.** InteropSurface не содержит самих внешних данных; он содержит ids, edition refs, mapping policy и evidence paths. Он может быть включён в SoTA-Pack(Core) через G.10:Ext.InteropCitation.

**Пример из животноводства.**

```text
IS-001: InteropSurface@Context
  - ExternalIndexId: EIC-001
  - ExternalIndexRef.edition: 2026-06-01
  - MapperId: CMC-001
  - ClaimMapperRef.edition: 1.0
  - SoSFeatureSetId: SFS-001
  - EvidenceGraphId: EG-001
  - PathSliceId: [PS-001]
```

**Ключевой признак.** InteropSurface содержит ExternalIndexRef.edition, ClaimMapperRef.edition и evidence refs.

### 3.8 IndexTelemetryPin

**Определение.** IndexTelemetryPin — это emitted refresh input, который делает изменения внешних источников RSCR-visible.

**Пояснение.** При изменении ExternalEdition, MappingPolicyRef, PlaneMapRef или ScaleEmbeddingSpecRef эмитируется canonical RSCRTriggerKindId с scope и payload pins. Это позволяет G.11 планировать re-alignment.

**Пример из животноводства.**

```text
ITP-001: IndexTelemetryPin
  - triggerKindId: EditionPinChange
  - scope: PS-001
  - payloadPins: {ExternalIndexRef.edition, ClaimMapperRef.edition, MappingPolicyRef}
```

**Ключевой признак.** IndexTelemetryPin несёт canonical trigger kind, scope и edition/policy payload.

---

## 4. Почему смешивать / игнорировать — значит рисковать

Рассмотрим типичное смешанное утверждение:

> *«Внешний индекс говорит, что этот метод лучше всего подходит для профилактики кетоза.»*

**Разложение по G.13:**

| Часть утверждения | Что это в FPF | Почему важно разделять |
|---|---|---|
| «внешний индекс» | ExternalIndexCard | Нужна регистрация и edition |
| «говорит» | external signal | Не является evidence без mapping и CHR typing |
| «лучше всего подходит» | dominance claim | Требует CAL policy и selector (G.5) |

**Основные риски смешивания:**

1. **Metric authority bias.** Внешний индекс воспринимается как авторитет вместо входа.
2. **Hidden edition drift.** Изменение алгоритма индекса не отслеживается.
3. **Implicit cross-context reuse.** Методы из других областей переносятся без bridge.

---

## 5. Как это выглядит на ферме: правильное применение

**Ситуация:** использование внешнего claim graph для обогащения SoTA по кетозу.

**Было (смешанное / нечёткое):**
> «Импортнём статьи из индекса и добавим их в обзор.»

**Стало (разложенное / ясное):**

**ExternalIndexCard EIC-001:**
> Provider: PubMed-like index; CoverageScope: dairy cattle ketosis 2015–2025; ExternalEdition: 2026-06-01.

**ClaimMapperCard CMC-001:**
> ExternalIndexId: EIC-001; MappingPolicyRef: POL-MAP-001; Targets: ClaimSheet, BridgeHints.

**SoSFeatureTransform SFT-001:**
> Inputs: ClaimSheets; CHR typing: CH-001, SC-001; EvidenceGraphId EG-001.

**InteropSurface IS-001:**
> ExternalIndexRef.edition: 2026-06-01; ClaimMapperRef.edition: 1.0; PathSliceId PS-001.

**IndexTelemetryPin ITP-001:**
> EditionPinChange; scope PS-001; payload ExternalIndexRef.edition.

**Результат:**
- Внешние источники зарегистрированы и типизированы.
- Mapping policy explicit.
- Изменения индекса вызывают RSCR trigger и re-alignment.

---

## 6. Практическое применение: с чего начать

**Шаг 1.** Зарегистрируйте каждый внешний источник как ExternalIndexCard@Context с ExternalEdition.

**Шаг 2.** Создайте ClaimMapperCard@Context с MappingPolicyRef и target artefacts.

**Шаг 3.** Если нужны derived features — объявите SoSFeatureTransform@Context с CHR typing refs.

**Шаг 4.** Опубликуйте InteropSurface@Context, цитируя все edition pins.

**Шаг 5.** Настройте IndexTelemetryPin на изменения edition/policy/plane map.

---

## 7. Проверь себя

| Вопрос | Если ответ «да» — проблема |
|---|---|
| Внешний источник не зарегистрирован как ExternalIndexCard? | Нет edition discipline; drift неотслеживаем. |
| ClaimMapperCard отсутствует? | Внешние сигналы не типизированы и не маппируются. |
| Derived features не имеют CHR typing? | Возможна недопустимая арифметика или hidden scale invention. |
| InteropSurface не публикует edition pins? | Потребитель не может проверить freshness. |
| Изменения индекса не эмитируют RSCR trigger? | Refresh не происходит автоматически. |

---

## 8. Связь с другими паттернами

| Паттерн | Связь |
|---|---|
| G.2 SoTA Harvester | потребляет ClaimSheets и BridgeHints из mapper |
| G.3 CHR Authoring | используется для CHR typing в SoSFeatureTransform |
| G.12 DHC Dashboards | может потреблять SoSFeatureSet как DHC slots |
| G.10 SoTA Pack Shipping | включает InteropSurface через G.10:Ext.InteropCitation |
| G.Core | гарантирует no-shadow-specs, crossing visibility и set-return |

---

## 9. Что запомнить

1. G.13 превращает внешние индексы в управляемые входы с edition pins.
2. ExternalIndexCard фиксирует источник и его ExternalEdition.
3. ClaimMapperCard описывает mapping recipe, но не является legality gate.
4. SoSFeatureTransform типизирует derived features через CHR.
5. IndexTelemetryPin делает interop changes RSCR-visible для G.11.

---

*Capture создан в рамках изучения Part G FPF.*
*FPF Source: FPF/FPF-Spec.md §G.13*
