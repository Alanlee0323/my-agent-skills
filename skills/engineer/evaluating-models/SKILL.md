---
name: evaluating-models
description: Expert system for evaluating machine learning models. Automates the analysis of Confusion Matrices, PR Curves, and MLflow history comparison to provide objective, data-driven recommendations.
---

# Model Evaluation Expert

## When to use this skill
- When a training run completes.
- When the user asks "How is the model performing?".
- When comparing multiple experimental runs.
- When generating reports for stakeholders.

## Core Capabilities

1.  **Deep Metric Analysis**:
    *   **Confusion Matrix**: Identify specific class confusion (e.g., "Model constantly mistakes 'background' for 'person'").
    *   **PR Curve (Precision-Recall)**: Analyze the trade-off. Is the model aggressive or conservative?
    *   **F1-Score**: Check the harmonic mean at different confidence thresholds.

2.  **Historical Benchmarking (MLflow)**:
    *   **Rule**: NEVER evaluate a run in isolation.
    *   **Action**: Query MLflow for the `best_run` (highest mAP50 or mAP50-95).
    *   **Comparison**: Calculate delta (e.g., "mAP50 improved by +2.5% vs baseline").

3.  **Objective Recommendations**:
    *   Based on data, suggested next steps (e.g., "Increase background images", "Tune IoU threshold", "Add more samples for class X").

## Workflow

### 1. Fetch Artifacts
Locate the evaluation artifacts (usually in `runs/detect/trainX/` or MLflow):
- `confusion_matrix.png`
- `PR_curve.png`
- `results.csv`

### 2. Analyze & Compare
Run the comparison logic:
- Current mAP@50 vs Best Historical mAP@50
- Precision vs Recall balance check

### 3. Generate Report
Output a markdown report in the following format:

```markdown
### 📊 Evaluation Report: [Run Name]

**🏆 Performance vs Baseline**
- **mAP@50**: 0.95 (+1.2% 🟢)
- **mAP@50-95**: 0.72 (-0.5% 🔻)
- **Best Run**: [Run ID] (0.938 mAP)

**🔍 Key Insights**
1. **Confusion**: Significant confusion between `dog` and `cat` (15% misclassification).
2. **Recall Risk**: High precision but low recall on `bicycle` class.

**💡 Recommendations**
- Collect more hard-negative samples for `cat`.
- Lower confidence threshold for `bicycle` deployment.
```

## Anti-Hallucination Rules
- If artifacts are missing, say "Cannot evaluate without [Artifact Name]".
- Do not invent numbers.
- If MLflow is unreachable, compare against the "Manual Baseline" provided by the user.
