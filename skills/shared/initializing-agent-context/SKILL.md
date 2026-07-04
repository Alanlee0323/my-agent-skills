---
name: initializing-agent-context
description: Creates and maintains agent onboarding files (AGENTS.md, CLAUDE.md, GEMINI.md, copilot-instructions) for a repository — what belongs in them, what must stay out, and how to verify every documented command actually works. Use when the user says init, 初始化專案, onboarding, 建立 AGENTS.md, or when starting agent work in an undocumented repo.
version: 1.0.0
---

# Initializing Agent Context

Agent 上下文檔是「新 agent 進場第一分鐘讀的東西」。它的價值密度決定所有後續 session 的
品質。原則：**只寫程式碼推不出來的事**，且**每條指令寫入前都要實際執行驗證**。

## When to use this skill

- 為新 repo 建立 AGENTS.md / CLAUDE.md / GEMINI.md / .github/copilot-instructions.md。
- 既有上下文檔過期、臃腫、或包含錯誤指令時的重寫。
- `conducting-postmortem` 產出「這個坑要讓未來 agent 知道」的寫回目標。

## What belongs（高價值內容——按序）

1. **可執行指令**（build / test / lint / run / deploy），每條都經實跑驗證，附工作目錄。
2. **架構一句話地圖**：模組 → 職責 → 關鍵入口檔（不是檔案樹複印）。
3. **反直覺的慣例**：與生態系預設不同之處（「本 repo 用 pathlib 禁字串路徑」「測試要先起
   docker compose」）。
4. **已知陷阱**：postmortem 累積的坑（「改 X 必須同步改 Y」）。
5. **邊界宣告**：agent 不得動的區域（產線設定、生成物、vendored code）。

## What must stay OUT（低價值/負價值內容）

- 程式碼能自述的事實（函式清單、目錄樹全文、依賴清單複印）——會過期且浪費上下文。
- 通用最佳實踐說教（「寫乾淨的程式碼」）——沒有資訊量。
- 大段貼上的範本程式碼——改用指向 repo 內範例檔的路徑。
- 波動性高的細節（版本號、issue 連結）——放連結不放內容。
- 目標長度：**100 行內**；超過 → 拆到 `docs/` 並留單行指標（漸進揭露，同 skill 庫原則）。

## Workflow

1. **偵察**：讀 README、CI 設定、package 管理檔，列出候選指令集。
2. **驗證**：逐條實跑候選指令（`verifying-changes` 紀律）——跑不通的指令寫進去是負資產。
3. **訪談差異**：詢問使用者「這個 repo 有什麼新人常踩的坑？」——這是檔案裡最值錢的內容。
4. **撰寫**：依上方清單排序；每節 ≤10 行。
5. **多 agent 佈署**：內容只維護一份 canonical（建議 `AGENTS.md`），其他檔
   （CLAUDE.md/GEMINI.md）以單行引用指向，不複製內容（同名漂移防治，
   同 `maintaining-skill-library` 的唯一事實來源原則）。

## Maintenance contract（寫完不是結束）

- 指令變更（build 系統遷移、腳本改名）時同步更新——驗證方式：CI 加一步驟跑檔內指令。
- postmortem 的「PREVENTATIVE ACTION」若屬專案層知識 → 寫回本檔而非 skill 庫。
- 每次重大重構後重驗全部指令；過期的上下文檔比沒有更危險（agent 會自信地執行錯誤指令）。

## Evolution Log

- 2026-07-04 v1.0.0 — Initial capture — 觸發事件: 差集分析發現 readme 架構圖引用 AGENTS.md
  但庫內沒有任何「如何寫好 agent 上下文檔」的方法論；自 Claude Code 內建 init 方法論蒸餾，
  並依本庫「唯一事實來源」原則加入多 agent 單一 canonical 檔規則。
