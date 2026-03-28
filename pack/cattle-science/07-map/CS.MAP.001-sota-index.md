# CS.MAP.001: SoTA Index — Научные источники

> Карта научно-обоснованных знаний в PACK-cattle-science
> 
> **Версия:** 2.0 (Sharded)  
> **Всего SoTA:** 65  
> **Последнее обновление:** 2026-03-28

---

## Быстрая навигация (шарды)

| Область | SoTA | Шард | Описание |
|---------|------|------|----------|
| 🧬 **reproduction** | 11 | [Перейти →](./sota-index/CS.MAP.001-reproduction.md) | Репродуктивный менеджмент, TAI, синхронизация |
| 🌾 **feeding** | 13 | [Перейти →](./sota-index/CS.MAP.001-feeding.md) | Кормление, метаболизм, переходный период |
| 🏥 **health** | 36 | [Перейти →](./sota-index/CS.MAP.001-health.md) | Здоровье, кетоз, иммунитет, печень |
| 💰 **economics** | 4 | [Перейти →](./sota-index/CS.MAP.001-economics.md) | Экономика, моделирование, оптимизация |
| 📊 **management** | 1 | [Перейти →](./sota-index/CS.MAP.001-management.md) | Менеджмент, алгоритмы, оценка |

---

## Статистика по уровням

| Уровень | Количество | Описание |
|---------|------------|----------|
| **P0** — Фундаментальные | 5 | Определяют парадигму |
| **P1** — Критически важные | 30 | Meta-analysis, крупные обзоры |
| **P2** — Важные | 29 | Эксперименты, уточняющие исследования |

---

## Статистика по типам

| Тип | Количество | % |
|-----|------------|---|
| Review | 22 | 34% |
| Field-study | 21 | 33% |
| Experimental | 12 | 19% |
| Meta-analysis | 4 | 6% |
| Simulation | 3 | 5% |
| Survey | 2 | 3% |

---

## Хронология

| Период | Количество |
|--------|------------|
| 1977-1990 | 5 |
| 1991-2000 | 8 |
| 2001-2010 | 12 |
| 2011-2020 | 22 |
| 2021-2025 | 17 |

---

## Поиск

- **По ID:** Ctrl+F → `CS.SOTA.XXX`
- **По автору:** Ctrl+F → фамилия
- **По тегу:** Перейти в соответствующий шард
- **По теме:** См. разделы "По темам" в шардах

---

## Полный список (компактный)

### Reproduction (11)
`CS.SOTA.001` `CS.SOTA.002` `CS.SOTA.003` `CS.SOTA.004` `CS.SOTA.005` `CS.SOTA.006` `CS.SOTA.007` `CS.SOTA.014` `CS.SOTA.019` `CS.SOTA.023` `CS.SOTA.025`

### Feeding (13)
`CS.SOTA.012` `CS.SOTA.013` `CS.SOTA.015` `CS.SOTA.016` `CS.SOTA.017` `CS.SOTA.018` `CS.SOTA.031` `CS.SOTA.048` `CS.SOTA.049` `CS.SOTA.057` `CS.SOTA.059` `CS.SOTA.064`

### Health (36)
`CS.SOTA.008` `CS.SOTA.009` `CS.SOTA.020` `CS.SOTA.026` `CS.SOTA.027` `CS.SOTA.028` `CS.SOTA.029` `CS.SOTA.030` `CS.SOTA.032` `CS.SOTA.035` `CS.SOTA.036` `CS.SOTA.037` `CS.SOTA.038` `CS.SOTA.039` `CS.SOTA.040` `CS.SOTA.041` `CS.SOTA.042` `CS.SOTA.043` `CS.SOTA.044` `CS.SOTA.045` `CS.SOTA.046` `CS.SOTA.047` `CS.SOTA.053` `CS.SOTA.054` `CS.SOTA.055` `CS.SOTA.056` `CS.SOTA.058` `CS.SOTA.059` `CS.SOTA.060` `CS.SOTA.061` `CS.SOTA.062` `CS.SOTA.063` `CS.SOTA.065` `CS.SOTA.066` `CS.SOTA.067` `CS.SOTA.068`

### Economics (4)
`CS.SOTA.021` `CS.SOTA.022` `CS.SOTA.024` `CS.SOTA.069`

### Management (1)
`CS.SOTA.026`

---

## Структура папок

```
06-sota/
├── reproduction/     # 11 SoTA
├── feeding/          # 13 SoTA
├── health/           # 36 SoTA
├── economics/        # 3 SoTA
└── management/       # 1 SoTA
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
│   ├── CS.MAP.001-feeding.md (13 SoTA)
│   ├── CS.MAP.001-health.md (36 SoTA)
│   ├── CS.MAP.001-economics.md (3 SoTA)
│   └── CS.MAP.001-management.md (1 SoTA)
```

**Преимущества:**
- Быстрый доступ к нужной области
- Параллельное редактирование
- Масштабируемость до 1000+ SoTA

---

*Версия 2.0 — Шардированная структура*  
*Создано: 2026-03-28*
