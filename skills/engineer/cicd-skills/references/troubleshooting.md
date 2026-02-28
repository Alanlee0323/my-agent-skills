# Troubleshooting & Best Practices

## Expert Recommendations 🛡️

### 1. Security: SSH Key Scanning
**Problem**: Using `StrictHostKeyChecking=no` allows Man-in-the-Middle attacks.
**Fix**: Use `ssh-keyscan` to populate known hosts securely.
```yaml
before_script:
  - mkdir -p ~/.ssh
  - ssh-keyscan -H "$SSH_HOST" >> ~/.ssh/known_hosts
  - chmod 644 ~/.ssh/known_hosts
```

### 2. Efficiency: Git Fetch vs Clone
**Problem**: `git clone` fails if the directory exists.
**Fix**: Use fetch & reset.
```bash
if [ ! -d "$PROJECT_DIR" ]; then
  git clone "$REPO_URL" "$PROJECT_DIR"
else
  cd "$PROJECT_DIR"
  git fetch --all
  git reset --hard origin/$CI_COMMIT_BRANCH
fi
```

### 3. Hardware: OOM (Out Of Memory)
**Problem**: Deep Learning models often crash if VRAM is full.
**Prevention**: Run this check *before* deploying.
- **Nvidia**: `nvidia-smi` (Check Memory-Usage)
- **AMD**: `rocm-smi`

## Common Errors

### "Permission denied (publickey)"
- **Cause**: `SSH_PRIVATE_KEY` variable is wrong, has extra newlines, or the public key isn't in `~/.ssh/authorized_keys` on the target machine.
- **Fix**: Re-copy the private key to GitLab Variables. uncheck "Protect" if testing on a non-protected branch.

### "docker: command not found"
- **Cause**: The `alpine` image used in CI doesn't have docker installed.
- **Fix**: The CI script actually uses SSH to run docker *on the remote host*, not the runner. Ensure the *remote host* has docker installed.

### "xhost: unable to open display"
- **Cause**: `DISPLAY=:0` is set but no X server is running (headless server).
- **Fix**: If you don't need GUI, remove `xhost` and `DISPLAY` vars. If you do (for visualization), ensure a monitor is plugged in or a virtual display is running.
