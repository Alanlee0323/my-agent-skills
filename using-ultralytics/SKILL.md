---
name: using-ultralytics
description: Expert system for Ultralytics YOLOv8/v9/v10. Actively assists and enforces best practices for training, detection, segmentation, and deployment.
---

# Ultralytics (YOLO) Skill

Expert system for Ultralytics YOLO models (Object Detection, Segmentation, Classification).

## When to Use This Skill

This skill should be triggered when:
- Training YOLO models (v8, v9, v10, v11)
- Running inference (detection, segmentation, pose estimation)
- Exporting models to ONNX, TensorRT, CoreML, etc.
- Configuring datasets (COCO, custom YAML)
- Debugging training pipelines or performance issues
- **Rule Enforcement**: Check for data leakage! Ensure proper Train/Val split is defined in the YAML before starting training.

## Quick Reference

### Common Patterns

**Pattern 1: Train Model (CLI)**
```bash
yolo detect train data=coco128.yaml model=yolov8n.pt epochs=100 imgsz=640
```

**Pattern 2: Predict (CLI)**
```bash
yolo detect predict model=yolov8n.pt source='https://ultralytics.com/images/bus.jpg'
```

**Pattern 3: Export Model**
```bash
yolo export model=yolov8n.pt format=onnx
```

**Pattern 4: Train (Python)**
```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

**Pattern 5: Predict (Python)**
```python
from ultralytics import YOLO

model = YOLO("yolov8n.pt")
results = model("path/to/image.jpg")
```

**Pattern 6: Segmentation Training**
```python
model = YOLO("yolov8n-seg.pt")
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

Use `view_file` to read these files for in-depth information.

## usage

### For Beginners
Start with `references/tasks.md` to understand the capabilities (Detect, Segment, etc.) and `references/modes.md` for the workflow (Train -> Val -> Predict).

### For Custom Training
Refer to `references/datasets.md` to ensure your data YAML and directory structure are correct before starting training.

### For Deployment
Check `references/guides.md` (or export documentation) for details on optimizing models for different hardware using `yolo export`.
