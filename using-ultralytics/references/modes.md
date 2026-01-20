# Raw-Ultralytics - Modes

**Pages:** 1

---

## Ultralytics YOLO26 Modes

**URL:** https://docs.ultralytics.com/modes/

**Contents:**
- Ultralytics YOLO26 Modes
- Introduction
  - Modes at a Glance
- Train
- Val
- Predict
- Export
- Track
- Benchmark
- FAQ

Ultralytics YOLO26 is not just another object detection model; it's a versatile framework designed to cover the entire lifecycle of machine learning models—from data ingestion and model training to validation, deployment, and real-world tracking. Each mode serves a specific purpose and is engineered to offer you the flexibility and efficiency required for different tasks and use cases.

Watch: Ultralytics Modes Tutorial: Train, Validate, Predict, Export & Benchmark.

Understanding the different modes that Ultralytics YOLO26 supports is critical to getting the most out of your models:

This comprehensive guide aims to give you an overview and practical insights into each mode, helping you harness the full potential of YOLO26.

Train mode is used for training a YOLO26 model on a custom dataset. In this mode, the model is trained using the specified dataset and hyperparameters. The training process involves optimizing the model's parameters so that it can accurately predict the classes and locations of objects in an image. Training is essential for creating models that can recognize specific objects relevant to your application.

Val mode is used for validating a YOLO26 model after it has been trained. In this mode, the model is evaluated on a validation set to measure its accuracy and generalization performance. Validation helps identify potential issues like overfitting and provides metrics such as mean Average Precision (mAP) to quantify model performance. This mode is crucial for tuning hyperparameters and improving overall model effectiveness.

Predict mode is used for making predictions using a trained YOLO26 model on new images or videos. In this mode, the model is loaded from a checkpoint file, and the user can provide images or videos to perform inference. The model identifies and localizes objects in the input media, making it ready for real-world applications. Predict mode is the gateway to applying your trained model to solve practical problems.

Export mode is used for converting a YOLO26 model to formats suitable for deployment across different platforms and devices. This mode transforms your PyTorch model into optimized formats like ONNX, TensorRT, or CoreML, enabling deployment in production environments. Exporting is essential for integrating your model with various software applications or hardware devices, often resulting in significant performance improvements.

Track mode extends YOLO26's object detection capabilities to track objects across video frames or live streams. This mode is particularly valuable for applications requiring persistent object identification, such as surveillance systems or self-driving cars. Track mode implements sophisticated algorithms like ByteTrack to maintain object identity across frames, even when objects temporarily disappear from view.

Benchmark mode profiles the speed and accuracy of various export formats for YOLO26. This mode provides comprehensive metrics on model size, accuracy (mAP50-95 for detection tasks or accuracy_top5 for classification), and inference time across different formats like ONNX, OpenVINO, and TensorRT. Benchmarking helps you select the optimal export format based on your specific requirements for speed and accuracy in your deployment environment.

Training a custom object detection model with Ultralytics YOLO26 involves using the train mode. You need a dataset formatted in YOLO format, containing images and corresponding annotation files. Use the following command to start the training process:

For more detailed instructions, you can refer to the Ultralytics Train Guide.

Ultralytics YOLO26 uses various metrics during the validation process to assess model performance. These include:

You can run the following command to start the validation:

Refer to the Validation Guide for further details.

Ultralytics YOLO26 offers export functionality to convert your trained model into various deployment formats such as ONNX, TensorRT, CoreML, and more. Use the following example to export your model:

Detailed steps for each export format can be found in the Export Guide.

Benchmark mode in Ultralytics YOLO26 is used to analyze the speed and accuracy of various export formats such as ONNX, TensorRT, and OpenVINO. It provides metrics like model size, mAP50-95 for object detection, and inference time across different hardware setups, helping you choose the most suitable format for your deployment needs.

For more details, refer to the Benchmark Guide.

Real-time object tracking can be achieved using the track mode in Ultralytics YOLO26. This mode extends object detection capabilities to track objects across video frames or live feeds. Use the following example to enable tracking:

For in-depth instructions, visit the Track Guide.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (you can choose n, s, m, l, or x versions)
model = YOLO("yolo26n.pt")

# Start training on your custom dataset
model.train(data="path/to/dataset.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Train a YOLO model from the command line
yolo detect train data=path/to/dataset.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a pretrained or custom YOLO model
model = YOLO("yolo26n.pt")

# Run validation on your dataset
model.val(data="path/to/validation.yaml")
```

Example 4 (sql):
```sql
# Validate a YOLO model from the command line
yolo val model=yolo26n.pt data=path/to/validation.yaml
```

---
