---
name: visualizing-data
description: Design methodology for charts, dashboards, and data visualizations in any medium or library — form selection by data relationship, a disciplined color system, decluttering rules, and finance-specific conventions. Use before writing any chart code or when the user mentions 圖表, 視覺化, 儀表板, dashboard, plot, chart, or 報告配圖.
version: 1.0.0
---

# Visualizing Data

在寫第一行繪圖程式碼**之前**先讀本 skill。圖表是論證，不是裝飾——
每張圖先回答「讀者要比較什麼」，再選圖型與顏色。

## When to use this skill

- 任何圖表/儀表板產出前（matplotlib、plotly、Recharts、ECharts、Excel、SVG 皆適用）。
- 金融報告配圖（估值敏感度、績效歸因、資產配置、情境比較）。
- 審查既有圖表的可讀性問題。

## 1. Form selection（先問關係，再選圖型）

| 讀者要看的關係 | 圖型 | 備註 |
|---|---|---|
| 類別間比較 | 橫/直條圖 | 類別多或名稱長 → 橫條；**數值軸必從 0 起** |
| 時間趨勢 | 折線圖 | 序列 >4 條改小倍數（small multiples），不要義大利麵圖 |
| 部分對整體 | 堆疊條 / 100% 堆疊 | 圓餅僅限 ≤4 類且差異明顯；環圈同理 |
| 分佈 | 直方圖 / 箱型圖 | 比較多組分佈用箱型或山脊圖 |
| 相關性 | 散佈圖 | 加趨勢線需標明方法；第三維用點大小勿用顏色漸層混類別 |
| 敏感度/情境 | 龍捲風圖 / 熱力表 | 估值敏感度首選（bear/base/bull 對照） |
| 單一 KPI | 大數字卡 + 微趨勢線 | 勿用儀表盤（gauge 浪費空間且難比較） |

**先想「這張圖的一句話結論」**；說不出來的圖不該存在，改用表格或刪除。
精確查值需求 → 表格；模式與比較需求 → 圖。

## 2. Color system（顏色是編碼，不是裝飾）

- 單一序列：一個中性主色即可，**不要**每根條子不同色（顏色無資訊時是雜訊）。
- 類別色：最多 5–6 色；超過 → 合併長尾為「其他」或改小倍數。
- 有序數值 → 循序色階（淺→深單一色相）；有正負/偏離基準 → 發散色階（雙色相過白）。
- 強調：全圖灰階 + 唯一强調色，是最有力的「看這裡」手法。
- 同一報告內**同一實體永遠同一顏色**（跨圖一致的 series→color 映射表）。
- 色盲安全：紅綠對比必加第二編碼（形狀/標籤/深淺）；驗證工具過一次 deuteranopia。
- **市場慣例陷阱**：美股綠漲紅跌；**台股/陸股紅漲綠跌**——面向台灣讀者的金融圖表
  遵循紅漲綠跌，並在圖例明示，避免跨市場誤讀。

## 3. Declutter（每個元素都要付出注意力成本）

- 刪：3D 效果、背景色塊、重邊框、多餘格線（保留淺色水平線即可）、重複的軸標題。
- 直接標籤優於圖例（折線末端標名；條圖端點標值），圖例迫使讀者來回對照。
- 軸刻度取整、單位標在軸標題（「營收（億元）」）不逐點重複。
- 標題寫結論（「毛利率連續六季改善」）而非變數名（「毛利率趨勢圖」）。

## 4. Dashboard composition（多圖成系統）

- 資訊層級：KPI 卡（現況）→ 趨勢圖（怎麼來的）→ 明細表（下鑽），由上而下。
- 全版共用一套色彩映射與字級系統；同型圖表同尺寸對齊網格。
- 明暗雙主題時：勿用純黑/純白背景色硬編碼，顏色經對比度檢查（WCAG AA）。

## 5. Integrity（圖表誠信——不可協商）

- 條圖軸截斷 = 視覺說謊；必須從 0。折線圖可不從 0 但需明示範圍。
- 雙 Y 軸極易誤導，預設禁用；確需並列改上下兩張同寬圖。
- 資料來源與截止日期直接標在圖上（金融圖表必備，同 `analyzing-macro-regime` 的時效紀律）。

## Evolution Log

- 2026-07-04 v1.0.0 — Initial capture — 觸發事件: 差集分析發現庫內金融分析輸出鏈
  （storytelling/reviewing）完全沒有視覺化方法論；自 Claude Code 內建 dataviz 系統
  （form heuristic、color formula、declutter、one-system dashboards）蒸餾，並補上
  台美市場紅綠慣例相反的在地化警告。
