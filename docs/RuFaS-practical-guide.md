# Практическое руководство по RuFaS

> **Назначение.** Этот документ — рабочая шпаргалка для запуска, настройки и отладки модели RuFaS (Ruminant Farm Systems) на локальной машине. Он собран из официальной вики RuFaS, onboarding-видео и опыта интеграции с `PACK-cattle-science` / `DS-cattle-course`.
>
> **Актуальность:** июнь 2026. Версия кода в репозитории `/home/asus/IWE/RuFaS`.

---

## Содержание

1. [Что такое RuFaS и зачем он нужен](#1-что-такое-rufas-и-зачем-он-нужен)
2. [Установка и первый запуск](#2-установка-и-первый-запуск)
3. [Архитектура и структура проекта](#3-архитектура-и-структура-проекта)
4. [Пошаговый сценарий: первая симуляция](#4-пошаговый-сценарий-первая-симуляция)
5. [Работа с входными данными и metadata](#5-работа-с-входными-данными-и-metadata)
6. [Выходные данные: как читать и интерпретировать](#6-выходные-данные-как-читать-и-интерпретировать)
7. [Отладка кода](#7-отладка-кода)
8. [Best practices](#8-best-practices)
9. [Типичные проблемы и решения](#9-типичные-проблемы-и-решения)
10. [Связь с DS-cattle-course / PACK-cattle-science](#10-связь-с-ds-cattle-course--pack-cattle-science)
11. [Открытые вопросы](#11-открытые-вопросы)

---

## 1. Что такое RuFaS и зачем он нужен

**RuFaS** (Ruminant Farm Systems model) — открытая (open-source) целоферменная модель на Python, которая симулирует работу молочной фермы: поле → корм → животные → навоз → поле. Модель рассчитывает производство молока, динамику стада, кормление, выбытие, воспроизводство, а также экономику, энергию и выбросы (EEE — Economic & Environmental Estimator).

### Кому полезен

- Исследователям — для сценарного анализа и публикаций.
- Техническим консультантам — для оценки влияния изменений рациона или менеджмента.
- Фермерам и агрономам — для прогноза урожая, затрат и экологического следа.

### Что моделирует

- **Animal Module** — индивидуальная динамика животных в стаде: рождение, отъём, выращивание нетелей, осеменение, отёл, сухостойность, лактация, выбытие, энтерический метан.
- **Feed Storage Module** — заготовка, хранение и рационирование кормов (user-defined или optimized).
- **Manure Module** — удаление навоза, сепарация, анаэробное Digestion, хранение, выбросы.
- **Soil and Crop Module** — рост культур, почвенные процессы, циклы N/P/C, удобрения.
- **EEE** — экономика и экология: цены на молоко и корма, энергия, выбросы ГПГ.

### Режимы симуляции

| Режим | Что включает | Когда использовать |
|-------|--------------|-------------------|
| `animals_only` | Только животные + кормление + EEE | Быстрая оценка стада и молока без полей |
| `field_and_feed` | Животные + поля + корма | Оценка баланса кормов и полей |
| `full_farm` | Все модули | Полная ферма |

---

## 2. Установка и первый запуск

### 2.1. Требования

- **Python 3.12 или 3.13** (RuFaS поддерживает только эти версии).
- **Git**.
- **IDE**: VS Code (рекомендуется командой) или PyCharm.
- ОС: Windows, macOS, Linux. Примеры команд ниже даны для Linux/macOS; для Windows заменяйте `python3` на `python` или `py -3.13`.

### 2.2. Клонирование и переход в папку

```bash
cd /home/asus/IWE
git clone https://github.com/RuminantFarmSystems/RuFaS.git  # если ещё не склонировано
cd RuFaS
```

Рабочая копия в этом руководстве: `/home/asus/IWE/RuFaS`.

### 2.3. Виртуальное окружение

```bash
python3 -m venv .venv
source .venv/bin/activate        # Linux/macOS
# .venv\Scripts\activate         # Windows
```

### 2.4. Установка зависимостей

```bash
pip install .
```

Команда читает `pyproject.toml` / `requirements.txt` и ставит все нужные пакеты (numpy, pandas, matplotlib и др.).

### 2.5. Первый запуск

Самый простой вариант — запуск example-сценария по умолчанию:

```bash
python main.py
```

Если всё в порядке, в терминале появится версия RuFaS и сообщение о старте симуляции. Результаты по умолчанию пишутся в `output/`.

### 2.6. Запуск конкретного сценария

```bash
python main.py -p input/metadata/animals_only_tm_metadata.json
```

Флаг `-p` указывает на **task manager metadata**, а не напрямую на metadata симуляции.

### 2.7. Основные аргументы командной строки

Справка:

```bash
python main.py -h
```

| Аргумент | Длинная форма | Действие |
|----------|---------------|----------|
| `-g` | `--no-graphics` | Не генерировать графики (ускоряет прогон) |
| `-v` | `--verbose` | Выводить в терминал логи/варнинги/ошибки. Варианты: `none`, `errors`, `warnings`, `logs`, `credits` |
| `-c` | `--clear-output` | Очистить выходную директорию перед запуском |
| `-o` | `--output-dir` | Задать выходную директорию (по умолчанию `output/`) |
| `-s` | `--suppress-log-files` | Не писать лог-файлы |
| `-l` | `--logs-dir` | Директория для логов (по умолчанию `output/logs`) |
| `-i` | `--exclude_info_maps` | Исключить объёмные info_maps из выходных файлов |
| `-m` | `--metadata-depth-limit` | Лимит вложенности metadata (по умолчанию 7) |
| `-p` | `--path-to-metadata` | Путь к task manager metadata |

Примеры комбинаций:

```bash
# очистить выход, не строить графики, выводить warnings
python main.py -c -g -v warnings

# запустить только валидацию входных данных (см. примечание ниже)
python main.py -ov

# запустить animals_only с чисткой выхода
python main.py -p input/metadata/animals_only_tm_metadata.json -c -g
```

> **Примечание по валидации.** В wiki Input Manager упоминается флаг `-ov` (only validation). В onboarding-видео используется `--validate_only`. Точный синтаксис уточняйте через `python main.py -h` в вашей версии.

---

## 3. Архитектура и структура проекта

### 3.1. Высокоуровневая цепочка

```
main.py
  └── Task Manager
        └── Input Manager  ← metadata + properties + biophysical data
              └── Simulation Engine
                    └── Biophysical modules (Animal, Feed Storage, Manure, Soil/Crop)
                    └── EEE (Economic & Environmental Estimator)
                          └── Output Manager
                                ├── CSV/JSON dumps
                                ├── logs / warnings / errors
                                ├── reports (Report Generator)
                                └── graphs (Graph Generator)
```

### 3.2. Ключевые модули

| Модуль | Файл / папка | Ответственность |
|--------|--------------|-----------------|
| **Task Manager** | `RUFAS/task_manager.py` | Оркестрация задач: `SIMULATION_SINGLE_RUN`, `SIMULATION_MULTI_RUN`, `SENSITIVITY_ANALYSIS`, `HERD_INITIALIZATION` и др. Параллельные воркеры, префиксы выходных файлов |
| **Input Manager** | `RUFAS/input_manager.py` | Загрузка metadata, валидация входных данных, единый пул входных данных (`get_data`) |
| **Simulation Engine** | `RUFAS/simulation_engine.py` | Главный цикл `simulate()`: годовой и ежедневный циклы, вызов биофизических модулей |
| **Output Manager** | `RUFAS/output_manager.py` | Сбор переменных, логов, warnings, errors; фильтрация и запись CSV/JSON |
| **Report Generator** | `RUFAS/report_generator.py` | Агрегация данных в отчёты по JSON-фильтрам `report_*` |
| **Graph Generator** | `RUFAS/graph_generator.py` | Построение графиков по JSON-фильтрам `graph_*` |

### 3.3. Структура папок

```
/home/asus/IWE/RuFaS/
├── main.py                     # Точка входа
├── RUFAS/                      # Исходный код
│   ├── main.py
│   ├── task_manager.py
│   ├── input_manager.py
│   ├── simulation_engine.py
│   ├── output_manager.py
│   ├── report_generator.py
│   ├── graph_generator.py
│   ├── biophysical/            # Животные, поля, навоз и т.д.
│   └── EEE/                    # Экономика и экология
├── input/
│   ├── metadata/               # Metadata сценариев
│   │   ├── properties/         # Правила валидации (default.json, ...)
│   │   ├── task_manager_metadata.json
│   │   ├── animals_only_tm_metadata.json
│   │   ├── example_animals_only_metadata.json
│   │   └── ...
│   └── data/                   # Биофизические входные данные
│       ├── animal/
│       ├── feed/
│       ├── feed_management/
│       ├── config/
│       ├── manure/
│       ├── crop/, field/, soil/
│       ├── weather/
│       └── tasks/              # Task-файлы
├── output/                     # Результаты (не коммитятся)
│   └── output_filters/         # Фильтры выходных данных
├── tests/                      # Тесты
├── pyproject.toml              # Конфигурация Black, mypy и т.д.
├── .flake8                     # Конфигурация flake8
└── changelog.md
```

---

## 4. Пошаговый сценарий: первая симуляция

### Шаг 1. Создать или переключиться на ветку

Даже если вы просто экспериментируете, работайте в отдельной ветке.

```bash
git checkout -b my-first-rufas-run
```

### Шаг 2. Убедиться, что окружение и зависимости установлены

```bash
source .venv/bin/activate
python --version   # должна быть 3.12 или 3.13
pip install .      # если зависимости ещё не установлены
```

### Шаг 3. Запустить готовый сценарий `animals_only`

```bash
python main.py -p input/metadata/animals_only_tm_metadata.json -c -g -v warnings
```

Что происходит:

1. `main.py` читает `animals_only_tm_metadata.json`.
2. Task Manager загружает `input/data/tasks/example_animals_only_task.json`.
3. Task Manager видит `task_type: SIMULATION_SINGLE_RUN` и `metadata_file_path: input/metadata/example_animals_only_metadata.json`.
4. Input Manager валидирует входные файлы, указанные в metadata.
5. Simulation Engine прогоняет модель с 2013:1 по 2019:365.
6. Output Manager пишет результаты в `output/animals_only/`.

### Шаг 4. Проверить выходные файлы

```bash
ls -R output/animals_only/
```

Ожидаемые файлы:

- `output/animals_only/CSVs/` — CSV-таблицы (если есть активные `csv_*` фильтры).
- `output/animals_only/JSONs/` — JSON-дампы.
- `output/animals_only/reports/` — отчёты (если есть `report_*` фильтры).
- `output/animals_only/graphics/` — графики (если есть `graph_*` фильтры и не был указан `-g`).
- `output/logs/` — логи, warnings, errors.

### Шаг 5. Посмотреть список доступных переменных

```bash
cat output/variable_names_*.txt | head -50
```

Каждая строка — это полный ключ переменной вида:

```
ClassName.function_name.variable_name
```

Пример:

```
LifeCycleManager.daily_update.daily_milk_production
AnimalModuleReporter.report_herd_statistics_data.milking_cow_num
```

---

## 5. Работа с входными данными и metadata

### 5.1. Четыре уровня входных файлов

```
Биофизические данные  →  Metadata  →  Task  →  Task Manager Metadata
input/data/...         input/metadata/... input/data/tasks/... input/metadata/*_tm_metadata.json
```

- **Биофизические данные** — JSON/CSV с параметрами фермы.
- **Metadata** — указывает, какие файлы использовать и как их валидировать.
- **Task** — список задач; одна задача = один прогон (или несколько в случае multi-run/SA).
- **Task Manager Metadata** — точка входа, которую принимает `main.py -p`.

### 5.2. Где лежат основные файлы

| Компонент | Путь |
|-----------|------|
| Task manager metadata по умолчанию | `input/metadata/task_manager_metadata.json` |
| Task manager metadata для `animals_only` | `input/metadata/animals_only_tm_metadata.json` |
| Task-файл для `animals_only` | `input/data/tasks/example_animals_only_task.json` |
| Metadata симуляции `animals_only` | `input/metadata/example_animals_only_metadata.json` |
| Общие параметры симуляции | `input/data/config/example_animals_only_config.json` |
| Стадо и менеджмент | `input/data/animal/example_freestall_animal.json` |
| Рационы и корма | `input/data/feed/example_Midwest_feed.json` |
| Параметры лактационной кривой | `input/data/animal/lactation_curve_adjustment_inputs.json` |
| Погода | `input/data/weather/example_temperate_weather.csv` |
| Правила валидации | `input/metadata/properties/default.json` |

### 5.3. Как редактировать входные данные

1. **Не трогайте оригинальные example-файлы напрямую.** Сделайте копию, например:

   ```bash
   cp input/data/animal/example_freestall_animal.json input/data/animal/my_farm_animal.json
   cp input/data/feed/example_Midwest_feed.json input/data/feed/my_farm_feed.json
   ```

2. Измените нужные значения в JSON. Например, в `my_farm_animal.json`:

   ```json
   {
     "herd_information": {
       "cow_num": 150,
       "replace_num": 600,
       "breed": "HO"
     }
   }
   ```

3. **Обновите metadata**, чтобы она указывала на ваши файлы. Скопируйте metadata:

   ```bash
   cp input/metadata/example_animals_only_metadata.json input/metadata/my_farm_metadata.json
   ```

   Внутри `my_farm_metadata.json` измените пути, например:

   ```json
   "animal": {
     "path": "input/data/animal/my_farm_animal.json",
     ...
   },
   "feed": {
     "path": "input/data/feed/my_farm_feed.json",
     ...
   }
   ```

4. **Обновите task-файл** (или создайте новый):

   ```bash
   cp input/data/tasks/example_animals_only_task.json input/data/tasks/my_farm_task.json
   ```

   Внутри `my_farm_task.json`:

   ```json
   {
     "task_type": "SIMULATION_SINGLE_RUN",
     "metadata_file_path": "input/metadata/my_farm_metadata.json",
     "output_prefix": "my_farm",
     ...
   }
   ```

5. **Обновите task manager metadata**:

   ```bash
   cp input/metadata/animals_only_tm_metadata.json input/metadata/my_farm_tm_metadata.json
   ```

   Внутри измените путь к task-файлу:

   ```json
   "tasks": {
     "path": "input/data/tasks/my_farm_task.json",
     ...
   }
   ```

6. Запустите:

   ```bash
   python main.py -p input/metadata/my_farm_tm_metadata.json -c -g
   ```

### 5.4. Как добавить свою ферму: чек-лист данных

Для режима `animals_only` (достаточно для большинства задач PACK-cattle-science) нужны:

#### A. Общие параметры (`config.json`)

- Начальная дата (`start_date`, формат `"год:день_года"`, например `"2013:1"`).
- Конечная дата (`end_date`).
- `simulation_type`: `animals_only` / `field_and_feed` / `full_farm`.
- `nutrient_standard`: `NASEM` или `NRC`.
- `set_seed`, `include_detailed_values`, `FIPS_county_code`.

#### B. Стадо (`animal.json`)

- Количество по группам: телки, нетели, сухостойные, дойные.
- Загоны (`pen`) и группы дойных.
- Распределение по паритетам и средние DIM.
- Порода (`HO`, `JE` и др.), живой вес.
- Репродуктивные параметры: процент осеменения, возраст первого отёла, сухостойность.
- Правила выбытия: по молоку, DIM, возрасту, плодовитости.

#### C. Лактационная кривая

- `input/data/animal/lactation_curve_adjustment_inputs.json`.
- Средние удои по декадам/месяцам DIM, жир, белок, 305-дневный удой.
- Если есть параметры кривой Wood — записать.

#### D. Корма и рационы (`feed.json`)

- Список `feed_type` (ID из `input/data/feed/user_feeds.csv` или `NASEM_Comp_with_TDN_urea.csv`).
- Для каждого корма: цена, buffer, лимиты закупки.
- Рационы по группам: `calf`, `growing`, `dry`, `lactating` и т.д.

#### E. Пустые конфиги для отключённых модулей

В режиме `animals_only` используются пустые, но **структурно корректные** файлы:

- `input/data/manure/no_manure_processor_configs.json`
- `input/data/manure/no_manure_processor_connections.json`
- `input/data/crop_configurations/no_crop_configs.json`
- `input/data/field/no_field.json`
- `input/data/soil/no_soil.json`
- `input/data/crop/no_crop.json`
- `input/data/fertilizer_schedule/no_fertilizer.json`
- `input/data/manure_schedule/no_manure.json`
- `input/data/tillage_schedule/no_till.json`
- `input/data/feed_management/no_feed_storage_configs.json`
- `input/data/feed_management/no_feed_storages.json`
- `input/data/EEE/no_tractor_dataset.csv`

> **Важно:** в некоторых версиях файлы `no_feed_storage_configs.json` и `no_feed_storages.json` содержали только `{"exclude_from_pool": true}`, что приводило к ошибке валидации. Правильная форма — пустой словарь `{}` или полная структура. Подробнее см. раздел [Типичные проблемы](#9-типичные-проблемы-и-решения).

### 5.5. Валидация через Input Manager

Input Manager проверяет:

- типы данных;
- минимум/максимум;
- регулярные выражения (`pattern`);
- наличие обязательных полей.

Если поле некритичное и не прошло валидацию, подставляется значение по умолчанию из `default.json`. Если критичное — симуляция останавливается.

Перед полным прогоном полезно запустить валидацию:

```bash
python main.py -ov
```

(или `python main.py --validate_only` — уточняйте через `python main.py -h`).

---

## 6. Выходные данные: как читать и интерпретировать

### 6.1. Четыре пула Output Manager

Output Manager собирает:

1. **variables** — рассчитанные величины (молоко, количество коров, выбросы и т.д.).
2. **logs** — события (загрузка файла, создание директории).
3. **warnings** — предупреждения, не прерывающие прогон.
4. **errors** — ошибки, влияющие на результат, но не обязательно прерывающие прогон.
5. **exceptions** — критические ошибки, прерывающие симуляцию.

### 6.2. Файл `variable_names`

После прогона в `output/` появляется `variable_names_<timestamp>.txt` — список всех переменных в пуле. Используйте его для составления фильтров.

Формат ключа:

```
ClassName.function_name.variable_name
```

Примеры:

```
LifeCycleManager.daily_update.daily_milk_production
AnimalModuleReporter.report_herd_statistics_data.milking_cow_num
AnimalModuleReporter.report_herd_statistics_data.avg_days_in_milk
AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_herd_mean
```

### 6.3. Фильтры выходных данных

Фильтры лежат в `output/output_filters/`. Имя файла определяет формат:

| Префикс | Формат | Обработчик |
|---------|--------|------------|
| `csv_` | CSV | Output Manager |
| `json_` | JSON | Output Manager |
| `report_` | CSV-отчёт | Report Generator |
| `graph_` | PNG/PDF | Graph Generator |

Файлы, начинающиеся с `_`, игнорируются.

#### Пример CSV-фильтра

Создайте `output/output_filters/csv_milk.txt`:

```text
.*daily_milk_production.*
.*milking_cow_num.*
.*avg_days_in_milk.*
```

После запуска в `output/CSVs/om/` появится `saved_variables_csv_milk_<timestamp>.csv`.

#### Пример JSON-фильтра с data origins

Создайте `output/output_filters/json_ration_true_origin.json`:

```json
{
  "name": "Ration Nutrients True Origin",
  "filters": [
    "AnimalModuleReporter.report_ration_interval_data.ration_nutrient_amount_pen_.*"
  ],
  "origin_label": "true origin"
}
```

### 6.4. Report Generator

JSON-фильтры `report_*` позволяют агрегировать данные.

Пример: среднесуточный надой за последний год.

```json
{
  "multiple": [
    {
      "name": "Last Year's Average Daily Milk Production",
      "filters": ["LifeCycleManager.daily_update.daily_milk_production"],
      "vertical_aggregation": "average",
      "slice_start": -365,
      "direction": "landscape"
    }
  ]
}
```

Доступные агрегаторы: `average`, `sum`, `product`, `division`, `subtraction`, `SD`.

### 6.5. Graph Generator

JSON-фильтры `graph_*` строят графики.

Пример:

```json
{
  "type": "plot",
  "filters": [
    "AnimalModuleReporter.report_herd_statistics_data.daily_milk_production"
  ],
  "title": "Daily Milk Production",
  "use_calendar_dates": true
}
```

Для headless-режима (без GUI) используйте `-g`, чтобы не строить графики, или настройте matplotlib backend на `Agg` в `RUFAS/graph_generator.py`.

### 6.6. Как интерпретировать результаты

- **Ежедневный надой стада**: `LifeCycleManager.daily_update.daily_milk_production` (кг/сут).
- **Количество дойных**: `AnimalModuleReporter.report_herd_statistics_data.milking_cow_num`.
- **Средние DIM**: `AnimalModuleReporter.report_herd_statistics_data.avg_days_in_milk`.
- **Удой на корову**: деление `daily_milk_production` на `milking_cow_num`.
- **305-дневный удой**: `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_herd_mean`.
- **Жир / белок**: `herd_milk_fat_percent`, `herd_milk_protein_percent`.

Пример валидации для CASE-002:

1. Baseline-прогон RuFaS.
2. Сравнение predicted vs actual по молоку, DIM, составу молока.
3. При необходимости — калибровка `lactation_curve_adjustment_inputs.json`.
4. Scenario-прогон с изменённым рационом/менеджментом.
5. Сравнение Δ predicted vs Δ actual.

---

## 7. Отладка кода

### 7.1. Общий подход

1. Найти, где возникает проблема (логи, warnings, exceptions).
2. Открыть соответствующий Python-файл.
3. Использовать поиск по всей кодовой базе (`Ctrl+Shift+F` в VS Code).
4. Трассировать переменную от входного файла до расчёта и до Output Manager.

### 7.2. Поиск научных уравнений

В научной документации уравнения имеют идентификаторы вида `A_NSM_1`:

- `A` — Animal module;
- `NSM` — подраздел (например, nutrient requirements);
- `1` — номер уравнения.

Чтобы найти реализацию в коде:

```text
VS Code → Ctrl+Shift+F → A_NSM_1
```

### 7.3. Трассировка входных переменных

Входные данные читаются через Input Manager:

```python
from RUFAS.input_manager import InputManager
im = InputManager()
cow_data = im.get_data('cow_data')
```

Переменные часто переименовываются на пути от входных файлов к внутренней логике. Ищите:

- исходное имя в JSON;
- имя внутри класса (например, `calf_num` → `animal_num`);
- место использования через `Ctrl+Shift+F`.

### 7.4. Трассировка выходных переменных

Переменные добавляются в Output Manager примерно так:

```python
om.report_variable(
    name="daily_milk_production",
    value=milk,
    info_map=info_map
)
```

Точное имя метода может отличаться в зависимости от версии. Ищите по частям имени, потому что имена часто формируются динамически через f-строки.

### 7.5. Отладка через `print`

Самый простой способ — вставить `print()` в нужное место:

```python
print(f"DEBUG: calf_num = {calf_num}")
```

Осторожно: большое количество `print` замедляет симуляцию и засоряет терминал. Удаляйте их после отладки.

### 7.6. Отладка через VS Code debugger

1. Откройте файл, например `RUFAS/routines/animal/herd_manager.py`.
2. Поставьте breakpoint кликом слева от номера строки.
3. Нажмите `F5` или `Run → Start Debugging`.
4. В Debug Console смотрите переменные, call stack, watch-лист.

Полезные команды в Debug Console:

```python
herd_statistics  # весь объект
herd_statistics.calf_num
```

### 7.7. Снижение объёма выходных данных

Если выходные файлы слишком большие:

- используйте `-i` / `--exclude_info_maps`;
- отключайте ненужные фильтры (переименуйте с `_` в начале);
- используйте `csv_*` фильтры вместо полного JSON-дампа;
- для длинных прогонов настройте chunkification (см. wiki Chunkification).

---

## 8. Best practices

### 8.1. Форматирование: Black

RuFaS использует `Black` с длиной строки 120 символов (см. `pyproject.toml`).

```bash
black RUFAS/routines/animal/animal_manager.py
```

Black также запускается автоматически в GitHub Actions.

### 8.2. Линтинг: Flake8

```bash
flake8 RUFAS/routines/animal/animal_manager.py
```

Конфигурация в `.flake8`:

```ini
[flake8]
count = True
max-line-length = 120
```

Для проверки только изменённых файлов используйте:

```bash
./check_changes.sh          # Linux/macOS
.\check_changes.bat         # Windows
```

### 8.3. Type checking: mypy

```bash
mypy RUFAS/routines/animal/animal_manager.py
```

Конфигурация в `pyproject.toml`. GitHub Actions пока не блокирует PR по ошибкам mypy, но их число должно не расти.

### 8.4. Тесты: pytest

```bash
pytest
```

Все новые/изменённые функции должны иметь unit-тесты.

### 8.5. Code review

Перед PR убедитесь, что:

- код проходит `pytest`;
- нет новых ошибок `flake8`;
- `mypy` не увеличивает число ошибок;
- добавлены docstrings в формате NumPy;
- добавлены type hints;
- PR привязан к issue;
- описание PR следует структуре What / Why / How / Test Plan;
- обновлён `changelog.md`;
- нет временных файлов и лишних `print`.

### 8.6. Branching strategy

- `dev` — основная ветка разработки, в неё мержатся PR (нужно 2 аппрува).
- `test` — стабилизация перед релизом.
- `main` — стабильный релиз, только админы.

Создавайте feature-ветки от `dev`:

```bash
git checkout dev
git pull
git checkout -b feature/my-change
```

### 8.7. Общение с командой

1. Сначала поищите ответ в wiki и README.
2. Если вопрос общий — создайте GitHub Discussion.
3. Если это конкретный баг или задача — создайте Issue.
4. Только после этого пишите личные письма (для логистики/конфиденциальности).

---

## 9. Типичные проблемы и решения

### 9.1. Ошибка валидации `feed_storage_configs` / `feed_storage_instances`

**Симптом:** в режиме `animals_only` падает с ошибкой, что feed storage configs == `None`.

**Причина:** файлы `no_feed_storage_configs.json` и `no_feed_storages.json` содержали `{"exclude_from_pool": true}`, и Input Manager пропускал их, а EEE ожидал словарь.

**Решение:** замените содержимое на пустой, но корректный словарь:

```json
{}
```

Или добавьте защитный патч в `RUFAS/EEE/emissions.py` на случай `None`.

Пути:

- `input/data/feed_management/no_feed_storage_configs.json`
- `input/data/feed_management/no_feed_storages.json`

### 9.2. Matplotlib падает в headless-окружении

**Симптом:** `ImportError: Cannot load backend 'TkAgg'` или похожее.

**Решение:** в `RUFAS/graph_generator.py` замените:

```python
matplotlib.use("TkAgg")
```

на:

```python
matplotlib.use("Agg")
```

Или всегда запускайте с `-g` / `--no-graphics`.

### 9.3. Не сохраняется CSV-выход

**Симптом:** симуляция завершилась, но CSV нет.

**Причины:**

- в task-файле не задан `csv_output_directory`;
- в `output/output_filters/` нет активного фильтра с префиксом `csv_`;
- файл фильтра начинается с `_` и игнорируется.

**Решение:**

1. В task-файле укажите:

   ```json
   "csv_output_directory": "output/my_run/CSVs/."
   ```

2. Создайте фильтр `output/output_filters/csv_all.txt`:

   ```text
   .*
   ```

### 9.4. Много warnings — это нормально?

Да. Стандартный `freestyle`-сценарий выдаёт ~174 warnings. Warnings не обязательно критичны, но их стоит анализировать при неожиданном поведении.

### 9.5. Один user-defined рацион на группу LAC_COW

**Ограничение:** `RationManager` хранит `user_defined_rations` как `dict[AnimalCombination, ...]`. Для дойных используется только `LAC_COW`, поэтому две разные `user_defined` записи для дойных перезапишут друг друга.

**Обходные пути:**

- Используйте `optimized` рационы: разные `pen` получают разные оптимизированные рационы через `RationOptimizer`.
- Запускайте отдельные прогоны для разных групп дойных.

### 9.6. Не найдена переменная в фильтре

Убедитесь, что:

- имя ключа точно совпадает с `variable_names_<timestamp>.txt`;
- вы ищете только часть `ClassName.function_name.variable_name` (не `values:` / `info_maps:`);
- регулярное выражение экранировано правильно (особенно точки `\.`);
- переменная действительно добавляется в пул (проверьте в `variable_names`).

---

## 10. Связь с DS-cattle-course / PACK-cattle-science

### 10.1. Разделение ролей: RuFaS vs AMTS

| Инструмент | Сильная сторона | Когда использовать |
|------------|-----------------|--------------------|
| **AMTS** | Детальное групповое рационирование по NASEM | Расчёт рационов для групп 15/1, интервенции в питании |
| **RuFaS** | Whole-farm динамика стада, сценарии, выбытие, воспроизводство | Прогноз молока на уровне стада, валидация по фактическим данным, оценка сценариев |

### 10.2. Рабочий пайплайн для CASE-002

1. **Baseline** RuFaS с параметрами фермы.
2. Сравнение predicted vs actual (молоко, DIM, жир, белок).
3. Калибровка кривой лактации через `lactation_curve_adjustment_inputs.json`.
4. **Интервенция** в AMTS (изменение рациона группы).
5. **Scenario-прогон** RuFaS с обновлённым рационом/параметрами.
6. Сравнение Δ predicted vs Δ actual.

### 10.3. Какие знания курса использовать

- **NASEM 2021 / CNCPS 2026** — понимание требований животных, разделения RDP/RUP, энергии (NEL, TDN).
- **Кривые лактации** — параметризация Wood и калибровка под ферму.
- **Структура стада** — паритеты, DIM, выбытие, воспроизводство.
- **Экономика** — цены на молоко, корма, выбывших животных.
- **Экология** — энтерический метан, выбросы от навоза, баланс азота.

### 10.4. Полезные источники внутри IWE

- Опыт интеграции с CASE-002: `/home/asus/IWE/RuFaS/PACK-integration/RuFaS-integration-notes.md`
- Нарративы onboarding-видео: `/home/asus/IWE/RuFaS/PACK-integration/YouTube-video/narratives/`
- Официальная вики: `/home/asus/IWE/RuFaS/docs/_src/_wiki/`
- Курс: `/home/asus/IWE/DS-cattle-course/`

---

## 11. Открытые вопросы

Ниже перечислены несоответствия или пробелы в источниках, которые нужно уточнять у команды RuFaS или проверять экспериментально.

1. **Флаг валидации только входных данных.** В разных источниках встречаются `-ov`, `--validate_only`, `--validate-only`. Точный синтаксис уточняйте через `python main.py -h`.
2. **Точное имя метода Output Manager для добавления переменных.** В транскриптах видео оно искажено (`om.report_variable`, `om.add_variable` и др.). Уточняйте в `RUFAS/output_manager.py`.
3. **Поддерживаемые версии Python.** Wiki и видео указывают 3.12/3.13, но в `pyproject.toml` для Black указаны `py310`, `py311` — это конфигурация форматера, а не runtime.
4. **Расшифровка идентификаторов уравнений.** Например, `NSM` в `A_NSM_1` не расшифрована в видео; ищите в научной документации.
5. **Data Origins.** На ноябрь 2024 реализован только для Animal Module; для остальных модулей — в разработке.
6. **Обработка навоза (Manure processing).** В onboarding-лекции указано, что часть функциональности находится в стадии разработки.
7. **Локальные правки vs PR.** Некоторые фиксы (например, `matplotlib.use("Agg")` или защита от `None` в EEE) являются локальными патчами; перед внесением в общий репозиторий нужен PR с тестами.
8. **Точные значения по умолчанию для `parallel_workers` и памяти.** Рекомендуется запускать с количеством воркеров, равным числу ядер, но при недостатке памяти уменьшать.

---

*Руководство составлено на основе:*

- `/home/asus/IWE/RuFaS/docs/_src/_wiki/` (все `.rst`, включая `_release_notes/`)
- `/home/asus/IWE/RuFaS/PACK-integration/YouTube-video/narratives/*.md`
- `/home/asus/IWE/RuFaS/PACK-integration/RuFaS-integration-notes.md`
