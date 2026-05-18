# Методы (Methods)

> **Назначение:** Клинические протоколы, методы мониторинга и диагностические алгоритмы  
> **Источник:** Синтез SoTA-данных + доменный опыт  
> **Формат:** SPF-совместимые метод-карты (YAML frontmatter + структурированные разделы)

---

## Структура

| ID | Файл | Назначение | Статус |
|----|------|-----------|--------|
| CS.METHOD.001 | [ketosis-diagnosis-treatment.md](./CS.METHOD.001-ketosis-diagnosis-treatment.md) | Диагностика и лечение кетоза | 🟢 Active |
| CS.METHOD.002 | [hypocalcemia-diagnosis-treatment.md](./CS.METHOD.002-hypocalcemia-diagnosis-treatment.md) | Диагностика и лечение гипокальцемии | 🟢 Active |
| CS.METHOD.005 | [calcium-monitoring-hypocalcemia-prevention.md](./CS.METHOD.005-calcium-monitoring-hypocalcemia-prevention.md) | Мониторинг кальция и профилактика гипокальцемии | 🟢 Active |

---

## Принципы создания методов

1. **Основаны на SoTA** — каждый метод синтезирован из interpretations
2. **SPF-совместимы** — YAML frontmatter, типизированные связи, статусы SoTA
3. **Практичны** — пороги, дозы, алгоритмы действий
4. **Актуальны** — включают современные подходы (ML, метаболомика)

---

## Связь с другими разделами

```
SoTA (06-sota/)
      ↓
Interpretations (02-domain-entities/03-interpretations/)
      ↓
Methods (03-methods/) ← Вы здесь
      ↓
Work Products (04-work-products/)
      ↓
Clinical Protocols (практическое применение)
```

---

## Шаблон для новых методов

См. `SPF/pack-template/03-methods/_method-card-template.md`

---

*Создан: 2026-03-28*  
*Обновлено: 2026-05-18 (WP-83 Methods PACK)*
