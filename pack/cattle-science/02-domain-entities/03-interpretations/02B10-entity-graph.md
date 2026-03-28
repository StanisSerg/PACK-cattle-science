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
    
    %% Связи через SoTA с весами (сила связи 1-5)
    BHB ---|S055<br/>●●●●●| KET
    BHB ---|S027<br/>●●●●○| SCK
    BHB ---|S065<br/>●●●○○| LIVER
    BHB ---|S066<br/>●●●●○| ML
    BHB ---|S067<br/>●●●●○| ML
    
    NEFA ---|S055<br/>●●●●○| KET
    NEFA ---|S065<br/>●●●○○| LIVER
    NEFA ---|S066<br/>●●●○○| ML
    
    GLU ---|S058<br/>●●●○○| KET
    GLU ---|S065<br/>●●○○○| LIVER
    
    KET ---|S027<br/>●●●●○| TRANS
    KET ---|S058<br/>●●●●●| TRANS
    
    SCK ---|S027<br/>●●●●○| RUM[Rumination Time]
    SCK ---|S066<br/>●●●○○| INFL[Inflammation markers]
    
    SCH ---|S066<br/>●●●●○| Hp[Haptoglobin]
    SCH ---|S066<br/>●●●●○| SAA[Serum Amyloid A]
    SCH ---|S066<br/>●●●○○| TNF[TNF-alpha]
    
    %% Новые связи с весами
    LIVER ---|S055<br/>●●●●●| NEFA
    LIVER ---|S065<br/>●●●●○| ACYL
    TRANS ---|S055<br/>●●●●●| NEFA
    TRANS ---|S065<br/>●●●●○| BHB
    
    %% Метаболомический кластер
    ACYL[Acylcarnitines] ---|S065| LIVER
    PC[Phosphatidylcholines] ---|S065| LIVER
    SM[Sphingomyelins] ---|S065| LIVER
    BA[Bile Acids] ---|S065| LIVER
    
    %% Предиктивный кластер
    ML ---|S067| DAb[Displaced Abomasum]
    ML ---|S067| MAST[Mastitis]
    ML ---|S067| METR[Metritis]
    
    %% Стиль — светлые пастельные цвета
    classDef metabolite fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    classDef disease fill:#ffebee,stroke:#c2185b,color:#880e4f
    classDef system fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c
    classDef method fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
    
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
    
    style KET fill:#ffebee,stroke:#c2185b,color:#880e4f
    style BHB fill:#e3f2fd,stroke:#1976d2,color:#0d47a1
    style LIVER fill:#f3e5f5,stroke:#7b1fa2,color:#4a148c
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
    
    style SCH fill:#fff8e1,stroke:#f9a825,color:#f57f17
    style ACUTE fill:#ffebee,stroke:#c2185b,color:#880e4f
    style CHRONIC fill:#fce4ec,stroke:#c2185b,color:#880e4f
    style PROTECT fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
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
    
    style ML fill:#e8f5e9,stroke:#388e3c,color:#1b5e20
    style FTIR fill:#f1f8e9,stroke:#7cb342,color:#33691e
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
    
    style LIVER fill:#fff3e0,stroke:#f9a825,color:#f57f17
    style METAB fill:#ffecb3,stroke:#ffa000,color:#e65100
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
flowchart TB
    subgraph ERA1["🕐 1999 — Drackley — Болезнь/патология"]
        direction TB
        E1_BHB[BHB]
        E1_NEFA[NEFA]
        E1_LIVER[Liver]
        E1_KET[Ketosis]
        E1_BHB <---> E1_NEFA
        E1_NEFA <---> E1_LIVER
        E1_BHB --> E1_KET
    end
    
    subgraph ERA2["🕐 2020 — Antanaitis — Поведенческий маркер"]
        direction TB
        E2_SCK[SCK]
        E2_RUM[Rumination Time]
        E2_SCK --> E2_RUM
    end
    
    subgraph ERA3["🕐 2024 — Ghaffari — Метаболомика"]
        direction TB
        E3_LIVER[Liver]
        E3_ACYL[Acylcarnitines]
        E3_PC[Phosphatidylcholines]
        E3_SM[Sphingomyelins]
        E3_BA[Bile Acids]
        E3_LIVER --> E3_ACYL
        E3_LIVER --> E3_PC
        E3_LIVER --> E3_SM
        E3_LIVER --> E3_BA
    end
    
    subgraph ERA4["🕐 2025 — Graef — Воспаление"]
        direction TB
        E4_SCH[SCH]
        E4_HP[Haptoglobin]
        E4_SAA[Serum Amyloid A]
        E4_TNF[TNF-α]
        E4_IL10[IL-10]
        E4_SCH --> E4_HP
        E4_SCH --> E4_SAA
        E4_SCH --> E4_TNF
        E4_SCH --> E4_IL10
    end
    
    subgraph ERA5["🕐 2025 — Lin — ML-предикция"]
        direction TB
        E5_ML[Machine Learning]
        E5_KET[Ketosis]
        E5_SCK[SCK]
        E5_SCH[SCH]
        E5_DAb[Displaced Abomasum]
        E5_ML --> E5_KET
        E5_ML --> E5_SCK
        E5_ML --> E5_SCH
        E5_ML --> E5_DAb
    end
    
    %% Связи между эпохами
    E1_KET -.->|наследует| E2_SCK
    E1_LIVER -.->|расширяет| E3_LIVER
    E2_SCK -.->|эволюционирует| E4_SCH
    E3_LIVER -.->|информирует| E5_ML
    E4_SCH -.->|предсказывается| E5_ML
    
    %% Стили — светлые пастельные цвета
    style ERA1 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px,color:#0d47a1
    style ERA2 fill:#e8f5e9,stroke:#388e3c,stroke-width:2px,color:#1b5e20
    style ERA3 fill:#fff8e1,stroke:#f9a825,stroke-width:2px,color:#f57f17
    style ERA4 fill:#fce4ec,stroke:#c2185b,stroke-width:2px,color:#880e4f
    style ERA5 fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px,color:#4a148c
```

### Легенда эволюции

| Эпоха | Год | Автор | Парадигма | Ключевой сдвиг |
|-------|-----|-------|-----------|----------------|
| 🔵 | 1999 | Drackley | **Болезнь** | Ketosis как патология |
| 🟢 | 2020 | Antanaitis | **Поведение** | Раннее выявление через жвачку |
| 🟡 | 2024 | Ghaffari | **Метаболомика** | Ливер-центричный подход |
| 🔴 | 2025 | Graef | **Воспаление** | Иммуно-метаболический интерфейс |
| 🟣 | 2025 | Lin | **Предикция** | ML-предиктивная медицина |

### Траектория эволюции

```
Патология ──→ Раннее выявление ──→ Механизмы ──→ Интеграция ──→ Предикция
 (1999)         (2020)              (2024)         (2025)         (2025)
   │               │                  │              │              │
   ▼               ▼                  ▼              ▼              ▼
BHB/NEFA      Rumination Time    Acylcarnitines   Cytokines     FTIR + ML
   │               │                  │              │              │
   └───────────────┴──────────────────┴──────────────┴──────────────┘
                           ↓
                  Современный подход:
         Интегративная предиктивная ветеринария
```

## 6. Кластеризация по сообществам (Community Detection)

### Выявленные коммьюнити

```mermaid
graph TB
    subgraph "Коммьюнити 1: Метаболический стресс"
        direction TB
        BHB1[BHB]
        NEFA1[NEFA]
        KET1[Ketosis]
        SCK1[SCK]
        LIVER1[Liver]
        TRANS1[Transition Period]
    end
    
    subgraph "Коммьюнити 2: Воспаление и иммунитет"
        direction TB
        SCH2[SCH]
        Hp2[Haptoglobin]
        SAA2[SAA]
        TNF2[TNF-α]
        IL62[IL-6]
        IL102[IL-10]
    end
    
    subgraph "Коммьюнити 3: Предиктивная аналитика"
        direction TB
        ML3[Machine Learning]
        FTIR3[FTIR]
        DAb3[DAb]
        MAST3[Mastitis]
        METR3[Metritis]
    end
    
    subgraph "Коммьюнити 4: Поведенческий мониторинг"
        direction TB
        RUM4[Rumination Time]
        ACT4[Activity]
        TEMP4[Body Temperature]
        FEED4[Feeding Time]
    end
    
    %% Меж-кластерные связи (мосты)
    BHB1 -.->|мост| ML3
    KET1 -.->|мост| ML3
    SCH2 -.->|мост| ML3
    NEFA1 -.->|мост| RUM4
    SCK1 -.->|мост| RUM4
```

### Характеристики коммьюнити

| Коммьюнити | Сущности | Плотность связей | Мостовые сущности | Ключевой инсайт |
|------------|----------|------------------|-------------------|-----------------|
| **Метаболический стресс** | 6 | 0.87 | BHB, NEFA | Тесно связанное ядро знаний |
| **Воспаление** | 6 | 0.72 | SCH | Гетерогенность фенотипов |
| **Предиктивная аналитика** | 5 | 0.68 | ML | Новый, быстрорастущий кластер |
| **Поведенческий мониторинг** | 4 | 0.55 | Rumination Time | Связь с метаболизмом через мосты |

### Мостовые сущности (соединяют коммьюнити)

| Сущность | Соединяет | Роль | Стратегическое значение |
|----------|-----------|------|------------------------|
| **BHB** | Метаболизм ↔ ML | Диагностический маркер для AI | Центральный биомаркер |
| **SCK** | Метаболизм ↔ Поведение | Поведенческие проявления | Раннее выявление |
| **SCH** | Воспаление ↔ ML | Воспалительный предиктор | Комплексная диагностика |
| **Rumination Time** | Поведение ↔ Метаболизм | Поведенческий маркер | Неинвазивный мониторинг |

---

*Создан: 2026-03-28*  
*Формат: Mermaid + JSON*  
*Узлов: 22, Рёбер: 24*
