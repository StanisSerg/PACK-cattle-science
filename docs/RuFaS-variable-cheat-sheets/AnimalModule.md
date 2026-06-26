# AnimalModule

Животноводческий модуль: демография стада, рационы, молоко, репродукция, навоз, продажи, события.

## Примеры regex-фильтров

```regex
^AnimalModuleReporter\.
```

## Демография популяции (исходная и текущая)

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_animal_population_statistics.population_breed` | unitless | Показатель популяции |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_calves` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_heiferIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_heiferIIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_heiferIIIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_replacement_heiferIIIS` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_lactating_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_dry_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_1_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_2_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_3_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_4_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_5_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.population_number_of_parity_6_or_more_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_calf_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferI_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferII_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferIII_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_replacement_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_0.0_to_11.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_11.8_to_23.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_23.6_to_35.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_35.4_to_47.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.population_calf_age_47.2_to_59.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_60.0_to_123.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_123.8_to_187.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_187.6_to_251.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_251.4_to_315.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferI_age_315.2_to_379.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_380.0_to_450.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_450.6_to_521.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_521.2_to_591.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_591.8_to_662.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferII_age_662.4_to_733.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_648.0_to_671.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_671.8_to_695.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_695.6_to_719.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_719.4_to_743.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.population_heiferIII_age_743.2_to_767.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_672.0_to_985.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_985.8_to_1299.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_1299.6_to_1613.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_1613.4_to_1927.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.population_cow_age_1927.2_to_2241.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_658.0_to_683.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_683.0_to_708.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_708.0_to_733.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_733.0_to_758.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_replacement_age_758.0_to_783.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_calf_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferI_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferII_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_heiferIII_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_replacement_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_days_in_pregnancy` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_days_in_milk` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_parity` | unitless | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.population_average_cow_calving_interval` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_breed` | unitless | Начальное (исходное) значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_calves` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_heiferIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_heiferIIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_heiferIIIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_replacement_heiferIIIS` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_lactating_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_dry_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_1_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_2_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_3_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_4_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_5_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.initial_number_of_parity_6_or_more_cows` | animals | Средний паритет |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_calf_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferI_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferII_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferIII_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_replacement_age` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_7.0_to_17.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_17.0_to_27.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_27.0_to_37.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_37.0_to_47.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_calf_age_47.0_to_57.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_65.0_to_127.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_127.8_to_190.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_190.6_to_253.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_253.4_to_316.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferI_age_316.2_to_379.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_380.0_to_439.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_439.6_to_499.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_499.2_to_558.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_558.8_to_618.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferII_age_618.4_to_678.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_655.0_to_669.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_669.0_to_683.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_683.0_to_697.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_697.0_to_711.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_heiferIII_age_711.0_to_725.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_695.0_to_997.8` | animals | Корм/ингредиент с ID 8 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_997.8_to_1300.6` | animals | Корм/ингредиент с ID 6 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_1300.6_to_1603.4` | animals | Корм/ингредиент с ID 4 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_1603.4_to_1906.2` | animals | Корм/ингредиент с ID 2 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_cow_age_1906.2_to_2209.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_659.0_to_683.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_683.0_to_707.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_707.0_to_731.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_731.0_to_755.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_replacement_age_755.0_to_779.0` | animals | Корм/ингредиент с ID 0 |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_calf_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferI_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferII_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_heiferIII_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_replacement_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_days_in_pregnancy` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_days_in_milk` | day | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_parity` | unitless | Средний возраст |
| `AnimalModuleReporter.report_animal_population_statistics.initial_average_cow_calving_interval` | day | Средний возраст |

## Ежедневная численность и падеж

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_animal_population.sim_day` | simulation day | День симуляции |
| `AnimalModuleReporter.report_daily_animal_population.num_animals` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.CALF_deaths` | animals | Выбытие/падеж |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.HEIFER_I_deaths` | animals | Выбытие/падеж |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.HEIFER_II_deaths` | animals | Выбытие/падеж |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.HEIFER_III_deaths` | animals | Выбытие/падеж |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.LAC_COW_deaths` | animals | Выбытие/падеж |
| `AnimalModuleReporter.report_daily_animal_population.AnimalType.DRY_COW_deaths` | animals | Выбытие/падеж |
| `AnimalModuleReporter.report_daily_animal_population.num_calves` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.num_heiferIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.num_heiferIIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.num_heiferIIIs` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.num_lactating_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.num_dry_cows` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_animal_population.num_cows_total` | animals | Среднее значение |

## Численность по pen

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_0_CALF` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_1_GROWING` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_2_CLOSE_UP` | animals | Среднее значение |
| `AnimalModuleReporter.report_daily_pen_total.number_of_animals_in_pen_3_LAC_COW` | animals | Среднее значение |

## Стадовые показатели

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_herd_statistics_data.sold_cow_oversupply_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.bought_heifer_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.sold_heiferII_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.cow_herd_exit_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.sold_cow_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.GnRH_injection_num_h` | injection | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.GnRH_injection_num` | injection | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.PGF_injection_num` | injection | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.PGF_injection_num_h` | injection | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.ai_num` | AI | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.ai_num_h` | AI | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.preg_check_num` | preg check | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.preg_check_num_h` | preg check | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.num_heiferII_in_ed_period` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_in_ed_period` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.sold_calf_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.born_calf_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.stillborn_calf_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.daily_milk_production` | kg/day | Суточный удой |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_fat_percent` | unitless | Жирность молока / жир молока |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_fat_kg` | kg/day | Жирность молока / жир молока |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_protein_kg` | kg/day | Белок молока |
| `AnimalModuleReporter.report_herd_statistics_data.herd_milk_protein_percent` | percent | Белок молока |
| `AnimalModuleReporter.report_herd_statistics_data.open_cow_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.vwp_cow_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.preg_cow_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.milking_cow_num` | animals | Средний молочный показатель |
| `AnimalModuleReporter.report_herd_statistics_data.dry_cow_num` | animals | Среднее значение |
| `AnimalModuleReporter.report_herd_statistics_data.avg_days_in_milk` | day | Средние дни лактации |
| `AnimalModuleReporter.report_herd_statistics_data.avg_days_in_preg` | day | Средние дни беременности |
| `AnimalModuleReporter.report_herd_statistics_data.avg_cow_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_herd_statistics_data.avg_parity_num` | unitless | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.avg_calving_interval` | day | Средний межотельный интервал |
| `AnimalModuleReporter.report_herd_statistics_data.avg_breeding_to_preg_time` | day | Среднее время от осеменения до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.avg_heifer_culling_age` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_cow_culling_age` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_mature_body_weight` | kg | Средняя масса тела |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_1` | animals | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_2` | animals | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_3` | animals | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_4` | animals | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_5` | animals | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.num_cow_for_parity_greater_than_5` | animals | Средний паритет |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_1` | day | Время от отела до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_2` | day | Время от отела до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_3` | day | Время от отела до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_4` | day | Время от отела до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_5` | day | Время от отела до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.calving_to_preg_time_greater_than_5` | day | Время от отела до стельности |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_1` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_2` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_3` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_4` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_5` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.avg_age_for_calving_greater_than_5` | day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for death` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for herd resize` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for lameness` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for injury` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for mastitis` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for disease` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for udder` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.cull_reason_stats.culled for unknown` | unitless | Выбытие/падеж |
| `AnimalModuleReporter.report_herd_statistics_data.heifer_average_daily_gain_in_pen_1` | kg/day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.heiferI_average_daily_gain` | kg/day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.heiferII_average_daily_gain` | kg/day | Средний возраст |
| `AnimalModuleReporter.report_herd_statistics_data.heiferIII_average_daily_gain` | kg/day | Средний возраст |

## Рацион на голову

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CALF_PEN_0.202` | kg | Корм/ингредиент с ID 202 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CALF_PEN_0.216` | kg | Корм/ингредиент с ID 216 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CALF_PEN_0.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.95` | kg | Корм/ингредиент с ID 95 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_GROWING_PEN_1.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.95` | kg | Корм/ингредиент с ID 95 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_CLOSE_UP_PEN_2.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.23` | kg | Корм/ингредиент с ID 23 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_ration_per_animal.ration_per_animal_for_LAC_COW_PEN_3.dry_matter_intake_total` | kg | Суммарное значение (kg) |

## Питательные вещества рациона

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.dm` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.CP` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.ADF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NDF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.lignin` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.ash` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.phosphorus` | kg/animal | Фосфор |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.potassium` | kg/animal | Калий |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.N` | kg/animal | Азот |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.as_fed` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.EE` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.starch` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.TDN` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.DE` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.calcium` | kg/animal | Кальций |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.fat` | g | (?) (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.fat_percentage` | percent | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.forage_ndf` | kg | Возраст (kg) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.forage_ndf_percent` | percent of DM | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.ME` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NE_maintenance_and_activity` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NE_lactation` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.NE_growth` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CALF_PEN_0.metabolizable_protein` | g | Протеин/белок (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.dm` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.CP` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.ADF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NDF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.lignin` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.ash` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.phosphorus` | kg/animal | Фосфор |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.potassium` | kg/animal | Калий |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.N` | kg/animal | Азот |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.as_fed` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.EE` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.starch` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.TDN` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.DE` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.calcium` | kg/animal | Кальций |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.fat` | g | (?) (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.fat_percentage` | percent | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.forage_ndf` | kg | Возраст (kg) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.forage_ndf_percent` | percent of DM | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.ME` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NE_maintenance_and_activity` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NE_lactation` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.NE_growth` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_GROWING_PEN_1.metabolizable_protein` | g | Протеин/белок (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.dm` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.CP` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.ADF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NDF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.lignin` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.ash` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.phosphorus` | kg/animal | Фосфор |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.potassium` | kg/animal | Калий |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.N` | kg/animal | Азот |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.as_fed` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.EE` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.starch` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.TDN` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.DE` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.calcium` | kg/animal | Кальций |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.fat` | g | (?) (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.fat_percentage` | percent | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.forage_ndf` | kg | Возраст (kg) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.forage_ndf_percent` | percent of DM | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.ME` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NE_maintenance_and_activity` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NE_lactation` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.NE_growth` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_CLOSE_UP_PEN_2.metabolizable_protein` | g | Протеин/белок (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.dm` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.CP` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.ADF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NDF` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.lignin` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.ash` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.phosphorus` | kg/animal | Фосфор |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.potassium` | kg/animal | Калий |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.N` | kg/animal | Азот |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.as_fed` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.EE` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.starch` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.TDN` | kg/animal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.DE` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.calcium` | kg/animal | Кальций |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.fat` | g | (?) (g) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.fat_percentage` | percent | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.forage_ndf` | kg | Возраст (kg) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.forage_ndf_percent` | percent of DM | Возраст |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.ME` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NE_maintenance_and_activity` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NE_lactation` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.NE_growth` | Mcal | (?) |
| `AnimalModuleReporter.report_nutrient_amounts.ration_nutrient_amount_for_LAC_COW_PEN_3.metabolizable_protein` | g | Протеин/белок (g) |

## Метаболизируемая энергия рациона

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_me_diet.MEdiet_for_CALF_PEN_0` | Mcal | Рацион/корм |
| `AnimalModuleReporter.report_me_diet.MEdiet_for_GROWING_PEN_1` | Mcal | Рацион/корм |
| `AnimalModuleReporter.report_me_diet.MEdiet_for_CLOSE_UP_PEN_2` | Mcal | Рацион/корм |
| `AnimalModuleReporter.report_me_diet.MEdiet_for_LAC_COW_PEN_3` | Mcal | Рацион/корм |

## Средние потребности в нутриентах

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEmaint_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEa_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEg_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEpreg_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.NEl_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.MP_requirement` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.Ca_requirement` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.P_req` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.P_req_process` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.DMIest_requirement` | kg | (?) (kg) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.avg_BW` | kg | Среднее значение (kg) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.avg_milk_production_reduction_pen` | kg/animal | Средний молочный показатель |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_GROWING_PEN_1.avg_essential_amino_acid_requirement` | g/day | Среднее значение |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEmaint_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEa_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEg_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEpreg_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.NEl_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.MP_requirement` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.Ca_requirement` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.P_req` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.P_req_process` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.DMIest_requirement` | kg | (?) (kg) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.avg_BW` | kg | Среднее значение (kg) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.avg_milk_production_reduction_pen` | kg/animal | Средний молочный показатель |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_CLOSE_UP_PEN_2.avg_essential_amino_acid_requirement` | g/day | Среднее значение |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEmaint_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEa_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEg_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEpreg_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.NEl_requirement` | Mcal | (?) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.MP_requirement` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.Ca_requirement` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.P_req` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.P_req_process` | g | (?) (g) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.DMIest_requirement` | kg | (?) (kg) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.avg_BW` | kg | Среднее значение (kg) |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.avg_milk_production_reduction_pen` | kg/animal | Средний молочный показатель |
| `AnimalModuleReporter.report_average_nutrient_requirements.avg_rqmts_for_LAC_COW_PEN_3.avg_essential_amino_acid_requirement` | g/day | Среднее значение |

## Оценка соответствия рациона потребностям

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.total_energy_difference` | Mcal | Суммарное значение |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.maintenance_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.lactation_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.growth_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.metabolizable_protein_difference` | g | Протеин/белок (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.calcium_difference` | g | Кальций (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.phosphorus_difference` | g | Фосфор (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.dry_matter_difference` | kg | (?) (kg) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.ndf_percent_difference` | percent | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.forage_ndf_percent_difference` | percent | Возраст |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_GROWING_PEN_1.fat_percent_difference` | percent | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.is_valid_heifer_ration` | unitless | Рацион/корм |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.is_valid_cow_ration` | unitless | Рацион/корм |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.total_energy_acceptable` | unitless | Суммарное значение |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.maintenance_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.lactation_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.growth_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.metabolizable_protein_acceptable` | unitless | Протеин/белок |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.calcium_acceptable` | unitless | Кальций |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.phosphorus_acceptable` | unitless | Фосфор |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.dry_matter_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.ndf_percent_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.forage_ndf_percent_acceptable` | unitless | Возраст |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_GROWING_PEN_1.fat_percent_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.total_energy_difference` | Mcal | Суммарное значение |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.maintenance_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.lactation_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.growth_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.metabolizable_protein_difference` | g | Протеин/белок (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.calcium_difference` | g | Кальций (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.phosphorus_difference` | g | Фосфор (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.dry_matter_difference` | kg | (?) (kg) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.ndf_percent_difference` | percent | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.forage_ndf_percent_difference` | percent | Возраст |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_CLOSE_UP_PEN_2.fat_percent_difference` | percent | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.is_valid_heifer_ration` | unitless | Рацион/корм |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.is_valid_cow_ration` | unitless | Рацион/корм |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.total_energy_acceptable` | unitless | Суммарное значение |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.maintenance_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.lactation_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.growth_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.metabolizable_protein_acceptable` | unitless | Протеин/белок |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.calcium_acceptable` | unitless | Кальций |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.phosphorus_acceptable` | unitless | Фосфор |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.dry_matter_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.ndf_percent_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.forage_ndf_percent_acceptable` | unitless | Возраст |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_CLOSE_UP_PEN_2.fat_percent_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.total_energy_difference` | Mcal | Суммарное значение |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.maintenance_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.lactation_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.growth_energy_difference` | Mcal | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.metabolizable_protein_difference` | g | Протеин/белок (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.calcium_difference` | g | Кальций (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.phosphorus_difference` | g | Фосфор (g) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.dry_matter_difference` | kg | (?) (kg) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.ndf_percent_difference` | percent | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.forage_ndf_percent_difference` | percent | Возраст |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_results_for_LAC_COW_PEN_3.fat_percent_difference` | percent | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.is_valid_heifer_ration` | unitless | Рацион/корм |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.is_valid_cow_ration` | unitless | Рацион/корм |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.total_energy_acceptable` | unitless | Суммарное значение |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.maintenance_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.lactation_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.growth_energy_acceptable` | unitless | Энергия |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.metabolizable_protein_acceptable` | unitless | Протеин/белок |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.calcium_acceptable` | unitless | Кальций |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.phosphorus_acceptable` | unitless | Фосфор |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.dry_matter_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.ndf_percent_acceptable` | unitless | (?) |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.forage_ndf_percent_acceptable` | unitless | Возраст |
| `AnimalModuleReporter.report_average_nutrient_evaluation_results.avg_eval_report_for_LAC_COW_PEN_3.fat_percent_acceptable` | unitless | (?) |

## Суточный рацион по pen

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.202` | kg | Корм/ингредиент с ID 202 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.216` | kg | Корм/ингредиент с ID 216 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_0_CALF.byproducts_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.95` | kg | Корм/ингредиент с ID 95 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_1_GROWING.byproducts_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.95` | kg | Корм/ингредиент с ID 95 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_2_CLOSE_UP.byproducts_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.23` | kg | Корм/ингредиент с ID 23 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_ration_per_pen.ration_daily_feed_totals_for_pen_3_LAC_COW.byproducts_total` | kg | Суммарное значение (kg) |

## Суточный рацион по стаду

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.202` | kg | Корм/ингредиент с ID 202 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.216` | kg | Корм/ингредиент с ID 216 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.dry_matter_intake_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.byproducts_total` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.44` | kg | Корм/ингредиент с ID 44 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.50` | kg | Корм/ингредиент с ID 50 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.95` | kg | Корм/ингредиент с ID 95 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.104` | kg | Корм/ингредиент с ID 104 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.110` | kg | Корм/ингредиент с ID 110 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.301` | kg | Корм/ингредиент с ID 301 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.302` | kg | Корм/ингредиент с ID 302 (kg) |
| `AnimalModuleReporter.report_daily_herd_total_ration.ration_daily_feed_total_across_pens.23` | kg | Корм/ингредиент с ID 23 (kg) |

## Индивидуальные молочные данные

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.cow_id` | unitless | (?) |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.pen_id` | unitless | (?) |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.is_milking` | unitless | Молочный показатель |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.days_in_milk` | day | Молочный показатель |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.estimated_daily_milk_produced` | kg/day | Суточный удой |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_protein` | kg/day | Белок молока |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_fat` | kg/day | Жирность молока / жир молока |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.milk_lactose` | kg/day | Лактоза молока |
| `AnimalModuleReporter.report_milk.milk_data_at_milk_update.parity` | unitless | Порядок отела (паритет) |

## 305-дневный удой

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_herd_mean` | kg | Удой молока (kg) |
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_l1_mean` | kg | Удой молока (kg) |
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_l2_mean` | kg | Удой молока (kg) |
| `AnimalModuleReporter.report_305_day_milk_yield.milk_305_day_yield_l3plus_mean` | kg | Удой молока (kg) |

## Ежедневная репродукция

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_daily_reproduction_statistics.num_successful_conceptions` | conception | Среднее значение |
| `AnimalModuleReporter.report_daily_reproduction_statistics.heiferII_num_successful_conceptions` | conception | Среднее значение |
| `AnimalModuleReporter.report_daily_reproduction_statistics.cow_num_successful_conceptions` | conception | Среднее значение |

## Оплодотворяемость нетелок (heifer II)

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_total_num_ai_performed` | AI | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_total_num_successful_conceptions` | conception | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_overall_conception_rate` | conceptions per service | Уровень оплодотворяемости |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_ai_performed_in_ED` | AI | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_successful_conceptions_in_ED` | conception | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_ED_conception_rate` | conceptions per service | Уровень оплодотворяемости |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_ai_performed_in_TAI` | AI | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_successful_conceptions_in_TAI` | conception | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_TAI_conception_rate` | conceptions per service | Уровень оплодотворяемости |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_ai_performed_in_SynchED` | AI | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_num_successful_conceptions_in_SynchED` | conception | Среднее значение |
| `AnimalModuleReporter._record_heiferIIs_conception_rate.heiferII_SynchED_conception_rate` | conceptions per service | Уровень оплодотворяемости |

## Оплодотворяемость коров

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter._record_cows_conception_rate.cow_total_num_ai_performed` | AI | Среднее значение |
| `AnimalModuleReporter._record_cows_conception_rate.cow_total_num_successful_conceptions` | conception | Среднее значение |
| `AnimalModuleReporter._record_cows_conception_rate.cow_overall_conception_rate` | conceptions per service | Уровень оплодотворяемости |

## Энтеральные выбросы метана

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_CALF_PEN_0` | g | Метан (g) |
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_GROWING_PEN_1` | g | Метан (g) |
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_CLOSE_UP_PEN_2` | g | Метан (g) |
| `AnimalModuleReporter.report_enteric_methane_emission.enteric_methane_emission_for_LAC_COW_PEN_3` | g | Метан (g) |

## Выделения навоза и мочи

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_urea` | g/L | Мочевина |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_urine` | kg | Моча (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_manure_total_ammoniacal_nitrogen` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_urine_nitrogen` | kg | Азот в моче (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_manure_nitrogen` | kg | Азот в навозе (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_manure_mass` | kg | Масса навоза |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_total_solids` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_non_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_non_water_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_non_water_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_phosphorus` | g | Фосфор (g) |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CALF_PEN_0_potassium` | g | Калий (g) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_urea` | g/L | Мочевина |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_urine` | kg | Моча (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_manure_total_ammoniacal_nitrogen` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_urine_nitrogen` | kg | Азот в моче (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_manure_nitrogen` | kg | Азот в навозе (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_manure_mass` | kg | Масса навоза |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_total_solids` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_non_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_non_water_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_non_water_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_phosphorus` | g | Фосфор (g) |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.GROWING_PEN_1_potassium` | g | Калий (g) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_urea` | g/L | Мочевина |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_urine` | kg | Моча (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_manure_total_ammoniacal_nitrogen` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_urine_nitrogen` | kg | Азот в моче (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_manure_nitrogen` | kg | Азот в навозе (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_manure_mass` | kg | Масса навоза |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_total_solids` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_non_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_non_water_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_non_water_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_phosphorus` | g | Фосфор (g) |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.CLOSE_UP_PEN_2_potassium` | g | Калий (g) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_urea` | g/L | Мочевина |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_urine` | kg | Моча (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_manure_total_ammoniacal_nitrogen` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_urine_nitrogen` | kg | Азот в моче (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_manure_nitrogen` | kg | Азот в навозе (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_manure_mass` | kg | Масса навоза |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_total_solids` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_non_degradable_volatile_solids` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_non_water_inorganic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_non_water_organic_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_phosphorus` | g | Фосфор (g) |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_phosphorus_fraction` | unitless | Фосфор |
| `AnimalModuleReporter.report_manure_excretions.LAC_COW_PEN_3_potassium` | g | Калий (g) |

## Потоки навоза (масса, объём, питательные вещества)

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_manure_streams.water_calf_pen_CALF_PEN_0` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_calf_pen_CALF_PEN_0` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.nitrogen_calf_pen_CALF_PEN_0` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.phosphorus_calf_pen_CALF_PEN_0` | kg | Фосфор (kg) |
| `AnimalModuleReporter.report_manure_streams.potassium_calf_pen_CALF_PEN_0` | kg | Калий (kg) |
| `AnimalModuleReporter.report_manure_streams.ash_calf_pen_CALF_PEN_0` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_calf_pen_CALF_PEN_0` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_calf_pen_CALF_PEN_0` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_calf_pen_CALF_PEN_0` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_solids_calf_pen_CALF_PEN_0` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.volume_calf_pen_CALF_PEN_0` | m^3 | (?) |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_calf_pen_CALF_PEN_0` | m^3/kg | Метан |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_calf_pen_CALF_PEN_0` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.mass_calf_pen_CALF_PEN_0` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_calf_pen_CALF_PEN_0` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_calf_pen_CALF_PEN_0` | m^3 | Суммарное значение |
| `AnimalModuleReporter.report_manure_streams.water_grow_pen_GROWING_PEN_1` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_grow_pen_GROWING_PEN_1` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.nitrogen_grow_pen_GROWING_PEN_1` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.phosphorus_grow_pen_GROWING_PEN_1` | kg | Фосфор (kg) |
| `AnimalModuleReporter.report_manure_streams.potassium_grow_pen_GROWING_PEN_1` | kg | Калий (kg) |
| `AnimalModuleReporter.report_manure_streams.ash_grow_pen_GROWING_PEN_1` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_grow_pen_GROWING_PEN_1` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_grow_pen_GROWING_PEN_1` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_grow_pen_GROWING_PEN_1` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_solids_grow_pen_GROWING_PEN_1` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.volume_grow_pen_GROWING_PEN_1` | m^3 | (?) |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_grow_pen_GROWING_PEN_1` | m^3/kg | Метан |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_grow_pen_GROWING_PEN_1` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.mass_grow_pen_GROWING_PEN_1` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_grow_pen_GROWING_PEN_1` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_grow_pen_GROWING_PEN_1` | m^3 | Суммарное значение |
| `AnimalModuleReporter.report_manure_streams.water_closeup_pen_CLOSE_UP_PEN_2` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_closeup_pen_CLOSE_UP_PEN_2` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.nitrogen_closeup_pen_CLOSE_UP_PEN_2` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.phosphorus_closeup_pen_CLOSE_UP_PEN_2` | kg | Фосфор (kg) |
| `AnimalModuleReporter.report_manure_streams.potassium_closeup_pen_CLOSE_UP_PEN_2` | kg | Калий (kg) |
| `AnimalModuleReporter.report_manure_streams.ash_closeup_pen_CLOSE_UP_PEN_2` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.volume_closeup_pen_CLOSE_UP_PEN_2` | m^3 | (?) |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_closeup_pen_CLOSE_UP_PEN_2` | m^3/kg | Метан |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_closeup_pen_CLOSE_UP_PEN_2` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.mass_closeup_pen_CLOSE_UP_PEN_2` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_closeup_pen_CLOSE_UP_PEN_2` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_closeup_pen_CLOSE_UP_PEN_2` | m^3 | Суммарное значение |
| `AnimalModuleReporter.report_manure_streams.water_early_lac_parlor_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_early_lac_parlor_PEN_3` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.nitrogen_early_lac_parlor_PEN_3` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.phosphorus_early_lac_parlor_PEN_3` | kg | Фосфор (kg) |
| `AnimalModuleReporter.report_manure_streams.potassium_early_lac_parlor_PEN_3` | kg | Калий (kg) |
| `AnimalModuleReporter.report_manure_streams.ash_early_lac_parlor_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_early_lac_parlor_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_early_lac_parlor_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_early_lac_parlor_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_solids_early_lac_parlor_PEN_3` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.volume_early_lac_parlor_PEN_3` | m^3 | (?) |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_early_lac_parlor_PEN_3` | m^3/kg | Метан |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_early_lac_parlor_PEN_3` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.mass_early_lac_parlor_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_early_lac_parlor_PEN_3` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_early_lac_parlor_PEN_3` | m^3 | Суммарное значение |
| `AnimalModuleReporter.report_manure_streams.water_early_lac_pen_LAC_COW_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.ammoniacal_nitrogen_early_lac_pen_LAC_COW_PEN_3` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.nitrogen_early_lac_pen_LAC_COW_PEN_3` | kg | Азот (kg) |
| `AnimalModuleReporter.report_manure_streams.phosphorus_early_lac_pen_LAC_COW_PEN_3` | kg | Фосфор (kg) |
| `AnimalModuleReporter.report_manure_streams.potassium_early_lac_pen_LAC_COW_PEN_3` | kg | Калий (kg) |
| `AnimalModuleReporter.report_manure_streams.ash_early_lac_pen_LAC_COW_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.degradable_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.non_degradable_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.bedding_non_degradable_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.volume_early_lac_pen_LAC_COW_PEN_3` | m^3 | (?) |
| `AnimalModuleReporter.report_manure_streams.methane_production_potential_early_lac_pen_LAC_COW_PEN_3` | m^3/kg | Метан |
| `AnimalModuleReporter.report_manure_streams.total_volatile_solids_early_lac_pen_LAC_COW_PEN_3` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.mass_early_lac_pen_LAC_COW_PEN_3` | kg | (?) (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_mass_early_lac_pen_LAC_COW_PEN_3` | kg | Суммарное значение (kg) |
| `AnimalModuleReporter.report_manure_streams.total_bedding_volume_early_lac_pen_LAC_COW_PEN_3` | m^3 | Суммарное значение |

## Информация о проданных животных

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_sold_animal_information.animal_id` | unitless | (?) |
| `AnimalModuleReporter.report_sold_animal_information.animal_type` | unitless | (?) |
| `AnimalModuleReporter.report_sold_animal_information.body_weight` | kg | Масса тела |
| `AnimalModuleReporter.report_sold_animal_information.sold_day` | simulation day | Проданные животные |
| `AnimalModuleReporter.report_sold_animal_information.cull_reason` | unitless | Причина выбытия |
| `AnimalModuleReporter.report_sold_animal_information.days_in_milk` | day | Молочный показатель |
| `AnimalModuleReporter.report_sold_animal_information.parity` | unitless | Порядок отела (паритет) |
| `AnimalModuleReporter.report_sold_animal_information.genetic_history` | unitless | Генетическая история |

## Сводка по продажам

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_first_sell_event` | simulation day | Дата события продажи |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_last_sell_event` | simulation day | Дата события продажи |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_sold_count` | animals | Количество проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_calves_sold_weight` | kg | Масса проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_first_sell_event` | simulation day | (?) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_last_sell_event` | simulation day | (?) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_sold_count` | animals | Количество проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferII_sold_weight` | kg | Масса проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_first_sell_event` | simulation day | (?) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_last_sell_event` | simulation day | (?) |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_sold_count` | animals | Количество проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.heiferIII_sold_weight` | kg | Масса проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_first_sell_event` | simulation day | Дата события продажи |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_last_sell_event` | simulation day | Дата события продажи |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_sold_count` | animals | Количество проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_and_died_cows_sold_weight` | kg | Масса проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_first_sell_event` | simulation day | Дата события продажи |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_last_sell_event` | simulation day | Дата события продажи |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_sold_count` | animals | Количество проданных |
| `AnimalModuleReporter.report_sold_animal_information_sort_by_sell_day.sold_cows_sold_weight` | kg | Масса проданных |

## Мертворожденные

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_first_stillborn_event` | simulation day | Мертворожденные |
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_last_stillborn_event` | simulation day | Мертворожденные |
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_stillborn_count` | animals | Мертворожденные |
| `AnimalModuleReporter.report_stillborn_calves_information.stillborn_calves_stillborn_birth_weight` | kg | Мертворожденные (kg) |

## Записи событий по животным

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13597_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13601_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13617_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13622_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13635_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13636_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13637_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13638_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13640_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13645_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13646_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13647_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13652_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13659_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13660_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13667_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13669_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13670_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13677_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13679_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13680_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13685_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13687_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13688_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13689_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13697_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13699_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13701_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13702_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13704_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.HEIFER_II_13705_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13109_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13465_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13290_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13510_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13611_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13392_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13609_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13614_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13599_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12338_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13338_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12413_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13610_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13607_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12940_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13234_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13368_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13277_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13242_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13602_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13594_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13586_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13343_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13223_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13484_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13589_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12401_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12390_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13468_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13196_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13453_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13565_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13442_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13461_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13574_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13334_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13211_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13576_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13575_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13448_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13312_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13186_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13578_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13190_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13301_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12975_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13572_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13454_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13455_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13566_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13531_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13571_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13450_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13562_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13546_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13559_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13433_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13555_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13551_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13550_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13395_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13096_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13402_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13435_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13549_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13429_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13423_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13525_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13276_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13537_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13321_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13323_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13320_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13424_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13533_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13403_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13411_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13530_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13180_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13521_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13520_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13527_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13405_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13497_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13292_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13511_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13503_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13380_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13492_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13483_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13382_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13482_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13209_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13352_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13430_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_12433_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13388_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13374_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13269_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13383_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.LAC_COW_13619_day_2556` | unitless | (?) |
| `AnimalModuleReporter._record_animal_events.DRY_COW_13523_day_2556` | unitless | (?) |
