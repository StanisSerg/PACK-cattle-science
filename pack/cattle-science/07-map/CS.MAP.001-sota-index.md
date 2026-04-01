# CS.MAP.001: SoTA Index — Научные источники

> Карта научно-обоснованных знаний в PACK-cattle-science
> 
> **Версия:** 2.1 (Sharded)  
> **Всего SoTA:** 114  
> **Последнее обновление:** 2026-04-01

---

## Быстрая навигация (шарды)

| Область | SoTA | Шард | Описание |
|---------|------|------|----------|
| 🧬 **reproduction** | 12 | [Перейти →](./sota-index/CS.MAP.001-reproduction.md) | Репродуктивный менеджмент, TAI, синхронизация |
| 🌾 **feeding** | 44 | [Перейти →](./sota-index/CS.SOTA.feeding.index.md) | Кормление, метаболизм, переходный период |
| 🏥 **health** | 48 | [Перейти →](./sota-index/CS.MAP.001-health.md) | Здоровье, кетоз, иммунитет, печень |
| 💰 **economics** | 4 | [Перейти →](./sota-index/CS.MAP.001-economics.md) | Экономика, моделирование, оптимизация |
| 📊 **management** | 2 | [Перейти →](./sota-index/CS.MAP.001-management.md) | Менеджмент, алгоритмы, оценка |

---

## Статистика по категориям

```
Всего SoTA: 105
├── health:        48 ████████████████████████████████████ (46%)
├── feeding:       40 ████████████████████████████████░░░░ (38%)
├── reproduction:  12 ██████████░░░░░░░░░░░░░░░░░░░░░░░░░░ (11%)
├── economics:      4 ███░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (4%)
└── management:     2 ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ (2%)
```

---

## Статистика по уровням

| Уровень | Количество | Описание |
|---------|------------|----------|
| **P0** — Фундаментальные | 8 | Определяют парадигму |
| **P1** — Критически важные | 45 | Meta-analysis, крупные обзоры |
| **P2** — Важные | 48 | Эксперименты, уточняющие исследования |

---

## Хронология

| Период | Количество |
|--------|------------|
| 1977-1990 | 8 |
| 1991-2000 | 12 |
| 2001-2010 | 18 |
| 2011-2020 | 28 |
| 2021-2025 | 35 |

---

## Поиск

- **По ID:** Ctrl+F → `CS.SOTA.XXX`
- **По автору:** Перейти в шард категории
- **По тегу:** Перейти в соответствующий шард
- **По теме:** См. разделы "По темам" в шардах

---

## Полный список (компактный)

### Reproduction (13)
`CS.SOTA.001` `CS.SOTA.002` `CS.SOTA.003` `CS.SOTA.004` `CS.SOTA.005` `CS.SOTA.006` `CS.SOTA.007` `CS.SOTA.010` `CS.SOTA.014` `CS.SOTA.019` `CS.SOTA.023` `CS.SOTA.025` `CS.SOTA.112`

### Feeding (47)
`CS.SOTA.012` `CS.SOTA.013` `CS.SOTA.015` `CS.SOTA.016` `CS.SOTA.017` `CS.SOTA.018` `CS.SOTA.031` `CS.SOTA.033` `CS.SOTA.034` `CS.SOTA.048` `CS.SOTA.049` `CS.SOTA.057` `CS.SOTA.064` `CS.SOTA.070` `CS.SOTA.072` `CS.SOTA.073` `CS.SOTA.074` `CS.SOTA.075` `CS.SOTA.076` `CS.SOTA.077` `CS.SOTA.078` `CS.SOTA.079` `CS.SOTA.080` `CS.SOTA.081` `CS.SOTA.082` `CS.SOTA.083` `CS.SOTA.084` `CS.SOTA.085` `CS.SOTA.086` `CS.SOTA.087` `CS.SOTA.088` `CS.SOTA.089` `CS.SOTA.090` `CS.SOTA.095` `CS.SOTA.096` `CS.SOTA.098` `CS.SOTA.100` `CS.SOTA.101` `CS.SOTA.102` `CS.SOTA.105` `CS.SOTA.106` `CS.SOTA.107` `CS.SOTA.108` `CS.SOTA.111` `CS.SOTA.113` `CS.SOTA.114`

### Health (48)
`CS.SOTA.008` `CS.SOTA.009` `CS.SOTA.020` `CS.SOTA.026` `CS.SOTA.027` `CS.SOTA.028` `CS.SOTA.029` `CS.SOTA.030` `CS.SOTA.032` `CS.SOTA.035` `CS.SOTA.036` `CS.SOTA.037` `CS.SOTA.038` `CS.SOTA.039` `CS.SOTA.040` `CS.SOTA.041` `CS.SOTA.042` `CS.SOTA.043` `CS.SOTA.044` `CS.SOTA.045` `CS.SOTA.046` `CS.SOTA.047` `CS.SOTA.053` `CS.SOTA.054` `CS.SOTA.055` `CS.SOTA.056` `CS.SOTA.058` `CS.SOTA.059` `CS.SOTA.060` `CS.SOTA.061` `CS.SOTA.062` `CS.SOTA.063` `CS.SOTA.065` `CS.SOTA.066` `CS.SOTA.067` `CS.SOTA.068` `CS.SOTA.091` `CS.SOTA.092` `CS.SOTA.093` `CS.SOTA.094` `CS.SOTA.097` `CS.SOTA.103` `CS.SOTA.104` `CS.SOTA.106` `CS.SOTA.107` `CS.SOTA.108

### Economics (4)
`CS.SOTA.021` `CS.SOTA.022` `CS.SOTA.024` `CS.SOTA.069`

### Management (2)
`CS.SOTA.026` `CS.SOTA.099`

---

## Структура папок

```
06-sota/
├── reproduction/     # 12 SoTA
├── feeding/          # 40 SoTA
├── health/           # 48 SoTA
├── economics/        # 4 SoTA
└── management/       # 2 SoTA
```

---

## Обновление индекса

При добавлении нового SoTA:
1. Добавить в соответствующий шард
2. Обновить счётчики в мастер-индексе
3. Обновить хронологию при необходимости

---

## Архитектура шардирования

```
CS.MAP.001-sota-index.md (мастер)
├── sota-index/
│   ├── CS.MAP.001-reproduction.md (11 SoTA)
│   ├── CS.SOTA.feeding.index.md (40 SoTA)
│   ├── CS.MAP.001-health.md (44 SoTA)
│   ├── CS.MAP.001-economics.md (4 SoTA)
│   └── CS.MAP.001-management.md (2 SoTA)
```

**Преимущества:**
- Быстрый доступ к нужной области
- Параллельное редактирование
- Масштабируемость до 1000+ SoTA

---

## Прогресс к цели

| Метрика | Значение |
|---------|----------|
| **Цель SoTA** | 400 |
| **Текущий прогресс** | 105 (26%) |
| **Осталось** | 299 |
| **Темп обработки** | ~5 мин/статью |
| **Оценка времени** | ~25 часов |

---

*Версия 2.3 — Обновлено: 2026-04-01*  
*Автоматический подсчёт: 105 SoTA*
