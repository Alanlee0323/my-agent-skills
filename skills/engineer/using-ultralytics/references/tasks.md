# Raw-Ultralytics - Tasks

**Pages:** 4

---

## Computer Vision Tasks Supported by Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/tasks/

**Contents:**
- Computer Vision Tasks Supported by Ultralytics YOLO26
- Detection
- Image segmentation
- Classification
- Pose estimation
- OBB
- Conclusion
- FAQ
  - What computer vision tasks can Ultralytics YOLO26 perform?
  - How do I use Ultralytics YOLO26 for object detection?

Ultralytics YOLO26 is a versatile AI framework that supports multiple computer visiontasks. The framework can be used to perform detection, segmentation, OBB, classification, and pose estimation. Each of these tasks has a different objective and use case, allowing you to address various computer vision challenges with a single framework.

Watch: Explore Ultralytics YOLO Tasks: Object Detection, Segmentation, OBB, Tracking, and Pose Estimation.

Detection is the primary task supported by YOLO26. It involves identifying objects in an image or video frame and drawing bounding boxes around them. The detected objects are classified into different categories based on their features. YOLO26 can detect multiple objects in a single image or video frame with high accuracy and speed, making it ideal for real-time applications like surveillance systems and autonomous vehicles.

Segmentation takes object detection further by producing pixel-level masks for each object. This precision is useful for applications such as medical imaging, agricultural analysis, and manufacturing quality control.

Segmentation Examples

Classification involves categorizing entire images based on their content. This task is essential for applications like product categorization in e-commerce, content moderation, and wildlife monitoring.

Classification Examples

Pose estimation detects specific keypoints in images or video frames to track movements or estimate poses. These keypoints can represent human joints, facial features, or other significant points of interest. YOLO26 excels at keypoint detection with high accuracy and speed, making it valuable for fitness applications, sports analytics, and human-computer interaction.

Oriented Bounding Box (OBB) detection enhances traditional object detection by adding an orientation angle to better locate rotated objects. This capability is particularly valuable for aerial imagery analysis, document processing, and industrial applications where objects appear at various angles. YOLO26 delivers high accuracy and speed for detecting rotated objects in diverse scenarios.

Ultralytics YOLO26 supports multiple computer vision tasks, including detection, segmentation, classification, oriented object detection, and keypoint detection. Each task addresses specific needs in the computer vision landscape, from basic object identification to detailed pose analysis. By understanding the capabilities and applications of each task, you can select the most appropriate approach for your specific computer vision challenges and leverage YOLO26's powerful features to build effective solutions.

Ultralytics YOLO26 is a versatile AI framework capable of performing various computer vision tasks with high accuracy and speed. These tasks include:

To use Ultralytics YOLO26 for object detection, follow these steps:

For more detailed instructions, check out our detection examples.

Using YOLO26 for segmentation tasks provides several advantages:

Learn more about the benefits and use cases of YOLO26 for segmentation in the image segmentation section.

Yes, Ultralytics YOLO26 can effectively perform pose estimation and keypoint detection with high accuracy and speed. This feature is particularly useful for tracking movements in sports analytics, healthcare, and human-computer interaction applications. YOLO26 detects keypoints in an image or video frame, allowing for precise pose estimation.

For more details and implementation tips, visit our pose estimation examples.

Oriented Object Detection (OBB) with YOLO26 provides enhanced precision by detecting objects with an additional angle parameter. This feature is beneficial for applications requiring accurate localization of rotated objects, such as aerial imagery analysis and warehouse automation.

Check out the Oriented Object Detection section for more details and examples.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (adjust model type as needed)
model = YOLO("yolo26n.pt")  # n, s, m, l, x versions available

# Perform object detection on an image
results = model.predict(source="image.jpg")  # Can also use video, directory, URL, etc.

# Display the results
results[0].show()  # Show the first image results
```

Example 2 (sql):
```sql
# Run YOLO detection from the command line
yolo detect model=yolo26n.pt source="image.jpg" # Adjust model and source as needed
```

---

## Image Classification

**URL:** https://docs.ultralytics.com/tasks/classify/

**Contents:**
- Image Classification
- Models
- Train
  - Dataset format
- Val
- Predict
- Export
- FAQ
  - What is the purpose of YOLO26 in image classification?
  - How do I train a YOLO26 model for image classification?

Image classification is the simplest of the three tasks and involves classifying an entire image into one of a set of predefined classes.

The output of an image classifier is a single class label and a confidence score. Image classification is useful when you need to know only what class an image belongs to and don't need to know where objects of that class are located or what their exact shape is.

Watch: Explore Ultralytics YOLO Tasks: Image Classification using Ultralytics Platform

YOLO26 Classify models use the -cls suffix, i.e., yolo26n-cls.pt, and are pretrained on ImageNet.

YOLO26 pretrained Classify models are shown here. Detect, Segment, and Pose models are pretrained on the COCO dataset, while Classify models are pretrained on the ImageNet dataset.

Models are downloaded automatically from the latest Ultralytics release on first use.

Train YOLO26n-cls on the MNIST160 dataset for 100 epochs at image size 64. For a full list of available arguments see the Configuration page.

Ultralytics YOLO classification uses torchvision.transforms.RandomResizedCrop for training and torchvision.transforms.CenterCrop for validation and inference. These cropping-based transforms assume square inputs and may inadvertently crop out important regions from images with extreme aspect ratios, potentially causing loss of critical visual information during training. To preserve the full image while maintaining its proportions, consider using torchvision.transforms.Resize instead of cropping transforms.

You can implement this by customizing your augmentation pipeline through a custom ClassificationDataset and ClassificationTrainer.

YOLO classification dataset format can be found in detail in the Dataset Guide.

Validate trained YOLO26n-cls model accuracy on the MNIST160 dataset. No arguments are needed as the model retains its training data and arguments as model attributes.

As mentioned in the training section, you can handle extreme aspect ratios during training by using a custom ClassificationTrainer. You need to apply the same approach for consistent validation results by implementing a custom ClassificationValidator when calling the val() method. Refer to the complete code example in the training section for implementation details.

Use a trained YOLO26n-cls model to run predictions on images.

See full predict mode details in the Predict page.

Export a YOLO26n-cls model to a different format like ONNX, CoreML, etc.

Available YOLO26-cls export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'. You can predict or validate directly on exported models, i.e., yolo predict model=yolo26n-cls.onnx. Usage examples are shown for your model after export completes.

See full export details in the Export page.

YOLO26 models, such as yolo26n-cls.pt, are designed for efficient image classification. They assign a single class label to an entire image along with a confidence score. This is particularly useful for applications where knowing the specific class of an image is sufficient, rather than identifying the location or shape of objects within the image.

To train a YOLO26 model, you can use either Python or CLI commands. For example, to train a yolo26n-cls model on the MNIST160 dataset for 100 epochs at an image size of 64:

For more configuration options, visit the Configuration page.

Pretrained YOLO26 classification models can be found in the Models section. Models like yolo26n-cls.pt, yolo26s-cls.pt, yolo26m-cls.pt, etc., are pretrained on the ImageNet dataset and can be easily downloaded and used for various image classification tasks.

You can export a trained YOLO26 model to various formats using Python or CLI commands. For instance, to export a model to ONNX format:

For detailed export options, refer to the Export page.

To validate a trained model's accuracy on a dataset like MNIST160, you can use the following Python or CLI commands:

For more information, visit the Validate section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.yaml")  # build a new model from YAML
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-cls.yaml").load("yolo26n-cls.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="mnist160", epochs=100, imgsz=64)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo classify train data=mnist160 model=yolo26n-cls.yaml epochs=100 imgsz=64

# Start training from a pretrained *.pt model
yolo classify train data=mnist160 model=yolo26n-cls.pt epochs=100 imgsz=64

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo classify train data=mnist160 model=yolo26n-cls.yaml pretrained=yolo26n-cls.pt epochs=100 imgsz=64
```

Example 3 (python):
```python
import torch
import torchvision.transforms as T

from ultralytics import YOLO
from ultralytics.data.dataset import ClassificationDataset
from ultralytics.models.yolo.classify import ClassificationTrainer, ClassificationValidator


class CustomizedDataset(ClassificationDataset):
    """A customized dataset class for image classification with enhanced data augmentation transforms."""

    def __init__(self, root: str, args, augment: bool = False, prefix: str = ""):
        """Initialize a customized classification dataset with enhanced data augmentation transforms."""
        super().__init__(root, args, augment, prefix)

        # Add your custom training transforms here
        train_transforms = T.Compose(
            [
                T.Resize((args.imgsz, args.imgsz)),
                T.RandomHorizontalFlip(p=args.fliplr),
                T.RandomVerticalFlip(p=args.flipud),
                T.RandAugment(interpolation=T.InterpolationMode.BILINEAR),
                T.ColorJitter(brightness=args.hsv_v, contrast=args.hsv_v, saturation=args.hsv_s, hue=args.hsv_h),
                T.ToTensor(),
                T.Normalize(mean=torch.tensor(0), std=torch.tensor(1)),
                T.RandomErasing(p=args.erasing, inplace=True),
            ]
        )

        # Add your custom validation transforms here
        val_transforms = T.Compose(
            [
                T.Resize((args.imgsz, args.imgsz)),
                T.ToTensor(),
                T.Normalize(mean=torch.tensor(0), std=torch.tensor(1)),
            ]
        )
        self.torch_transforms = train_transforms if augment else val_transforms


class CustomizedTrainer(ClassificationTrainer):
    """A customized trainer class for YOLO classification models with enhanced dataset handling."""

    def build_dataset(self, img_path: str, mode: str = "train", batch=None):
        """Build a customized dataset for classification training and the validation during training."""
        return CustomizedDataset(root=img_path, args=self.args, augment=mode == "train", prefix=mode)


class CustomizedValidator(ClassificationValidator):
    """A customized validator class for YOLO classification models with enhanced dataset handling."""

    def build_dataset(self, img_path: str, mode: str = "train"):
        """Build a customized dataset for classification standalone validation."""
        return CustomizedDataset(root=img_path, args=self.args, augment=mode == "train", prefix=self.args.split)


model = YOLO("yolo26n-cls.pt")
model.train(data="imagenet1000", trainer=CustomizedTrainer, epochs=10, imgsz=224, batch=64)
model.val(data="imagenet1000", validator=CustomizedValidator, imgsz=224, batch=64)
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.top1  # top1 accuracy
metrics.top5  # top5 accuracy
```

---

## Instance Segmentation

**URL:** https://docs.ultralytics.com/tasks/segment/

**Contents:**
- Instance Segmentation
- Models
- Train
  - Dataset format
- Val
- Predict
- Export
- FAQ
  - How do I train a YOLO26 segmentation model on a custom dataset?
  - What is the difference between object detection and instance segmentation in YOLO26?

Instance segmentation goes a step further than object detection and involves identifying individual objects in an image and segmenting them from the rest of the image.

The output of an instance segmentation model is a set of masks or contours that outline each object in the image, along with class labels and confidence scores for each object. Instance segmentation is useful when you need to know not only where objects are in an image, but also what their exact shape is.

Watch: Run Segmentation with Pretrained Ultralytics YOLO Model in Python.

YOLO26 Segment models use the -seg suffix, i.e., yolo26n-seg.pt, and are pretrained on COCO.

YOLO26 pretrained Segment models are shown here. Detect, Segment and Pose models are pretrained on the COCO dataset, while Classify models are pretrained on the ImageNet dataset.

Models download automatically from the latest Ultralytics release on first use.

Train YOLO26n-seg on the COCO8-seg dataset for 100 epochs at image size 640. For a full list of available arguments see the Configuration page.

YOLO segmentation dataset format can be found in detail in the Dataset Guide. To convert your existing dataset from other formats (like COCO etc.) to YOLO format, please use JSON2YOLO tool by Ultralytics.

Validate trained YOLO26n-seg model accuracy on the COCO8-seg dataset. No arguments are needed as the model retains its training data and arguments as model attributes.

Use a trained YOLO26n-seg model to run predictions on images.

See full predict mode details in the Predict page.

Export a YOLO26n-seg model to a different format like ONNX, CoreML, etc.

Available YOLO26-seg export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'. You can predict or validate directly on exported models, i.e., yolo predict model=yolo26n-seg.onnx. Usage examples are shown for your model after export completes.

See full export details in the Export page.

To train a YOLO26 segmentation model on a custom dataset, you first need to prepare your dataset in the YOLO segmentation format. You can use tools like JSON2YOLO to convert datasets from other formats. Once your dataset is ready, you can train the model using Python or CLI commands:

Check the Configuration page for more available arguments.

Object detection identifies and localizes objects within an image by drawing bounding boxes around them, whereas instance segmentation not only identifies the bounding boxes but also delineates the exact shape of each object. YOLO26 instance segmentation models provide masks or contours that outline each detected object, which is particularly useful for tasks where knowing the precise shape of objects is important, such as medical imaging or autonomous driving.

Ultralytics YOLO26 is a state-of-the-art model recognized for its high accuracy and real-time performance, making it ideal for instance segmentation tasks. YOLO26 Segment models come pretrained on the COCO dataset, ensuring robust performance across a variety of objects. Additionally, YOLO supports training, validation, prediction, and export functionalities with seamless integration, making it highly versatile for both research and industry applications.

Loading and validating a pretrained YOLO segmentation model is straightforward. Here's how you can do it using both Python and CLI:

These steps will provide you with validation metrics like Mean Average Precision (mAP), crucial for assessing model performance.

Exporting a YOLO segmentation model to ONNX format is simple and can be done using Python or CLI commands:

For more details on exporting to various formats, refer to the Export page.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.yaml")  # build a new model from YAML
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-seg.yaml").load("yolo26n.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.yaml pretrained=yolo26n-seg.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95(B)
metrics.box.map50  # map50(B)
metrics.box.map75  # map75(B)
metrics.box.maps  # a list containing mAP50-95(B) for each category
metrics.seg.map  # map50-95(M)
metrics.seg.map50  # map50(M)
metrics.seg.map75  # map75(M)
metrics.seg.maps  # a list containing mAP50-95(M) for each category
```

Example 4 (unknown):
```unknown
yolo segment val model=yolo26n-seg.pt  # val official model
yolo segment val model=path/to/best.pt # val custom model
```

---

## Pose Estimation

**URL:** https://docs.ultralytics.com/tasks/pose/

**Contents:**
- Pose Estimation
- Models
- Train
  - Dataset format
- Val
- Predict
- Export
- FAQ
  - What is Pose Estimation with Ultralytics YOLO26 and how does it work?
  - How can I train a YOLO26-pose model on a custom dataset?

Pose estimation is a task that involves identifying the location of specific points in an image, usually referred to as keypoints. The keypoints can represent various parts of the object such as joints, landmarks, or other distinctive features. The locations of the keypoints are usually represented as a set of 2D [x, y] or 3D [x, y, visible] coordinates.

The output of a pose estimation model is a set of points that represent the keypoints on an object in the image, usually along with the confidence scores for each point. Pose estimation is a good choice when you need to identify specific parts of an object in a scene, and their location in relation to each other.

Watch: Ultralytics YOLO26 Pose Estimation Tutorial | Real-Time Object Tracking and Human Pose Detection

YOLO26 pose models use the -pose suffix, i.e., yolo26n-pose.pt. These models are trained on the COCO keypoints dataset and are suitable for a variety of pose estimation tasks.

In the default YOLO26 pose model, there are 17 keypoints, each representing a different part of the human body. Here is the mapping of each index to its respective body joint:

Ultralytics YOLO26 pretrained Pose models are shown here. Detect, Segment and Pose models are pretrained on the COCO dataset, while Classify models are pretrained on the ImageNet dataset.

Models download automatically from the latest Ultralytics release on first use.

Train a YOLO26-pose model on the COCO8-pose dataset. The COCO8-pose dataset is a small sample dataset that's perfect for testing and debugging your pose estimation models.

YOLO pose dataset format can be found in detail in the Dataset Guide. To convert your existing dataset from other formats (like COCO etc.) to YOLO format, please use the JSON2YOLO tool by Ultralytics.

For custom pose estimation tasks, you can also explore specialized datasets like Tiger-Pose for animal pose estimation, Hand Keypoints for hand tracking, or Dog-Pose for canine pose analysis.

Validate trained YOLO26n-pose model accuracy on the COCO8-pose dataset. No arguments are needed as the model retains its training data and arguments as model attributes.

Use a trained YOLO26n-pose model to run predictions on images. The predict mode allows you to perform inference on images, videos, or real-time streams.

See full predict mode details in the Predict page.

Export a YOLO26n Pose model to a different format like ONNX, CoreML, etc. This allows you to deploy your model on various platforms and devices for real-time inference.

Available YOLO26-pose export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'. You can predict or validate directly on exported models, i.e., yolo predict model=yolo26n-pose.onnx. Usage examples are shown for your model after export completes.

See full export details in the Export page.

Pose estimation with Ultralytics YOLO26 involves identifying specific points, known as keypoints, in an image. These keypoints typically represent joints or other important features of the object. The output includes the [x, y] coordinates and confidence scores for each point. YOLO26-pose models are specifically designed for this task and use the -pose suffix, such as yolo26n-pose.pt. These models are pretrained on datasets like COCO keypoints and can be used for various pose estimation tasks. For more information, visit the Pose Estimation Page.

Training a YOLO26-pose model on a custom dataset involves loading a model, either a new model defined by a YAML file or a pretrained model. You can then start the training process using your specified dataset and parameters.

For comprehensive details on training, refer to the Train Section. You can also use Ultralytics Platform for a no-code approach to training custom pose estimation models.

Validation of a YOLO26-pose model involves assessing its accuracy using the same dataset parameters retained during training. Here's an example:

For more information, visit the Val Section.

Yes, you can export a YOLO26-pose model to various formats like ONNX, CoreML, TensorRT, and more. This can be done using either Python or the Command Line Interface (CLI).

Refer to the Export Section for more details. Exported models can be deployed on edge devices for real-time applications like fitness tracking, sports analysis, or robotics.

Ultralytics YOLO26 offers various pretrained pose models such as YOLO26n-pose, YOLO26s-pose, YOLO26m-pose, among others. These models differ in size, accuracy (mAP), and speed. For instance, the YOLO26n-pose model achieves a mAPpose50-95 of 50.0 and an mAPpose50 of 81.0. For a complete list and performance details, visit the Models Section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.yaml")  # build a new model from YAML
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolo26n-pose.yaml").load("yolo26n-pose.pt")  # build from YAML and transfer weights

# Train the model
results = model.train(data="coco8-pose.yaml", epochs=100, imgsz=640)
```

Example 2 (sql):
```sql
# Build a new model from YAML and start training from scratch
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.yaml epochs=100 imgsz=640

# Start training from a pretrained *.pt model
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.pt epochs=100 imgsz=640

# Build a new model from YAML, transfer pretrained weights to it and start training
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.yaml pretrained=yolo26n-pose.pt epochs=100 imgsz=640
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom model

# Validate the model
metrics = model.val()  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list containing mAP50-95 for each category
metrics.pose.map  # map50-95(P)
metrics.pose.map50  # map50(P)
metrics.pose.map75  # map75(P)
metrics.pose.maps  # a list containing mAP50-95(P) for each category
```

Example 4 (unknown):
```unknown
yolo pose val model=yolo26n-pose.pt # val official model
yolo pose val model=path/to/best.pt # val custom model
```

---
