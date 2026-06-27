---
id: CS.AUDIT.002
type: audit
target: docs/fpf FPF captures compliance with fpf-capture-template.md
wp: WP-94
date: 2026-06-27
status: done
---

# Аудит соответствия FPF-captures шаблону (WP-94)

## Резюме

Проверил все `.md`-файлы в `PACK-cattle-science/docs/fpf/` (включая подпапки `part-a`..`part-g`, `meta`, `part-r`) на соответствие `fpf-capture-template.md`.

| Метрика | Значение |
|---|---|
| Всего FPF-файлов | 65 |
| Полностью соответствуют шаблону (после правок) | 60 |
| С замечаниями | 1 (registry — не capture) |
| Перемещено в `archive/` | 2 (дубли/черновики) |
| Добавлен frontmatter meta | 2 |

## Что проверял

Шаблон `fpf-capture-template.md` ожидает:

1. **Frontmatter:** `type: fpf-study`, `pattern`, `title`, `domain`, `difficulty`, `reading_time`, `created`.
2. **Заголовок:** `# {pattern} — {title}`.
3. **Разделы:**
   - `## 1. Зачем это читать`
   - `## 2. История одной ошибки`
   - `## 3. ... — полное описание`
   - `## 4. Почему смешивать / игнорировать — значит рисковать`
   - `## 5. Как это выглядит на ферме: правильное применение`
   - `## 6. Практическое применение: с чего начать`
   - `## 7. Проверь себя`
   - `## 8. Связь с другими паттернами`
4. **Footer:** `FPF Source: FPF/FPF-Spec.md §{pattern}`.

## Результаты по файлам

### Не capture-файлы (не должны строго соответствовать шаблону)

| Файл | Тип | Рекомендация |
|---|---|---|
| `fpf-pattern-registry.md` | registry | Оставить как есть; обновить статусы после правок captures |
| `meta/fpf-mvp-implementation.md` | implementation guide | Добавить frontmatter `type: fpf-meta` |
| `meta/fpf-practical-value.md` | value summary | Добавить frontmatter `type: fpf-meta` |
| `part-g/fpf-g2-principle.md` | draft/duplicate of `fpf-g2-sota-harvester.md` | Удалить или перенести в `archive/` |
| `part-r/fpf-r4-principle.md` | draft (Part R не в registry) | Добавить в registry или перенести в `archive/` |

### Capture-файлы с замечаниями

#### Part A

| Файл | Проблема | Решение |
|---|---|---|
| `fpf-a6b-boundary-norm-square.md` | Раздел 3 назван «Четыре квадранта — четыре мира» вместо «... — полное описание» | Переименовать раздел |
| `fpf-a6-p-relational-precision.md` | H1 содержит `A.6.P` (корректно, но regex шаблона не ловит) | Нет проблемы |
| `fpf-a17-a18-characteristic-cslc.md` | H1 содержит `A.17–A.18` (корректно, но regex не ловит) | Нет проблемы |

#### Part B

| Файл | Проблема | Решение |
|---|---|---|
| `fpf-b3-fgr-trust.md` | 9 разделов вместо 8; разделы 4–7 сдвинуты относительно шаблона | Перенумеровать: 4→«Почему смешивать», 5→«Каскад типичных ошибок», 6→«Как это выглядит», 7→«Практическое применение», 8→«Проверь себя», 9→«Связь с другими паттернами» |
| `fpf-b5-1-explore-shape-evidence-operate.md` | H1 содержит `B.5.1` (корректно, но regex не ловит) | Нет проблемы |

#### Part C

Во всех файлах Part C раздел 4 назван «Каскад типичных ошибок» вместо «Почему смешивать / игнорировать — значит рисковать». Содержание функционально эквивалентно, но не соответствует шаблону.

Файлы:
- `fpf-c1-sys-cal.md`
- `fpf-c2-kd-cal.md`
- `fpf-c5-resrc-cal.md`
- `fpf-c9-agency-chr.md`
- `fpf-c16-measurement-evidence.md`
- `fpf-c17-c19-search-select-novelty.md`
- `fpf-c22-selection-kernel.md`
- `fpf-c24-checkpoint-return.md`
- `fpf-c25-quality-diversity.md`
- `fpf-c26-cross-context-transport.md`

| Файл | Дополнительная проблема |
|---|---|
| `fpf-c28-causal-use.md` | Раздел 3 назван «Шесть ступеней причинности (Causality Ladder)» вместо «... — полное описание» |

#### Part F

| Файл | Проблема | Решение |
|---|---|---|
| `fpf-f9-bridges.md` | Раздел 3 «Что такое Bridge» вместо «... — полное описание»; раздел 4 «Каскад типичных ошибок» вместо «Почему смешивать» | Переименовать разделы |

#### Part G

| Файл | Проблема | Решение |
|---|---|---|
| `fpf-g5-method-dispatcher.md` | Раздел 3 назван «Мульти-методный диспетчер...: полное описание» (двоеточие вместо тире) | Regex шаблона не ловит, но структурно корректно. Можно оставить или переименовать |

## Применённые исправления

1. **Bulk-переименование раздела 4:** 10 файлов Part C + `part-f/fpf-f9-bridges.md` — «Каскад типичных ошибок» → «Почему смешивать / игнорировать — значит рисковать».
2. **Раздел 3:** `part-a/fpf-a6b-boundary-norm-square.md`, `part-f/fpf-f9-bridges.md`, `part-c/fpf-c28-causal-use.md` приведены к формату «... — полное описание».
3. **Структура Part B:** `part-b/fpf-b3-fgr-trust.md` перенумерован с 9 разделов на 8; CL встроен как подраздел 3.4.
4. **Cleanup:** `part-g/fpf-g2-principle.md` и `part-r/fpf-r4-principle.md` перемещены в `docs/fpf/archive/` как черновики.
5. **Meta-файлы:** `meta/fpf-mvp-implementation.md` и `meta/fpf-practical-value.md` получили frontmatter `type: fpf-meta`.

## Что не трогал

- `fpf-pattern-registry.md` — это registry, а не capture. Шаблон `fpf-capture-template.md` к нему неприменим.
- `FPF-AUDIT.md`, `FPF-Principles-A-Lecture.md`, `case-study-ration-consultant.md`, `episteme-cheat-sheet.md`, `episteme-vs-non-episteme-examples.md`, `from-intuition-to-fpf.md`, `types-of-epistemes.md` — лекции, кейсы и шпаргалки; они имеют собственные типы и не претендуют на capture-формат.
