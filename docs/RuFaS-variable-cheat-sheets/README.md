# RuFaS — шпаргалки по выходным переменным

Эта папка содержит краткие справочники по переменным, которые выводит модель RuFaS.
Источник: `RuFaS/output/logs/animals_only_variable_names_26-Jun-2026_Fri_00-13-41.txt`.

## Как устроены фильтры

В папке `RuFaS/output/output_filters/` лежат текстовые файлы — по одному regex-паттерну на строку.
Каждая строка сравнивается с **полным именем переменной** (например, `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_fat`).
Если хотя бы один паттерн совпадает с именем переменной, переменная попадает в выходной файл.

## Как применять фильтр

1. Создайте файл в `RuFaS/output/output_filters/`, например `csv_animal.txt`.
2. Добавьте в него один или несколько regex-паттернов — каждый с новой строки.
3. Запустите симуляцию; имя файла фильтра обычно соответствует формату выходного файла.
   Например, `csv_animal.txt` выберет переменные, подходящие под паттерны, и запишет их в CSV.

## Примеры типичных фильтров

```regex
^AnimalModuleReporter\.
```
Выбирает все переменные животноводческого модуля.

```regex
^AnimalModuleReporter\.report_herd_statistics_data\.
```
Только стадовые показатели (удои, численность, статус репродукции и т.д.).

```regex
^AnimalModuleReporter\.report_milk\.
```
Только индивидуальные молочные данные.

```regex
^Weather\.
```
Все погодные переменные.

```regex
^RationManager\.|^RationOptimizer\.
```
Всё, что связано с рационами и их оптимизацией.

```regex
^EmissionsEstimator\.|^EnergyEstimator\.
```
Выбросы и энергопотребление.

## Список шпаргалок

- [TaskManager.md](TaskManager.md)
- [LactationCurve.md](LactationCurve.md)
- [AnimalModule.md](AnimalModule.md)
- [FeedAndRation.md](FeedAndRation.md)
- [EmissionsAndEnergy.md](EmissionsAndEnergy.md)
- [Weather.md](Weather.md)
- [RufasTime.md](RufasTime.md)

**Всего основных переменных:** 891

## Служебные производные поля

К некоторым переменным автоматически добавляются служебные поля:
`.timestamp`, `.units`, `.data_origin`, `.simulation_day`, `.prefix`.
В шпаргалках они не отображаются, но при необходимости их можно включить/исключить фильтрами:

```regex
\.timestamp$|\.units$|\.data_origin$|\.simulation_day$|\.prefix$
```
— выбрать только служебные производные.

```regex
^(?!.*\.(timestamp|units|data_origin|simulation_day|prefix)$).+
```
— исключить служебные производные (поведение по умолчанию в шпаргалках).

> Пометка `(?)` в графе «Пояснение» означает, что интерпретация имени переменной является разумным предположением.