# Ultralytics Guides Reference

Use this file as a curated map to advanced guides.

## High-Value Guide Categories
- Environment setup (Conda, Docker, package installation).
- Training optimization (hyperparameter tuning, augmentation strategy).
- Deployment/export (ONNX, TensorRT, TFLite, Edge TPU, CoreML).
- Workflow operations (benchmarking, tracking, monitoring outputs).

## Suggested Read Order
1. Environment setup guide for your platform.
2. Task + mode docs (`tasks.md`, `modes.md`) for baseline workflow.
3. Deployment guide matching your target runtime.
4. Optimization guides only after baseline is reproducible.

## Practical Rule
- Do not tune hyperparameters until data quality and split policy are verified.
- Do not optimize export target until baseline val metrics are stable.

## Official Links
- Guides index: https://docs.ultralytics.com/guides/
- Conda quickstart: https://docs.ultralytics.com/guides/conda-quickstart/
- Hyperparameter tuning: https://docs.ultralytics.com/guides/hyperparameter-tuning/
