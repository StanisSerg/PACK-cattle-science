---
wp: 109
type: fpf-pass
seminar: 3
date: 2026-08-01
patterns: [A.3.1, A.3.2]
project: "Система контроля отчётов технологов — переход 4→5"
status: captured
---

# Полный проход через корпус FPF: A.3.1 / A.3.2 → метод «Замер и внесение данных при посещении»

> Цель файла: показать, что корпус FPF реально выдаёт на один поставленный вопрос —
> сырой ответ (дословно) + применение к проекту. Прогон по запросу из сессии 2026-08-01.

## 1. Запрос (шаблон, по форме практикумов семинара 3)

```
В моём проекте «Система контроля отчётов технологов» есть разорванный
переход 4→5 большой P2W-развёртки: метод «замер и внесение данных при
посещении хозяйства» существует только как моя ручная практика и не
оформлен как передаваемый способ, который могут выполнять помощники.

Используя FPF:
1. Открой A.3.1 (U.Method) и A.3.2 (U.MethodDescription) и дай точные
   обязательства (Solution) обоих паттернов: что обязано содержать
   заявление метода и что обязано содержать его описание, чтобы другой
   человек выполнил метод без автора.
2. Примени эти обязательства к моему методу: составь method claim
   (participant meanings, applicability, conditions, intended effect,
   bounds, ближайшая остановка) и перечень необходимых MethodDescription.
3. Не выдумывай факты проекта; где не хватает сведений — явный пробел.
   Не выдавай выбор паттерна за выбор предметного метода.
Пиши ответ в файл.
```

Механика прогона: `query_fpf_spec` в режиме `proof` (нормативные формулировки с цитатами) — два запроса, по одному на паттерн.

## 2. Сырой ответ корпуса

### 2.1 A.3.1 U.Method (proof, confidence 0.98; цитаты: A.3.1:4, :12, :7, :1)

> A U.Method is: **semantically local**: its identity uses the declared participant meanings, applicability, conditions, intended effects or preserved conditions, and bounds; add an effective reference scheme and local senses only when a meaning difference would change the method identification or a stated comparison; **semantic**: it is the way of doing that descriptions denote and work may enact; **concern-explicit**: it states what a future enactment is intended to do or decide — change, observe, compare, classify, evaluate, communicate, select, derive, prove, control, produce, or preserve — and its intended effect or preserved condition; it identifies no actual changed referent, participant, occurrence, or result; **description-independent**: one method may be described by several U.MethodDescription epistemes; **run-independent**: one method may be enacted by many Work occurrences admitted under U.Work; **assignment-independent**: method admission conditions may name role kinds or capability-fit conditions, but named holders and dated assignments belong elsewhere; **participant-semantic**: it may state generic participant meanings and method-side applicability without declaring RelationSignature SlotSpecs, OperationAlgebra argument or result positions, planned fillers, or actual participants.

**Таблица маршрутизации (что куда относится — из того же ответа):**

| Объект | Куда в FPF |
|--------|-----------|
| Способ действия (semantic way of doing) | **A.3.1 U.Method** |
| Описание способа: SOP, программа, протокол, диаграмма, рецепт | **A.3.2 U.MethodDescription** |
| Назначение роли, ответственность, «кто делает» | A.2, A.2.1, A.2.7, A.15 |
| Плановая датированная работа | A.15.2 U.WorkPlan |
| Фактический запуск, прогон, журнал | A.15.1 U.Work |
| Композиция методов с порядком | B.1.5 |
| Непонятный ярлык («практика», «школа», «традиция») | оставить unresolved → A.1.1 / C.36.P |

Координация: A.3.2 (описания), A.3.3 (динамика), B.1.5 (композиция), G.5 (семейства методов). Informs: E.18 и E.18.1 — когда формулировки потока/P2W обязаны держать описания, методы и работы раздельно.

### 2.2 A.3.2 U.MethodDescription (proof, confidence 0.98; цитаты: A.3.2:4.1, :4, :12, :7, :4.3)

> Membership holds when the already identified episteme has one admitted U.Method as its exact EntityOfConcern and its claims, interpreted under the effective U.ReferenceScheme, make at least one substantive claim about that method as a way of doing.

> An assertion or description episteme about one dated Work occurrence may cite methodDescriptionRef when its claim depends on that description edition.

> Classify the episteme as U.MethodDescription only after its claim and admitted Method pass **CC-A3.2-1** and **CC-A3.2-2**.

> The episteme must make at least one substantive claim about the method as a way of doing, such as its transformation or enactment concern, generic participant meanings, [applicability, conditions, effects].

**Перевод на русский рабочий:** описание считается MethodDescription, только если (1) его предмет — ровно один допущенный метод и (2) в нём есть хотя бы одно содержательное утверждение о методе как о способе действия (концерн, участники, применимость, условия, эффект). Протокол/журнал конкретного запуска — не описание метода, а эпистема о Work (A.15.1), которая может ссылаться на редакцию описания через methodDescriptionRef.

## 3. Применение к проекту (подстановка «яблок из жизни»)

### 3.1 Method claim — «Замер и внесение данных при посещении»

| Элемент (обязательства A.3.1) | Содержание |
|-------------------------------|-----------|
| **Способ (way of doing)** | При посещении технолог выполняет замер (СВ, Пенсильванские сита, навозные сита, жвачка, молоко из компьютера, реализация из журнала) и вносит данные в два приёмника: АМТС — до отъезда; markdown-запись кейса — до конца недели; корректирует рацион в рамках основного рациона |
| **Participant meanings** | технолог (роль); зоотехник хозяйства (согласование); ведущий технолог (владелец основного рациона) — kind'ы ролей, без имён |
| **Applicability** | Хозяйства на сопровождении с регулярными визитами технолога (обычно 1/нед, индивидуально 2/нед – 1/2 нед); корректировки в рамках основного рациона |
| **Conditions** | Основной рацион существует; АМТС доступна на месте; markdown-шаблон кейса опубликован; канал связи с ведущим технологом для эскалации |
| **Intended effect (concern-explicit)** | change + preserve: данные замера сохранены в системе (2a + 2b), рацион скорректирован и согласован в день визита; цепочка «замер → данные → корректировка» замыкается без ведущего технолога в рутине |
| **Bounds** | Выход за рамки основного рациона — вне метода (эскалация ведущему); внедрение без согласования зоотехника — вне метода |
| **Ближайшая остановка** (local method mantra) | АМТС недоступна или данные неполные → стоп; markdown-фиксация «неполный замер»; уведомление ведущего; корректировка не выполняется по памяти |
| **Reference scheme / local senses** | _пробел_: по A.3.1 добавляется только если разница смыслов меняет идентификацию метода — пока основания нет |

**Три независимости, применённые к нам:** описания (чек-лист, шаблон, инструкция АМТС) — отдельные эпистемы, живут своими редакциями; каждый конкретный визит — Work (A.15.1), метод не «сгорит» от одного пропущенного визита; назначение конкретного технолога на хозяйство — A.2/A.15, в метод не вписывать.

### 3.2 Необходимые U.MethodDescription (по A.3.2 — каждое про один метод, с содержательным claim о способе)

| # | Описание | Содержательный claim (что делает его MethodDescription) | Статус |
|---|----------|----------------------------------------------------------|--------|
| D1 | Чек-лист визита | Порядок замера и правило «2a до отъезда»; пункты с наблюдаемыми признаками и ценой пропуска (слайд 146) | не создан |
| D2 | Markdown-шаблон замера | Структура записи кейса: показатели, связь с датой визита и хозяйством; правило «до конца недели» | не создан |
| D3 | Инструкция внесения в АМТС | Какие поля, как сохранить рацион, как проверить, что корректировка в рамках основного | не создан |
| D4 | Правило эскалации | Границы bounds: что считается выходом за рамки основного рациона, формат уведомления ведущего | не создан |

### 3.3 Что методом НЕ является (маршрутизация из 2.1)

- «Обучить технологов до конца августа» → **A.15.2 U.WorkPlan** (+ gate/commitment паттерны).
- Конкретный визит 05.08 → **A.15.1 U.Work**; его журнал — эпистема о Work, ссылающаяся на редакцию D1–D4 через methodDescriptionRef.
- Назначение технолога N на хозяйство X → **A.2/A.2.1/A.2.7** (+ A.2.2, если нужен порог способностей).

## 4. Честная остановка и следующий ход

Результат прогона: method claim собран, перечень описаний определён — **но ничего не утверждено и не создано** (эскиз ≠ метод). Следующая работа большой P2W (поз. 6–7): написать D1–D4, договориться с технологами, пробный визит (U.Work) — кандидат в отдельный РП «Метод внесения данных замера».

*Создано: 2026-08-01, сессия WP-109. Прогон выполнен через mcp__fpf_reference (актуальная compiled-версия корпуса).*
