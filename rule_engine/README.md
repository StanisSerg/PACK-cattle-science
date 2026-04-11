# Rule Engine v1.0

Исполняемая система правил для PACK-cattle-science.

## Архитектура

```
rule_engine/
├── models.py           # Dataclasses: Prediction, Decision, Evaluation
├── run_case.py         # Главный скрипт: кейс → правила → decision
├── evaluate_case.py    # Оценка: prediction vs fact
├── requirements.txt    # Зависимости
├── rules/              # Модули правил
│   ├── __init__.py
│   ├── rule_002.py     # SCK screening
│   └── rule_003.py     # PG treatment
└── cases/              # Кейсы
    └── CASE-001.yaml
```

## Установка

```bash
cd rule_engine
pip install -r requirements.txt
```

## Использование

### Шаг 1: Создать кейс

```yaml
# cases/CASE-001.yaml
case_id: CASE-001
input:
  bhb: 1.4
  dim: 6
  dmi_actual: 9.5
  dmi_norm: 16.0
  clinical_signs: []
  can_swallow: true
```

### Шаг 2: Запустить rule engine

```bash
python run_case.py cases/CASE-001.yaml
```

**Вывод:**
```
✓ Updated case: cases/CASE-001.yaml
  Primary rule: RULE-003
  Action: PG_300ML_X_5_DAYS_2X_DAILY
  Verdicts: ['RULE_002_TRIGGERED', 'RULE_003_APPLICABLE']
  Prediction: {'bhb': 'down', 'dmi': 'up'}
  Confidence: medium
```

### Шаг 3: Добавить фактические результаты

Отредактировать `cases/CASE-001.yaml`:

```yaml
fact:
  bhb_day7: 0.7
  dmi_day7: 15.2
```

### Шаг 4: Оценить результат

```bash
python evaluate_case.py cases/CASE-001.yaml
```

**Вывод:**
```
✓ Evaluation complete: cases/CASE-001.yaml
  Status: success
  Error type: None
  Root cause: None
  ✓ bhb_day7: fact=0.7, range=[0.6, 0.9]
  ✓ dmi_day7: fact=15.2, range=[14.0, 18.0]
```

## Принципы

1. **Прозрачность** — каждое решение объяснено (reasoning, basis)
2. **Детерминированность** — одинаковый input → одинаковый output
3. **Объяснимость** — можно проследить логику от input до decision
4. **Повторяемость** — кейс живёт во времени, дополняется fact

## Структура кейса

```yaml
case_id: CASE-XXX
input:          # Исходные данные
  bhb: 1.4
  dim: 6
  ...

derived:        # Рассчитывается автоматически
  dmi_ratio: 0.594
  bcs_loss: 0.5

decision:       # Заполняется run_case.py
  triggered_rules: [RULE-002, RULE-003]
  primary_rule: RULE-003
  action: PG_300ML_X_5_DAYS_2X_DAILY
  reasoning: [...]
  basis: {...}

prediction:     # Заполняется run_case.py
  direction: {bhb: down, dmi: up}
  range: {bhb_day7: [0.6, 0.9], dmi_day7: [14.0, 18.0]}
  confidence: medium

fact:           # Заполняется вручную через 7 дней
  bhb_day7: 0.7
  dmi_day7: 15.2

result:         # Заполняется evaluate_case.py
  status: success
  delta: {...}
```

## Приоритизация правил (v1)

```
Priority (high to low):
  100: RULE_003_BLOCKED       → Clinical emergency
   95: RULE_003_NOT_APPLICABLE → Severe SCK
   90: RULE_002_BLOCKED        → Clinical signs
   80: RULE_003_APPLICABLE     → PG treatment
   70: RULE_002_TRIGGERED      → SCK detected
   60: RULE_002_GRAY_ZONE      → Monitor
   10: NOT_TRIGGERED           → No action
```

## Roadmap

- [x] v1.0: Basic rules (002, 003)
- [ ] v1.1: Add RULE-001 (systemic decision)
- [ ] v1.2: Add RULE-005 (calcium)
- [ ] v1.3: State machine integration
- [ ] v2.0: Batch processing for herds
