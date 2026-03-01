# -*- coding: utf-8 -*-
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def create_test_pdf():
    output_path = r"D:\OneDrive\Рабочие файлы\Рабочий стол\Экзокортекс\PACK-cattle-science\process\working\test_russian.pdf"
    font_dir = r"D:\OneDrive\Рабочие файлы\Рабочий стол\Экзокортекс\PACK-cattle-science\process\working\fonts"
    
    # Register fonts
    pdfmetrics.registerFont(TTFont('DejaVu', f'{font_dir}\\DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuBold', f'{font_dir}\\DejaVuSans-Bold.ttf'))
    
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    
    # Title
    c.setFont('DejaVuBold', 16)
    c.drawString(50, height - 50, "Тест русского текста в PDF")
    
    # Regular text
    c.setFont('DejaVu', 12)
    c.drawString(50, height - 100, "Это обычный текст на русском языке.")
    c.drawString(50, height - 130, "Проверка: абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
    c.drawString(50, height - 160, "Заглавные: АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")
    
    # Table-like content
    c.setFont('DejaVuBold', 11)
    c.drawString(50, height - 220, "Таблица:")
    
    c.setFont('DejaVu', 10)
    y = height - 250
    for row in [
        "Контекст          | Значение  | Описание",
        "Минимальный       | >=20%     | Ниже — дефицит",
        "Целевой           | 25-30%    | Средний показатель",
        "Высокий           | 30-35%    | Лучшие хозяйства"
    ]:
        c.drawString(50, y, row)
        y -= 25
    
    c.save()
    print(f"Test PDF created: {output_path}")

create_test_pdf()
