# Ingestion Template

> Используйте этот шаблон для добавления новых статей

---

## Entry XXX: [Авторы] ([Год])

**Material:** [Название статьи]

**Authors:** [Фамилии авторов]

**Year:** [Год]

**Source Type:** [Тип источника]
- Peer-reviewed research (simulation study)
- Peer-reviewed research (field trial)
- Review article
- Meta-analysis
- Industry report

**Date Ingested:** [YYYY-MM-DD]

**Relevance:** 
- [Краткое описание релевантности для PACK-cattle-science]
- [Какие аспекты охватывает]

**Relevance Test:**
- [ ] Within bounded context? [YES/NO]
- [ ] Relates to identified entities? [YES/NO]
- [ ] Can be analyzed through distinctions? [YES/NO]

**Status:** [pending-analysis / analyzed / rejected]

**Initial Notes:**
- [Ключевые моменты из статьи]
- [Методология]
- [Основные выводы]

**Priority:** [High / Medium / Low]

**SoTA ID:** [CS.SOTA.XXX - будет присвоено при создании]

---

## Checklist для добавления статьи

- [ ] PDF скопирован в `new-articles/`
- [ ] Запущен `extract_pdf.py`
- [ ] Просмотрен `extraction_results.json`
- [ ] Заполнен ingestion log entry
- [ ] Создана SoTA-аннотация
- [ ] Создан метод/сущность (если применимо)

---

*Template version: 1.0*
