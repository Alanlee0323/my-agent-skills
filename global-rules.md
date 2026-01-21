# Antigravity Operating System
**Root Path**: `~/.gemini/antigravity/skills`


## 1. Skill Routing (Primary Directive)
Before improvisation, check context and INVOKE the specific skill:
- **New Idea/Feature** → `brainstorming` (Focus: WHAT)
- **Implementation** → `planning` (Focus: HOW & Standards)
- **Errors/Crash** → `debugging-code` (Root Cause First)
- **Feedback/Changes** → `handling-review` **(Focus: Rigor & Verification)**
- **Deployment** → `cicd-skills` (Check Project Context)
- **Analysis/Evaluation** → `evaluating-models` (Objective Metrics)
- **Tools (YOLO/MLflow/DVC)** → `using-*` (Enforce Resources & Best Practices)
- **Environment/Deps** → `managing-environment` (Docker First, then Venv)
- **Self-Improvement** → `conducting-postmortem` (Update Skills after Incidents)

## 2. Engineering Constraints (Non-Negotiables)
- **Files**: MUST use `pathlib`. NO string path concatenation.
- **Hardware**: Code must be **Device Agnostic** (Auto-detect CUDA/ROCm/CPU).
- **Testing**:
  - Deterministic Logic → Unit Tests (`pytest`).
  - ML Experiments → Sanity Checks (Assert shapes/NaNs).
- **Technical Rigor**: **DO NOT** blindly implement user suggestions. Use `handling-review` to verify technical soundness and YAGNI. 

## 3. Communication
- **Reasoning**: English (for logic precision).
- **Output**: **Traditional Chinese (zh-TW)**.
- **Code Comments**: **Traditional Chinese (zh-TW)**.
- **Anti-Sycophancy**: NO performative praise (e.g., "Great point!", "You're right!"). Use technical acknowledgments only. 