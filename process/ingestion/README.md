# Ingestion Process

> Процесс добавления новых статей в PACK-cattle-science

---

## Быстрый старт

### Шаг 1: Скопируй PDF-файлы

Скопируй PDF-файлы из Zotero в папку:
```
PACK-cattle-science/process/ingestion/new-articles/
```

### Шаг 2: Запусти извлечение текста

```bash
cd PACK-cattle-science/process/ingestion
python extract_pdf.py
```

Результат: `extraction_results.json` с извлечённым текстом.

### Шаг 3: Сообщи мне

Скажи: "Готово, извлеки статьи" — и я:
- Проанализирую текст
- Создам ingestion log entries
- Создам SoTA-аннотации
- Создам методы/сущности (если нужно)

---

## Структура папки

```
ingestion/
├── README.md                    # Этот файл
├── extract_pdf.py               # Скрипт извлечения текста
├── ingestion-template.md        # Шаблон для новых статей
├── new-articles/                # Сюда копировать PDF
│   ├── article1.pdf
│   └── article2.pdf
└── extraction_results.json      # Результат извлечения
```

---

## Требования

- Python 3.8+
- pdfplumber (`pip install pdfplumber`)

---

*Последнее обновление: 2026-03-02*
