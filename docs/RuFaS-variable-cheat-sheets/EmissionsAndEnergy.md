# Emissions & Energy

Оценка выбросов (купленные корма, изменение землепользования) и энергозатрат.

## Примеры regex-фильтров

```regex
^EmissionsEstimator\.
```
```regex
^EnergyEstimator\.
```

## Выбросы от кормов

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.202` | kg CO2 / kg DM | Корм/ингредиент с ID 202 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.44` | kg CO2 / kg DM | Корм/ингредиент с ID 44 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.50` | kg CO2 / kg DM | Корм/ингредиент с ID 50 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.95` | kg CO2 / kg DM | Корм/ингредиент с ID 95 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.104` | kg CO2 / kg DM | Корм/ингредиент с ID 104 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.110` | kg CO2 / kg DM | Корм/ингредиент с ID 110 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.302` | kg CO2 / kg DM | Корм/ингредиент с ID 302 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.purchased_feed_emissions.23` | kg CO2 / kg DM | Корм/ингредиент с ID 23 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.202` | kg CO2 / kg DM | Корм/ингредиент с ID 202 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.44` | kg CO2 / kg DM | Корм/ингредиент с ID 44 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.50` | kg CO2 / kg DM | Корм/ингредиент с ID 50 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.95` | kg CO2 / kg DM | Корм/ингредиент с ID 95 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.104` | kg CO2 / kg DM | Корм/ингредиент с ID 104 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.110` | kg CO2 / kg DM | Корм/ингредиент с ID 110 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.302` | kg CO2 / kg DM | Корм/ингредиент с ID 302 |
| `EmissionsEstimator.calculate_purchased_feed_emissions.land_use_change_emissions.23` | kg CO2 / kg DM | Корм/ингредиент с ID 23 |

## Энергозатраты

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `EnergyEstimator.estimate_all.total_diesel_consumption_tractor_implement` | L/ha | Суммарное значение |
