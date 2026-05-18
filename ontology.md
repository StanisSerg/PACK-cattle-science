---
id: CS.ONTOLOGY.ROOT
type: ontology
domain: cattle-science
version: 1.0
created: 2026-03-12
updated: 2026-05-18
language: ru
---

# Онтология PACK-cattle-science (Root)

> Корневая онтология Pack'а "Наука о содержании и кормлении молочного крупного рогатого скота".

---

## Идентификация Pack'а

| Атрибут | Значение |
|---------|----------|
| **ID** | PACK-cattle-science |
| **Название** | Наука о содержании и кормлении молочного КРС |
| **Английское название** | Dairy Cattle Science |
| **Версия** | 1.0.0 |
| **Создан** | 2026-03-01 |
| **Обновлён** | 2026-03-12 |
| **Владелец** | Stanis Serg |
| **Тип** | Domain Pack (L2) |

---

## Позиционирование в иерархии

```
FPF (Level 1) — First Principles Framework
    ↓ upstream
SPF (Level 2) — Second Principles Framework
    ↓ downstream
PACK-cattle-science (L2) — Domain Pack
    ↓ downstream
DS-cattle-course (L3) — Surface (курс)
```

### Связь с upstream

| Upstream | Элемент | Связь |
|----------|---------|-------|
| FPF | A.1 Bounded Context | Структура области |
| FPF | A.3 Method | Типология методов |
| FPF | A.7 Strict Distinction | Различения |
| FPF | Part G SoTA Kit | Работа с источниками |
| SPF | pack-template/ | Структура Pack'а |
| SPF | process/ | Процесс создания |

### Downstream

| Downstream | Тип | Связь |
|------------|-----|-------|
| DS-cattle-course | Surface (курс) | Обучение на основе Pack'а |
| Exocortex-V2 | Personal IWE | Использование знаний |

---

## Структура Pack'а

```
PACK-cattle-science/
├── README.md
├── CLAUDE.md
├── REPO-TYPE.md
├── WORKPLAN.md
├── ontology.md                    ← Этот файл
├── SPF-COMPLIANCE-REPORT.md
├── pack/cattle-science/
│   ├── 00-pack-manifest.md
│   ├── 01-domain-contract/
│   │   ├── 01A-bounded-context.md
│   │   ├── 01B-distinctions.md
│   │   └── 01C-ontology.md        ← Детальная онтология
│   ├── 02-domain-entities/
│   │   ├── CS.ENTITY.001-21d-pregnancy-rate.md
│   │   ├── 02A-roles.md           ← Роли
│   │   ├── 02C-methods-index.md   ← Индекс методов
│   │   └── 02D-tools-index.md     ← Индекс инструментов
│   ├── 03-methods/
│   │   ├── CS.METHOD.003-reproductive-economics.md
│   │   ├── CS.METHOD.004-cow-value-assessment.md
│   │   └── CS.METHOD.005-calcium-monitoring-hypocalcemia-prevention.md
│   ├── 04-work-products/
│   │   ├── CS.WP.003-reproduction-economic-report.md
│   │   ├── CS.WP.004-cow-value-report.md
│   │   └── CS.WP.005-reproductive-program-comparison.md
│   ├── 05-failure-modes/          ← Режимы отказа
│   │   ├── _failure-mode-template.md
│   │   ├── CS.FM.001-overestimation-21d-pr.md
│   │   └── CS.FM.002-ignoring-replacement-constraints.md
│   ├── 06-sota/
│   │   ├── reproduction/
│   │   │   ├── CS.SOTA.001-lauber-2025...
│   │   │   ├── ...
│   │   │   └── CS.SOTA.012-chebel-ribeiro-2016...
│   │   └── feeding/
│   │       └── CS.SOTA.010-XX-nasem...
│   └── 07-map/
│       └── CS.MAP.001-sota-index.md
└── process/
    ├── ingestion/
    └── working/
```

---

## Ключевые понятия (Top Level)

### Сущности (Entities)

| ID | Название | Описание |
|----|----------|----------|
| CS.ENTITY.001 | 21-day pregnancy rate | Ключевой показатель репродуктивной эффективности |

### Методы (Methods)

| ID | Название | Описание | Статус |
|----|----------|----------|--------|
| CS.METHOD.003 | Reproductive economics | Экономическая оценка репродуктивных программ | Active |
| CS.METHOD.004 | Cow value assessment | Оценка ценности коровы (RPO) | Active |
| CS.METHOD.005 | Transition health monitoring | Оценка уровня кальция и профилактика гипокальцемии в переходный период | Active |

### Рабочие продукты (Work Products)

| ID | Название | Описание |
|----|----------|----------|
| CS.WP.003 | Reproduction economic report | Отчёт об экономической оценке |
| CS.WP.004 | Cow value report | Отчёт об оценке ценности коровы |
| CS.WP.005 | Program comparison | Сравнение репродуктивных программ |

### Режимы отказа (Failure Modes)

| ID | Название | Описание |
|----|----------|----------|
| CS.FM.001 | Overestimation of 21-d PR | Завышение 21-дневного индекса стельности |
| CS.FM.002 | Ignoring replacement constraints | Игнорирование ограничений замены |

### SoTA (State of the Art)

| Диапазон | Тема | Количество |
|----------|------|------------|
| CS.SOTA.001-099 | Reproduction | 12 |
| CS.SOTA.010-019 | Feeding (NASEM) | 17 |

---

## Пространство имён (Namespace)

### Префиксы

| Префикс | Значение | Пример |
|---------|----------|--------|
| CS. | Cattle-Science (домен) | CS.METHOD.003 |
| CS.ENTITY. | Сущности | CS.ENTITY.001 |
| CS.METHOD. | Методы | CS.METHOD.003 |
| CS.WP. | Work Products | CS.WP.003 |
| CS.FM. | Failure Modes | CS.FM.001 |
| CS.SOTA. | State of the Art | CS.SOTA.001 |
| CS.MAP. | Карты/индексы | CS.MAP.001 |
| CS.ROLES. | Роли | CS.ROLES.001 |
| CS.TOOLS. | Инструменты | CS.TOOLS.001 |

### Диапазоны ID

| Тип | Диапазон | Описание |
|-----|----------|----------|
| Сущности | 001-999 | Доменные сущности |
| Методы | 001-599 | По категориям (001-099 кормление, 100-199 репродукция и т.д.) |
| Work Products | 001-999 | Рабочие продукты |
| Failure Modes | 001-999 | Режимы отказа |
| SoTA | 001-999 | По подпапкам (reproduction/, feeding/, health/) |
| Роли | 001-999 | Роли в области |
| Инструменты | 001-999 | Инструменты и ПО |

---

## Ключевые различения (Hard Distinctions)

### Внутренние различения домена

| Понятие 1 | Понятие 2 | Различение | Где документировано |
|-----------|-----------|------------|---------------------|
| Conception | Pregnancy | Conception = момент; Pregnancy = состояние | 01B-distinctions.md |
| Service Rate | Conception Rate | SR = % осеменённых; CR = % забеременевших | 01B-distinctions.md |
| Method | Tool | Method = как; Tool = чем | 01B-distinctions.md |

### Различения FPF/SPF в контексте

| FPF Различение | Применение | Статус |
|----------------|------------|--------|
| Role ≠ Actor | Роли vs исполнители | Применяется |
| Method ≠ Tool | Методы vs инструменты | Применяется |
| Work Product ≠ Description | Продукт vs описание | Применяется |
| System ≠ Episteme | Система vs область знания | Применяется |

---

## Процессы и гейты

### Процесс развития Pack'а

```
1. Domain Selection (SPF 01)
   ↓
2. Bounded Context (SPF 02)
   ↓
3. Distinctions Work (SPF 03)
   ↓
4. Entities Identification (SPF 04)
   ↓
5. Information Ingestion (SPF 05) ← SoTA ingestion
   ↓
6. Analysis & Formalization (SPF 06)
   ↓
7. Method & Product Extraction (SPF 07)
   ↓
8. Failure Modes Extraction (SPF 08)
   ↓
9. SoTA Annotation (SPF 09)
   ↓
10. Map Maintenance (SPF 10)
   ↓
11. Review & Evolution (SPF 11)
```

### Гейты (Lint)

| Гейт | Проверка | Когда |
|------|----------|-------|
| Structure Lint | Соответствие pack-template | Перед commit |
| ID Lint | Корректность идентификаторов | Перед commit |
| Content Lint | Отсутствие дидактики в Pack | Перед commit |
| Distinction Lint | Соблюдение Hard Distinctions | Перед commit |

---

## Метрики Pack'а

### Текущее состояние (2026-03-12)

| Метрика | Значение | Цель |
|---------|----------|------|
| SoTA документов | 29 | 100+ |
| Методов (Active) | 3 | 20+ |
| Work Products | 3 | 10+ |
| Failure Modes | 2 | 10+ |
| Сущностей | 1 | 10+ |
| Полнота по SPF | 85% | 100% |

### Качество

| Метрика | Статус |
|---------|--------|
| Структура соответствует SPF | ✅ 85% |
| Все ID уникальны | ✅ |
| Все ссылки валидны | ✅ |
| Нет дидактики в Pack | ✅ |

---

## Дорожная карта (Roadmap)

### Phase 1: Foundation (Q1 2026) ✅ Выполнено
- [x] Структура Pack'а
- [x] Базовые методы (3)
- [x] Базовые WP (3)
- [x] SoTA коллекция (29)
- [x] Failure modes (2)

### Phase 2: Completeness (Q2 2026) 🔄 В процессе
- [ ] Методы кормления (CS.METHOD.001-002)
- [ ] Методы репродукции (CS.METHOD.006-010)
- [ ] Дополнительные сущности
- [ ] Полный набор failure modes

### Phase 3: Depth (Q3-Q4 2026) ⏳ Запланировано
- [ ] Глубокая проработка всех категорий
- [ ] Интеграция с другими Pack'ами
- [ ] Валидация практикой

---

## Связи с внешними системами

### Upstream

| Система | Тип связи | Частота обновления |
|---------|-----------|-------------------|
| FPF | Нормативная | По мере выхода версий |
| SPF | Нормативная | По мере выхода версий |

### Downstream

| Система | Тип связи | Контракт |
|---------|-----------|----------|
| DS-cattle-course | Использование | Pack → Course |
| Exocortex-V2 | Использование | Pack → IWE |

### Peer (соседние Pack'и)

| Pack | Связь | Статус |
|------|-------|--------|
| PACK-personal | Методы обучения | Planned |
| PACK-ecosystem | Экосистема | Planned |

---

## Контакты и поддержка

| Роль | Контакт | Ответственность |
|------|---------|-----------------|
| Владелец Pack'а | Stanis Serg | Стратегия, приоритеты |
| Knowledge Engineer | Kimi Code | Интеграция, lint, формализация |
| Domain Expert | TBD | Предметная экспертиза |

---

*Создано: 2026-03-12*  
*Версия: 1.0*  
*Статус: Активное развитие*  
*Соответствие SPF: 85%*
