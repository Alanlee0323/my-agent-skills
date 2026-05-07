---
name: attributing-portfolio-performance
description: 對投資組合的績效進行多層歸因分析（Alpha/Beta 分離、技能層歸因、決策品質評分），並將結論回饋至上游技能以驅動系統自我進化。這是整條分析鏈的「閉環終端」——沒有它，系統只會重複犯同樣的錯誤。
---

# Attributing Portfolio Performance

## When to use this skill
- 每月定期執行一次（月度績效回顧）。
- 每季進行深度歸因（季度策略檢視）。
- 當組合發生重大虧損（單月 > -10% 或單標的 > -20%）時立即觸發。
- 當 `conducting-investment-postmortem` 需要系統性歸因數據作為輸入。
- 當用戶問「我的報酬是 alpha 還是純粹 beta？」。

## Workflow

1. Plan
- 確認回顧期間（月度/季度/年度/自定義）。
- 收集必要數據：
  - 期初/期末持倉快照（標的、股數、成本、市值）
  - 期間所有交易紀錄（買入/賣出/時間/價格）
  - 基準指數報酬（S&P 500, TAIEX, 自定義混合基準）
  - 期間的宏觀環境紀錄（來自歷史 macro snapshots）
  - 期間的分析報告/決策紀錄（來自歷史 reports）
- 確認歸因框架（見下方三層模型）。

2. Execute — 三層歸因模型

  ### Layer 1：Alpha / Beta 分離 (Return Attribution)

  **目的：** 你的報酬有多少來自「大盤上漲（Beta）」，有多少來自「你的選股/擇時能力（Alpha）」？

  **計算方法：**
  ```
  組合總報酬 = Alpha + Beta 報酬 + 殘差

  Beta 報酬 = 組合 Beta × 基準報酬
  Alpha = 組合總報酬 - Beta 報酬

  其中：
  - 組合 Beta = 加權平均 Beta（各標的 beta × 權重）
  - 基準報酬 = 混合基準（美股部位 vs S&P 500, 台股部位 vs TAIEX）
  ```

  **Alpha 分解：**
  - **選股 Alpha (Stock Selection)：** 在同一產業中，你選的標的 vs 產業平均表現的差異
  - **擇時 Alpha (Market Timing)：** 你的現金/股票比例調整帶來的超額報酬
  - **配置 Alpha (Sector Allocation)：** 你偏重/偏低某些產業帶來的超額報酬

  **報酬品質矩陣：**
  | Alpha | Beta | 解讀 | 行動 |
  |---|---|---|---|
  | 正 | 正 | 🌟 選股+順勢，最佳狀態 | 維持策略 |
  | 正 | 負 | 💪 逆勢有 alpha，能力強 | 提高信心度 |
  | 負 | 正 | ⚠️ 只是搭順風車，選股差 | 檢討選股流程 |
  | 負 | 負 | 🚨 全面失敗 | 立即觸發 postmortem |

  ### Layer 2：Pipeline 技能層歸因 (Skill-Level Attribution)

  **目的：** 當報酬不如預期時，追溯是哪個技能環節出了問題。

  **歸因框架：**
  | 技能環節 | 評估問題 | 失敗模式 | 證據來源 |
  |---|---|---|---|
  | `scanning-macro-news` | 是否遺漏了重大事件？ | 盲區型失敗 | 回顧期間的新聞 vs 掃描紀錄 |
  | `validating-financial-data` | 是否有錯誤數據流入分析？ | GIGO 失敗 | 驗證報告 vs 實際數據 |
  | `analyzing-macro-regime` | 體制判斷是否正確？ | 方向性失敗 | 體制報告 vs 實際體制 |
  | `analyzing-market-expectations` | 預期差判斷是否正確？ | 共識錯判 | 預期差報告 vs 實際價格走勢 |
  | `constructing-forward-scenarios` | 哪個情境實現了？機率估計是否合理？ | 機率校準失敗 | 情境推演 vs 實際路徑 |
  | `valuing-company` | 目標價是否合理？ | 估值錯誤 | 目標價 vs 實際價格 |
  | `sizing-portfolio-positions` | 倉位大小是否適當？ | 執行失敗 | 建議倉位 vs 實際損益分佈 |
  | `tracking-catalyst-calendar` | 催化劑是否被正確預判？ | 時機錯判 | 日曆 vs 實際催化事件 |

  **評分方法：**
  - 對每個技能環節，根據其預測/建議 vs 實際結果的偏差程度打分（1-5）
  - 1 = 完全正確
  - 3 = 部分正確
  - 5 = 完全錯誤或遺漏

  ### Layer 3：決策品質 vs 結果品質 (Process Quality Assessment)

  **目的：** 區分「決策品質」與「結果品質」——好決策可能有壞結果（運氣差），壞決策也可能有好結果（運氣好）。

  **2×2 決策矩陣：**
  ```
                     結果好          結果差
  決策好     ┌──────────────┬──────────────┐
             │  🌟 實力     │  📚 學費     │
             │  (繼續)       │  (檢查執行)   │
  決策差     ├──────────────┼──────────────┤
             │  🎰 運氣     │  🚨 失敗     │
             │  (不可複製)   │  (深度檢討)   │
             └──────────────┴──────────────┘
  ```

  **決策品質評估標準：**
  - 買入前是否完成完整分析鏈？（掃描→驗證→分析→sizing）
  - 是否設定了停損/證偽點？觸發時是否執行？
  - 是否在催化劑前後適當調整部位？
  - 是否因恐懼/貪婪偏離了原始計劃？

3. Validate
- **偏差分析：** 是否存在系統性偏差（總是在某個環節出錯）？
- **樣本量檢查：** 單月歸因可能受雜訊影響，季度/年度歸因更可靠。
- **基準適當性：** 使用的基準是否合理反映了組合的風險特徵？
- **倖存者偏差：** 是否忽略了已賣出的虧損部位？

4. Synthesize — 回饋與進化

  **回饋迴路 (Feedback Loop)：**

  a) **規則更新 (Rule Updates)**
  - 哪些技能環節需要調整參數？
    - 例：`stress-testing-portfolio` 的情境機率長期偏樂觀 → 調整預設機率分佈
    - 例：`sizing-portfolio-positions` 的 Kelly 勝率估計偏高 → 降低預設勝率
  - 哪些硬限制需要調整？
    - 例：單一產業 30% 上限在 AI 週期中反覆被挑戰 → 是否提高至 35%？

  b) **知識累積 (Knowledge Accumulation)**
  - 將「預測 vs 實際」的偏差模式記錄為歷史案例
  - 格式：`{情境, 預測, 實際, 偏差原因, 教訓}`
  - 存入 `research/` 或 session 資料庫中，供未來 `constructing-forward-scenarios` 參考
  - 建立「相似情境比對庫」——下次遇到類似宏觀環境時自動提示歷史偏差

  c) **技能校準分數 (Skill Calibration Score)**
  - 長期追蹤每個技能的預測準確度
  - 低準確度技能 → 降低其在下游決策中的權重
  - 高準確度技能 → 提高其影響力

## Instructions

- **誠實至上：** 歸因分析的價值取決於誠實程度。不可選擇性歸因（只歸因成功、忽略失敗）。
- **決策品質 > 結果品質：** 好決策壞結果不需要改流程；壞決策好結果必須檢討。
- Alpha/Beta 分離必須使用適當基準（美股用 S&P 500，台股用 TAIEX，混合組合用加權基準）。
- 月度回顧以 Layer 1（Alpha/Beta）為主；季度回顧加入 Layer 2（技能歸因）和 Layer 3（決策品質）。
- 回饋建議必須具體到「修改哪個技能的哪個參數」，不可泛泛說「要更保守」。
- 歸因結果必須存檔（建議存入 `my-holdings/{date}/for-ai/` 或 session 資料庫），供未來參考。
- 每次歸因後，檢查是否需要更新 `managing-long-term-investment-policy` 的長期政策。

### Output template

```markdown
## 📊 績效歸因報告 — <期間>

### 績效摘要
| 指標 | 組合 | 基準 | 差異 |
|---|---:|---:|---:|
| 總報酬 | ±X.X% | ±X.X% | ±X.X% |
| 年化波動率 | X.X% | X.X% | |
| 最大回撤 | -X.X% | -X.X% | |
| Sharpe Ratio | X.XX | X.XX | |

### Layer 1：Alpha / Beta 分離
| 成分 | 貢獻 | 解讀 |
|---|---:|---|
| Beta 報酬 | ±X.X% | <大盤貢獻> |
| 選股 Alpha | ±X.X% | <選股能力> |
| 擇時 Alpha | ±X.X% | <現金管理> |
| 配置 Alpha | ±X.X% | <產業配置> |
| **總 Alpha** | **±X.X%** | <綜合評價> |

### 報酬品質
- 類型：🌟 實力 / 💪 逆勢 / 🎰 運氣 / 🚨 失敗
- 解讀：<說明>

### Layer 2：技能層歸因
| 技能 | 評分 (1-5) | 說明 | 改進建議 |
|---|---|---|---|
| scanning-macro-news | X | <說明> | <建議> |
| validating-financial-data | X | <說明> | <建議> |
| analyzing-macro-regime | X | <說明> | <建議> |
| analyzing-market-expectations | X | <說明> | <建議> |
| constructing-forward-scenarios | X | <說明> | <建議> |
| valuing-company | X | <說明> | <建議> |
| sizing-portfolio-positions | X | <說明> | <建議> |

### Layer 3：決策品質審計
| 決策 | 品質 | 結果 | 分類 | 學習 |
|---|---|---|---|---|
| <買入 XXX> | 好/差 | 好/差 | 🌟/📚/🎰/🚨 | <教訓> |

### 回饋與進化建議

#### 規則更新
1. <技能>：<具體參數修改建議>

#### 知識累積
| 情境 | 預測 | 實際 | 偏差原因 |
|---|---|---|---|
| <情境> | <預測> | <實際> | <原因> |

#### 技能校準分數（滾動追蹤）
| 技能 | 本期 | 累計平均 | 趨勢 |
|---|---|---|---|
| <技能> | X.X | X.X | ↑/→/↓ |

### 下期重點
- 需要加強的環節：<列出>
- 需要調整的參數：<列出>
- 下次歸因日期：<date>
```

## Error handling

- 若缺乏完整交易紀錄，使用期初/期末持倉快照進行簡化歸因，並標記「⚠️ 簡化模式」。
- 若基準數據不可得，使用最接近的 ETF 作為替代基準。
- 若歷史分析報告缺失（無法進行 Layer 2 技能歸因），跳過 Layer 2 並建議未來存檔。
- 若回顧期間太短（< 1 月），降低歸因結論的信心度並標記「樣本不足」。
- 若歸因結果顯示長期系統性偏差（連續 3 期同方向），升級為「🚨 結構性問題」並強制觸發 `conducting-investment-postmortem`。

## Resources

- `conducting-investment-postmortem`（協同技能：單案深度檢討 vs 本技能的系統性歸因）
- `sizing-portfolio-positions`（上游技能：執行參數的品質直接影響本技能的歸因結果）
- `stress-testing-portfolio`（協同技能：壓力測試的預測準確度是歸因重點之一）
- `constructing-forward-scenarios`（協同技能：情境推演的準確度是歸因重點之一）
- `managing-long-term-investment-policy`（下游技能：歸因結論可能觸發長期政策調整）
- `collecting-market-data`（上游技能：提供基準與持倉的歷史數據）
