---
type: fpf-meta
subject: "MVP-внедрение FPF в PACK-cattle-science"
domain: cattle-science
created: 2026-04-18
updated: 2026-06-27
---

# MVP-внедрение FPF в PACK-cattle-science

> **Цель:** Получить 80% практической пользы от FPF за 20% времени.  
> **Формат:** 3 вечера по 1.5–2 часа каждый.  
> **Контекст:** Сессия 2026-04-18.

---

## Вечер 1. ClaimSheet-lite: привязать пороги к источникам

**Задача:** К каждому `rule_00N.py` добавить YAML-блок в начале файла. 5 полей. 10 минут на правило.

**Что это даёт:** Когда ветеринар ОАО МТК спросит «почему BHB 1.2», ты покажешь не комментарий в коде, а explicit card.

### Как сделать

Добавь в начало каждого `rule_engine/rules/rule_00N.py`:

```python
"""
---
rule_id: RULE-001
name: Ketosis-Threshold-Invalidation
source: "Galvão 2013 (CS.SOTA.002) + Bruinjé 2024 (CS.SOTA.001)"
threshold_basis: "BHB ≥ 1.2 mmol/L — clinical threshold for subclinical ketosis screening"
confidence: 0.75  # R_base
validity_region:
  breed: Holstein-Friesian
  dim: "3–14 days postpartum"
  context: "individual-cow metabolic screening"
failure_modes:
  - "FM1: False positive (BHB 1.2–1.4 without metabolic deficit) → overtreatment"
  - "FM2: Missed early ketosis (BHB 1.0–1.2, trajectory declining) — not caught by point threshold"
last_reviewed: "2026-04-18"
---
"""
```

**Для твоих 12 правил — 2 часа работы.** После этого у тебя будет **аудируемый паспорт каждого правила**.

---

## Вечер 2. Conflict Matrix: зафиксировать, кто кого перекрывает

**Задача:** Создать файл `rule_engine/CONFLICTS.md`. Таблица: какие правила/модули могут противоречить друг другу, при каких условиях, что делать.

**Что это даёт:** Сейчас `orchestrate.py` запускает `rule_001g` и всё. Когда добавишь `rule_002g`, `rule_003g` — система сломается от конфликтов. Conflict Matrix предотвращает это заранее.

### Как сделать

```markdown
# Conflict Matrix (MVP)

| Rule A | Rule B | Условие конфликта | Разрешение | Приоритет |
|--------|--------|-------------------|------------|-----------|
| RULE-001 (threshold) | RULE-001G (group) | BHB 1.1 индивидуально = норма, но +2σ от группового среднего | Group signal → `monitor`; Threshold signal → `no_action`. Если оба активны — Threshold wins (higher confidence). | Threshold: 0.75 > Group: 0.55 |
| RULE-002 (SCK screen) | RULE-003 (PG treat) | RULE-002 triggered, но RULE-001 blocked (clinical signs) | RULE-001 BLOCKED → Emergency protocol overrides PG. | Emergency: 1.0 > All |
| Group engine | Individual rules | Группа < 50 голов | Degrade group engine to `probe-only`; use individual thresholds. | N/A |
| T3 (MilkBot) | T1 (BHB threshold) | BHB норма, но M305 падает | Dual alert: metabolic normal, productivity risk. Do not merge into single score. | Parallel reporting |
```

**Это 1 час работы.** Но когда ты добавишь 13-е правило — ты будешь знать, куда его вставлять, а не ломать существующую логику.

---

## Вечер 3. R_eff-lite: доверие в коде

**Задача:** Добавить в `models.py` поле `confidence_score` и в `orchestrate.py` — простую политику разрешения конфликтов.

**Что это даёт:** Система перестаёт быть детерминированной в слепую. Она говорит: «Я 75% уверен в этом решении, но вот альтернатива с 55%».

### Как сделать

**Шаг 3a.** Добавить в `models.py`:

```python
@dataclass
class RuleMeta:
    """Паспорт правила (FPF ClaimSheet-lite)"""
    rule_id: str
    confidence: float  # 0.0–1.0, R_base
    validity_region: dict[str, Any] = field(default_factory=dict)
    failure_modes: list[str] = field(default_factory=list)


@dataclass
class Decision:
    triggered_rules: list[str] = field(default_factory=list)
    verdicts: list[str] = field(default_factory=list)
    primary_rule: str | None = None
    action: str | None = None
    reasoning: list[str] = field(default_factory=list)
    basis: dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0  # R_eff после применения Φ(CL)
```

**Шаг 3b.** Добавить в `orchestrate.py` (или `group_models.py`) функцию-арбитр:

```python
def resolve_conflict(decisions: list[Decision]) -> Decision:
    """
    Простейшая политика R4 (CL routing-lite):
    при конфликте выбираем решение с наибольшим confidence.
    Если разница < 0.2 — возвращаем Degrade(mode='probe-only').
    """
    if not decisions:
        return Decision(verdicts=["ABSTAIN"], reasoning=["No decisions available"])

    best = max(decisions, key=lambda d: d.confidence)

    # Проверяем, есть ли серьёзный конкурент
    contenders = [d for d in decisions if abs(d.confidence - best.confidence) < 0.2 and d != best]
    if contenders:
        return Decision(
            verdicts=["DEGRADE_PROBE_ONLY"],
            reasoning=[
                f"Conflicting signals: {best.primary_rule} (R_eff={best.confidence:.2f}) vs "
                f"{contenders[0].primary_rule} (R_eff={contenders[0].confidence:.2f}). "
                "Difference < 0.2 — require human review."
            ],
            confidence=best.confidence,
        )

    return best
```

**Шаг 3c.** В каждом `rule_00N.py` возвращать `confidence`:

```python
def evaluate(case: dict[str, Any]) -> tuple[Decision | None, Prediction | None]:
    # ... existing logic ...
    decision = Decision(
        triggered_rules=[RULE_ID],
        primary_rule=RULE_ID,
        action="PG_300ML_X_5_DAYS",
        confidence=0.75,  # R_base для этого правила
    )
    return decision, prediction
```

**Это 1.5–2 часа работы.**

---

## Что получится в итоге

| Было | Стало |
|------|-------|
| `if bhb >= 1.2:` — магия | `confidence=0.75, source="Galvão 2013"` — explicit |
| Group engine и individual rules в разных скриптах | Один арбитр `resolve_conflict()` с понятной политикой |
| «А вдруг они противоречат?» | «Вот таблица в CONFLICTS.md, мы это предвидели» |
| Новое правило = ломаем старое | Новое правило = новая строка в матрице, проверяем R_eff |
| «Почему система так решила?» — не знаем | «Потому что у этого правила R_eff=0.75, а у альтернативы 0.55» |

---

## Самый быстрый старт (если лень на 3 вечера)

Начни с **Вечера 2** — Conflict Matrix. Это даёт максимум пользы за минимум времени:

1. Открой `orchestrate.py`
2. Посмотри, какие модули вызываются
3. Запиши в `CONFLICTS.md`: «если group engine скажет GREEN, а individual rule скажет RED — что делать?»

**Ответ запиши прямо сейчас.** Иначе через месяц, когда добавишь reproductive rules, ты будешь дебажить это в продакшене.

---

*Создано: 2026-04-18 в ходе сессии применения FPF к PACK-cattle-science.*
