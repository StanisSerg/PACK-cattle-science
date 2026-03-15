# AGENTS.md — PACK-cattle-science

> **Назначение:** Инструкции для AI-ассистентов (Claude, Kimi, и др.)  
> **Домен:** Наука о молочном скоте (cattle-science)  
> **Уровень:** Pack (Level 2)  
> **Версия:** 1.3  
> **Обновлён:** 2026-03-14

---

## Быстрый старт

При начале работы с PACK-cattle-science:

1. **Прочитать** `PROTOCOLS/WP-75-sota-ingestion.md`
2. **Изучить** `TEMPLATES/SOTA-TEMPLATE.md`
3. **Посмотреть** `CS.SOTA.001` как reference
4. **Проверить** `CS.MAP.001-sota-index.md` для контекста

---

## Ключевые протоколы

### WP-75: SoTA Ingestion

**Когда использовать:** Создание новых SoTA (State of the Art)

**Параметры:**
- 4 часа / сессия
- 10 статей / сессия
- ~25 минут / статья
- Целевой ArchGate: ≥8/10

**Фазы:**
1. **Подготовка** (до сессии)
2. **Открытие** (15 мин) — настройка
3. **Работа** (3ч 20мин) — создание SoTA
4. **Закрытие** (25 мин) — оценка, индекс, git

**Выход:** Полноценный SoTA v1.3 (466 строк, 11 разделов)

---

## Структура SoTA v1.3 (Reference)

```
CS.SOTA.XXX/
├── CS.SOTA.XXX.md              # Основной файл (466 строк)
│   ├── YAML frontmatter        # Метаданные + теги + связи
│   ├── Abstract                # Резюме
│   ├── Introduction            # Введение [перевод]
│   ├── Materials & Methods     # Методы
│   ├── Results                 # Результаты + медиа-инвентарь
│   ├── Practical Application   # Алгоритм + калькулятор
│   ├── Lecture Materials       # Для преподавания
│   ├── Conclusions             # Выводы [перевод]
│   ├── Critical Analysis       # Критика + сравнение
│   ├── FAQ                     # 5-7 вопросов
│   ├── Tools & Templates       # Инструменты
│   ├── Sources                 # Источники
│   └── Processing Log          # Журнал
│
└── lecture-example/            # (опционально)
    ├── handout-student.md
    ├── slides.md + slides.pdf
    ├── lecturer-guide.md
    └── quiz.md
```

---

## Критерии качества (ArchGate)

| Критерий | Вес | Минимум | Цель |
|----------|-----|---------|------|
| Структура | 2 | 6 разделов | 11 разделов |
| Метаданные | 2 | Базовые YAML | YAML + теги + связи |
| Связи | 2 | 1-2 связи | 3-5 типированных |
| Полнота | 2 | Abstract+Results+Conclusions | +M&M+Analysis+FAQ |
| Источники | 2 | DOI | Open access |
| Актуальность | 2 | <5 лет | <2 лет |
| Медиа | 2 | Нет | Медиа-инвентарь |
| Практика | 2 | Нет | Алгоритм + инструменты |
| Лекции | 2 | Нет | Тайминг + комментарии |
| Версионирование | 2 | 1 запись | 3+ записи |

**Проходной балл: ≥8/10**

---

## Типы связей (related)

```yaml
type: compares_programs        # Сравнение программ
type: economic_analysis        # Экономический анализ
type: optimal_vwp              # Оптимальный VWP/IEP
type: simulation_methodology   # Методология симуляции
type: foundational             # Базовые основы
type: contradicts              # Противоречит
type: extends                  # Расширяет
type: replication              # Репликация
type: review                   # Обзор упоминает
```

---

## Обязательные теги

Каждый SoTA должен иметь:

```yaml
tags:
  # Методология (1+)
  - simulation-model | meta-analysis | field-study | review
  
  # Тематика (1+)
  - reproductive-management | feeding-strategy | herd-health | genetics
  
  # Технологии (применимо)
  - sexed-semen | beef-semen | embryo-transfer | precision-dairy
  
  # Фокус (1+)
  - economic-optimization | fertility | milk-yield | longevity
```

---

## Медиа-инвентарь

Для каждого графика/таблицы из статьи:

```markdown
### X.X. [Название]

**Название в статье:** Figure X. ...
**Источник:** [Авторы] [Год], стр. XXXX
**Тип:** [Гистограмма | Таблица | График | Диаграмма]

**Описание:**
- Что показано
- Ключевые элементы

**Ключевые цифры:**
- Цифра 1: значение
- Цифра 2: значение

**Комментарий лектора:**
> "Дословный текст для озвучивания на лекции"

**Действие:** [СКРИНШОТ] Добавить Figure X из PDF
```

---

## Частые задачи

### Создать новый SoTA

```bash
# 1. Определить ID
Следующий после CS.MAP.001-sota-index.md

# 2. Создать структуру
mkdir 06-sota/[area]/CS.SOTA.XXX-[название]
cp TEMPLATES/SOTA-TEMPLATE.md CS.SOTA.XXX.md

# 3. Следовать WP-75
# 4. Обновить индекс
# 5. Git commit
```

### Создать лекцию на основе SoTA

```bash
# В папке SoTA:
mkdir lecture-example/
cp TEMPLATES/LECTURE-TEMPLATE/* lecture-example/

# Заполнить:
# - handout-student.md
# - slides.md (Marp)
# - lecturer-guide.md
# - quiz.md

# Сгенерировать PDF:
npx @marp-team/marp-cli slides.md --pdf
```

### Обновить существующий SoTA

```markdown
## Журнал обработки
| Дата | Версия | Действие |
|------|--------|----------|
| 2026-03-14 | 1.0 | Создание |
| 2026-03-15 | 1.1 | Добавлены связи |
| 2026-03-16 | 1.2 | Добавлены FAQ |
```

---

## Индексы и навигация

| Файл | Назначение |
|------|------------|
| `CS.MAP.001-sota-index.md` | Все SoTA с метаданными |
| `CS.MAP.002-topic-index.md` | Тематические кластеры |
| `CS.MAP.003-lecture-index.md` | Готовые лекции |

---

## Связь с другими уровнями

```
FPF (L1) → SPF (L2) → PACK-cattle-science (L2) → Exocortex-V2 (L4)
                ↓
         TEMPLATES/
         PROTOCOLS/
         CS.SOTA.XXX/
```

---

## Контакты и обратная связь

Обновления этого файла:
- Через git commit
- Или инструкцию пользователя

---

*AGENTS.md для PACK-cattle-science*  
*Версия 1.3*  
*2026-03-14*
