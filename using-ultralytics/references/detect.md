# Raw-Ultralytics - Detect

**Pages:** 2

---

## Object Detection

**URL:** https://docs.ultralytics.com/tasks/detect/

**Contents:**
- Object Detection
- Models
- Train
  - Dataset format
- Val
- Predict
- Export
- FAQ
  - How do I train a YOLO26 model on my custom dataset?
  - What pretrained models are available in YOLO26?

Object detection is a task that involves identifying the location and class of objects in an image or video stream.

The output of an object detector is a set of bounding boxes that enclose the objects in the image, along with class labels and confidence scores for each box. Object detection is a good choice when you need to identify objects of interest in a scene, but don't need to know exactly where the object is or its exact shape.

Watch: Object Detection with Pretrained Ultralytics YOLO Model.

YOLO26 Detect models are the default YOLO26 models, i.e., yolo26n.pt, and are pretrained on COCO.

YOLO26 pretrained Detect models are shown here. Detect, Segment, and Pose models are pretrained on the COCO dataset, while Classify models are pretrained on the ImageNet dataset.

Models are downloaded automatically from the latest Ultralytics release on first use.

Train YOLO26n on the COCO8 dataset for 100 epochs at image size 640. For a full list of available arguments see the Configuration page.

YOLO detection dataset format can be found in detail in the Dataset Guide. To convert your existing dataset from other formats (like COCO etc.) to YOLO format, please use JSON2YOLO tool by Ultralytics.

Validate trained YOLO26n model accuracy on the COCO8 dataset. No arguments are needed as the model retains its training data and arguments as model attributes.

Use a trained YOLO26n model to run predictions on images.

See full predict mode details in the Predict page.

Export a YOLO26n model to a different format like ONNX, CoreML, etc.

Available YOLO26 export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'. You can predict or validate directly on exported models, i.e., yolo predict model=yolo26n.onnx. Usage examples are shown for your model after export completes.

See full export details in the Export page.

Training a YOLO26 model on a custom dataset involves a few steps:

For detailed configuration options, visit the Configuration page.

Ultralytics YOLO26 offers various pretrained models for object detection, segmentation, and pose estimation. These models are pretrained on the COCO dataset or ImageNet for classification tasks. Here are some of the available models:

For a detailed list and performance metrics, refer to the Models section.

To validate the accuracy of your trained YOLO26 model, you can use the .val() method in Python or the yolo detect val command in CLI. This will provide metrics like mAP50-95, mAP50, and more.

For more validation details, visit the Val page.

Ultralytics YOLO26 allows exporting models to various formats such as ONNX, TensorRT, CoreML, and more to ensure compatibility across different platforms and devices.

Check the full list of supported formats and instructions on the Export page.

Ultralytics YOLO26 is designed to offer state-of-the-art performance for object detection, segmentation, and pose estimation. Here are some key advantages:

Explore our Blog for use cases and success stories showcasing YOLO26 in action.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.yaml")  # build a new model from YAML
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo detect train data=coco8.yaml model=yolo26n.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo detect train data=coco8.yaml model=yolo26n.yaml pretrained=yolo26n.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
```

Example 4 (unknown):
```unknown
yolo detect val model=yolo26n.pt      # val official model
yolo detect val model=path/to/best.pt # val custom model
```

---

## Oriented Bounding Boxes Object Detection

**URL:** https://docs.ultralytics.com/tasks/obb/

**Contents:**
- Oriented Bounding Boxes Object Detection
- Visual Samples
- Models
- Train
  - Dataset format
- Val
- Predict
- Export
- Real-World Applications
- FAQ

Oriented object detection goes a step further than standard object detection by introducing an extra angle to locate objects more accurately in an image.

The output of an oriented object detector is a set of rotated bounding boxes that precisely enclose the objects in the image, along with class labels and confidence scores for each box. Oriented bounding boxes are particularly useful when objects appear at various angles, such as in aerial imagery, where traditional axis-aligned bounding boxes may include unnecessary background.

YOLO26 OBB models use the -obb suffix, i.e., yolo26n-obb.pt, and are pretrained on DOTAv1.

Watch: Object Detection using Ultralytics YOLO Oriented Bounding Boxes (YOLO-OBB)

YOLO26 pretrained OBB models are shown here, which are pretrained on the DOTAv1 dataset.

Models download automatically from the latest Ultralytics release on first use.

Train YOLO26n-obb on the DOTA8 dataset for 100 epochs at image size 640. For a full list of available arguments see the Configuration page.

OBB angles are constrained to the range 0–90 degrees (exclusive of 90). Angles of 90 degrees or greater are not supported.

Watch: How to Train Ultralytics YOLO-OBB (Oriented Bounding Boxes) Models on DOTA Dataset using Ultralytics Platform

OBB dataset format can be found in detail in the Dataset Guide. The YOLO OBB format designates bounding boxes by their four corner points with coordinates normalized between 0 and 1, following this structure:

Internally, YOLO processes losses and outputs in the xywhr format, which represents the bounding box's center point (xy), width, height, and rotation.

Validate trained YOLO26n-obb model accuracy on the DOTA8 dataset. No arguments are needed as the model retains its training data and arguments as model attributes.

Use a trained YOLO26n-obb model to run predictions on images.

Watch: How to Detect and Track Storage Tanks using Ultralytics YOLO-OBB | Oriented Bounding Boxes | DOTA

See full predict mode details in the Predict page.

Export a YOLO26n-obb model to a different format like ONNX, CoreML, etc.

Available YOLO26-obb export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'. You can predict or validate directly on exported models, i.e., yolo predict model=yolo26n-obb.onnx. Usage examples are shown for your model after export completes.

See full export details in the Export page.

OBB detection with YOLO26 has numerous practical applications across various industries:

These applications benefit from OBB's ability to precisely fit objects at any angle, providing more accurate detection than traditional bounding boxes.

Oriented Bounding Boxes (OBB) include an additional angle to enhance object localization accuracy in images. Unlike regular bounding boxes, which are axis-aligned rectangles, OBBs can rotate to fit the orientation of the object better. This is particularly useful for applications requiring precise object placement, such as aerial or satellite imagery (Dataset Guide).

To train a YOLO26n-obb model with a custom dataset, follow the example below using Python or CLI:

For more training arguments, check the Configuration section.

YOLO26-OBB models are pretrained on datasets like DOTAv1 but you can use any dataset formatted for OBB. Detailed information on OBB dataset formats can be found in the Dataset Guide.

Exporting a YOLO26-OBB model to ONNX format is straightforward using either Python or CLI:

For more export formats and details, refer to the Export page.

To validate a YOLO26n-obb model, you can use Python or CLI commands as shown below:

See full validation details in the Val section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-obb.yaml")  # build a new model from YAML
model = YOLO("yolo26n-obb.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-obb.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="dota8.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo obb train data=dota8.yaml model=yolo26n-obb.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo obb train data=dota8.yaml model=yolo26n-obb.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo obb train data=dota8.yaml model=yolo26n-obb.yaml pretrained=yolo26n-obb.pt epochs=100 imgsz=640
```

Example 3 (unknown):
```unknown
class_index x1 y1 x2 y2 x3 y3 x4 y4
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-obb.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val(data="dota8.yaml")  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95(B)
metrics.box.map50  # map50(B)
metrics.box.map75  # map75(B)
metrics.box.maps  # a list containing mAP50-95(B) for each category
```

---
