---
name: creating-skills-from-knowledge-folder
description: Creates new agent skills from a user-specified knowledge folder. Use when the user asks to convert notes, docs, templates, or domain references into reusable SKILL.md packages.
---

# Creating Skills from Knowledge Folder

## When to use this skill
- When the user provides a folder containing domain knowledge and asks to build new skills from it.
- When the user asks to batch-create or update skills from curated references.
- When skill drafting must follow `creating-agent-skills` and be audited by `reviewing-agent-skills`.

## Workflow

1. Plan
- Confirm the knowledge folder path and target output path.
- Confirm scope: create new skills, update existing skills, or both.
- Confirm target domains (for example: finance, engineering, legal).

2. Validate
- Build a file inventory (type, size, language, recency).
- Mark unsupported or low-quality inputs.
- Group files by domain intent and likely skill boundaries.

3. Execute
- For each domain group:
  - Propose skill name candidates (gerund, lowercase-hyphen).
  - Draft `SKILL.md` using `creating-agent-skills` conventions.
  - Run reviewer checklist from `reviewing-agent-skills`.
  - Apply fixes and output final skill package.

## Instructions

- Treat the folder as source-of-truth evidence, not a prompt dump.
- Do not merge unrelated domains into one oversized skill.
- Prefer multiple small skills over one broad skill.
- Keep each generated `SKILL.md` focused on:
  - Trigger conditions
  - Deterministic workflow
  - Validation/error handling
- If source material conflicts, preserve both viewpoints and ask user to resolve policy conflicts.

### Intake checklist

- [ ] Folder path confirmed
- [ ] Read permissions confirmed
- [ ] Inventory generated
- [ ] Domain clusters identified
- [ ] Candidate skill map approved

### Output contract

For each generated skill, return:

```markdown
## Generated Skill: <skill-id>
- Source files used: <list>
- Scope boundaries: <inclusions/exclusions>
- Risk notes: <hallucination risk, stale docs, conflicts>
- Audit verdict: <PASS/WARN/FAIL>
```

## Error handling

- If folder is missing or unreadable, stop and request a valid path.
- If files are too large or noisy, propose staged ingestion by subfolder.
- If confidence is low due to sparse sources, produce draft with explicit WARN status.

## Resources

- `creating-agent-skills`
- `reviewing-agent-skills`

