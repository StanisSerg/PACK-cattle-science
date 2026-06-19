---
type: fpf-study
pattern: A.16
title: "Language-State Move Coordination: как знания движутся по состояниям"
domain: cattle-science
difficulty: advanced
reading_time: 40 min
created: 2026-06-19
---

# A.16 — Language-State Move Coordination

## 1. Зачем это читать

Знания не появляются сразу готовыми. Они движутся от наброска к стабильной форме, от нескольких вариантов к выбранному маршруту, от формализации к операционному использованию. A.16 называет допустимые ходы этого движения, чтобы не путать зрелость с авторитетностью.

**FPF-тезис:** *«Не «оно созрело». А notice → stabilize → route → formalize → operationalize, и обратно — reopen.»*

---

## 2. Семейство допустимых ходов

| Move | Что делает | Пример |
|---|---|---|
| **notice** | Сохранить low-articulation cue | Оператор заметил странный шум в доильном зале |
| **stabilize** | Сделать форму устойчивее | Cue pack: что, где, когда, свидетели |
| **route** | Опубликовать несколько/выбранный маршрут | Либо оборудование, либо корм, либо инфекция |
| **projection** | Частичная публикация одного аспекта | Оценить только кормовой фактор |
| **formalize** | Увеличить символическую структуру | Записать SOP-черновик |
| **operationalize** | Направить к методу/работе/гейту | Внедрить процедуру проверки |
| **reopen** | Снизить closure, вернуть соперников | Новые данные опровергли диагноз |
| **sketchBackoff** | Вернуться к exploratory form | Формализация была преждевременной |
| **respecify** | Сохранить семейство, сменить framing | «Не кетоз, а ацидоз» |
| **retire** | Явно вывести ветку из current use | Версия протокола устарела |

---

## 3. Три слоя после docking

После `route`, `projection`, `formalize`, `operationalize` должны быть различимы:

1. **Publication form** — `U.PreArticulationCuePack`, `RoutedCueSet`, `U.AbductivePrompt`, `U.EpistemePublication`…
2. **Governing pattern** — `A.16.1`, `B.4.1`, `B.5.2.0`, `A.6.P`, `A.15`…
3. **MVPK face** — `PlainView`, `TechCard`, `AssuranceLane`…

> Название face — не form. Название pattern — не form.

---

## 4. Authority states

После route work публикация находится в одном из четырёх состояний:

- **open plurality** — несколько направлений активны;
- **selected-route-before-endpoint-publication** — выбран маршрут, но ещё не endpoint pattern;
- **endpoint-pattern-publication-issued** — named pattern теперь управляет публикацией;
- **retired/withdrawn** — ветка больше не current.

---

## 5. Фермерские примеры

### 5.1 Инцидент в доильном зале

```text
notice       → operator hears unusual noise
stabilize    → cue pack: time, location, symptoms
route        → {equipment fault | feed issue | mastitis cluster}
operationalize → work order for equipment inspection
reopen       → inspection found no fault; reopen feed route
```

### 5.2 Новое кормовое исследование

```text
notice       → preliminary trial shows lower BHB
stabilize    → dataset + protocol version
route        → {publish as recommendation | require larger trial}
projection   → technical report for veterinarians
formalize    → peer-reviewed protocol
operationalize → update SOP_Ketosis_Treatment
retire       → later study contradicts; old recommendation retired
```

---

## 6. Контрольный чеклист

- `CC-A.16.1`: A.16 не переопределяет F (formality) и не публикует второй formality-only climb.
- `CC-A.16.2`: локальная move note может стоять сама; `A.16.0` не обязателен.
- `CC-A.16.3`: каждый move именует pre/post conditions через language-state facets.
- `CC-A.16.4`: publication form, governing pattern, face не смешаны.
- `CC-A.16.5`: route plurality внутри одного member ≠ lineage fork.
- `CC-A.16.6`: `respecify` не скрывает slot-explicit repair, который принадлежит другому pattern.
- `CC-A.16.7`: retreat/retirement явно обрабатывает witnesses и authority.
- `CC-A.16.8`: graph publication истории — `E.18`; A.16 управляет семантикой ходов.

---

## 7. Связи

- **A.16.0 U.LanguageStateMoveTrajectory** — тяжёлые истории.
- **A.16.1 U.PreArticulationCuePack** — ранняя preservation.
- **A.16.2 Reopen/SketchBackoff/Respecify** — отступление.
- **B.4.1 Route Publication** — публикация маршрутов.
- **B.5.2.0 Abductive Prompt** — cue-derived reasoning.
- **A.19 CharacteristicSpace** — позиции в языковом пространстве.
- **E.18 E.TGA** — граф publication путей.

---

*Capture написан по FPF-Spec.md §A.16 для PACK-cattle-science.*
