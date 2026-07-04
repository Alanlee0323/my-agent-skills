---
name: verifying-changes
description: Verifies that a code change actually does what it claims by exercising the affected flow end-to-end and observing real behavior — not just tests or typecheck. Use before committing nontrivial changes, or when the user says 驗證, 實測, 跑起來確認, "does it actually work", or claims completion without runtime evidence.
version: 1.0.0
---

# Verifying Changes

「測試通過」不等於「功能正確」。本 skill 要求在宣告完成前，**驅動被改動的真實流程並觀察行為**，
以可重現的證據取代推定。

## When to use this skill

- 任何非平凡的程式改動，準備 commit / 交付 / 回報完成之前。
- 使用者質疑「這真的有效嗎」，或要求實測、驗證、demo。
- Postmortem 後的修復——修復必須以「重現原事故場景不再失敗」為證。
- 例外：僅改測試、文件、或無執行面的變更（無可觀察行為者無需驅動）。

## Workflow

### 1. Identify the runtime surface（找到可觀察的入口）

依專案型態選擇驅動方式：

| 型態 | 驅動方式 | 觀察對象 |
|---|---|---|
| CLI | 以真實參數執行改動路徑 | stdout/stderr、exit code、產出檔 |
| Server/API | 啟動後發真實 request（curl/httpx） | response body/status、日誌 |
| ML pipeline | 小樣本端到端跑一輪 | 輸出 shape/NaN、指標、artifact |
| Library | 寫最小驅動腳本 import 並呼叫 | 回傳值、副作用 |
| UI | 操作到受影響畫面 | 渲染結果、console error |

### 2. Define expectation BEFORE running（先寫預期，再執行）

執行前先寫下「若改動正確，我會觀察到 X」。先跑再解讀等於讓結果誘導預期。

### 3. Drive and observe（執行並記錄）

- 驅動**被改動的那條路徑**，不是隨便跑一下程式。
- 同時驗證至少一條 unhappy path（錯誤輸入、缺檔、斷網——依改動性質選）。
- 保留原始輸出（指令 + 關鍵輸出片段），這是完成報告的證據。

### 4. Compare and report（比對並如實回報）

- 預期 vs 實際逐項比對；不符 → 回到 `debugging-code`，不得「應該沒問題」帶過。
- 完成報告必附：執行的指令、觀察到的輸出、與預期的比對結論。
- **無法執行時明說**（缺環境/憑證/資料），標記 `UNVERIFIED` 並列出使用者需提供什麼——
  絕不以靜態閱讀冒充實測。

## Non-Negotiables

- 「tests pass」「typecheck 通過」不得單獨作為完成證據——它們是必要條件，非充分條件。
- 驗證輸出不可事後補寫；證據必須來自真實執行。
- 環境建立問題交給 `managing-environment`，不要在本 skill 內土法煉鋼。

## 與相鄰 skill 的分工

- `auditing-code`：靜態掃描（不執行）；本 skill 是動態驗證（必執行）。
- `reviewing-code-changes`：找「別人/自己 diff 裡的 bug」；本 skill 證明「宣稱的功能存在」。
- `debugging-code`：驗證失敗後的根因分析下游。

## Evolution Log

- 2026-07-04 v1.0.0 — Initial capture — 觸發事件: 全庫差集分析發現庫內只有靜態品質手段
  （auditing-code），缺「執行並觀察」的動態驗證紀律；自 Claude Code 內建 verify/run 方法論
  蒸餾為 agent-agnostic 版本（Fable 最終 session）。
