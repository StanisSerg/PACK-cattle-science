#!/usr/bin/env python3
"""md -> PDF через PyMuPDF Story (A4), для методов и лекций dept-practices.

Использование: python3 md2pdf-story.py <файл.md> [<файл.pdf>]
По умолчанию PDF кладётся рядом с md (то же имя, расширение .pdf).

Шрифты: DejaVu из /usr/share/fonts/truetype/dejavu (кириллица).
Конвертер markdown минимальный: заголовки, жирный/курсив/код, списки,
таблицы, цитаты, горизонтальная линия, frontmatter пропускается.
"""

import html
import re
import sys
from pathlib import Path

import pymupdf as fitz  # PyMuPDF

FONT_DIR = "/usr/share/fonts/truetype/dejavu"

CSS = """
body { font-family: "DejaVu Sans"; font-size: 10pt; line-height: 1.35; }
h1 { font-size: 17pt; margin: 0 0 10pt 0; }
h2 { font-size: 13.5pt; margin: 14pt 0 6pt 0; }
h3 { font-size: 11.5pt; margin: 10pt 0 4pt 0; }
p { margin: 4pt 0; }
ul, ol { margin: 4pt 0 4pt 16pt; }
li { margin: 2pt 0; }
blockquote { margin: 6pt 0 6pt 8pt; padding: 4pt 8pt; background-color: #f0f4f8;
             border-left: 2pt solid #5b87a8; }
table { border-collapse: collapse; margin: 6pt 0; width: 100%; }
th, td { border: 0.6pt solid #888; padding: 3pt 5pt; font-size: 9pt;
         vertical-align: top; text-align: left; }
hr { color: #bbb; margin: 8pt 0; }
code { font-family: "DejaVu Sans Mono"; font-size: 8.5pt; }
"""


def inline(text: str) -> str:
    """Жирный, курсив, код — в html (после экранирования)."""
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"(?<!\w)\*([^*]+?)\*(?!\w)", r"<i>\1</i>", text)
    text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
    return text


def flush_list(buf, out, ordered):
    if not buf:
        return
    tag = "ol" if ordered else "ul"
    items = "".join(f"<li>{inline(x)}</li>" for x in buf)
    out.append(f"<{tag}>{items}</{tag}>")
    buf.clear()


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    # пропустить frontmatter
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                lines = lines[i + 1:]
                break
    out, ol_buf, ul_buf, tbl, bq_buf = [], [], [], [], []
    for raw in lines:
        line = raw.rstrip()
        if line.lstrip().startswith("|"):
            flush_list(ol_buf, out, True)
            flush_list(ul_buf, out, False)
            flush_bq(bq_buf, out)
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                continue  # разделитель таблицы
            tbl.append(cells)
            continue
        if tbl:
            flush_table(tbl, out)
        if not line.strip():
            flush_list(ol_buf, out, True)
            flush_list(ul_buf, out, False)
            flush_bq(bq_buf, out)
            continue
        m = re.match(r"^(#{1,4})\s+(.*)", line)
        if m:
            flush_list(ol_buf, out, True)
            flush_list(ul_buf, out, False)
            flush_bq(bq_buf, out)
            lvl = len(m.group(1))
            out.append(f"<h{lvl}>{inline(m.group(2))}</h{lvl}>")
            continue
        if re.match(r"^---+\s*$", line):
            flush_list(ol_buf, out, True)
            flush_list(ul_buf, out, False)
            flush_bq(bq_buf, out)
            out.append("<hr/>")
            continue
        m = re.match(r"^>\s?(.*)", line)
        if m:
            flush_list(ol_buf, out, True)
            flush_list(ul_buf, out, False)
            bq_buf.append(m.group(1))
            continue
        m = re.match(r"^\s*(\d+)\.\s+(.*)", line)
        if m:
            flush_list(ul_buf, out, False)
            flush_bq(bq_buf, out)
            ol_buf.append(m.group(2))
            continue
        m = re.match(r"^\s*[-*]\s+(.*)", line)
        if m:
            flush_list(ol_buf, out, True)
            flush_bq(bq_buf, out)
            ul_buf.append(m.group(1))
            continue
        # продолжение открытого пункта списка или цитаты (перенос строки в md)
        if ol_buf:
            ol_buf[-1] += " " + line.strip()
            continue
        if ul_buf:
            ul_buf[-1] += " " + line.strip()
            continue
        if bq_buf:
            bq_buf[-1] += " " + line.strip()
            continue
        out.append(f"<p>{inline(line)}</p>")
    flush_list(ol_buf, out, True)
    flush_list(ul_buf, out, False)
    flush_bq(bq_buf, out)
    if tbl:  # таблица в конце файла
        flush_table(tbl, out)
    return f"<html><head><style>{CSS}</style></head><body>{''.join(out)}</body></html>"


def flush_bq(buf, out):
    if not buf:
        return
    out.append(f"<blockquote>{'<br/>'.join(inline(x) for x in buf)}</blockquote>")
    buf.clear()


def flush_table(tbl, out):
    head, *rows = tbl
    t = ["<table><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr>"]
    for r in rows:
        t.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>")
    t.append("</table>")
    out.append("".join(t))
    tbl.clear()


def main():
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else src.with_suffix(".pdf")
    md = src.read_text(encoding="utf-8")
    story = fitz.Story(html=md_to_html(md), archive=fitz.Archive(FONT_DIR))
    writer = fitz.DocumentWriter(str(dst))
    mediabox = fitz.paper_rect("a4")
    where = mediabox + (36, 36, -36, -36)  # поля ~12.7 мм
    while True:
        device = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(device)
        writer.end_page()
        if not more:
            break
    writer.close()
    print(f"OK: {dst} ({dst.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
