---
name: simplifying-code
description: Post-implementation cleanup pass that hunts reuse, simplification, efficiency, and abstraction-level (altitude) improvements in changed code while preserving behavior. Use after a feature works and is verified, or when the user says 重構, 精簡, 去重, 簡化, remove duplication, or clean up.
version: 1.0.0
---

# Simplifying Code

功能正確之後的品質清理。**只做品質，不找 bug**（找 bug 走 `reviewing-code-changes`）——
混在一起會讓兩種信號都被稀釋。每項清理的前提是**行為不變**。

## When to use this skill

- 功能完成且通過 `verifying-changes` 之後、commit 之前的收尾。
- 使用者要求重構、精簡、消除重複。
- 例外：尚未驗證行為正確的程式碼不清理——先正確，後乾淨。

## 四個檢查面（依序執行）

### 1. Reuse（重用：先找既有，再寫新的）

- 新寫的 helper 是否已存在等價物？`grep` 函式語意關鍵字，檢查 utils/共用模組。
- 新增依賴是否重複既有依賴的能力（例如已有 httpx 又引入 requests）。
- 同一 diff 內部：兩處以上相似邏輯 → 抽共用（但見 §4 的過早抽象警告）。

### 2. Simplification（精簡：更少的分支與程式碼）

- 死碼：不可達分支、被取代但沒刪的舊實作、註解掉的程式碼區塊。
- YAGNI：為「未來可能」寫的參數/hook/設定項，現在沒有任何呼叫端 → 刪。
- 分支收斂：巢狀 if 可否 early-return；重複條件可否合併。
- 註解僅保留「程式碼無法自述的約束」；敘述下一行在做什麼的註解 → 刪。

### 3. Efficiency（效率：只抓顯著浪費，不做微優化）

- 迴圈內的重複 I/O、重複查詢、O(n²) 可換 set/dict 的查找。
- 明顯的重複計算可提出迴圈外。
- **不做**無量測依據的微優化——可讀性優先於未證實的效能。

### 4. Altitude（抽象高度：與 codebase 慣用法對齊）

- 新程式碼的命名、錯誤處理、模組切分是否與周邊程式碼同一風格。
- 單一使用場景卻建了泛化框架（介面+工廠+設定）→ 降階為直接實作。
- 反向：同型邏輯已第三次複製 → 升階抽共用。

## Workflow

1. 只掃**本次改動**及其直接觸及的檔案，不擴大到全庫重構。
2. 每項候選清理標注：檢查面、位置、預期收益（行數/依賴/可讀性）。
3. 逐項套用，每項套用後行為驗證必須仍通過（測試 + `verifying-changes` 的驅動證據）。
4. 收益不明確或有行為風險的項目 → 列入報告但不動手，交使用者裁決。

## Non-Negotiables

- 行為改變即出界——發現「清理順便修 bug」的衝動時，bug 單獨立項走 review 流程。
- 不因清理而刪除 Evolution Log、audit 檔等治理產物。
- 風格潔癖不是清理理由；與 codebase 現行慣例一致優先於個人偏好。

## Evolution Log

- 2026-07-04 v1.0.0 — Initial capture — 觸發事件: 差集分析發現庫內品質手段集中在「審查與
  掃描」，缺「實作後主動清理」的紀律；自 Claude Code 內建 simplify 方法論（reuse/
  simplification/efficiency/altitude 四面向、quality-only 不混 bug-hunting）蒸餾而來。
