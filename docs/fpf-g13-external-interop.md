---
type: fpf-study
pattern: G.13
title: "External Interop Hooks: как импортировать внешнее знание, не разрушая структуру"
domain: cattle-science
difficulty: hard
reading_time: 18 min
created: 2026-05-26
---

# G.13 — External Interop Hooks (Интеграция с внешними научными индексами)

## 1. Зачем это читать

Если вы когда-нибудь копировали данные из PubMed, Google Scholar или ветеринарной базы знаний в свой PACK — и не задумывались, **что происходит с этими данными внутри вашей системы** — вы столкнулись с проблемой G.13. Этот паттерн не про то, **где искать статьи**. Он про то, **как встроить внешние источники в FPF-пайплайн так, чтобы они не стали теневой спецификацией**.

В мире software импорт данных из внешних API часто приводит к «утечке семантики»: формат JSON заменяет спецификацию, внешние id начинают жить своей жизнью, а через год никто не помнит, что означает импортированное поле. В мире ферм — когда вы импортируете PubMed-цитаты о кетозе, вы должны сохранить: какая редакция источника, как произведено сопоставление понятий, какие evidence-пути ведут к импортированным данным.

**Без G.13:** внешние данные «проваливаются» в PACK и начинают влиять на решения — без трассировки, без аудита, без обновления.

**С G.13:** каждый внешний источник зарегистрирован, сопоставление задокументировано, производные признаки типизированы, а изменения во внешнем источнике порождают RSCR-триггеры для обновления.

---

## 2. История одной ошибки

Ферма «Волжское» создавало PACK по управлению переходным периодом. Зоотехник нашёл 47 статей в PubMed по ключевым словам «dairy cow transition period ketosis». Импортировал их в справочник фермы:

- Названия статей
- Авторы
- Годы
- «Ключевые выводы» (скопированы из аннотаций)

Через год PACK использовался для принятия решений:

- «В статье Smith et al. 2019 сказано, что пропиленгликоль неэффективен» → протокол изменили, убрали ПГК.
- «В обзоре 2020 года рекомендовано DCAD > +400» → ввели новую политику минералов.

Аудит через полгода выявил:

- **Smith et al. 2019** — исследование на **овцах**, не на коровах. Кросс-видовой переход не был явно задекларирован.
- **Обзор 2020** — DCAD > +400 рекомендовано для **стельных нетелей**, а не для дойных коров после отёла. Контекст смешан.
- PubMed обновился: **Smith et al. 2019 получила corrigendum** — данные по ПГК были пересчитаны. На ферме об этом не узнали.
- Не было **EvidenceGraph** — нельзя было проследить, как именно внешняя цитата повлияла на протокол.
- Не было **типизации** — «ключевые выводы» хранились как текст, а не как CHR-типизированные утверждения.

FPF G.13 говорит: *внешние данные — это не evidence, пока они не типизированы, не привязаны к путям и не обновляются*.

---

## 3. Core concepts

### 3.1 ExternalIndexCard@Context — регистрация внешнего источника

Прежде чем использовать внешний источник, его нужно **зарегистрировать** — создать «карточку источника».

```
ExternalIndexCard@Context := ⟨
  ExternalIndexId,
  ProviderName?,
  ExternalIndexType,         // например, PubMed, CAB Abstracts, VetMed Resource
  CoverageScope,             // «кетоз крупного рогатого скота, 2015–2025»
  Licence?,
  ExternalEdition,           // версия/снимок внешнего источника
  FreshnessWindow?,          // как долго считать свежим
  describedEntity := ⟨GroundingHolon, ReferencePlane⟩,
  Notes?
⟩
```

**На ферме:**

```
ExternalIndexId: EXT-PUBMED-TRANSITION-2024
ProviderName: PubMed/NCBI
ExternalIndexType: CitationIndexWithAbstracts
CoverageScope: «dairy cattle transition period: ketosis, fatty liver, milk fever, 2015–2025»
ExternalEdition: «PubMed snapshot 2024-12-01, query: (dairy+cattle+transition+period)»
FreshnessWindow: 90 days
```

**Ключевой принцип:** downstream артефакты цитируют `ExternalIndexRef.edition`, а не копируют snapshot id. Это позволяет отслеживать, какая версия источника была использована, даже если провайдер изменил схему.

### 3.2 ClaimMapperCard@Context — рецепт сопоставления

`ClaimMapperCard` — это концептуальный «рецепт преобразования», который создаёт FPF-нативные артефакты из внешнего источника.

```
ClaimMapperCard@Context := ⟨
  MapperId,
  ExternalIndexId,
  MappingPolicyRef,
  Targets: {
    ClaimSheet?,
    BridgeHints?,
    SoSFeatureSet?,
    UTSProposals?
  },
  PlaneMapRef?,              // сопоставление плоскостей/контекстов
  ScaleEmbeddingSpecRef?,    // сопоставление шкал
  EvidenceGraphId?,
  CSLCProofStubs?            // заготовки доказательств CSLC
⟩
```

**На ферме:**

```
MapperId: MAP-PUBMED-TO-CS-2024
ExternalIndexId: EXT-PUBMED-TRANSITION-2024
MappingPolicyRef: POLICY-MAP-VET-TO-DAIRY-2024
Targets: {
  ClaimSheet: «Каждая PubMed-статья → ClaimSheet с утверждениями»,
  BridgeHints: «Кросс-видовые исследования → BridgeHints (овца→корова)»,
  SoSFeatureSet: «Evidence depth, replication status, study design»
}
ScaleEmbeddingSpecRef: SCALE-OVINE-TO-BOVINE-2024
  // «Метаболические показатели овец НЕ прямо переносимы на коров;
  //  требуется масштабирование с коэффициентом CL=0.7 и потерей Φ=0.3»
```

### 3.3 SoSFeatureTransform@Context — типизация внешних сигналов

```
SoSFeatureTransform@Context := ⟨
  SoSFeatureTransformId,
  Inputs: {ClaimSheetId[] | ExternalSignalsRef},
  SoSFeatureSetId,
  FeatureTypingRefs: {CharacteristicId, ScaleId, CoordinateId},
  ReferencePlane,
  EvidenceGraphId?,
  PathSliceId[]?,
  ProofHooks?
⟩
```

**На ферме:** внешние сигналы (число цитирований, статус репликации, тип исследования) превращаются в CHR-типизированные признаки:

- `CharacteristicId: EVIDENCE-DEPTH` → ScaleId: ORDINAL-{low, medium, high}
- `CharacteristicId: STUDY-DESIGN` → ScaleId: CATEGORICAL-{RCT, cohort, case-control, review}
- `CharacteristicId: REPLICATION-STATUS` → ScaleId: CATEGORICAL-{original, replicated, contradicted}

**Важно:** преобразование — это **типизация + происхождение**. Оно не вводит новых компараторов и не создаёт новых governance cards.

### 3.4 IndexTelemetryPin — обновление по изменению источника

```
IndexTelemetryPin := ⟨
  triggerKindId: RSCRTriggerKindId,
  scope: PathSliceId[] | PatternScopeId,
  payloadPins: {
    ExternalIndexId, ExternalIndexRef.edition,
    ClaimMapperRef.edition?, MappingPolicyRef?,
    PathId[]?, PathSliceId[]?
  }
⟩
```

**На ферме:** когда PubMed выпускает новый snapshot или статья получает corrigendum:

- `triggerKindId: EvidenceSurfaceEdit`
- `scope: PathSliceId.PUBMED-IMPORTED-CLAIMS-2024`
- `payloadPins: {EXT-PUBMED-TRANSITION-2024, newEdition: «2025-03-01»}`

Это попадает в `G.11 RefreshQueue` и планирует пересчёт затронутых claim sheets.

---

## 4. Антипаттерны

| Антипаттерн | Проявление на ферме | Почему опасно | Как исправить |
|---|---|---|---|
| **CN/CG Spec-Ref Leakage** | «В статье сказано 85% — значит, у нас тоже 85%» | Внешние числа трактуются как законные score без привязки к CHR/CAL/CG | Типизировать через `SoSFeatureTransform` с `CharacteristicId/ScaleId` |
| **Implicit Crossings** | Использование данных с других видов/регионов без явного перехода | Результат неприменим; скрытые потери | `PlaneMapRef` + `CrossingBundle` с `CL/Φ` |
| **Edition Drift** | PubMed-импорт 2024 vs 2026 — разные снимки, но одинаковые `ClaimSheetId` | Несравнимость; устаревшие данные | `ExternalIndexRef.edition` на каждом артефакте |
| **Evidence Disconnect** | «Производные признаки» без привязки к EvidenceGraph | Невозможно опровергнуть или исправить | `EvidenceGraphId` + `PathSliceId[]` на каждом transform |
| **Format-as-Norm** | «У нас RO-Crate — это и есть спецификация» | Формат заменяет концептуальную поверхность | Сериализация — в Annex/Interop; норматив — в conceptual surfaces |
| **Shadow Governance** | Импортированные данные начинают определять «что считать правильным» | Внешний источник становится теневым legality gate | Все решения — через `G.5` + `G.Core`, не через импорт |

---

## 5. Пример на ферме: импорт PubMed-цитат в PACK

**Контекст:** Ферма «Волжское» создаёт PACK по протоколу переходного периода. Нужно интегрировать внешние исследования как inputs для SoTA-авторинга.

**Step 1 — Регистрация источника:**

```
ExternalIndexCard@Context: ⟨
  ExternalIndexId: EXT-PUBMED-TP-2025
  ProviderName: PubMed
  ExternalIndexType: CitationIndexWithAbstracts
  CoverageScope: «dairy cattle, transition period, metabolic disorders, 2018–2025»
  ExternalEdition: «PubMed snapshot 2025-01-15, query: ("dairy cattle"[Mesh]) AND ("transition period"[Title/Abstract]) AND ("ketosis" OR "fatty liver" OR "milk fever")»
  FreshnessWindow: 90 days
  describedEntity: ⟨DairyHerd, Volzhskoye_Farm_2025⟩
⟩
```

**Step 2 — Создание рецепта сопоставления:**

```
ClaimMapperCard@Context: ⟨
  MapperId: MAP-PUBMED-TP-001
  ExternalIndexId: EXT-PUBMED-TP-2025
  MappingPolicyRef: POLICY-VET-EVIDENCE-TO-DAIRY-2025
  Targets: {
    ClaimSheet: «Каждая статья → ClaimSheet с утверждениями о transition period»,
    BridgeHints: «Кросс-видовые: овца→корова, коза→корова, модель→практика»
  }
  ScaleEmbeddingSpecRef: SCALE-MODEL-TO-FARM-2025
    // «Модельные исследования in silico требуют bridge
    //  с CL=0.4 и Φ=0.6 при переносе на ферму»
  EvidenceGraphId: EVG-INTEROP-2025-001
⟩
```

**Step 3 — Типизация признаков:**

```
SoSFeatureTransform@Context: ⟨
  SoSFeatureTransformId: TRANSFORM-PUBMED-EVIDENCE-001
  Inputs: [ClaimSheet_001, ClaimSheet_002, ..., ClaimSheet_047]
  SoSFeatureSetId: SFS-TP-EVIDENCE-2025
  FeatureTypingRefs: {
    {CharacteristicId: EVIDENCE-DEPTH, ScaleId: ORDINAL-3LEVEL},
    {CharacteristicId: STUDY-DESIGN, ScaleId: CATEGORICAL-DESIGN},
    {CharacteristicId: SPECIES-VALIDITY, ScaleId: ORDINAL-SPECIES-MATCH}
  }
  ReferencePlane: DairyHerd_Practice_2025
  EvidenceGraphId: EVG-INTEROP-2025-001
  PathSliceId: [Slice_PubMed_Imported_2025]
⟩
```

**Step 4 — Интеграция в pipeline:**

```
G.2 (Harvest)    → ClaimSheets попадают в палитру операторов/объектов
G.3 (CHR)        → Типизированные признаки формализуются как CHR-характеристики
G.5 (Selector)   → Селектор выбирает множество методов под trade-offs
G.9 (Parity)     → Parity-сравнение методов с указанием evidence-depth
G.10 (Shipping)  → InteropSurface включается в shipped pack как cited payload
G.11 (Refresh)   → При обновлении PubMed — RSCR-триггер планирует пересчёт
```

**Step 5 — Обновление:**

Через 3 месяца PubMed обновляется. Smith et al. 2019 получает corrigendum.

```
IndexTelemetryPin: ⟨
  triggerKindId: EvidenceSurfaceEdit
  scope: [Slice_PubMed_Imported_2025]
  payloadPins: {
    ExternalIndexId: EXT-PUBMED-TP-2025,
    ExternalIndexRef.edition: «2025-04-01»,
    affectedClaimSheet: ClaimSheet_003,
    changeType: «corrigendum: PPG efficacy data corrected»
  }
⟩
```

`G.11` планирует refresh:
- `UpdateEvidenceBindings` для ClaimSheet_003
- `RerunParity` для методов, использовавших Smith et al. 2019
- `ReshipPack` с обновлённым `InteropSurfaceId`

---

## 6. Практика: с чего начать

**Шаг 1. Зарегистрируйте один внешний источник.**
Выберите один источник, который вы используете (PubMed, CAB Abstracts, внутренняя база консультанта). Создайте `ExternalIndexCard` с указанием edition, coverage и freshness window.

**Шаг 2. Опишите сопоставление.**
Как именно вы превращаете внешние данные во внутренние? Какие понятия соответствуют друг другу? Запишите `ClaimMapperCard`. Если есть кросс-видовые или кросс-контекстные переходы — объявите `PlaneMapRef` и `ScaleEmbeddingSpecRef`.

**Шаг 3. Типизируйте признаки.**
Не храните «ключевые выводы» как текст. Превратите их в CHR-типизированные признаки с `CharacteristicId` и `ScaleId`. Укажите `EvidenceGraphId` и `PathSliceId`.

**Шаг 4. Проверьте pipeline.**
Убедитесь, что импортированные данные проходят через `G.2 → G.3 → G.5`, а не напрямую влияют на решения. Селектор и parity остаются governed by `G.5` + `G.Core`.

**Шаг 5. Настройте обновление.**
Запишите `IndexTelemetryPin` для случая, когда внешний источник изменится. Какие `PathSlice` затронуты? Какие действия нужны?

---

## 7. Проверь себя

| Вопрос | Если ответ «не знаю» — проблема |
|---|---|
| Можете ли вы назвать редакцию внешнего источника, который использовали месяц назад? | Edition Drift |
| Есть ли у вас статьи из других видов/регионов, используемые без явного перехода? | Implicit Crossings |
| Храните ли вы «ключевые выводы» как текст без типизации? | Evidence Disconnect |
| Влияют ли импортированные данные на решения напрямую, минуя селектор? | Shadow Governance |
| Можете ли вы через год восстановить, как именно PubMed-статья повлияла на протокол? | Отсутствие EvidenceGraph |
| Считаете ли вы формат импорта (JSON, CSV, RO-Crate) спецификацией? | Format-as-Norm |

---

## 8. Связи

- **G.Core** — Part-G инварианты, `TriggerAliasMap`, Default Governing Definition Index.
- **G.2 (SoTA Harvest)** — ClaimSheets и BridgeHints из `ClaimMapperCard` попадают в harvest.
- **G.3 (CHR Pack)** — `SoSFeatureSet` формализуется как CHR-типизированные характеристики.
- **G.5 (Selector)** — селектор потребляет произведённые артефакты под своими governing spec refs.
- **G.6 (EvidenceGraph)** — `EvidenceGraphId` + `PathSliceId` обеспечивают трассировку.
- **G.7 (Bridge Sentinels)** — `PlaneMapRef` и `CrossingBundle` управляют кросс-контекстными переходами.
- **G.9 (Parity)** — parity может сравнивать методы с указанием evidence-depth из внешних источников.
- **G.10 (Shipping)** — `InteropSurface@Context` включается в shipped pack как cited payload.
- **G.11 (Refresh)** — `IndexTelemetryPin` эмитирует RSCR-триггеры для обновления.
- **A.19 / G.0** — CN-Spec и CG-Spec; interop не вводит теневых legality gates.

---

## 9. Что читать дальше

- **G.13:Ext.ExternalIndexProviderWiring** — провайдеро-специфичная проводка (OpenAlex, Crossref, ORKG)
- **G.13:Ext.EmbeddingBasedAlignment** — выравнивание на основе эмбеддингов (Phase-3 seed)
- **G.13:Ext.EntityResolutionAndAliasDocking** — разрешение сущностей и докирование алиасов
- **FPF-Spec.md §G.13** — полная нормативная версия

---

*Этот capture создан в рамках WP-1 (Саморазвитие — изучение FPF) для PACK-cattle-science.*
*Цель: сделать архитектурный паттерн читаемым без погружения в 50 страниц спецификации.*
