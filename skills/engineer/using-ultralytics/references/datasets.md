# Ultralytics Datasets Reference

Use this file when preparing dataset contracts for training.

## 1. Dataset YAML Contract

Minimal detection dataset YAML:

```yaml
path: /data/my-dataset
train: images/train
val: images/val
test: images/test
names:
  0: person
  1: car
```

## 2. Directory Layout (Detect example)
```text
my-dataset/
  images/
    train/
    val/
    test/
  labels/
    train/
    val/
    test/
```

## 3. Annotation Hygiene Checklist
- Every image has matching label file (or intentionally empty).
- Class ids are contiguous and match `names`.
- Train/val/test splits have no overlap.
- Corrupt images and malformed labels are removed before training.

## 4. Split Policy
- Keep validation set stable across experiments.
- Use test split only for final reporting.
- For small data, prefer k-fold only when task requires robustness estimates.

## 5. Quick Sanity Run
```bash
yolo detect train data=dataset.yaml model=yolo26n.pt epochs=1 imgsz=640
```

Use a 1-epoch smoke test to catch path/schema issues before full training.

## 6. Common Failures
- Wrong `path` root in YAML.
- Class count mismatch between labels and `names`.
- Mixed annotation formats in one dataset.

## Official Links
- Datasets overview: https://docs.ultralytics.com/datasets/
- Detection datasets: https://docs.ultralytics.com/datasets/detect/
- Segmentation datasets: https://docs.ultralytics.com/datasets/segment/
- Pose datasets: https://docs.ultralytics.com/datasets/pose/
- OBB datasets: https://docs.ultralytics.com/datasets/obb/
