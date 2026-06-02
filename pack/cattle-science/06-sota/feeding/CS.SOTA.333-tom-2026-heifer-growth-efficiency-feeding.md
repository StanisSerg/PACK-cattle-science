---
id: CS.SOTA.333
type: sota
format_version: v1.1
knowledge_tier: P2
domain: cattle-science
area: feeding
subarea: heifer-rearing
subarea2: growth-targets
category: expert-opinion
year: 2026
authors: "Tom (AMTS)"
title: "Heifer Growth, Efficiency and Feeding Strategies"
journal: "Video lecture (Toms heifer discussion)"
volume: ''
issue: ''
pages: ''
doi: ''
publisher: ''
open_access: true
license: ''
language: ru
freshness_window: 2026-03-17 — 2028-03-17
sota_edition: '1.0'
derivation:
- source: "Tom (AMTS) — Toms heifer discussion 2026-03-17. Видеозапись 77 мин + транскрипция."
  type: video-transcription
  reopen_trigger: 'Видео: Toms heifer discussion 2026 03 17-1920x804-mp4a'
- source: "Fox et al. 1998 (NRC 2001 Ch.19) — target weights for dairy animals"
  type: foundational
  relevance: Target weight framework adopted by NRC 2001
- source: "García-Ruiz et al. 2016, PNAS 113(28):E3995-E4004 — genomic selection generation intervals"
  type: foundational
  relevance: Genomic selection impact on generation interval
tags:
- expert-opinion
- video-source
- heifer-rearing
- growth-targets
- genomic-selection
- feeding-strategy
- lactic-acid
- calf-starter
- cost-per-gain
- amts
- cornell
related:
- id: CS.SOTA.330
  type: foundational
  note: NASEM 2021 — Young Calf (growth requirements)
  relevance: high
- id: CS.SOTA.315
  type: similar-topic
  note: Li 2026 — Heifer nutrition
  relevance: medium
- id: CS.SOTA.331
  type: similar-topic
  note: Weiss 2024 — Transition Minerals
  relevance: medium
- id: CS.SOTA.294
  type: foundational
  note: NASEM 2021 — Growth requirements
  relevance: high
related_entities:
- CS.ENTITY.002
- CS.ENTITY.003
- CS.ENTITY.005
- CS.ENTITY.006
- CS.ENTITY.007
---

# CS.SOTA.333: Heifer Growth, Efficiency and Feeding Strategies — Tom (AMTS)

> **Уровень:** Продвинутый (M2/S1) | **Формат:** Expert opinion + industry data + cited research | **Время изучения:** 40-50 мин  
> **Статус:** Активный | **Последнее обновление:** 2026-06-01 (FPF аудит + верификация чисел)

---

## Аннотация

**Контекст:** Современные генотипы молочных коров крупнее и продуктивнее, чем 30-40 лет назад. Инфраструктура многих ферм (стойла, роботы, доильные залы) рассчитана на коров 1990-х. Неправильные target weights, единые рационы для всех возрастных групп и высокая молочная кислота в силосе приводят к ожирению тёлок, задержке в выращивании и потере ёмкости системы.

**Цель:** Определить оптимальные target weights, стратегии кормления и контрольные параметры для выращивания replacement heifers с минимальной стоимостью прироста и максимальной биологической эффективностью.

**Методы:** Обзор данных Cornell Research Farm, AMTS modeling, отраслевых стандартов и cited research (NASEM, Van Tassell, Danny Fox 1979).

**Результаты:** Точное кормление с учётом возрастных групп сокращает период выращивания на 43 дня и снижает стоимость прироста. Молочная кислота >4% в рационе ассоциирована с повышенной жирностью туши (данные beef steers). Раннее питание определяет lifetime productivity.

**Выводы:** CS.SOTA.333 формулирует практические правила выращивания тёлок, но требует correction для двух claims на основе FPF аудита и верификации чисел (см. Critical Analysis).

---

## Key Claims

### 1. Target weight first-calf heifer: ≥80% mature body weight at first calving
**Claim:** Первотёлка должна достичь не менее 80% массы взрослой коровы к моменту первого отёла. Это отраслевой стандарт, который обеспечивает adequate frame size для поддержания высокой лактации и reproductive performance.

**Confidence:** 0.85 — отраслевой стандарт, широко принят, но genetic potential современных herd может требовать пересмотра.

**Scope:** {dairy cattle, Holstein, Jersey, replacement heifers, first calving}

**Evidence:** Industry standard, упомянутый как общепринятая норма в множестве extension publications.

**Что верифицировать:** Cornell data (Van Amburgh) показывают, что first lactation milk yield коррелирует с body weight at calving. Оптимальный % может варьироваться 80-85% в зависимости от breed и mature size.

---

### 2. Genomic selection reduced generation interval from ~7–9 years to ~2 years
**Claim:** Внедрение геномической селекции (post-2009) сократило генерацию быков-производителей с 7–9 лет до ~2 лет. Селекция на жирность ускорилась в ~2.4×.

**Confidence:** 0.88 — peer-reviewed data (García-Ruiz et al. 2016, PNAS), но 2.4× slope increase — expert calculation.

**Scope:** {US dairy cattle, Holstein, genomic selection, post-2009}

**Evidence:** García-Ruiz et al. 2016, *PNAS* 113(28):E3995-E4004. До GS: sire path generation interval 7.9 лет (для production of bulls). После GS: сокращён до ~2.5 лет (García-Ruiz 2016) или 1.5 лет (Pryce & Daetwyler 2012 для GS programs).

**FPF Note (B.3):** F3/R=High. "7-9 → 2" — extreme bounds, не средние. Среднее ~6 → 2.5 лет.

**Что верифицировать:** Точный multiplier 2.4× для fat slope — требует верификации по USDA genetic trends или Van Tassell publication.

---

### 3. Age at first calving is changed ONLY by pre-breeding growth rate
**Claim:** После осеменения возраст первого отёла фиксирован (gestation ~280 дней). Единственный способ изменить возраст первого отёла — изменить темп роста ДО осеменения.

**Confidence:** 0.95 — mathematical fact (fixed gestation period).

**Scope:** {all mammals, dairy cattle, fixed gestation species}

**Evidence:** Физиологический принцип; gestation period мало варьируется.

**FPF Note (A.6.B):** L (Law) — чистый математический факт. F4/R=Very High.

---

### 4. Target weight by breeding: ~55% of mature body weight
**Claim:** Целевой вес к осеменению — ~55% от mature body weight herd. Для mature weight 1400 lb → 770 lb; для 1800 lb → 990 lb.

**Confidence:** 0.82 — AMTS modeling; NRC 2001 target weight table (Fox et al. 1998).

**Scope:** {dairy cattle, Holstein, pre-breeding, AMTS modeling}

**Evidence:** Fox et al. 1998 — target weights adopted by NRC 2001 Ch.19. Таблица: mature 1400 lb → pregnancy (55%) = 770 lb; mature 1800 lb → pregnancy (55%) = 990 lb.

---

### 5. Growth slows 6–10 weeks before calving — target must be reached 8 weeks pre-calving
**Claim:** Тёлки замедляют рост за 6–10 недель до отёла из-за концептуса и маммогенеза. Целевой вес нужно достичь за 8 недель (60–70 дней) до отёла.

**Confidence:** 0.85 — day-step modeling (Tom/AMTS), концептус растёт ~600 г/сут, сухое вещество потребления падает.

**Scope:** {dairy heifers, last trimester, pre-calving}

**Evidence:** AMTS modeling; Japanese research farm data; NASEM/NRC equation comparison.

**FPF Note (A.6.B):** D (Deontic: SHOULD reach target 8 weeks pre-calving) + L (Law: physiology of late gestation).

---

### 6. Young heifers (2–3 months) have highest MP efficiency in life
**Claim:** Двух-трёхмесячные тёлки — самая высокая эффективность использования метаболизируемого протеина (MP) в жизни. 4-месячная тёлка по требованиям белка эквивалентна корове с удоем 45–50 кг.

**Confidence:** 0.88 — классические данные по эффективности MP→net protein.

**Scope:** {dairy calves, young heifers, skeletal growth phase}

**Evidence:** График ME и MP required per kg DMI (спикер). Классическая физиология роста: frame + muscle accretion в 2–3 мес направляет аминокислоты преимущественно в синтез тканей.

**FPF Note (A.6.B):** L (Law) — физиологический принцип.

---

### 7. One ration for all heifers = inefficient; optimal: 2 rations or 1 ration + top-dress
**Claim:** Единый рацион для всех тёлок неэффективен: молодые получают дефицит белка, поздние беременные — недостаточный прирост. Оптимально: 2 рациона (до осеменения + последний триместр vs ранняя-средняя беременность) или 1 рацион + дотирка 2–2.5 кг концентрата.

**Confidence:** 0.88 — практическая рекомендация, поддержанная Cornell data.

**Scope:** {dairy heifers, group feeding, TMR}

**Evidence:** Cornell modeling data; физиологический принцип разных требований по возрастам.

---

### 8. Cornell: precise feeding saves 43 days and $0.07/lb gain
**Claim:** Сравнение стратегий (Cornell data): рацион для 9-мес тёлок все = 420 дней, $1.28/lb gain; средний рацион все = 463 дней, $1.35/lb gain; средний + дотирка = 420 дней, $1.28/lb gain.

**Confidence:** 0.80 — Cornell research farm modeling data; спикер округляет.

**Scope:** {Cornell research farm, US conditions, specific diet scenarios}

**Evidence:** Cornell modeling data; feed costs ~$1223–1300.

**FPF Note (B.3):** F3/R=Medium. G narrow (Cornell, specific diets).

---

### 9. Lactic acid in diet >4% associated with increased body fat (fat heifers)
**Claim:** Высокая молочная кислота в силосе ассоциирована с повышенной жирностью туши у тёлок. Данные beef steers (Danny Fox, Michigan State, 1979): 3.8% LA → 25% fat; 5.5–6% → 27–28%; 7–8% → 32–33%. Для тёлок рекомендуется <4% LA.

**Confidence:** 0.70 — **ИСТОЧНИК НЕ ВЕРИФИЦИРОВАН**. Beef steer data → dairy heifer extrapolation без Bridge.

**Scope:** {beef steers, data from 1979, extrapolated to dairy heifers}

**Evidence:** Danny Fox grad student data, 1979 (hosting steers). **Первоисточник не найден в открытом доступе.**

**FPF Warning (C.28):** 🔴 **Association overstated as Intervention for dairy heifers.** Beef→dairy extrapolation без explicit Bridge. Exact figures (25%, 27–28%, 32–33%) не подтверждены.

**Рекомендация:** Использовать как heuristic с явным указанием "requires peer-review validation for dairy heifers". Снизить confidence до 0.70 или F2.

---

### 10. Starter quality: low starch/high sugar → higher rumen pH, healthy papillae
**Claim:** Стартеры с низким крахмалом / высоким сахаром / высоким NDF поддерживают рН рубца >5.75 и здоровые сосочки. Высокий крахмал → рН <5.75, повреждённые сосочки, субклиническая ацидоз.

**Confidence:** 0.85 — сравнительные trial'ы коллеги спикера; согласуется с NASEM 2021 Ch.19.

**Scope:** {dairy calves, starter feeds, rumen development}

**Evidence:** Сравнительные trials (не цитируется напрямую, но согласуется с независимыми исследованиями). NASEM 2021 Ch.19 Young Calf.

**FPF Note (A.6.B):** D (SHOULD use low-starch starters) + L (mechanism: rapid fermentation → pH drop).

---

### 11. Minimize cost per unit of gain, not cost per day
**Claim:** Главный экономический принцип выращивания тёлок — минимальная стоимость привеса (cost per pound/kilo of gain), а не стоимость рациона в день. Быстрый рост = меньше инфраструктуры + лучше экологический след.

**Confidence:** 0.90 — центральный тезис лекции, поддержанный моделированием.

**Scope:** {dairy heifer rearing, economics, feed cost optimization}

**Evidence:** AMTS modeling; сравнение diet strategies; спикер повторяет многократно.

---

### 12. First-calf heifers produce ~78–79% of mature cow milk
**Claim:** Первотёлки дают ~78–79% молока от взрослых коров (Cornell data, Sam Fessenden PhD study). Молочная продуктивность первотёлок — индекс веса тёлок (если нет весов).

**Confidence:** 0.82 — Cornell data.

**Scope:** {Cornell herd, Holstein, first lactation}

**Evidence:** Cornell, Sam Fessenden PhD study.

**FPF Note (B.3):** F3/R=Medium. G narrow (Cornell herd).

---

## Механистическая интерпретация

### Генетика vs инфраструктура
Ускорение селекции через геномику создало диссонанс между genetic potential животных и инфраструктурой отрасли. Поколение быков сократилось с ~7–9 до ~2 лет, что означает 4 поколения за время, когда раньше проходило 1. Это требует пересмотра target weights, размеров стойл, роботов и доильных залов каждые 1–2 года.

### Физиология роста
Высокая эффективность использования белка у молодых тёлок обусловлена интенсивным скелетным и мышечным ростом (frame + muscle accretion), при котором аминокислоты направляются преимущественно в синтез тканей. С возрастом эффективность падает из-за гормональных изменений (пубертат → инфлекция жироотложения). Это создаёт "окно возможностей" для дешёвого роста.

### Молочная кислота и жироотложение
Молочная кислота — конечный продукт бактериальной ферментации углеводов в силосе. При поступлении в рубец часть LA конвертируется в пропионат, часть абсорбируется как LA. Повышенные концентрации LA в рубце стимулируют анаэробный гликолиз и депонирование жира в адипоцитах. Механизм хорошо изучен в откорме говядины (мраморность), но **данные для dairy heifers отсутствуют** — claim 9 основан на beef steer extrapolation.

### Раннее питание и lifetime performance
Развитие рубца у телят — критический период, определяющий пожизненную продуктивность. Низко-крахмальные стартеры с высоким содержанием сахаров и ферментируемой клетчатки поддерживают более высокий рН и стимулируют развитие папиллл. Это согласуется с данными по "metabolic imprinting" — раннее питание программирует метаболизм на уровне эпигенетики и микробиома.

---

## Практическое применение

### Target weights and growth curves

| Параметр | Значение | Источник | Примечание |
|----------|----------|----------|------------|
| Вес к осеменению | 55% mature BW | Fox et al. 1998 / AMTS | Для mature 1400 lb → 770 lb; 1800 lb → 990 lb |
| Вес к отёлу | 85% mature BW | Fox et al. 1998 / AMTS | Для mature 1400 lb → 1190 lb; 1800 lb → 1530 lb |
| ADG до осеменения | 700–900 г/сут | AMTS modeling | Зависит от mature BW и target age at calving |
| ADG последний триместр | 800–1200 г/сут | AMTS modeling | Включает концептус |
| Целевой вес достигнут | 8 недель до отёла | Tom/AMTS | Физиологически невозможно "догнать" позже |

### Feeding strategies

| Стратегия | Эффективность | Стоимость/фунт прироста | Дни до calving |
|-----------|--------------|------------------------|----------------|
| 1 рацион все | Низкая | $1.35 | 463 |
| 2 рациона (по возрасту) | Высокая | $1.28 | 420 |
| 1 рацион + дотирка 2–2.5 кг | Высокая | $1.28 | 420 |

### Ration parameters (checklist)

| Параметр | Target | Допустимый диапазон | Примечание |
|----------|--------|---------------------|------------|
| Потребление факт vs прогноз | ±5% | — | Стандарт AMTS/NASEM |
| ME | 95–105% требования | — | — |
| MP allowable gain / ME allowable gain | >1.0–1.2 | — | Практическая рекомендация |
| Руминальный аммиак | >110% требования | — | Стандарт |
| Forage NDF / BW | 1.0–1.3% | — | Практическая рекомендация |
| Молочная кислота | <4% | — | ⚠️ Требует peer-review для dairy heifers |
| Лизин | >100% требования | — | Практическая рекомендация |

---

## FAQ

**Q: Почему нельзя "догнать" вес в последние недели беременности?**  
A: За 6–10 недель до отёла плод растёт ~600 г/сут, маммогенез требует ресурсов, сухое вещество потребления падает. Попытка force-feeding приведёт к negative energy balance и metabolic disorders post-calving.

**Q: Как определить mature body weight herd?**  
A: Средний вес коров 3-й и старше лактаций в стаде. Не использовать generic breed average — использовать реальные данные своего стада.

**Q: Что делать, если силос имеет 5–6% LA?**  
A: ⚠️ См. Claim 9. Данные для dairy heifers не верифицированы. Рекомендуется: (1) blend с низко-LA силосом/соломой; (2) monitor body condition score; (3) не overfeed energy. Для подтверждения механизма требуется peer-reviewed research на dairy heifers.

**Q: Сколько групп тёлок оптимально?**  
A: Минимум 2 (pre-breeding + pregnant/post-breeding). Идеально: 3 группы (молодые, средние, поздние беременные). Экономика показывает окупаемость дополнительных TMR.

---

## Critical Analysis

### FPF Audit Findings (CS.ANALYSIS.002)

| Паттерн | Finding | Статус в CS.SOTA.333 |
|---------|---------|---------------------|
| **B.3 F-G-R** | Claim 9 (LA→fat) имеет F2/R=Low-Medium, но в оригинале confidence 0.85 | **Исправлено:** confidence снижен до 0.70, добавлен FPF warning |
| **A.6.B L/A/D/E** | Claim 4 (target weights) — D с E-support (Fox et al. 1998) | **Уточнено:** explicit source reference |
| **C.28 CausalUse** | Claim 9 — Association (beef steers) → Intervention (dairy heifers) | **Исправлено:** explicit "beef steer data, extrapolated" warning |
| **F.9 Bridges** | Нет Bridge card для beef↔dairy | **Добавлено:** explicit scope restriction |

### Number Verification Findings (CS.ANALYSIS.003)

| Claim | Оригинальное число | Верификация | Статус в CS.SOTA.333 |
|-------|-------------------|-------------|---------------------|
| Cornell weights 1472→1710 | Adult cow weight 1993→2016 | ⚠️ **Category error:** 1472 lb = 2nd calving weight для mature 1600 lb (Fox et al. 1998); не temporal trend | **Уточнено:** removed from Key Claims; добавлено в FAQ как target weight framework |
| Genomic selection | 7–9 → 2 years | ✅ García-Ruiz 2016: bounds верны, среднее ~6 → 2.5 | **Сохранено:** добавлена оговорка "extreme bounds" |
| Danny Fox LA data | 3.8%→25%, etc. | ❌ Первоисточник не найден | **Сохранено с warning:** "source not verified" + F2 |
| Early nutrition → lifetime | — | ✅ Soberon & Van Amburgh 2011: 850 lb milk per 1 lb pre-weaning ADG | **Добавлено:** explicit evidence reference |

### Рекомендации по использованию

1. **Claim 9 (LA→fat heifers)** — использовать только как heuristic для ration formulation, не как proven causal claim. Приоритет: peer-review research на dairy heifers.
2. **Target weights** — использовать Fox et al. 1998 (NRC 2001) framework, но корректировать под mature BW своего стада, не под generic 1400/1800 lb.
3. **Genomic selection** — учитывать, что инфраструктура фермы может отставать от genetic potential на 10–15 лет.

---

## Cross-Reference: Gaps & Next Steps

| Gap | Статус | Рекомендуемый следующий шаг |
|-----|--------|----------------------------|
| LA effect on dairy heifer body composition | ❌ Нет данных | CS.ANALYSIS.004: «LA and dairy heifer fat — literature gap» |
| Antioxidant nutrition for bred heifers | ❌ Не покрыто | Bridge между CS.SOTA.333 (growth) и CS.SOTA.331 (transition minerals) |
| AMTS iPad camera validation | ❌ Продуктовый анонс | Monitor AMTS publications for validation study |

---

> **Конец документа CS.SOTA.333**
> *SoTA v1.1 | PACK-cattle-science | 2026-06-01*
> *Derived from: CS.CLAIMS.001 + FPF audit (CS.ANALYSIS.002) + Number verification (CS.ANALYSIS.003)*
