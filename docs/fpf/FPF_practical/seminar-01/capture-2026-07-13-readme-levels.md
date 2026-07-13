---
type: capture
source: WP-109 / FPF-practical seminar 01 follow-up
date: 2026-07-13
topic: "Три уровня README: FPF-README, GitHub README, локальный README.md"
related:
  - WP-109
  - WP-94
  - E.4.FPF
  - E.11
  - E.17
  - E.10.D2
---

# Capture: Три разных README — не путать

## Insight

Слово «README» используется на трёх разных уровнях. В FPF важно различать карточки применения внутри файла FPF, публикационное лицо на GitHub и локальные инструкции проекта.

## Что уточнилось

- **FPF-README** — это entry point с карточками применения, мантрами и ведущими паттернами. Это часть FPF (`E.4.FPF`, `E.11`).
- **GitHub README** — publication face (`E.17`) того же FPF-README для удобства веб-входа. Содержание то же, carrier другой.
- **Локальный README.md** в папке проекта — это LPF/местная инструкция, не FPF. Он может ссылаться на FPF, но не содержит карточек применения.
- **AGENTS.md / CLAUDE.md** — тоже локальные инструкции для агентов, не FPF.
- Имена файлов (`README`, `ReadMe`, `readme`) — это naming convention операционной системы/workspace/агента, не онтология FPF (`F.18` касается имён внутри FPF, не файлов).

## Применение к текущей работе

В IWE/PACK-cattle-science:
- `FPF/Readme.md` — GitHub publication face для FPF.
- `PACK-cattle-science/docs/fpf/FPF_practical/seminar-01/2026-07-12-FPF-first-seminar-LECTURE.md` — локальный разбор, не FPF-README.
- `AGENTS.md` / `CLAUDE.md` — локальные инструкции для агентов.

Не искать паттерны в `AGENTS.md` и не путать entry point FPF с проектной документацией.

## Следующий ход

- При входе в FPF использовать именно FPF-README с голубыми карточками, а не GitHub README.
- При написании локальных README/AGENTS.md явно указывать, где лежит FPF и как к нему обращаться.
