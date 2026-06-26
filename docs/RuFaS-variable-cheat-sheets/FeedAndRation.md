# Feed / Ration

Управление рационами: пользовательские рационы и ограничения оптимизатора.

## Примеры regex-фильтров

```regex
^RationManager\.
```
```regex
^RationOptimizer\.
```

## Пользовательские рационы

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `RationManager.set_user_defined_rations.user_defined_ration.ration` | percent | Словарь кормов и долей в пользовательском рационе |
| `RationManager.set_user_defined_rations.user_defined_ration.animal_combination` | percent | Комбинация животных для рациона |
| `RationManager.set_user_defined_rations.user_defined_ration.202` | percent | Доля корма ID 202 в пользовательском рационе |
| `RationManager.set_user_defined_rations.user_defined_ration.216` | percent | Доля корма ID 216 в пользовательском рационе |

## Оптимизатор и ограничения

| Переменная (полное имя для фильтра) | Единицы | Пояснение |
|---|---|---|
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.simulation day` | simulation day | День симуляции |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.attempt number` | unitless | Номер попытки подбора рациона |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.constraints_failed_dict` | unitless | Список нарушенных ограничений |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.ration_attempted` | unitless | Попытка составленного рациона (корм → кг) |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.pen requirements` | {'maintenance_energy': 'Mcal', 'growth_energy': 'Mcal', 'pregnancy_energy': 'Mcal', 'lactation_energy': 'Mcal', 'metabolizable_protein': 'g', 'calcium': 'g', 'phosphorus': 'g', 'process_based_phosphorus': 'g', 'dry_matter': 'kg', 'activity_energy': 'Mcal'} | Потребности pen в питательных веществах |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.initial_dry_matter_requirement` | kg | Начальная потребность в сухом веществе |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_1.initial_protein_requirement` | g | Начальная потребность в метаболизируемом протеине |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.simulation day` | simulation day | День симуляции |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.attempt number` | unitless | Номер попытки подбора рациона |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.constraints_failed_dict` | unitless | Список нарушенных ограничений |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.ration_attempted` | unitless | Попытка составленного рациона (корм → кг) |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.pen requirements` | {'maintenance_energy': 'Mcal', 'growth_energy': 'Mcal', 'pregnancy_energy': 'Mcal', 'lactation_energy': 'Mcal', 'metabolizable_protein': 'g', 'calcium': 'g', 'phosphorus': 'g', 'process_based_phosphorus': 'g', 'dry_matter': 'kg', 'activity_energy': 'Mcal'} | Потребности pen в питательных веществах |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.initial_dry_matter_requirement` | kg | Начальная потребность в сухом веществе |
| `RationOptimizer.handle_failed_constraints.failed_constraint_summary_for_pen_2.initial_protein_requirement` | g | Начальная потребность в метаболизируемом протеине |
