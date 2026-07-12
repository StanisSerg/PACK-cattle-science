---
type: prompt-template
source: FPF seminar 01
topic: "Select README card by priority"
usage: "Copy the prompt, replace [one phrase] with a concrete project problem, attach FPF file"
---

# Prompt template: List and prioritize relevant README cards

## When to use

Use this prompt when you want the agent to suggest relevant FPF README cards for your situation, sorted by priority, before you choose which pattern to apply.

This avoids artificially limiting the agent to a fixed number of cards and helps you see the full field of options.

## Prompt

```text
Используй приложенный FPF. Ситуация моего проекта: [{{problem_one_liner}}].

Найди подходящие карточки README из FPF. Отсортируй их по релевантности — от наиболее подходящей к менее подходящей. Для каждой карточки укажи:
- название карточки;
- типичную ситуацию, которую она покрывает;
- первый полезный результат;
- ведущий паттерн;
- kind результата;
- почему эта карточка подходит (или не подходит) к моей ситуации.

Если ни одна карточка не подходит явно, скажи об этом и предложи, какую часть ситуации нужно уточнить.

Не применяй паттерн и не давай готового решения. Мне нужно выбрать подходящий вариант.
```

## Parameter

- `{{problem_one_liner}}` — one concrete sentence describing the current problem or question, including EOC and bounded context if known.

## Example

```text
Используй приложенный FPF. Ситуация моего проекта: падает продуктивность группы коров 3-й лактации после изменения рациона на ферме МТК Ленинский в июле 2026.

Найди подходящие карточки README из FPF. Отсортируй их по релевантности — от наиболее подходящей к менее подходящей. Для каждой карточки укажи...
```

## Notes

- Attach the actual FPF file, do not paste it into the prompt.
- Use the strongest available model.
- Ask the agent to write the response into a separate markdown file.
- After reviewing the list, choose one card and ask the agent to apply its leading pattern.
