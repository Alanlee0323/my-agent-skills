# Antigravity Global Skill Library

**Location**: `C:\Users\AlanY.Lee\.gemini\antigravity\skills`
**Maintainer**: Agent Antigravity
**Last Audit**: 2026-01-20

This library contains **Context-Aware Agent Skills** designed to guide the AI through the entire software engineering lifecycle, from ideation to deployment.

---

## 🛠️ Skill Inventory

### 1. Ideation & Architecture
- **[brainstorming](brainstorming/SKILL.md)**
    - **Role**: Socratic Product Manager
    - **Trigger**: "Brainstorm app idea", "Design a feature"
    - **Output**: `product_design.md`
    - **Key Feature**: Focuses on *What* to build, not *How*.

### 2. Planning & Engineering
- **[planning](planning/SKILL.md)**
    - **Role**: Software Architect
    - **Trigger**: "Plan implementation", "How to build this"
    - **Output**: `implementation_plan.md`
    - **Key Feature**:
        - **Context-Aware Standards**: Automatically enforces `pathlib`, `logging`, and Type Hints.
        - **Smart Testing**: Distinguishes between **Unit Tests** (Logic) and **Sanity Checks** (ML Experiments).

### 3. Execution & Debugging
- **[debugging-code](debugging-code/SKILL.md)** *(formerly `troubleshooting`)*
    - **Role**: Senior Debugger
    - **Trigger**: "Fix this error", "Runtime exception"
    - **Key Feature**: **English Reasoning / Chinese Output**. Enforces Root Cause Analysis before coding.

### 4. Domain-Specific Tools (Active Enforcement)
These skills do not just provide docs; they **enforce best practices** proactively.

- **[using-ultralytics](using-ultralytics/SKILL.md)**
    - **Domain**: YOLOv8/v9/v10/v11
    - **Guardrail**: Checks for **Data Leakage** (Train/Val split) before training.
- **[using-mlflow](using-mlflow/SKILL.md)**
    - **Domain**: Experiment Tracking
    - **Guardrail**: Enforces standardized experiment naming conventions.
- **[using-dvc](using-dvc/SKILL.md)**
    - **Domain**: Data Version Control
    - **Guardrail**: Ensures `dvc commit` and `git commit` are synchronized.

### 5. Deployment (CI/CD)
- **[cicd-skills](cicd-skills/SKILL.md)**
    - **Role**: DevOps Engineer
    - **Trigger**: "Deploy to production", "Pipeline failed"
    - **Key Feature**: **Dynamic Context Switching**.
        - If Project == `LB-ASM-X2648`: Uses specific lab IPs.
        - If Other: Asks user for `{{TARGET_IP}}`.

### 6. Meta-Skills
- **[gemini-skill-creator](gemini-skill-creator/SKILL.md)**
    - **Role**: Skill Factory
    - **Usage**: Used to generate *new* skills following this very standard.

---

## 🚀 Workflow Integration

Typical lifecycle usage:

1.  `Brainstorming` -> Define the app.
2.  `Planning` -> Create the checklist and select standards.
3.  (Coding...)
4.  `Debugging-Code` -> If errors occur.
5.  `Using-*` -> When specific libraries are invoked.
6.  `CI/CD` -> When deploying to testing/production servers.