---
name: using-mlflow
description: Provides MLflow documentation covering Tracking, Projects, Models, and Registry. Use when the user asks about MLflow features, APIs, implementation, or debugging.
---

# MLflow Skill

Expert system for MLflow operations, tracking, and model management.

## When to Use This Skill

This skill should be triggered when:
- Working with MLflow Tracking, Projects, Models, or Registry
- Looking up MLflow API references or feature documentation
- Implementing MLflow integration in machine learning pipelines
- Debugging MLflow-related errors or issues
- Seeking best practices for experiment tracking and model deployment

## Quick Reference

### Common Patterns

**Pattern 1: Install MLflow**
```bash
pip install mlflow[auth]
```

**Pattern 2: Command Line Help**
```bash
mlflow --help
```

**Pattern 3: Install Extras**
```bash
# Time series
pip install mlflow[sktime]
pip install mlflavors
# Visualization
pip install mlflow-vizmod
# Cloud
pip install bigmlflow
pip install mlflow[aliyun-oss]
```

**Pattern 4: Start UI**
```bash
mlflow ui
```

**Pattern 5: referencing models**
```
models:/<model_name>/<version>
models:/<model_name>/Production
```

**Pattern 6: Log Model (PyTorch example)**
```python
mlflow.pytorch.log_model(model, "model")
```

### Example Code Patterns

**Example 1: Configure S3 Endpoint (Bash)**
```bash
export MLFLOW_S3_ENDPOINT_URL=https://s3.us-west-1.amazonaws.com
```

**Example 2: Set Bucket Owner (Bash)**
```bash
export MLFLOW_S3_EXPECTED_BUCKET_OWNER=123456789012
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **ml.md** - Complete MLflow documentation covering all major components.

Use the `view_file` tool to read specific sections of these files when the user needs detailed explanations.

## usage

### For Beginners
Start by reading the overview or getting started sections in `references/ml.md` to understand the core concepts of Runs, Experiments, and the Tracking Server.

### For API Lookups
Search for the specific function or class name (e.g., `mlflow.log_param`, `mlflow.sklearn.log_model`) within `references/ml.md` to find parameters and usage examples.

### For Troubleshooting
Check the reference documentation for configuration options and common pitfalls, especially regarding authentication and remote server connectivity.
