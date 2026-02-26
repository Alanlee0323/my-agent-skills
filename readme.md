# Antigravity Skills Pack

本目錄是跨專案共用的**全域技能庫**，提供「任務路由 + 實作守門 + 領域最佳實踐」三層能力，協助 AI 代理在多步驟工程任務中維持一致性與可追蹤性。

## 1) 雙層架構

```text
your-project/
├─ skills/                  ← 專案層（Project-Local）：只放該專案的差異覆寫
│  └─ cicd-skills/
│     └─ SKILL.md           ← 覆寫 global 同名 skill（優先載入）
├─ my-agent-skills/         ← 全域層（Global）：本目錄，跨專案通用
│  ├─ cicd-skills/
│  │  └─ SKILL.md           ← 通用 trunk-based CI/CD 流程
│  ├─ planning/
│  ├─ ...
│  └─ global-rules.md
├─ AGENTS.md
└─ skill_scheduler.py
```

### 優先順序規則
- `skill_scheduler.py` 先掃 `./skills/`，再掃 `./my-agent-skills/`。
- **同名 identifier 去重**：第一個被掃到的贏（= project-local 覆寫 global）。
- 若 `./skills/` 不存在或為空，所有技能自動 fallback 到 global 層。

### 何時使用哪一層？

| 內容類型 | 放置位置 | 範例 |
|---|---|---|
| 跨專案通用流程 | `./my-agent-skills/` | trunk-based CI/CD、planning、code review |
| 專案特定參數/覆寫 | `./skills/` | IP whitelist、job 名稱、硬體對照表 |
| 專案獨有且不通用的 skill | `./skills/` | 專案私有部署腳本、內部 API 整合 |

### 撰寫 Project Override 的原則
1. **只寫差異**：繼承 global 的流程，只覆寫專案特定細節（IP、環境、job 名稱）。
2. **保持同名**：`name` frontmatter 必須與 global skill 的 identifier 一致，scheduler 才能正確去重。
3. **交叉引用**：在 override 中註明「通用流程請參考 global skill」，避免內容重複維護。

## 2) Global Skill Inventory（含潛在風險）

| Skill | 主要職責 | 潛在風險 | 風險控制建議 |
|---|---|---|---|
| [brainstorming-product-design](brainstorming/skill.md) | 需求探索與產品構想釐清 | 需求尚未收斂就進入實作，造成返工 | 先輸出可驗證需求，再交由 planning 拆解 |
| [planning-implementation](planning/skill.md) | 產出可執行的實作步驟 | 過度規劃或步驟粒度不一致，影響執行效率 | 強制原子化步驟，並在每階段加入驗證點 |
| [managing-environment](managing-environment/SKILL.md) | 依賴安裝、環境初始化、容器化決策 | Docker-first 在非容器場景可能增加啟動成本 | 先檢查專案現況，保留 venv/conda 合理落地分支 |
| [handling-review](handling-review/SKILL.md) | 審查意見技術化評估與執行 | 過度保守造成變更吞吐下降 | 區分阻斷性問題與一般建議，採分層處理 |
| [auditing-code](auditing-code/SKILL.md) | 靜態分析、資安檢查、反模式偵測 | 誤報造成噪音，影響決策速度 | 將檢查結果分級（Critical/High/Info）並附可重現證據 |
| [managing-cicd-workflow](cicd-skills/SKILL.md) | 通用 trunk-based CI/CD 流程 | 過度通用導致專案細節遺漏 | 搭配 `./skills/` project override 補充專案參數 |
| [evaluating-models](evaluating-models/SKILL.md) | 模型評估、指標比較、結果解讀 | 指標導向偏誤，忽略資料品質與成本約束 | 評估結論必須同時附資料假設與使用情境 |
| [using-ultralytics](using-ultralytics/SKILL.md) | YOLO 系列訓練/推論/部署指引 | 版本更新快，文件易過期 | 引用前標註版本，必要時回查官方文件 |
| [using-mlflow](using-mlflow/SKILL.md) | MLflow Tracking/Registry 實作指引 | 實驗命名與追蹤規範不一致，導致可追溯性下降 | 先統一命名規範與 artifact policy 再執行 |
| [using-dvc](using-dvc/SKILL.md) | 資料與模型版本治理 | `dvc commit` / `git commit` 不同步造成狀態漂移 | 在流程中加入同步檢查與 pre-commit 驗證 |
| [creating-agent-skills](gemini-skill-creator/skill.md) | 生成新技能框架與模板 | 快速生成可能複製舊規範缺陷 | 產出後必須經 reviewer skill 審核 |
| [reviewing-agent-skills](gemini-skill-reviewer/SKILL.md) | 技能品質審計與紅隊檢查 | 審計規則若過嚴會抑制迭代速度 | 以風險優先級定義必過/可延後項目 |
| [conducting-postmortem](conducting-postmortem/SKILL.md) | 事故回饋與技能持續改進 | 事故樣本偏差造成錯誤優化方向 | 要求跨事件比對，避免單一案例過擬合 |

## 3) 路由與治理建議

1. **先跑 scheduler，再執行技能**：避免憑直覺選錯技能。
2. **預設採「Plan → Domain → Review」順序**：降低漏檢與回滾成本。
3. **對高風險任務（部署、資料、相依）保留人工確認點**。
4. 若出現 guardrail 警告，優先處理「候選篩選噪音」而非盲目提高 read limit。
5. **專案特化需求一律走 `./skills/` override**，不要修改本目錄內的 global skill。

## 4) 維運建議（給技能維護者）

- 每次新增/修改 skill，至少更新：
  - 對應 frontmatter（`name`, `description`）
  - 觸發條件（When to use this skill）
  - 風險與限制（至少 1 條）
- 建議定期檢查：
  - 路由名稱是否與檔名/identifier 一致
  - 是否存在專案綁定假設（IP、平台、路徑）未被明確標記
  - 全域規則與各 skill 規則是否衝突
- **Project override 維護**：
  - override 的 `name` 必須與 global skill 完全一致
  - override 不應複製 global 的流程內容，只寫差異
  - 當 global skill 變更時，檢查現有 override 是否仍相容
