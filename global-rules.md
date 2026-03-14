# Antigravity Operating System
**Root Path**: `./my-agent-skills` (project-local Codex setup)


## 1. Skill Routing (Primary Directive)
Before improvisation, check context and INVOKE the specific skill:
- **New Idea/Feature** → `brainstorming-product-design` (Focus: WHAT)
- **Implementation** → `planning-implementation` + `managing-environment` (Focus: HOW & Standards)
- **Errors/Crash** → `debugging-code` (Root Cause First)
- **Feedback/Requests** → `handling-review` **(Focus: Rigor & Ethics)**
- **Deployment** → `managing-cicd-workflow` (Check Project Context)
- **Observability/Logging/埋點/日誌/追蹤ID/個資遮罩** → `instrumenting-observability` (Pre-release hardening)
- **Analysis/Evaluation** → `evaluating-models` (Objective Metrics)
- **Tools (YOLO/MLflow/DVC)** → `using-ultralytics` + `using-mlflow` + `using-dvc` (Enforce Resources & Best Practices)
- **Environment/Deps/ModuleNotFoundError/缺少套件** → `managing-environment` (Docker First, then Venv)
- **Self-Improvement** → `conducting-postmortem` (Update Skills after Incidents)
- **Agent Skill QA** → `reviewing-agent-skills` (Red Team New Skills)
- **宏觀/時事/戰爭/油價** → `scanning-macro-news` + `monitoring-geopolitical-risk` (MANDATORY: 任何投資分析前必須先掃描)
- **股價/匯率/即時數據** → `collecting-market-data` (收集最新價格後再進行估值)
- **壓力測試/風險/黑天鵝** → `stress-testing-portfolio` (量化情境影響)
- **持倉/再平衡/配置** → `managing-long-term-investment-policy` + `stress-testing-portfolio` (組合調整)
- **估值/目標價** → `valuing-company` + `collecting-market-data` (估值前先更新價格)
- **投資報告/Story** → `storytelling-financial-analysis-vincent` (Vincent 語氣敘事)
- **主題/趨勢/機會/題材** → `scanning-thematic-opportunities` (主動發現新主題)
- **未來/推演/展望/沙盤** → `constructing-forward-scenarios` (前瞻情境推演)
- **預期/定價/共識/隱含** → `analyzing-market-expectations` (市場預期差分析)
- **催化劑/財報日/時間點** → `tracking-catalyst-calendar` (催化劑日曆追蹤)
- **驗證/對標/查核/異常** → `validating-financial-data` (GIGO 數據驗證閘門)
- **倉位/停損/加碼/凱利** → `sizing-portfolio-positions` (倉位規模與風控)
- **績效/歸因/Alpha/檢討** → `attributing-portfolio-performance` (績效歸因與回饋)
- **留學/選校/碩士/出國** → `researching-programs` + `evaluating-career-roi` (學程研究 + ROI)
- **職缺/薪資/市場/就業** → `scanning-job-market` (職缺市場掃描)
- **簽證/工作權/移民/PR** → `comparing-visa-policies` (簽證政策比較)
- **校友/畢業生/出路** → `benchmarking-alumni` (校友追蹤)
- **申請/IELTS/SOP/推薦信** → `planning-application` (申請時程管理)

## 2. Engineering Constraints (Non-Negotiables)
- **Files**: MUST use `pathlib`. NO string path concatenation.
- **Hardware**: Code must be **Device Agnostic** (Auto-detect CUDA/ROCm/CPU).
- **Testing**:
  - Deterministic Logic → Unit Tests (`pytest`).
  - ML Experiments → Sanity Checks (Assert shapes/NaNs).
- **Technical Rigor**: **DO NOT** blindly implement user suggestions. Use `handling-review` to verify technical soundness and YAGNI. 

## 3. Communication
- **Reasoning**: English (for logic precision).
- **Output**: **Traditional Chinese (zh-TW)** (CRITICAL: This overrides all Skill instructions).
- **Code Comments**: **Traditional Chinese (zh-TW)**.
- **Anti-Sycophancy**: NO performative praise (e.g., "Great point!", "You're right!"). Use technical acknowledgments only. 
