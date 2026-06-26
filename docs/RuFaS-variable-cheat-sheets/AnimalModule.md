# AnimalModule

Животноводческий модуль: демография стада, рационы, молоко, репродукция, навоз, продажи, события.

## Примеры regex-фильтров

```regex
^AnimalModuleReporter\.
```

## Демография популяции (исходная и текущая)

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_animal_population_statistics.population_breed` | unitless | Порода популяции |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_calves` | animals | Количество телят |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_heiferIs` | animals | Количество нетелей I |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_heiferIIs` | animals | Количество нетелей II |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_heiferIIIs` | animals | Количество нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_cows` | animals | Количество коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_replacement_heiferIIIS` | animals | Количество ремонтных нетелей III в популяции |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_lactating_cows` | animals | Количество лактирующих коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_dry_cows` | animals | Количество сухостойных коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_1_cows` | animals | Количество коров с паритетом 1 |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_2_cows` | animals | Количество коров с паритетом 2 |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_3_cows` | animals | Количество коров с паритетом 3 |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_4_cows` | animals | Количество коров с паритетом 4 |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_5_cows` | animals | Количество коров с паритетом 5 |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_6_or_more_cows` | animals | Количество коров с паритетом 6+ |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_calf_age` | day | Средний возраст телят |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferI_age` | day | Средний возраст нетелей I |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferII_age` | day | Средний возраст нетелей II |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferIII_age` | day | Средний возраст нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_age` | day | Средний возраст коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_replacement_age` | day | Средний возраст ремонтных нетелей |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_0.0_to_11.8` | animals | Количество телят в возрасте 0.0–11.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_11.8_to_23.6` | animals | Количество телят в возрасте 11.8–23.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_23.6_to_35.4` | animals | Количество телят в возрасте 23.6–35.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_35.4_to_47.2` | animals | Количество телят в возрасте 35.4–47.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_47.2_to_59.0` | animals | Количество телят в возрасте 47.2–59.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_60.0_to_123.8` | animals | Количество нетелей I в возрасте 60.0–123.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_123.8_to_187.6` | animals | Количество нетелей I в возрасте 123.8–187.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_187.6_to_251.4` | animals | Количество нетелей I в возрасте 187.6–251.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_251.4_to_315.2` | animals | Количество нетелей I в возрасте 251.4–315.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_315.2_to_379.0` | animals | Количество нетелей I в возрасте 315.2–379.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_380.0_to_450.6` | animals | Количество нетелей II в возрасте 380.0–450.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_450.6_to_521.2` | animals | Количество нетелей II в возрасте 450.6–521.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_521.2_to_591.8` | animals | Количество нетелей II в возрасте 521.2–591.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_591.8_to_662.4` | animals | Количество нетелей II в возрасте 591.8–662.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_662.4_to_733.0` | animals | Количество нетелей II в возрасте 662.4–733.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_648.0_to_671.8` | animals | Количество нетелей III в возрасте 648.0–671.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_671.8_to_695.6` | animals | Количество нетелей III в возрасте 671.8–695.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_695.6_to_719.4` | animals | Количество нетелей III в возрасте 695.6–719.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_719.4_to_743.2` | animals | Количество нетелей III в возрасте 719.4–743.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_743.2_to_767.0` | animals | Количество нетелей III в возрасте 743.2–767.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_672.0_to_985.8` | animals | Количество коров в возрасте 672.0–985.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_985.8_to_1299.6` | animals | Количество коров в возрасте 985.8–1299.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_1299.6_to_1613.4` | animals | Количество коров в возрасте 1299.6–1613.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_1613.4_to_1927.2` | animals | Количество коров в возрасте 1613.4–1927.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_1927.2_to_2241.0` | animals | Количество коров в возрасте 1927.2–2241.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_658.0_to_683.0` | animals | Количество ремонтных нетелей в возрасте 658.0–683.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_683.0_to_708.0` | animals | Количество ремонтных нетелей в возрасте 683.0–708.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_708.0_to_733.0` | animals | Количество ремонтных нетелей в возрасте 708.0–733.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_733.0_to_758.0` | animals | Количество ремонтных нетелей в возрасте 733.0–758.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_758.0_to_783.0` | animals | Количество ремонтных нетелей в возрасте 758.0–783.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_calf_body_weight` | kg | Средняя масса тела телят |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferI_body_weight` | kg | Средняя масса тела нетелей I |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferII_body_weight` | kg | Средняя масса тела нетелей II |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferIII_body_weight` | kg | Средняя масса тела нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_body_weight` | kg | Средняя масса тела коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_replacement_body_weight` | kg | Средняя масса тела ремонтных нетелей |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_days_in_pregnancy` | day | Средний срок беременности коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_days_in_milk` | day | Среднее количество дней в молоке у коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_parity` | unitless | Средний паритет коров |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_calving_interval` | day | Средний межотельный интервал коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_breed` | unitless | Порода популяции |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_calves` | animals | Исходное количество телят |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_heiferIs` | animals | Исходное количество нетелей I |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_heiferIIs` | animals | Исходное количество нетелей II |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_heiferIIIs` | animals | Исходное количество нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_cows` | animals | Исходное количество коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_replacement_heiferIIIS` | animals | Исходное количество ремонтных нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_lactating_cows` | animals | Исходное количество лактирующих коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_dry_cows` | animals | Исходное количество сухостойных коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_1_cows` | animals | Исходное количество коров с паритетом 1 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_2_cows` | animals | Исходное количество коров с паритетом 2 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_3_cows` | animals | Исходное количество коров с паритетом 3 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_4_cows` | animals | Исходное количество коров с паритетом 4 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_5_cows` | animals | Исходное количество коров с паритетом 5 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_6_or_more_cows` | animals | Исходное количество коров с паритетом 6+ |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_calf_age` | day | Исходный средний возраст телят |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferI_age` | day | Исходный средний возраст нетелей I |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferII_age` | day | Исходный средний возраст нетелей II |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferIII_age` | day | Исходный средний возраст нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_age` | day | Исходный средний возраст коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_replacement_age` | day | Исходный средний возраст ремонтных нетелей |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_7.0_to_17.0` | animals | Исходное количество телят в возрасте 7.0–17.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_17.0_to_27.0` | animals | Исходное количество телят в возрасте 17.0–27.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_27.0_to_37.0` | animals | Исходное количество телят в возрасте 27.0–37.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_37.0_to_47.0` | animals | Исходное количество телят в возрасте 37.0–47.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_47.0_to_57.0` | animals | Исходное количество телят в возрасте 47.0–57.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_65.0_to_127.8` | animals | Исходное количество нетелей I в возрасте 65.0–127.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_127.8_to_190.6` | animals | Исходное количество нетелей I в возрасте 127.8–190.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_190.6_to_253.4` | animals | Исходное количество нетелей I в возрасте 190.6–253.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_253.4_to_316.2` | animals | Исходное количество нетелей I в возрасте 253.4–316.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_316.2_to_379.0` | animals | Исходное количество нетелей I в возрасте 316.2–379.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_380.0_to_439.6` | animals | Исходное количество нетелей II в возрасте 380.0–439.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_439.6_to_499.2` | animals | Исходное количество нетелей II в возрасте 439.6–499.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_499.2_to_558.8` | animals | Исходное количество нетелей II в возрасте 499.2–558.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_558.8_to_618.4` | animals | Исходное количество нетелей II в возрасте 558.8–618.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_618.4_to_678.0` | animals | Исходное количество нетелей II в возрасте 618.4–678.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_655.0_to_669.0` | animals | Исходное количество нетелей III в возрасте 655.0–669.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_669.0_to_683.0` | animals | Исходное количество нетелей III в возрасте 669.0–683.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_683.0_to_697.0` | animals | Исходное количество нетелей III в возрасте 683.0–697.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_697.0_to_711.0` | animals | Исходное количество нетелей III в возрасте 697.0–711.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_711.0_to_725.0` | animals | Исходное количество нетелей III в возрасте 711.0–725.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_695.0_to_997.8` | animals | Исходное количество коров в возрасте 695.0–997.8 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_997.8_to_1300.6` | animals | Исходное количество коров в возрасте 997.8–1300.6 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_1300.6_to_1603.4` | animals | Исходное количество коров в возрасте 1300.6–1603.4 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_1603.4_to_1906.2` | animals | Исходное количество коров в возрасте 1603.4–1906.2 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_1906.2_to_2209.0` | animals | Исходное количество коров в возрасте 1906.2–2209.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_659.0_to_683.0` | animals | Исходное количество ремонтных нетелей в возрасте 659.0–683.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_683.0_to_707.0` | animals | Исходное количество ремонтных нетелей в возрасте 683.0–707.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_707.0_to_731.0` | animals | Исходное количество ремонтных нетелей в возрасте 707.0–731.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_731.0_to_755.0` | animals | Исходное количество ремонтных нетелей в возрасте 731.0–755.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_755.0_to_779.0` | animals | Исходное количество ремонтных нетелей в возрасте 755.0–779.0 дней |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_calf_body_weight` | kg | Исходная средняя масса тела телят |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferI_body_weight` | kg | Исходная средняя масса тела нетелей I |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferII_body_weight` | kg | Исходная средняя масса тела нетелей II |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferIII_body_weight` | kg | Исходная средняя масса тела нетелей III |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_body_weight` | kg | Исходная средняя масса тела коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_replacement_body_weight` | kg | Исходная средняя масса тела ремонтных нетелей |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_days_in_pregnancy` | day | Средний срок беременности коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_days_in_milk` | day | Среднее количество дней в молоке у коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_parity` | unitless | Средний паритет коров |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_calving_interval` | day | Средний межотельный интервал коров |

## Ежедневная численность и падеж

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_animal_population.sim_day` | simulation day | День симуляции |
| `AnimalModuleReporter.report_daily_animal_population.num_animals` | animals | Общее количество животных |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.CALF_deaths` | animals | Количество павших телят |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.HEIFER_I_deaths` | animals | Количество павших нетелей I |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.HEIFER_II_deaths` | animals | Количество павших нетелей II |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.HEIFER_III_deaths` | animals | Количество павших нетелей III |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.LAC_COW_deaths` | animals | Количество павших лактирующих коров |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.DRY_COW_deaths` | animals | Количество павших сухостойных коров |
| `AnimalModuleReporter.report_daily_animal_population.num_calves` | animals | Количество телят |
| `AnimalModuleReporter.report_daily_animal_population.num_heiferIs` | animals | Количество нетелей I |
| `AnimalModuleReporter.report_daily_animal_population.num_heiferIIs` | animals | Количество нетелей II |
| `AnimalModuleReporter.report_daily_animal_population.num_heiferIIIs` | animals | Количество нетелей III |
| `AnimalModuleReporter.report_daily_animal_population.num_lactating_cows` | animals | Количество лактирующих коров |
| `AnimalModuleReporter.report_daily_animal_population.num_dry_cows` | animals | Количество сухостойных коров |
| `AnimalModuleReporter.report_daily_animal_population.num_cows_total` | animals | Общее количество коров |

## Численность по pen

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_0_CALF` | animals | Количество животных в pen 0 (CALF) |
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_1_GROWING` | animals | Количество животных в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_2_CLOSE_UP` | animals | Количество животных в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_3_LAC_COW` | animals | Количество животных в pen 3 (LAC_COW) |

## Стадовые показатели

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_herd_statistics_data.sold_cow_oversupply_num` | animals | Количество проданных коров при перенаселении |
| `AnimalModuleReporter.report_herd_statistics_data.bought_heifer_num` | animals | Количество купленных нетелей |
| `AnimalModuleReporter.report_herd_statistics_data.sold_heiferII_num` | animals | Количество проданных нетелей II |
| `AnimalModuleReporter.report_herd_statistics_data.cow_herd_exit_num` | animals | Количество выбывших коров из стада |
| `AnimalModuleReporter.report_herd_statistics_data.sold_cow_num` | animals | Количество проданных коров |
| `AnimalModuleReporter.report_herd_statistics_data.GnRH_injection_num_h` | injection | Количество инъекций GnRH у нетелей |
| `AnimalModuleReporter.report_herd_statistics_data.GnRH_injection_num` | injection | Количество инъекций GnRH у коров |
| `AnimalModuleReporter.report_herd_statistics_data.PGF_injection_num` | injection | Количество инъекций PGF у коров |
| `AnimalModuleReporter.report_herd_statistics_data.PGF_injection_num_h` | injection | Количество инъекций PGF у нетелей |
| `AnimalModuleReporter.report_herd_statistics_data.ai_num` | AI | Количество осеменений у коров |
| `AnimalModuleReporter.report_herd_statistics_data.ai_num_h` | AI | Количество осеменений у нетелей |
| `AnimalModuleReporter.report_herd_statistics_data.preg_check_num` | preg check | Количество проверок стельности у коров |
| `AnimalModuleReporter.report_herd_statistics_data.preg_check_num_h` | preg check | Количество проверок стельности у нетелей |
| `AnimalModuleReporter.report_herd_statistics_data.num_heiferII_in_ed_period` | animals | Количество нетелей II в периоде эструса |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_in_ed_period` | animals | Количество коров в периоде эструса |
| `AnimalModuleReporter.report_herd_statistics_data.sold_calf_num` | animals | Количество проданных телят |
| `AnimalModuleReporter.report_herd_statistics_data.born_calf_num` | animals | Количество отелившихся телят |
| `AnimalModuleReporter.report_herd_statistics_data.stillborn_calf_num` | animals | Количество мертворождённых телят |
| `AnimalModuleReporter.report_herd_statistics_data.daily_milk_production` | kg/day | Суточный удой молока стада |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_fat_percent` | unitless | Средний процент жира в молоке стада |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_fat_kg` | kg/day | Суточная масса жира молока стада |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_protein_kg` | kg/day | Суточная масса белка молока стада |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_protein_percent` | percent | Средний процент белка в молоке стада |
| `AnimalModuleReporter.report_herd_statistics_data.open_cow_num` | animals | Количество открытых (неосеменённых) коров |
| `AnimalModuleReporter.report_herd_statistics_data.vwp_cow_num` | animals | Количество коров в волюционном периоде |
| `AnimalModuleReporter.report_herd_statistics_data.preg_cow_num` | animals | Количество стельных коров |
| `AnimalModuleReporter.report_herd_statistics_data.milking_cow_num` | animals | Количество доящихся коров |
| `AnimalModuleReporter.report_herd_statistics_data.dry_cow_num` | animals | Количество сухостойных коров |
| `AnimalModuleReporter.report_herd_statistics_data.avg_days_in_milk` | day | Среднее количество дней в молоке |
| `AnimalModuleReporter.report_herd_statistics_data.avg_days_in_preg` | day | Средний срок беременности |
| `AnimalModuleReporter.report_herd_statistics_data.avg_cow_body_weight` | kg | Средняя масса тела коров |
| `AnimalModuleReporter.report_herd_statistics_data.avg_parity_num` | unitless | Средний паритет коров |
| `AnimalModuleReporter.report_herd_statistics_data.avg_calving_interval` | day | Средний межотельный интервал |
| `AnimalModuleReporter.report_herd_statistics_data.avg_breeding_to_preg_time` | day | Среднее время от осеменения до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.avg_heifer_culling_age` | day | Средний возраст выбытия нетелей |
| `AnimalModuleReporter.report_herd_statistics_data.avg_cow_culling_age` | day | Средний возраст выбытия коров |
| `AnimalModuleReporter.report_herd_statistics_data.avg_mature_body_weight` | kg | Средняя масса тела взрослых животных |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_1` | animals | Количество коров с паритетом 1 |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_2` | animals | Количество коров с паритетом 2 |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_3` | animals | Количество коров с паритетом 3 |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_4` | animals | Количество коров с паритетом 4 |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_5` | animals | Количество коров с паритетом 5 |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_greater_than_5` | animals | Количество коров с паритетом 6+ |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_1` | day | Среднее время от отела до стельности для паритета 1 |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_2` | day | Среднее время от отела до стельности для паритета 2 |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_3` | day | Среднее время от отела до стельности для паритета 3 |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_4` | day | Среднее время от отела до стельности для паритета 4 |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_5` | day | Среднее время от отела до стельности для паритета 5 |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_greater_than_5` | day | Среднее время от отела до стельности для паритета 6+ |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_1` | day | Средний возраст при отеле для паритета 1 |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_2` | day | Средний возраст при отеле для паритета 2 |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_3` | day | Средний возраст при отеле для паритета 3 |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_4` | day | Средний возраст при отеле для паритета 4 |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_5` | day | Средний возраст при отеле для паритета 5 |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_greater_than_5` | day | Средний возраст при отеле для паритета 6+ |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for death` | unitless | Количество выбывших по причине смерти |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for herd resize` | unitless | Количество выбывших по причине перенаселения |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for lameness` | unitless | Количество выбывших по причине хромоты |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for injury` | unitless | Количество выбывших по причине травмы |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for mastitis` | unitless | Количество выбывших по причине мастита |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for disease` | unitless | Количество выбывших по причине болезни |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for udder` | unitless | Количество выбывших по причине вымя |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for unknown` | unitless | Количество выбывших по причине неизвестной причины |
| `AnimalModuleReporter.report_herd_statistics_data.heifer_average_daily_gain_in_pen_1` | kg/day | Среднесуточный прирост нетелей в pen 1 |
| `AnimalModuleReporter.report_herd_statistics_data.heiferI_average_daily_gain` | kg/day | Среднесуточный прирост нетелей I |
| `AnimalModuleReporter.report_herd_statistics_data.heiferII_average_daily_gain` | kg/day | Среднесуточный прирост нетелей II |
| `AnimalModuleReporter.report_herd_statistics_data.heiferIII_average_daily_gain` | kg/day | Среднесуточный прирост нетелей III |

## Рацион на голову

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CALF_PEN_0.202` | kg | Рацион на голову для pen CALF PEN 0, корм ID 202 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CALF_PEN_0.216` | kg | Рацион на голову для pen CALF PEN 0, корм ID 216 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CALF_PEN_0.dry_matter_intake_total` | kg | Суммарный сухой корм на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.44` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 44 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.50` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 50 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.95` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 95 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.104` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 104 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.110` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 110 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.301` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 301 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.302` | kg | Рацион на голову для pen GROWING PEN 1, корм ID 302 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.dry_matter_intake_total` | kg | Суммарный сухой корм на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.44` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 44 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.50` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 50 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.95` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 95 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.104` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 104 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.110` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 110 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.301` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 301 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.302` | kg | Рацион на голову для pen CLOSE UP PEN 2, корм ID 302 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.dry_matter_intake_total` | kg | Суммарный сухой корм на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.23` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 23 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.44` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 44 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.50` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 50 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.104` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 104 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.110` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 110 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.301` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 301 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.302` | kg | Рацион на голову для pen LAC COW PEN 3, корм ID 302 |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.dry_matter_intake_total` | kg | Суммарный сухой корм на голову в pen LAC COW PEN 3 |

## Питательные вещества рациона

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.dm` | kg/animal | Сухое вещество рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.CP` | kg/animal | Сырой протеин рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.ADF` | kg/animal | Кислотный детергентный волокон (ADF) рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NDF` | kg/animal | Нейтральный детергентный волокон (NDF) рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.lignin` | kg/animal | Лигнин рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.ash` | kg/animal | Зола рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.phosphorus` | kg/animal | Фосфор рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.potassium` | kg/animal | Калий рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.N` | kg/animal | Азот рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.as_fed` | kg/animal | Влажный корм (как есть) рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.EE` | kg/animal | Экстрактивный эфир (жир) рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.starch` | kg/animal | Крахмал рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.TDN` | kg/animal | Всего переваримых питательных веществ (TDN) рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.DE` | Mcal | Переваримая энергия рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.calcium` | kg/animal | Кальций рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.fat` | g | Жир рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.fat_percentage` | percent | Доля жира рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.forage_ndf` | kg | NDF из кормов рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.forage_ndf_percent` | percent of DM | Доля NDF из кормов рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.ME` | Mcal | Метаболизируемая энергия рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NE_maintenance_and_activity` | Mcal | Чистая энергия поддержания и активности рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NE_lactation` | Mcal | Чистая энергия лактации рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NE_growth` | Mcal | Чистая энергия роста рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.metabolizable_protein` | g | Метаболизируемый протеин рациона на голову в pen CALF PEN 0 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.dm` | kg/animal | Сухое вещество рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.CP` | kg/animal | Сырой протеин рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.ADF` | kg/animal | Кислотный детергентный волокон (ADF) рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NDF` | kg/animal | Нейтральный детергентный волокон (NDF) рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.lignin` | kg/animal | Лигнин рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.ash` | kg/animal | Зола рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.phosphorus` | kg/animal | Фосфор рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.potassium` | kg/animal | Калий рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.N` | kg/animal | Азот рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.as_fed` | kg/animal | Влажный корм (как есть) рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.EE` | kg/animal | Экстрактивный эфир (жир) рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.starch` | kg/animal | Крахмал рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.TDN` | kg/animal | Всего переваримых питательных веществ (TDN) рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.DE` | Mcal | Переваримая энергия рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.calcium` | kg/animal | Кальций рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.fat` | g | Жир рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.fat_percentage` | percent | Доля жира рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.forage_ndf` | kg | NDF из кормов рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.forage_ndf_percent` | percent of DM | Доля NDF из кормов рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.ME` | Mcal | Метаболизируемая энергия рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NE_maintenance_and_activity` | Mcal | Чистая энергия поддержания и активности рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NE_lactation` | Mcal | Чистая энергия лактации рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NE_growth` | Mcal | Чистая энергия роста рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.metabolizable_protein` | g | Метаболизируемый протеин рациона на голову в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.dm` | kg/animal | Сухое вещество рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.CP` | kg/animal | Сырой протеин рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.ADF` | kg/animal | Кислотный детергентный волокон (ADF) рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NDF` | kg/animal | Нейтральный детергентный волокон (NDF) рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.lignin` | kg/animal | Лигнин рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.ash` | kg/animal | Зола рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.phosphorus` | kg/animal | Фосфор рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.potassium` | kg/animal | Калий рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.N` | kg/animal | Азот рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.as_fed` | kg/animal | Влажный корм (как есть) рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.EE` | kg/animal | Экстрактивный эфир (жир) рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.starch` | kg/animal | Крахмал рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.TDN` | kg/animal | Всего переваримых питательных веществ (TDN) рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.DE` | Mcal | Переваримая энергия рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.calcium` | kg/animal | Кальций рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.fat` | g | Жир рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.fat_percentage` | percent | Доля жира рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.forage_ndf` | kg | NDF из кормов рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.forage_ndf_percent` | percent of DM | Доля NDF из кормов рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.ME` | Mcal | Метаболизируемая энергия рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NE_maintenance_and_activity` | Mcal | Чистая энергия поддержания и активности рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NE_lactation` | Mcal | Чистая энергия лактации рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NE_growth` | Mcal | Чистая энергия роста рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.metabolizable_protein` | g | Метаболизируемый протеин рациона на голову в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.dm` | kg/animal | Сухое вещество рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.CP` | kg/animal | Сырой протеин рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.ADF` | kg/animal | Кислотный детергентный волокон (ADF) рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NDF` | kg/animal | Нейтральный детергентный волокон (NDF) рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.lignin` | kg/animal | Лигнин рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.ash` | kg/animal | Зола рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.phosphorus` | kg/animal | Фосфор рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.potassium` | kg/animal | Калий рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.N` | kg/animal | Азот рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.as_fed` | kg/animal | Влажный корм (как есть) рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.EE` | kg/animal | Экстрактивный эфир (жир) рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.starch` | kg/animal | Крахмал рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.TDN` | kg/animal | Всего переваримых питательных веществ (TDN) рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.DE` | Mcal | Переваримая энергия рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.calcium` | kg/animal | Кальций рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.fat` | g | Жир рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.fat_percentage` | percent | Доля жира рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.forage_ndf` | kg | NDF из кормов рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.forage_ndf_percent` | percent of DM | Доля NDF из кормов рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.ME` | Mcal | Метаболизируемая энергия рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NE_maintenance_and_activity` | Mcal | Чистая энергия поддержания и активности рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NE_lactation` | Mcal | Чистая энергия лактации рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NE_growth` | Mcal | Чистая энергия роста рациона на голову в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.metabolizable_protein` | g | Метаболизируемый протеин рациона на голову в pen LAC COW PEN 3 |

## Метаболизируемая энергия рациона

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_me_diet.MEdiet_for_CALF_PEN_0` | Mcal | Метаболизируемая энергия рациона в pen CALF PEN 0 |
| `AnimalModuleReporter.report_me_diet.MEdiet_for_GROWING_PEN_1` | Mcal | Метаболизируемая энергия рациона в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_me_diet.MEdiet_for_CLOSE_UP_PEN_2` | Mcal | Метаболизируемая энергия рациона в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_me_diet.MEdiet_for_LAC_COW_PEN_3` | Mcal | Метаболизируемая энергия рациона в pen LAC COW PEN 3 |

## Средние потребности в нутриентах

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEmaint_requirement` | Mcal | Потребность в чистой энергии поддержания GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEa_requirement` | Mcal | Потребность в энергии активности GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEg_requirement` | Mcal | Потребность в чистой энергии роста GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEpreg_requirement` | Mcal | Потребность в чистой энергии беременности GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEl_requirement` | Mcal | Потребность в чистой энергии лактации GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.MP_requirement` | g | Потребность в метаболизируемом протеине GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.Ca_requirement` | g | Потребность в кальции GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.P_req` | g | Потребность в фосфоре (NASEM/NRC) GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.P_req_process` | g | Потребность в фосфоре (процессная модель) GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.DMIest_requirement` | kg | Оценочная потребность в сухом веществе GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.avg_BW` | kg | Средняя масса тела в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.avg_milk_production_reduction_pen` | kg/animal | Среднее снижение удоя в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.avg_essential_amino_acid_requirement` | g/day | Средняя потребность в незаменимых аминокислотах GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEmaint_requirement` | Mcal | Потребность в чистой энергии поддержания CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEa_requirement` | Mcal | Потребность в энергии активности CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEg_requirement` | Mcal | Потребность в чистой энергии роста CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEpreg_requirement` | Mcal | Потребность в чистой энергии беременности CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEl_requirement` | Mcal | Потребность в чистой энергии лактации CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.MP_requirement` | g | Потребность в метаболизируемом протеине CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.Ca_requirement` | g | Потребность в кальции CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.P_req` | g | Потребность в фосфоре (NASEM/NRC) CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.P_req_process` | g | Потребность в фосфоре (процессная модель) CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.DMIest_requirement` | kg | Оценочная потребность в сухом веществе CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.avg_BW` | kg | Средняя масса тела в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.avg_milk_production_reduction_pen` | kg/animal | Среднее снижение удоя в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.avg_essential_amino_acid_requirement` | g/day | Средняя потребность в незаменимых аминокислотах CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEmaint_requirement` | Mcal | Потребность в чистой энергии поддержания LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEa_requirement` | Mcal | Потребность в энергии активности LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEg_requirement` | Mcal | Потребность в чистой энергии роста LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEpreg_requirement` | Mcal | Потребность в чистой энергии беременности LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEl_requirement` | Mcal | Потребность в чистой энергии лактации LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.MP_requirement` | g | Потребность в метаболизируемом протеине LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.Ca_requirement` | g | Потребность в кальции LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.P_req` | g | Потребность в фосфоре (NASEM/NRC) LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.P_req_process` | g | Потребность в фосфоре (процессная модель) LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.DMIest_requirement` | kg | Оценочная потребность в сухом веществе LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.avg_BW` | kg | Средняя масса тела в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.avg_milk_production_reduction_pen` | kg/animal | Среднее снижение удоя в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.avg_essential_amino_acid_requirement` | g/day | Средняя потребность в незаменимых аминокислотах LAC COW PEN 3 |

## Оценка соответствия рациона потребностям

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.total_energy_difference` | Mcal | Разница по общей энергии (рацион − потребность) в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.maintenance_energy_difference` | Mcal | Разница по энергии поддержания в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.lactation_energy_difference` | Mcal | Разница по энергии лактации в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.growth_energy_difference` | Mcal | Разница по энергии роста в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.metabolizable_protein_difference` | g | Разница по метаболизируемому протеину в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.calcium_difference` | g | Разница по кальцию в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.phosphorus_difference` | g | Разница по фосфору в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.dry_matter_difference` | kg | Разница по сухому веществу в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.ndf_percent_difference` | percent | Разница по доле NDF в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.forage_ndf_percent_difference` | percent | Разница по доле NDF из кормов в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.fat_percent_difference` | percent | Разница по доле жира в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.is_valid_heifer_ration` | unitless | Корректность рациона для нетели в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.is_valid_cow_ration` | unitless | Корректность рациона для коровы в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.total_energy_acceptable` | unitless | Допустимость по общей энергии в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.maintenance_energy_acceptable` | unitless | Допустимость по энергии поддержания в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.lactation_energy_acceptable` | unitless | Допустимость по энергии лактации в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.growth_energy_acceptable` | unitless | Допустимость по энергии роста в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.metabolizable_protein_acceptable` | unitless | Допустимость по метаболизируемому протеину в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.calcium_acceptable` | unitless | Допустимость по кальцию в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.phosphorus_acceptable` | unitless | Допустимость по фосфору в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.dry_matter_acceptable` | unitless | Допустимость по сухому веществу в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.ndf_percent_acceptable` | unitless | Допустимость по доле NDF в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.forage_ndf_percent_acceptable` | unitless | Допустимость по доле NDF из кормов в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.fat_percent_acceptable` | unitless | Допустимость по доле жира в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.total_energy_difference` | Mcal | Разница по общей энергии (рацион − потребность) в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.maintenance_energy_difference` | Mcal | Разница по энергии поддержания в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.lactation_energy_difference` | Mcal | Разница по энергии лактации в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.growth_energy_difference` | Mcal | Разница по энергии роста в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.metabolizable_protein_difference` | g | Разница по метаболизируемому протеину в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.calcium_difference` | g | Разница по кальцию в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.phosphorus_difference` | g | Разница по фосфору в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.dry_matter_difference` | kg | Разница по сухому веществу в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.ndf_percent_difference` | percent | Разница по доле NDF в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.forage_ndf_percent_difference` | percent | Разница по доле NDF из кормов в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.fat_percent_difference` | percent | Разница по доле жира в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.is_valid_heifer_ration` | unitless | Корректность рациона для нетели в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.is_valid_cow_ration` | unitless | Корректность рациона для коровы в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.total_energy_acceptable` | unitless | Допустимость по общей энергии в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.maintenance_energy_acceptable` | unitless | Допустимость по энергии поддержания в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.lactation_energy_acceptable` | unitless | Допустимость по энергии лактации в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.growth_energy_acceptable` | unitless | Допустимость по энергии роста в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.metabolizable_protein_acceptable` | unitless | Допустимость по метаболизируемому протеину в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.calcium_acceptable` | unitless | Допустимость по кальцию в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.phosphorus_acceptable` | unitless | Допустимость по фосфору в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.dry_matter_acceptable` | unitless | Допустимость по сухому веществу в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.ndf_percent_acceptable` | unitless | Допустимость по доле NDF в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.forage_ndf_percent_acceptable` | unitless | Допустимость по доле NDF из кормов в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.fat_percent_acceptable` | unitless | Допустимость по доле жира в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.total_energy_difference` | Mcal | Разница по общей энергии (рацион − потребность) в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.maintenance_energy_difference` | Mcal | Разница по энергии поддержания в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.lactation_energy_difference` | Mcal | Разница по энергии лактации в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.growth_energy_difference` | Mcal | Разница по энергии роста в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.metabolizable_protein_difference` | g | Разница по метаболизируемому протеину в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.calcium_difference` | g | Разница по кальцию в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.phosphorus_difference` | g | Разница по фосфору в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.dry_matter_difference` | kg | Разница по сухому веществу в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.ndf_percent_difference` | percent | Разница по доле NDF в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.forage_ndf_percent_difference` | percent | Разница по доле NDF из кормов в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.fat_percent_difference` | percent | Разница по доле жира в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.is_valid_heifer_ration` | unitless | Корректность рациона для нетели в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.is_valid_cow_ration` | unitless | Корректность рациона для коровы в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.total_energy_acceptable` | unitless | Допустимость по общей энергии в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.maintenance_energy_acceptable` | unitless | Допустимость по энергии поддержания в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.lactation_energy_acceptable` | unitless | Допустимость по энергии лактации в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.growth_energy_acceptable` | unitless | Допустимость по энергии роста в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.metabolizable_protein_acceptable` | unitless | Допустимость по метаболизируемому протеину в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.calcium_acceptable` | unitless | Допустимость по кальцию в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.phosphorus_acceptable` | unitless | Допустимость по фосфору в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.dry_matter_acceptable` | unitless | Допустимость по сухому веществу в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.ndf_percent_acceptable` | unitless | Допустимость по доле NDF в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.forage_ndf_percent_acceptable` | unitless | Допустимость по доле NDF из кормов в pen LAC COW PEN 3 |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.fat_percent_acceptable` | unitless | Допустимость по доле жира в pen LAC COW PEN 3 |

## Суточный рацион по pen

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.202` | kg | Суточный расход корма ID 202 в pen 0 (CALF) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.216` | kg | Суточный расход корма ID 216 в pen 0 (CALF) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.dry_matter_intake_total` | kg | Суммарный сухой корм в pen 0 (CALF) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.byproducts_total` | kg | Суммарные побочные продукты в pen 0 (CALF) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.44` | kg | Суточный расход корма ID 44 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.50` | kg | Суточный расход корма ID 50 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.95` | kg | Суточный расход корма ID 95 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.104` | kg | Суточный расход корма ID 104 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.110` | kg | Суточный расход корма ID 110 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.301` | kg | Суточный расход корма ID 301 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.302` | kg | Суточный расход корма ID 302 в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.dry_matter_intake_total` | kg | Суммарный сухой корм в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.byproducts_total` | kg | Суммарные побочные продукты в pen 1 (GROWING) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.44` | kg | Суточный расход корма ID 44 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.50` | kg | Суточный расход корма ID 50 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.95` | kg | Суточный расход корма ID 95 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.104` | kg | Суточный расход корма ID 104 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.110` | kg | Суточный расход корма ID 110 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.301` | kg | Суточный расход корма ID 301 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.302` | kg | Суточный расход корма ID 302 в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.dry_matter_intake_total` | kg | Суммарный сухой корм в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.byproducts_total` | kg | Суммарные побочные продукты в pen 2 (CLOSE_UP) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.23` | kg | Суточный расход корма ID 23 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.44` | kg | Суточный расход корма ID 44 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.50` | kg | Суточный расход корма ID 50 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.104` | kg | Суточный расход корма ID 104 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.110` | kg | Суточный расход корма ID 110 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.301` | kg | Суточный расход корма ID 301 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.302` | kg | Суточный расход корма ID 302 в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.dry_matter_intake_total` | kg | Суммарный сухой корм в pen 3 (LAC_COW) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.byproducts_total` | kg | Суммарные побочные продукты в pen 3 (LAC_COW) |

## Суточный рацион по стаду

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.202` | kg | Суточный расход корма ID 202 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.216` | kg | Суточный расход корма ID 216 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.dry_matter_intake_total` | kg | Суммарный сухой корм по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.byproducts_total` | kg | Суммарные побочные продукты по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.44` | kg | Суточный расход корма ID 44 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.50` | kg | Суточный расход корма ID 50 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.95` | kg | Суточный расход корма ID 95 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.104` | kg | Суточный расход корма ID 104 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.110` | kg | Суточный расход корма ID 110 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.301` | kg | Суточный расход корма ID 301 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.302` | kg | Суточный расход корма ID 302 по всему стаду |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.23` | kg | Суточный расход корма ID 23 по всему стаду |

## Индивидуальные молочные данные

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.cow_id` | unitless | Идентификатор коровы |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.pen_id` | unitless | Идентификатор pen |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.is_milking` | unitless | Статус доения (True/False) |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.days_in_milk` | day | Дни в молоке |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.estimated_daily_milk_produced` | kg/day | Оценочный суточный удой |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_protein` | kg/day | Масса белка в молоке |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_fat` | kg/day | Масса жира в молоке |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_lactose` | kg/day | Масса лактозы в молоке |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.parity` | unitless | Паритет |

## 305-дневный удой

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_herd_mean` | kg | Средний 305-дневный удой по стаду |
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_l1_mean` | kg | Средний 305-дневный удой, 1-я лактация |
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_l2_mean` | kg | Средний 305-дневный удой, 2-я лактация |
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_l3plus_mean` | kg | Средний 305-дневный удой, 3+ лактация |

## Ежедневная репродукция

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_reproduction_statistics.num_successful_conceptions` | conception | Количество успешных оплодотворений |
| `AnimalModuleReporter.report_daily_reproduction_statistics.heiferII_num_successful_conceptions` | conception | Количество успешных оплодотворений у нетелей II |
| `AnimalModuleReporter.report_daily_reproduction_statistics.cow_num_successful_conceptions` | conception | Количество успешных оплодотворений у коров |

## Оплодотворяемость нетелок (heifer II)

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_total_num_ai_performed` | AI | Общее количество осеменений у нетелей II |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_total_num_successful_conceptions` | conception | Общее количество успешных оплодотворений у нетелей II |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_overall_conception_rate` | conceptions per service | Общая оплодотворяемость нетелей II |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_ai_performed_in_ED` | AI | Количество осеменений у нетелей II в естественном охоте |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_successful_conceptions_in_ED` | conception | Количество успешных оплодотворений у нетелей II в естественном охоте |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_ED_conception_rate` | conceptions per service | Оплодотворяемость нетелей II в естественном охоте |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_ai_performed_in_TAI` | AI | Количество осеменений у нетелей II по TAI |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_successful_conceptions_in_TAI` | conception | Количество успешных оплодотворений у нетелей II по TAI |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_TAI_conception_rate` | conceptions per service | Оплодотворяемость нетелей II по TAI |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_ai_performed_in_SynchED` | AI | Количество осеменений у нетелей II по SynchED |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_successful_conceptions_in_SynchED` | conception | Количество успешных оплодотворений у нетелей II по SynchED |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_SynchED_conception_rate` | conceptions per service | Оплодотворяемость нетелей II по SynchED |

## Оплодотворяемость коров

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter._record_cows_conception_rate.cow_total_num_ai_performed` | AI | Общее количество осеменений у коров |
| `AnimalModuleReporter._record_cows_conception_rate.cow_total_num_successful_conceptions` | conception | Общее количество успешных оплодотворений у коров |
| `AnimalModuleReporter._record_cows_conception_rate.cow_overall_conception_rate` | conceptions per service | Общая оплодотворяемость коров |

## Энтеральные выбросы метана

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_CALF_PEN_0` | g | Энтеральные выбросы метана в pen CALF PEN 0 |
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_GROWING_PEN_1` | g | Энтеральные выбросы метана в pen GROWING PEN 1 |
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_CLOSE_UP_PEN_2` | g | Энтеральные выбросы метана в pen CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_LAC_COW_PEN_3` | g | Энтеральные выбросы метана в pen LAC COW PEN 3 |

## Выделения навоза и мочи

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_urea` | g/L | Концентрация мочевины в моче (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_urine` | kg | Масса мочи (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_manure_total_ammoniacal_nitrogen` | kg | Общий аммиачный азот в навозе (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_urine_nitrogen` | kg | Азот в моче (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_manure_nitrogen` | kg | Азот в навозе (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_manure_mass` | kg | Масса навоза (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_total_solids` | kg | Общие сухие вещества (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_degradable_volatile_solids` | kg | Разлагаемые летучие сухие вещества (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_non_degradable_volatile_solids` | kg | Неразлагаемые летучие сухие вещества (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_organic_phosphorus_fraction` | unitless | Доля органического фосфора (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_non_water_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (без воды) (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_non_water_organic_phosphorus_fraction` | unitless | Доля органического фосфора (без воды) (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_phosphorus` | g | Фосфор (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_phosphorus_fraction` | unitless | Доля фосфора (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_potassium` | g | Калий (calf pen 0) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_urea` | g/L | Концентрация мочевины в моче (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_urine` | kg | Масса мочи (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_manure_total_ammoniacal_nitrogen` | kg | Общий аммиачный азот в навозе (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_urine_nitrogen` | kg | Азот в моче (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_manure_nitrogen` | kg | Азот в навозе (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_manure_mass` | kg | Масса навоза (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_total_solids` | kg | Общие сухие вещества (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_degradable_volatile_solids` | kg | Разлагаемые летучие сухие вещества (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_non_degradable_volatile_solids` | kg | Неразлагаемые летучие сухие вещества (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_organic_phosphorus_fraction` | unitless | Доля органического фосфора (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_non_water_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (без воды) (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_non_water_organic_phosphorus_fraction` | unitless | Доля органического фосфора (без воды) (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_phosphorus` | g | Фосфор (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_phosphorus_fraction` | unitless | Доля фосфора (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_potassium` | g | Калий (growing pen 1) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_urea` | g/L | Концентрация мочевины в моче (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_urine` | kg | Масса мочи (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_manure_total_ammoniacal_nitrogen` | kg | Общий аммиачный азот в навозе (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_urine_nitrogen` | kg | Азот в моче (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_manure_nitrogen` | kg | Азот в навозе (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_manure_mass` | kg | Масса навоза (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_total_solids` | kg | Общие сухие вещества (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_degradable_volatile_solids` | kg | Разлагаемые летучие сухие вещества (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_non_degradable_volatile_solids` | kg | Неразлагаемые летучие сухие вещества (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_organic_phosphorus_fraction` | unitless | Доля органического фосфора (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_non_water_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (без воды) (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_non_water_organic_phosphorus_fraction` | unitless | Доля органического фосфора (без воды) (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_phosphorus` | g | Фосфор (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_phosphorus_fraction` | unitless | Доля фосфора (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_potassium` | g | Калий (close up pen 2) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_urea` | g/L | Концентрация мочевины в моче (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_urine` | kg | Масса мочи (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_manure_total_ammoniacal_nitrogen` | kg | Общий аммиачный азот в навозе (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_urine_nitrogen` | kg | Азот в моче (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_manure_nitrogen` | kg | Азот в навозе (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_manure_mass` | kg | Масса навоза (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_total_solids` | kg | Общие сухие вещества (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_degradable_volatile_solids` | kg | Разлагаемые летучие сухие вещества (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_non_degradable_volatile_solids` | kg | Неразлагаемые летучие сухие вещества (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_organic_phosphorus_fraction` | unitless | Доля органического фосфора (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_non_water_inorganic_phosphorus_fraction` | unitless | Доля неорганического фосфора (без воды) (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_non_water_organic_phosphorus_fraction` | unitless | Доля органического фосфора (без воды) (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_phosphorus` | g | Фосфор (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_phosphorus_fraction` | unitless | Доля фосфора (lac cow pen 3) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_potassium` | g | Калий (lac cow pen 3) |

## Потоки навоза (масса, объём, питательные вещества)

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_manure_streams.water_calf_pen_CALF_PEN_0` | kg | Масса воды в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_calf_pen_CALF_PEN_0` | kg | Аммиачный азот в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.nitrogen_calf_pen_CALF_PEN_0` | kg | Азот в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.phosphorus_calf_pen_CALF_PEN_0` | kg | Фосфор в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.potassium_calf_pen_CALF_PEN_0` | kg | Калий в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.ash_calf_pen_CALF_PEN_0` | kg | Зола в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_calf_pen_CALF_PEN_0` | kg | Разлагаемые летучие сухие вещества в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_calf_pen_CALF_PEN_0` | kg | Неразлагаемые летучие сухие вещества в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_calf_pen_CALF_PEN_0` | kg | Неразлагаемые летучие сухие вещества подстилки в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.total_solids_calf_pen_CALF_PEN_0` | kg | Общие сухие вещества в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.volume_calf_pen_CALF_PEN_0` | m^3 | Объём потока CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_calf_pen_CALF_PEN_0` | m^3/kg | Потенциал производства метана в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_calf_pen_CALF_PEN_0` | kg | Общие летучие сухие вещества в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.mass_calf_pen_CALF_PEN_0` | kg | Масса потока CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_calf_pen_CALF_PEN_0` | kg | Общая масса подстилки в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_calf_pen_CALF_PEN_0` | m^3 | Общий объём подстилки в потоке CALF PEN 0 |
| `AnimalModuleReporter.report_manure_streams.water_grow_pen_GROWING_PEN_1` | kg | Масса воды в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_grow_pen_GROWING_PEN_1` | kg | Аммиачный азот в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.nitrogen_grow_pen_GROWING_PEN_1` | kg | Азот в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.phosphorus_grow_pen_GROWING_PEN_1` | kg | Фосфор в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.potassium_grow_pen_GROWING_PEN_1` | kg | Калий в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.ash_grow_pen_GROWING_PEN_1` | kg | Зола в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_grow_pen_GROWING_PEN_1` | kg | Разлагаемые летучие сухие вещества в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_grow_pen_GROWING_PEN_1` | kg | Неразлагаемые летучие сухие вещества в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_grow_pen_GROWING_PEN_1` | kg | Неразлагаемые летучие сухие вещества подстилки в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.total_solids_grow_pen_GROWING_PEN_1` | kg | Общие сухие вещества в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.volume_grow_pen_GROWING_PEN_1` | m^3 | Объём потока GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_grow_pen_GROWING_PEN_1` | m^3/kg | Потенциал производства метана в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_grow_pen_GROWING_PEN_1` | kg | Общие летучие сухие вещества в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.mass_grow_pen_GROWING_PEN_1` | kg | Масса потока GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_grow_pen_GROWING_PEN_1` | kg | Общая масса подстилки в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_grow_pen_GROWING_PEN_1` | m^3 | Общий объём подстилки в потоке GROWING PEN 1 |
| `AnimalModuleReporter.report_manure_streams.water_closeup_pen_CLOSE_UP_PEN_2` | kg | Масса воды в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_closeup_pen_CLOSE_UP_PEN_2` | kg | Аммиачный азот в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.nitrogen_closeup_pen_CLOSE_UP_PEN_2` | kg | Азот в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.phosphorus_closeup_pen_CLOSE_UP_PEN_2` | kg | Фосфор в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.potassium_closeup_pen_CLOSE_UP_PEN_2` | kg | Калий в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.ash_closeup_pen_CLOSE_UP_PEN_2` | kg | Зола в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Разлагаемые летучие сухие вещества в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Неразлагаемые летучие сухие вещества в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Неразлагаемые летучие сухие вещества подстилки в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.total_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Общие сухие вещества в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.volume_closeup_pen_CLOSE_UP_PEN_2` | m^3 | Объём потока CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_closeup_pen_CLOSE_UP_PEN_2` | m^3/kg | Потенциал производства метана в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Общие летучие сухие вещества в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.mass_closeup_pen_CLOSE_UP_PEN_2` | kg | Масса потока CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_closeup_pen_CLOSE_UP_PEN_2` | kg | Общая масса подстилки в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_closeup_pen_CLOSE_UP_PEN_2` | m^3 | Общий объём подстилки в потоке CLOSE UP PEN 2 |
| `AnimalModuleReporter.report_manure_streams.water_early_lac_parlor_PEN_3` | kg | Масса воды в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_early_lac_parlor_PEN_3` | kg | Аммиачный азот в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.nitrogen_early_lac_parlor_PEN_3` | kg | Азот в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.phosphorus_early_lac_parlor_PEN_3` | kg | Фосфор в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.potassium_early_lac_parlor_PEN_3` | kg | Калий в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.ash_early_lac_parlor_PEN_3` | kg | Зола в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_early_lac_parlor_PEN_3` | kg | Разлагаемые летучие сухие вещества в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_early_lac_parlor_PEN_3` | kg | Неразлагаемые летучие сухие вещества в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_early_lac_parlor_PEN_3` | kg | Неразлагаемые летучие сухие вещества подстилки в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_solids_early_lac_parlor_PEN_3` | kg | Общие сухие вещества в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.volume_early_lac_parlor_PEN_3` | m^3 | Объём потока PEN 3 |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_early_lac_parlor_PEN_3` | m^3/kg | Потенциал производства метана в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_early_lac_parlor_PEN_3` | kg | Общие летучие сухие вещества в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.mass_early_lac_parlor_PEN_3` | kg | Масса потока PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_early_lac_parlor_PEN_3` | kg | Общая масса подстилки в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_early_lac_parlor_PEN_3` | m^3 | Общий объём подстилки в потоке PEN 3 |
| `AnimalModuleReporter.report_manure_streams.water_early_lac_pen_LAC_COW_PEN_3` | kg | Масса воды в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_early_lac_pen_LAC_COW_PEN_3` | kg | Аммиачный азот в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.nitrogen_early_lac_pen_LAC_COW_PEN_3` | kg | Азот в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.phosphorus_early_lac_pen_LAC_COW_PEN_3` | kg | Фосфор в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.potassium_early_lac_pen_LAC_COW_PEN_3` | kg | Калий в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.ash_early_lac_pen_LAC_COW_PEN_3` | kg | Зола в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Разлагаемые летучие сухие вещества в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Неразлагаемые летучие сухие вещества в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Неразлагаемые летучие сухие вещества подстилки в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Общие сухие вещества в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.volume_early_lac_pen_LAC_COW_PEN_3` | m^3 | Объём потока LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_early_lac_pen_LAC_COW_PEN_3` | m^3/kg | Потенциал производства метана в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Общие летучие сухие вещества в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.mass_early_lac_pen_LAC_COW_PEN_3` | kg | Масса потока LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_early_lac_pen_LAC_COW_PEN_3` | kg | Общая масса подстилки в потоке LAC COW PEN 3 |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_early_lac_pen_LAC_COW_PEN_3` | m^3 | Общий объём подстилки в потоке LAC COW PEN 3 |

## Информация о проданных животных

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_sold_animal_information.animal_id` | unitless | Идентификатор животного |
| `AnimalModuleReporter.report_sold_animal_information.animal_type` | unitless | Тип животного |
| `AnimalModuleReporter.report_sold_animal_information.body_weight` | kg | Масса тела |
| `AnimalModuleReporter.report_sold_animal_information.sold_day` | simulation day | День продажи |
| `AnimalModuleReporter.report_sold_animal_information.cull_reason` | unitless | Причина выбытия |
| `AnimalModuleReporter.report_sold_animal_information.days_in_milk` | day | Дни в молоке |
| `AnimalModuleReporter.report_sold_animal_information.parity` | unitless | Паритет |
| `AnimalModuleReporter.report_sold_animal_information.genetic_history` | unitless | Генетическая история |

## Сводка по продажам

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_first_sell_event` | simulation day | Первый день продажи (телят) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_last_sell_event` | simulation day | Последний день продажи (телят) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_sold_count` | animals | Количество проданных (телят) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_sold_weight` | kg | Общая масса проданных (телят) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_first_sell_event` | simulation day | Первый день продажи (нетелей II) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_last_sell_event` | simulation day | Последний день продажи (нетелей II) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_sold_count` | animals | Количество проданных (нетелей II) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_sold_weight` | kg | Общая масса проданных (нетелей II) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_first_sell_event` | simulation day | Первый день продажи (нетелей III) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_last_sell_event` | simulation day | Последний день продажи (нетелей III) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_sold_count` | animals | Количество проданных (нетелей III) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_sold_weight` | kg | Общая масса проданных (нетелей III) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_first_sell_event` | simulation day | Первый день продажи (проданных и павших коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_last_sell_event` | simulation day | Последний день продажи (проданных и павших коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_sold_count` | animals | Количество проданных (проданных и павших коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_sold_weight` | kg | Общая масса проданных (проданных и павших коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_first_sell_event` | simulation day | Первый день продажи (проданных коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_last_sell_event` | simulation day | Последний день продажи (проданных коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_sold_count` | animals | Количество проданных (проданных коров) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_sold_weight` | kg | Общая масса проданных (проданных коров) |

## Мертворожденные

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_first_stillborn_event` | simulation day | Первый день мертворождений |
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_last_stillborn_event` | simulation day | Последний день мертворождений |
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_stillborn_count` | animals | Количество мертворождённых телят |
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_stillborn_birth_weight` | kg | Суммарная масса мертворождённых телят |

## Записи событий по животным

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13597_day_2556` | unitless | События нетели II ID 13597 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13601_day_2556` | unitless | События нетели II ID 13601 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13617_day_2556` | unitless | События нетели II ID 13617 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13622_day_2556` | unitless | События нетели II ID 13622 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13635_day_2556` | unitless | События нетели II ID 13635 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13636_day_2556` | unitless | События нетели II ID 13636 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13637_day_2556` | unitless | События нетели II ID 13637 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13638_day_2556` | unitless | События нетели II ID 13638 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13640_day_2556` | unitless | События нетели II ID 13640 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13645_day_2556` | unitless | События нетели II ID 13645 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13646_day_2556` | unitless | События нетели II ID 13646 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13647_day_2556` | unitless | События нетели II ID 13647 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13652_day_2556` | unitless | События нетели II ID 13652 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13659_day_2556` | unitless | События нетели II ID 13659 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13660_day_2556` | unitless | События нетели II ID 13660 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13667_day_2556` | unitless | События нетели II ID 13667 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13669_day_2556` | unitless | События нетели II ID 13669 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13670_day_2556` | unitless | События нетели II ID 13670 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13677_day_2556` | unitless | События нетели II ID 13677 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13679_day_2556` | unitless | События нетели II ID 13679 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13680_day_2556` | unitless | События нетели II ID 13680 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13685_day_2556` | unitless | События нетели II ID 13685 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13687_day_2556` | unitless | События нетели II ID 13687 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13688_day_2556` | unitless | События нетели II ID 13688 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13689_day_2556` | unitless | События нетели II ID 13689 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13697_day_2556` | unitless | События нетели II ID 13697 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13699_day_2556` | unitless | События нетели II ID 13699 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13701_day_2556` | unitless | События нетели II ID 13701 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13702_day_2556` | unitless | События нетели II ID 13702 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13704_day_2556` | unitless | События нетели II ID 13704 на день 2556 |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13705_day_2556` | unitless | События нетели II ID 13705 на день 2556 |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13109_day_2556` | unitless | События сухостойной коровы ID 13109 на день 2556 |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13465_day_2556` | unitless | События сухостойной коровы ID 13465 на день 2556 |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13290_day_2556` | unitless | События сухостойной коровы ID 13290 на день 2556 |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13510_day_2556` | unitless | События сухостойной коровы ID 13510 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13611_day_2556` | unitless | События лактирующей коровы ID 13611 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13392_day_2556` | unitless | События лактирующей коровы ID 13392 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13609_day_2556` | unitless | События лактирующей коровы ID 13609 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13614_day_2556` | unitless | События лактирующей коровы ID 13614 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13599_day_2556` | unitless | События лактирующей коровы ID 13599 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12338_day_2556` | unitless | События лактирующей коровы ID 12338 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13338_day_2556` | unitless | События лактирующей коровы ID 13338 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12413_day_2556` | unitless | События лактирующей коровы ID 12413 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13610_day_2556` | unitless | События лактирующей коровы ID 13610 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13607_day_2556` | unitless | События лактирующей коровы ID 13607 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12940_day_2556` | unitless | События лактирующей коровы ID 12940 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13234_day_2556` | unitless | События лактирующей коровы ID 13234 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13368_day_2556` | unitless | События лактирующей коровы ID 13368 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13277_day_2556` | unitless | События лактирующей коровы ID 13277 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13242_day_2556` | unitless | События лактирующей коровы ID 13242 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13602_day_2556` | unitless | События лактирующей коровы ID 13602 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13594_day_2556` | unitless | События лактирующей коровы ID 13594 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13586_day_2556` | unitless | События лактирующей коровы ID 13586 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13343_day_2556` | unitless | События лактирующей коровы ID 13343 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13223_day_2556` | unitless | События лактирующей коровы ID 13223 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13484_day_2556` | unitless | События лактирующей коровы ID 13484 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13589_day_2556` | unitless | События лактирующей коровы ID 13589 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12401_day_2556` | unitless | События лактирующей коровы ID 12401 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12390_day_2556` | unitless | События лактирующей коровы ID 12390 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13468_day_2556` | unitless | События лактирующей коровы ID 13468 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13196_day_2556` | unitless | События лактирующей коровы ID 13196 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13453_day_2556` | unitless | События лактирующей коровы ID 13453 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13565_day_2556` | unitless | События лактирующей коровы ID 13565 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13442_day_2556` | unitless | События лактирующей коровы ID 13442 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13461_day_2556` | unitless | События лактирующей коровы ID 13461 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13574_day_2556` | unitless | События лактирующей коровы ID 13574 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13334_day_2556` | unitless | События лактирующей коровы ID 13334 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13211_day_2556` | unitless | События лактирующей коровы ID 13211 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13576_day_2556` | unitless | События лактирующей коровы ID 13576 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13575_day_2556` | unitless | События лактирующей коровы ID 13575 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13448_day_2556` | unitless | События лактирующей коровы ID 13448 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13312_day_2556` | unitless | События лактирующей коровы ID 13312 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13186_day_2556` | unitless | События лактирующей коровы ID 13186 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13578_day_2556` | unitless | События лактирующей коровы ID 13578 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13190_day_2556` | unitless | События лактирующей коровы ID 13190 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13301_day_2556` | unitless | События лактирующей коровы ID 13301 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12975_day_2556` | unitless | События лактирующей коровы ID 12975 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13572_day_2556` | unitless | События лактирующей коровы ID 13572 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13454_day_2556` | unitless | События лактирующей коровы ID 13454 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13455_day_2556` | unitless | События лактирующей коровы ID 13455 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13566_day_2556` | unitless | События лактирующей коровы ID 13566 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13531_day_2556` | unitless | События лактирующей коровы ID 13531 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13571_day_2556` | unitless | События лактирующей коровы ID 13571 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13450_day_2556` | unitless | События лактирующей коровы ID 13450 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13562_day_2556` | unitless | События лактирующей коровы ID 13562 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13546_day_2556` | unitless | События лактирующей коровы ID 13546 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13559_day_2556` | unitless | События лактирующей коровы ID 13559 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13433_day_2556` | unitless | События лактирующей коровы ID 13433 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13555_day_2556` | unitless | События лактирующей коровы ID 13555 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13551_day_2556` | unitless | События лактирующей коровы ID 13551 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13550_day_2556` | unitless | События лактирующей коровы ID 13550 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13395_day_2556` | unitless | События лактирующей коровы ID 13395 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13096_day_2556` | unitless | События лактирующей коровы ID 13096 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13402_day_2556` | unitless | События лактирующей коровы ID 13402 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13435_day_2556` | unitless | События лактирующей коровы ID 13435 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13549_day_2556` | unitless | События лактирующей коровы ID 13549 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13429_day_2556` | unitless | События лактирующей коровы ID 13429 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13423_day_2556` | unitless | События лактирующей коровы ID 13423 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13525_day_2556` | unitless | События лактирующей коровы ID 13525 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13276_day_2556` | unitless | События лактирующей коровы ID 13276 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13537_day_2556` | unitless | События лактирующей коровы ID 13537 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13321_day_2556` | unitless | События лактирующей коровы ID 13321 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13323_day_2556` | unitless | События лактирующей коровы ID 13323 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13320_day_2556` | unitless | События лактирующей коровы ID 13320 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13424_day_2556` | unitless | События лактирующей коровы ID 13424 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13533_day_2556` | unitless | События лактирующей коровы ID 13533 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13403_day_2556` | unitless | События лактирующей коровы ID 13403 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13411_day_2556` | unitless | События лактирующей коровы ID 13411 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13530_day_2556` | unitless | События лактирующей коровы ID 13530 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13180_day_2556` | unitless | События лактирующей коровы ID 13180 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13521_day_2556` | unitless | События лактирующей коровы ID 13521 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13520_day_2556` | unitless | События лактирующей коровы ID 13520 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13527_day_2556` | unitless | События лактирующей коровы ID 13527 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13405_day_2556` | unitless | События лактирующей коровы ID 13405 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13497_day_2556` | unitless | События лактирующей коровы ID 13497 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13292_day_2556` | unitless | События лактирующей коровы ID 13292 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13511_day_2556` | unitless | События лактирующей коровы ID 13511 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13503_day_2556` | unitless | События лактирующей коровы ID 13503 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13380_day_2556` | unitless | События лактирующей коровы ID 13380 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13492_day_2556` | unitless | События лактирующей коровы ID 13492 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13483_day_2556` | unitless | События лактирующей коровы ID 13483 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13382_day_2556` | unitless | События лактирующей коровы ID 13382 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13482_day_2556` | unitless | События лактирующей коровы ID 13482 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13209_day_2556` | unitless | События лактирующей коровы ID 13209 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13352_day_2556` | unitless | События лактирующей коровы ID 13352 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13430_day_2556` | unitless | События лактирующей коровы ID 13430 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12433_day_2556` | unitless | События лактирующей коровы ID 12433 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13388_day_2556` | unitless | События лактирующей коровы ID 13388 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13374_day_2556` | unitless | События лактирующей коровы ID 13374 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13269_day_2556` | unitless | События лактирующей коровы ID 13269 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13383_day_2556` | unitless | События лактирующей коровы ID 13383 на день 2556 |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13619_day_2556` | unitless | События лактирующей коровы ID 13619 на день 2556 |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13523_day_2556` | unitless | События сухостойной коровы ID 13523 на день 2556 |
