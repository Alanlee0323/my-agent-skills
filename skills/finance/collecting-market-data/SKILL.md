---
name: collecting-market-data
description: 主動收集即時市場數據（股價、大宗商品、匯率、債券殖利率、波動率指標），確保所有估值與組合分析都基於最新數據而非過時快照。
---

# Collecting Market Data

## When to use this skill
- 在執行任何估值（`valuing-company`）之前——確認目標價格為最新。
- 在執行組合再平衡之前——確認所有持倉的現價。
- 在撰寫投資報告之前——確認引用的數據為最新。
- 當距離上次數據收集超過交易日 1 天。
- 當用戶明確要求「更新到最新數據」。

## Workflow

1. Plan
- 確定需要收集的數據類別：
  - 個股價格（持倉 + 觀察清單）
  - 基準指數（S&P 500, NASDAQ, TAIEX, SOX）
  - 大宗商品（原油 Brent/WTI, 黃金, 銅）
  - 匯率（USD/TWD, DXY 美元指數）
  - 債券殖利率（US 2Y, 10Y, 30Y）
  - 波動率（VIX, MOVE 債券波動率指數）
- 確認目標日期（最近交易日 vs 指定日期）。
- 確認數據粒度（收盤價 vs 盤中即時）。

2. Execute — 分層收集
- **Layer 1：核心持倉價格**（優先級最高）
  - 使用 `web_search` 搜尋每個持倉標的的最新收盤價。
  - 搜尋模板：`"{TICKER} stock price today"` 或 `"{TICKER} 股價"`
  - 平行搜尋以提升效率（每次最多 5 個 ticker）。

- **Layer 2：基準與宏觀指標**
  - 搜尋：`"S&P 500 close today"`, `"VIX index"`, `"US 10 year treasury yield"`
  - 搜尋：`"Brent crude oil price"`, `"gold price per ounce"`, `"USD TWD exchange rate"`

- **Layer 3：衍生數據計算**
  - 計算各標的的漲跌幅（vs 前次記錄價格）。
  - 計算距離 Bear/Base/Bull 目標價的偏離百分比。
  - 計算持倉市值（股數 × 現價）與權重偏移。

3. Validate
- **多源交叉驗證**：對關鍵標的（權重 > 5% 的持倉），至少用 2 個來源確認價格。
- **合理性檢查**：單日漲跌幅 > 10% 的個股，搜尋確認是否有重大事件（財報、併購、監管）。
- **時間一致性**：確保所有價格為同一交易日（避免混用週五美股價與週一台股價）。

4. Output
- 產出結構化的 Market Data Snapshot。
- 標記與前次快照的差異。
- 標記需要關注的異常值。

## Instructions

- **必須使用 web_search 取得即時數據**——禁止僅依賴記憶中的價格。
- 美股收盤價以 NYSE/NASDAQ 官方收盤為準。
- 台股收盤價以 TWSE 官方收盤為準。
- 匯率使用中間價（非買入/賣出價）。
- 所有價格標註至小數點後 2 位。
- 若目標日為非交易日，使用最近前一交易日的收盤價並標註。
- 價格來源優先級：
  1. 官方交易所數據
  2. 主流財經網站（Yahoo Finance, Google Finance, MarketWatch）
  3. 財經新聞報導中引用的數據

### 異常值閾值
- 個股單日漲跌 > ±5%：標記 ⚠️ 並搜尋原因
- 個股單日漲跌 > ±10%：標記 🚨 並強制搜尋新聞
- 原油單日漲跌 > ±3%：標記 ⚠️
- VIX > 25：標記 ⚠️
- VIX > 35：標記 🚨

### Output template

```markdown
## 📊 Market Data Snapshot — <YYYY-MM-DD>

### 持倉價格
| Ticker | 名稱 | 收盤價 | vs 前次 | 漲跌% | vs Bear | vs Base | vs Bull | 備註 |
|---|---|---:|---:|---:|---:|---:|---:|---|
| <TICKER> | <名稱> | $XX.XX | $XX.XX | ±X.X% | ±X% | ±X% | ±X% | <異常標記> |

### 宏觀指標
| 指標 | 數值 | vs 前次 | 變動 | 狀態 |
|---|---:|---:|---:|---|
| S&P 500 | XXXX | XXXX | ±X.X% | 🟢/🟡/🔴 |
| VIX | XX.X | XX.X | ±X.X | 🟢/🟡/🔴 |
| Brent 原油 | $XX.XX | $XX.XX | ±X.X% | 🟢/🟡/🔴 |
| 黃金 | $XXXX | $XXXX | ±X.X% | 🟢/🟡/🔴 |
| US 10Y 殖利率 | X.XX% | X.XX% | ±X bp | 🟢/🟡/🔴 |
| USD/TWD | XX.XX | XX.XX | ±X.X% | 🟢/🟡/🔴 |

### 異常值警報
- <如有 ⚠️ 或 🚨 標記的項目，列出原因>

### 數據品質
- 來源：<列出使用的來源>
- 時間一致性：✅/⚠️
- 交叉驗證狀態：<已驗證/部分驗證/未驗證>
```

## Error handling

- 若 web_search 不可用，使用最後已知價格並標記為 `⚠️ 過期數據 — 最後更新 <date>`。
- 若兩個來源的價格差異 > 1%，標記為 `⚠️ 來源衝突` 並取官方交易所數據。
- 若某標的已停牌或下市，標記為 `🚫 停牌/下市` 並搜尋原因。
- 若為非交易時段（盤中），標註為盤中即時價並提醒尚未收盤。

## Resources

- `valuing-company`（下游技能：使用收集到的價格進行估值比較）
- `stress-testing-portfolio`（下游技能：使用收集到的數據作為壓力測試基準）
- `scanning-macro-news`（協同技能：宏觀指標與新聞掃描互補）
