# Ultralytics Models Reference

Use this file to select model family and size before training.

## Model Families (high level)
- YOLO family: default general-purpose models.
- Specialized families in Ultralytics docs: RT-DETR, SAM/FastSAM, YOLO-World, YOLOE (availability depends on task/workflow).

## Size Selection Heuristic (n/s/m/l/x)
- `n`: fastest, lowest memory, lower accuracy ceiling.
- `s`/`m`: balanced choice for most production teams.
- `l`/`x`: higher accuracy potential, high VRAM and latency cost.

## Practical Selection Flow
1. Start with `n` or `s` to validate data and pipeline.
2. Promote to `m` only if metrics are below target and hardware budget allows.
3. Use `l/x` only with explicit latency and memory acceptance.

## Checkpoint Naming Convention
- Detect: `yolo26n.pt`, `yolo26s.pt`, ...
- Segment: `yolo26n-seg.pt`, ...
- Classify: `yolo26n-cls.pt`, ...
- Pose: `yolo26n-pose.pt`, ...
- OBB: `yolo26n-obb.pt`, ...

## Promotion Guardrails
- Compare against baseline with fixed dataset split and seed.
- Keep one change per experiment (model size OR augmentation OR optimizer).
- Log runtime cost (VRAM, FPS/latency, training wall time), not accuracy only.

## Official Links
- Models overview: https://docs.ultralytics.com/models/
- RT-DETR page: https://docs.ultralytics.com/models/rtdetr/
