---
type: prompt-template
source: FPF seminar 01, slide 41
topic: "Entity of Concern identification"
usage: "Copy the prompt, replace [one phrase] with a concrete project problem, attach FPF file"
---

# Prompt template: Identify Role, EntityOfConcern, and BoundedContext

## When to use

Use this prompt when you have a practical project situation but are unsure:
- which role you are acting in;
- what the `EntityOfConcern` is;
- what the `boundedContext` should be.

This template prevents overly broad requests like "improve my whole project".

## Prompt

```text
Используй приложенный FPF. Для такой задачи моего текущего проекта: [{{problem_one_liner}}]. Найди подходящую карточку README и предложи, в какой роли я сейчас действую, что является интересующей сущностью (EntityOfConcern) и какой ограниченный контекст (boundedContext) нужен для рассуждения. Начни ответ ровно с трёх коротких строк: Роль: …, Интересующая сущность: …, Ограниченный контекст: ….
```

## Parameter

- `{{problem_one_liner}}` — one concrete sentence describing the current problem or question.

## Example

```text
Используй приложенный FPF. Для такой задачи моего текущего проекта: падает продуктивность группы коров 3-й лактации после изменения рациона на ферме МТК Ленинский в июле 2026. Найди подходящую карточку README и предложи, в какой роли я сейчас действую, что является интересующей сущностью (EntityOfConcern) и какой ограниченный контекст (boundedContext) нужен для рассуждения. Начни ответ ровно с трёх коротких строк: Роль: …, Интересующая сущность: …, Ограниченный контекст: ….
```

## Expected output format

```text
Роль: …
Интересующая сущность: …
Ограниченный контекст: …
```

## Notes

- Attach the actual FPF file, do not paste it into the prompt.
- Use the strongest available model.
- Ask the agent to write the response into a separate markdown file.
