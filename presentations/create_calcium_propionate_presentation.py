#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Генерация PDF-презентации "Пропионат кальция у дойных коров в transition period".
Источники: CS.SOTA.333–340 (PACK-cattle-science).
"""
import os
import base64
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from weasyprint import HTML, CSS

BASE = Path('/home/asus/IWE/PACK-cattle-science')
OUT_DIR = BASE / 'presentations'
OUT_DIR.mkdir(parents=True, exist_ok=True)
CHART_DIR = OUT_DIR / 'charts'
CHART_DIR.mkdir(parents=True, exist_ok=True)
MEDIA_DIR = BASE / 'pack/cattle-science/06-sota/health/CS.SOTA.336-media'

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12


def save_chart(name, fig):
    path = CHART_DIR / name
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    return path


def file_url(path: Path) -> str:
    return path.resolve().as_uri()


def chart_fcm_protein():
    """Martins 2019: FCM и белок в ранней лактации."""
    treatments = ['CP\n(200 г/сут)', 'CA\n(300 г/сут)', 'CG\n(контроль)', 'CSFA\n(300 г/сут)']
    fcm = [21.13, 18.31, 15.67, 15.26]
    protein = [3.12, 2.98, 3.14, 2.99]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))
    bars1 = ax1.bar(treatments, fcm, color=['#2E7D32', '#1565C0', '#757575', '#C62828'])
    ax1.set_ylabel('FCM, л/сут')
    ax1.set_title('Корректированный удой (3,5 % жира)')
    ax1.set_ylim(0, 25)
    for bar, val in zip(bars1, fcm):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.4,
                 f'{val:.2f}', ha='center', va='bottom', fontsize=10)

    bars2 = ax2.bar(treatments, protein, color=['#2E7D32', '#1565C0', '#757575', '#C62828'])
    ax2.set_ylabel('Белок, г/л')
    ax2.set_title('Содержание молочного белка')
    ax2.set_ylim(0, 3.6)
    for bar, val in zip(bars2, protein):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05,
                 f'{val:.2f}', ha='center', va='bottom', fontsize=10)

    fig.suptitle('Martins et al. 2019 — ранняя лактация', fontsize=13, y=1.02)
    return save_chart('martins_2019_fcm_protein.png', fig)


def chart_milk_fever():
    """Goff 1996 Jersey + Pehrson 1998 сравнение."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

    # Goff 1996 Jersey
    labels1 = ['Контроль', 'Ca-пропионат']
    vals1 = [50, 29]
    bars1 = ax1.bar(labels1, vals1, color=['#757575', '#2E7D32'])
    ax1.set_ylabel('Заболеваемость, %')
    ax1.set_title('Goff et al. 1996 — стадо Jersey')
    ax1.set_ylim(0, 60)
    for bar, val in zip(bars1, vals1):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{val}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

    # Pehrson 1998
    labels2 = ['Без профилактики\n(исторический контроль)', 'Ca-пропионат', 'CaCl₂']
    vals2 = [36.0, 25.3, 23.2]
    bars2 = ax2.bar(labels2, vals2, color=['#C62828', '#2E7D32', '#1565C0'])
    ax2.set_ylabel('Заболеваемость, %')
    ax2.set_title('Pehrson et al. 1998 — коровы с анамнезом')
    ax2.set_ylim(0, 45)
    for bar, val in zip(bars2, vals2):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.7,
                 f'{val}%', ha='center', va='bottom', fontsize=11, fontweight='bold')

    fig.suptitle('Профилактика молочной лихорадки', fontsize=13, y=1.02)
    return save_chart('milk_fever_prevention.png', fig)


def chart_liu_trends():
    """Liu 2010: направление дозозависимых эффектов (схематично)."""
    doses = [0, 100, 200, 300]
    # Нормированные относительные индексы: условные, отражают направление тренда
    glucose = [50, 60, 72, 85]
    insulin = [50, 58, 70, 82]
    nefa = [100, 82, 68, 55]
    bhba = [100, 84, 70, 58]

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(doses, glucose, marker='o', label='Глюкоза плазмы', linewidth=2)
    ax.plot(doses, insulin, marker='s', label='Инсулин сыворотки', linewidth=2)
    ax.plot(doses, nefa, marker='^', label='NEFA', linewidth=2)
    ax.plot(doses, bhba, marker='v', label='BHBA', linewidth=2)
    ax.set_xlabel('Доза Ca-пропионата, г/сут')
    ax.set_ylabel('Условный относительный индекс')
    ax.set_title('Liu et al. 2010 — дозозависимые метаболические сдвиги\n(направление эффектов, p < 0,01)')
    ax.legend(loc='best')
    ax.set_xticks(doses)
    ax.grid(True, alpha=0.3)
    ax.text(0.02, 0.02, '*условные индексы, иллюстрирующие линейный тренд из abstract',
            transform=ax.transAxes, fontsize=9, color='#555')
    return save_chart('liu_2010_trends.png', fig)


# Генерируем графики
chart_fcm_protein()
chart_milk_fever()
chart_liu_trends()

html = f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<title>Пропионат кальция у дойных коров</title>
<style>
@page {{
  size: 320mm 180mm;
  margin: 0;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: "DejaVu Sans", sans-serif;
  color: #222;
  background: #fff;
}}
.slide {{
  width: 320mm;
  height: 180mm;
  padding: 14mm 18mm;
  page-break-after: always;
  position: relative;
  overflow: hidden;
}}
.slide:last-child {{
  page-break-after: auto;
}}
.title-slide {{
  background: linear-gradient(135deg, #1B5E20 0%, #2E7D32 60%, #66BB6A 100%);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}}
.title-slide h1 {{ font-size: 42px; margin: 0 0 12mm 0; }}
.title-slide h2 {{ font-size: 24px; font-weight: normal; margin: 0 0 8mm 0; }}
.title-slide p {{ font-size: 16px; opacity: 0.9; }}
h1.slide-title {{
  font-size: 28px;
  color: #1B5E20;
  border-bottom: 3px solid #66BB6A;
  padding-bottom: 4mm;
  margin: 0 0 8mm 0;
}}
h2 {{ font-size: 20px; color: #1565C0; margin: 6mm 0 3mm 0; }}
p, li {{ font-size: 15px; line-height: 1.5; }}
ul {{ margin: 0; padding-left: 6mm; }}
li {{ margin-bottom: 2.5mm; }}
.two-col {{
  display: flex;
  gap: 10mm;
}}
.two-col > div {{
  flex: 1;
}}
.fig {{
  max-width: 100%;
  max-height: 115mm;
  display: block;
  margin: 4mm auto 0 auto;
}}
.small {{
  font-size: 11px;
  color: #555;
  margin-top: 2mm;
}}
table {{
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
  margin-top: 4mm;
}}
th, td {{
  border: 1px solid #999;
  padding: 3mm 4mm;
  text-align: left;
}}
th {{
  background: #E8F5E9;
  color: #1B5E20;
}}
.highlight {{
  background: #FFF9C4;
  padding: 1mm 2mm;
  border-radius: 2mm;
}}
.footer {{
  position: absolute;
  bottom: 5mm;
  left: 18mm;
  right: 18mm;
  font-size: 10px;
  color: #777;
  border-top: 1px solid #ddd;
  padding-top: 2mm;
}}
.number {{
  display: inline-block;
  background: #1B5E20;
  color: white;
  width: 8mm;
  height: 8mm;
  line-height: 8mm;
  border-radius: 50%;
  text-align: center;
  margin-right: 3mm;
  font-size: 13px;
}}
</style>
</head>
<body>

<div class="slide title-slide">
  <h1>Пропионат кальция у дойных коров</h1>
  <h2>Механизмы, дозировки и практическое применение в transition period</h2>
  <p>На основе PACK-cattle-science: CS.SOTA.333–340</p>
  <p style="margin-top: 12mm; font-size: 14px;">Июнь 2026</p>
</div>

<div class="slide">
  <h1 class="slide-title">Почему transition period — критическая точка?</h1>
  <div class="two-col">
    <div>
      <ul>
        <li><b>Отрицательный энергетический баланс (ОЭБ):</b> DMI не покрывает затраты на молоко.</li>
        <li><b>Мобилизация жира:</b> рост NEFA и BHBA → риск кетоза и жировой дистрофии печени.</li>
        <li><b>Гипокальцемия:</b> клиническая молочная лихорадка 3–10 %, субклиническая — 25–50 % многоплодных коров.</li>
        <li><b>Последствия:</b> снижение фертильности, мастит, метрит, смещение сычуга.</li>
      </ul>
    </div>
    <div>
      <h2>Роль пропионата кальция</h2>
      <p>Двойной эффект:</p>
      <ul>
        <li><span class="highlight">Ca²⁺</span> — поддержка кальциевого гомеостаза.</li>
        <li><span class="highlight">Пропионат</span> — основной глюконеогенный прекурсор в рубце.</li>
      </ul>
      <p class="small">Источники: CS.SOTA.335 (Zhang 2020), CS.SOTA.337 (Kara 2013).</p>
    </div>
  </div>
  <div class="footer">PACK-cattle-science / CS.SOTA.333–340</div>
</div>

<div class="slide">
  <h1 class="slide-title">Что такое пропионат кальция?</h1>
  <div class="two-col">
    <div>
      <h2>Химия и метаболизм</h2>
      <ul>
        <li>Формула: (CH₃CH₂COO)₂Ca.</li>
        <li>Гидролиз в рубце → Ca²⁺ + пропионат.</li>
        <li>Пропионат — основной субстрат гепатического глюконеогенеза (до 60 % синтеза глюкозы).</li>
        <li>Ca²⁺ повышает ионизированный Ca в крови, снижая риск гипокальцемии.</li>
      </ul>
      <p class="small">Источники: CS.SOTA.335, CS.SOTA.336, CS.SOTA.337.</p>
    </div>
    <div>
      <h2>Преимущества формы</h2>
      <ul>
        <li>Нейтральный вкус, меньше раздражает слизистую, чем CaCl₂.</li>
        <li>Более длительное повышение Ca по сравнению с CaCl₂.</li>
        <li>Дополнительный глюконеогенный эффект.</li>
        <li>Антигрибковые свойства (силос, TMR).</li>
      </ul>
    </div>
  </div>
  <div class="footer">PACK-cattle-science / CS.SOTA.333–340</div>
</div>

<div class="slide">
  <h1 class="slide-title">Механизм 1: глюконеогенез и энергетический статус</h1>
  <div class="two-col">
    <div>
      <h2>Liu et al. 2010</h2>
      <ul>
        <li>32 многоплодные Holstein, 1–63 DIM.</li>
        <li>Дозы: 0, 100, 200, 300 г Ca-пропионата/сут.</li>
        <li>Глюкоза и инсулин ↑ линейно (p &lt; 0,01).</li>
        <li>NEFA, BHBA и кетоны мочи ↓ линейно (p &lt; 0,01).</li>
        <li>Удой и состав молока — без изменений.</li>
      </ul>
      <p class="small">*График отражает направление линейных трендов, а не абсолютные значения (abstract-only).</p>
    </div>
    <div>
      <img class="fig" src="{file_url(CHART_DIR / 'liu_2010_trends.png')}" alt="Liu 2010 trends">
    </div>
  </div>
  <div class="footer">Источник: CS.SOTA.340</div>
</div>

<div class="slide">
  <h1 class="slide-title">Механизм 2: кальций и профилактика молочной лихорадки</h1>
  <img class="fig" src="{file_url(CHART_DIR / 'milk_fever_prevention.png')}" alt="Milk fever prevention">
  <p class="small" style="text-align:center;">
    Слева: Goff et al. 1996, стадо Jersey с высокой базовой заболеваемостью (abstract-only).<br>
    Справа: Pehrson et al. 1998, коровы с молочной лихорадкой в предыдущую лактацию (abstract-only).<br>
    Peralta et al. 2011: смесь Ca-пропионат + пропиленгликоль повышала сывороточный Ca, но не влияла на NEFA.
  </p>
  <div class="footer">Источники: CS.SOTA.338, CS.SOTA.339, CS.SOTA.334</div>
</div>

<div class="slide">
  <h1 class="slide-title">Влияние на рубцовую микробиоту (Zhang et al. 2022)</h1>
  <div class="two-col">
    <div>
      <img class="fig" src="{file_url(MEDIA_DIR / 'figure-1-alpha-diversity.png')}" alt="Alpha diversity">
      <p class="small" style="text-align:center;">Рис. 1 — Альфа-разнообразие рубцовой микробиоты</p>
    </div>
    <div>
      <img class="fig" src="{file_url(MEDIA_DIR / 'figure-2-bacterial-community-composition.png')}" alt="Community composition">
      <p class="small" style="text-align:center;">Рис. 2 — Состав бактериального сообщества</p>
    </div>
  </div>
  <ul>
    <li>Ca-пропионат 200–500 г/сут не изменил основное брожение и альфа-разнообразие.</li>
    <li>Обнаружены дозозависимые сдвиги на уровне отдельных таксонов (Bacteroidetes, Firmicutes).</li>
  </ul>
  <div class="footer">Источник: CS.SOTA.336</div>
</div>

<div class="slide">
  <h1 class="slide-title">Дозировки и способы введения</h1>
  <table>
    <tr>
      <th>Цель</th>
      <th>Способ введения</th>
      <th>Доза</th>
      <th>Тайминг</th>
      <th>Источник</th>
    </tr>
    <tr>
      <td>Поддержка энергии в ранней лактации</td>
      <td>В корм (TMR/концентрат)</td>
      <td>150–200 г/сут</td>
      <td>1–63 DIM</td>
      <td>CS.SOTA.333, CS.SOTA.340</td>
    </tr>
    <tr>
      <td>Профилактика молочной лихорадки</td>
      <td>Пероральная паста</td>
      <td>74–111 г Ca (2–3 тубы по 37 г Ca)</td>
      <td>В отёл + через 12 ч</td>
      <td>CS.SOTA.338</td>
    </tr>
    <tr>
      <td>Профилактика молочной лихорадки</td>
      <td>Болюсы</td>
      <td>до 6 × 20 г Ca как Ca-пропионат</td>
      <td>−36 ч … +24 ч от отёла</td>
      <td>CS.SOTA.339</td>
    </tr>
    <tr>
      <td>Однократная энерго-Ca поддержка</td>
      <td>Drench (Ca-пропионат + пропиленгликоль)</td>
      <td>375 г Ca-пропионат + 400 г PG</td>
      <td>12 ч послеродово</td>
      <td>CS.SOTA.334</td>
    </tr>
    <tr>
      <td>Консервант силоса/TMR</td>
      <td>В силос или TMR</td>
      <td>~10 г/кг свежей массы силоса</td>
      <td>При заготовке/раздаче</td>
      <td>CS.SOTA.335</td>
    </tr>
  </table>
  <div class="footer">Источники: CS.SOTA.333–340</div>
</div>

<div class="slide">
  <h1 class="slide-title">Эффекты на продуктивность (Martins et al. 2019)</h1>
  <img class="fig" src="{file_url(CHART_DIR / 'martins_2019_fcm_protein.png')}" alt="Martins 2019">
  <p class="small" style="text-align:center;">
    Ранняя лактация. CP = Ca-пропионат 200 г/сут; CA = Ca-ацетат 300 г; CG = контроль; CSFA = кальциевые соли жирных кислот.<br>
    CP повысил FCM и белок; CSFA снизила FCM.
  </p>
  <div class="footer">Источник: CS.SOTA.333</div>
</div>

<div class="slide">
  <h1 class="slide-title">Практический алгоритм внедрения</h1>
  <div style="display:flex; flex-direction:column; gap:4mm;">
    <div><span class="number">1</span><b>Аудит стада.</b> Определить частоту субклинической гипокальцемии и кетоза. Интервенция оправдана при риске &gt;25 %.</div>
    <div><span class="number">2</span><b>Выбор группы риска.</b> Многоплодные коровы, Jersey, коровы с историей молочной лихорадки, высокопродуктивные раннелактирующие.</div>
    <div><span class="number">3</span><b>Выбор схемы.</b> Ранняя лактация — 150–200 г/сут в корм; перипартум — паста/болюс Ca-пропионата.</div>
    <div><span class="number">4</span><b>Мониторинг.</b> DMI, удой, жирность, Ca сыворотки, NEFA/BHBA через 7–14 дней.</div>
    <div><span class="number">5</span><b>Корректировка.</b> При снижении DMI &gt;5–7 % снизить дозу; при недостаточном эффекте добавить анионную диету или CaCl₂-болюсы.</div>
  </div>
  <div class="footer">На основе CS.SOTA.333–340</div>
</div>

<div class="slide">
  <h1 class="slide-title">Риски и ограничения</h1>
  <div class="two-col">
    <div>
      <h2>Риски</h2>
      <ul>
        <li><b>Гипофагия:</b> высокие дозы пропионата могут снижать DMI.</li>
        <li><b>Породные различия:</b> Jersey более чувствительны к молочной лихорадке, чем Holstein.</li>
        <li><b>Не заменяет энергию рациона:</b> при глубоком ОЭБ требуется коррекция рациона.</li>
        <li><b>Острая молочная лихорадка:</b> паста — профилактика, а не лечение.</li>
      </ul>
    </div>
    <div>
      <h2>Ограничения evidence</h2>
      <ul>
        <li>Goff 1996, Pehrson 1998, Liu 2010 — only PubMed abstract (CS.SOTA.338–340).</li>
        <li>Малая выборка в некоторых исследованиях (Martins n=8, Liu n=32).</li>
        <li>Различаются дизайны: корм, drench, болюс, паста — эффект зависит от формы.</li>
      </ul>
    </div>
  </div>
  <div class="footer">PACK-cattle-science / CS.SOTA.333–340</div>
</div>

<div class="slide">
  <h1 class="slide-title">Выводы</h1>
  <div style="font-size: 16px; line-height: 1.6;">
    <ul>
      <li><b>Двойной механизм:</b> Ca-пропионат одновременно поддерживает Ca²⁺ и глюконеогенез.</li>
      <li><b>Ранняя лактация:</b> 150–200 г/сут улучшает энергетический статус (NEFA↓, BHBA↓, глюкоза↑), при этом удой может не меняться.</li>
      <li><b>Продуктивность:</b> 200 г/сут CP повышает FCM, белок, лактозу и жир в ранней лактации (Martins 2019).</li>
      <li><b>Профилактика гипокальцемии:</b> пероральные пасты/болюсы эффективны, особенно в стадах с высоким риском.</li>
      <li><b>Рубцовая микробиота:</b> дозы 200–500 г/сут не меняют общее брожение, но вызывают таксономические сдвиги.</li>
      <li><b>Ключевое правило:</b> мониторить DMI и корректировать дозу — пропионат не заменяет сбалансированный рацион.</li>
    </ul>
  </div>
  <div class="footer">PACK-cattle-science / CS.SOTA.333–340</div>
</div>

</body>
</html>
"""

html_path = OUT_DIR / 'calcium_propionate_presentation.html'
html_path.write_text(html, encoding='utf-8')

pdf_path = OUT_DIR / 'calcium_propionate_presentation.pdf'
HTML(filename=str(html_path)).write_pdf(str(pdf_path))

print(f"PDF создан: {pdf_path}")
print(f"HTML сохранён: {html_path}")
