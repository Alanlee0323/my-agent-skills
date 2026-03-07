# DVC Practical Reference

Use this file as the default reference when implementing DVC in a project.

## 1. Core Workflow

### 1.1 Initialize
```bash
dvc init
git add .dvc .dvcignore
git commit -m "Initialize DVC"
```

### 1.2 Track large data/model artifacts
```bash
dvc add data/raw
git add data/raw.dvc .gitignore
git commit -m "Track raw data with DVC"
```

### 1.3 Configure remote storage
```bash
dvc remote add -d storage s3://my-bucket/my-project-dvc
dvc remote modify storage endpointurl https://s3.us-west-1.amazonaws.com
git add .dvc/config
git commit -m "Configure DVC remote"
```

### 1.4 Sync data
```bash
# Upload local cache to remote
dvc push

# Download required cache from remote
dvc pull
```

## 2. Pipeline Management (`dvc.yaml`)

Prefer `dvc stage add` for new/updated pipeline stages.

```bash
dvc stage add -n prepare \
  -d src/prepare.py -d data/raw \
  -o data/processed \
  python src/prepare.py data/raw data/processed
```

Run or re-run pipeline based on changed deps/params:

```bash
dvc repro
```

Inspect status before/after:

```bash
dvc status
```

## 3. Experiment Iteration

Use experiment commands to compare candidate changes quickly:

```bash
dvc exp run
dvc exp show
dvc exp diff
```

Typical interpretation:
- `dvc exp show`: compare metrics/params across runs.
- `dvc exp diff`: compare current workspace experiment vs baseline.

## 4. Team Collaboration Rules
- Commit `.dvc` files, `dvc.yaml`, `dvc.lock`, and params files to Git.
- Do not commit large binaries tracked by DVC into Git directly.
- Pin pipeline dependencies explicitly (`-d`) to keep reproduction deterministic.
- Keep stage outputs stable and avoid writing undeclared side-effect files.

## 5. Troubleshooting

### 5.1 "file not found in cache" or missing outputs
```bash
dvc pull
dvc checkout
```

### 5.2 Remote authentication or connectivity
```bash
dvc remote list
dvc doctor
```

Check cloud credentials/environment variables for the configured remote backend.

### 5.3 Pipeline does not re-run when expected
- Verify dependencies and params are declared in `dvc.yaml`.
- Run `dvc status` to inspect which stage is stale.
- Rebuild explicitly with `dvc repro <stage-name>`.

## 6. Official Links
- Docs home: https://dvc.org/doc
- `dvc add`: https://dvc.org/doc/command-reference/add
- `dvc stage add`: https://dvc.org/doc/command-reference/stage/add
- `dvc repro`: https://dvc.org/doc/command-reference/repro
- `dvc exp`: https://dvc.org/doc/command-reference/exp
- `dvc remote add`: https://dvc.org/doc/command-reference/remote/add
