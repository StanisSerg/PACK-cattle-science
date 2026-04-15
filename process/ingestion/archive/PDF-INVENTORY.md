---
type: inventory
scope: external-pdf-archive
location: /root/PACK-cattle-science-pdfs/
---

# PDF-INVENTORY: Архив исходных статей

> **Важно:** PDF-файлы вынесены из git-репозитория во внешнюю директорию.
> 
> **Локальный путь:** `/root/PACK-cattle-science-pdfs/`

## Структура архива

```
/root/PACK-cattle-science-pdfs/
├── W 2026 февраль/     # 26 PDF (SoTA 268-293)
├── W 2026 январь/      # 15 PDF (SoTA 253-267)
├── W10-11/             # ~55 PDF (ранние интеграции WP-75)
├── W12/                # ~42 PDF
├── W13/                # ~38 PDF
├── W14/                # 2 PDF
├── W15/                # ~43 PDF
└── W16/                # ~55 PDF (SoTA 197-203)
```

## Поиск оригинала по SoTA

1. Определите автора и год из `CS.SOTA.XXX`.
2. Перейдите в соответствующую неделю в `/root/PACK-cattle-science-pdfs/`.
3. Найдите PDF по имени файла (автор + год в названии).

## История миграции

- **2026-04-15:** Все PDF и TXT-артефакты вынесены из `process/ingestion/archive/` во внешнюю директорию `/root/PACK-cattle-science-pdfs/` для облегчения репозитория (~295 МБ → 0 МБ).
