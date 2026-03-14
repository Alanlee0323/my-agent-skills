---
name: benchmarking-alumni
description: 分析目標學程的校友 5-10 年職涯路徑——職位、公司、薪資級距、地理分佈。用於驗證「這個學位真的能帶你到想去的地方」。
---

# Benchmarking Alumni

## When to use this skill
- 當使用者問「NTU AI 畢業生都去哪」
- 當需要驗證學程的就業承諾是否屬實
- 當需要建立畢業後的現實期望值
- 當在多個 offer 間猶豫，需要看「前人走過的路」

## Workflow

### 1. Plan
- 確認目標學程（學校 + 科系 + 畢業年份範圍）
- 確認分析維度（公司、職位、薪資、地理、升遷速度）
- 確定樣本目標（至少 30 位校友才有統計意義）

### 2. Collect
- LinkedIn 校友搜尋：`school:"NTU" AND "MSc AI" AND "MLOps"`
- 學校官方就業報告（Employment Report / Career Outcomes）
- Glassdoor/levels.fyi 公司薪資交叉比對
- 校友社群/論壇（Reddit、PTT、Telegram groups）
- 學校 Career Service 公開數據

### 3. Analyze
- **就業分佈**：FAANG / 金融 / 新創 / 顧問 / 學術 / 其他
- **地理分佈**：留在當地 / 回母國 / 去第三國
- **職位級距**：畢業即 Senior / 需要 2-3 年才 Senior
- **薪資區間**：P25 / P50 / P75（依公司類型）
- **升遷速度**：幾年到 Senior / Lead / Manager
- **跳板效果**：第一份工作 vs 5 年後的公司品牌提升

### 4. Validate
- 交叉比對 LinkedIn 資料與學校官方報告
- 注意 survivorship bias（LinkedIn 上活躍的人通常混得不錯）
- 區分「全職 offer」vs「合約/派遣」
- 注意 COVID/經濟週期對特定畢業年份的影響

## Instructions

- 至少收集 30 位校友資料才做統計推論
- 聚焦在與使用者背景相似的校友（台灣人、工程背景、AI 方向）
- 不要只看「最成功的人」，也要看「中位數的人」
- 「5 年後在哪」比「第一份工作在哪」更重要
- 標註資料收集方法與可能的 bias

### 校友分析框架

```
畢業 → 第一份工作 → 2年 → 5年 → 10年
  │        │          │      │       │
  └── 公司  └── 職位    └── 跳槽  └── 創業?
      薪資      城市        升遷      財務自由?
```

### Output template

```markdown
## 校友追蹤報告：<School> <Program>

### 樣本概述
| 項目 | 數據 |
|------|------|
| 樣本數 | N 位 |
| 畢業年份 | YYYY-YYYY |
| 資料來源 | LinkedIn + 官方報告 |
| 台灣人佔比 | ~X% |

### 就業分佈（第一份工作）
| 公司類型 | 比例 | 代表企業 | 平均起薪 |
|---------|------|---------|---------|
| FAANG | X% | ... | ... |
| 金融科技 | X% | ... | ... |
| 新創 | X% | ... | ... |

### 地理分佈
| 地區 | 比例 | 說明 |
|------|------|------|
| 留在當地 | X% | ... |
| 回台灣 | X% | ... |
| 第三國 | X% | ... |

### 5 年後的職涯樣貌
| 指標 | P25 | P50 | P75 |
|------|-----|-----|-----|
| 職位 | ... | ... | ... |
| 年薪 | ... | ... | ... |
| 管理人數 | ... | ... | ... |

### 成功案例 vs 中位數
- 🌟 Top case：...
- 📊 Median case：...
- ⚠️ Bottom case：...

### 結論
> <這個學位是否能帶你到想去的地方？>
```

## Error handling
- 若樣本 <30 人，標註「樣本不足，結論僅供參考」
- 若學程太新（<5 屆畢業生），改用同校相近科系的校友做 proxy
- 若 LinkedIn 搜尋結果被限制，標註「資料可能不完整」

## Resources
- `researching-programs` — 學程基本資訊
- `scanning-job-market` — 驗證校友就業市場是否仍然健在
- `evaluating-career-roi` — 校友薪資數據輸入 ROI 計算
