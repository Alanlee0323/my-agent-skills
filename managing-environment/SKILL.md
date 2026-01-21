---
name: managing-environment
description: Infrastructure Architect acting as the guardian of reproducibility. Manages package installations, environment setup, and containerization decisions with a "Docker First" mentality.
---

# Managing Environment & Dependencies

## When to use this skill
- When the user asks to "install packages", "setup project", or "initialize environment".
- When encountering `ModuleNotFoundError` or missing dependencies.
- When creating new projects.
- Triggers: "初始化環境", "缺少套件", "Module not found", "安裝依賴", "setup project"

## Logic Flow & Decision Tree

### 1. Detection Phase
**Action**: Check project root for containerization markers:
- `docker-compose.yml`
- `Dockerfile`

### 2. Branch A: Containerized Project (Exists)
**Context**: The project is already dockerized.
**Rule**: **Strictly Forbidden** to suggest `pip install` on Local Host.
**Actions**:
- Modify `Dockerfile` or `pyproject.toml`/`requirements.txt` inside the container source.
- Rebuild: Suggest `docker-compose build` or `docker build`.
- Maintain consistency: Ensure the container image remains the single source of truth.

### 3. Branch B: Local Project (Missing Docker)
**Context**: No Docker configuration found.
**Action**:
1.  **Proactive Inquiry**:
    > "偵測到此專案尚未容器化。是否建立 Docker 環境以確保一致性？ (Detected non-containerized project. Should we dockerize?)"
2.  **If User Accepts (YES)**:
    - Generate `Dockerfile` (Multi-stage best practices).
    - Generate `docker-compose.yml` (Development volume mapping).
3.  **If User Rejects (NO)**:
    - **Strict Check**: Verify if running inside `venv` or `conda`.
    - **Safeguard**: If no virtual env active, **WARN** user about global pollution before proceeding.
    - **Proceed**: Install locally.

## Dependency Standards

### 1. Premier Choice (Default): `pyproject.toml`
- **Tooling**: Standard for Poetry, Hatch, or modern Setuptools.
- **Usage**: Always prefer creating/updating `pyproject.toml` for new dependencies.
- **Why**: Metadata + Dependencies in one place.

### 2. Legacy Fallback: `requirements.txt`
- **Usage**: Only if:
    1. User explicitly requests it.
    2. Project is legacy and already strictly binds to it.
