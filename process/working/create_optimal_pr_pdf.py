# -*- coding: utf-8 -*-
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT

def create_optimal_pr_pdf():
    output_path = r"D:\OneDrive\Рабочие файлы\Рабочий стол\Экзокортекс\PACK-cattle-science\process\working\Optimal_21d_PR_Guide.pdf"
    font_dir = r"D:\OneDrive\Рабочие файлы\Рабочий стол\Экзокортекс\PACK-cattle-science\process\working\fonts"
    
    # Register DejaVu fonts
    pdfmetrics.registerFont(TTFont('DejaVu', f'{font_dir}\\DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuBold', f'{font_dir}\\DejaVuSans-Bold.ttf'))
    
    # Override Helvetica to use DejaVu
    pdfmetrics.registerFont(TTFont('Helvetica', f'{font_dir}\\DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('Helvetica-Bold', f'{font_dir}\\DejaVuSans-Bold.ttf'))
    
    font_name = 'DejaVu'
    font_name_bold = 'DejaVuBold'
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    styles = getSampleStyleSheet()
    
    # Large readable fonts
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=22,
        textColor=colors.HexColor('#1a472a'),
        spaceAfter=8,
        alignment=TA_CENTER,
        fontName=font_name_bold
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=12,
        textColor=colors.HexColor('#555555'),
        alignment=TA_CENTER,
        spaceAfter=20,
        fontName=font_name
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#2c5f2d'),
        spaceAfter=12,
        spaceBefore=18,
        fontName=font_name_bold
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=12,
        alignment=TA_LEFT,
        spaceAfter=8,
        fontName=font_name,
        leading=16
    )
    
    note_style = ParagraphStyle(
        'NoteStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#1a472a'),
        backColor=colors.HexColor('#e8f5e9'),
        borderColor=colors.HexColor('#2c5f2d'),
        borderWidth=1,
        borderPadding=10,
        leftIndent=0,
        rightIndent=0,
        spaceBefore=12,
        spaceAfter=12,
        fontName=font_name
    )
    
    story = []
    
    # Title
    story.append(Paragraph("Оптимальный 21-дневный коэффициент оплодотворения (21-d PR)", title_style))
    story.append(Paragraph("Целевые показатели репродуктивной эффективности молочного стада", subtitle_style))
    
    # Table 1
    story.append(Paragraph("Оптимальный 21-d PR по контекстам", heading2_style))
    
    data1 = [
        ['Контекст', 'Оптимальный 21-d PR', 'Обоснование'],
        ['Минимально приемлемый', '>=20%', 'Ниже — дефицит телок (Lauber 2025)'],
        ['Целевой (средний)', '25-30%', 'Средний показатель по отрасли'],
        ['Высокий (топ 25%)', '30-35%', 'Лучшие хозяйства'],
        ['Отличный (топ 10%)', '>=35%', 'Максимальная эффективность']
    ]
    
    t1 = Table(data1, colWidths=[6*cm, 4*cm, 6.5*cm])
    t1.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTNAME', (0, 0), (-1, 0), font_name_bold),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5f2d')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f5f5f5')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#e8f5e9')])
    ]))
    story.append(t1)
    
    # Economics table
    story.append(Paragraph("Экономика разных уровней 21-d PR", heading2_style))
    
    data2 = [
        ['21-d PR', 'Статус', 'Доходность', 'Оптимальный IEP'],
        ['20%', 'Низкий', 'Базовый ($0)', '170 дней'],
        ['25%', 'Ниже среднего', '+$10-30/кор/год', '140 дней'],
        ['30%', 'Средний', '+$30-60/кор/год', '110 дней'],
        ['35%', 'Выше среднего', '+$60-90/кор/год', '95 дней'],
        ['40%', 'Высокий', '+$90-120/кор/год', '80 дней']
    ]
    
    t2 = Table(data2, colWidths=[3*cm, 4*cm, 4.5*cm, 3.5*cm])
    t2.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTNAME', (0, 0), (-1, 0), font_name_bold),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1a472a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [
            colors.HexColor('#ffebee'),
            colors.HexColor('#fff3e0'),
            colors.HexColor('#fffde7'),
            colors.HexColor('#e8f5e9'),
            colors.HexColor('#c8e6c9')
        ])
    ]))
    story.append(t2)
    
    # Key finding box
    story.append(Paragraph("<b>💡 Ключевой вывод:</b> Каждый +1% к 21-d PR приносит дополнительно <b>$2-7/кор/год</b> прибыли (Lauber 2025)", note_style))
    
    # New page
    story.append(Spacer(1, 0.5*cm))
    
    # Recommendations
    story.append(Paragraph("Практические рекомендации по уровням", heading2_style))
    
    story.append(Paragraph("<b>🔴 Критический: 21-d PR < 20%</b><br/>"
                          "Недостаток телок для замены → срочно улучшать репродукцию или выживаемость телок.<br/>"
                          "<b>IEP: 170+ дней</b> (максимальный период)", normal_style))
    
    story.append(Paragraph("<b>🟠 Низкий: 21-d PR 20-25%</b><br/>"
                          "IEP: <b>140-170 дней</b> (conventional семя). Приоритет — рост до 30%+.<br/>"
                          "<b>Не использовать sexed+beef</b> — риск дефицита replacements", normal_style))
    
    story.append(Paragraph("<b>🟡 Средний: 21-d PR 25-35%</b><br/>"
                          "IEP: <b>110-140 дней</b>. Можно переходить на sexed+beef при <b>HSR > 85%</b>", normal_style))
    
    story.append(Paragraph("<b>🟢 Высокий: 21-d PR ≥ 35%</b><br/>"
                          "IEP: <b>80-110 дней</b> (короткий период!). <b>Sexed+beef оптимален</b> (+$51/кор/год).<br/>"
                          "Стратегия: максимизировать доход от молока, быстрая замена", normal_style))
    
    # Formula
    story.append(Paragraph("Формула расчета", heading2_style))
    
    data3 = [
        ['Компонент', 'Описание', 'Типичное значение'],
        ['Service Rate', '% коров, осемененных за 21 день', '60-80%'],
        ['P/AI (Conception)', '% оплодотворения на осеменение', '35-45%'],
        ['21-d PR', 'Service Rate × P/AI × 100', '20-40%']
    ]
    
    t3 = Table(data3, colWidths=[4*cm, 8*cm, 3*cm])
    t3.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), font_name),
        ('FONTNAME', (0, 0), (-1, 0), font_name_bold),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4a7c59')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 10),
        ('TOPPADDING', (0, 1), (-1, -1), 10),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#f0f7f0')),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#e8f5e9')])
    ]))
    story.append(t3)
    
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("<b>Пример:</b> Service Rate = 70%, P/AI = 40% → 21-d PR = 0.70 × 0.40 × 100 = <b>28%</b>", normal_style))
    
    # Footer
    story.append(Spacer(1, 0.8*cm))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.grey,
        alignment=TA_CENTER,
        fontName=font_name
    )
    story.append(Paragraph("<b>Источники:</b> Lauber et al. (2025) — CS.SOTA.001 | Giordano et al. (2012) — CS.SOTA.003<br/>"
                          "PACK-cattle-science | github.com/StanisSerg/PACK-cattle-science | 2026", footer_style))
    
    doc.build(story)
    print(f"PDF создан: {output_path}")
    return output_path

if __name__ == "__main__":
    create_optimal_pr_pdf()
