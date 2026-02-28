---
name: conducting-postmortem
description: Implements a Knowledge Feedback Loop. Analyzes debugging sessions and project outcomes to identify systemic failures, then proactively updates `using-*` skills to prevent recurrence.
---

# Post-Mortem & Skill Evolution

## When to use this skill
- After a complex debugging session (`debugging-code` completion).
- At project completion (Project Retrospective).
- When the user asks "Why did this keep happening?" or "Update your protocols".
- When you detect a recurring pattern of errors related to a specific tool.

## Philosophy: The Self-Evolving Agent
> "A mistake repeated is a decision."

This skill transforms **Reactive Fixes** (fixing the code) into **Proactive Guardrails** (fixing the process).

## Workflow

### 1. Root Cause Analysis (RCA)
Analyze the recent interaction history or `debugging-code` logs.
- **Incident**: What broke? (e.g., "CUDA OOM error")
- **Root Cause**: Why? (e.g., "Batch size 64 was too large for 8GB VRAM")
- **Pattern**: Is this governed by a `using-*` skill? (e.g., `using-ultralytics`)

### 2. Gap Analysis
Check the current `SKILL.md` for the relevant tool.
- Does it already warn about this?
- Was the warning ignored, or was it missing?

### 3. Optimization Proposal
Draft an update to the `SKILL.md` to prevent this specific failure mode.
- **New Check**: Add to "Pre-Flight Checks".
- **New Reference**: Add to "Quick Reference".
- **New Rule**: Add to instructions.

### 4. Implementation
1.  **Draft**: Create the specific markdown update.
2.  **Verify**: Ensure it doesn't conflict with existing rules.
3.  **Apply**: Use `replace_file_content` to update the `SKILL.md`.

## Example Scenario

**Incident**: User faced `RuntimeError: dataset.yaml not found` when training YOLO.
**Analysis**: The `using-ultralytics` skill mentions datasets but doesn't force a path check.
**Action**:
1.  Open `my-agent-skills/skills/engineer/using-ultralytics/SKILL.md`.
2.  Add a check to "Pre-Flight Checks":
    > "Verify `data` YAML path exists and is absolute before passing to `model.train()`."
3.  Notify User: "I've updated my internal protocols to always verify YAML paths before training in the future."

## Trigger Words
- "Conduct a post-mortem"
- "Update your learnings"
- "Never let this happen again"
