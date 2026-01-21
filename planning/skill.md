---
name: planning-implementation
description: Converts approved designs or detailed requirements into actionable, atomic implementation steps. Use when the user approves a design or asks "how to implement".
---

# Planning & Implementation Breakdown

## When to use this skill
- User has approved a `product_design.md`.
- User provides a detailed requirement and asks for a plan.
- User asks "how to implement" a specific complex feature.

## Workflow

1.  **Read Context & Standards**
    - Read `product_design.md` or the user's specific requirements.
    - **MANDATORY**: Check `managing-environment` skill for Project Setup & Dependency standards (Docker/pyproject.toml).

2.  **Atomic Task Decomposition**
    - Break the project down into a linear series of steps.
    - **Atomic Rule**: Each step must be small enough to be completed by an AI agent in 2-5 minutes (e.g., "Create button component" is good; "Build entire frontend" is bad).
    - **No Code**: This phase is for *planning* the code, not writing it.

3.  **Generate Documentation**
    - Create or update `implementation_plan.md`.
    - Format:
        ```markdown
        # Implementation Plan - [Project Name]
        
        - [ ] Step 1: Environment Setup
            - Initialize project (e.g., `npm create vite@latest`).
            - Install dependencies.
        - [ ] Step 2: Foundation
            - Create basic directory structure.
            - Setup global styles/theme.
        - [ ] Step 3: [Feature A] - Component X
            - Create file...
            - Implement logic...
        ...
        ```

4.  **Best Practices**
    - **TDD**: Include steps for creating tests *before* implementation where appropriate.
    - **Verification**: Include a verification step after major implementation blocks (e.g., "Run tests", "Check browser").

## Instructions

- **Granularity**: If a step feels like it has "sub-steps", break it apart.
- **Clarity**: Use exact file paths and command examples in the plan where possible.
- **Output**: The primary deliverable is the `implementation_plan.md`.

## Resources
- [None]
