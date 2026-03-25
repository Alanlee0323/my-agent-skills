---
name: technical-doc-writer
description: Use this skill when creating, rewriting, structuring, or reviewing technical documentation in Chinese. Suitable for 技術文件, 文件撰寫, 教學文件, 操作指南, 架構說明, API 文件, README 重構, and troubleshooting docs. It classifies docs with Diataxis, defines audience and single goal, and generates a skimmable Markdown structure.
---

# Technical Doc Writer

當使用者要求撰寫、改寫、整理、審閱、拆分、補強技術文件時，使用這個 skill。

此 skill 的預設輸出語言是繁體中文。除非使用者明確要求其他語言，所有文件草稿、標題、摘要、表格說明、圖表註解與 review 意見都必須使用中文撰寫。程式碼、CLI 指令、API 欄位名稱可保留英文，但周邊說明仍應使用中文。

## Goals

此 skill 幫助你：

- 先判斷文件類型，再開始寫作
- 先定義受眾與單一目標，再產出內容
- 產出可掃讀、可維護、可拆分的 Markdown 文件
- 避免把任務型文件和概念型文件混寫
- 讓技術文件維持中文一致性與可讀性

## Skill Composition

這個 skill 可與其他 skill 串接使用，建議順序如下：

1. 文件範圍大、需要拆批次或排程時
   - 先用 `planning-implementation`
   - 產出文件撰寫計畫、批次順序、原子化交付項目
2. 文件主題涉及安裝、依賴、Docker、pyproject、環境設定時
   - 讀取 `managing-environment`
   - 以該 skill 的環境標準為準，再用本 skill 轉成中文文件
3. 文件需要審查、修改意見、嚴格驗證時
   - 讀取 `handling-review`
   - 先驗證修改建議是否合理，再回到本 skill 修正文稿

若任務是「大規模技術文件規劃」，優先順序為：

1. `planning-implementation`
2. `technical-doc-writer`
3. `handling-review`

## When to use this skill

適用情境：

- README 重構或補寫
- 新功能教學文件
- 安裝與設定指南
- 遷移指南
- 架構說明文件
- API / CLI / Config 參考文件
- Troubleshooting 文件
- 內部工程文件與 onboarding 文件
- 技術文件撰寫
- 技術文件改寫
- 文件結構重整
- 文件審查與補強
- 教學文件
- 操作指南
- 解釋型文件
- 參考型文件

不適用情境：

- 純行銷文案
- 只有公告性質的 release notes
- 主要是法務、政策、合約文件的任務

## Required Workflow

1. 先建立 `Document Brief`
2. 判斷文件屬於哪一種 Diataxis 類型
3. 明確寫出目標讀者與單一目標
4. 如果任務跨多份文件或多模組，先用 `planning-implementation` 拆成批次
5. 先產出大綱，再寫完整內容
6. 依文件類型填入正確層級的內容
7. 若內容涉及環境與依賴，參照 `managing-environment`
8. 補上必要的範例、圖表、表格、連結與 gotchas
9. 若使用者是在 review 或修改既有文件，參照 `handling-review`
10. 交付前做一次自我審查

## Document Brief

開始寫作前，先用以下格式整理需求；若使用者沒有提供完整資訊，請先根據上下文合理推斷，並把推斷寫明。

```md
## 文件摘要
- 文件類型：
- 目標讀者：
- 文件目標：
- 非目標：
- 前置條件：
- 預期輸出格式：
- 是否需要範例程式碼／指令／圖表：
```

## Diataxis Decision Rules

只選一個主要類型作為主軸：

- `Tutorial`
  - 適合新手逐步上手
  - 重點是讓讀者跟著做出可見成果
- `How-to`
  - 適合已知目標的任務導向操作
  - 重點是快速完成工作，不展開大量原理
- `Explanation`
  - 適合說明概念、架構、設計取捨與原因
  - 重點是回答為什麼
- `Reference`
  - 適合提供查詢型資訊
  - 重點是結構化、精準、可快速查找

如果使用者要「完成任務」，優先寫 `How-to`，不要把大量背景知識塞進步驟中。若背景知識必要，請獨立成 `Explanation`，並在任務文件中連結過去。

## Writing Rules

- 預設讀者會掃讀，不會從頭到尾細讀
- 段落第一句就放最重要的資訊
- 一份文件只服務一個主要目標
- 不預設讀者已具備背景知識、權限、環境或上下文
- 能用表格、步驟、範例、圖表說清楚時，不要用長段落硬寫
- 文件若過長，拆檔優先於堆疊更多次級標題
- 使用簡單直白的中文，避免中英夾雜造成理解負擔
- 專有名詞可保留英文，但第一次出現時應搭配中文說明

## Output Defaults

除非使用者另有要求，預設輸出應包含：

1. `文件摘要`
2. `Diataxis 分類`
3. `Markdown 大綱`
4. `完整草稿`
5. `自我審查清單`

若任務是大規模文件工程，額外包含：

6. `文件批次計畫`
7. `每份文件的 Diataxis 分類與目標讀者`
8. `依賴其他 skill 的註記`

## Review Rules

交付前必查：

- 是否混入不屬於該文件類型的內容
- 是否真的對應單一目標
- 是否能讓讀者快速掃讀並找到答案
- 是否補齊前置條件與限制
- 是否提供可執行的範例或可視化輔助
- 是否全篇維持中文說明一致性

## References

按需讀取下列檔案：

- `references/diataxis.md`
  - 需要判斷文件類型、避免混類時讀取
- `references/document-templates.md`
  - 需要快速產出骨架或完整模板時讀取
- `references/writing-principles.md`
  - 需要風格準則、內容取捨原則時讀取
- `references/review-checklist.md`
  - 需要交付前審查、review 文件品質時讀取
- `references/example-prompts.md`
  - 需要快速產生需求描述或驗證 scheduler 路由時讀取
