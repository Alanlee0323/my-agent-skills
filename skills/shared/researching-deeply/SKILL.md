---
name: researching-deeply
description: Systematic deep-investigation methodology for auditing codebases, evaluating systems, and researching complex questions. Enforces breadth-first mapping, claim-evidence discipline, cross-artifact consistency checks, and negative-space analysis. Use when the user asks for a deep review, audit, investigation, 深度檢視, 盤點, 稽核, or when a conclusion will drive an important decision.
version: 1.0.0
---

# Researching Deeply

Distilled investigation methodology. The goal of any deep research task is not "read a lot" —
it is to produce **decision-grade findings**: every claim traceable to evidence, every gap
made explicit, ranked by impact.

## When to use this skill

- Deep review / audit of a codebase, skill library, config system, or document set.
- Research questions where a wrong conclusion is expensive (architecture, investment, migration).
- Any task phrased as: 深度檢索, 深度檢視, 全面盤點, 稽核, "is X complete/correct/consistent?".

## Core Principles（順序即優先級）

### 1. Map before you read（先測繪，後深讀）

Never start by reading files one-by-one. First build a complete inventory of the terrain:

- List every directory, file, and artifact class (`glob`, `ls -R`, `git log --oneline`).
- Identify the *artifact types*: source of truth, derived docs, config, indexes, external refs.
- Only then choose what to read deeply — and read the **governing documents first**
  (README, rules, schemas), because they tell you what the system *claims* to be.

> Rationale: depth without a map produces anecdotes. The map lets you know when you are done.

### 2. Gather evidence in parallel, conclude in series

- Batch independent lookups together (multiple reads/searches per round, not one at a time).
- Never form the verdict until the inventory pass is complete — early conclusions bias
  which evidence you look for afterward (confirmation bias applies to agents too).

### 3. Claim–evidence discipline（主張必附證據）

Every finding must carry a pointer that lets someone else re-verify it in under a minute:

- Code/docs: `path/to/file.md:42`
- Data: value + source + retrieval timestamp
- External: URL + accessed date

If you cannot attach a pointer, downgrade the claim to a hypothesis and label it as such.

### 4. Cross-artifact consistency check（漂移偵測——最高產出的單一技巧）

**Any fact maintained in more than one place will eventually diverge.** This is where the
highest-value findings live. Procedure:

1. Enumerate every place a given fact is recorded (e.g., a skill's name may appear in:
   frontmatter, folder name, routing table, bundle yaml, README index, other skills' text).
2. Extract the value from each location mechanically (grep/script, not memory).
3. Diff them. Every mismatch is a confirmed finding — no judgment call needed.

Typical high-yield fact classes: names/identifiers, version numbers, file paths,
counts ("we have N modules"), mandatory-rule references, model/API identifiers.

### 5. Negative-space analysis（檢查「應存在而不存在」的東西）

Absence is evidence. For each rule or convention the system declares, ask:
"if this rule were followed, what artifact would exist?" — then check for it.

- Examples: a review gate that mandates audit reports → count actual audit files;
  a skill referencing a file under its `resources/` folder → verify the file exists;
  a doc citing a script → verify the script is in the repo.

### 6. Self-application check（系統是否遵守自己的規則）

Run the system's own standards against itself. A naming convention document that violates
its own naming convention is both a real defect and a signal of missing enforcement.

### 7. Triangulate load-bearing claims（關鍵結論需雙來源）

Any claim that the final recommendation depends on needs ≥2 independent confirmations
(e.g., code + config, or doc + git history). Single-source claims get a confidence tag.

### 8. Grade confidence explicitly

Use a fixed vocabulary so readers can calibrate:

- `CONFIRMED` — mechanically verified (diff, existence check, executed command).
- `PLAUSIBLE` — inferred from consistent evidence, not directly executed.
- `HYPOTHESIS` — pattern-matched; needs verification before acting on it.

### 9. Findings-first reporting（結論先行）

Structure the output for the reader, not for your process:

1. **Verdict first** — one paragraph: overall state + the single biggest risk.
2. **Confirmed findings** — each with evidence pointer, ordered by impact (not by discovery order).
3. **Structural gaps** — problems with the *system*, not just instances (an instance is
   "this link is broken"; the structural gap is "nothing detects broken links").
4. **Prioritized recommendations** — ordered by leverage: fixes that prevent future
   defect classes rank above fixes for single defects.

### 10. Know when to stop

Stop conditions — declare completion when any holds:

- The inventory is fully covered and new samples repeat known finding classes (saturation).
- Remaining unknowns cannot change the verdict.
- Deeper digging requires inputs only the requester can provide → list them and stop.

## Anti-patterns（紅線）

- ❌ Reading files in discovery order instead of governance-first order.
- ❌ Reporting findings in the order you found them (order by impact instead).
- ❌ "Looks fine" without stating what was checked — always enumerate the checks performed.
- ❌ Fixing things mid-investigation when the deliverable is an assessment (report first;
  change only on request).
- ❌ Summary compression that drops evidence pointers — a finding without a pointer is a rumor.

## Output contract

```markdown
## 總評
<verdict paragraph: state + biggest risk>

## 已確認發現（依影響排序）
1. [CONFIRMED] <finding> — 證據: <path:line / url+date>
...

## 結構性缺口
A. <system-level gap and why instances will recur>
...

## 建議優先順序
1. <highest-leverage action> — <why first>
...
```

## Evolution Log

- 2026-07-04 v1.0.0 — Initial capture. Distilled from a full-library drift audit session
  (Claude Fable 5): the cross-artifact consistency check (#4) and negative-space analysis
  (#5) produced 7 confirmed findings in that session; codified here for reuse by any agent.
