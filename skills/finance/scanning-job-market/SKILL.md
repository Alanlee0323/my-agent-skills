---
name: scanning-job-market
description: 掃描目標市場的 AI Infra / MLOps 職缺趨勢——薪資帶、技能需求、企業類型、成長性。用於評估留學目的地的就業前景。
---

# Scanning Job Market

## When to use this skill
- 當使用者問「新加坡 MLOps 現在需要什麼技能」
- 當需要了解特定市場的 AI 職缺供需
- 當需要比較不同城市/國家的薪資水平
- 當需要識別高需求技能以指導學習方向

## Workflow

### 1. Plan
- 確認目標市場（城市/國家）
- 確認目標職位（AI Infra Engineer、MLOps、Platform Engineer 等）
- 確認資訊需求（薪資、技能、企業類型、趨勢）

### 2. Collect
- 爬取主要求職平台：
  - 🇸🇬 新加坡：MyCareersFuture、LinkedIn Singapore、NodeFlair
  - 🇬🇧 英國：LinkedIn UK、Indeed UK、Glassdoor UK
  - 🇹🇼 台灣：104、CakeResume、LinkedIn Taiwan
  - 🌐 全球：levels.fyi、Glassdoor、Blind
- 收集薪資報告：Morgan McKinley、Robert Half、Hays
- 查詢政府統計：SG MOM、UK ONS、TW DGBAS

### 3. Analyze
- 薪資分佈：P25 / P50 / P75 / P90
- 技能需求頻率：Top 10 required skills
- 企業類型分佈：FAANG / 金融 / 新創 / 傳產
- YoY 趨勢：職缺數量、薪資漲幅
- 供需缺口：需求成長率 vs 人才供給

### 4. Validate
- 交叉比對至少 2 個薪資來源
- 區分 base salary vs total compensation（含 bonus/RSU）
- 確認資料年份與幣別

## Instructions

- 薪資一律報告「稅前年薪」+「估計稅後月收」+「扣生活費後可投資」
- 技能需求要區分「必備」vs「加分」
- 不要只看當下，要看 3 年趨勢（是在漲還是在跌）
- 標註資料來源與時間戳
- 將技能需求與目標學程的課程做交叉比對

### 技能分類框架
| 類別 | 技能 |
|------|------|
| Cloud & Infra | AWS/GCP/Azure、Terraform、Kubernetes |
| ML Pipeline | MLflow、Kubeflow、Airflow、DVC |
| Data | Spark、dbt、Delta Lake、Iceberg |
| LLM/GenAI | LangChain、RAG、Fine-tuning、vLLM |
| Monitoring | Prometheus、Grafana、Weights & Biases |
| Languages | Python、Go、Rust、SQL |
| Soft Skills | System Design、Communication、Project Lead |

### Output template

```markdown
## 職缺市場掃描：<Market> <Role>

### 薪資分佈
| 級距 | 年薪（稅前） | 稅後月收 | 可投資/月 |
|------|------------|---------|----------|
| P25 (Junior) | ... | ... | ... |
| P50 (Mid) | ... | ... | ... |
| P75 (Senior) | ... | ... | ... |
| P90 (Lead) | ... | ... | ... |

### Top 10 需求技能
| # | 技能 | 出現頻率 | 必備/加分 |
|---|------|---------|----------|
| 1 | ... | ...% | 必備 |

### 主要僱主
| 類型 | 代表企業 | 薪資帶 |
|------|---------|-------|
| FAANG | ... | ... |
| 金融 | ... | ... |
| 新創 | ... | ... |

### 3 年趨勢
- 職缺數量：...
- 薪資漲幅：...
- 新興需求：...

### 與學程對齊建議
- 🟢 已覆蓋：...
- 🔴 需自學補強：...
```

## Error handling
- 若職缺數量太少（<50），標註「樣本不足」
- 若薪資數據來自自報平台（Glassdoor），標註可能的 selection bias
- 若市場正在快速變化（如 AI 泡沫），標註趨勢不確定性

## Resources
- `researching-programs` — 課程與技能對齊
- `evaluating-career-roi` — 薪資數據輸入 ROI 計算
- `comparing-visa-policies` — 工作簽證是否允許該職位
