---
name: reviewing-code-changes
description: Reviews a diff or pending changes for correctness bugs using a findings-first discipline — hypothesize concrete failure scenarios, verify each finding against the code before reporting, rank by severity. Use when the user asks for code review, 審查程式碼, 找 bug, PR review, or before merging a branch.
version: 1.0.0
---

# Reviewing Code Changes

主動審查 diff 找正確性缺陷。核心紀律：**每個 finding 在報告前必須先驗證**——
未經驗證的直覺不是 finding，是雜訊；**空結果是合法結果**，硬湊 findings 比漏報更有害。

## When to use this skill

- 合併前審查自己或他人的 branch/PR diff。
- 使用者要求 code review、找 bug、檢查改動。
- 高風險改動（資料寫入、金流、部署腳本）的強制閘門。

## Workflow

### 1. Read the diff in context（帶上下文讀 diff）

- 不只讀改動行——讀被改動函式的完整定義、呼叫端、以及被改動行為的既有假設。
- 列出 diff 宣稱的意圖（來自 commit message / PR 描述），審查「實作是否兌現意圖」。

### 2. Hypothesize failure scenarios（假設具體失敗場景）

對每個改動點問：「什麼輸入/狀態會讓這段產生錯誤輸出或崩潰？」高產出檢查面：

- 邊界：空集合、None/null、零、負數、極大值、Unicode、時區。
- 狀態：並發、重入、部分失敗後的殘留狀態、順序依賴。
- 契約：呼叫端未同步更新、回傳型別改變、例外種類改變、預設值改變。
- 資源：檔案未關、連線洩漏、無界快取/遞迴。
- 遺漏面：diff 改了 A 處但同型邏輯的 B 處沒改（grep 同 pattern）。

### 3. Verify before reporting（報告前逐項驗證）

每個候選 finding 必須通過其一才可報告：

- 沿程式碼追蹤該輸入的實際資料流，確認錯誤路徑真實存在（`CONFIRMED`）。
- 能執行時：以最小重現輸入實跑（交給 `verifying-changes` 手法）（`CONFIRMED`）。
- 資料流一致但無法完全排除防護存在 → 降級標記 `PLAUSIBLE`，說明未驗證的環節。

驗證中被推翻的候選**直接丟棄**，不進報告。

### 4. Report findings-first（依嚴重度排序輸出）

```markdown
## Findings（依嚴重度排序）
1. [Critical|High|Medium|Low][CONFIRMED|PLAUSIBLE] path/to/file.py:42
   - 缺陷：<一句話>
   - 失敗場景：<具體輸入/狀態 → 錯誤結果>
   - 建議：<最小修法>

## 審查範圍聲明
- 已檢查：<檔案/面向清單>；未涵蓋：<明列>
```

- 正確性缺陷與風格建議**分區呈現**，不得混排稀釋信號。
- 無 finding 時輸出「已檢查清單 + 無發現」，不硬湊。

## Non-Negotiables

- 禁止「這裡可能有問題」式的未驗證泛論——要嘛給出失敗場景，要嘛不報。
- 嚴重度依「觸發機率 × 影響」評，不依發現順序。
- 審查結論不因作者身分軟化（anti-sycophancy，同 global-rules §3）。

## 與相鄰 skill 的分工

- `handling-review`：處理**收到的**審查意見；本 skill 是**發出**審查。
- `auditing-code`：全庫靜態/安全基線掃描；本 skill 聚焦單一 diff 的正確性。
- `simplifying-code`：品質清理（不找 bug）；順序上先本 skill 後 simplify。
- 金融領域對應：`reviewing-financial-analysis`（同一 findings-first 紀律的分析版）。

## Evolution Log

- 2026-07-04 v1.0.0 — Initial capture — 觸發事件: 差集分析發現庫內 handling-review 只覆蓋
  「回應審查」單向，缺「主動審 diff + 驗證後才報告」紀律；自 Claude Code 內建 code-review
  方法論（verified findings、failure scenario、嚴重度排序、空結果合法）蒸餾為 agent-agnostic 版。
