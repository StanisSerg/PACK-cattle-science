# Правила интеграции новых SoTA

> Автоматическая классификация и размещение новых источников

---

## Алгоритм классификации

### Шаг 1: Определить тему по ключевым словам

```
ЕСЛИ type == "core":
    → папка core/
    # Фундаментальные сущности: cow, milk, rumen, metabolism, 
    # reproductive-system, immunity и т.д.

ЕСЛИ keywords СОДЕРЖИТ (репродукция OR осеменение OR стельность OR нетель OR 
                       сперма OR IEP OR VWP OR 21-d PR OR pregnancy):
    → папка reproduction/

ИНАЧЕ ЕСЛИ keywords СОДЕРЖИТ (кормление OR рацион OR энергия OR протеин OR 
                             минералы OR витамины OR NDF OR NEL OR MP OR 
                             CNCPS OR AMTS OR рубец OR ферментация):
    → папка feeding/

ИНАЧЕ ЕСЛИ keywords СОДЕРЖИТ (здоровье OR болезнь OR метаболизм OR кетоз OR 
                             гипокальция OR мастит OR ламинит OR иммунитет):
    → папка health/

ИНАЧЕ:
    → определить вручную / создать новую папку
```

### Шаг 2: Определить ID

| Папка | Диапазон ID | Правило нумерации | Тип YAML |
|-------|-------------|-------------------|----------|
| core/ | CORE.001-099 | Фундаментальные сущности | `type: core` |
| methods/ | METHOD.001-099 | Расчётные и практические методы | `type: method` |
| applications/ | APP.001-099 | Протоколы и шаблоны | `type: application` |
| reproduction/ | 001-099 | SoTA по репродукции | `type: sota` |
| feeding/ | 010-XXX | NASEM: 010-YY, остальные: 011-099 | `type: sota` |
| health/ | 100-199 | SoTA по здоровью | `type: sota` |

### Шаг 3: Проверить необходимость новой папки

```
ЕСЛИ новая тема НЕ входит в существующие:
    → предложить создать папку
    → примеры: genetics/, welfare/, precision-farming/
```

---

## Ключевые слова по папкам

### core/
- **Type:** `type: core` в YAML frontmatter
- **Сущности:** cow, milk, rumen, metabolism, reproductive-system, immunity
- **Характеристики:** Фундаментальные концепции, на которые ссылаются другие SoTA
- **ID format:** `CS.CORE.XXX`

### methods/
- **Type:** `type: method` в YAML frontmatter
- **Содержание:** Расчётные методы, SOP, алгоритмы, чек-листы
- **Связь:** Реализуют SoTA в практические инструкции
- **ID format:** `CS.METHOD.XXX`
- **Примеры:** calculate-nel, calculate-mp, assess-bcs, detect-heat

### applications/
- **Type:** `type: application` в YAML frontmatter
- **Содержание:** Готовые протоколы, шаблоны рационов, программы
- **Связь:** Используют methods для конкретных ситуаций
- **ID format:** `CS.APP.XXX`
- **Примеры:** early-lactation-ration, transition-protocol, ketosis-prevention

### reproduction/
- **Primary:** reproduction, insemination, pregnancy, conception, estrus, heat detection
- **Secondary:** semen, IEP, VWP, 21-d PR, pregnancy rate, breeding, AI, TAI, ED
- **Economic:** economic value, replacement, culling, optimal, simulation, Markov

### feeding/
- **Primary:** nutrition, feeding, diet, ration, energy, protein, mineral, vitamin
- **Models:** CNCPS, AMTS, NRC, NASEM, model, prediction
- **Parameters:** NEL, NEM, MP, RUP, RDP, NDF, ADF, DMI, intake
- **Processes:** rumen, fermentation, digestion, microbial, VFA

### health/
- **Primary:** health, disease, disorder, syndrome, infection, inflammation
- **Metabolic:** ketosis, hypocalcemia, milk fever, displaced abomasum, DA
- **Indicators:** NEFA, BHBA, BCS, body condition, immune, cortisol
- **Management:** prevention, treatment, therapy, antibiotic, vaccine

---

## Примеры классификации

| Статья | Ключевые слова | Папка | ID |
|--------|---------------|-------|-----|
| "Effect of progesterone on fertility" | progesterone, fertility, pregnancy | reproduction/ | 007 |
| "Energy requirements for high-producing cows" | energy, requirements, NEL | feeding/ | 011 |
| "Ketosis prevention strategies" | ketosis, prevention, health | health/ | 100 |
| "Genetic markers for longevity" | genetic, markers, longevity | ??? | вручную |

---

## Процесс добавления новой SoTA

### Ручной режим (сейчас)

1. Пользователь предоставляет статью (PDF или ссылку)
2. Я анализирую abstract/title/keywords
3. Применяю правила классификации
4. Сообщаю: "Это reproduction/ → CS.SOTA.010"
5. Создаю файл в правильной папке

### Полуавтоматический (цель)

```
Пользователь: "Добавь SoTA: https://doi.org/..."

Я:
1. Fetch URL → получаю метаданные
2. Применяю правила классификации
3. Предлагаю: "reproduction/ → CS.SOTA.010?"
4. После подтверждения — создаю файл
```

---

## Создание новых папок

### Триггеры

| Ситуация | Действие |
|----------|----------|
| >5 статей не подходят под существующие | Предложить новую папку |
| Новая предметная область | Создать папку + обновить индекс |
| Пересечение тем | Выбрать primary, добавить теги |

### Примеры будущих папок

```
06-sota/
├── core/             # фундаментальные сущности (6 файлов)
│   └── CS.CORE.XXX.md
├── methods/          # методы и алгоритмы (SOP)
│   └── CS.METHOD.XXX.md
├── applications/     # практическое применение (протоколы)
│   └── CS.APP.XXX.md
├── reproduction/     # репродукция (14 файлов)
│   └── CS.SOTA.XXX.md
├── feeding/          # питание (6 файлов)
│   └── CS.SOTA.XXX.md
├── health/           # здоровье (резерв)
│   └── CS.SOTA.XXX.md
├── genetics/         # будущее: GWAS, genomic selection
├── welfare/          # будущее: behavior, housing, stress
└── precision-farming/# будущее: sensors, AI, automation
```

---

## Интеграция с CS.MAP.001

При добавлении новой SoTA:
1. Обновить таблицу в соответствующем разделе
2. Добавить в "Полный список"
3. Обновить "По темам" если новая категория
4. Обновить "По году"
5. Обновить счётчик: "Всего SoTA: X"

---

*Rules version: 0.1.0 | Created: 2026-03-03*
