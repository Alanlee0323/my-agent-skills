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
