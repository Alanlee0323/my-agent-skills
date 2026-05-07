# Ultralytics Modes Reference

Modes define what lifecycle action to run.

## Mode Map
- `train`: Fit model on training set.
- `val`: Evaluate trained model on validation/test set.
- `predict`: Run inference on images/video/stream.
- `export`: Convert model to ONNX, TensorRT, CoreML, etc.
- `track`: Detect + multi-object tracking on video stream.
- `benchmark`: Compare performance across export targets.

## Typical Lifecycle
1. `train`
2. `val`
3. `predict`
4. `export`
5. `benchmark`
6. Optional `track` for video use cases

## CLI Patterns
```bash
yolo detect train data=dataset.yaml model=yolo26n.pt epochs=100 imgsz=640
yolo detect val model=runs/detect/train/weights/best.pt data=dataset.yaml
yolo detect predict model=runs/detect/train/weights/best.pt source=demo.jpg
yolo export model=runs/detect/train/weights/best.pt format=onnx
yolo track model=runs/detect/train/weights/best.pt source=demo.mp4
yolo benchmark model=runs/detect/train/weights/best.pt data=dataset.yaml imgsz=640
```

## Guardrails
- Never skip `val` before export/promotion.
- Freeze dataset version before benchmarking.
- Compare benchmark results on the same hardware and batch size.

## Official Link
- Modes overview: https://docs.ultralytics.com/modes/
