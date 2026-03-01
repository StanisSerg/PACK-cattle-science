---
marp: true
theme: default
class:
  - lead
backgroundColor: #fff
style: |
  @page {
    size: A4 portrait;
    margin: 20mm;
  }
  section {
    font-family: "Segoe UI", "Arial", sans-serif;
    font-size: 12px;
    padding: 20px 30px;
    margin: 0;
    line-height: 1.5;
  }
  h1 {
    color: #1a472a;
    font-size: 20px;
    text-align: center;
    margin: 0 0 8px 0;
  }
  h2 {
    color: #2c5f2d;
    font-size: 14px;
    margin: 18px 0 10px 0;
    border-bottom: 2px solid #2c5f2d;
    padding-bottom: 5px;
  }
  table {
    font-size: 11px;
    width: 100%;
    margin: 10px 0;
    border-collapse: collapse;
  }
  th {
    background-color: #2c5f2d;
    color: white;
    padding: 8px 10px;
    text-align: left;
    font-weight: 600;
  }
  td {
    padding: 6px 10px;
    border-bottom: 1px solid #ddd;
  }
  tr:nth-child(even) {
    background-color: #f5f5f5;
  }
  p {
    margin: 8px 0;
  }
  .subtitle {
    text-align: center;
    font-size: 11px;
    color: #555;
    margin-bottom: 18px;
  }
  .note {
    font-size: 11px;
    color: #1a472a;
    background: #e8f5e9;
    padding: 10px 15px;
    border-radius: 5px;
    margin: 15px 0;
    border-left: 4px solid #2c5f2d;
  }
  .footer {
    font-size: 9px;
    color: #666;
    text-align: center;
    margin-top: 20px;
    padding-top: 10px;
    border-top: 1px solid #ddd;
  }
  .rec-box {
    margin: 10px 0;
    padding: 10px 12px;
    background: #f8f8f8;
    border-radius: 5px;
    border-left: 4px solid #ccc;
  }
  .rec-critical { border-left-color: #d32f2f; }
  .rec-low { border-left-color: #f57c00; }
  .rec-medium { border-left-color: #fbc02d; }
  .rec-high { border-left-color: #388e3c; }
---

# Оптимальный 21-дневный коэффициент оплодотворения (21-d PR)

<div class="subtitle">Целевые показатели репродуктивной эффективности молочного стада</div>

## Оптимальный 21-d PR по контекстам

| Контекст | Оптимальный 21-d PR | Обоснование |
|:---------|:-------------------:|:------------|
| Минимально приемлемый | **≥20%** | Ниже — дефицит телок (Lauber 2025) |
| Целевой (средний) | **25-30%** | Средний показатель по отрасли |
| Высокий (топ 25%) | **30-35%** | Лучшие хозяйства |
| Отличный (топ 10%) | **≥35%** | Максимальная эффективность |

## Экономика разных уровней

| 21-d PR | Статус | Доходность | Оптимальный IEP |
|:-------:|:-------|:-----------|:----------------|
| 20% | Низкий | Базовый ($0) | 170 дней |
| 25% | Ниже среднего | +$10-30/кор/год | 140 дней |
| 30% | Средний | +$30-60/кор/год | 110 дней |
| 35% | Выше среднего | +$60-90/кор/год | 95 дней |
| 40% | Высокий | +$90-120/кор/год | 80 дней |

<div class="note">
<b>💡 Ключевой вывод:</b> Каждый +1% к 21-d PR приносит дополнительно <b>$2-7/кор/год</b> прибыли (Lauber 2025)
</div>

---

## Практические рекомендации по уровням

<div class="rec-box rec-critical">
<b>🔴 Критический: 21-d PR < 20%</b><br>
Недостаток телок для замены → срочно улучшать репродукцию или выживаемость телок<br>
<b>IEP: 170+ дней</b> (максимальный период)
</div>

<div class="rec-box rec-low">
<b>🟠 Низкий: 21-d PR 20-25%</b><br>
IEP: <b>140-170 дней</b> (conventional семя). Приоритет — рост до 30%+.<br>
<b>Не использовать sexed+beef</b> — риск дефицита replacements
</div>

<div class="rec-box rec-medium">
<b>🟡 Средний: 21-d PR 25-35%</b><br>
IEP: <b>110-140 дней</b>. Можно переходить на sexed+beef при <b>HSR > 85%</b>
</div>

<div class="rec-box rec-high">
<b>🟢 Высокий: 21-d PR ≥ 35%</b><br>
IEP: <b>80-110 дней</b> (короткий период!). <b>Sexed+beef оптимален</b> (+$51/кор/год)<br>
Стратегия: максимизировать доход от молока, быстрая замена
</div>

## Формула расчёта

| Компонент | Описание | Типичное значение |
|:----------|:---------|:------------------|
| **Service Rate** | % коров, осеменённых за 21 день | 60-80% |
| **P/AI** | % оплодотворения на осеменение | 35-45% |
| **21-d PR** | Service Rate × P/AI × 100 | **20-40%** |

<p><b>Пример:</b> Service Rate = 70%, P/AI = 40% → 21-d PR = 0.70 × 0.40 × 100 = <b>28%</b></p>

<div class="footer">
<b>Источники:</b> Lauber et al. (2025) — CS.SOTA.001 | Giordano et al. (2012) — CS.SOTA.003<br>
PACK-cattle-science | github.com/StanisSerg/PACK-cattle-science | 2026
</div>
