---
name: scanning-macro-news
description: 在執行任何投資分析或組合調整之前，主動上網搜尋當前宏觀經濟與地緣政治重大事件。這是一個「閘門技能」——確保所有下游分析都建立在最新現實之上，而非過時假設。
---

# Scanning Macro News

## When to use this skill
- **每次**開始投資分析、組合再平衡或撰寫投資報告之前（強制性前置步驟）。
- 當用戶詢問任何與市場相關的問題時，作為第一步執行。
- 當距離上次掃描已超過 24 小時。
- 當用戶明確要求更新宏觀環境資訊。

## Workflow

1. Plan
- 定義掃描範圍：全球宏觀（預設）或特定區域/主題。
- 確認上次掃描時間戳（若有）。
- 準備搜尋關鍵字清單。

2. Execute — 五軸掃描
- 依序（或平行）執行以下五個搜尋軸：

  **軸 1：地緣政治衝突與戰爭**
  - 搜尋：active military conflicts, sanctions, trade wars, Strait of Hormuz, Taiwan Strait
  - 重點：是否有新衝突爆發、現有衝突是否升級/降溫

  **軸 2：大宗商品與能源價格**
  - 搜尋：Brent crude oil price today, WTI oil price, gold price today, copper price
  - 重點：原油是否突破關鍵價位（$80/$100/$120）、黃金是否創新高

  **軸 3：央行政策與利率**
  - 搜尋：Fed funds rate decision, FOMC meeting, ECB rate, BOJ policy
  - 重點：下次會議日期、市場降息/升息預期、點陣圖變化

  **軸 4：經濟數據與衰退信號**
  - 搜尋：US nonfarm payrolls, CPI inflation, PMI manufacturing, unemployment rate
  - 重點：是否出現 stagflation（高通膨+低成長）信號

  **軸 5：市場情緒與系統性風險**
  - 搜尋：VIX index, S&P 500 trend, yield curve inversion, credit spreads
  - 重點：VIX 是否 >25（恐慌）、殖利率曲線是否倒掛

3. Validate
- 交叉驗證至少兩個來源的關鍵數據點。
- 標註數據時效性（< 24hr / < 7 days / stale）。
- 識別互相矛盾的信號。

4. Synthesize
- 產出一份精簡的 Macro Snapshot。
- 標記對當前持倉或分析目標的**直接影響**。
- 設定「紅色警報」閾值觸發條件。

## Instructions

- 使用 `web_search` 工具執行搜尋——不可僅依賴訓練數據中的記憶。
- 每個搜尋軸至少執行 1 次搜尋，關鍵軸（地緣政治、油價）執行 2 次。
- 搜尋結果必須包含具體數字（價格、利率、指數值）而非僅有敘述。
- 所有數據點標註來源與日期。
- 若發現重大事件（戰爭爆發、央行意外決議、原油 >$100），立即在 Snapshot 頂部標記 🚨 紅色警報。
- 掃描結果必須在後續分析中被引用——不可掃描後忽略。

### 紅色警報觸發條件
- 原油價格 > $100/桶
- VIX > 30
- 主要央行意外升息/降息
- 新軍事衝突爆發或現有衝突大規模升級
- 主要經濟體 PMI < 45（衰退區間）
- 信用利差急劇擴大（> 2 個標準差）

### Output template

```markdown
## 🌐 Macro Snapshot — <YYYY-MM-DD>

### 🚨 紅色警報
- <如有觸發條件，列於此處。無則標記「無活躍警報」>

### 五軸掃描摘要

| 軸 | 狀態 | 關鍵數據 | 趨勢 | 對持倉影響 |
|---|---|---|---|---|
| 地緣政治 | 🔴/🟡/🟢 | <事件摘要> | 升溫/持平/降溫 | <影響> |
| 大宗商品 | 🔴/🟡/🟢 | Brent $XX, Gold $XX | ↑/→/↓ | <影響> |
| 央行政策 | 🔴/🟡/🟢 | Fed X.XX%, 下次會議 MM/DD | 鷹/鴿/持平 | <影響> |
| 經濟數據 | 🔴/🟡/🟢 | NFP XXK, CPI X.X% | 擴張/放緩/收縮 | <影響> |
| 市場情緒 | 🔴/🟡/🟢 | VIX XX, S&P XXXX | 恐慌/中性/貪婪 | <影響> |

### 資料時效性
- 最新數據時間戳：<timestamp>
- 掃描完成時間：<timestamp>

### 下游分析影響
- <列出此宏觀環境對即將執行的分析/決策的具體影響>
```

## Error handling

- 若 web_search 工具不可用，明確標記「⚠️ 離線模式：以下分析基於訓練數據截止日，可能不反映最新事件」。
- 若某個搜尋軸無法取得數據，標記該軸為「數據缺失」並降低相關結論的信心度。
- 若搜尋結果互相矛盾，保留兩方數據並標記為「信號衝突」。

## Resources

- `analyzing-macro-regime`（下游技能：將掃描結果轉化為體制判斷）
- `stress-testing-portfolio`（下游技能：將掃描中的紅色警報轉化為壓力測試情境）
