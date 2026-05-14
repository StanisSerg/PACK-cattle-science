# TEMPLATES — Шаблоны и утилиты для SoTA

## Содержание

| Файл | Назначение |
|------|------------|
| `SOTA-TEMPLATE.md` | Базовый шаблон SoTA для статей и исследований (paper/article) |
| `SOTA-CHAPTER-EXPANDED-TEMPLATE.md` | Расширенный шаблон SoTA для глав референсных книг (book chapter, expanded v1.3) |
| `extract-media-from-pdf.py` | Утилита для извлечения PNG-crops из PDF |

---

## extract-media-from-pdf.py

Утилита для извлечения скриншотов (PNG crops) из PDF-файлов NASEM / NRC для встраивания в SoTA.

### Зависимости

```bash
pip install pymupdf
```

### Режим 1: Анализ PDF (inspect)

Показывает изображения, векторные линии (drawings) и ключевые текстовые блоки на каждой странице.

```bash
python extract-media-from-pdf.py --pdf "Глава 5.pdf" --inspect
```

### Режим 2: Генерация превью (preview)

Создаёт PNG всех страниц для визуального выбора crop-зон.

```bash
python extract-media-from-pdf.py --pdf "Глава 5.pdf" --preview --preview-dir ./preview
```

### Режим 3: Ручное создание crops (рекомендуемый)

После анализа и превью создайте crops с явным указанием зон:

```bash
python extract-media-from-pdf.py \
    --pdf "Глава 5.pdf" \
    --sota-id CS.SOTA.297 \
    --output-dir "../06-sota/feeding/" \
    --crop "page:2,y:75-265,name:figure-5-1-carbohydrate-fractions" \
    --crop "page:7,y:295-485,name:table-5-1-recommended-ndf-starch" \
    --crop "page:7,y:220-410,name:figure-5-2-optimal-fndf-factors" \
    --crop "page:9,y:75-1175,name:table-5-2-pandf-predictions" \
    --crop "page:10,y:75-315,name:figure-5-3-adf-ndf-ratio"
```

Результат сохраняется в `../06-sota/feeding/CS.SOTA.297-media/`.

**Параметры crop:**
- `page:N` — номер страницы (1-based)
- `y:Y0-Y1` — вертикальный диапазон crop (X = полная ширина)
- `rect:x0,y0,x1,y1` — точный bounding box (альтернатива `y`)
- `name:STRING` — имя файла без расширения

### Режим 4: Авто-экстракция изображений

Извлекает все встроенные растровые изображения из PDF (будьте осторожны — может включать логотипы и декор).

```bash
python extract-media-from-pdf.py \
    --pdf "Глава 5.pdf" \
    --sota-id CS.SOTA.297 \
    --output-dir "../06-sota/feeding/" \
    --auto-images
```

### Соглашение об именовании файлов

| Тип | Шаблон имени | Пример |
|-----|-------------|--------|
| Рисунок | `figure-{N}-{desc}.png` | `figure-5-1-carbohydrate-fractions.png` |
| Таблица | `table-{N}-{desc}.png` | `table-5-1-recommended-ndf-starch.png` |
| Уравнение | `equation-{N}-{desc}.png` | `equation-3-14-nel-milk.png` |

### DPI

По умолчанию 200 dpi — достаточно для чтения на экране и печати. Для превью используется 150 dpi.
