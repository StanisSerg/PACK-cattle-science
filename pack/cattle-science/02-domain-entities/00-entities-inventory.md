# Инвентарь сущностей PACK-cattle-science

> Полный каталог entities из всех SoTA (213 файлов)
>
> **Дата создания:** 2026-04-15
> **Всего сущностей:** 213
> **Статус:** Активный

---

## Сводка

| Категория | Количество | Процент |
|-----------|-----------|---------|
| **Всего сущностей** | **213** | 100% |
| **P0 (Fundamental)** | 60 | 28% |
| **P1 (Important)** | 106 | 49% |
| **P2 (Specific)** | 47 | 22% |

### По типам FPF

| Тип | Количество | Описание |
|-----|-----------|----------|
| **U.Characteristic** | 104 | Измеримые характеристики |
| **Unknown** | 36 |  |
| **U.Method** | 25 | Методы/процедуры |
| **U.System** | 25 | Биологические системы |
| **U.Episteme** | 23 | Понятия/состояния |

### По областям

| Область | Упоминания |
|---------|-----------|
| feeding | 96 |
| health | 59 |
| reproduction | 40 |
| economics | 16 |
| management | 1 |
| genetics | 1 |

---

## P0 — Fundamental Entities (60 шт)

Встречаются в 5+ SoTA. Критические для понимания дисциплины.

### Feeding

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.004** | Рубец | Rumen | Rumen | U.System |
| **CS.ENTITY.010** | Пропионат | Propionate | C3 | U.Characteristic |
| **CS.ENTITY.011** | Ацетат | Acetate | C2 | U.Characteristic |
| **CS.ENTITY.012** | Бутират | Butyrate | C4 | U.Characteristic |
| **CS.ENTITY.013** | Лактат | Lactate | LA | U.Characteristic |
| **CS.ENTITY.014** | Мочевина | Urea | UUN | U.Characteristic |
| **CS.ENTITY.023** | Глюконеогенез | Gluconeogenesis | GNG | U.Episteme |
| **CS.ENTITY.030** | Потребление сухого вещества | Dry matter intake | DMI | U.Characteristic |
| **CS.ENTITY.032** | Жир молока | Milk fat | MF | U.Characteristic |
| **CS.ENTITY.033** | Белок молока | Milk protein | MP | U.Characteristic |
| **CS.ENTITY.052** | FTIR-спектроскопия | FTIR spectroscopy | FTIR | U.Method |
| **CS.ENTITY.058** | Кишечник | Intestine | INT | U.System |
| **CS.ENTITY.188** | Нейтрально-детергентная клетчатка | Neutral Detergent Fiber | NDF | U.Characteristic |
| **CS.ENTITY.189** | Рубцовое брожение | Rumen Fermentation | — | U.System |
| **CS.ENTITY.190** | pH рубца | Rumen pH | — | U.Characteristic |

### Health

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.002** | Субклинический кетоз | Subclinical ketosis | SCK | U.Episteme |
| **CS.ENTITY.003** | Печень | Liver | Hepatic | U.System |
| **CS.ENTITY.005** | Жировая ткань | Adipose tissue | AT | U.System |
| **CS.ENTITY.007** | β-гидроксибутират | Beta-hydroxybutyrate | BHB | U.Characteristic |
| **CS.ENTITY.008** | Неэтерифицированные жирные кислоты | Non-esterified fatty acids | NEFA | U.Characteristic |
| **CS.ENTITY.009** | Глюкоза | Glucose | Glc | U.Characteristic |
| **CS.ENTITY.015** | Инсулин | Insulin | INS | U.Characteristic |
| **CS.ENTITY.016** | Глюкагон | Glucagon | GLN | U.Characteristic |
| **CS.ENTITY.017** | Кортизол | Cortisol | CORT | U.Characteristic |
| **CS.ENTITY.018** | Кетоз | Ketosis | KET | U.Episteme |
| **CS.ENTITY.019** | Жировой гепатоз | Fatty liver disease | FLD | U.Episteme |
| **CS.ENTITY.020** | Гипокальциемия | Hypocalcemia | HYPOCA | U.Episteme |
| **CS.ENTITY.021** | Мастит | Mastitis | MAST | U.Episteme |
| **CS.ENTITY.022** | Метрит | Metritis | METR | U.Episteme |
| **CS.ENTITY.027** | Задержка последа | Retained placenta | RFM | U.Episteme |
| **CS.ENTITY.028** | Смещение сычуга | Displaced abomasum | DA | U.Episteme |
| **CS.ENTITY.029** | Оценка упитанности | Body condition score | BCS | U.Characteristic |
| **CS.ENTITY.036** | Переходный период | Transition period | TP | U.Episteme |
| **CS.ENTITY.041** | Гаптоглобин | Haptoglobin | Hp | U.Characteristic |
| **CS.ENTITY.042** | Эндометрит | Endometritis | ENDO | U.Episteme |
| **CS.ENTITY.050** | Руминальный ацидоз | Ruminal acidosis | RA | U.Episteme |
| **CS.ENTITY.054** | Иммунная система | Immune system | IS | U.System |
| **CS.ENTITY.055** | Нервная система | Nervous system | NS | U.System |
| **CS.ENTITY.057** | Ось гипоталамус-гипофиз-надпочечники | Hypothalamic-pituitary-adrenal axis | HPA axis | U.System |

### Management

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.053** | Машинное обучение | Machine learning | ML | U.Method |

### Reproduction

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.001** | 21-дневная стельность | 21-Day Pregnancy Rate | 21-d PR | U.Characteristic |
| **CS.ENTITY.006** | Молоко | Milk | Milk | U.System |
| **CS.ENTITY.024** | Искусственное осеменение | Artificial Insemination | AI | U.Method |
| **CS.ENTITY.025** | Синхронизация по времени | Timed Artificial Insemination | TAI | U.Method |
| **CS.ENTITY.026** | Обнаружение охоты | Heat Detection | HD | U.Method |
| **CS.ENTITY.031** | Удой | Milk yield | MY | U.Characteristic |
| **CS.ENTITY.034** | Протокол CIDR | CIDR protocol | CIDR | U.Method |
| **CS.ENTITY.037** | Сухостойный период | Dry period | DP | U.Episteme |
| **CS.ENTITY.038** | Ранняя лактация | Early lactation | EL | U.Episteme |
| **CS.ENTITY.039** | Период около отёла | Periparturient period | PP | U.Episteme |
| **CS.ENTITY.040** | Прогестерон | Progesterone | P4 | U.Characteristic |
| **CS.ENTITY.043** | Гонадотропин-рилизинг гормон | Gonadotropin-releasing hormone | GnRH | U.Method |
| **CS.ENTITY.044** | Яичники | Ovaries | OV | U.System |
| **CS.ENTITY.045** | Матка | Uterus | UT | U.System |
| **CS.ENTITY.046** | Молочная железа | Mammary gland | MG | U.System |
| **CS.ENTITY.047** | Дни открытой | Days open | DO | U.Characteristic |
| **CS.ENTITY.048** | Интервал между отёлами | Calving interval | CI | U.Characteristic |
| **CS.ENTITY.049** | Продолжительность гестации | Gestation length | GL | U.Characteristic |
| **CS.ENTITY.051** | Тест на беременность | Pregnancy test | PT | U.Method |
| **CS.ENTITY.056** | Эндокринная система | Endocrine system | ES | U.System |


---

## P1 — Important Entities (106 шт)

Расширенные понятия, важные для специализации.

### Economics

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.111** | Коэффициент обновления стада | Herd turnover rate | HTR | U.Characteristic |
| **CS.ENTITY.112** | Коэффициент замещения | Replacement rate | RR | U.Characteristic |
| **CS.ENTITY.128** | Выбытие | Culling | — | U.Method |
| **CS.ENTITY.129** | Коэффициент оборачиваемости стада | Herd turnover rate | HTR | U.Characteristic |
| **CS.ENTITY.130** | Коэффициент замены | Replacement rate | RR | U.Characteristic |
| **CS.ENTITY.131** | Долговечность | Longevity | — | U.Characteristic |
| **CS.ENTITY.140** | Частота дойки | Milking frequency | MF | U.Characteristic |
| **CS.ENTITY.141** | Система содержания | Housing system | — | U.System |
| **CS.ENTITY.142** | Точное молочное животноводство | Precision dairy farming | PDF | U.Method |
| **CS.ENTITY.144** | Экономическая эффективность | Economic efficiency | — | U.Characteristic |
| **CS.ENTITY.145** | Устойчивость | Sustainability | — | U.Characteristic |
| **CS.ENTITY.146** | Цифровое сельское хозяйство | Digital agriculture | — | U.Method |
| **CS.ENTITY.147** | Искусственный интеллект | Artificial intelligence | AI | U.Method |
| **CS.ENTITY.148** | Блокчейн | Blockchain | — | U.Method |
| **CS.ENTITY.149** | Интернет вещей | Internet of Things | IoT | U.Method |
| **CS.ENTITY.150** | Облачные вычисления | Cloud computing | — | U.Method |

### Feeding

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.067** | Ацилкарнитины | Acylcarnitines | AC | U.Characteristic |
| **CS.ENTITY.068** | Фосфатидилхолины | Phosphatidylcholines | PC | U.Characteristic |
| **CS.ENTITY.069** | Сфингомиелины | Sphingomyelins | SM | U.Characteristic |
| **CS.ENTITY.070** | Жёлчные кислоты | Bile acids | BA | U.Characteristic |
| **CS.ENTITY.071** | Лизофосфатидилхолин | Lysophosphatidylcholine | LPC | U.Characteristic |
| **CS.ENTITY.072** | Триацилглицериды | Triacylglycerols | TAG | U.Characteristic |
| **CS.ENTITY.073** | Холестерин | Cholesterol | CHOL | U.Characteristic |
| **CS.ENTITY.074** | Жирные кислоты | Fatty acids | FA | U.Characteristic |
| **CS.ENTITY.075** | Пальмитиновая кислота | Palmitic acid | C16:0 | U.Characteristic |
| **CS.ENTITY.076** | Олеиновая кислота | Oleic acid | C18:1 | U.Characteristic |
| **CS.ENTITY.077** | Пропандиол | Propanediol | 1,2-PD | U.Characteristic |
| **CS.ENTITY.078** | Глицерол | Glycerol | GLY | U.Characteristic |
| **CS.ENTITY.079** | Ацетоацетат | Acetoacetate | AcAc | U.Characteristic |
| **CS.ENTITY.080** | Ацетон | Acetone | ACE | U.Characteristic |
| **CS.ENTITY.081** | Аминокислоты | Amino acids | AA | U.Characteristic |
| **CS.ENTITY.082** | Пролин | Proline | Pro | U.Characteristic |
| **CS.ENTITY.083** | Глутамин | Glutamine | Gln | U.Characteristic |
| **CS.ENTITY.084** | Лейцин | Leucine | Leu | U.Characteristic |
| **CS.ENTITY.085** | Изолейцин | Isoleucine | Ile | U.Characteristic |
| **CS.ENTITY.086** | Валин | Valine | Val | U.Characteristic |
| **CS.ENTITY.087** | Метионин | Methionine | Met | U.Characteristic |
| **CS.ENTITY.088** | Холин | Choline | Chol | U.Characteristic |
| **CS.ENTITY.089** | Витамин B12 | Vitamin B12 | B12 | U.Characteristic |
| **CS.ENTITY.090** | Карнитин | Carnitine | CAR | U.Characteristic |
| **CS.ENTITY.132** | Мочевина в молоке | Milk urea nitrogen | MUN | U.Characteristic |
| **CS.ENTITY.133** | Кормовая эффективность | Feed efficiency | FE | U.Characteristic |
| **CS.ENTITY.134** | Масса тела | Body weight | BW | U.Characteristic |
| **CS.ENTITY.135** | Потребление воды | Water intake | WI | U.Characteristic |
| **CS.ENTITY.191** | Система углеводов и белков Cornell | Cornell Net Carbohydrate and Protein System | CNCPS | U.Method |
| **CS.ENTITY.192** | Кукурузный силос | Corn Silage | — | U.System |
| **CS.ENTITY.193** | Сырой протеин | Crude Protein | CP | U.Characteristic |
| **CS.ENTITY.194** | Распределение энергии | Energy Partitioning | — | U.Episteme |
| **CS.ENTITY.195** | Кормовое поведение | Feeding Behavior | — | U.Episteme |
| **CS.ENTITY.197** | Микробный протеин | Microbial Protein | MCP | U.Characteristic |
| **CS.ENTITY.198** | Депрессия жира молока | Milk Fat Depression | MFD | U.Episteme |
| **CS.ENTITY.199** | Переваримость NDF | NDF Digestibility | NDFD | U.Characteristic |
| **CS.ENTITY.200** | Неклетчаточные углеводы | Non-Fiber Carbohydrate | NFC | U.Characteristic |
| **CS.ENTITY.201** | Азотистый обмен | Nitrogen Metabolism | — | U.System |
| **CS.ENTITY.202** | Размер частиц | Particle Size | — | U.Characteristic |
| **CS.ENTITY.203** | Стеариновая кислота | Stearic Acid | C18:0 | U.Characteristic |

### Genetics

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.143** | Генетический отбор | Genetic selection | — | U.Method |

### Health

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.059** | Почки | Kidneys | KID | U.System |
| **CS.ENTITY.060** | Мышцы | Muscles | MUS | U.System |
| **CS.ENTITY.061** | Кости | Bones | BON | U.System |
| **CS.ENTITY.062** | Сердечно-сосудистая система | Cardiovascular system | CVS | U.System |
| **CS.ENTITY.063** | Поджелудочная железа | Pancreas | PAN | U.System |
| **CS.ENTITY.064** | Надпочечники | Adrenal glands | ADR | U.System |
| **CS.ENTITY.065** | Щитовидная железа | Thyroid gland | THY | U.System |
| **CS.ENTITY.066** | Печень | Liver | LIV | U.System |
| **CS.ENTITY.098** | Сывороточный амилоид А | Serum amyloid A | SAA | U.Characteristic |
| **CS.ENTITY.099** | Фактор некроза опухоли-альфа | Tumor necrosis factor-alpha | TNF-α | U.Characteristic |
| **CS.ENTITY.100** | Интерлейкин-6 | Interleukin-6 | IL-6 | U.Characteristic |
| **CS.ENTITY.101** | Интерлейкин-10 | Interleukin-10 | IL-10 | U.Characteristic |
| **CS.ENTITY.102** | Интерферон-гамма | Interferon-gamma | IFN-γ | U.Characteristic |
| **CS.ENTITY.103** | Субклиническая гипокальциемия | Subclinical hypocalcemia | SCH | U.Characteristic |
| **CS.ENTITY.104** | Клиническая гипокальциемия | Clinical hypocalcemia | CH | U.Characteristic |
| **CS.ENTITY.105** | Молочнокислый ацидоз | Lactic acidosis | LA | U.Characteristic |
| **CS.ENTITY.113** | Температура тела | Body temperature | BT | U.Characteristic |
| **CS.ENTITY.114** | Активность | Activity | ACT | U.Characteristic |
| **CS.ENTITY.115** | Время жвачки | Rumination time | RT | U.Characteristic |
| **CS.ENTITY.116** | Время кормления | Feeding time | FT | U.Characteristic |
| **CS.ENTITY.117** | Время лежания | Lying time | LT | U.Characteristic |
| **CS.ENTITY.121** | Метаболомика | Metabolomics | — | U.Method |
| **CS.ENTITY.122** | Липидомика | Lipidomics | — | U.Method |
| **CS.ENTITY.136** | Тепловой стресс | Heat stress | HS | U.Characteristic |
| **CS.ENTITY.137** | Хромота | Lameness | — | U.Characteristic |
| **CS.ENTITY.138** | Мастит | Mastitis | — | U.Characteristic |
| **CS.ENTITY.139** | Счёт соматических клеток | Somatic cell count | SCC | U.Characteristic |
| **CS.ENTITY.196** | Ламинит | Laminitis | — | U.Episteme |
| **CS.ENTITY.204** | Субострый руминальный ацидоз | Subacute Ruminal Acidosis | SARA | U.Episteme |

### Reproduction

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.091** | Пролактин | Prolactin | PRL | U.Characteristic |
| **CS.ENTITY.092** | Гормон роста | Growth hormone | GH | U.Characteristic |
| **CS.ENTITY.093** | Лептин | Leptin | LEP | U.Characteristic |
| **CS.ENTITY.094** | Грелин | Ghrelin | GHRL | U.Characteristic |
| **CS.ENTITY.095** | Инсулиноподобный фактор роста-1 | Insulin-like growth factor-1 | IGF-1 | U.Characteristic |
| **CS.ENTITY.096** | Тиреоидные гормоны | Thyroid hormones | TH | U.Characteristic |
| **CS.ENTITY.097** | PPAR-рецепторы | PPAR receptors | PPAR | U.Characteristic |
| **CS.ENTITY.106** | Яичниковая киста | Ovarian cyst | OC | U.Characteristic |
| **CS.ENTITY.107** | Анэструс | Anestrus | ANE | U.Characteristic |
| **CS.ENTITY.108** | Задержка овуляции | Delayed ovulation | DO | U.Characteristic |
| **CS.ENTITY.109** | Период пригодности к осеменению | Insemination eligibility period | IEP | U.Characteristic |
| **CS.ENTITY.110** | Добровольный период ожидания | Voluntary waiting period | VWP | U.Characteristic |
| **CS.ENTITY.118** | Трансплантация эмбрионов | Embryo transfer | ET | U.Method |
| **CS.ENTITY.119** | Инъекция простагландина | Prostaglandin injection | PGF2α | U.Method |
| **CS.ENTITY.120** | Ультразвуковое исследование яичников | Ovarian ultrasonography | USG | U.Method |
| **CS.ENTITY.123** | Диагностика беременности | Pregnancy diagnosis | PD | U.Method |
| **CS.ENTITY.124** | Легкость отела | Calving ease | CE | U.Characteristic |
| **CS.ENTITY.125** | Мёртворождение | Stillbirth | SB | U.Characteristic |
| **CS.ENTITY.126** | Двойня | Twinning | — | U.Characteristic |
| **CS.ENTITY.127** | Аборт | Abortion | — | U.Characteristic |


---

## P2 — Specific Entities (47 шт)

Детальные/молекулярные сущности.

### Feeding

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.151** | Unknown | Unknown | Cer | Unknown |
| **CS.ENTITY.154** | Unknown | Unknown | Ac-CoA | Unknown |
| **CS.ENTITY.155** | Unknown | Unknown | Pyr | Unknown |
| **CS.ENTITY.157** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.158** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.159** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.160** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.161** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.162** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.163** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.164** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.165** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.166** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.167** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.168** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.169** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.170** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.171** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.172** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.173** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.174** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.175** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.176** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.177** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.178** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.179** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.180** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.181** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.182** | Unknown | Unknown | — | Unknown |
| **CS.ENTITY.183** | Аланинаминотрансфераза | Alanine Aminotransferase | ALT | U.Characteristic |
| **CS.ENTITY.184** | Аспартатаминотрансфераза | Aspartate Aminotransferase | — | Unknown |
| **CS.ENTITY.185** | Глютаматдегидрогеназа | Glutamate Dehydrogenase | — | Unknown |
| **CS.ENTITY.186** | Ацетил-КоА карбоксилаза | Acetyl-CoA Carboxylase | — | Unknown |
| **CS.ENTITY.187** | Метаболом | Metabolome | — | Unknown |
| **CS.ENTITY.206** | Метод in situ | In Situ Technique | in situ | U.Method |
| **CS.ENTITY.207** | Метод in vitro | In Vitro Technique | in vitro | U.Method |
| **CS.ENTITY.210** | Шаблон приёма пищи | Meal Pattern | — | U.Episteme |
| **CS.ENTITY.211** | Меласса | Molasses | — | U.System |
| **CS.ENTITY.212** | Физически эффективная NDF | Physically Effective NDF | peNDF | U.Characteristic |
| **CS.ENTITY.213** | Сортировка корма | Sorting | — | U.Episteme |
| **CS.ENTITY.214** | Транс-жирные кислоты | Trans Fatty Acids | TFA | U.Characteristic |

### Health

| ID | Сущность (рус) | Сущность (англ) | Аббр. | Тип |
|-----|---------------|-----------------|-------|-----|
| **CS.ENTITY.152** | Unknown | Unknown | Mito | Unknown |
| **CS.ENTITY.153** | Unknown | Unknown | PXS | Unknown |
| **CS.ENTITY.156** | Unknown | Unknown | LDH | Unknown |
| **CS.ENTITY.205** | Эндотоксин | Endotoxin | LPS | U.Characteristic |
| **CS.ENTITY.208** | Липополисахарид | Lipopolysaccharide | LPS | U.Characteristic |
| **CS.ENTITY.209** | Печеночный абсцесс | Liver Abscess | — | U.Episteme |


---

*Сгенерировано: 2026-04-15*
*Автоматическое обновление через: `python3 scripts/reindex-entities.py`