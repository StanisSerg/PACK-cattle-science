---
type: fpf-study
pattern: A.6.P
title: "Relational Precision Restoration: когда «связан с» недостаточно"
domain: cattle-science
difficulty: advanced
reading_time: 50 min
created: 2026-06-19
---

# A.6.P — Relational Precision Restoration: когда «связан с» недостаточно

## 1. Зачем это читать
«Эта ферма связана с кооперативом», «корова зависит от кормовой базы», «данные привязаны к сезону». Все эти фразы скрывают вид отношения, участников, направление, область действия и время. A.6.P учит восстанавливать скрытую структуру, прежде чем полагаться на такие утверждения.

**FPF-тезис:** *«Зонтичные глаголы — это не отношения. Это триггеры для ремонта.»*

## 2. История одной ошибки
В договоре с переработчиком было написано: «Ферма связана с переработчиком». Никто не уточнял, что именно поставляется, в какие сроки и по каким правилам. Когда переработчик отказался принять партию молока из-за бактерий, стороны спорили, чьё это обязательство — поставлять качественное сырьё или принимать весь объём.

## 3. Relational Precision Restoration: когда «связан с» недостаточно — полное описание

### 3.1 Когда применять
Используйте A.6.P, когда в тексте встречаются:

- «связан с», «зависит от», «влияет на», «основан на»;
- «синхронизирован», «привязан», «поддерживается»;
- «тот же», «эквивалентен», «соответствует»;
- метонимические или местоименные конечные точки («это», «здесь», «у них»);
- отношения, используемые для gate, assurance, cross-context reuse.

### 3.2 Рецепт RPR
```text
1. Восстановить head kind — что за вещь стоит за словом.
2. Определить конечные точки и их facets/kinds.
3. Выбрать стабильный lens (n-ary relation, base relation, bridge, span).
4. Заменить зонтичный глагол на явный RelationKind token.
5. Сделать слоты явными: scope, Γ_time, viewpoint, witnesses.
6. Разложить на L/A/D/E (A.6.B).
```

### 3.3 Candidate-Set Note
Если конечная точка неоднозначна, запишите:

```text
CandidateSetNote:
  triggerSpan: "у них"
  role: endpointRef(p2)
  candidates:
    - Coop_DairyNorth
    - Processor_B
    - RegionalLab_C
  selected: Processor_B
  why: contract reference #2026-044
  consequence: use deliversMilkTo, add contractRef slot
```

## 4. Почему смешивать / игнорировать — значит рисковать
Если пренебречь A.6.P, типичные риски на ферме:

| Что происходит | Почему это опасно |
|---|---|
| Решения принимаются на основе смешанных или устаревших данных | Невозможно отследить, что именно повлияло на результат |
| Роли и методы не разделены | Один и тот же человек или документ отвечает за несовместимые обязательства |
| Перенос знаний между контекстами без явного bridge | Рекомендации из одной традиции применяют к другой без учёта потерь |
| Отсутствие контрольного списка | Ошибки обнаруживаются слишком поздно, когда они уже стоят денег |

**Каскад:** нечёткое утверждение → неправильная интерпретация → некорректное решение → экономический убыток и снижение доверия к системе.

## 5. Как это выглядит на ферме: Фермерские примеры
### 5.1 «Ферма связана с переработчиком»
| Шаг | Ремонт |
|---|---|
| head kind | supply contract / milk delivery relation |
| endpoints | FarmA, DairyProcessorB |
| relation kind | `deliversMilkTo` |
| slots | volume (L/day), quality spec, pickup window, bridge to processor context |
| qualifiers | effective window, price formula, penalties |

Правильно:

```text
deliversMilkTo(
  supplier = FarmA,
  receiver = DairyProcessorB,
  productSpec = MilkQuality_SLA_v3,
  volumeSlot = 1200 L/day,
  Γ_time = 2026-01-01..2026-12-31,
  bridge = FarmContext→DairyContext(B-001, CL=low)
)
```

### 5.2 «Данные привязаны к сезону»
| Шаг | Ремонт |
|---|---|
| head kind | measurement series |
| relation kind | `validForSeason` или `sampledInSeason` |
| slots | datasetRef, seasonRef, weather window, grazing regime |

Правильно:

```text
validForSeason(
  dataset = PastureYield_2026,
  season  = GrazingSeason_2026_North,
  Γ_time  = 2026-05-01..2026-10-15,
  witnesses = {satelliteimagery#12, fieldlog#45}
)
```

## 6. Практическое применение: с чего начать
**Шаг 1.** Соберите все связи во внешних договорах и SOP, которые описаны размытыми глаголами («связано», «обслуживает», «координирует»).

**Шаг 2.** Для каждой связи восстановите точное relation name и endpoints.

**Шаг 3.** Опишите обязательные slots: что, сколько, когда, по какому критерию.

**Шаг 4.** Зафиксируйте bridge conditions для сравнения с другими объектами.

**Шаг 5.** Проверьте, не скрывается ли за одним relation'ом несколько разных связей.

## 7. Проверь себя
| Вопрос | Если ответ «да» — проблема |
|---|---|
| `CC-A.6P.1`: зонтичный глагол заменён на явный `RelationKind` token. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.6P.2`: все participant/qualifier slots явны (`SlotKind`, `ValueKind`, `RefKind`). | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.6P.3`: метонимические или местоименные endpoints восстановлены. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.6P.4`: scope, `Γ_time`, viewpoint и witnesses указаны, если нужны для решения. | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.6P.5`: cross-context relation использует Bridge + CL (F.9). | Контрольный критерий не выполнен — возможна структурная ошибка. |
| `CC-A.6P.6`: semantic change class явна (`retarget`, `revise`, `rescope`, `retime`, `refreshWitnesses`). | Контрольный критерий не выполнен — возможна структурная ошибка. |

## 8. Связь с другими паттернами
| Паттерн | Связь |
|---|---|
| A.6 Signature Stack | L/A/D/E раскладка. |
| A.6.B Boundary Norm Square | классификация claims. |
| A.6.6 Structured Witnessed Base Declaration | для basedness/anchored. |
| A.6.5 Relation Slot Discipline | SlotKind/ValueKind/RefKind. |
| A.10 Evidence Graph Referring | witnesses. |
| F.9 Bridges | cross-context relations. |
| F.18 Naming | mint-or-reuse RelationKind tokens. |
---

*Capture создан в рамках изучения FPF.*
*FPF Source: FPF/FPF-Spec.md §A.6.P*
