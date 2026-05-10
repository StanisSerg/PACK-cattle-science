#!/usr/bin/env python3
"""
extract-media-from-pdf.py — извлечение PNG-crops из PDF для SoTA Book Chapter.

Зависимости:
    pip install pymupdf

Использование:

    1. Анализ PDF (показать изображения и блоки на каждой странице):
       python extract-media-from-pdf.py --pdf "Глава 5.pdf" --inspect

    2. Создать crops вручную (рекомендуемый режим):
       python extract-media-from-pdf.py \\
           --pdf "Глава 5.pdf" \\
           --sota-id CS.SOTA.297 \\
           --output-dir "../06-sota/feeding/" \\
           --crop "page:2,rect:0,75,612.6,265,name:figure-5-1-carbohydrate-fractions" \\
           --crop "page:7,rect:0,295,612.6,485,name:table-5-1-recommended-ndf-starch"

    3. Авто-экстракция изображений (все картинки из PDF):
       python extract-media-from-pdf.py \\
           --pdf "Глава 5.pdf" \\
           --sota-id CS.SOTA.297 \\
           --output-dir "../06-sota/feeding/" \\
           --auto-images

    4. Генерация превью всех страниц (для визуального выбора зон):
       python extract-media-from-pdf.py --pdf "Глава 5.pdf" --preview --preview-dir ./preview

Параметры crop:
    page:N       — номер страницы в PDF (1-based)
    rect:x0,y0,x1,y1 — bounding box в координатах PDF-страницы (points)
    name:STRING  — имя выходного файла (без расширения)

    Альтернатива rect — relative позиционирование:
    y:Y0-Y1      — обрезать по вертикали (x берётся полная ширина страницы)

Нотация имени файла:
    figure-N-DESC.png   — для рисунков
    table-N-DESC.png    — для таблиц
    equation-N-DESC.png — для уравнений (редко)

Стандарт DPI: 200 (достаточно для чтения, ~150–300 KB на файл).
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: PyMuPDF не установлен. Установите: pip install pymupdf")
    sys.exit(1)


def inspect_pdf(pdf_path: str):
    """Анализ PDF: показать изображения, drawings и текстовые блоки на каждой странице."""
    doc = fitz.open(pdf_path)
    print(f"\n📄 PDF: {pdf_path}")
    print(f"   Страниц: {len(doc)}")
    print(f"   Размер страницы (page 1): {doc[0].rect}\n")

    for i in range(len(doc)):
        page = doc[i]
        page_num = i + 1
        images = page.get_images()
        drawings = page.get_drawings()
        blocks = page.get_text("blocks")

        has_content = bool(images) or len(drawings) > 50 or any(
            b[4].strip().startswith(("TABLE", "FIGURE", "Equation")) for b in blocks
        )
        if not has_content:
            continue

        print(f"=== Page {page_num} ===")
        print(f"   Images: {len(images)}")
        for img in images:
            rects = page.get_image_rects(img[0])
            for r in rects:
                print(f"      Image rect: ({r.x0:.1f}, {r.y0:.1f}, {r.x1:.1f}, {r.y1:.1f})")

        if len(drawings) > 50:
            print(f"   Drawings (vector lines): {len(drawings)} — возможно таблица или диаграмма")

        for b in blocks:
            text = b[4].strip().replace("\n", " ")[:80]
            if text.startswith(("TABLE", "FIGURE", "Equation", "INTRODUCTION")):
                print(f"   Block ({b[0]:.1f},{b[1]:.1f},{b[2]:.1f},{b[3]:.1f}): {text}")

        print()


def generate_previews(pdf_path: str, preview_dir: str, dpi: int = 150):
    """Сгенерировать PNG-превью всех страниц для визуального выбора зон."""
    doc = fitz.open(pdf_path)
    out_dir = Path(preview_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for i in range(len(doc)):
        page = doc[i]
        pix = page.get_pixmap(dpi=dpi)
        fname = out_dir / f"page_{i+1:02d}_preview.png"
        pix.save(str(fname))
        print(f"   Saved preview: {fname}")

    print(f"\n✅ Превью сохранены в: {out_dir.absolute()}")


def parse_crop_spec(spec: str) -> dict:
    """Парсинг строки crop-спецификации."""
    result = {}
    parts = spec.split(",")
    for part in parts:
        if ":" not in part:
            continue
        key, value = part.split(":", 1)
        key = key.strip()
        value = value.strip()

        if key == "page":
            result["page"] = int(value) - 1  # 0-based
        elif key == "name":
            result["name"] = value
        elif key == "rect":
            coords = [float(x.strip()) for x in value.split(",")]
            if len(coords) != 4:
                raise ValueError(f"rect требует 4 координаты: x0,y0,x1,y1. Получено: {value}")
            result["rect"] = fitz.Rect(*coords)
        elif key == "y":
            y_parts = [float(x.strip()) for x in value.split("-")]
            if len(y_parts) != 2:
                raise ValueError(f"y требует диапазон Y0-Y1. Получено: {value}")
            result["y_range"] = (y_parts[0], y_parts[1])

    if "page" not in result or "name" not in result:
        raise ValueError(f"crop-спецификация должна содержать page и name: {spec}")

    return result


def create_crops(pdf_path: str, sota_id: str, output_dir: str, crop_specs: list, dpi: int = 200):
    """Создать PNG-crops по спецификациям."""
    doc = fitz.open(pdf_path)
    media_dir = Path(output_dir) / f"{sota_id}-media"
    media_dir.mkdir(parents=True, exist_ok=True)

    for spec in crop_specs:
        try:
            cfg = parse_crop_spec(spec)
        except ValueError as e:
            print(f"⚠️  Пропущена спецификация: {e}")
            continue

        page_idx = cfg["page"]
        name = cfg["name"]
        page = doc[page_idx]
        page_rect = page.rect

        # Определить crop rect
        if "rect" in cfg:
            crop_rect = cfg["rect"]
        elif "y_range" in cfg:
            y0, y1 = cfg["y_range"]
            crop_rect = fitz.Rect(0, y0, page_rect.width, y1)
        else:
            print(f"⚠️  Не указан rect или y для '{name}' — пропущено")
            continue

        # Проверить границы
        crop_rect = crop_rect & page_rect  # intersection
        if crop_rect.is_empty:
            print(f"⚠️  Crop rect вне границ страницы для '{name}' — пропущено")
            continue

        pix = page.get_pixmap(clip=crop_rect, dpi=dpi)
        out_path = media_dir / f"{name}.png"
        pix.save(str(out_path))
        print(f"   ✅ {out_path.name} ({crop_rect.width:.0f}×{crop_rect.height:.0f} @ {dpi}dpi)")

    print(f"\n📁 Медиа сохранены в: {media_dir.absolute()}")


def auto_extract_images(pdf_path: str, sota_id: str, output_dir: str, dpi: int = 200):
    """Автоматически извлечь все встроенные изображения из PDF."""
    doc = fitz.open(pdf_path)
    media_dir = Path(output_dir) / f"{sota_id}-media"
    media_dir.mkdir(parents=True, exist_ok=True)

    img_count = 0
    for i in range(len(doc)):
        page = doc[i]
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            rects = page.get_image_rects(xref)
            for rect in rects:
                pix = page.get_pixmap(clip=rect, dpi=dpi)
                img_count += 1
                name = f"auto-page{i+1}-img{img_count}"
                out_path = media_dir / f"{name}.png"
                pix.save(str(out_path))
                print(f"   ✅ {out_path.name} ({rect.width:.0f}×{rect.height:.0f} @ {dpi}dpi)")

    print(f"\n📁 Авто-извлечение завершено. Файлы в: {media_dir.absolute()}")
    print("   ⚠️  Автоматически извлечённые изображения могут включать логотипы,")
    print("      декоративные элементы и фрагменты текста. Рекомендуется ручной отбор.")


def main():
    parser = argparse.ArgumentParser(
        description="Извлечение PNG-crops из PDF для SoTA Book Chapter",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("--pdf", required=True, help="Путь к PDF-файлу")
    parser.add_argument("--sota-id", help="ID SoTA (например, CS.SOTA.297)")
    parser.add_argument("--output-dir", default=".", help="Базовая директория для выходных файлов")
    parser.add_argument("--inspect", action="store_true", help="Анализировать PDF и показать структуру")
    parser.add_argument("--preview", action="store_true", help="Сгенерировать превью всех страниц")
    parser.add_argument("--preview-dir", default="./preview", help="Директория для превью")
    parser.add_argument("--crop", action="append", help="Спецификация crop-зоны (можно несколько)")
    parser.add_argument("--auto-images", action="store_true", help="Автоматически извлечь все изображения")
    parser.add_argument("--dpi", type=int, default=200, help="DPI для рендеринга (default: 200)")

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"ERROR: Файл не найден: {args.pdf}")
        sys.exit(1)

    if args.inspect:
        inspect_pdf(args.pdf)
        return

    if args.preview:
        generate_previews(args.pdf, args.preview_dir, dpi=args.dpi)
        return

    if args.auto_images:
        if not args.sota_id:
            print("ERROR: --auto-images требует --sota-id")
            sys.exit(1)
        auto_extract_images(args.pdf, args.sota_id, args.output_dir, dpi=args.dpi)
        return

    if args.crop:
        if not args.sota_id:
            print("ERROR: --crop требует --sota-id")
            sys.exit(1)
        create_crops(args.pdf, args.sota_id, args.output_dir, args.crop, dpi=args.dpi)
        return

    print("ERROR: Укажите режим работы: --inspect, --preview, --auto-images или --crop")
    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
