# CI/CD Troubleshooting Practical Reference

Use this file for fast diagnosis of deployment and pipeline failures.

## 1. Security and Connectivity

### 1.1 SSH host verification
Problem: Using `StrictHostKeyChecking=no` weakens SSH trust checks.
Fix: Preload host keys with `ssh-keyscan`.
```yaml
before_script:
  - mkdir -p ~/.ssh
  - ssh-keyscan -H "$SSH_HOST" >> ~/.ssh/known_hosts
  - chmod 644 ~/.ssh/known_hosts
```

### 1.2 Repo sync in deployment host
Problem: `git clone` fails when target directory already exists.
Fix: Use fetch + fast-forward + detached checkout.
```bash
if [ ! -d "$PROJECT_DIR" ]; then
  git clone "$REPO_URL" "$PROJECT_DIR"
else
  cd "$PROJECT_DIR"
  git fetch --all --prune
  git checkout "$CI_COMMIT_BRANCH" || git checkout -b "$CI_COMMIT_BRANCH" "origin/$CI_COMMIT_BRANCH"
  git merge --ff-only "origin/$CI_COMMIT_BRANCH"
  git checkout --detach "$CI_COMMIT_SHA"
fi
```

## 2. Runtime Stability

### 2.1 GPU OOM before service start
Problem: model container crashes due to memory exhaustion.
Prevention:
- NVIDIA: check `nvidia-smi`.
- AMD: check `rocm-smi`.

## 3. Common Errors

### "Permission denied (publickey)"
- Cause: invalid key value, bad newline formatting, or missing public key in target host `authorized_keys`.
- Fix: re-import key to CI variables and verify branch protection scope.

### "docker: command not found"
- Cause: runner image has no docker binary.
- Fix: ensure deployment script runs Docker commands on remote host where Docker is installed.

### "xhost: unable to open display"
- Cause: `DISPLAY=:0` set on headless host without active X server.
- Fix: remove GUI-specific commands for headless deployment, or provide virtual display.

## 4. Triage Order
1. Confirm branch/tag trigger and job rules.
2. Confirm secrets and SSH connectivity.
3. Confirm repository sync and target revision.
4. Confirm runtime dependencies on target host (Docker, GPU drivers, display stack).
