---
type: fpf-pattern-application
pattern: "E.17 Multi-View Publication Kit (MVPK)"
sourceEntityOfConcern: "Проектная работа с AI-агентами в рамках FPF (семинар 02, 2026-07-19)"
---

# Multi-View Publication Kit (E.17) для семинара FPF-02

## Набор представлений одного и того же содержания

| Представление | Файл | Роль | Паттерн |
|---------------|------|------|---------|
| Исходный транскрипт | `07-19 Лекция Проектная работа с AI-агентами и системное мышление.txt` | Source-bearing side | — |
| Подробный narrative | `2026-07-19-FPF-second-seminar-project-work-AI-agents-NARRATIVE.md` | Чтение в параллель с семинаром | A.6.3.NAR + A.6.3.CR |
| Краткий пересказ | `2026-07-19-FPF-second-seminar-project-work-AI-agents-COARSENED.md` | Быстрый обзор | A.6.3.CSC |
| Консервативная переформулировка | `2026-07-19-FPF-second-seminar-project-work-AI-agents-CR.md` | Тот же смысл, другие слова | A.6.3.CR |
| Смена схемы представления | `2026-07-19-FPF-second-seminar-project-work-AI-agents-RT.md` | Структурированный тематический документ | A.6.3.RT |
| Рендеринг из структуры | `2026-07-19-FPF-second-seminar-project-work-AI-agents-NAR.md` | Связный рассказ по слайдоменту | A.6.3.NAR |
| Faithfulness profile | `2026-07-19-FPF-second-seminar-project-work-AI-agents-EFP.md` | Проверка объяснений | E.17.EFP |
| Сравнительный обзор | `2026-07-19-FPF-second-seminar-project-work-AI-agents-IDCR.md` | Сравнение NARRATIVE vs COARSENED | E.17.ID.CR |
| Structural adequacy | `2026-07-19-FPF-second-seminar-project-work-AI-agents-C33.md` | Что захвачено и потеряно | C.33 |
| Domain principle framework | `2026-07-19-FPF-second-seminar-project-work-AI-agents-DPF.md` | Принципы из семинара | E.4.DPF |
| Relation precision | `2026-07-19-FPF-second-seminar-project-work-AI-agents-RPR.md` | Kind-explicit relations | A.6.P |
| Lexical rules check | `2026-07-19-FPF-second-seminar-project-work-AI-agents-E10.md` | Проверка терминов | E.10 |
| Wording precision | `2026-07-19-FPF-second-seminar-project-work-AI-agents-E10ARCH.md` | Восстановление точности формулировок | E.10.ARCH |
| Epistemic retargeting | `2026-07-19-FPF-second-seminar-project-work-AI-agents-RETARGET.md` | Система → холон | A.6.4 |
| Карта представлений | `2026-07-19-FPF-second-seminar-project-work-AI-agents-MVPK.md` | Этот файл | E.17 |

## Correspondence model

Все представления ссылаются на одну и ту же entityOfConcern: проектную работу с AI-агентами в FPF, семинар 02. Они отличаются:
- **grain** (детализация),
- **recoverability** (возможность восстановить source),
- **admissible use** (допустимое использование),
- **loss profile** (что потеряно).

## Границы

- MVPK не заменяет source-bearing side.
- Каждое представление должно иметь declared loss и reopen path.
- Для gate-bearing claims использовать B.3 (Trust & Assurance Calculus) и A.21 (GateProfilization).
