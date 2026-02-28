# Raw-Ultralytics - Other

**Pages:** 13

---

## Cloud Training

**URL:** https://docs.ultralytics.com/platform/train/cloud-training/

**Contents:**
- Cloud Training
- Train from UI
  - Step 1: Select Dataset
  - Step 2: Configure Model
  - Step 3: Select GPU
  - Step 4: Start Training
- Monitor Training
  - Live Metrics
  - Checkpoints
- Stop and Resume

Ultralytics Platform Cloud Training offers single-click training on cloud GPUs, making model training accessible without complex setup. Train YOLO models with real-time metrics streaming and automatic checkpoint saving.

Watch: Cloud Training with Ultralytics Platform

Start cloud training directly from the Platform:

Choose a dataset from your uploads:

Select base model and parameters:

Choose your compute resources:

Click Start Training to launch your job. The Platform:

New accounts receive $5 in signup credits ($25 for company emails) - enough for several training runs. Check your balance in Settings > Billing.

View real-time training progress:

Checkpoints are saved automatically:

Click Stop Training to pause your job:

Continue from your last checkpoint:

You can only resume training that was explicitly stopped. Failed training jobs may need to restart from scratch.

Train on your own hardware while streaming metrics to the Platform.

Package Version Requirement

Platform integration requires ultralytics>=8.4.0. Lower versions will NOT work with Platform.

Use the project and name parameters to stream metrics:

Train with datasets stored on the Platform:

The ul:// URI format automatically downloads and configures your dataset.

Training costs are based on GPU usage:

A minimum balance of $5.00 is required to start epoch-based training.

After training, view detailed costs in the Billing tab:

Training time depends on:

Typical times (1000 images, 100 epochs):

Yes, training continues until completion. You'll receive a notification when training finishes. Make sure your account has sufficient balance for epoch-based training.

Training pauses at the end of the current epoch. Your checkpoint is saved, and you can resume after adding credits.

Yes, advanced users can specify additional arguments in the training configuration.

Task-Specific Parameters

Some parameters only apply to specific tasks:

**Examples:**

Example 1 (unknown):
```unknown
pip install "ultralytics>=8.4.0"
```

Example 2 (unknown):
```unknown
export ULTRALYTICS_API_KEY="your_api_key"
```

Example 3 (unknown):
```unknown
yolo train model=yolo26n.pt data=coco.yaml epochs=100 \
  project=username/my-project name=experiment-1
```

Example 4 (python):
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
model.train(
    data="coco.yaml",
    epochs=100,
    project="username/my-project",
    name="experiment-1",
)
```

---

## Command Line Interface

**URL:** https://docs.ultralytics.com/usage/cli/

**Contents:**
- Command Line Interface
- Train
- Val
- Predict
- Export
- Overriding Default Arguments
- Overriding Default Config File
- Solutions Commands
- FAQ
  - How do I use the Ultralytics YOLO command line interface (CLI) for model training?

The Ultralytics command line interface (CLI) provides a straightforward way to use Ultralytics YOLO models without needing a Python environment. The CLI supports running various tasks directly from the terminal using the yolo command, requiring no customization or Python code.

Watch: Mastering Ultralytics YOLO: CLI

Ultralytics yolo commands use the following syntax:

Where: - TASK (optional) is one of [detect, segment, classify, pose, obb] - MODE (required) is one of [train, val, predict, export, track, benchmark] - ARGS (optional) are any number of custom arg=value pairs like imgsz=320 that override defaults.

See all ARGS in the full Configuration Guide or with yolo cfg.

Train a detection model for 10 epochs with an initial learning rate of 0.01:

Predict using a pretrained segmentation model on a YouTube video at image size 320:

Validate a pretrained detection model with a batch size of 1 and image size 640:

Export a YOLO classification model to ONNX format with image size 224x128 (no TASK required):

Run special commands to view version, settings, run checks, and more:

Arguments must be passed as arg=val pairs, separated by an equals = sign and delimited by spaces between pairs. Do not use -- argument prefixes or commas , between arguments.

Train YOLO on the COCO8 dataset for 100 epochs at image size 640. For a full list of available arguments, see the Configuration page.

Start training YOLO26n on COCO8 for 100 epochs at image size 640:

Resume an interrupted training session:

Validate the accuracy of the trained model on the COCO8 dataset. No arguments are needed as the model retains its training data and arguments as model attributes.

Validate an official YOLO26n model:

Validate a custom-trained model:

Use a trained model to run predictions on images.

Predict with an official YOLO26n model:

Predict with a custom model:

Export a model to a different format like ONNX or CoreML.

Export an official YOLO26n model to ONNX format:

Export a custom-trained model to ONNX format:

Available Ultralytics export formats are in the table below. You can export to any format using the format argument, i.e., format='onnx' or format='engine'.

See full export details on the Export page.

Override default arguments by passing them in the CLI as arg=value pairs.

Train a detection model for 10 epochs with a learning rate of 0.01:

Predict using a pretrained segmentation model on a YouTube video at image size 320:

Validate a pretrained detection model with a batch size of 1 and image size 640:

Override the default.yaml configuration file entirely by passing a new file with the cfg argument, such as cfg=custom.yaml.

To do this, first create a copy of default.yaml in your current working directory with the yolo copy-cfg command, which creates a default_copy.yaml file.

You can then pass this file as cfg=default_copy.yaml along with any additional arguments, like imgsz=320 in this example:

Ultralytics provides ready-to-use solutions for common computer vision applications through the CLI. These solutions simplify the implementation of complex tasks like object counting, workout monitoring, and queue management.

Count objects in a video or live stream:

Monitor workout exercises using a pose model:

Count objects in a designated queue or region:

Perform object detection, instance segmentation, or pose estimation in a web browser using Streamlit:

View available solutions and their options:

For more information on Ultralytics solutions, visit the Solutions page.

To train a model using the CLI, execute a single-line command in the terminal. For example, to train a detection model for 10 epochs with a learning rate of 0.01, run:

This command uses the train mode with specific arguments. For a full list of available arguments, refer to the Configuration Guide.

The Ultralytics YOLO CLI supports various tasks, including detection, segmentation, classification, pose estimation, and oriented bounding box detection. You can also perform operations like:

Customize each task with various arguments. For detailed syntax and examples, see the respective sections like Train, Predict, and Export.

To validate a model's accuracy, use the val mode. For example, to validate a pretrained detection model with a batch size of 1 and an image size of 640, run:

This command evaluates the model on the specified dataset and provides performance metrics like mAP, precision, and recall. For more details, refer to the Val section.

You can export YOLO models to various formats including ONNX, TensorRT, CoreML, TensorFlow, and more. For instance, to export a model to ONNX format, run:

The export command supports numerous options to optimize your model for specific deployment environments. For complete details on all available export formats and their specific parameters, visit the Export page.

Ultralytics provides ready-to-use solutions through the solutions command. For example, to count objects in a video:

These solutions require minimal configuration and provide immediate functionality for common computer vision tasks. To see all available solutions, run yolo solutions help. Each solution has specific parameters that can be customized to fit your needs.

**Examples:**

Example 1 (unknown):
```unknown
yolo TASK MODE ARGS
```

Example 2 (unknown):
```unknown
yolo train data=coco8.yaml model=yolo26n.pt epochs=10 lr0=0.01
```

Example 3 (unknown):
```unknown
yolo predict model=yolo26n-seg.pt source='https://youtu.be/LNwODJXcvt4' imgsz=320
```

Example 4 (unknown):
```unknown
yolo val model=yolo26n.pt data=coco8.yaml batch=1 imgsz=640
```

---

## Configuration

**URL:** https://docs.ultralytics.com/usage/cfg/

**Contents:**
- Configuration
- Tasks
- Modes
- Train Settings
- Predict Settings
- Validation Settings
- Export Settings
- Solutions Settings
- Augmentation Settings
- Logging, Checkpoints and Plotting Settings

YOLO settings and hyperparameters play a critical role in the model's performance, speed, and accuracy. These settings can affect the model's behavior at various stages, including training, validation, and prediction.

Watch: Mastering Ultralytics YOLO: Configuration

Watch: Mastering Ultralytics YOLO: Configuration

Ultralytics commands use the following syntax:

Default ARG values are defined on this page and come from the cfg/default.yaml file.

Ultralytics YOLO models can perform a variety of computer vision tasks, including:

Ultralytics YOLO models operate in different modes, each designed for a specific stage of the model lifecycle:

Training settings for YOLO models include hyperparameters and configurations that affect the model's performance, speed, and accuracy. Key settings include batch size, learning rate, momentum, and weight decay. The choice of optimizer, loss function, and dataset composition also impact training. Tuning and experimentation are crucial for optimal performance. For more details, see the Ultralytics entrypoint function.

Note on Batch-size Settings

The batch argument offers three configuration options:

Prediction settings for YOLO models include hyperparameters and configurations that influence performance, speed, and accuracy during inference. Key settings include the confidence threshold, Non-Maximum Suppression (NMS) threshold, and the number of classes. Input data size, format, and supplementary features like masks also affect predictions. Tuning these settings is essential for optimal performance.

Visualization arguments:

Validation settings for YOLO models involve hyperparameters and configurations to evaluate performance on a validation dataset. These settings influence performance, speed, and accuracy. Common settings include batch size, validation frequency, and performance metrics. The validation dataset's size and composition, along with the specific task, also affect the process.

Careful tuning and experimentation are crucial to ensure optimal performance and to detect and prevent overfitting.

Export settings for YOLO models include configurations for saving or exporting the model for use in different environments. These settings impact performance, size, and compatibility. Key settings include the exported file format (e.g., ONNX, TensorFlow SavedModel), the target device (e.g., CPU, GPU), and features like masks. The model's task and the destination environment's constraints also affect the export process.

Thoughtful configuration ensures the exported model is optimized for its use case and functions effectively in the target environment.

Ultralytics Solutions configuration settings offer flexibility to customize models for tasks like object counting, heatmap creation, workout tracking, data analysis, zone tracking, queue management, and region-based counting. These options allow easy adjustments for accurate and useful results tailored to specific needs.

Data augmentation techniques are essential for improving YOLO model robustness and performance by introducing variability into the training data, helping the model generalize better to unseen data. The following table outlines each augmentation argument's purpose and effect:

Adjust these settings to meet dataset and task requirements. Experimenting with different values can help find the optimal augmentation strategy for the best model performance.

Logging, checkpoints, plotting, and file management are important when training a YOLO model:

Effective management of these aspects helps track progress and makes debugging and optimization easier.

Improve performance by tuning hyperparameters like batch size, learning rate, momentum, and weight decay. Adjust data augmentation settings, select the right optimizer, and use techniques like early stopping or mixed precision. For details, see the Train Guide.

Key hyperparameters affecting accuracy include:

Adjust these based on your dataset and hardware. Learn more in Train Settings.

The learning rate (lr0) is crucial; start with 0.01 for SGD or 0.001 for Adam optimizer. Monitor metrics and adjust as needed. Use cosine learning rate schedulers (cos_lr) or warmup (warmup_epochs, warmup_momentum). Details are in the Train Guide.

Default settings include:

For a full overview, see Predict Settings and the Predict Guide.

Mixed precision training (amp=True) reduces memory usage and speeds up training using FP16 and FP32. It's beneficial for modern GPUs, allowing larger models and faster computations without significant accuracy loss. Learn more in the Train Guide.

**Examples:**

Example 1 (unknown):
```unknown
yolo TASK MODE ARGS
```

Example 2 (json):
```json
from ultralytics import YOLO

# Load a YOLO model from a pretrained weights file
model = YOLO("yolo26n.pt")

# Run the model in MODE using custom ARGS
MODE = "predict"
ARGS = {"source": "image.jpg", "imgsz": 640}
getattr(model, MODE)(**ARGS)
```

---

## Contributing to Ultralytics Open-Source Projects

**URL:** https://docs.ultralytics.com/help/contributing/

**Contents:**
- Contributing to Ultralytics Open-Source Projects
- 🤝 Code of Conduct
- 🚀 Contributing via Pull Requests
  - 📝 CLA Signing
  - ✍️ Google-Style Docstrings
  - ✅ GitHub Actions CI Tests
- ✨ Best Practices for Code Contributions
- 👀 Reviewing Pull Requests
- 🐞 Reporting Bugs
- 📜 License

Welcome! We're thrilled that you're considering contributing to our Ultralyticsopen-source projects. Your involvement not only helps enhance the quality of our repositories but also benefits the entire computer vision community. This guide provides clear guidelines and best practices to help you get started.

Watch: How to Contribute to Ultralytics Repository | Ultralytics Models, Datasets and Documentation 🚀

To ensure a welcoming and inclusive environment for everyone, all contributors must adhere to our Code of Conduct. Respect, kindness, and professionalism are at the heart of our community.

We greatly appreciate contributions in the form of pull requests (PRs). To make the review process as smooth as possible, please follow these steps:

Before we can merge your pull request, you must sign our Contributor License Agreement (CLA). This legal agreement ensures that your contributions are properly licensed, allowing the project to continue being distributed under the AGPL-3.0 license.

After submitting your pull request, the CLA bot will guide you through the signing process. To sign the CLA, simply add a comment in your PR stating:

When adding new functions or classes, include Google-style docstrings for clear, standardized documentation. Always enclose both input and output types in parentheses (e.g., (bool), (np.ndarray)).

This example illustrates the standard Google-style docstring format. Note how it clearly separates the function description, arguments, return value, and examples for maximum readability.

This example demonstrates how to document named return variables. Using named returns can make your code more self-documenting and easier to understand, especially for complex functions.

This example shows how to document functions that return multiple values. Each return value should be documented separately with its own type and description for clarity.

Note: Even though Python returns multiple values as a tuple (e.g., return masks, scores), always document each value separately for clarity and better tool integration. When documenting functions that return multiple values:

✅ Good - Document each return value separately:

❌ Bad - Don't document as a tuple with nested elements:

This example combines Google-style docstrings with Python type hints. When using type hints, you can omit the type information in the docstring arguments section, as it's already specified in the function signature.

For smaller or simpler functions, a single-line docstring may be sufficient. These should be concise but complete sentences that start with a capital letter and end with a period.

All pull requests must pass the GitHub ActionsContinuous Integration (CI) tests before they can be merged. These tests include linting, unit tests, and other checks to ensure that your changes meet the project's quality standards. Review the CI output and address any issues that arise.

When contributing code to Ultralytics projects, keep these best practices in mind:

Reviewing pull requests is another valuable way to contribute. When reviewing PRs:

We highly value bug reports as they help us improve the quality and reliability of our projects. When reporting a bug via GitHub Issues:

Ultralytics uses the GNU Affero General Public License v3.0 (AGPL-3.0) for its repositories. This license promotes openness, transparency, and collaborative improvement in software development. It ensures that all users have the freedom to use, modify, and share the software, fostering a strong community of collaboration and innovation.

We encourage all contributors to familiarize themselves with the terms of the AGPL-3.0 license to contribute effectively and ethically to the Ultralytics open-source community.

Using Ultralytics YOLO models or code in your project? The AGPL-3.0 license requires that your entire derivative work also be open-sourced under AGPL-3.0. This ensures modifications and larger projects built upon open-source foundations remain open.

If you prefer not to open-source your project, consider obtaining an Enterprise License.

Complying means making the complete corresponding source code of your project publicly available under the AGPL-3.0 license.

Choose Your Starting Point:

License Your Project:

Publish Your Source Code:

Refer to the Ultralytics Template Repository for a practical example structure:

By following these guidelines, you ensure compliance with AGPL-3.0, supporting the open-source ecosystem that enables powerful tools like Ultralytics YOLO.

Thank you for your interest in contributing to Ultralyticsopen-source YOLO projects. Your participation is essential in shaping the future of our software and building a vibrant community of innovation and collaboration. Whether you're enhancing code, reporting bugs, or suggesting new features, your contributions are invaluable.

We're excited to see your ideas come to life and appreciate your commitment to advancing object detection technology. Together, let's continue to grow and innovate in this exciting open-source journey.

Contributing to Ultralytics YOLO open-source repositories improves the software, making it more robust and feature-rich for the entire community. Contributions can include code enhancements, bug fixes, documentation improvements, and new feature implementations. Additionally, contributing allows you to collaborate with other skilled developers and experts in the field, enhancing your own skills and reputation. For details on how to get started, refer to the Contributing via Pull Requests section.

To sign the Contributor License Agreement (CLA), follow the instructions provided by the CLA bot after submitting your pull request. This process ensures that your contributions are properly licensed under the AGPL-3.0 license, maintaining the legal integrity of the open-source project. Add a comment in your pull request stating:

For more information, see the CLA Signing section.

Google-style docstrings provide clear, concise documentation for functions and classes, improving code readability and maintainability. These docstrings outline the function's purpose, arguments, and return values with specific formatting rules. When contributing to Ultralytics YOLO, following Google-style docstrings ensures that your additions are well-documented and easily understood. For examples and guidelines, visit the Google-Style Docstrings section.

Before your pull request can be merged, it must pass all GitHub Actions Continuous Integration (CI) tests. These tests include linting, unit tests, and other checks to ensure the code meets the project's quality standards. Review the CI output and fix any issues. For detailed information on the CI process and troubleshooting tips, see the GitHub Actions CI Tests section.

To report a bug, provide a clear and concise Minimum Reproducible Example along with your bug report. This helps developers quickly identify and fix the issue. Ensure your example is minimal yet sufficient to replicate the problem. For more detailed steps on reporting bugs, refer to the Reporting Bugs section.

If you use Ultralytics YOLO code or models (licensed under AGPL-3.0) in your project, the AGPL-3.0 license requires that your entire project (the derivative work) must also be licensed under AGPL-3.0 and its complete source code must be made publicly available. This ensures that the open-source nature of the software is preserved throughout its derivatives. If you cannot meet these requirements, you need to obtain an Enterprise License. See the Open-Sourcing Your Project section for details.

**Examples:**

Example 1 (unknown):
```unknown
I have read the CLA Document and I sign the CLA
```

Example 2 (python):
```python
def example_function(arg1, arg2=4):
    """Example function demonstrating Google-style docstrings.

    Args:
        arg1 (int): The first argument.
        arg2 (int): The second argument.

    Returns:
        (bool): True if arguments are equal, False otherwise.

    Examples:
        >>> example_function(4, 4)  # True
        >>> example_function(1, 2)  # False
    """
    return arg1 == arg2
```

Example 3 (python):
```python
def example_function(arg1, arg2=4):
    """Example function demonstrating Google-style docstrings.

    Args:
        arg1 (int): The first argument.
        arg2 (int): The second argument.

    Returns:
        equals (bool): True if arguments are equal, False otherwise.

    Examples:
        >>> example_function(4, 4)  # True
    """
    equals = arg1 == arg2
    return equals
```

Example 4 (python):
```python
def example_function(arg1, arg2=4):
    """Example function demonstrating Google-style docstrings.

    Args:
        arg1 (int): The first argument.
        arg2 (int): The second argument.

    Returns:
        equals (bool): True if arguments are equal, False otherwise.
        added (int): Sum of both input arguments.

    Examples:
        >>> equals, added = example_function(2, 2)  # True, 4
    """
    equals = arg1 == arg2
    added = arg1 + arg2
    return equals, added
```

---

## Help

**URL:** https://docs.ultralytics.com/help/

**Contents:**
- Help
- FAQ
  - What is Ultralytics YOLO and how does it benefit my machine learning projects?
  - How do I contribute to Ultralytics YOLO repositories?
  - Why should I use Ultralytics Platform for my machine learning projects?
  - What is Continuous Integration (CI) in Ultralytics, and how does it ensure high-quality code?
  - How is data privacy handled by Ultralytics?
- Comments

Welcome to the Ultralytics Help page. This page brings together practical guides, policies, and FAQs to support your work with Ultralytics YOLO models and repositories.

We encourage you to review these resources for a smooth and productive experience. If you need additional support, reach out via GitHub Issues or the Ultralytics Community.

Ultralytics YOLO (You Only Look Once) is a state-of-the-art, real-time object detection model. Its latest version, YOLO26, delivers faster, lighter, end-to-end NMS-free inference optimized for edge and low-power devices, making it ideal for a wide range of applications, from real-time video analytics to advanced machine learning research. YOLO's efficiency in detecting objects in images and videos has made it the go-to solution for businesses and researchers looking to integrate robust computer vision capabilities into their projects.

For more details on YOLO26, visit the YOLO26 documentation.

Contributing to Ultralytics YOLO repositories is straightforward. Start by reviewing the Contributing Guide to understand the protocols for submitting pull requests, reporting bugs, and more. You'll also need to sign the Contributor License Agreement (CLA) to ensure your contributions are legally recognized. For effective bug reporting, refer to the Minimum Reproducible Example (MRE) Guide.

Ultralytics Platform offers a seamless, no-code solution for managing your machine learning projects. It enables you to generate, train, and deploy AI models like YOLO26 effortlessly. Unique features include cloud training, real-time tracking, and intuitive dataset management. Ultralytics Platform simplifies the entire workflow, from data processing to model deployment, making it an indispensable tool for both beginners and advanced users.

To get started, visit Ultralytics Platform Quickstart.

Continuous Integration (CI) in Ultralytics involves automated processes that ensure the integrity and quality of the codebase. Our CI setup includes Docker deployment, broken link checks, CodeQL analysis, and PyPI publishing. These processes help maintain stable and secure repositories by automatically running tests and checks on new code submissions.

Learn more in the Continuous Integration (CI) Guide.

Ultralytics takes data privacy seriously. Our Privacy Policy outlines how we collect and use anonymized data to improve the YOLO package while prioritizing user privacy and control. We adhere to strict data protection regulations to ensure your information is secure at all times.

For more information, review our Privacy Policy.

---

## Home

**URL:** https://docs.ultralytics.com/

**Contents:**
- Home
- Where to Start
- YOLO: A Brief History
- YOLO Licenses: How is Ultralytics YOLO licensed?
- The Evolution of Object Detection
- FAQ
  - What is Ultralytics YOLO and how does it improve object detection?
  - How can I get started with YOLO installation and setup?
  - How can I train a custom YOLO model on my dataset?
  - What are the licensing options available for Ultralytics YOLO?

Introducing Ultralytics YOLO26, the latest version of the acclaimed real-time object detection and image segmentation model. YOLO26 is built on deep learning and computer vision advancements, featuring end-to-end NMS-free inference and optimized edge deployment. Its streamlined design makes it suitable for various applications and easily adaptable to different hardware platforms, from edge devices to cloud APIs. For stable production workloads, both YOLO26 and YOLO11 are recommended.

Explore the Ultralytics Docs, a comprehensive resource designed to help you understand and utilize its features and capabilities. Whether you are a seasoned machine learning practitioner or new to the field, this hub aims to maximize YOLO's potential in your projects.

Install ultralytics with pip and get up and running in minutes to train a YOLO model

Predict on new images, videos and streams with YOLO

Train a new YOLO model on your own custom dataset from scratch or load and train on a pretrained model

Explore Computer Vision Tasks

Discover YOLO tasks like detect, segment, classify, pose, OBB and track

Discover Ultralytics' latest YOLO26 models with NMS-free inference and edge optimization

SAM 3: Segment Anything with Concepts 🚀 NEW

Meta's latest SAM 3 with Promptable Concept Segmentation - segment all instances using text or image exemplars

Open Source, AGPL-3.0

Ultralytics offers two YOLO licenses: AGPL-3.0 and Enterprise. Explore YOLO on GitHub.

Watch: How to Train a YOLO11 model on Your Custom Dataset in Google Colab.

YOLO (You Only Look Once), a popular object detection and image segmentation model, was developed by Joseph Redmon and Ali Farhadi at the University of Washington. Launched in 2015, YOLO gained popularity for its high speed and accuracy.

Ultralytics offers two licensing options to accommodate diverse use cases:

Our licensing strategy is designed to ensure that any improvements to our open-source projects are returned to the community. We believe in open source, and our mission is to ensure that our contributions can be used and expanded in ways that benefit everyone.

Object detection has evolved significantly over the years, from traditional computer vision techniques to advanced deep learning models. The YOLO family of models has been at the forefront of this evolution, consistently pushing the boundaries of what's possible in real-time object detection.

YOLO's unique approach treats object detection as a single regression problem, predicting bounding boxes and class probabilities directly from full images in one evaluation. This revolutionary method has made YOLO models significantly faster than previous two-stage detectors while maintaining high accuracy.

With each new version, YOLO has introduced architectural improvements and innovative techniques that have enhanced performance across various metrics. YOLO26 continues this tradition by incorporating the latest advancements in computer vision research, featuring end-to-end NMS-free inference and optimized edge deployment for real-world applications.

Ultralytics YOLO is the acclaimed YOLO (You Only Look Once) series for real-time object detection and image segmentation. The latest model, YOLO26, builds on previous versions by introducing end-to-end NMS-free inference and optimized edge deployment. YOLO supports various vision AI tasks such as detection, segmentation, pose estimation, tracking, and classification. Its efficient architecture ensures excellent speed and accuracy, making it suitable for diverse applications, including edge devices and cloud APIs.

Getting started with YOLO is quick and straightforward. You can install the Ultralytics package using pip and get up and running in minutes. Here's a basic installation command:

Installation using pip

For a comprehensive step-by-step guide, visit our Quickstart page. This resource will help you with installation instructions, initial setup, and running your first model.

Training a custom YOLO model on your dataset involves a few detailed steps:

Here's example code for the Object Detection Task:

Train Example for Object Detection Task

For a detailed walkthrough, check out our Train a Model guide, which includes examples and tips for optimizing your training process.

Ultralytics offers two licensing options for YOLO:

For more details, visit our Licensing page.

Ultralytics YOLO supports efficient and customizable multi-object tracking. To utilize tracking capabilities, you can use the yolo track command, as shown below:

Example for Object Tracking on a Video

For a detailed guide on setting up and running object tracking, check our Track Mode documentation, which explains the configuration and practical applications in real-time scenarios.

**Examples:**

Example 1 (unknown):
```unknown
pip install -U ultralytics
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (you can choose n, s, m, l, or x versions)
model = YOLO("yolo26n.pt")

# Start training on your custom dataset
model.train(data="path/to/dataset.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Train a YOLO model from the command line
yolo detect train data=path/to/dataset.yaml epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Start tracking objects in a video
# You can also use live video streams or webcam input
model.track(source="path/to/video.mp4")
```

---

## Home

**URL:** https://docs.ultralytics.com

**Contents:**
- Home
- Where to Start
- YOLO: A Brief History
- YOLO Licenses: How is Ultralytics YOLO licensed?
- The Evolution of Object Detection
- FAQ
  - What is Ultralytics YOLO and how does it improve object detection?
  - How can I get started with YOLO installation and setup?
  - How can I train a custom YOLO model on my dataset?
  - What are the licensing options available for Ultralytics YOLO?

Introducing Ultralytics YOLO26, the latest version of the acclaimed real-time object detection and image segmentation model. YOLO26 is built on deep learning and computer vision advancements, featuring end-to-end NMS-free inference and optimized edge deployment. Its streamlined design makes it suitable for various applications and easily adaptable to different hardware platforms, from edge devices to cloud APIs. For stable production workloads, both YOLO26 and YOLO11 are recommended.

Explore the Ultralytics Docs, a comprehensive resource designed to help you understand and utilize its features and capabilities. Whether you are a seasoned machine learning practitioner or new to the field, this hub aims to maximize YOLO's potential in your projects.

Install ultralytics with pip and get up and running in minutes to train a YOLO model

Predict on new images, videos and streams with YOLO

Train a new YOLO model on your own custom dataset from scratch or load and train on a pretrained model

Explore Computer Vision Tasks

Discover YOLO tasks like detect, segment, classify, pose, OBB and track

Discover Ultralytics' latest YOLO26 models with NMS-free inference and edge optimization

SAM 3: Segment Anything with Concepts 🚀 NEW

Meta's latest SAM 3 with Promptable Concept Segmentation - segment all instances using text or image exemplars

Open Source, AGPL-3.0

Ultralytics offers two YOLO licenses: AGPL-3.0 and Enterprise. Explore YOLO on GitHub.

Watch: How to Train a YOLO11 model on Your Custom Dataset in Google Colab.

YOLO (You Only Look Once), a popular object detection and image segmentation model, was developed by Joseph Redmon and Ali Farhadi at the University of Washington. Launched in 2015, YOLO gained popularity for its high speed and accuracy.

Ultralytics offers two licensing options to accommodate diverse use cases:

Our licensing strategy is designed to ensure that any improvements to our open-source projects are returned to the community. We believe in open source, and our mission is to ensure that our contributions can be used and expanded in ways that benefit everyone.

Object detection has evolved significantly over the years, from traditional computer vision techniques to advanced deep learning models. The YOLO family of models has been at the forefront of this evolution, consistently pushing the boundaries of what's possible in real-time object detection.

YOLO's unique approach treats object detection as a single regression problem, predicting bounding boxes and class probabilities directly from full images in one evaluation. This revolutionary method has made YOLO models significantly faster than previous two-stage detectors while maintaining high accuracy.

With each new version, YOLO has introduced architectural improvements and innovative techniques that have enhanced performance across various metrics. YOLO26 continues this tradition by incorporating the latest advancements in computer vision research, featuring end-to-end NMS-free inference and optimized edge deployment for real-world applications.

Ultralytics YOLO is the acclaimed YOLO (You Only Look Once) series for real-time object detection and image segmentation. The latest model, YOLO26, builds on previous versions by introducing end-to-end NMS-free inference and optimized edge deployment. YOLO supports various vision AI tasks such as detection, segmentation, pose estimation, tracking, and classification. Its efficient architecture ensures excellent speed and accuracy, making it suitable for diverse applications, including edge devices and cloud APIs.

Getting started with YOLO is quick and straightforward. You can install the Ultralytics package using pip and get up and running in minutes. Here's a basic installation command:

Installation using pip

For a comprehensive step-by-step guide, visit our Quickstart page. This resource will help you with installation instructions, initial setup, and running your first model.

Training a custom YOLO model on your dataset involves a few detailed steps:

Here's example code for the Object Detection Task:

Train Example for Object Detection Task

For a detailed walkthrough, check out our Train a Model guide, which includes examples and tips for optimizing your training process.

Ultralytics offers two licensing options for YOLO:

For more details, visit our Licensing page.

Ultralytics YOLO supports efficient and customizable multi-object tracking. To utilize tracking capabilities, you can use the yolo track command, as shown below:

Example for Object Tracking on a Video

For a detailed guide on setting up and running object tracking, check our Track Mode documentation, which explains the configuration and practical applications in real-time scenarios.

**Examples:**

Example 1 (unknown):
```unknown
pip install -U ultralytics
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model (you can choose n, s, m, l, or x versions)
model = YOLO("yolo26n.pt")

# Start training on your custom dataset
model.train(data="path/to/dataset.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Train a YOLO model from the command line
yolo detect train data=path/to/dataset.yaml epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO model
model = YOLO("yolo26n.pt")

# Start tracking objects in a video
# You can also use live video streams or webcam input
model.track(source="path/to/video.mp4")
```

---

## Intel OpenVINO Export

**URL:** https://docs.ultralytics.com/integrations/openvino/

**Contents:**
- Intel OpenVINO Export
- Usage Examples
- Export Arguments
- Benefits of OpenVINO
- OpenVINO Export Structure
- Using OpenVINO Export in Deployment
  - Inference with Ultralytics
  - Inference with OpenVINO Runtime
- OpenVINO YOLO11 Benchmarks
  - Intel Core CPU

In this guide, we cover exporting YOLO26 models to the OpenVINO format, which can provide up to 3x CPU speedup, as well as accelerating YOLO inference on Intel GPU and NPU hardware.

OpenVINO, short for Open Visual Inference & Neural Network Optimization toolkit, is a comprehensive toolkit for optimizing and deploying AI inference models. Even though the name contains Visual, OpenVINO also supports various additional tasks including language, audio, time series, etc.

Watch: How to Export Ultralytics YOLO26 to Intel OpenVINO Format for Faster Inference 🚀

Export a YOLO26n model to OpenVINO format and run inference with the exported model.

For more details about the export process, visit the Ultralytics documentation page on exporting.

OpenVINO™ is compatible with most Intel® processors but to ensure optimal performance:

Verify OpenVINO™ support Check whether your Intel® chip is officially supported by OpenVINO™ using Intel's compatibility list.

Identify your accelerator Determine if your processor includes an integrated NPU (Neural Processing Unit) or GPU (integrated GPU) by consulting Intel's hardware guide.

Install the latest drivers If your chip supports an NPU or GPU but OpenVINO™ isn't detecting it, you may need to install or update the associated drivers. Follow the driver‑installation instructions to enable full acceleration.

By following these three steps, you can ensure OpenVINO™ runs optimally on your Intel® hardware.

When you export a model to OpenVINO format, it results in a directory containing the following:

You can use these files to run inference with the OpenVINO Inference Engine.

Once your model is successfully exported to the OpenVINO format, you have two primary options for running inference:

Use the ultralytics package, which provides a high-level API and wraps the OpenVINO Runtime.

Use the native openvino package for more advanced or customized control over inference behavior.

The ultralytics package allows you to easily run inference using the exported OpenVINO model via the predict method. You can also specify the target device (e.g., intel:gpu, intel:npu, intel:cpu) using the device argument.

This approach is ideal for fast prototyping or deployment when you don't need full control over the inference pipeline.

The OpenVINO Runtime provides a unified API for inference across all supported Intel hardware. It also provides advanced capabilities like load balancing across Intel hardware and asynchronous execution. For more information on running inference, refer to the YOLO26 notebooks.

Remember, you'll need the XML and BIN files as well as any application-specific settings like input size, scale factor for normalization, etc., to correctly set up and use the model with the Runtime.

In your deployment application, you would typically do the following steps:

For more detailed steps and code snippets, refer to the OpenVINO documentation or API tutorial.

The Ultralytics team benchmarked YOLO11 across various model formats and precision, evaluating speed and accuracy on different Intel devices compatible with OpenVINO.

The benchmarking results below are for reference and might vary based on the exact hardware and software configuration of a system, as well as the current workload of the system at the time the benchmarks are run.

All benchmarks run with openvino Python package version 2025.1.0.

The Intel® Core® series is a range of high-performance processors by Intel. The lineup includes Core i3 (entry-level), Core i5 (mid-range), Core i7 (high-end), and Core i9 (extreme performance). Each series caters to different computing needs and budgets, from everyday tasks to demanding professional workloads. With each new generation, improvements are made to performance, energy efficiency, and features.

Benchmarks below run on 12th Gen Intel® Core® i9-12900KS CPU at FP32 precision.

The Intel® Core™ Ultra™ series represents a new benchmark in high-performance computing, engineered to meet the evolving demands of modern users—from gamers and creators to professionals leveraging AI. This next-generation lineup is more than a traditional CPU series; it combines powerful CPU cores, integrated high-performance GPU capabilities, and a dedicated Neural Processing Unit (NPU) within a single chip, offering a unified solution for diverse and intensive computing workloads.

At the heart of the Intel® Core Ultra™ architecture is a hybrid design that enables exceptional performance across traditional processing tasks, GPU-accelerated workloads, and AI-driven operations. The inclusion of the NPU enhances on-device AI inference, enabling faster, more efficient machine learning and data processing across a wide range of applications.

The Core Ultra™ family includes various models tailored for different performance needs, with options ranging from energy-efficient designs to high-power variants marked by the "H" designation—ideal for laptops and compact form factors that demand serious computing power. Across the lineup, users benefit from the synergy of CPU, GPU, and NPU integration, delivering remarkable efficiency, responsiveness, and multitasking capabilities.

As part of Intel's ongoing innovation, the Core Ultra™ series sets a new standard for future-ready computing. With multiple models available and more on the horizon, this series underscores Intel's commitment to delivering cutting-edge solutions for the next generation of intelligent, AI-enhanced devices.

Benchmarks below run on Intel® Core™ Ultra™ 7 258V and Intel® Core™ Ultra™ 7 265K at FP32 and INT8 precision.

Intel® Arc™ is Intel's line of discrete graphics cards designed for high-performance gaming, content creation, and AI workloads. The Arc series features advanced GPU architectures that support real-time ray tracing, AI-enhanced graphics, and high-resolution gaming. With a focus on performance and efficiency, Intel® Arc™ aims to compete with other leading GPU brands while providing unique features like hardware-accelerated AV1 encoding and support for the latest graphics APIs.

Benchmarks below run on Intel Arc A770 and Intel Arc B580 at FP32 and INT8 precision.

To reproduce the Ultralytics benchmarks above on all export formats run this code:

Note that benchmarking results might vary based on the exact hardware and software configuration of a system, as well as the current workload of the system at the time the benchmarks are run. For the most reliable results use a dataset with a large number of images, i.e. data='coco.yaml' (5000 val images).

The benchmarking results clearly demonstrate the benefits of exporting the YOLO11 model to the OpenVINO format. Across different models and hardware platforms, the OpenVINO format consistently outperforms other formats in terms of inference speed while maintaining comparable accuracy.

The benchmarks underline the effectiveness of OpenVINO as a tool for deploying deep learning models. By converting models to the OpenVINO format, developers can achieve significant performance improvements, making it easier to deploy these models in real-world applications.

For more detailed information and instructions on using OpenVINO, refer to the official OpenVINO documentation.

Exporting YOLO26 models to the OpenVINO format can significantly enhance CPU speed and enable GPU and NPU accelerations on Intel hardware. To export, you can use either Python or CLI as shown below:

For more information, refer to the export formats documentation.

Using Intel's OpenVINO toolkit with YOLO26 models offers several benefits:

For detailed performance comparisons, visit our benchmarks section.

After exporting a YOLO26n model to OpenVINO format, you can run inference using Python or CLI:

Refer to our predict mode documentation for more details.

Ultralytics YOLO26 is optimized for real-time object detection with high accuracy and speed. Specifically, when combined with OpenVINO, YOLO26 provides:

For in-depth performance analysis, check our detailed YOLO11 benchmarks on different hardware.

Yes, you can benchmark YOLO26 models in various formats including PyTorch, TorchScript, ONNX, and OpenVINO. Use the following code snippet to run benchmarks on your chosen dataset:

For detailed benchmark results, refer to our benchmarks section and export formats documentation.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a YOLO26n PyTorch model
model = YOLO("yolo26n.pt")

# Export the model
model.export(format="openvino")  # creates 'yolo26n_openvino_model/'

# Load the exported OpenVINO model
ov_model = YOLO("yolo26n_openvino_model/")

# Run inference
results = ov_model("https://ultralytics.com/images/bus.jpg")

# Run inference with specified device, available devices: ["intel:gpu", "intel:npu", "intel:cpu"]
results = ov_model("https://ultralytics.com/images/bus.jpg", device="intel:gpu")
```

Example 2 (markdown):
```markdown
# Export a YOLO26n PyTorch model to OpenVINO format
yolo export model=yolo26n.pt format=openvino # creates 'yolo26n_openvino_model/'

# Run inference with the exported model
yolo predict model=yolo26n_openvino_model source='https://ultralytics.com/images/bus.jpg'

# Run inference with specified device, available devices: ["intel:gpu", "intel:npu", "intel:cpu"]
yolo predict model=yolo26n_openvino_model source='https://ultralytics.com/images/bus.jpg' device="intel:gpu"
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load the exported OpenVINO model
ov_model = YOLO("yolo26n_openvino_model/")  # the path of your exported OpenVINO model
# Run inference with the exported model
ov_model.predict(device="intel:gpu")  # specify the device you want to run inference on
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a YOLO11n PyTorch model
model = YOLO("yolo11n.pt")

# Benchmark YOLO11n speed and accuracy on the COCO128 dataset for all export formats
results = model.benchmark(data="coco128.yaml")
```

---

## MLflow Integration for Ultralytics YOLO

**URL:** https://docs.ultralytics.com/integrations/mlflow/

**Contents:**
- MLflow Integration for Ultralytics YOLO
- Introduction
- What is MLflow?
- Features
- Setup and Prerequisites
- How to Use
  - Commands
  - Logging
- Examples
- Disabling MLflow

Experiment logging is a crucial aspect of machine learning workflows that enables tracking of various metrics, parameters, and artifacts. It helps to enhance model reproducibility, debug issues, and improve model performance. Ultralytics YOLO, known for its real-time object detection capabilities, now offers integration with MLflow, an open-source platform for complete machine learning lifecycle management.

This documentation page is a comprehensive guide to setting up and utilizing the MLflow logging capabilities for your Ultralytics YOLO project.

MLflow is an open-source platform developed by Databricks for managing the end-to-end machine learning lifecycle. It includes tools for tracking experiments, packaging code into reproducible runs, and sharing and deploying models. MLflow is designed to work with any machine learning library and programming language.

Ensure MLflow is installed. If not, install it using pip:

Make sure that MLflow logging is enabled in Ultralytics settings. Usually, this is controlled by the settings mlflow key. See the settings page for more info.

Update Ultralytics MLflow Settings

Within the Python environment, call the update method on the settings object to change your settings:

If you prefer using the command-line interface, the following commands will allow you to modify your settings:

Set a Project Name: You can set the project name via an environment variable:

Or use the project=<project> argument when training a YOLO model, i.e. yolo train project=my_project.

Set a Run Name: Similar to setting a project name, you can set the run name via an environment variable:

Or use the name=<name> argument when training a YOLO model, i.e. yolo train project=my_project name=my_name.

Start Local MLflow Server: To start tracking, use:

This will start a local server at http://127.0.0.1:5000 by default and save all mlflow logs to the 'runs/mlflow' directory. To specify a different URI, set the MLFLOW_TRACKING_URI environment variable.

Kill MLflow Server Instances: To stop all running MLflow instances, run:

The logging is taken care of by the on_pretrain_routine_end, on_fit_epoch_end, and on_train_end callback functions. These functions are automatically called during the respective stages of the training process, and they handle the logging of parameters, metrics, and artifacts.

Logging Custom Metrics: You can add custom metrics to be logged by modifying the trainer.metrics dictionary before on_fit_epoch_end is called.

View Experiment: To view your logs, navigate to your MLflow server (usually http://127.0.0.1:5000) and select your experiment and run.

View Run: Runs are individual models inside an experiment. Click on a Run and see the Run details, including uploaded artifacts and model weights.

To turn off MLflow logging:

MLflow logging integration with Ultralytics YOLO offers a streamlined way to keep track of your machine learning experiments. It empowers you to monitor performance metrics and manage artifacts effectively, thus aiding in robust model development and deployment. For further details please visit the MLflow official documentation.

To set up MLflow logging with Ultralytics YOLO, you first need to ensure MLflow is installed. You can install it using pip:

Next, enable MLflow logging in Ultralytics settings. This can be controlled using the mlflow key. For more information, see the settings guide.

Update Ultralytics MLflow Settings

Finally, start a local MLflow server for tracking:

Ultralytics YOLO with MLflow supports logging various metrics, parameters, and artifacts throughout the training process:

For more detailed information, visit the Ultralytics YOLO tracking documentation.

Yes, you can disable MLflow logging for Ultralytics YOLO by updating the settings. Here's how you can do it using the CLI:

For further customization and resetting settings, refer to the settings guide.

To start an MLflow server for tracking your experiments in Ultralytics YOLO, use the following command:

This command starts a local server at http://127.0.0.1:5000 by default. If you need to stop running MLflow server instances, use the following bash command:

Refer to the commands section for more command options.

Integrating MLflow with Ultralytics YOLO offers several benefits for managing your machine learning experiments:

For an in-depth look at setting up and leveraging MLflow with Ultralytics YOLO, explore the MLflow Integration for Ultralytics YOLO documentation.

**Examples:**

Example 1 (unknown):
```unknown
pip install mlflow
```

Example 2 (sql):
```sql
from ultralytics import settings

# Update a setting
settings.update({"mlflow": True})

# Reset settings to default values
settings.reset()
```

Example 3 (sql):
```sql
# Update a setting
yolo settings mlflow=True

# Reset settings to default values
yolo settings reset
```

Example 4 (unknown):
```unknown
export MLFLOW_EXPERIMENT_NAME=YOUR_EXPERIMENT_NAME
```

---

## Python Usage

**URL:** https://docs.ultralytics.com/usage/python/

**Contents:**
- Python Usage
- Train
- Val
- Predict
- Export
- Track
- Benchmark
- Using Trainers
- FAQ
  - How can I integrate YOLO into my Python project for object detection?

Welcome to the Ultralytics YOLO Python Usage documentation! This guide is designed to help you seamlessly integrate Ultralytics YOLO into your Python projects for object detection, segmentation, and classification. Here, you'll learn how to load and use pretrained models, train new models, and perform predictions on images. The easy-to-use Python interface is a valuable resource for anyone looking to incorporate YOLO into their Python projects, allowing you to quickly implement advanced object detection capabilities. Let's get started!

Watch: Mastering Ultralytics YOLO: Python

For example, users can load a model, train it, evaluate its performance on a validation set, and even export it to ONNX format with just a few lines of code.

Train mode is used for training a YOLO model on a custom dataset. In this mode, the model is trained using the specified dataset and hyperparameters. The training process involves optimizing the model's parameters so that it can accurately predict the classes and locations of objects in an image.

Val mode is used for validating a YOLO model after it has been trained. In this mode, the model is evaluated on a validation set to measure its accuracy and generalization performance. This mode can be used to tune the hyperparameters of the model to improve its performance.

Predict mode is used for making predictions using a trained YOLO model on new images or videos. In this mode, the model is loaded from a checkpoint file, and the user can provide images or videos to perform inference. The model predicts the classes and locations of objects in the input images or videos.

Export mode is used for exporting a YOLO model to a format that can be used for deployment. In this mode, the model is converted to a format that can be used by other software applications or hardware devices. This mode is useful when deploying the model to production environments.

Export an official YOLO model to ONNX with dynamic batch-size and image-size.

Export an official YOLO model to TensorRT on device=0 for acceleration on CUDA devices.

Track mode is used for tracking objects in real-time using a YOLO model. In this mode, the model is loaded from a checkpoint file, and the user can provide a live video stream to perform real-time object tracking. This mode is useful for applications such as surveillance systems or self-driving cars.

Benchmark mode is used to profile the speed and accuracy of various export formats for YOLO. The benchmarks provide information on the size of the exported format, its mAP50-95 metrics (for object detection and segmentation) or accuracy_top5 metrics (for classification), and the inference time in milliseconds per image across various export formats like ONNX, OpenVINO, TensorRT and others. This information can help users choose the optimal export format for their specific use case based on their requirements for speed and accuracy.

Benchmark an official YOLO model across all export formats.

The YOLO model class serves as a high-level wrapper for the Trainer classes. Each YOLO task has its own trainer, which inherits from BaseTrainer. This architecture allows for greater flexibility and customization in your machine learning workflows.

Detection Trainer Example

You can easily customize Trainers to support custom tasks or explore research and development ideas. The modular design of Ultralytics YOLO allows you to adapt the framework to your specific needs, whether you're working on a novel computer vision task or fine-tuning existing models for better performance.

Customization tutorials

Integrating Ultralytics YOLO into your Python projects is simple. You can load a pretrained model or train a new model from scratch. Here's how to get started:

See more detailed examples in our Predict Mode section.

Ultralytics YOLO provides various modes to cater to different machine learning workflows. These include:

Each mode is designed to provide comprehensive functionalities for different stages of model development and deployment.

To train a custom YOLO model, you need to specify your dataset and other hyperparameters. Here's a quick example:

For more details on training and hyperlinks to example usage, visit our Train Mode page.

Exporting YOLO models in a format suitable for deployment is straightforward with the export function. For example, you can export a model to ONNX format:

For various export options, refer to the Export Mode documentation.

Yes, validating YOLO models on different datasets is possible. After training, you can use the validation mode to evaluate the performance:

Check the Val Mode page for detailed examples and usage.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Create a new YOLO model from scratch
model = YOLO("yolo26n.yaml")

# Load a pretrained YOLO model (recommended for training)
model = YOLO("yolo26n.pt")

# Train the model using the 'coco8.yaml' dataset for 3 epochs
results = model.train(data="coco8.yaml", epochs=3)

# Evaluate the model's performance on the validation set
results = model.val()

# Perform object detection on an image using the model
results = model("https://ultralytics.com/images/bus.jpg")

# Export the model to ONNX format
success = model.export(format="onnx")
```

Example 2 (typescript):
```typescript
from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # pass any model type
results = model.train(epochs=5)
```

Example 3 (python):
```python
from ultralytics import YOLO

model = YOLO("yolo26n.yaml")
results = model.train(data="coco8.yaml", epochs=5)
```

Example 4 (unknown):
```unknown
model = YOLO("last.pt")
results = model.train(resume=True)
```

---

## Ultralytics Integrations

**URL:** https://docs.ultralytics.com/integrations/

**Contents:**
- Ultralytics Integrations
- Training Integrations
- Deployment Integrations
- Datasets Integrations
  - Export Formats
- Contribute to Our Integrations
- FAQ
  - What is Ultralytics Platform, and how does it streamline the ML workflow?
  - Can I track the performance of my Ultralytics models using MLFlow?
  - What are the benefits of using Neural Magic for YOLO26 model optimization?

Welcome to the Ultralytics Integrations page! This page provides an overview of our partnerships with various tools and platforms, designed to streamline your machine learning workflows, enhance dataset management, simplify model training, and facilitate efficient deployment.

Watch: Ultralytics YOLO Deployment and Integrations

Albumentations: Enhance your Ultralytics models with powerful image augmentations to improve model robustness and generalization.

Amazon SageMaker: Leverage Amazon SageMaker to efficiently build, train, and deploy Ultralytics models, providing an all-in-one platform for the ML lifecycle.

ClearML: Automate your Ultralytics ML workflows, monitor experiments, and foster team collaboration.

Comet ML: Enhance your model development with Ultralytics by tracking, comparing, and optimizing your machine learning experiments.

DVC: Implement version control for your Ultralytics machine learning projects, synchronizing data, code, and models effectively.

Google Colab: Use Google Colab to train and evaluate Ultralytics models in a cloud-based environment that supports collaboration and sharing.

IBM Watsonx: See how IBM Watsonx simplifies the training and evaluation of Ultralytics models with its cutting-edge AI tools, effortless integration, and advanced model management system.

JupyterLab: Find out how to use JupyterLab's interactive and customizable environment to train and evaluate Ultralytics models with ease and efficiency.

Kaggle: Explore how you can use Kaggle to train and evaluate Ultralytics models in a cloud-based environment with pre-installed libraries, GPU support, and a vibrant community for collaboration and sharing.

MLFlow: Streamline the entire ML lifecycle of Ultralytics models, from experimentation and reproducibility to deployment.

Neptune: Maintain a comprehensive log of your ML experiments with Ultralytics in this metadata store designed for MLOps.

Paperspace Gradient: Paperspace Gradient simplifies working on YOLO26 projects by providing easy-to-use cloud tools for training, testing, and deploying your models quickly.

Ray Tune: Optimize the hyperparameters of your Ultralytics models at any scale.

TensorBoard: Visualize your Ultralytics ML workflows, monitor model metrics, and foster team collaboration.

Ultralytics Platform: Access and contribute to a community of pretrained Ultralytics models.

VS Code: An extension for VS Code that provides code snippets to accelerate Ultralytics development workflows and offers examples to help anyone learn or get started.

Weights & Biases (W&B): Monitor experiments, visualize metrics, and foster reproducibility and collaboration on Ultralytics projects.

Axelera: Explore Metis accelerators and the Voyager SDK for running Ultralytics models with efficient edge inference.

CoreML: CoreML, developed by Apple, is a framework designed for efficiently integrating machine learning models into applications across iOS, macOS, watchOS, and tvOS, using Apple's hardware for effective and secure model deployment.

ExecuTorch: Developed by Meta, ExecuTorch is PyTorch's unified solution for deploying Ultralytics YOLO models on edge devices.

Gradio: Deploy Ultralytics models with Gradio for real-time, interactive object detection demos.

MNN: Developed by Alibaba, MNN is a highly efficient and lightweight deep learning framework. It supports inference and training of deep learning models and has industry-leading performance for inference and training on-device.

NCNN: Developed by Tencent, NCNN is an efficient neural network inference framework tailored for mobile devices. It enables direct deployment of AI models into apps, optimizing performance across various mobile platforms.

Neural Magic: Leverage Quantization Aware Training (QAT) and pruning techniques to optimize Ultralytics models for superior performance and leaner size.

ONNX: An open-source format created by Microsoft for facilitating the transfer of AI models between various frameworks, enhancing the versatility and deployment flexibility of Ultralytics models.

OpenVINO: Intel's toolkit for optimizing and deploying computer vision models efficiently across various Intel CPU and GPU platforms.

PaddlePaddle: An open-source deep learning platform by Baidu, PaddlePaddle enables the efficient deployment of AI models and focuses on the scalability of industrial applications.

Rockchip RKNN: Developed by Rockchip, RKNN is a specialized neural network inference framework optimized for Rockchip's hardware platforms, particularly their NPUs. It facilitates efficient deployment of AI models on edge devices, enabling high-performance inference in real-time applications.

Seeed Studio reCamera: Developed by Seeed Studio, the reCamera is an advanced edge AI device designed for real-time computer vision applications. Powered by the RISC-V-based SG200X processor, it delivers high-performance AI inference with energy efficiency. Its modular design, advanced video processing capabilities, and support for flexible deployment make it an ideal choice for various use cases, including safety monitoring, environmental applications, and manufacturing.

SONY IMX500: Optimize and deploy Ultralytics YOLO26 models on Raspberry Pi AI Cameras with the IMX500 sensor for fast, low-power performance.

TensorRT: Developed by NVIDIA, this high-performance deep learning inference framework and model format optimizes AI models for accelerated speed and efficiency on NVIDIA GPUs, ensuring streamlined deployment.

TF GraphDef: Developed by Google, GraphDef is TensorFlow's format for representing computation graphs, enabling optimized execution of machine learning models across diverse hardware.

TF SavedModel: Developed by Google, TF SavedModel is a universal serialization format for TensorFlow models, enabling easy sharing and deployment across a wide range of platforms, from servers to edge devices.

TF.js: Developed by Google to facilitate machine learning in browsers and Node.js, TF.js allows JavaScript-based deployment of ML models.

TFLite: Developed by Google, TFLite is a lightweight framework for deploying machine learning models on mobile and edge devices, ensuring fast, efficient inference with minimal memory footprint.

TFLite Edge TPU: Developed by Google for optimizing TensorFlow Lite models on Edge TPUs, this model format ensures high-speed, efficient edge computing.

TorchScript: Developed as part of the PyTorch framework, TorchScript enables efficient execution and deployment of machine learning models in various production environments without the need for Python dependencies.

We also support a variety of model export formats for deployment in different environments. Here are the available formats:

Explore the links to learn more about each integration and how to get the most out of them with Ultralytics. See full export details in the Export page.

We're always excited to see how the community integrates Ultralytics YOLO with other technologies, tools, and platforms! If you have successfully integrated YOLO with a new system or have valuable insights to share, consider contributing to our Integrations Docs.

By writing a guide or tutorial, you can help expand our documentation and provide real-world examples that benefit the community. It's an excellent way to contribute to the growing ecosystem around Ultralytics YOLO.

To contribute, please check out our Contributing Guide for instructions on how to submit a Pull Request (PR) 🛠️. We eagerly await your contributions!

Let's collaborate to make the Ultralytics YOLO ecosystem more expansive and feature-rich 🙏!

Ultralytics Platform is a cloud-based platform designed to make machine learning workflows for Ultralytics models seamless and efficient. By using this tool, you can easily upload datasets, train models, perform real-time tracking, and deploy YOLO models without needing extensive coding skills. The platform serves as a centralized workspace where you can manage your entire ML pipeline from data preparation to deployment. You can explore the key features on the Ultralytics Platform page and get started quickly with our Quickstart guide.

Yes, you can. Integrating MLFlow with Ultralytics models allows you to track experiments, improve reproducibility, and streamline the entire ML lifecycle. Detailed instructions for setting up this integration can be found on the MLFlow integration page. This integration is particularly useful for monitoring model metrics, comparing different training runs, and managing the ML workflow efficiently. MLFlow provides a centralized platform to log parameters, metrics, and artifacts, making it easier to understand model behavior and make data-driven improvements.

Neural Magic optimizes YOLO26 models by leveraging techniques like Quantization Aware Training (QAT) and pruning, resulting in highly efficient, smaller models that perform better on resource-limited hardware. Check out the Neural Magic integration page to learn how to implement these optimizations for superior performance and leaner models. This is especially beneficial for deployment on edge devices where computational resources are constrained. Neural Magic's DeepSparse engine can deliver up to 6x faster inference on CPUs, making it possible to run complex models without specialized hardware.

To deploy Ultralytics YOLO models with Gradio for interactive object detection demos, you can follow the steps outlined on the Gradio integration page. Gradio allows you to create easy-to-use web interfaces for real-time model inference, making it an excellent tool for showcasing your YOLO model's capabilities in a user-friendly format suitable for both developers and end-users. With just a few lines of code, you can build interactive applications that demonstrate your model's performance on custom inputs, facilitating better understanding and evaluation of your computer vision solutions.

---

## Ultralytics Platform

**URL:** https://docs.ultralytics.com/platform/

**Contents:**
- Ultralytics Platform
- What is Ultralytics Platform?
- Workflow: Data → Train → Deploy
- Multi-Region Infrastructure
- Key Features
  - Data Preparation
  - Model Training
  - Deployment
  - Account Management
- Quick Links

Ultralytics Platform is a comprehensive end-to-end computer vision platform that streamlines the entire ML workflow from data preparation to model deployment. Built for teams and individuals who need production-ready computer vision solutions without the infrastructure complexity.

Watch: Getting Started with Ultralytics Platform

Ultralytics Platform is designed to replace fragmented ML tooling with a unified solution. It combines the capabilities of:

All in one platform with native support for YOLO26 and YOLO11 models.

The Platform follows a streamlined three-stage workflow:

Your data stays in your region. Ultralytics Platform operates infrastructure in three global regions:

You select your region during onboarding, and all your data, models, and deployments remain in that region.

Get started with these resources:

To get started with Ultralytics Platform:

For a detailed guide, see the Quickstart page.

Ultralytics Platform offers:

Ultralytics Platform supports multiple GPU types for cloud training:

See Cloud Training for complete pricing and GPU options.

You can train models anywhere and stream metrics to Platform.

Package Version Requirement

Platform integration requires ultralytics>=8.4.0. Lower versions will NOT work with Platform.

See Cloud Training for more details on remote training.

The Platform includes a full-featured annotation editor supporting:

See Annotation for the complete guide.

**Examples:**

Example 1 (php):
```php
graph LR
    subgraph Data["📁 Data"]
        A[Upload] --> B[Annotate]
        B --> C[Analyze]
    end
    subgraph Train["🚀 Train"]
        D[Configure] --> E[Train on GPU]
        E --> F[View Metrics]
    end
    subgraph Deploy["🌐 Deploy"]
        G[Test] --> H[Deploy Endpoint]
        H --> I[Monitor]
    end
    Data --> Train --> Deploy
```

Example 2 (unknown):
```unknown
pip install "ultralytics>=8.4.0"
```

Example 3 (markdown):
```markdown
# Set your API key
export ULTRALYTICS_API_KEY="your_api_key"

# Train with project/name to stream metrics
yolo train model=yolo26n.pt data=coco.yaml epochs=100 project=username/my-project name=exp1
```

---

## Ultralytics VS Code Extension

**URL:** https://docs.ultralytics.com/integrations/vscode/

**Contents:**
- Ultralytics VS Code Extension
- Features and Benefits
- Inspired by the Ultralytics Community
- Why VS Code?
- Installing the Extension
  - Installing in VS Code
  - Installing from the VS Code Extension Marketplace
- Using the Ultralytics-Snippets Extension
  - Overview
  - Code Snippet Fields

Watch: How to use Ultralytics Visual Studio Code Extension | Ready-to-Use Code Snippets | Ultralytics YOLO 🎉

✅ Are you a data scientist or machine learning engineer building computer vision applications with Ultralytics?

✅ Do you despise writing the same blocks of code repeatedly?

✅ Are you always forgetting the arguments or default values for the export, predict, train, track, or val methods?

✅ Looking to get started with Ultralytics and wish you had an easier way to reference or run code examples?

✅ Want to speed up your development cycle when working with Ultralytics?

If you use Visual Studio Code and answered 'yes' to any of the above, then the Ultralytics-snippets extension for VS Code is here to help! Read on to learn more about the extension, how to install it, and how to use it.

Run example code using Ultralytics YOLO in under 20 seconds! 🚀

The inspiration to build this extension came from the Ultralytics Community. Questions from the Community around similar topics and examples fueled the development for this project. Additionally, many members of the Ultralytics team use VS Code to accelerate their own work ⚡.

Visual Studio Code is extremely popular with developers worldwide and has ranked most popular by the Stack Overflow Developer Survey in 2021, 2022, 2023, and 2024. Due to VS Code's high level of customization, built-in features, broad compatibility, and extensibility, it's no surprise that so many developers are using it. Given the popularity in the wider developer community and within the Ultralytics Discord, Discourse, Reddit, and GitHub Communities, it made sense to build a VS Code extension to help streamline your workflow and boost your productivity.

Want to let us know what you use for developing code? Head over to our Discourse community poll and let us know! While you're there, maybe check out some of our favorite computer vision, machine learning, AI, and developer memes, or even post your favorite!

Any code environment that will allow for installing VS Code extensions should be compatible with the Ultralytics-snippets extension. After publishing the extension, it was discovered that neovim can be made compatible with VS Code extensions. To learn more see the neovim install section of the Readme in the Ultralytics-Snippets repository.

Navigate to the Extensions menu in VS Code or use the shortcut Ctrl+Shift ⇑+x, and search for Ultralytics-snippets.

Click the Install button.

Visit the VS Code Extension Marketplace and search for Ultralytics-snippets or go straight to the extension page on the VS Code marketplace.

Click the Install button and allow your browser to launch a VS Code session.

Follow any prompts to install the extension.

Visual Studio Code Extension Marketplace page for Ultralytics-Snippets

🧠 Intelligent Code Completion: Write code faster and more accurately with advanced code completion suggestions tailored to the Ultralytics API.

⌛ Increased Development Speed: Save time by eliminating repetitive coding tasks and leveraging pre-built code block snippets.

🔬 Improved Code Quality: Write cleaner, more consistent, and error-free code with intelligent code completion.

💎 Streamlined Workflow: Stay focused on the core logic of your project by automating common tasks.

The extension will only operate when the Language Mode is configured for Python 🐍. This is to avoid snippets from being inserted when working on any other file type. All snippets have prefix starting with ultra, and simply typing ultra in your editor after installing the extension, will display a list of possible snippets to use. You can also open the VS Code Command Palette using Ctrl+Shift ⇑+p and running the command Snippets: Insert Snippet.

Many snippets have "fields" with default placeholder values or names. For instance, output from the predict method could be saved to a Python variable named r, results, detections, preds or whatever else a developer chooses, which is why snippets include "fields". Using Tab ⇥ on your keyboard after a snippet is inserted, your cursor will move between fields quickly. Once a field is selected, typing a new variable name will change that instance, but also every other instance in the snippet code for that variable!

After inserting snippet, renaming model as world_model updates all instances. Pressing Tab ⇥ moves to the next field, which opens a dropdown menu and allows for selection of a model scale, and moving to the next field provides another dropdown to choose either world or worldv2 model variant.

Even Shorter Shortcuts

It's not required to type the full prefix of the snippet, or even to start typing from the start of the snippet. See example in the image below.

The snippets are named in the most descriptive way possible, but this means there could be a lot to type and that would be counterproductive if the aim is to move faster. Luckily VS Code lets users type ultra.example-yolo-predict, example-yolo-predict, yolo-predict, or even ex-yolo-p and still reach the intended snippet option! If the intended snippet was actually ultra.example-yolo-predict-kwords, then just using your keyboard arrows ↑ or ↓ to highlight the desired snippet and pressing Enter ↵ or Tab ⇥ will insert the correct block of code.

Typing ex-yolo-p will still arrive at the correct snippet.

These are the current snippet categories available to the Ultralytics-snippets extension. More will be added in the future, so make sure to check for updates and to enable auto-updates for the extension. You can also request additional snippets to be added if you feel there's any missing.

The ultra.examples snippets are very useful for anyone looking to learn how to get started with the basics of working with Ultralytics YOLO. Example snippets are intended to run once inserted (some have dropdown options as well). An example of this is shown at the animation at the top of this page, where after the snippet is inserted, all code is selected and run interactively using Shift ⇑+Enter ↵.

Just like the animation shows at the top of this page, you can use the snippet ultra.example-yolo-predict to insert the following code example. Once inserted, the only configurable option is for the model scale which can be any one of: n, s, m, l, or x.

The aim for snippets other than the ultra.examples are for making development easier and quicker when working with Ultralytics. A common code block to be used in many projects, is to iterate the list of Results returned from using the model predict method. The ultra.result-loop snippet can help with this.

Using the ultra.result-loop will insert the following default code (including comments).

However, since Ultralytics supports numerous tasks, when working with inference results there are other Results attributes that you may wish to access, which is where the snippet fields will be powerful.

Once tabbed to the boxes field, a dropdown menu appears to allow selection of another attribute as required.

There are over 💯 keyword arguments for all the various Ultralytics tasks and modes! That's a lot to remember, and it can be easy to forget if the argument is save_frame or save_frames (it's definitely save_frames by the way). This is where the ultra.kwargs snippets can help out!

To insert the predict method, including all inference arguments, use ultra.kwargs-predict, which will insert the following code (including comments).

This snippet has fields for all the keyword arguments, but also for model and src in case you've used a different variable in your code. On each line containing a keyword argument, a brief description is included for reference.

The best way to find out what snippets are available is to download and install the extension and try it out! If you're curious and want to take a look at the list beforehand, you can visit the repo or extension page on the VS Code marketplace to view the tables for all available snippets.

The Ultralytics-Snippets extension for VS Code is designed to empower data scientists and machine learning engineers to build computer vision applications using Ultralytics YOLO more efficiently. By providing pre-built code snippets and useful examples, we help you focus on what matters most: creating innovative solutions. Please share your feedback by visiting the extension page on the VS Code marketplace and leaving a review. ⭐

New snippets can be requested using the Issues on the Ultralytics-Snippets repo.

VS Code uses the key combination Ctrl+Space to show more/less information in the preview window. If you're not seeing a snippet preview when you type in a code snippet prefix, using this key combination should restore the preview.

If you use VS Code and have started to see a message prompting you to install the Ultralytics-snippets extension, and don't want to see the message any more, there are two ways to disable this message.

Install Ultralytics-snippets and the message will no longer be shown 😆!

You can be using yolo settings vscode_msg False to disable the message from showing without having to install the extension. You can learn more about the Ultralytics Settings on the quickstart page if you're unfamiliar.

Visit the Ultralytics-snippets repo and open an Issue or Pull Request!

Like any other VS Code extension, you can uninstall it by navigating to the Extensions menu in VS Code. Find the Ultralytics-snippets extension in the menu and click the cog icon (⚙) and then click on "Uninstall" to remove the extension.

**Examples:**

Example 1 (python):
```python
from ultralytics import ASSETS, YOLO

model = YOLO("yolo26n.pt", task="detect")
results = model(source=ASSETS / "bus.jpg")

for result in results:
    print(result.boxes.data)
    # result.show()  # uncomment to view each result image
```

Example 2 (markdown):
```markdown
# reference https://docs.ultralytics.com/modes/predict/#working-with-results

for result in results:
    result.boxes.data  # torch.Tensor array
```

Example 3 (sql):
```sql
model.predict(
    source=src,  # (str, optional) source directory for images or videos
    imgsz=640,  # (int | list) input images size as int or list[w,h] for predict
    conf=0.25,  # (float) minimum confidence threshold
    iou=0.7,  # (float) intersection over union (IoU) threshold for NMS
    vid_stride=1,  # (int) video frame-rate stride
    stream_buffer=False,  # (bool) buffer incoming frames in a queue (True) or only keep the most recent frame (False)
    visualize=False,  # (bool) visualize model features
    augment=False,  # (bool) apply image augmentation to prediction sources
    agnostic_nms=False,  # (bool) class-agnostic NMS
    classes=None,  # (int | list[int], optional) filter results by class, i.e. classes=0, or classes=[0,2,3]
    retina_masks=False,  # (bool) use high-resolution segmentation masks
    embed=None,  # (list[int], optional) return feature vectors/embeddings from given layers
    show=False,  # (bool) show predicted images and videos if environment allows
    save=True,  # (bool) save prediction results
    save_frames=False,  # (bool) save predicted individual video frames
    save_txt=False,  # (bool) save results as .txt file
    save_conf=False,  # (bool) save results with confidence scores
    save_crop=False,  # (bool) save cropped images with results
    stream=False,  # (bool) for processing long videos or numerous images with reduced memory usage by returning a generator
    verbose=True,  # (bool) enable/disable verbose inference logging in the terminal
)
```

---
