---
name: sdd-driven-development
description: Guides Specification-Driven Development (SDD) from ambiguous requests to clear, testable specs before coding. Use when the user asks for 規格驅動開發, spec-first workflow, 先寫規格再寫程式, or requests requirements/design/tasks documents with staged review gates for medium-to-large engineering changes.
---

# Conducting Specification-Driven Development (SDD)

## When to use this skill
- User asks for "規格驅動開發", "SDD", "spec-first", or "先寫規格再寫程式".
- User asks to define spec first, then implement.
- Requirement is unclear, cross-module, or high risk.
- Team needs phase-by-phase review points before coding.
- User asks for "requirements.md", "design.md", "tasks.md", "需求文件", "技術設計", or "任務拆解".

## Workflow

0. Scope gate (avoid over-engineering)
- If change is a tiny bugfix or low-risk patch, run SDD-Lite:
  - Write minimal requirements and acceptance criteria.
  - Write atomic tasks with verification.
  - Skip heavy design docs unless user asks.
- If change is medium/large or uncertain, run full SDD below.

1. Analyze and classify
- Confirm problem, goal, constraints, and success signal.
- Classify domain to choose templates/checklists.

2. Load only required references
- Web API: `references/templates/web_api.md` + `references/checklists/web_review.md`
- Web DB: `references/templates/web_db.md` + `references/checklists/web_review.md`
- Web UI/UX: `references/templates/web_uiux.md` + `references/checklists/web_review.md`
- ML experiment: `references/templates/ml_experiment.md` + `references/checklists/ml_review.md`
- CV pipeline: `references/templates/cv_pipeline.md` + `references/checklists/ml_review.md`
- Unknown domain: `references/templates/general.md` + `references/checklists/general_review.md`

3. Phase 1 - Requirements
- Produce `requirements.md` with:
  - User stories or jobs-to-be-done
  - Scope and out-of-scope
  - Edge cases
  - Acceptance criteria in EARS style
- Pause for review and require explicit user confirmation.

4. Phase 2 - Design
- Produce `design.md` with:
  - Architecture and data flow
  - Major technical decisions and tradeoffs
  - Integration constraints and failure handling
- Pause for review and require explicit user confirmation.

5. Phase 3 - Tasks
- Produce `tasks.md` with atomic tasks.
- Each task must include a verification method (unit/integration/manual).
- Prefer TDD: test first when feasible.
- For logic-changing tasks, require explicit evidence fields:
  - `red_evidence`: failing test name and failure signal
  - `green_evidence`: passing test name and pass signal
  - `refactor_check`: confirmation that tests still pass after cleanup
- Pause for final sign-off before coding.

6. Implementation handoff
- Start code changes only after approved `tasks.md`.
- Keep spec files aligned with implementation; update stale sections immediately.

## Instructions

- Keep docs lean; avoid duplicate or decorative text.
- Do not output all phases at once. Complete one phase, stop, and request review.
- Do not jump into coding when core requirements or acceptance criteria are unresolved.
- Use precise, testable language. Avoid vague criteria like "works well" or "fast enough".
- Use EARS format for acceptance criteria:
  - `When <trigger>, the system shall <observable behavior>.`
  - `If <precondition>, the system shall <observable behavior>.`
- Every phase must track:
  - Open questions
  - Assumptions
  - Risks and mitigation
- Ask for missing domain constraints early (security, compliance, latency, cost).
- For destructive operations (schema drops, data deletion, irreversible migrations), require explicit approval plus rollback/backups in the design.

## Fallback and expansion

- If no domain template fits, use `general.md` and continue delivery.
- After first approved spec in a new domain, propose extracting a new template/checklist for reuse.
- Do not block current delivery while waiting for new template creation.

## Deliverable contract

- `requirements.md`: clear "what/why" and EARS acceptance criteria.
- `design.md`: clear "how" with explicit constraints/tradeoffs.
- `tasks.md`: executable sequence with verification per task, including `red_evidence`, `green_evidence`, and `refactor_check` for logic tasks.
