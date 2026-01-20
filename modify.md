# Role: Antigravity Skill Architect
Please perform a "Refactoring & Optimization" task on my global skill library located at:
`C:\Users\AlanY.Lee\.gemini\antigravity\skills`

Based on the recent audit, I need you to update the following `SKILL.md` files to improve proactivity, security, and standardization.

---

## Task 1: Rename & Standardize Language (Troubleshooting)
**Target:** `troubleshooting-and-error-handling`
1.  **Rename**: Rename the folder and the ID to `debugging-code` (shorter, action-oriented).
2.  **Language Strategy**: Rewrite the internal *Instructions* and *System Prompts* in **English** to ensure logical precision.
3.  **Output Requirement**: Explicitly add a rule: "Reasoning process must be in English, but the final explanation and communication with the user must be in **Traditional Chinese (繁體中文)**."

## Task 2: Active "Best Practice" Enforcement (Tools)
**Target:** `using-dvc`, `using-mlflow`, `using-ultralytics`
1.  **Shift Tone**: Change the description from "Provides documentation..." to "Actively assists and enforces best practices for...".
2.  **Add Rules**:
    - For **Ultralytics**: Add "Check for data leakage and ensure proper train/val split before training."
    - For **DVC**: Add "Remind user to `dvc commit` and `git commit` when data changes are detected."
    - For **MLflow**: Add "Ensure experiment names are standardized before logging runs."

## Task 3: Security & Generalization (CI/CD)
**Target:** `cicd-skills`
1.  **Remove Hardcoding**: Identify the hardcoded IP `192.168.137.51`. Replace it with a variable placeholder (e.g., `{{TARGET_IP}}`) or a logic step that checks environment variables first.
2.  **Context Logic**: Update the trigger logic to: "If project is LB-ASM-X2648, use default IP; otherwise, ask user for the target deployment IP."

## Task 4: Inject "Context-Aware" Engineering Standards
**Target:** `planning-implementation`

1.  **Add Section**: Insert a "Dynamic Engineering Standards" section.
2.  **Define Rules**:

    **A. Universal Standards (Apply to ALL projects):**
    -   **Path Handling**: ALWAYS use `pathlib` for file paths. (Reason: Cross-platform compatibility for Win/Linux/Docker).
    -   **Code Quality**: Use Python 3.10+ syntax and enforce Type Hinting (`def func(x: int) -> str:`) for all functions.
    -   **Logging**: Use the standard `logging` module instead of `print()` for status updates (to ensure logs are capture-ready).

    **B. Conditional Standards (Apply ONLY when relevant):**
    -   **IF "Model Training" or "Deep Learning" is detected:**
        -   **Device Logic**: Code MUST be device-agnostic. Use `torch.device` checks. Do NOT hardcode `cuda` (to support AMD/NVIDIA hybrid envs).
        -   **Observability**: IF `mlflow` is installed or requested, enforce parameter logging (`mlflow.log_params`) and metric tracking.
    -   **IF "Data Processing" or "Large Files" are involved:**
        -   **Versioning**: Assume data might be versioned by DVC. Do not hardcode absolute paths; use relative paths or config files.
    -   **IF "Docker" or "Container" context is active:**
        -   Ensure code does not rely on GUI popups (e.g., `cv2.imshow`) and saves outputs to disk instead.

3.  **Instruction for Agent**:
    -   "Before generating code, briefly analyze the tech stack of the current request. Apply the 'Conditional Standards' only if the relevant technologies are being used."

## Task 5: Integrate "Context-Aware Testing" Strategy
**Target:** `planning-implementation`

1.  **Add Section**: Insert a "Testing & Validation Strategy" section.
2.  **Define Rules**:
    Instead of strict TDD for everything, apply the following logic:

    **A. Deterministic Logic (Must Test):**
    -   **Scope**: Data preprocessing functions, metric calculations, custom loss functions, and file parsing utilities.
    -   **Action**: Generate a small `pytest` file alongside the implementation.
    -   **Standard**: Use `pytest`. Ensure tests mock external dependencies (e.g., do not actually connect to S3 or MLflow during unit tests).

    **B. Model Training & Experiments (Sanity Checks):**
    -   **Scope**: Training loops, model architecture definitions (`nn.Module`).
    -   **Action**: Do NOT write full unit tests. Instead, insert **Runtime Assertions** (Sanity Checks) within the code.
    -   **Example**: `assert output.shape == target.shape, "Shape mismatch in forward pass"` or checking for `NaN` values.

    **C. Hardware Simulation:**
    -   If generating tests for GPU-related code, always safeguard with:
        `@pytest.mark.skipif(not torch.cuda.is_available(), reason="Skipping GPU test on CPU machine")`

3.  **Instruction for Agent**:
    -   "When planning, explicitly state whether the current task requires a 'Unit Test' (for logic) or just 'Sanity Checks' (for experiments). Do not default to TDD for exploratory data science tasks."

---

## Execution Steps:
1.  **Read** the current content of these specific skills.
2.  **Apply** the changes described above to the files.
3.  **Report** a summary of changes made (Diff).

Please proceed with the update.