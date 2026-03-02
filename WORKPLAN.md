---
type: workplan
updated: 2026-03-02
---

# WORKPLAN: PACK-cattle-science

> Рабочие продукты для Pack'а «Наука о содержании и кормлении КРС»

---

## Текущий статус

| Фаза | Статус | Прогресс |
|------|--------|----------|
| Phase A: Domain Contract | 🔄 В работе | Bounded context ✓, Distinctions ✓, SoTA 5 шт. ✓ |
| Phase B: Methods & Entities | ⏳ Не начата | Требуется формализация методов |
| Phase C: Work Products | ⏳ Не начата | Шаблоны отчётов |
| Phase D: Integration | ⏳ Не начата | Связь с курсом |

---

## Активные РП

| # | РП | Бюджет | Статус | Критерии приёмки |
|---|-----|--------|--------|------------------|
| 1 | SoTA: Bruinjé 2024 | 2h | ✅ Done | Аннотация создана, интегрирована в карту |
| 2 | SoTA: Galvão 2013 | 2h | ✅ Done | Аннотация создана, интегрирована в карту |
| 3 | SoTA Index (CS.MAP.001) | 1h | ✅ Done | Навигационная карта по всем источникам |
| 4 | Обновить манифест пака | 0.5h | ✅ Done | Сущности, методы, work products добавлены |

---

## Ближайшие РП (следующая сессия)

| # | РП | Бюджет | Приоритет |
|---|-----|--------|-----------|
| 5 | CS.METHOD.003: Reproductive program evaluation | 4h | High |
| 6 | CS.METHOD.005: Transition health monitoring | 4h | High |
| 7 | CS.WP.003: Reproduction economic report (template) | 3h | Medium |
| 8 | CS.WP.005: Health-fertility risk assessment (template) | 3h | Medium |

---

## Бэклог

### Methods
- [ ] CS.METHOD.001: Protein norm calculation
- [ ] CS.METHOD.002: Energy requirement assessment
- [ ] CS.METHOD.004: Economic simulation modeling
- [ ] CS.METHOD.006: Reproductive program selection

### Domain Entities (полная спецификация)
- [ ] CS.ENTITY.001: 21-day pregnancy rate (полная карточка)
- [ ] CS.ENTITY.002: Postpartum health syndrome (полная карточка)
- [ ] CS.ENTITY.003: Reproductive program efficiency (полная карточка)

### Work Products
- [ ] CS.WP.006: Reproductive program economic analysis

### SoTA (будущие)
- [ ] Добавить SoTA по кормлению (не репродукция)
- [ ] Добавить SoTA по профилактике метаболических заболеваний

---

## Связь с другими проектами

| Проект | Зависимость | Статус |
|--------|-------------|--------|
| DS-cattle-course | PACK-cattle-science → downstream | Module 1 в работе |
| PACK-personal (Phase A) | Независимый | В работе |

---

*Workplan version: 0.1.0 | Updated: 2026-03-01*
