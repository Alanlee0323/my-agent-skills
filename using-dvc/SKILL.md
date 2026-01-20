---
name: using-dvc
description:  Actively assists and enforces best practices for Data Version Control (DVC). Use when the user asks about versioning large files, creating pipelines, or reproducing experiments.
---

# DVC Skill

Expert system for Data Version Control (DVC) operations.

## When to Use This Skill

This skill should be triggered when:
- Versioning large datasets or models (that git cannot handle)
- Defining and running reproducible data pipelines (`dvc.yaml`)
- Tracking and comparing machine learning experiments
- Debugging DVC cache or remote storage issues
- **Rule Enforcement**: Always check if `dvc commit` and `git commit` are in sync when data changes.

## Quick Reference

### Common Patterns

**Pattern 1: Initialize DVC**
```bash
dvc init
git commit -m "Initialize DVC"
```

**Pattern 2: Versioning specific file**
```bash
dvc add data/data.xml
git add data/data.xml.dvc data/.gitignore
git commit -m "Add data.xml to DVC"
```

**Pattern 3: Define Pipeline Stage**
```bash
dvc run -n prepare \
          -p prepare.seed,prepare.split \
          -d src/prepare.py -d data/data.xml \
          -o data/prepared \
          python src/prepare.py data/data.xml
```

**Pattern 4: Reproduce Pipeline**
```bash
dvc repro
```

**Pattern 5: Push/Pull Data**
```bash
dvc push
dvc pull
```

**Pattern 6: Metrics and Plots**
```bash
dvc metrics show
dvc plots show
```

### Example Code Patterns

**Example 1: Configure Remote (S3)**
```bash
dvc remote add -d myremote s3://mybucket/dvcstore
dvc remote modify myremote endpointurl https://s3.us-west-1.amazonaws.com
```

**Example 2: DVC YAML Structure**
```yaml
stages:
  prepare:
    cmd: python src/prepare.py data/data.xml
    deps:
      - data/data.xml
      - src/prepare.py
    params:
      - prepare.seed
      - prepare.split
    outs:
      - data/prepared
```

## Reference Files

This skill includes documentation in `references/`:

- **other.md** - General DVC documentation notes (Contribution guide).

> [!NOTE]
> The reference documentation is currently limited. Rely on `dvc --help` or the official website for complex inquiries not covered by the Quick Reference.

## usage

### For Beginners
Start with `dvc init` and `dvc add` to understand the basic workflow of tracking files alongside git.

### For Pipelines
Use `dvc run` (or edit `dvc.yaml` directly) to define stages. Use `dvc repro` to execute them.

### For Debugging
Use `dvc doctor` to diagnose environment issues.
