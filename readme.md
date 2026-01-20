# Antigravity 全域技能庫 (Global Skill Library)

**位置**: `C:\Users\AlanY.Lee\.gemini\antigravity\skills`
**維護者**: Agent Antigravity
**上次審計**: 2026-01-20

此技能庫包含 **情境感知 (Context-Aware) Agent Skills**，旨在引導 AI 完成從構思到部署的完整軟體工程生命週期。

---

## 🛠️ 技能清單 (Skill Inventory)

### 1. 構思與架構 (Ideation & Architecture)
- **[brainstorming](brainstorming/SKILL.md)**
    - **角色**: 蘇格拉底式產品經理
    - **觸發**: "發想 App 點子", "設計一個功能"
    - **產出**: `product_design.md`
    - **核心特色**: 專注於 **做什麼 (What)**，而非 **怎麼做 (How)**。

### 2. 規劃與工程 (Planning & Engineering)
- **[planning](planning/SKILL.md)**
    - **角色**: 軟體架構師
    - **觸發**: "規劃實作", "如何建立這個"
    - **產出**: `implementation_plan.md`
    - **核心特色**:
        - **情境感知標準**: 自動強制使用 `pathlib`, `logging` 和 Type Hints。
        - **智慧測試策略**: 區分 **單元測試** (邏輯) 與 **健全性檢查 (Sanity Checks)** (ML 實驗)。

### 3. 執行與除錯 (Execution & Debugging)
- **[debugging-code](debugging-code/SKILL.md)** *(原 `troubleshooting`)*
    - **角色**: 資深除錯專家
    - **觸發**: "修復這個錯誤", "Runtime exception"
    - **核心特色**: **英文推理 / 中文輸出**。在寫 Code 之前強制執行根因分析。

### 4. 領域特定工具 (主動執行)
這些技能不僅提供文件，還會 **主動強制執行最佳實踐**。

- **[using-ultralytics](using-ultralytics/SKILL.md)**
    - **領域**: YOLOv8/v9/v10/v11
    - **防護機制**: 在訓練前檢查 **資料洩漏 (Data Leakage)** (Train/Val 分割)。
- **[using-mlflow](using-mlflow/SKILL.md)**
    - **領域**: 實驗追蹤 (Experiment Tracking)
    - **防護機制**: 強制執行標準化的實驗命名規範。
- **[using-dvc](using-dvc/SKILL.md)**
    - **領域**: 資料版本控制 (Data Version Control)
    - **防護機制**: 確保 `dvc commit` 與 `git commit` 保持同步。

### 5. 部署 (CI/CD)
- **[cicd-skills](cicd-skills/SKILL.md)**
    - **角色**: DevOps 工程師
    - **觸發**: "部署到正式環境", "Pipeline 失敗"
    - **核心特色**: **動態情境切換**。
        - 若專案為 `LB-ASM-X2648`: 使用特定實驗室 IP。
        - 若為其他專案: 詢問使用者 `{{TARGET_IP}}`。

### 6. 元技能 (Meta-Skills)
- **[gemini-skill-creator](gemini-skill-creator/SKILL.md)**
    - **角色**: 技能工廠
    - **用途**: 用於生成符合此標準的 *新* 技能。

---

## 🚀 工作流程整合 (Workflow Integration)

典型生命週期用法:

1.  `Brainstorming` -> 定義 App 內容。
2.  `Planning` -> 建立檢查清單並選擇工程標準。
3.  (Coding... 寫程式)
4.  `Debugging-Code` -> 如果發生錯誤。
5.  `Using-*` -> 當調用特定函式庫時。
6.  `CI/CD` -> 當部署到測試/正式伺服器時。