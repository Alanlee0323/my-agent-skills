---
name: using-ultralytics
description: Expert system for Ultralytics YOLO workflows (including YOLO26). Use when the user asks about training, validation, inference, dataset setup, model export, tracking, or performance tuning in Ultralytics.
---

# Ultralytics (YOLO) Skill

Expert system for Ultralytics YOLO models (Object Detection, Segmentation, Classification).

## When to Use This Skill

This skill should be triggered when:
- Training Ultralytics YOLO models (including YOLO26)
- Running inference (detection, segmentation, pose estimation)
- Exporting models to ONNX, TensorRT, CoreML, etc.
- Configuring datasets (COCO, custom YAML)
- Debugging training pipelines or performance issues
- **Training Config Requests**: "Set batch size to 128", "Train on CPU", "Use optimizer SGD"

## Logic Flow & Decision Tree

### 0. Configuration Gatekeeper (The OOM Stopper)
**When**: User proposes specific training parameters (Batch Size, Device, Image Size).
**Action**:
1.  **PAUSE**. Perform a "Mental Simulation" of resource usage.
2.  **Calculate (Heuristic)**:
    *   `YOLO26x` + `Batch 128` ≈ **40GB+ VRAM Needed**.
    *   `CPU Training` + `Large Model` = **Extremely Slow (Days)**.
3.  **BLOCK/WARN**:
    > "Training YOLO26x with Batch 128 requires ~40GB VRAM (A100 class). Your environment (Laptop GPU/CPU) will likely crash (OOM). Recommendation: Batch 4 or 8."

## Pre-Flight Checks (Mandatory)

Before starting any training run, you MUST:

1.  **Check GPU Resources (CUDA/ROCm)**:
    *   Verify device availability: `torch.cuda.is_available()`
    *   Check VRAM capacity: `nvidia-smi` or `torch.cuda.get_device_properties(0).total_memory`
    *   **Auto-Batch Suggestion**:
        *   < 6GB VRAM: `batch=4` or `batch=8`
        *   6GB - 12GB VRAM: `batch=16`
        *   > 12GB VRAM: `batch=32`+
        *   *Tip*: Use `batch=-1` for Ultralytics auto-batch if unsure.

2.  **Verify Data Leakage**:
    *   Ensure NO overlap between Train and Val image files.


## Quick Reference

### Common Patterns

**Pattern 1: Train Model (CLI)**
```bash
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640
```

**Pattern 2: Predict (CLI)**
```bash
yolo detect predict model=yolo26n.pt source='https://ultralytics.com/images/bus.jpg'
```

**Pattern 3: Export Model**
```bash
yolo export model=yolo26n.pt format=onnx
```

**Pattern 4: Train (Python)**
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

**Pattern 5: Predict (Python)**
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
results = model("path/to/image.jpg")
```

**Pattern 6: Segmentation Training**
```python
model = YOLO("yolo26n-seg.pt")
model.train(data="coco8-seg.yaml", epochs=100)
```

## Reference Files

This skill includes comprehensive documentation in `references/`:

- **guides.md** - Step-by-step guides for common tasks.
- **models.md** - Details on available model architectures.
- **datasets.md** - How to format and use datasets.
- **tasks.md** - Explanation of tasks (Detect, Segment, Classify, Pose, OBB).
- **modes.md** - Modes of operation (Train, Val, Predict, Export, Track).
- **detect.md** - Specifics for object detection.

Read these files on demand for in-depth information.

## usage

### For Beginners
Start with `references/tasks.md` to understand the capabilities (Detect, Segment, etc.) and `references/modes.md` for the workflow (Train -> Val -> Predict).

### For Custom Training
Refer to `references/datasets.md` to ensure your data YAML and directory structure are correct before starting training.

### For Deployment
Check `references/guides.md` (or export documentation) for details on optimizing models for different hardware using `yolo export`.
