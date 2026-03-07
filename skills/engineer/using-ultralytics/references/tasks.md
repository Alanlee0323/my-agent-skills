# Ultralytics Tasks Reference

Use this file to choose the correct task before writing training code.

## Supported Tasks
- `detect`: Bounding-box object detection.
- `segment`: Instance segmentation (pixel masks).
- `classify`: Image-level classification.
- `pose`: Keypoint detection / pose estimation.
- `obb`: Oriented bounding box detection.

## Task Selection Heuristic
- Need object location only -> `detect`.
- Need exact object shape -> `segment`.
- Need one label per image -> `classify`.
- Need joints/keypoints -> `pose`.
- Need rotated boxes (aerial/docs/industrial) -> `obb`.

## Minimal CLI Patterns
```bash
yolo detect train data=dataset.yaml model=yolo26n.pt epochs=100 imgsz=640
yolo segment train data=dataset.yaml model=yolo26n-seg.pt epochs=100 imgsz=640
yolo classify train data=dataset.yaml model=yolo26n-cls.pt epochs=100 imgsz=224
yolo pose train data=dataset.yaml model=yolo26n-pose.pt epochs=100 imgsz=640
yolo obb train data=dataset.yaml model=yolo26n-obb.pt epochs=100 imgsz=640
```

## Minimal Python Pattern
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.train(data="dataset.yaml", epochs=100, imgsz=640)
```

## Common Mistakes
- Wrong task-model pair (for example running `detect` with `-seg` weights).
- Dataset format does not match task annotations.
- Evaluating with wrong metrics for task type.

## Official Links
- Tasks overview: https://docs.ultralytics.com/tasks/
- Detect: https://docs.ultralytics.com/tasks/detect/
- Segment: https://docs.ultralytics.com/tasks/segment/
- Classify: https://docs.ultralytics.com/tasks/classify/
- Pose: https://docs.ultralytics.com/tasks/pose/
- OBB: https://docs.ultralytics.com/tasks/obb/
