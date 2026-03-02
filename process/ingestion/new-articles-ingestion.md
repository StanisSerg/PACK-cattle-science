# New Articles Ingestion (2026-03-02)

> 5 новых статей для добавления в PACK-cattle-science

---

## Entry 004: Cabrera - Economic evaluation of reproductive performance

**Material:** Economic evaluation of reproductive performance

**Authors:** Victor E. Cabrera

**Year:** 2015

**Source Type:** Review article / Decision support tool

**Date Ingested:** 2026-03-02

**Relevance:** 
- Обзор экономической оценки воспроизводства
- Инструменты поддержки решений (UW-Madison)
- Связь репродуктивной эффективности с экономикой
- Расчёт ценности стельности, стоимости потери стельности

**Relevance Test:**
- [x] Within bounded context? YES (reproduction economics)
- [x] Relates to identified entities? YES (CS.METHOD.003, CS.METHOD.004)
- [x] Can be analyzed through distinctions? YES

**Status:** pending-analysis

**Initial Notes:**
- Обзорная статья от разработчика моделей Cabrera
- Описывает инструменты: economic value of dairy cow, heifer pregnancy rate, Wisconsin-Cornell dairy repro
- Закон убывающей отдачи для репродуктивной эффективности
- Сравнение ED vs TAI программ

**Priority:** High (обзор от ключевого автора)

**SoTA ID:** CS.SOTA.006 (предполагаемый)

---

## Entry 005: Carvalho et al. (2019) - Progesterone manipulation

**Material:** Effect of manipulating progesterone before timed artificial insemination on reproductive and endocrine outcomes in high-producing multiparous Holstein cows

**Authors:** P.D. Carvalho, V.G. Santos, H.P. Fricke, L.L. Hernandez, P.M. Fricke

**Year:** 2019

**Source Type:** Peer-reviewed research (field trial)

**DOI:** 10.3168/jds.2019-16536

**Date Ingested:** 2026-03-02

**Relevance:** 
- Манипуляция прогестероном перед TAI
- Двойная овуляция и двойняшность
- Эндокринные исходы
- High-producing cows (релевантно для современных стад)

**Relevance Test:**
- [x] Within bounded context? YES (reproduction, TAI)
- [x] Relates to identified entities? YES (pregnancy, ovulation)
- [x] Can be analyzed through distinctions? YES

**Status:** pending-analysis

**Initial Notes:**
- Double-Ovsynch protocol
- Low-P4 vs High-P4 группы
- Влияние на двойную овуляцию и двойняшность
- Может дополнить CS.METHOD.005

**Priority:** Medium (специфическая методика)

**SoTA ID:** CS.SOTA.007 (предполагаемый)

---

## Entry 006: De Vries (2017) - Genetic improvement vs longevity

**Material:** Economic trade-offs between genetic improvement and longevity in dairy cattle

**Authors:** A. De Vries

**Year:** 2017

**Source Type:** Peer-reviewed research (review/analysis)

**DOI:** 10.3168/jds.2016-11847

**Date Ingested:** 2026-03-02

**Relevance:** 
- Трейд-офф между генетическим прогрессом и долголетием
- Оптимальные нормы выбытия
- Влияние генетического лага
- Экономика замены

**Relevance Test:**
- [x] Within bounded context? YES (economics, culling)
- [x] Relates to identified entities? YES (CS.METHOD.004)
- [x] Can be analyzed through distinctions? YES

**Status:** pending-analysis

**Initial Notes:**
- Генетический прогресс ускоряется → больше выбытие?
- Но: оптимальная норма выбытия нечувствительна к генетическому улучшению
- Важнее амортизация коровы, чем генетический прогресс
- Подтверждает подход Cabrera 2012

**Priority:** High (фундаментальный экономический анализ)

**SoTA ID:** CS.SOTA.008 (предполагаемый)

---

## Entry 007: Hansson et al. (2025) - Voluntary waiting period

**Material:** Effect of voluntary waiting period length on milk yield, fertility, and culling in high-yielding, second-parity cows

**Authors:** A. Hansson, K. Holtenius, R. Båge, M. Lindberg, C. Kronqvist

**Year:** 2025

**Source Type:** Peer-reviewed research (field trial)

**DOI:** 10.3168/jds.2025-26348

**Date Ingested:** 2026-03-02

**Relevance:** 
- Длина VWP (50 vs 140 дней)
- Влияние на удой, фертильность, выбытие
- Second-parity cows (специфика)
- High-yielding herds

**Relevance Test:**
- [x] Within bounded context? YES (reproduction, VWP)
- [x] Relates to identified entities? YES (IEP/VWP decisions)
- [x] Can be analyzed through distinctions? YES

**Status:** pending-analysis

**Initial Notes:**
- 50-d vs 140-d VWP в controlled study
- 140 дней VWP — жизнеспособная альтернатива
- Не влияет на удой и фертильность (second parity)
- Может дополнить CS.METHOD.003 (IEP оптимизация)

**Priority:** High (современное исследование, релевантное для IEP)

**SoTA ID:** CS.SOTA.009 (предполагаемый)

---

## Entry 008: Hansson et al. (2025) - VWP (duplicate?)

**Material:** Effect of voluntary waiting period length on milk yield, fertility, and culling in high-yielding, second-parity cows

**Authors:** A. Hansson et al.

**Year:** 2025

**Note:** Похоже на дубликат Entry 007 или другую версию (preprint vs published)

**Status:** check-duplicate

**Action:** Проверить, не дубликат ли Entry 007

---

## Summary

| # | Статья | Приоритет | SoTA ID |
|---|--------|-----------|---------|
| 004 | Cabrera (2015) | High | CS.SOTA.006 |
| 005 | Carvalho (2019) | Medium | CS.SOTA.007 |
| 006 | De Vries (2017) | High | CS.SOTA.008 |
| 007 | Hansson (2025) | High | CS.SOTA.009 |
| 008 | Hansson (2025) | Check | — |

**Следующий шаг:** Создать SoTA-аннотации для статей 004-007

---

*Created: 2026-03-02*
