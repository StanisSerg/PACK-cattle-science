# Принцип G.2 — SoTA Harvester & Synthesis (FPF)

> **Источник:** FPF-Spec.md, раздел G.2  
> **Тип:** Архитектурный паттерн (Part G)  
> **Статус:** Stable

---

## Суть

G.2 — это **дисциплина сбора знаний перед проектированием**. Он не позволяет «просто почитать статьи и начать кодить». Он требует, чтобы вы явно зафиксировали: кто конкурирует, где расходятся, на каких доказательствах стоите, и отдали это downstream в виде структурированного, цитируемого пакета — сохраняя плюрализм и запрещая тихое слияние несовместимого.

---

## Проблема

Когда команда начинает новый CG-Frame, она сталкивается с литературой/практикой, которая:

- **Плюралистична** — несколько конкурирующих `Tradition` (школ мысли, методологий) с несовместимыми посылками;
- **Контекстно-зависима** — результаты работают только в своём `BoundedContext` и для конкретной `describedEntity`;
- **Методологически гетерогенна** — разные стили доказательств, операторы, нормы валидности;
- **Быстро устаревает** — особенно всё, что post-2015.

Если просто «прочитать статьи и написать код», downstream-паттерны (G.3 CHR, G.4 CAL, G.5 селектор) унаследуют скрытые семантические коллизии.

---

## Главный артефакт: `SoTA Synthesis Pack@CG-Frame`

Это не просто библиография. Пакет обязан содержать именованные, цитируемые компоненты:

| Компонент | Что это |
|-----------|---------|
| **G.2a CorpusLedger** | Реестр источников со статусом триажа (include / park / retire) и обоснованием |
| **G.2b ClaimSheets[Tradition]** | Утверждения **по каждой Tradition отдельно** — с контекстом, якорями доказательств (A.10), окнами свежести. **Не смешиваются по умолчанию.** |
| **G.2c OperatorAndObjectInventory** | Заглушки (stubs) операторов и измеримых терминов для downstream-авторинга CHR/CAL |
| **G.2d BridgeMatrix** | Матрица выравнивания/расхождения между Tradition × Tradition с явными потерями (`loss notes`) |
| **G.2e MicroExamples** | Проработанные микро-примеры для каждого несущего утверждения — на гетерогенных субстратах, с A.10-якорями |
| **G.2f UTSProposals** | Черновики Name Cards + MDS для публикуемых идентификаторов |
| **G.2g describedEntity Map** | Карта: термин/утверждение → ⟨GroundingHolon, ReferencePlane⟩ |
| **G.2h PRISMA Flow Record** | Прозрачный след отбора (исторический нейминг; нотационно-независим) |
| **G.2i SoSIndicatorFamilies** | Индикаторы как **семейства/варианты** с явной ветвью Acceptence, а не единый скаляр |
| **G.2j MethodFamilyCards** | Кандидатные семейства методов — с регионами валидности, известными failure modes, заглушками для G.5 |
| **G.2k GeneratorFamilyCards** | То же для генераторов (если применимо) |

Плюс экспортные представления: `SoTA_Set@CG-Frame` (M2-выход для downstream) и `SoTAPaletteDescription` (основная consumable surface).

---

## Ключевые принципы G.2

1. **Плюрализм по умолчанию.**  
   Пакет **должен** содержать ≥2 `Tradition` и ≥3 `U.BoundedContext`. Монокультура запрещена. Однолинейный «SoTA score» — антипаттерн.

2. **Не скаляризовать.**  
   Оценочные конструкты представляются как семейства/варианты (окна, ограничения, допущения) с ветвями Acceptance. Скалярный summary разрешён только как report-only, если владелец (G.4/G.5) явно не продвинул его.

3. **Нет тихого слияния (fusion).**  
   Утверждения разных Tradition хранятся дизъюнктно. Если нужно объединить — требуется либо (i) явное доказательство выравнивания (`BridgeMatrix` + `CC-GCORE-CROSS-1`), либо (ii) запись `GammaEpistSynthId` (alias **G.2-F**) с объединением провенанса, явными alignment-refs и assurance tuples. «По здравому смыслу» — недопустимо.

4. **Evidence-addressable.**  
   Каждое несущее утверждение цепляется к A.10-носителям. Микро-примеры без якорей — антипаттерн (AP-G2-4).

5. **Refreshable (RSCR).**  
   Все edition pins, policy pins, freshness windows закреплены. Любое изменение эмитирует типизированный `RSCRTriggerKindId`, а не свободный текст.

6. **Actionable для downstream.**  
   Пакет **обязан** эмитировать hand-off манифесты для G.3 (CHR), G.4 (CAL) и G.5 (registry/dispatch), чтобы downstream не переизобретал семантику.

---

## Harvester Loop (концептуальная хореография)

```
1. Объявить scope, plurality, describedEntity
2. Discover & triage → CorpusLedger
3. Дистилляция Claim Sheets (по Tradition, не смешивая)
4. Inventory operators/objects (как stubs, без threshold)
5. Build BridgeMatrix (alignment/divergence)
6. Γ_epist synthesis (только при явном fusion/substitution)
7. Micro-examples (≥2 на гетерогенных субстратах)
8. Gates (FamilyCoverageFloorK=3; если не прошёл — repair, не тихое ослабление)
9. Hand-off manifests → G.3 / G.4 / G.5
```

---

## Conformance: главные чекпоинты (CC-G2)

- **CC-G2-Pluralism-1:** ≥2 Tradition, ≥3 BoundedContext.
- **CC-G2-ClaimSheets-1:** по Tradition — отдельно, без cross-Tradition fusion по умолчанию.
- **CC-G2-Palette-1:** `SoTA_Set` и `SoTAPaletteDescription` реконструируются по id, без скрытой структуры.
- **CC-G2-Alignment-1:** cross-Tradition reuse — только через explicit crossing bundles.
- **CC-G2-GammaSynth-1:** fusion → обязательна `GammaEpistSynthId`.
- **CC-G2-Families-1:** индикаторы — семейства с Acceptance-ветвями, не скаляры.
- **CC-G2-CoverageGate-1:** `k=3` по умолчанию; при провале — broaden search, не silent weakening.

---

## Связи

- **Использует:** G.Core, A.10 (provenance), B.3 (trust/decay), F.9 (bridges/CL), G.0 (CG-Spec legality).
- **Потребляют:** G.1 (генератор), G.3 (CHR), G.4 (CAL), G.5 (dispatch), G.10 (shipping), G.11 (refresh).

---

*Создано: 2026-04-18 в ходе сессии применения FPF к PACK-cattle-science.*
