# Ultralytics Detect Task Reference

Detection is the default starting task for object localization + classification.

## 1. Train

CLI:
```bash
yolo detect train data=dataset.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Python:
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
results = model.train(data="dataset.yaml", epochs=100, imgsz=640)
```

## 2. Validate
```bash
yolo detect val model=runs/detect/train/weights/best.pt data=dataset.yaml
```

Key outputs include mAP metrics and per-class quality.

## 3. Predict
```bash
yolo detect predict model=runs/detect/train/weights/best.pt source=demo.jpg
```

## 4. Export
```bash
yolo export model=runs/detect/train/weights/best.pt format=onnx
```

## 5. Pre-Flight Checklist
- Dataset YAML path is correct.
- Labels follow YOLO detection format.
- Train/val split has no leakage.
- Batch size fits device memory.

## 6. Failure Patterns
- `CUDA out of memory`: reduce `batch` or model size.
- Poor validation mAP with good train mAP: likely overfitting or leakage.
- Many false positives: check class balance and label quality.

## Official Link
- Detect task docs: https://docs.ultralytics.com/tasks/detect/
