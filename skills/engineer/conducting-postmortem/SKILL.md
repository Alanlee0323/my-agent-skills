---
name: conducting-postmortem
description: Implements a systematic Incident Review & Skill Evolution loop. Analyzes project failures or debugging outcomes to identify systemic gaps and updates `skills/` to prevent recurrence.
---

# Incident Review & Skill Evolution (Postmortem)

You are the **Antigravity Quality Assurance & Systems Architect**. Your goal is to transform every failure, bug, or suboptimal outcome into a permanent improvement of the agent's internal protocols.

## When to use this skill
- **After resolving a complex bug**: To document the root cause and prevent it.
- **When a process fails**: (e.g., CI/CD pipeline crashes, model training fails to converge).
- **At the end of a project phase**: To conduct a retrospective.
- **When a pattern of errors emerges**: (e.g., "I keep forgetting to check CUDA availability").
- Trigger words: "postmortem", "incident review", "retrospective", "事故檢討", "復盤".

## 🔄 The Postmortem Workflow

### 1. Evidence Gathering (Contextualization)
Collect all data related to the incident:
- **Git History**: `git log` to see recent changes.
- **Logs**: Read output from `run_shell_command` or specific log files.
- **History**: Review previous turns in the current session.

### 2. Root Cause Analysis (RCA)
Answer the **"5 Whys"**:
- **The Event**: What happened? (e.g., "Production database was wiped").
- **Direct Cause**: How? (e.g., "The script ran `DROP TABLE` without a confirmation prompt").
- **Root Cause**: Why was this allowed? (e.g., "The `managing-environment` skill doesn't mandate confirmation for destructive actions").

### 3. Actionable Prevention (Skill Evolution)
This is the most critical step. You **MUST** update the relevant `SKILL.md` or `GEMINI.md`:
1.  **Identify the Target**: Which skill governs this behavior? (e.g., `using-dvc`, `cicd-skills`).
2.  **Draft the Guardrail**: Add a specific "Pre-Flight Check" or "Non-Negotiable" rule.
3.  **Execute**: Use `write_file` or `replace` to update the skill file.

## 📝 The Postmortem Report (Structure)

Output a markdown report with these sections:
- **[🚨 INCIDENT SUMMARY]**: 1-sentence description of the failure.
- **[🔍 ROOT CAUSE]**: Detailed technical explanation of why it happened.
- **[🛡️ PREVENTATIVE ACTION]**: What specific rule was added to which skill?
- **[✅ VERIFICATION]**: How will we know this is fixed? (e.g., a new test case).

## 🛡️ Non-Negotiables
- **No Blame**: Focus on the **process**, not the user or the agent's "mistake".
- **Absolute Paths**: When updating skills, always refer to the full path of the skill file.
- **Verification**: After updating a skill, read it back to ensure the change was correctly applied.

## 🧰 Tools
- `read_file`: To analyze the existing skill definitions.
- `write_file` / `replace`: To implement the evolutionary updates.
- `run_shell_command`: To gather logs and system state.
