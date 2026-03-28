# Статьи для добавления в SoTA

**Дата:** 2026-03-28  
**Следующий ID:** CS.SOTA.069

---

## Приоритет 1: Критически важные

### 1. "How Much are You Losing from Extra Days Open"
- **Статус:** Не в SoTA
- **Тема:** Экономика открытого периода
- **Почему важно:** Экономическая оценка ключевого показателя
- **Рекомендуемый ID:** CS.SOTA.069
- **Область:** economics
- **Приоритет:** P1

---

## Приоритет 2: Важные (дополнения к существующим)

### 2. "Effects of rate and amount of propionic acid infused into the rumen..."
- **Статус:** Возможно связано с CS.SOTA.015 (Schuler 2013)
- **Тема:** Пропионат и поведение при кормлении
- **Действие:** Проверить — если новое, добавить как CS.SOTA.070
- **Область:** feeding
- **Приоритет:** P2

### 3. "Highly fermentable starch at different diet starch concentrations..."
- **Статус:** Возможно связано с CS.SOTA.016 (Albornoz 2018)
- **Тема:** Крахмал в постпартум
- **Действие:** Проверить — если новое, добавить как CS.SOTA.071
- **Область:** feeding
- **Приоритет:** P2

### 4. "A randomized controlled trial to evaluate propylene glycol alone" (W13)
- **Статус:** Возможно связано с CS.SOTA.060 (Capel 2021)
- **Тема:** PG ± дексроза
- **Действие:** Проверить — если новое исследование, добавить
- **Область:** health
- **Приоритет:** P2

### 5. "Effect of propylene glycol on adipose tissue mobilization" (W13)
- **Статус:** Возможно связано с CS.SOTA.061 (Bjerre-Harpøth 2015)
- **Тема:** PG и жировая ткань
- **Действие:** Проверить — если новое, добавить
- **Область:** health
- **Приоритет:** P2

---

## Проверить содержимое

Для точной идентификации нужно извлечь метаданные:

```bash
# Приоритет 1 — проверить первым
cd process/ingestion/new-articles
pdftotext "How Much are You Losing from Extra Days Open.pdf" - | head -100

# Приоритет 2 — проверить авторов и год
pdftotext "Effects of rate and amount of propionic acid..." - | head -50
pdftotext "Highly fermentable starch..." - | head -50
pdftotext "W13/A randomized controlled trial..." - | head -50
pdftotext "W13/Effect of propylene glycol..." - | head -50
```

---

## Резюме

| Приоритет | Количество | Действие |
|-----------|------------|----------|
| P1 | 1 | Добавить как CS.SOTA.069 |
| P2 | 4 | Проверить и добавить при необходимости |
| **Итого** | **5** | **На рассмотрении** |

---

*Список создан на основе анализа 79 файлов в new-articles*  
*~74 файла уже в SoTA, 5 требуют проверки*
