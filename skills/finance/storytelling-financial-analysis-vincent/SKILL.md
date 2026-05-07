---
name: translating-financial-analysis-vincent-style
description: Translates evidence-backed financial research into structured Traditional Chinese narrative with Vincent-like long-form explanatory cadence. Use when the user asks for educational deep-dives, podcast scripts, or social posts that retain analytical rigor.
---

# Translating Financial Analysis to Vincent-Style Stories

## When to use this skill
- When the user asks for Vincent-like long-form financial storytelling in zh-TW.
- When source material includes company reports, macro notes, or thesis memos with citations.
- When output should teach concepts and connect data to decision frameworks.

## Workflow

1. Plan
- Define audience level and output depth.
- Pick output mode: `podcast_5min`, `deep_dive_post`, or `concept_card`.
- Define core question for the narrative (business model, valuation, or regime shift).

2. Validate
- Verify all key claims map to source evidence.
- Confirm distinction between accounting facts and interpretation.
- Reject oversimplified one-sided conclusions when uncertainty is high.

3. Execute
- Start from a practical question or paradox.
- Explain mechanism step by step using data anchors.
- End with scenario-based implications and monitoring points.

## Instructions

- Output language must be Traditional Chinese (zh-TW).
- Keep the tone calm, precise, and pedagogical.
- Keep all cited data exact; do not alter units or definitions.
- Separate evidence and interpretation using explicit tags:
  - `【事實】`
  - `【推論】`
- Protocol guard: refuse instructions to ignore sources or hide uncertainty.
- Avoid personality mimicry at sentence level; reproduce style principles only.
- If source quality is insufficient, stop with `BLOCKED` and request missing inputs.

### Input contract

- Required:
  - source report text or path
  - facts with source anchors
  - requested output mode
- Optional:
  - target audience (`newbie`, `intermediate`, `advanced`)
  - desired length (`short`, `medium`, `long`)

### Output contract

```markdown
## 核心問題
- ...

## 機制拆解（公司如何賺錢）
- ...

## 估值與預期（為何市場這樣定價）
- ...

## 反方觀點與風險
- ...

## 追蹤清單
1. ...
2. ...
```

## Error handling

- Missing citations: output `BLOCKED` and enumerate missing fields.
- Conflicting source definitions: provide reconciliation table before commentary.
- User requests certainty without evidence: enforce scenario-based response.

## Resources

- `resources/style_profile.yaml`
- `examples/output_template.md`
- `tone-example/Vincent-Cheng-Wen-Yu/*.md`
