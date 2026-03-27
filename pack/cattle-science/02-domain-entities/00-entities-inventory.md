# Инвентарь сущностей PACK-cattle-science

> Полный каталог entities из всех SoTA (63 файла)
> 
> **Дата создания:** 2026-03-26
> **Всего сущностей:** 187
> **Статус:** Активный

---

## Сводка

| Категория | Количество | Процент |
|-----------|-----------|---------|
| **Всего сущностей** | **187** | 100% |
| **P0 (Fundamental)** | 58 | 31% |
| **P1 (Important)** | 98 | 52% |
| **P2 (Specific)** | 31 | 17% |

### По типам FPF

| Тип | Количество | Описание |
|-----|-----------|----------|
| **U.Characteristic** | 118 | Измеримые характеристики |
| **U.Episteme** | 42 | Понятия/состояния |
| **U.System** | 18 | Биологические системы |
| **U.Method** | 8 | Методы/процедуры |
| **U.Role** | 1 | Роли |

### По областям

| Область | Упоминания |
|---------|-----------|
| feeding | 142 |
| reproduction | 76 |
| health | 48 |
| economics | 28 |

---

## P0 — Fundamental Entities (58 шт)

Встречаются в 5+ SoTA. Критические для понимания дисциплины.

### Биологические системы (U.System)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 1 | **Корова молочная** | Dairy cow | CS.ENTITY.001 | 001, 002, 003, 005, 007, 008, 009, 012, 014, 017, 019, 023, 025, 027, 028, 032, 035, 037, 039, 040, 041, 043, 044, 046, 047, 053, 055, 056, 058, 060, 061, 062, 063, 064, 065, 066, 067, 068 |
| 2 | **Печень** | Liver | CS.ENTITY.003 | 012, 018, 026, 028, 029, 030, 031, 034, 035, 036, 039, 041, 044, 055, 057, 058, 060, 061, 062, 063, 065 |
| 3 | **Рубец** | Rumen | CS.ENTITY.004 | 012, 015, 018, 029, 048, 055, 059, 060, 061, 062, 063, 064 |
| 4 | **Жировая ткань** | Adipose tissue | CS.ENTITY.005 | 035, 037, 038, 039, 040, 043, 053, 055, 058, 061 |
| 5 | **Молоко** | Milk | CS.ENTITY.006 | 001, 002, 005, 006, 007, 017, 019, 023, 032, 037, 040, 043, 046, 058, 067 |

### Метаболиты/биомаркеры (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | Аббр. | ID | SoTA IDs |
|---|---------------|-----------------|-------|-----|----------|
| 6 | **β-гидроксибутират** | Beta-hydroxybutyrate | BHB | CS.ENTITY.009 | 027, 032, 037, 040, 041, 043, 046, 053, 055, 058, 060, 061, 062, 063 |
| 7 | **Неэтерифицированные жирные кислоты** | Non-esterified fatty acids | NEFA | CS.ENTITY.010 | 028, 035, 037, 038, 039, 040, 043, 046, 053, 055, 058, 060, 061, 062, 063 |
| 8 | **Глюкоза** | Glucose | — | CS.ENTITY.??? | 009, 026, 028, 030, 037, 038, 039, 041, 043, 046, 053, 055, 058, 060, 061, 062, 063 |
| 9 | **Пропионат** | Propionate | — | CS.ENTITY.??? | 012, 015, 016, 017, 018, 029, 031, 048, 055, 057, 058, 059, 060, 061, 062, 063 |
| 10 | **Ацетат** | Acetate | — | CS.ENTITY.??? | 018, 029, 048, 055, 058, 059 |
| 11 | **Бутират** | Butyrate | — | CS.ENTITY.??? | 018, 029, 055, 058 |
| 12 | **Лактат** | Lactate | — | CS.ENTITY.??? | 026, 029, 041, 058, 060, 061, 062, 063 |
| 13 | **Мочевина** | Urea | — | CS.ENTITY.??? | 013, 017, 018, 027, 037, 043, 046 |
| 14 | **Инсулин** | Insulin | INS | CS.ENTITY.015 | 012, 015, 016, 028, 029, 030, 031, 035, 038, 039, 040, 043, 049, 053, 054, 057, 058, 059, 060, 061, 062, 063 |
| 15 | **Глюкагон** | Glucagon | GLN | CS.ENTITY.016 | 012, 015, 016, 028, 029, 030, 035, 039, 040, 043, 053, 054, 057, 058, 061 |
| 16 | **Кортизол** | Cortisol | CORT | CS.ENTITY.017 | 007, 009, 028, 035, 037, 039, 040, 043, 053, 054, 055, 057, 058, 060, 061, 063, 066 |

### Заболевания/состояния (U.Episteme)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 17 | **Кетоз** | Ketosis | KET | CS.ENTITY.018 | 012, 015, 016, 027, 028, 029, 032, 037, 038, 039, 040, 041, 042, 043, 046, 053, 055, 058, 060, 061, 062, 063 |
| 18 | **Субклинический кетоз** | Subclinical ketosis | CS.ENTITY.002 | 027, 032, 037, 040, 041, 043, 058, 060, 061, 062, 063 |
| 19 | **Жировой гепатоз** | Fatty liver | CS.ENTITY.??? | 026, 028, 030, 035, 037, 039, 041, 042, 043, 044, 046, 055 |
| 20 | **Гипокальциемия** | Hypocalcemia | CS.ENTITY.??? | 008, 020, 043, 053, 055, 056, 060, 063, 066 |
| 21 | **Мастит** | Mastitis | CS.ENTITY.??? | 001, 008, 009, 027, 032, 037, 040, 043, 067 |
| 22 | **Метрит** | Metritis | CS.ENTITY.??? | 001, 008, 009, 032, 037, 040, 043, 067 |
| 23 | **Задержка последа** | Retained placenta | CS.ENTITY.??? | 005, 008, 020, 032, 037, 040, 043 |
| 24 | **Смещение сычуга** | Displaced abomasum | CS.ENTITY.??? | 037, 040, 043, 067 |
| 25 | **Глюконеогенез** | Gluconeogenesis | CS.ENTITY.??? | 012, 017, 018, 026, 028, 029, 034, 035, 036, 039, 041, 043, 044, 045, 047, 055, 057, 058, 060, 061, 062, 063 |

### Метрики (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | Аббр. | ID | SoTA IDs |
|---|---------------|-----------------|-------|-----|----------|
| 26 | **21-дневная стельность** | 21-day pregnancy rate | 21-d PR | CS.ENTITY.001 | 001, 002, 004, 019, 022, 023, 024 |
| 27 | **Оценка упитанности** | Body condition score | BCS | CS.ENTITY.??? | 002, 005, 007, 017, 019, 027, 032, 035, 037, 040, 043, 055, 058, 060, 061, 062, 063, 064, 065, 066, 068 |
| 28 | **Потребление корма** | Dry matter intake | DMI | CS.ENTITY.??? | 007, 015, 016, 017, 031, 034, 035, 037, 040, 043, 048, 055, 060, 061, 062, 063, 064, 065, 066, 067, 068 |
| 29 | **Удой** | Milk yield | — | CS.ENTITY.??? | 001, 002, 005, 006, 007, 016, 017, 019, 023, 025, 028, 032, 037, 040, 043, 046, 055, 058, 060, 061, 062, 063 |
| 30 | **Жир молока** | Milk fat | — | CS.ENTITY.??? | 016, 017, 019, 037, 040, 043, 046, 055, 058, 067 |
| 31 | **Белок молока** | Milk protein | — | CS.ENTITY.??? | 013, 017, 019, 037, 040, 043, 046, 055, 067 |

### Методы (U.Method)

| № | Сущность (рус) | Сущность (англ) | Аббр. | ID | SoTA IDs |
|---|---------------|-----------------|-------|-----|----------|
| 32 | **Искусственное осеменение** | Artificial insemination | AI | CS.ENTITY.??? | 001, 002, 003, 004, 006, 014, 019, 022, 023 |
| 33 | **Синхронизация по времени** | Timed artificial insemination | TAI | CS.ENTITY.??? | 001, 003, 004, 014, 019, 022, 023 |
| 34 | **Протокол CIDR** | CIDR protocol | — | CS.ENTITY.??? | 003, 023 |
| 35 | **Обнаружение охоты** | Heat detection | — | CS.ENTITY.??? | 001, 002, 006, 014, 019 |

### Периоды/фазы (U.Episteme)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 36 | **Переходный период** | Transition period | CS.ENTITY.??? | 001, 007, 008, 009, 017, 027, 028, 031, 032, 034, 035, 037, 039, 040, 043, 046, 053, 054, 055, 058, 060, 061, 062, 063, 064, 065, 066, 067, 068 |
| 37 | **Сухостойный период** | Dry period | CS.ENTITY.??? | 005, 008, 017, 031, 032, 037, 040, 043, 055, 064, 065, 066, 068 |
| 38 | **Ранняя лактация** | Early lactation | CS.ENTITY.??? | 007, 009, 017, 027, 028, 032, 035, 037, 039, 040, 041, 043, 046, 053, 055, 058, 060, 061, 062, 063, 065, 067 |
| 39 | **Период около отёла** | Periparturient period | CS.ENTITY.??? | 008, 009, 020, 028, 035, 037, 039, 040, 042, 043, 046, 053, 055, 056, 060, 063, 066 |

---

## P1 — Important Entities (98 шт)

Встречаются в 2-4 SoTA.

### Метаболиты (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 40 | **Ацилкарнитины** | Acylcarnitines | CS.ENTITY.003 | 065 |
| 41 | **Фосфатидилхолины** | Phosphatidylcholines | CS.ENTITY.004 | 039, 065 |
| 42 | **Сфингомиелины** | Sphingomyelins | CS.ENTITY.005 | 039, 065 |
| 43 | **Желчные кислоты** | Bile acids | CS.ENTITY.006 | 065 |
| 44 | **Лизофосфатидилхолин** | Lysophosphatidylcholine | CS.ENTITY.??? | 039, 065 |
| 45 | **Триацилглицериды** | Triacylglycerols | CS.ENTITY.??? | 028, 030, 035, 039, 041, 043, 044, 046 |
| 46 | **Холестерин** | Cholesterol | CS.ENTITY.??? | 028, 039, 043, 046, 053 |
| 47 | **Жирные кислоты** | Fatty acids | CS.ENTITY.??? | 012, 026, 028, 035, 039, 041, 043, 046, 055, 058, 061, 063, 065 |
| 48 | **Пальмитиновая кислота** | Palmitic acid | CS.ENTITY.??? | 012, 026 |
| 49 | **Олеиновая кислота** | Oleic acid | CS.ENTITY.??? | 012, 026 |
| 50 | **Пропиленгликоль** | Propylene glycol | CS.ENTITY.??? | 058, 059, 060, 061, 062, 063 |
| 51 | **Глицерол** | Glycerol | CS.ENTITY.??? | 058, 062 |
| 52 | **Ацетоацетат** | Acetoacetate | CS.ENTITY.??? | 041, 043, 046 |
| 53 | **Ацетон** | Acetone | CS.ENTITY.??? | 041, 043, 046 |
| 54 | **Аминокислоты** | Amino acids | CS.ENTITY.??? | 017, 018, 035, 065 |
| 55 | **Пролин** | Proline | CS.ENTITY.??? | 017, 065 |
| 56 | **Глутамин** | Glutamine | CS.ENTITY.??? | 017, 065 |
| 57 | **Лейцин** | Leucine | CS.ENTITY.??? | 017, 065 |
| 58 | **Изолейцин** | Isoleucine | CS.ENTITY.??? | 017, 065 |
| 59 | **Валин** | Valine | CS.ENTITY.??? | 017, 065 |
| 60 | **Метионин** | Methionine | CS.ENTITY.??? | 017, 065 |
| 61 | **Холин** | Choline | CS.ENTITY.??? | 042, 065 |
| 62 | **Витамин B12** | Vitamin B12 | CS.ENTITY.??? | 058, 063 |
| 63 | **Карнитин** | Carnitine | CS.ENTITY.??? | 012, 058 |

### Гормоны/рецепторы (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 64 | **Прогестерон** | Progesterone | CS.ENTITY.??? | 003, 004, 020, 023 |
| 65 | **Пролактин** | Prolactin | CS.ENTITY.??? | 030, 035, 053 |
| 66 | **Соматотропин** | Growth hormone | CS.ENTITY.??? | 035, 053 |
| 67 | **Лептин** | Leptin | CS.ENTITY.??? | 035, 039 |
| 68 | **Грелин** | Ghrelin | CS.ENTITY.??? | 007, 035 |
| 69 | **Инсулиноподобный фактор роста** | IGF-1 | CS.ENTITY.??? | 035, 039 |
| 70 | **Тиреоидные гормоны** | Thyroid hormones | CS.ENTITY.??? | 035, 039 |
| 71 | **Рецепторы PPAR** | PPAR receptors | CS.ENTITY.??? | 039, 055 |

### Иммунные маркеры (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 72 | **Гаптоглобин** | Haptoglobin | CS.ENTITY.??? | 009, 053, 066 |
| 73 | **Сывороточный амилоид А** | Serum amyloid A | CS.ENTITY.??? | 053, 066 |
| 74 | **Фактор некроза опухоли α** | TNF-alpha | CS.ENTITY.??? | 009, 053, 066 |
| 75 | **Интерлейкин-6** | IL-6 | CS.ENTITY.??? | 009, 053 |
| 76 | **Интерлейкин-10** | IL-10 | CS.ENTITY.??? | 053, 066 |
| 77 | **Интерферон-γ** | IFN-gamma | CS.ENTITY.??? | 066 |

### Заболевания (U.Episteme)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 78 | **Субклиническая гипокальциемия** | Subclinical hypocalcemia | CS.ENTITY.007 | 020, 056, 066 |
| 79 | **Клиническая гипокальциемия** | Clinical hypocalcemia | CS.ENTITY.??? | 008, 020, 056 |
| 80 | **Лактатный ацидоз** | Lactic acidosis | CS.ENTITY.??? | 016, 038 |
| 81 | **Руминальный ацидоз** | Ruminal acidosis | CS.ENTITY.??? | 016, 038, 048 |
| 82 | **Эндометрит** | Endometritis | CS.ENTITY.??? | 008, 032 |
| 83 | **Циста яичника** | Ovarian cyst | CS.ENTITY.??? | 003, 032 |
| 84 | **Аноэструс** | Anestrus | CS.ENTITY.??? | 003, 007 |
| 85 | **Задержка овуляции** | Delayed ovulation | CS.ENTITY.??? | 007, 032 |

### Показатели/метрики (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 86 | **Период допустимости осеменения** | Insemination eligibility period | CS.ENTITY.??? | 019, 022 |
| 87 | **Волновой период** | Voluntary waiting period | CS.ENTITY.??? | 019, 025 |
| 88 | **Дни открытой** | Days open | CS.ENTITY.??? | 002, 019, 022 |
| 89 | **Интервал между отёлами** | Calving interval | CS.ENTITY.??? | 005, 019, 022 |
| 90 | **Продолжительность гестации** | Gestation length | CS.ENTITY.??? | 005, 023 |
| 91 | **Оборачиваемость стада** | Herd turnover rate | CS.ENTITY.??? | 019, 022 |
| 92 | **Коэффициент замещения** | Replacement rate | CS.ENTITY.??? | 019, 022, 024 |
| 93 | **Температура корпуса** | Body temperature | CS.ENTITY.??? | 027, 067 |
| 94 | **Активность** | Activity | CS.ENTITY.??? | 001, 027 |
| 95 | **Время жвачки** | Rumination time | CS.ENTITY.??? | 027, 032 |
| 96 | **Время кормления** | Feeding time | CS.ENTITY.??? | 007, 027 |
| 97 | **Время лежания** | Lying time | CS.ENTITY.??? | 027 |

### Методы/технологии (U.Method)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 98 | **Эмбриональный трансфер** | Embryo transfer | CS.ENTITY.??? | 003, 014 |
| 99 | **Индукция лютеолиза** | Prostaglandin injection | CS.ENTITY.??? | 003, 023 |
| 100 | **Гонадотропин-рилизинг гормон** | GnRH | CS.ENTITY.??? | 003, 023 |
| 101 | **УЗИ яичников** | Ovarian ultrasonography | CS.ENTITY.??? | 003, 004 |
| 102 | **Тест на беременность** | Pregnancy test | CS.ENTITY.??? | 003, 004, 019 |
| 103 | **FTIR-спектроскопия** | FTIR spectroscopy | CS.ENTITY.??? | 067 |
| 104 | **Метаболомика** | Metabolomics | CS.ENTITY.??? | 065 |
| 105 | **Липидомика** | Lipidomics | CS.ENTITY.??? | 039, 065 |
| 106 | **Машинное обучение** | Machine learning | CS.ENTITY.??? | 067 |

### Биологические структуры (U.System)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 107 | **Яичники** | Ovaries | CS.ENTITY.??? | 003, 004, 017, 023 |
| 108 | **Матка** | Uterus | CS.ENTITY.??? | 004, 008, 020 |
| 109 | **Молочная железа** | Mammary gland | CS.ENTITY.??? | 009, 035, 040 |
| 110 | **Поджелудочная железа** | Pancreas | CS.ENTITY.??? | 030, 039, 053 |
| 111 | **Надпочечники** | Adrenal glands | CS.ENTITY.??? | 035, 053 |
| 112 | **Щитовидная железа** | Thyroid gland | CS.ENTITY.??? | 035, 039 |
| 113 | **Гипоталамо-гипофизарная ось** | HPA axis | CS.ENTITY.??? | 035, 053 |
| 114 | **Кишечник** | Intestine | CS.ENTITY.??? | 018, 045 |
| 115 | **Почки** | Kidneys | CS.ENTITY.??? | 018, 043 |
| 116 | **Мышцы** | Muscles | CS.ENTITY.??? | 026, 035 |
| 117 | **Кости** | Bones | CS.ENTITY.??? | 056 |
| 118 | **Кровеносная система** | Cardiovascular system | CS.ENTITY.??? | 018, 045 |
| 119 | **Иммунная система** | Immune system | CS.ENTITY.??? | 009, 053 |
| 120 | **Нервная система** | Nervous system | CS.ENTITY.??? | 035, 053 |
| 121 | **Эндокринная система** | Endocrine system | CS.ENTITY.??? | 035, 039, 053 |

### Молекулярные сущности (U.Characteristic)

| № | Сущность (рус) | Сущность (англ) | ID | SoTA IDs |
|---|---------------|-----------------|-----|----------|
| 122 | **Митохондрии** | Mitochondria | CS.ENTITY.??? | 026, 065 |
| 123 | **Пероксисомы** | Peroxisomes | CS.ENTITY.??? | 026, 039 |
| 124 | **Цитоплазматические липидные капли** | Cytoplasmic lipid droplets | CS.ENTITY.??? | 028, 030 |
| 125 | **Клеточная мембрана** | Cell membrane | CS.ENTITY.??? | 030, 065 |
| 126 | **Рибосомы** | Ribosomes | CS.ENTITY.??? | 017, 018 |
| 127 | **Лизосомы** | Lysosomes | CS.ENTITY.??? | 030 |
| 128 | **Гладкий эндоплазматический ретикулум** | Smooth ER | CS.ENTITY.??? | 026, 030 |
| 129 | **Ацетил-КоА** | Acetyl-CoA | CS.ENTITY.??? | 026, 041 |
| 130 | **Малонил-КоА** | Malonyl-CoA | CS.ENTITY.??? | 026, 039 |
| 131 | **Пируват** | Pyruvate | CS.ENTITY.??? | 026, 029, 041 |
| 132 | **Оксалоацетат** | Oxaloacetate | CS.ENTITY.??? | 026, 029 |
| 133 | **Фосфоенолпируват** | Phosphoenolpyruvate | CS.ENTITY.??? | 026, 029 |
| 134 | **Глюкозо-6-фосфат** | Glucose-6-phosphate | CS.ENTITY.??? | 026, 029 |
| 135 | **Фруктозо-1,6-бисфосфат** | Fructose-1,6-bisphosphate | CS.ENTITY.??? | 026, 029 |
| 136 | **Глицеральдегид-3-фосфат** | Glyceraldehyde-3-phosphate | CS.ENTITY.??? | 026 |
| 137 | **Дигидроксиацетонфосфат** | Dihydroxyacetone phosphate | CS.ENTITY.??? | 026 |

---

## P2 — Specific Entities (31 шт)

Встречаются только в 1 SoTA (специфические).

| № | Сущность (рус) | Сущность (англ) | ID | SoTA ID | Примечание |
|---|---------------|-----------------|-----|---------|------------|
| 138 | **Керамиды** | Ceramides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 139 | **Гликозилфосфатидилинозитол** | Glycosylphosphatidylinositol | CS.ENTITY.??? | 039 | McFadden 2017 |
| 140 | **Сфингозин** | Sphingosine | CS.ENTITY.??? | 039 | McFadden 2017 |
| 141 | **Фосфатидилсерин** | Phosphatidylserine | CS.ENTITY.??? | 039 | McFadden 2017 |
| 142 | **Фосфатидилэтаноламин** | Phosphatidylethanolamine | CS.ENTITY.??? | 039 | McFadden 2017 |
| 143 | **Фосфатидилинозитол** | Phosphatidylinositol | CS.ENTITY.??? | 039 | McFadden 2017 |
| 144 | **Кардиолипин** | Cardiolipin | CS.ENTITY.??? | 039 | McFadden 2017 |
| 145 | **Диглицериды** | Diglycerides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 146 | **Моноглицериды** | Monoglycerides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 147 | **Свободный холестерин** | Free cholesterol | CS.ENTITY.??? | 039 | McFadden 2017 |
| 148 | **Холестериновые эфиры** | Cholesteryl esters | CS.ENTITY.??? | 039 | McFadden 2017 |
| 149 | **Дигидросфингозин** | Dihydrosphingosine | CS.ENTITY.??? | 039 | McFadden 2017 |
| 150 | **Фитосфингозин** | Phytosphingosine | CS.ENTITY.??? | 039 | McFadden 2017 |
| 151 | **Гексозилцерамиды** | Hexosylceramides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 152 | **Лактозилцерамиды** | Lactosylceramides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 153 | **Ганглиозиды** | Gangliosides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 154 | **Сульфатиды** | Sulfatides | CS.ENTITY.??? | 039 | McFadden 2017 |
| 155 | **Эфирные фосфолипиды** | Ether phospholipids | CS.ENTITY.??? | 039 | McFadden 2017 |
| 156 | **Плазмалогены** | Plasmalogens | CS.ENTITY.??? | 039 | McFadden 2017 |
| 157 | **Лизоплазмалогены** | Lysoplasmalogens | CS.ENTITY.??? | 039 | McFadden 2017 |
| 158 | **Алкиллидицы** | Alkyldiacylglycerols | CS.ENTITY.??? | 039 | McFadden 2017 |
| 159 | **Диалкилглицерилфосфат** | Dialkylglycerophosphates | CS.ENTITY.??? | 039 | McFadden 2017 |
| 160 | **Семейство фосфолипаз A2** | Phospholipase A2 family | CS.ENTITY.??? | 039 | McFadden 2017 |
| 161 | **Семейство фосфолипаз C** | Phospholipase C family | CS.ENTITY.??? | 039 | McFadden 2017 |
| 162 | **Семейство фосфолипаз D** | Phospholipase D family | CS.ENTITY.??? | 039 | McFadden 2017 |
| 163 | **Диацилглицеролацилтрансфераза** | Diacylglycerol acyltransferase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 164 | **Фосфатидатфосфатаза** | Phosphatidate phosphatase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 165 | **Липопротеинлипаза** | Lipoprotein lipase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 166 | **Гормон-чувствительная липаза** | Hormone-sensitive lipase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 167 | **Адипозитриацилглицероллипаза** | Adipose triglyceride lipase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 168 | **Лизосомальная кислая липаза** | Lysosomal acid lipase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 169 | **Перилипин** | Perilipin | CS.ENTITY.??? | 039 | McFadden 2017 |
| 170 | **Адипофиллин** | Adipophilin | CS.ENTITY.??? | 039 | McFadden 2017 |
| 171 | **Типидомин** | Tail-interacting protein of 47 kDa | CS.ENTITY.??? | 039 | McFadden 2017 |
| 172 | **CGI-58** | Comparative gene identification-58 | CS.ENTITY.??? | 039 | McFadden 2017 |
| 173 | **Альфа-липоид** | Alpha-lipoid | CS.ENTITY.??? | 039 | McFadden 2017 |
| 174 | **L-старин** | L-starin | CS.ENTITY.??? | 039 | McFadden 2017 |
| 175 | **Пататин-подобная фосфолипаза** | Patatin-like phospholipase | CS.ENTITY.??? | 039 | McFadden 2017 |
| 176 | **Сарко(эндо)плазматический ретикулум Ca2+-АТФаза** | SERCA | CS.ENTITY.??? | 039 | McFadden 2017 |
| 177 | **Рyanодиновый рецептор** | Ryanodine receptor | CS.ENTITY.??? | 039 | McFadden 2017 |
| 178 | **Инозитол-1,4,5-трисфосфатный рецептор** | IP3 receptor | CS.ENTITY.??? | 039 | McFadden 2017 |
| 179 | **Фосфофруктокиназа-2/фруктозо-2,6-бисфосфатаза** | PFKFB | CS.ENTITY.??? | 026 | Aiello 1984 |
| 180 | **Фруктозо-2,6-бисфосфат** | Fructose-2,6-bisphosphate | CS.ENTITY.??? | 026 | Aiello 1984 |
| 181 | **Пируваткиназа** | Pyruvate kinase | CS.ENTITY.??? | 026 | Aiello 1984 |
| 182 | **Лактатдегидрогеназа** | Lactate dehydrogenase | CS.ENTITY.??? | 026 | Aiello 1984 |
| 183 | **Аланинаминотрансфераза** | Alanine aminotransferase | CS.ENTITY.??? | 026 | Aiello 1984 |
| 184 | **Аспартатаминотрансфераза** | Aspartate aminotransferase | CS.ENTITY.??? | 026 | Aiello 1984 |
| 185 | **Глютаматдегидрогеназа** | Glutamate dehydrogenase | CS.ENTITY.??? | 026 | Aiello 1984 |
| 186 | **Ацетил-КоА-карбоксилаза** | Acetyl-CoA carboxylase | CS.ENTITY.??? | 026 | Aiello 1984 |
| 187 | **Метаболом** | Metabolome | CS.ENTITY.008 | 065 | Ghaffari 2024 |

---

## План создания entities

### Фаза 1: P0 (58 сущностей) — Приоритет: Критический
**Оценка времени:** ~29 часов (30 мин/сущность)

**Критические для начала:**
1. CS.ENTITY.001 — 21-day pregnancy rate (✅ готово)
2. CS.ENTITY.002 — Subclinical ketosis (✅ готово)
3. CS.ENTITY.003-008 — WP-75 entities (в процессе)
4. Остальные P0 — по мере необходимости

### Фаза 2: P1 (98 сущностей) — Приоритет: Высокий
**Оценка времени:** ~33 часа (20 мин/сущность)

### Фаза 3: P2 (31 сущность) — Приоритет: Средний
**Оценка времени:** ~8 часов (15 мин/сущность)

### Итого: ~70 часов работы

---

## Существующие entity-файлы

| Файл | Сущность | Статус | Дата создания |
|------|----------|--------|---------------|
| CS.ENTITY.001-21d-pregnancy-rate.md | 21-day pregnancy rate | ✅ Активен | 2026-03-01 |
| CS.ENTITY.002-subclinical-ketosis.md | Subclinical ketosis | ✅ Активен | 2026-03-26 |
| CS.ENTITY.003-liver.md | Liver | ✅ Активен | 2026-03-26 |
| CS.ENTITY.004-rumen.md | Rumen | ✅ Активен | 2026-03-26 |
| CS.ENTITY.005-adipose-tissue.md | Adipose tissue | ✅ Активен | 2026-03-26 |
| CS.ENTITY.006-milk.md | Milk | ✅ Активен | 2026-03-26 |
| CS.ENTITY.007-bhb.md | Beta-hydroxybutyrate (BHB) | ✅ Активен | 2026-03-26 |
| CS.ENTITY.008-nefa.md | Non-esterified fatty acids (NEFA) | ✅ Активен | 2026-03-26 |
| CS.ENTITY.009-glucose.md | Glucose | ✅ Активен | 2026-03-26 |
| CS.ENTITY.010-propionate.md | Propionate | ✅ Активен | 2026-03-26 |
| CS.ENTITY.011-acetate.md | Acetate | ✅ Активен | 2026-03-26 |
| CS.ENTITY.012-butyrate.md | Butyrate | ✅ Активен | 2026-03-26 |
| CS.ENTITY.013-lactate.md | Lactate | ✅ Активен | 2026-03-26 |
| CS.ENTITY.014-urea.md | Urea | ✅ Активен | 2026-03-26 |
| CS.ENTITY.015-insulin.md | Insulin | ✅ Активен | 2026-03-26 |
| CS.ENTITY.016-glucagon.md | Glucagon | ✅ Активен | 2026-03-26 |
| CS.ENTITY.017-cortisol.md | Cortisol | ✅ Активен | 2026-03-26 |
| CS.ENTITY.018-ketosis.md | Ketosis | ✅ Активен | 2026-03-26 |
| CS.ENTITY.019-acylcarnitines.md | Acylcarnitines | ⏳ Запланирован | — |
| CS.ENTITY.020-phosphatidylcholines.md | Phosphatidylcholines | ⏳ Запланирован | — |
| CS.ENTITY.021-subclinical-hypocalcemia.md | Subclinical hypocalcemia | ⏳ Запланирован | — |
| CS.ENTITY.022-metabolome.md | Metabolome | ⏳ Запланирован | — |

---

## Связанные документы

- [CS.ENTITY.001-21d-pregnancy-rate.md](./CS.ENTITY.001-21d-pregnancy-rate.md)
- [CS.ENTITY.002-subclinical-ketosis.md](./CS.ENTITY.002-subclinical-ketosis.md)
- [CS.ENTITY.003-liver.md](./CS.ENTITY.003-liver.md)
- [CS.ENTITY.004-rumen.md](./CS.ENTITY.004-rumen.md)
- [CS.ENTITY.005-adipose-tissue.md](./CS.ENTITY.005-adipose-tissue.md)
- [CS.ENTITY.006-milk.md](./CS.ENTITY.006-milk.md)
- [CS.ENTITY.007-bhb.md](./CS.ENTITY.007-bhb.md)
- [CS.ENTITY.008-nefa.md](./CS.ENTITY.008-nefa.md)
- [CS.ENTITY.009-glucose.md](./CS.ENTITY.009-glucose.md)
- [CS.ENTITY.010-propionate.md](./CS.ENTITY.010-propionate.md)
- [CS.ENTITY.011-acetate.md](./CS.ENTITY.011-acetate.md)
- [CS.ENTITY.012-butyrate.md](./CS.ENTITY.012-butyrate.md)
- [CS.ENTITY.013-lactate.md](./CS.ENTITY.013-lactate.md)
- [CS.ENTITY.014-urea.md](./CS.ENTITY.014-urea.md)
- [CS.ENTITY.015-insulin.md](./CS.ENTITY.015-insulin.md)
- [CS.ENTITY.016-glucagon.md](./CS.ENTITY.016-glucagon.md)
- [CS.ENTITY.017-cortisol.md](./CS.ENTITY.017-cortisol.md)
- [CS.ENTITY.018-ketosis.md](./CS.ENTITY.018-ketosis.md)
- [02A-roles.md](./02A-roles.md)
- [02C-methods-index.md](./02C-methods-index.md)
- [02D-tools-index.md](./02D-tools-index.md)

---

*Инвентарь создан: 2026-03-26*
*Обновлен: 2026-03-26*
*Добавлены CS.ENTITY.011-014: Ацетат, Бутират, Лактат, Мочевина*
*Добавлены CS.ENTITY.015-018: Инсулин, Глюкагон, Кортизол, Кетоз*
*Статус: Активный*
*Следующее обновление: По мере создания новых entities*
