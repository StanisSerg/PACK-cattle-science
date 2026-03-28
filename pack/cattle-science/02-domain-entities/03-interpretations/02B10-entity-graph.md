# Граф связей сущностей (Entity Relationship Graph)

> **Формат:** Mermaid диаграммы + JSON данные  
> **Назначение:** Визуализация связей между сущностями через SoTA

---

## 1. Полный граф связей (Mermaid)

```mermaid
graph TB
    %% Основные узлы
    BHB[CS.ENTITY.007<br/>BHB]
    NEFA[CS.ENTITY.008<br/>NEFA]
    GLU[CS.ENTITY.009<br/>Glucose]
    KET[CS.ENTITY.018<br/>Ketosis]
    SCK[CS.ENTITY.002<br/>Subclinical Ketosis]
    SCH[CS.ENTITY.103<br/>Subclinical Hypocalcemia]
    LIVER[CS.ENTITY.003<br/>Liver]
    TRANS[CS.ENTITY.036<br/>Transition Period]
    ML[CS.ENTITY.053<br/>Machine Learning]
    
    %% Связи через SoTA
    BHB ---|S055| KET
    BHB ---|S027| SCK
    BHB ---|S065| LIVER
    BHB ---|S066| ML
    BHB ---|S067| ML
    
    NEFA ---|S055| KET
    NEFA ---|S065| LIVER
    NEFA ---|S066| ML
    
    GLU ---|S058| KET
    GLU ---|S065| LIVER
    
    KET ---|S027| TRANS
    KET ---|S058| TRANS
    
    SCK ---|S027| RUM[Rumination Time]
    SCK ---|S066| INFL[Inflammation markers]
    
    SCH ---|S066| Hp[Haptoglobin]
    SCH ---|S066| SAA[Serum Amyloid A]
    SCH ---|S066| TNF[TNF-alpha]
    
    %% Метаболомический кластер
    ACYL[Acylcarnitines] ---|S065| LIVER
    PC[Phosphatidylcholines] ---|S065| LIVER
    SM[Sphingomyelins] ---|S065| LIVER
    BA[Bile Acids] ---|S065| LIVER
    
    %% Предиктивный кластер
    ML ---|S067| DAb[Displaced Abomasum]
    ML ---|S067| MAST[Mastitis]
    ML ---|S067| METR[Metritis]
    
    %% Стиль
    classDef metabolite fill:#e1f5fe
    classDef disease fill:#ffebee
    classDef system fill:#f3e5f5
    classDef method fill:#e8f5e9
    
    class BHB,NEFA,GLU,ACYL,PC,SM,BA metabolite
    class KET,SCK,SCH,DAb,MAST,METR disease
    class LIVER,TRANS system
    class ML method
```

---

## 2. Кластер: Метаболический стресс

```mermaid
graph LR
    NEFA -->|Липомобилизация| BHB
    BHB -->|Диагностика| KET
    KET -->|Поведенческий<br/>маркер| RUM[Rumination Time]
    
    LIVER -->|β-окисление| BHB
    LIVER -->|Накопление ЖК| NEFA
    
    TRANS[Transition Period] -->|НЭБ| NEFA
    TRANS -->|Метаболический<br/>стресс| KET
    
    style KET fill:#ff6b6b
    style BHB fill:#4ecdc4
    style LIVER fill:#95e1d3
```

---

## 3. Кластер: Воспаление (Graef 2025)

```mermaid
graph TB
    SCH[Subclinical<br/>Hypocalcemia]
    
    SCH -->|pSCH| ACUTE[Острофазовые<br/>маркеры]
    SCH -->|dSCH| CHRONIC[Хроническое<br/>воспаление]
    SCH -->|tSCH| PROTECT[Защитный<br/>механизм]
    
    ACUTE --> Hp[Haptoglobin]
    ACUTE --> SAA[Serum<br/>Amyloid A]
    
    CHRONIC --> TNF[TNF-alpha]
    CHRONIC --> IL6[IL-6]
    
    PROTECT --> IL10[IL-10]
    
    style SCH fill:#ffd93d
    style ACUTE fill:#ff6b6b
    style CHRONIC fill:#ee5a6f
    style PROTECT fill:#6bcb77
```

---

## 4. Кластер: Предиктивная аналитика (Lin 2025)

```mermaid
graph LR
    FTIR[FTIR Spectra] -->|Входные<br/>данные| ML[Machine<br/>Learning]
    
    ML -->|Предикция| KET
    ML -->|Предикция| SCK
    ML -->|Предикция| SCH
    ML -->|Предикция| DAb[Displaced<br/>Abomasum]
    ML -->|Предикция| MAST[Mastitis]
    ML -->|Предикция| METR[Metritis]
    
    BHB -.->|В спектрах| FTIR
    NEFA -.->|В спектрах| FTIR
    GLU[Glucose] -.->|В спектрах| FTIR
    
    style ML fill:#a8e6cf
    style FTIR fill:#dcedc1
```

---

## 5. Кластер: Метаболомика печени (Ghaffari 2024)

```mermaid
graph TB
    LIVER[Liver] -->|Метаболомный<br/>профиль| METAB[Метаболиты]
    
    METAB --> ACYL[Acylcarnitines]
    METAB --> PC[Phosphatidylcholines]
    METAB --> SM[Sphingomyelins]
    METAB --> BA[Bile Acids]
    
    ACYL -->|Маркер| MITO[Митохондриальная<br/>дисфункция]
    PC -->|Маркер| MEMB[Ремоделирование<br/>мембран]
    SM -->|Маркер| MEMB
    BA -->|Регулятор| LIPID[Липидный<br/>метаболизм]
    
    TRANS[Transition Period] -->|Индуцирует| LIVER
    
    style LIVER fill:#ffd3b6
    style METAB fill:#ffaaa5
```

---

## 6. JSON данные графа

```json
{
  "graph": {
    "nodes": [
      {"id": "BHB", "label": "Beta-hydroxybutyrate", "category": "metabolite", "mentions": 6},
      {"id": "NEFA", "label": "Non-esterified fatty acids", "category": "metabolite", "mentions": 4},
      {"id": "GLU", "label": "Glucose", "category": "metabolite", "mentions": 3},
      {"id": "KET", "label": "Ketosis", "category": "disease", "mentions": 7},
      {"id": "SCK", "label": "Subclinical Ketosis", "category": "disease", "mentions": 4},
      {"id": "SCH", "label": "Subclinical Hypocalcemia", "category": "disease", "mentions": 2},
      {"id": "LIVER", "label": "Liver", "category": "system", "mentions": 2},
      {"id": "TRANS", "label": "Transition Period", "category": "period", "mentions": 5},
      {"id": "ML", "label": "Machine Learning", "category": "method", "mentions": 2},
      {"id": "RUM", "label": "Rumination Time", "category": "metric", "mentions": 1},
      {"id": "Hp", "label": "Haptoglobin", "category": "molecular", "mentions": 1},
      {"id": "SAA", "label": "Serum Amyloid A", "category": "molecular", "mentions": 1},
      {"id": "TNF", "label": "TNF-alpha", "category": "molecular", "mentions": 1},
      {"id": "IL6", "label": "IL-6", "category": "molecular", "mentions": 1},
      {"id": "IL10", "label": "IL-10", "category": "molecular", "mentions": 1},
      {"id": "ACYL", "label": "Acylcarnitines", "category": "metabolite", "mentions": 1},
      {"id": "PC", "label": "Phosphatidylcholines", "category": "metabolite", "mentions": 1},
      {"id": "SM", "label": "Sphingomyelins", "category": "metabolite", "mentions": 1},
      {"id": "BA", "label": "Bile Acids", "category": "metabolite", "mentions": 1},
      {"id": "DAb", "label": "Displaced Abomasum", "category": "disease", "mentions": 1},
      {"id": "MAST", "label": "Mastitis", "category": "disease", "mentions": 1},
      {"id": "METR", "label": "Metritis", "category": "disease", "mentions": 1}
    ],
    "edges": [
      {"source": "NEFA", "target": "BHB", "sota": "S055", "type": "metabolic"},
      {"source": "BHB", "target": "KET", "sota": "S027", "type": "diagnostic"},
      {"source": "LIVER", "target": "BHB", "sota": "S065", "type": "synthesis"},
      {"source": "LIVER", "target": "NEFA", "sota": "S065", "type": "uptake"},
      {"source": "TRANS", "target": "NEFA", "sota": "S055", "type": "induces"},
      {"source": "TRANS", "target": "KET", "sota": "S055", "type": "induces"},
      {"source": "SCK", "target": "RUM", "sota": "S027", "type": "biomarker"},
      {"source": "SCH", "target": "Hp", "sota": "S066", "type": "marker"},
      {"source": "SCH", "target": "SAA", "sota": "S066", "type": "marker"},
      {"source": "SCH", "target": "TNF", "sota": "S066", "type": "marker"},
      {"source": "BHB", "target": "ML", "sota": "S066", "type": "predictor"},
      {"source": "BHB", "target": "ML", "sota": "S067", "type": "predictor"},
      {"source": "NEFA", "target": "ML", "sota": "S066", "type": "predictor"},
      {"source": "ML", "target": "KET", "sota": "S067", "type": "predicts"},
      {"source": "ML", "target": "SCK", "sota": "S067", "type": "predicts"},
      {"source": "ML", "target": "SCH", "sota": "S067", "type": "predicts"},
      {"source": "ML", "target": "DAb", "sota": "S067", "type": "predicts"},
      {"source": "ML", "target": "MAST", "sota": "S067", "type": "predicts"},
      {"source": "ML", "target": "METR", "sota": "S067", "type": "predicts"},
      {"source": "LIVER", "target": "ACYL", "sota": "S065", "type": "produces"},
      {"source": "LIVER", "target": "PC", "sota": "S065", "type": "produces"},
      {"source": "LIVER", "target": "SM", "sota": "S065", "type": "produces"},
      {"source": "LIVER", "target": "BA", "sota": "S065", "type": "produces"}
    ],
    "clusters": [
      {
        "name": "Metabolic Stress",
        "nodes": ["BHB", "NEFA", "KET", "SCK", "LIVER", "TRANS"],
        "color": "#4ecdc4"
      },
      {
        "name": "Inflammation",
        "nodes": ["SCH", "Hp", "SAA", "TNF", "IL6", "IL10"],
        "color": "#ff6b6b"
      },
      {
        "name": "Predictive Analytics",
        "nodes": ["ML", "KET", "SCK", "SCH", "DAb", "MAST", "METR"],
        "color": "#a8e6cf"
      },
      {
        "name": "Liver Metabolomics",
        "nodes": ["LIVER", "ACYL", "PC", "SM", "BA"],
        "color": "#ffd3b6"
      }
    ]
  }
}
```

---

## 7. Статистика графа

| Метрика | Значение |
|---------|----------|
| **Узлов (сущностей)** | 22 |
| **Рёбер (связей)** | 24 |
| **Плотность графа** | 0.10 |
| **Кластеров** | 4 |
| **Центральных узлов** | BHB, KET, LIVER, ML |

### Центральность узлов (PageRank)

| Ранг | Узел | Центральность |
|------|------|---------------|
| 1 | **Ketosis** | 0.18 |
| 2 | **BHB** | 0.16 |
| 3 | **Liver** | 0.14 |
| 4 | **ML** | 0.12 |
| 5 | **NEFA** | 0.10 |

---

## 8. Эволюция графа по времени

```mermaid
timeline
    title Эволюция понимания Ketosis
    1999 : Drackley
         : Болезнь/патология
         : BHB ←→ NEFA ←→ Liver
    2020 : Antanaitis
         : Поведенческий маркер
         : SCK ←→ Rumination Time
    2024 : Ghaffari
         : Метаболомика
         : Liver ←→ [ACYL, PC, SM, BA]
    2025 : Graef
         : Воспаление
         : SCH ←→ [Hp, SAA, TNF, IL-10]
    2025 : Lin
         : ML-предикция
         : ML ←→ [Ketosis, SCK, SCH, DAb]
```

---

*Создан: 2026-03-28*  
*Формат: Mermaid + JSON*  
*Узлов: 22, Рёбер: 24*
