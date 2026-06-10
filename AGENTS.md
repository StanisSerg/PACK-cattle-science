# AGENTS.md — PACK-cattle-science

> **Локальные инструкции для PACK-cattle-science.** Переопределяют корневые настройки в рамках этого репозитория.

---

## FPF Reference MCP — Обязательный вызов

При работе с файлами в следующих директориях агент **ДОЛЖЕН** вызывать `fpf_reference` **до** начала создания или редактирования артефакта:

- `cases/` — сырые кейсы
- `decisions/` — Decision Layer (DL)
- `pack/rules/` — правила Pack
- `pack/cattle-science/01-domain-contract/` — границы и различения
- `pack/cattle-science/03-methods/` — методы оценки

### Алгоритм вызова

1. **`get_fpf_index_status`** — проверить свежесть индекса
2. Если `fresh: true` — **`query_fpf_spec(question="<суть задачи>", mode="compact")`**
3. Если `fresh: false` — сообщить пилоту и использовать локальный fallback (`grep` по `FPF/`)

### Что делать с ответом

- Поле `ids` — включить в frontmatter артефакта (`fpf_context: ["A.15", "C.11"]`)
- Поле `constraints` — проверить перед финализацией артефакта
- Поле `gaps` — вынести в раздел «Вопросы / Требует проверки»

### Режимы задач → ожидаемые FPF-паттерны

| Тип задачи | Триггер | Ключевые паттерны |
|---|---|---|
| Создание CASE | Новый файл в `cases/` | A.6.P (precision), C.16 (measurement), C.26.1 (probe-coupled) |
| Создание DL | Новый файл в `decisions/` | A.15 (role-method-work), C.11 (decision theory), B.3 (F-G-R), A.6.B (L/A/D/E) |
| Создание RULE | Новый файл в `pack/rules/` | A.6 (boundary), A.2.8 (commitment), A.6.C (contract unpacking), B.4 (evolution loop) |
| SoTA-аннотация | Работа с `06-sota/` | A.10 (evidence graph), B.3 (trust), C.2 (KD-CAL), A.6.3.CSC (coarsening) |
| Сравнение вариантов | «сравни», «оцени», «выбери» | A.17-A.19 (CSLC), C.11 (Decsn-CAL), B.5 (ADI) |

---

## Commit Attribution

При коммитах с участием Kimi:
```bash
git commit -m "feat: description" --trailer "Co-Authored-By: Kimi <noreply@moonshot.ai>"
```

---

*AGENTS.md для PACK-cattle-science. Действует в рамках этого репозитория.*
