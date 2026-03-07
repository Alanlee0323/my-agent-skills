# ML Experiment SDD Template

## 1. Experiment Contract
- Hypothesis:
- Target metric and threshold:
- Minimum acceptable baseline:

## 2. Dataset Contract
- Data sources:
- Feature schema:
- Label definition:
- Split strategy (train/val/test):
- Leakage prevention rules:

## 3. Training Plan
- Candidate models:
- Hyperparameter search space:
- Resource budget (GPU/CPU/time):
- Reproducibility requirements (seed/versioning):

## 4. Evaluation Plan
- Primary metrics:
- Secondary guardrail metrics:
- Slice analysis:
- Failure criteria:

## 5. Deployment Constraints
- Inference latency target:
- Model size/memory limit:
- Monitoring and drift detection:

## 6. Acceptance Criteria (EARS)
- When `<training runs on approved data split>`, the system shall `<produce reproducible metric report>`.
- If `<metric under threshold>`, the system shall `<block promotion and report failure reason>`.
- When `<model promoted>`, the system shall `<register version and metadata>`.

