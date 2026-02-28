# Raw-Ultralytics - Ar

**Pages:** 26

---

## Conda Quickstart Guide for Ultralytics

**URL:** https://docs.ultralytics.com/guides/conda-quickstart/

**Contents:**
- Conda Quickstart Guide for Ultralytics
- What You Will Learn
- Prerequisites
- Setting up a Conda Environment
- Installing Ultralytics
  - Note on CUDA Environment
- Using Ultralytics
- Ultralytics Conda Docker Image
- Speeding Up Installation with Libmamba
  - How to Enable Libmamba

This guide provides a comprehensive introduction to setting up a Conda environment for your Ultralytics projects. Conda is an open-source package and environment management system that offers an excellent alternative to pip for installing packages and dependencies. Its isolated environments make it particularly well-suited for data science and machine learning endeavors. For more details, visit the Ultralytics Conda package on Anaconda and check out the Ultralytics feedstock repository for package updates on GitHub.

First, let's create a new Conda environment. Open your terminal and run the following command:

Activate the new environment:

You can install the Ultralytics package from the conda-forge channel. Execute the following command:

If you're working in a CUDA-enabled environment, it's a good practice to install ultralytics, pytorch, and pytorch-cuda together to resolve any conflicts:

With Ultralytics installed, you can now start using its robust features for object detection, instance segmentation, and more. For example, to predict an image, you can run:

If you prefer using Docker, Ultralytics offers Docker images with a Conda environment included. You can pull these images from DockerHub.

Pull the latest Ultralytics image:

If you're looking to speed up the package installation process in Conda, you can opt to use libmamba, a fast, cross-platform, and dependency-aware package manager that serves as an alternative solver to Conda's default.

To enable libmamba as the solver for Conda, you can perform the following steps:

First, install the conda-libmamba-solver package. This can be skipped if your Conda version is 4.11 or above, as libmamba is included by default.

Next, configure Conda to use libmamba as the solver:

And that's it! Your Conda installation will now use libmamba as the solver, which should result in a faster package installation process.

You have successfully set up a Conda environment, installed the Ultralytics package, and are now ready to explore its features. For more advanced tutorials and examples, see the Ultralytics documentation.

Setting up a Conda environment for Ultralytics projects is straightforward and ensures smooth package management. First, create a new Conda environment using the following command:

Then, activate the new environment with:

Finally, install Ultralytics from the conda-forge channel:

Conda is a robust package and environment management system that offers several advantages over pip. It manages dependencies efficiently and ensures that all necessary libraries are compatible. Conda's isolated environments prevent conflicts between packages, which is crucial in data science and machine learning projects. Additionally, Conda supports binary package distribution, speeding up the installation process.

Yes, you can enhance performance by utilizing a CUDA-enabled environment. Ensure that you install ultralytics, pytorch, and pytorch-cuda together to avoid conflicts:

This setup enables GPU acceleration, crucial for intensive tasks like deep learning model training and inference. For more information, visit the Ultralytics installation guide.

Using Ultralytics Docker images ensures a consistent and reproducible environment, eliminating "it works on my machine" issues. These images include a pre-configured Conda environment, simplifying the setup process. You can pull and run the latest Ultralytics Docker image with the following commands:

This approach is ideal for deploying applications in production or running complex workflows without manual configuration. Learn more about Ultralytics Conda Docker Image.

You can speed up the package installation process by using libmamba, a fast dependency solver for Conda. First, install the conda-libmamba-solver package:

Then configure Conda to use libmamba as the solver:

This setup provides faster and more efficient package management. For more tips on optimizing your environment, read about libmamba installation.

**Examples:**

Example 1 (unknown):
```unknown
conda create --name ultralytics-env python=3.11 -y
```

Example 2 (unknown):
```unknown
conda activate ultralytics-env
```

Example 3 (unknown):
```unknown
conda install -c conda-forge ultralytics
```

Example 4 (unknown):
```unknown
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics
```

---

## Data Preparation

**URL:** https://docs.ultralytics.com/platform/data/

**Contents:**
- Data Preparation
- Overview
- Workflow
- Supported Tasks
- Key Features
  - Smart Storage
  - Dataset URIs
  - Statistics and Visualization
- Quick Links
- FAQ

Data preparation is the foundation of successful computer vision models. Ultralytics Platform provides comprehensive tools for managing your training data, from upload through annotation to analysis.

The Data section of Ultralytics Platform helps you:

Ultralytics Platform supports all 5 YOLO task types:

Ultralytics Platform uses efficient storage technology:

Reference datasets using the ul:// URI format:

This allows training on Platform datasets from any machine with your API key configured.

Every dataset includes automatic statistics:

Ultralytics Platform supports:

Storage limits depend on your plan:

Yes! Use the dataset URI format to train locally:

Or export your dataset in NDJSON format for fully offline training.

**Examples:**

Example 1 (php):
```php
graph LR
    A[📤 Upload] --> B[🏷️ Annotate]
    B --> C[📊 Analyze]
    C --> D[🚀 Train]

    style A fill:#4CAF50,color:#fff
    style B fill:#2196F3,color:#fff
    style C fill:#FF9800,color:#fff
    style D fill:#9C27B0,color:#fff
```

Example 2 (unknown):
```unknown
yolo train data=ul://username/datasets/my-dataset
```

Example 3 (unknown):
```unknown
export ULTRALYTICS_API_KEY="your_key"
yolo train data=ul://username/datasets/my-dataset epochs=100
```

---

## Docker Quickstart Guide for Ultralytics

**URL:** https://docs.ultralytics.com/guides/docker-quickstart/

**Contents:**
- Docker Quickstart Guide for Ultralytics
- What You Will Learn
- Prerequisites
- Setting up Docker with NVIDIA Support
  - Installing NVIDIA Container Toolkit
  - Verify NVIDIA Runtime with Docker
- Installing Ultralytics Docker Images
- Running Ultralytics in Docker Container
  - Using only the CPU
  - Using GPUs

This guide serves as a comprehensive introduction to setting up a Docker environment for your Ultralytics projects. Docker is a platform for developing, shipping, and running applications in containers. It is particularly beneficial for ensuring that the software will always run the same, regardless of where it's deployed. For more details, visit the Ultralytics Docker repository on Docker Hub.

Watch: How to Get started with Docker | Usage of Ultralytics Python Package inside Docker live demo 🎉

First, verify that the NVIDIA drivers are properly installed by running:

Now, let's install the NVIDIA Container Toolkit to enable GPU support in Docker containers:

Install the latest version of nvidia-container-toolkit:

Optionally, you can install a specific version of the nvidia-container-toolkit by setting the NVIDIA_CONTAINER_TOOLKIT_VERSION environment variable:

Update the package lists and install the nvidia-container-toolkit package:

Optionally, you can install a specific version of the nvidia-container-toolkit by setting the NVIDIA_CONTAINER_TOOLKIT_VERSION environment variable:

Run docker info | grep -i runtime to ensure that nvidia appears in the list of runtimes:

Ultralytics offers several Docker images optimized for various platforms and use-cases:

To pull the latest image:

Here's how to execute the Ultralytics Docker container:

The -it flag assigns a pseudo-TTY and keeps stdin open, allowing you to interact with the container. The --ipc=host flag enables sharing of host's IPC namespace, essential for sharing memory between processes. The --gpus flag allows the container to access the host's GPUs.

To work with files on your local machine within the container, you can use Docker volumes:

Replace /path/on/host with the directory path on your local machine and /path/in/container with the desired path inside the Docker container.

Training outputs save to /ultralytics/runs/<task>/<name>/ inside the container by default. Without mounting a host directory, outputs are lost when the container is removed.

To persist training outputs:

This saves all training outputs to ./runs on your host machine.

Highly Experimental - User Assumes All Risk

The following instructions are experimental. Sharing a X11 socket with a Docker container poses potential security risks. Therefore, it's recommended to test this solution only in a controlled environment. For more information, refer to these resources on how to use xhost(1)(2).

Docker is primarily used to containerize background applications and CLI programs, but it can also run graphical programs. In the Linux world, two main graphic servers handle graphical display: X11 (also known as the X Window System) and Wayland. Before starting, it's essential to determine which graphics server you are currently using. Run this command to find out:

Setup and configuration of an X11 or Wayland display server is outside the scope of this guide. If the above command returns nothing, then you'll need to start by getting either working for your system before continuing.

If you're using X11, you can run the following command to allow the Docker container to access the X11 socket:

This command sets the DISPLAY environment variable to the host's display, mounts the X11 socket, and maps the .Xauthority file to the container. The xhost +local:docker command allows the Docker container to access the X11 server.

For Wayland, use the following command:

This command sets the DISPLAY environment variable to the host's display, mounts the Wayland socket, and allows the Docker container to access the Wayland server.

Now you can display graphical applications inside your Docker container. For example, you can run the following CLI command to visualize the predictions from a YOLO26 model:

A simple way to validate that the Docker group has access to the X11 server is to run a container with a GUI program like xclock or xeyes. Alternatively, you can also install these programs in the Ultralytics Docker container to test the access to the X11 server of your GNU-Linux display server. If you run into any problems, consider setting the environment variable -e QT_DEBUG_PLUGINS=1. Setting this environment variable enables the output of debugging information, aiding in the troubleshooting process.

In both cases, don't forget to revoke access from the Docker group when you're done.

Refer to the following guide on viewing the image results using a terminal

You are now set up to use Ultralytics with Docker and ready to take advantage of its capabilities. For alternative installation methods, see the Ultralytics quickstart documentation.

To set up Ultralytics with Docker, first ensure that Docker is installed on your system. If you have an NVIDIA GPU, install the NVIDIA Container Toolkit to enable GPU support. Then, pull the latest Ultralytics Docker image from Docker Hub using the following command:

For detailed steps, refer to our Docker Quickstart Guide.

Using Ultralytics Docker images ensures a consistent environment across different machines, replicating the same software and dependencies. This is particularly useful for collaborating across teams, running models on various hardware, and maintaining reproducibility. For GPU-based training, Ultralytics provides optimized Docker images such as Dockerfile for general GPU usage and Dockerfile-jetson for NVIDIA Jetson devices. Explore Ultralytics Docker Hub for more details.

First, ensure that the NVIDIA Container Toolkit is installed and configured. Then, use the following command to run Ultralytics YOLO with GPU support:

This command sets up a Docker container with GPU access. For additional details, see the Docker Quickstart Guide.

To visualize YOLO prediction results with a GUI in a Docker container, you need to allow Docker to access your display server. For systems running X11, the command is:

For systems running Wayland, use:

More information can be found in the Run graphical user interface (GUI) applications in a Docker Container section.

Yes, you can mount local directories into the Ultralytics Docker container using the -v flag:

Replace /path/on/host with the directory on your local machine and /path/in/container with the desired path inside the container. This setup allows you to work with your local files within the container. For more information, refer to the Note on File Accessibility section.

**Examples:**

Example 1 (unknown):
```unknown
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \
  | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \
    | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```

Example 2 (sql):
```sql
sudo apt-get update
```

Example 3 (unknown):
```unknown
sudo apt-get install -y nvidia-container-toolkit \
  nvidia-container-toolkit-base libnvidia-container-tools \
  libnvidia-container1
```

Example 4 (bash):
```bash
export NVIDIA_CONTAINER_TOOLKIT_VERSION=1.17.8-1
sudo apt-get install -y \
  nvidia-container-toolkit=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  nvidia-container-toolkit-base=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container-tools=${NVIDIA_CONTAINER_TOOLKIT_VERSION} \
  libnvidia-container1=${NVIDIA_CONTAINER_TOOLKIT_VERSION}
```

---

## Install Ultralytics

**URL:** https://docs.ultralytics.com/quickstart/

**Contents:**
- Install Ultralytics
  - Conda Docker Image
- Headless Server Installation
- Advanced Installation
- Use Ultralytics with CLI
- Use Ultralytics with Python
- Ultralytics Settings
  - Inspecting Settings
  - Modifying Settings
  - Understanding Settings

Ultralytics offers a variety of installation methods, including pip, conda, and Docker. You can install YOLO via the ultralytics pip package for the latest stable release, or by cloning the Ultralytics GitHub repository for the most current version. Docker is also an option to run the package in an isolated container, which avoids local installation.

Watch: Ultralytics YOLO Quick Start Guide

Install or update the ultralytics package using pip by running pip install -U ultralytics. For more details on the ultralytics package, visit the Python Package Index (PyPI).

You can also install ultralytics directly from the Ultralytics GitHub repository. This can be useful if you want the latest development version. Ensure you have the Git command-line tool installed, and then run:

Conda can be used as an alternative package manager to pip. For more details, visit Anaconda. The Ultralytics feedstock repository for updating the conda package is available at GitHub.

If you are installing in a CUDA environment, it is best practice to install ultralytics, pytorch, and pytorch-cuda in the same command. This allows the conda package manager to resolve any conflicts. Alternatively, install pytorch-cuda last to override the CPU-specific pytorch package if necessary.

Ultralytics Conda Docker images are also available on Docker Hub. These images are based on Miniconda3 and provide a straightforward way to start using ultralytics in a Conda environment.

Clone the Ultralytics GitHub repository if you are interested in contributing to development or wish to experiment with the latest source code. After cloning, navigate into the directory and install the package in editable mode -e using pip.

Use Docker to execute the ultralytics package in an isolated container, ensuring consistent performance across various environments. By selecting one of the official ultralytics images from Docker Hub, you avoid the complexity of local installation and gain access to a verified working environment. Ultralytics offers five main supported Docker images, each designed for high compatibility and efficiency:

Here are the commands to get the latest image and execute it:

The above command initializes a Docker container with the latest ultralytics image. The -it flags assign a pseudo-TTY and keep stdin open, allowing interaction with the container. The --ipc=host flag sets the IPC (Inter-Process Communication) namespace to the host, which is essential for sharing memory between processes. The --gpus all flag enables access to all available GPUs inside the container, crucial for tasks requiring GPU computation.

Note: To work with files on your local machine within the container, use Docker volumes to mount a local directory into the container:

Replace /path/on/host with the directory path on your local machine, and /path/in/container with the desired path inside the Docker container.

For advanced Docker usage, explore the Ultralytics Docker Guide.

See the ultralytics pyproject.toml file for a list of dependencies. Note that all examples above install all required dependencies.

PyTorch requirements vary by operating system and CUDA requirements, so install PyTorch first by following the instructions at PyTorch.

For server environments without a display (e.g., cloud VMs, Docker containers, CI/CD pipelines), use the ultralytics-opencv-headless package. This is identical to the standard ultralytics package but depends on opencv-python-headless instead of opencv-python, avoiding unnecessary GUI dependencies and potential libGL errors.

Both packages provide the same functionality and API. The headless variant simply excludes OpenCV's GUI components that require display libraries.

While the standard installation methods cover most use cases, you might need a more tailored setup for development or custom configurations.

If you need persistent custom modifications, you can fork the Ultralytics repository, make changes to pyproject.toml or other code, and install from your fork.

Clone the repository locally, modify files as needed, and install in editable mode.

This approach is useful for development or testing local changes before committing.

Specify a custom Ultralytics fork in your requirements.txt file to ensure consistent installations across your team.

Install dependencies from the file:

The Ultralytics command-line interface (CLI) allows for simple single-line commands without needing a Python environment. CLI requires no customization or Python code; run all tasks from the terminal with the yolo command. For more on using YOLO from the command line, see the CLI Guide.

Ultralytics yolo commands use the following syntax:

See all ARGS in the full Configuration Guide or with the yolo cfg CLI command.

Train a detection model for 10 epochs with an initial learning rate of 0.01:

Predict a YouTube video using a pretrained segmentation model at image size 320:

Validate a pretrained detection model with a batch size of 1 and image size of 640:

Export a YOLO26n classification model to ONNX format with an image size of 224x128 (no TASK required):

Count objects in a video or live stream using YOLO26:

Monitor workout exercises using a YOLO26 pose model:

Use YOLO26 to count objects in a designated queue or region:

Perform object detection, instance segmentation, or pose estimation in a web browser using Streamlit:

Run special commands to see the version, view settings, run checks, and more:

Arguments must be passed as arg=value pairs, split by an equals = sign and delimited by spaces. Do not use -- argument prefixes or commas , between arguments.

The Ultralytics YOLO Python interface offers seamless integration into Python projects, making it easy to load, run, and process model outputs. Designed for simplicity, the Python interface allows users to quickly implement object detection, segmentation, and classification. This makes the YOLO Python interface an invaluable tool for incorporating these functionalities into Python projects.

For instance, users can load a model, train it, evaluate its performance, and export it to ONNX format with just a few lines of code. Explore the Python Guide to learn more about using YOLO within your Python projects.

The Ultralytics library includes a SettingsManager for fine-grained control over experiments, allowing users to access and modify settings easily. Stored in a JSON file within the environment's user configuration directory, these settings can be viewed or modified in the Python environment or via the Command-Line Interface (CLI).

To view the current configuration of your settings:

Use Python to view your settings by importing the settings object from the ultralytics module. Print and return settings with these commands:

The command-line interface allows you to check your settings with:

Ultralytics makes it easy to modify settings in the following ways:

In Python, use the update method on the settings object:

To modify settings using the command-line interface:

The table below overviews the adjustable settings within Ultralytics, including example values, data types, and descriptions.

Revisit these settings as you progress through projects or experiments to ensure optimal configuration.

Install Ultralytics with pip using:

This installs the latest stable release of the ultralytics package from PyPI. To install the development version directly from GitHub:

Ensure the Git command-line tool is installed on your system.

Yes, install Ultralytics YOLO using conda with:

This method is a great alternative to pip, ensuring compatibility with other packages. For CUDA environments, install ultralytics, pytorch, and pytorch-cuda together to resolve conflicts:

For more instructions, see the Conda quickstart guide.

Docker provides an isolated, consistent environment for Ultralytics YOLO, ensuring smooth performance across systems and avoiding local installation complexities. Official Docker images are available on Docker Hub, with variants for GPU, CPU, ARM64, NVIDIA Jetson, and Conda. To pull and run the latest image:

For detailed Docker instructions, see the Docker quickstart guide.

Clone the Ultralytics repository and set up a development environment with:

This allows contributions to the project or experimentation with the latest source code. For details, visit the Ultralytics GitHub repository.

The Ultralytics YOLO CLI simplifies running object detection tasks without Python code, enabling single-line commands for training, validation, and prediction directly from your terminal. The basic syntax is:

For example, to train a detection model:

Explore more commands and usage examples in the full CLI Guide.

**Examples:**

Example 1 (go):
```go
# Install or upgrade the ultralytics package from PyPI
pip install -U ultralytics
```

Example 2 (swift):
```swift
# Install the ultralytics package from GitHub
pip install git+https://github.com/ultralytics/ultralytics.git@main
```

Example 3 (go):
```go
# Install the ultralytics package using conda
conda install -c conda-forge ultralytics
```

Example 4 (julia):
```julia
# Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics
```

---

## Parking Management using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/parking-management/

**Contents:**
- Parking Management using Ultralytics YOLO26 🚀
- What is Parking Management System?
- Advantages of Parking Management System
- Real World Applications
- Parking Management System Code Workflow
  - ParkingManagement Arguments
- FAQ
  - How does Ultralytics YOLO26 enhance parking management systems?
  - What are the benefits of using Ultralytics YOLO26 for smart parking?
  - How can I define parking spaces using Ultralytics YOLO26?

Parking management with Ultralytics YOLO26 ensures efficient and safe parking by organizing spaces and monitoring availability. YOLO26 can improve parking lot management through real-time vehicle detection, and insights into parking occupancy.

Watch: How to Implement Parking Management Using Ultralytics YOLO 🚀

Choosing parking points is a critical and complex task in parking management systems. Ultralytics streamlines this process by providing a tool "Parking slots annotator" that lets you define parking lot areas, which can be utilized later for additional processing.

Step-1: Capture a frame from the video or camera stream where you want to manage the parking lot.

Step-2: Use the provided code to launch a graphical interface, where you can select an image and start outlining parking regions by mouse click to create polygons.

Parking slots annotator Ultralytics YOLO

Generally, tkinter comes pre-packaged with Python. However, if it did not, you can install it using the highlighted steps:

Step-3: After defining the parking areas with polygons, click save to store a JSON file with the data in your working directory.

Step-4: You can now utilize the provided code for parking management with Ultralytics YOLO.

Parking Management using Ultralytics YOLO

Here's a table with the ParkingManagement arguments:

The ParkingManagement solution allows the use of several track parameters:

Moreover, the following visualization options are supported:

Ultralytics YOLO26 greatly enhances parking management systems by providing real-time vehicle detection and monitoring. This results in optimized usage of parking spaces, reduced congestion, and improved safety through continuous surveillance. The Parking Management System enables efficient traffic flow, minimizing idle times and emissions in parking lots, thereby contributing to environmental sustainability. For further details, refer to the parking management code workflow.

Using Ultralytics YOLO26 for smart parking yields numerous benefits:

Defining parking spaces is straightforward with Ultralytics YOLO26:

Yes, Ultralytics YOLO26 allows customization for specific parking management needs. You can adjust parameters such as the occupied and available region colors, margins for text display, and much more. Utilizing the ParkingManagement class's arguments, you can tailor the model to suit your particular requirements, ensuring maximum efficiency and effectiveness.

Ultralytics YOLO26 is utilized in various real-world applications for parking lot management, including:

**Examples:**

Example 1 (python):
```python
from ultralytics import solutions

solutions.ParkingPtsSelection()
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

# Video capture
cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("parking management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize parking management object
parkingmanager = solutions.ParkingManagement(
    model="yolo26n.pt",  # path to model file
    json_file="bounding_boxes.json",  # path to parking annotations file
)

while cap.isOpened():
    ret, im0 = cap.read()
    if not ret:
        break

    results = parkingmanager(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

---

## Ultralytics Solutions: Harness YOLO26 to Solve Real-World Problems

**URL:** https://docs.ultralytics.com/solutions/

**Contents:**
- Ultralytics Solutions: Harness YOLO26 to Solve Real-World Problems
- Solutions
  - Solutions Arguments
  - Usage of SolutionAnnotator
  - Working with SolutionResults
  - Solutions Usage via CLI
  - Contribute to Our Solutions
- FAQ
  - How can I use Ultralytics YOLO for real-time object counting?
  - What are the benefits of using Ultralytics YOLO for security systems?

Ultralytics Solutions provide cutting-edge applications of YOLO models, offering real-world solutions like object counting, blurring, and security systems, enhancing efficiency and accuracy in diverse industries. Discover the power of YOLO26 for practical, impactful implementations.

Watch: How to Run Ultralytics Solutions from the Command Line (CLI) | Ultralytics YOLO26 🚀

Here's our curated list of Ultralytics solutions that can be used to create awesome computer vision projects.

Solutions also support some of the arguments from track, including parameters such as conf, line_width, tracker, model, show, verbose and classes.

You can use show_conf, show_labels, and other mentioned arguments to customize the visualization.

All Ultralytics Solutions use the separate class SolutionAnnotator, that extends the main Annotator class, and have the following methods:

Except Similarity Search, each Solution calls return a list of SolutionResults object.

SolutionResults object have the following attributes:

For more details, refer to the SolutionResults class documentation.

Most of the Solutions can be used directly through the command-line interface, including:

Count, Crop, Blur, Workout, Heatmap, Isegment, Visioneye, Speed, Queue, Analytics, Inference

We welcome contributions from the community! If you've mastered a particular aspect of Ultralytics YOLO that's not yet covered in our solutions, we encourage you to share your expertise. Writing a guide is a great way to give back to the community and help us make our documentation more comprehensive and user-friendly.

To get started, please read our Contributing Guide for guidelines on how to open up a Pull Request (PR) 🛠️. We look forward to your contributions!

Let's work together to make the Ultralytics YOLO ecosystem more robust and versatile 🙏!

Ultralytics YOLO26 can be used for real-time object counting by leveraging its advanced object detection capabilities. You can follow our detailed guide on Object Counting to set up YOLO26 for live video stream analysis. Simply install YOLO26, load your model, and process video frames to count objects dynamically.

Ultralytics YOLO26 enhances security systems by offering real-time object detection and alert mechanisms. By employing YOLO26, you can create a security alarm system that triggers alerts when new objects are detected in the surveillance area. Learn how to set up a Security Alarm System with YOLO26 for robust security monitoring.

Ultralytics YOLO26 can significantly improve queue management systems by accurately counting and tracking people in queues, thus helping to reduce wait times and optimize service efficiency. Follow our detailed guide on Queue Management to learn how to implement YOLO26 for effective queue monitoring and analysis.

Yes, Ultralytics YOLO26 can be effectively used for monitoring workouts by tracking and analyzing fitness routines in real-time. This allows for precise evaluation of exercise form and performance. Explore our guide on Workouts Monitoring to learn how to set up an AI-powered workout monitoring system using YOLO26.

Ultralytics YOLO26 can generate heatmaps to visualize data intensity across a given area, highlighting regions of high activity or interest. This feature is particularly useful in understanding patterns and trends in various computer vision tasks. Learn more about creating and using Heatmaps with YOLO26 for comprehensive data analysis and visualization.

**Examples:**

Example 1 (python):
```python
import cv2

from ultralytics import solutions

im0 = cv2.imread("path/to/img")

region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]

counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",  # model="yolo26n-obb.pt" for object counting with OBB model.
    # classes=[0, 2],  # count specific classes i.e. person and car with COCO pretrained model.
    # tracker="botsort.yaml"  # Choose trackers i.e "bytetrack.yaml"
)
results = counter(im0)
print(results.in_count)  # display in_counts
print(results.out_count)  # display out_counts
print(results.classwise_count)  # display classwise_count
```

Example 2 (unknown):
```unknown
yolo SOLUTIONS SOLUTION_NAME ARGS
```

Example 3 (unknown):
```unknown
yolo solutions count show=True # for object counting

yolo solutions count source="path/to/video.mp4" # specify video file path
```

---

## أنماط Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/ar/modes/

**Contents:**
- أنماط Ultralytics YOLO26
- مقدمة
  - لمحة عن الأوضاع
- تدريب
- التحقق
- توقع
- تصدير
- تتبع
- قياس الأداء
- الأسئلة الشائعة

Ultralytics YOLO26 ليس مجرد نموذج آخر لـ detect الكائنات؛ إنه إطار عمل متعدد الاستخدامات مصمم لتغطية دورة الحياة الكاملة لنماذج التعلم الآلي—من استيعاب البيانات وتدريب النموذج إلى التحقق والنشر والـ track في العالم الحقيقي. يخدم كل نمط غرضًا محددًا ومصممًا ليوفر لك المرونة والكفاءة المطلوبة للمهام وحالات الاستخدام المختلفة.

شاهد: البرنامج التعليمي لأوضاع Ultralytics: التدريب والتحقق والتنبؤ والتصدير ووضع المعايير.

يعد فهم الأنماط المختلفة التي يدعمها Ultralytics YOLO26 أمرًا بالغ الأهمية لتحقيق أقصى استفادة من نماذجك:

يهدف هذا الدليل الشامل إلى تزويدك بنظرة عامة ورؤى عملية حول كل نمط، مما يساعدك على تسخير الإمكانات الكاملة لـ YOLO26.

يُستخدم نمط التدريب (Train mode) لتدريب نموذج YOLO26 على مجموعة بيانات مخصصة. في هذا النمط، يتم تدريب النموذج باستخدام مجموعة البيانات والمعلمات الفائقة المحددة. تتضمن عملية التدريب تحسين معلمات النموذج بحيث يمكنه التنبؤ بدقة بفئات ومواقع الكائنات في الصورة. التدريب ضروري لإنشاء نماذج يمكنها التعرف على كائنات محددة ذات صلة بتطبيقك.

يُستخدم نمط التحقق (Val mode) للتحقق من نموذج YOLO26 بعد تدريبه. في هذا النمط، يتم تقييم النموذج على مجموعة تحقق لقياس دقته وأداء التعميم الخاص به. يساعد التحقق في تحديد المشكلات المحتملة مثل الفرط في التجهيز (overfitting) ويوفر مقاييس مثل متوسط الدقة المتوسطة (mean Average Precision) (mAP) لتحديد أداء النموذج كمياً. هذا النمط حاسم لضبط المعلمات الفائقة وتحسين الفعالية الكلية للنموذج.

أمثلة على التحقق من الصحة

يُستخدم نمط التنبؤ (Predict mode) لإجراء تنبؤات باستخدام نموذج YOLO26 مدرب على صور أو مقاطع فيديو جديدة. في هذا النمط، يتم تحميل النموذج من ملف نقطة تحقق، ويمكن للمستخدم توفير صور أو مقاطع فيديو لإجراء الاستدلال. يحدد النموذج الكائنات ويحدد مواقعها في وسائط الإدخال، مما يجعله جاهزًا للتطبيقات الواقعية. نمط التنبؤ هو البوابة لتطبيق نموذجك المدرب لحل المشكلات العملية.

يُستخدم نمط التصدير (Export mode) لتحويل نموذج YOLO26 إلى تنسيقات مناسبة للنشر عبر منصات وأجهزة مختلفة. يحول هذا النمط نموذج PyTorch الخاص بك إلى تنسيقات محسنة مثل ONNX أو TensorRT أو CoreML، مما يتيح النشر في بيئات الإنتاج. التصدير ضروري لدمج نموذجك مع تطبيقات برمجية أو أجهزة مختلفة، وغالبًا ما يؤدي إلى تحسينات كبيرة في الأداء.

يوسع نمط الـ track قدرات detect الكائنات في YOLO26 لـ track الكائنات عبر إطارات الفيديو أو البث المباشر. هذا النمط ذو قيمة خاصة للتطبيقات التي تتطلب تحديد الكائنات بشكل مستمر، مثل أنظمة المراقبة أو السيارات ذاتية القيادة. يطبق نمط الـ track خوارزميات متطورة مثل ByteTrack للحفاظ على هوية الكائن عبر الإطارات، حتى عندما تختفي الكائنات مؤقتًا عن الأنظار.

يقوم نمط التقييم المعياري (Benchmark mode) بتحديد سرعة ودقة تنسيقات التصدير المختلفة لـ YOLO26. يوفر هذا النمط مقاييس شاملة حول حجم النموذج، والدقة (mAP50-95 لمهام الـ detect أو accuracy_top5 للتصنيف)، ووقت الاستدلال عبر تنسيقات مختلفة مثل ONNX و OpenVINO و TensorRT. يساعدك التقييم المعياري على اختيار تنسيق التصدير الأمثل بناءً على متطلباتك المحددة للسرعة والدقة في بيئة النشر الخاصة بك.

يتضمن تدريب نموذج detect الكائنات المخصص باستخدام Ultralytics YOLO26 استخدام نمط التدريب (train mode). تحتاج إلى مجموعة بيانات منسقة بتنسيق YOLO، تحتوي على صور وملفات تعليقات توضيحية مقابلة. استخدم الأمر التالي لبدء عملية التدريب:

للحصول على إرشادات أكثر تفصيلاً، يمكنك الرجوع إلى دليل تدريب Ultralytics.

يستخدم Ultralytics YOLO26 مقاييس متنوعة أثناء عملية التحقق لتقييم أداء النموذج. وتشمل هذه:

يمكنك تشغيل الأمر التالي لبدء التحقق من الصحة:

راجع دليل التحقق من الصحة لمزيد من التفاصيل.

توفر Ultralytics YOLO26 وظيفة التصدير لتحويل نموذجك المدرب إلى تنسيقات نشر مختلفة مثل ONNX و TensorRT و CoreML والمزيد. استخدم المثال التالي لتصدير نموذجك:

يمكن العثور على خطوات تفصيلية لكل صيغة تصدير في دليل التصدير.

يُستخدم وضع المعيار (Benchmark mode) في Ultralytics YOLO26 لتحليل السرعة و الدقة لصيغ التصدير المختلفة مثل ONNX و TensorRT و OpenVINO. وهو يوفر مقاييس مثل حجم النموذج، mAP50-95 لاكتشاف الكائنات، ووقت الاستدلال عبر إعدادات الأجهزة المختلفة، مما يساعدك على اختيار التنسيق الأنسب لاحتياجات النشر الخاصة بك.

لمزيد من التفاصيل، راجع دليل القياس المعياري.

يمكن تحقيق تتبع الكائنات في الوقت الفعلي باستخدام وضع الـ track في Ultralytics YOLO26. يوسع هذا الوضع قدرات اكتشاف الكائنات لتتبعها عبر إطارات الفيديو أو البث المباشر. استخدم المثال التالي لتمكين التتبع:

للحصول على تعليمات متعمقة، قم بزيارة دليل التتبع.

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

## التحقق من صحة النموذج باستخدام Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/modes/val/

**Contents:**
- التحقق من صحة النموذج باستخدام Ultralytics YOLO
- مقدمة
- لماذا التحقق من الصحة باستخدام Ultralytics YOLO؟
  - الميزات الرئيسية لوضع Val
- أمثلة الاستخدام
- حجج للتحقق من صحة نموذج YOLO
  - مثال للتحقق من الصحة مع الحجج
- الأسئلة الشائعة
  - كيف أقوم بالتحقق من صحة نموذج YOLO26 الخاص بي باستخدام Ultralytics؟
  - ما هي المقاييس التي يمكنني الحصول عليها من التحقق من صحة نموذج YOLO26؟

التحقق من الصحة خطوة حاسمة في مسار تعلم الآلة، مما يتيح لك تقييم جودة نماذجك المدربة. يوفر وضع Val في Ultralytics YOLO26 مجموعة قوية من الأدوات والمقاييس لتقييم أداء نماذج اكتشاف الكائنات الخاصة بك. يعمل هذا الدليل كمورد كامل لفهم كيفية استخدام وضع Val بفعالية لضمان أن نماذجك دقيقة وموثوقة على حد سواء.

شاهد: Ultralytics Modes Tutorial: Validation

إليك سبب كون استخدام وضع Val في YOLO26 مفيدًا:

هذه هي الوظائف البارزة التي يوفرها وضع Val في YOLO26:

التحقق من صحة نموذج YOLO26n مدرب الدقة على مجموعة بيانات COCO8. لا توجد حاجة إلى وسيطات حيث أن model يحتفظ بالتدريب الخاص به data والوسائط كسمات للنموذج. راجع قسم الوسائط أدناه للحصول على قائمة كاملة بوسائط التحقق.

خطأ تعدد العمليات في نظام التشغيل Windows

في نظام التشغيل Windows، قد تتلقى RuntimeError عند إطلاق التحقق من الصحة كنص برمجي. أضف if __name__ == "__main__": الكتلة قبل كود التحقق الخاص بك لحل المشكلة.

عند التحقق من نماذج YOLO، يمكن ضبط العديد من الوسائط لتحسين عملية التقييم. تتحكم هذه الوسائط في جوانب مثل حجم صورة الإدخال ومعالجة الدُفعات وعتبات الأداء. فيما يلي تفصيل تفصيلي لكل وسيطة لمساعدتك على تخصيص إعدادات التحقق الخاصة بك بشكل فعال.

يلعب كل من هذه الإعدادات دورًا حيويًا في عملية التحقق، مما يسمح بتقييم قابل للتخصيص وفعال لنماذج YOLO. يمكن أن يساعد تعديل هذه المعلمات وفقًا لاحتياجاتك ومواردك الخاصة في تحقيق أفضل توازن بين الدقة والأداء.

شاهد: كيفية تصدير نتائج التحقق من النموذج بتنسيقات CSV و JSON و SQL و Polars DataFrame والمزيد

تعرض الأمثلة أدناه التحقق من نموذج YOLO باستخدام وسيطات مخصصة في Python و CLI.

تصدير مصفوفة الالتباس ConfusionMatrix

يمكنك أيضًا حفظ نتائج ConfusionMatrix بتنسيقات مختلفة باستخدام الكود المقدم.

لمزيد من التفاصيل، راجع DataExportMixin توثيق الفئة.

للتحقق من صحة نموذج YOLO26 الخاص بك، يمكنك استخدام وضع Val الذي توفره Ultralytics. على سبيل المثال، باستخدام واجهة برمجة تطبيقات python، يمكنك تحميل نموذج وتشغيل التحقق من الصحة به:

بدلاً من ذلك، يمكنك استخدام واجهة سطر الأوامر (CLI):

لمزيد من التخصيص، يمكنك تعديل العديد من الوسائط مثل imgsz, batch، و conf في كل من وضعي Python و CLI. تحقق من حجج للتحقق من صحة نموذج YOLO قسم للحصول على القائمة الكاملة للمعلمات.

يوفر التحقق من صحة نموذج YOLO26 العديد من المقاييس الرئيسية لتقييم أداء النموذج. وتشمل:

باستخدام Python API، يمكنك الوصول إلى هذه المقاييس على النحو التالي:

لتقييم كامل للأداء، من الضروري مراجعة جميع هذه المقاييس. لمزيد من التفاصيل، راجع الميزات الرئيسية لوضع Val.

يوفر استخدام Ultralytics YOLO للتحقق من الصحة العديد من المزايا:

تضمن هذه المزايا تقييم نماذجك بدقة ويمكن تحسينها للحصول على نتائج فائقة. تعرف على المزيد حول هذه المزايا في قسم لماذا تتحقق من الصحة باستخدام Ultralytics YOLO.

نعم، يمكنك التحقق من صحة نموذج YOLO26 الخاص بك باستخدام مجموعة بيانات مخصصة. حدد الـ data وسيطة مع مسار ملف تكوين مجموعة البيانات الخاصة بك. يجب أن يتضمن هذا الملف المسار إلى بيانات التحقق.

يتم إجراء التحقق باستخدام أسماء الفئات الخاصة بالنموذج، والتي يمكنك عرضها باستخدام model.names، والتي قد تختلف عن تلك المحددة في ملف تكوين مجموعة البيانات.

لمزيد من الخيارات القابلة للتخصيص أثناء التحقق، راجع قسم مثال التحقق مع الوسائط.

لحفظ نتائج التحقق في ملف JSON، يمكنك تعيين save_json إلى True عند تشغيل التحقق. يمكن القيام بذلك في كل من Python API و CLI.

هذه الوظيفة مفيدة بشكل خاص لمزيد من التحليل أو التكامل مع الأدوات الأخرى. تحقق من وسائط التحقق من نموذج YOLO لمزيد من التفاصيل.

**Examples:**

Example 1 (python):
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

Example 2 (unknown):
```unknown
yolo detect val model=yolo26n.pt      # val official model
yolo detect val model=path/to/best.pt # val custom model
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")

# Customize validation settings
metrics = model.val(data="coco8.yaml", imgsz=640, batch=16, conf=0.25, iou=0.7, device="0")
```

Example 4 (unknown):
```unknown
yolo val model=yolo26n.pt data=coco8.yaml imgsz=640 batch=16 conf=0.25 iou=0.7 device=0
```

---

## الرئيسية

**URL:** https://docs.ultralytics.com/ar/

**Contents:**
- الرئيسية
- من أين أبدأ؟
- YOLO: لمحة تاريخية موجزة
- تراخيص YOLO: كيف يتم ترخيص Ultralytics YOLO؟
- تطور اكتشاف الأجسام
- الأسئلة الشائعة
  - ما هو Ultralytics YOLO وكيف يحسن من اكتشاف الكائنات؟
  - كيف يمكنني البدء في تثبيت وإعداد YOLO؟
  - كيف يمكنني تدريب نموذج YOLO مخصص على مجموعة البيانات الخاصة بي؟
  - ما هي خيارات الترخيص المتاحة لـ Ultralytics YOLO؟

نقدم Ultralytics YOLO26، أحدث إصدار من نموذج الكشف عن الكائنات في الوقت الفعلي وتجزئة الصور الشهير. تم بناء YOLO26 على أساس التطورات في التعلم العميق ورؤية الكمبيوتر، ويتميز باستدلال خالٍ من NMS من البداية إلى النهاية ونشر مُحسّن على الأجهزة الطرفية. تصميمه المبسّط يجعله مناسبًا لمجموعة متنوعة من التطبيقات وقابلاً للتكيف بسهولة مع منصات الأجهزة المختلفة، من الأجهزة الطرفية إلى واجهات برمجة تطبيقات السحابة. لأحمال عمل الإنتاج المستقرة، يوصى بكل من YOLO26 وYOLO11.

استكشف وثائق Ultralytics، وهي مصدر شامل مصمم لمساعدتك على فهم ميزاتها وقدراتها واستخدامها. سواء كنت ممارسًا متمرسًا في التعلم الآلي أو جديدًا في هذا المجال، يهدف هذا المركز إلى زيادة إمكانات YOLO في مشاريعك.

تثبيت ultralytics باستخدام pip وابدأ العمل في دقائق لتدريب نموذج YOLO

توقع على الصور ومقاطع الفيديو والبث الجديدة باستخدام YOLO

قم بتدريب نموذج YOLO جديد على مجموعة البيانات المخصصة الخاصة بك من البداية أو قم بتحميله والتدريب عليه على نموذج مُدرَّب مسبقًا

استكشف مهام رؤية الكمبيوتر

اكتشف مهام YOLO مثل detect و segment و classify و pose و OBB و track

اكتشف أحدث نماذج Ultralytics YOLO26 مع استدلال خالٍ من NMS وتحسين للأجهزة الطرفية.

SAM 3: segment أي شيء بالمفاهيم 🚀 جديد

أحدث إصدار من SAM 3 من Meta مع segment المفاهيم القابل للتوجيه - segment جميع الكائنات باستخدام موجهات نصية أو صور أمثلة

مفتوح المصدر، AGPL-3.0

تقدم Ultralytics ترخيصين لـ YOLO: AGPL-3.0 و Enterprise. استكشف YOLO على GitHub.

شاهد: كيفية تدريب نموذج YOLO11 على مجموعة البيانات المخصصة الخاصة بك في Google Colab.

YOLO ‏(You Only Look Once)، وهو نموذج شائع لاكتشاف الكائنات وتقسيم الصور، تم تطويره بواسطة جوزيف ريدمون وعلي فرهادي في جامعة واشنطن. تم إطلاق YOLO في عام 2015، واكتسب شعبية بسبب سرعته ودقته العالية.

تقدم Ultralytics خيارين للترخيص لاستيعاب حالات الاستخدام المتنوعة:

تم تصميم استراتيجية الترخيص لدينا لضمان عودة أي تحسينات على مشاريعنا مفتوحة المصدر إلى المجتمع. نحن نؤمن بالمصدر المفتوح، ومهمتنا هي ضمان إمكانية استخدام مساهماتنا وتوسيعها بطرق تفيد الجميع.

تطور الكشف عن الكائنات بشكل كبير على مر السنين، من تقنيات رؤية الكمبيوتر التقليدية إلى نماذج التعلم العميق المتقدمة. كانت عائلة نماذج YOLO في طليعة هذا التطور، حيث دفعت باستمرار حدود الممكن في الكشف عن الكائنات في الوقت الفعلي.

يعالج نهج YOLO الفريد اكتشاف الكائنات كمشكلة انحدار واحدة، ويتوقع مربعات الإحاطة واحتمالات الفئة مباشرة من الصور الكاملة في تقييم واحد. لقد جعلت هذه الطريقة الثورية نماذج YOLO أسرع بكثير من الكاشفات السابقة ذات المرحلتين مع الحفاظ على دقة عالية.

مع كل إصدار جديد، قدم YOLO تحسينات معمارية وتقنيات مبتكرة عززت الأداء عبر مقاييس مختلفة. يواصل YOLO26 هذا التقليد من خلال دمج أحدث التطورات في أبحاث رؤية الكمبيوتر، ويتميز باستدلال خالٍ من NMS من البداية إلى النهاية ونشر مُحسّن على الأجهزة الطرفية للتطبيقات الواقعية.

Ultralytics YOLO هي سلسلة YOLO (You Only Look Once) الشهيرة للكشف عن الكائنات في الوقت الفعلي وتجزئة الصور. يعتمد أحدث نموذج، YOLO26، على الإصدارات السابقة من خلال تقديم استدلال خالٍ من NMS من البداية إلى النهاية ونشر مُحسّن على الأجهزة الطرفية. يدعم YOLO مهام الذكاء الاصطناعي البصري المتنوعة مثل detect، وsegment، وتقدير الوضعيات، وtrack، والتصنيف. تضمن بنيته الفعالة سرعة ودقة ممتازتين، مما يجعله مناسبًا لمجموعة متنوعة من التطبيقات، بما في ذلك الأجهزة الطرفية وواجهات برمجة تطبيقات السحابة.

البدء في استخدام YOLO سريع ومباشر. يمكنك تثبيت حزمة Ultralytics باستخدام pip والبدء في غضون دقائق. إليك أمر تثبيت أساسي:

للحصول على دليل شامل خطوة بخطوة، قم بزيارة صفحة البدء السريع الخاصة بنا. سيساعدك هذا المورد في تعليمات التثبيت والإعداد الأولي وتشغيل النموذج الأول الخاص بك.

يتضمن تدريب نموذج YOLO مخصص على مجموعة البيانات الخاصة بك بعض الخطوات التفصيلية:

إليك مثال على التعليمات البرمجية لمهمة الكشف عن الكائنات:

مثال على التدريب لمهمة الكشف عن الكائنات

للحصول على شرح تفصيلي، راجع دليل تدريب نموذج الخاص بنا، والذي يتضمن أمثلة ونصائح لتحسين عملية التدريب.

تقدم Ultralytics خيارين للترخيص لـ YOLO:

للمزيد من التفاصيل، يرجى زيارة صفحة التراخيص الخاصة بنا.

يدعم Ultralytics YOLO تتبعًا فعالًا وقابلاً للتخصيص لأجسام متعددة. للاستفادة من إمكانات التتبع، يمكنك استخدام الأمر yolo track الأمر، كما هو موضح أدناه:

مثال لتتبع الأجسام على مقطع فيديو

للحصول على دليل مفصل حول إعداد وتشغيل تتبع الكائنات، راجع وثائق وضع التتبع (Track Mode) الخاص بنا، والذي يشرح التكوين والتطبيقات العملية في سيناريوهات الوقت الفعلي.

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

## الكشف عن الكائنات

**URL:** https://docs.ultralytics.com/ar/tasks/detect/

**Contents:**
- الكشف عن الكائنات
- النماذج
- تدريب
  - تنسيق مجموعة البيانات
- التحقق
- توقع
- تصدير
- الأسئلة الشائعة
  - كيف أقوم بتدريب نموذج YOLO26 على مجموعة البيانات المخصصة الخاصة بي؟
  - ما هي النماذج المدربة مسبقًا المتوفرة في YOLO26؟

الكشف عن الأجسام هي مهمة تتضمن تحديد موقع وفئة الأجسام في صورة أو دفق فيديو.

ناتج الكشف عن الأجسام هو مجموعة من المربعات المحيطة التي تحيط بالأجسام في الصورة، جنبًا إلى جنب مع تسميات الفئات وعلامات الثقة لكل مربع. يعد الكشف عن الأجسام خيارًا جيدًا عندما تحتاج إلى تحديد الأجسام محل الاهتمام في مشهد ما، ولكن لا تحتاج إلى معرفة مكان الجسم بالضبط أو شكله الدقيق.

شاهد: اكتشاف الكائنات باستخدام نموذج Ultralytics YOLO المُدرب مسبقًا.

نماذج YOLO26 detect هي نماذج YOLO26 الافتراضية، أي، yolo26n.pt، ويتم تدريبها مسبقًا على COCO.

نماذج YOLO26 detect المدربة مسبقًا معروضة هنا. نماذج detect و segment و Pose مدربة مسبقًا على مجموعة بيانات COCO، بينما نماذج classify مدربة مسبقًا على مجموعة بيانات ImageNet.

يتم تنزيل النماذج تلقائيًا من أحدث إصدار Ultralytics عند الاستخدام الأول.

درب YOLO26n على مجموعة بيانات COCO8 لمدة 100 حقبة تدريبية بحجم صورة 640. للحصول على قائمة كاملة بالوسائط المتاحة، راجع صفحة التكوين.

يمكن العثور على تنسيق مجموعة بيانات اكتشاف YOLO بالتفصيل في دليل مجموعة البيانات. لتحويل مجموعة البيانات الحالية الخاصة بك من تنسيقات أخرى (مثل COCO وما إلى ذلك) إلى تنسيق YOLO، يرجى استخدام أداة JSON2YOLO بواسطة Ultralytics.

التحقق من صحة نموذج YOLO26n المدرب الدقة على مجموعة بيانات COCO8. لا توجد حاجة إلى وسيطات حيث أن model يحتفظ بالتدريب الخاص به data والوسائط كسمات للنموذج.

استخدم نموذج YOLO26n مدربًا لتشغيل التنبؤات على الصور.

اطلع على التفاصيل الكاملة predict لأوضاع التشغيل في صفحة توقع التنبؤ.

صدّر نموذج YOLO26n إلى صيغة مختلفة مثل ONNX، CoreML، إلخ.

تتوفر تنسيقات تصدير YOLO26 في الجدول أدناه. يمكنك التصدير إلى أي تنسيق باستخدام format الوسيطة، أي format='onnx' أو format='engine'. يمكنك التنبؤ أو التحقق مباشرة على النماذج المصدرة، أي، yolo predict model=yolo26n.onnx. يتم عرض أمثلة الاستخدام لنموذجك بعد اكتمال التصدير.

اطلع على التفاصيل الكاملة export التفاصيل في تصدير التنبؤ.

يتضمن تدريب نموذج YOLO26 على مجموعة بيانات مخصصة عدة خطوات:

لخيارات التكوين التفصيلية، قم بزيارة صفحة التكوين.

تقدم Ultralytics YOLO26 نماذج متنوعة مدربة مسبقًا لاكتشاف الكائنات، والتجزئة، وتقدير الوضعيات. هذه النماذج مدربة مسبقًا على مجموعة بيانات COCO أو ImageNet لمهام التصنيف. فيما يلي بعض النماذج المتاحة:

للحصول على قائمة تفصيلية ومقاييس الأداء، راجع قسم النماذج.

للتحقق من دقة نموذج YOLO26 المدرب الخاص بك، يمكنك استخدام .val() الطريقة في python أو yolo detect val الأمر في CLI. سيوفر هذا مقاييس مثل mAP50-95 و mAP50 والمزيد.

لمزيد من تفاصيل التحقق، قم بزيارة صفحة Val.

تسمح Ultralytics YOLO26 بتصدير النماذج إلى تنسيقات متنوعة مثل ONNX، TensorRT، CoreML، والمزيد لضمان التوافق عبر مختلف المنصات والأجهزة.

تحقق من القائمة الكاملة للتنسيقات المدعومة والتعليمات على صفحة Export.

صُممت Ultralytics YOLO26 لتقديم أداء متطور لاكتشاف الكائنات، والتجزئة، وتقدير الوضعيات. فيما يلي بعض المزايا الرئيسية:

استكشف مدونتنا لحالات الاستخدام وقصص النجاح التي تعرض YOLO26 عمليًا.

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

## تتبع الأجسام المتعددة باستخدام Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/modes/track/

**Contents:**
- تتبع الأجسام المتعددة باستخدام Ultralytics YOLO
- لماذا تختار Ultralytics YOLO لتتبع الأجسام؟
- تطبيقات واقعية
- لمحة عن الميزات
- أدوات التتبع المتاحة
- تتبع
- التكوين
  - وسائط تتبع
  - تحديد المتعقب
  - وسائط التتبع

يُعد تتبع الأجسام في مجال تحليلات الفيديو مهمة بالغة الأهمية لا تقتصر على تحديد موقع الأجسام وفئتها داخل الإطار فحسب، بل تحافظ أيضًا على مُعرّف فريد لكل جسم يتم اكتشافه مع تقدم الفيديو. التطبيقات لا حدود لها — بدءًا من المراقبة والأمن وصولًا إلى تحليلات الرياضة في الوقت الفعلي.

يتوافق الإخراج من أدوات التتبع Ultralytics مع اكتشاف الكائنات القياسي ولكنه يتمتع بالقيمة المضافة لمعرفات الكائنات. هذا يجعل من السهل تتبع الكائنات في تدفقات الفيديو وإجراء تحليلات لاحقة. إليك سبب وجوب التفكير في استخدام Ultralytics YOLO لتلبية احتياجاتك في تتبع الكائنات:

شاهد: اكتشاف الأجسام وتتبعها باستخدام Ultralytics YOLO.

تعمل Ultralytics YOLO على توسيع ميزات اكتشاف الأجسام الخاصة بها لتوفير تتبع قوي ومتعدد الاستخدامات للأجسام:

تدعم Ultralytics YOLO خوارزميات التتبع التالية. يمكن تفعيلها عن طريق تمرير ملف تكوين YAML ذي الصلة مثل tracker=tracker_type.yaml:

أداة التتبع الافتراضية هي BoT-SORT.

لتشغيل المتتبع على تدفقات الفيديو، استخدم نموذج Detect أو Segment أو Pose مدربًا مثل YOLO26n أو YOLO26n-seg أو YOLO26n-pose.

كما هو موضح في الاستخدام أعلاه، يتوفر التتبع لجميع نماذج Detect و Segment و Pose التي يتم تشغيلها على مقاطع الفيديو أو مصادر البث.

تشارك تهيئة التتبع الخصائص مع وضع التوقع (Predict)، مثل conf, iou، و show. لمزيد من التكوينات، ارجع إلى توقع صفحة النموذج.

تتيح لك Ultralytics أيضًا استخدام ملف تكوين مُعدَّل لأداة التتبع. للقيام بذلك، ما عليك سوى عمل نسخة من ملف تكوين أداة التتبع (على سبيل المثال، custom_tracker.yaml) من ultralytics/cfg/trackers وقم بتعديل أي تكوينات (باستثناء tracker_type) حسب احتياجاتك.

راجع قسم وسيطات التعقب للحصول على وصف تفصيلي لكل معلمة.

يمكن ضبط بعض سلوكيات التتبع بدقة عن طريق تعديل ملفات تكوين YAML الخاصة بكل خوارزمية تتبع. تحدد هذه الملفات معلمات مثل العتبات والمخازن المؤقتة ومنطق المطابقة:

يوفر الجدول التالي وصفًا لكل معلمة:

معلومات حول عتبة أداة التتبع

إذا كانت درجة الثقة الخاصة بالكشف أقل من track_high_thresh، لن يقوم المتعقب بتحديث هذا الكائن، مما يؤدي إلى عدم وجود مسارات نشطة.

بشكل افتراضي، يتم إيقاف تشغيل ReID لتقليل النفقات العامة للأداء. تمكينها بسيط - فقط قم بتعيين with_reid: True في تكوين المتعقب: يمكنك أيضًا تخصيص الـ model يستخدم لـ ReID، مما يسمح لك بالمفاضلة بين الدقة والسرعة اعتمادًا على حالة الاستخدام الخاصة بك:

للحصول على أداء أفضل، خاصة عند استخدام نموذج تصنيف منفصل لـ ReID، يمكنك تصديره إلى واجهة خلفية أسرع مثل TensorRT:

تصدير نموذج ReID إلى TensorRT

بمجرد التصدير، يمكنك الإشارة إلى مسار نموذج TensorRT في إعدادات المتعقب الخاص بك، وسيتم استخدامه لـ ReID أثناء التتبع.

شاهد: كيفية بناء تتبع تفاعلي للكائنات باستخدام Ultralytics YOLO | انقر للاقتصاص والعرض ⚡

إليك برنامج python نصي يستخدم OpenCV (cv2) و YOLO26 لتشغيل تتبع الكائنات على إطارات الفيديو. يفترض هذا السكريبت وجود الحزم الضرورية (opencv-python و ultralytics) مثبتة بالفعل. ال persist=True تخبر الوسيطة المتعقب أن الصورة أو الإطار الحالي هو التالي في التسلسل، وتتوقع مسارات من الصورة السابقة في الصورة الحالية.

حلقة تكرار (for-loop) متدفقة مع التتبع

يرجى ملاحظة التغيير من model(frame) إلى model.track(frame)، مما يتيح تتبع الكائنات بدلاً من الاكتشاف البسيط. سيقوم هذا البرنامج النصي المعدل بتشغيل المتعقب على كل إطار من الفيديو، وتصور النتائج، وعرضها في نافذة. يمكن الخروج من الحلقة بالضغط على 'q'.

يمكن أن يوفر تصور مسارات الكائنات عبر الإطارات المتتالية رؤى قيمة حول أنماط الحركة وسلوك الكائنات المكتشفة داخل الفيديو. ومع Ultralytics YOLO26، يعد رسم هذه المسارات عملية سلسة وفعالة.

في المثال التالي، نوضح كيفية الاستفادة من قدرات التتبع في YOLO26 لرسم حركة الكائنات المكتشفة عبر إطارات فيديو متعددة. يتضمن هذا السكريبت فتح ملف فيديو، وقراءته إطارًا بإطار، واستخدام نموذج YOLO لتحديد وتتبع الكائنات المختلفة. من خلال الاحتفاظ بالنقاط المركزية لصناديق الإحاطة المكتشفة وربطها، يمكننا رسم خطوط تمثل المسارات التي تتبعها الكائنات المتتبعة.

رسم المسارات عبر إطارات فيديو متعددة

يوفر التتبع متعدد الخيوط القدرة على تشغيل تتبع الكائنات على تدفقات فيديو متعددة في وقت واحد. هذا مفيد بشكل خاص عند التعامل مع مدخلات فيديو متعددة، مثل من كاميرات مراقبة متعددة، حيث يمكن للمعالجة المتزامنة أن تعزز الكفاءة والأداء بشكل كبير.

في برنامج python النصي المتوفر، نستخدم وحدة python threading لتشغيل مثيلات متعددة من المتعقب في وقت واحد. كل مؤشر ترابط مسؤول عن تشغيل المتعقب على ملف فيديو واحد، وتعمل جميع مؤشرات الترابط في وقت واحد في الخلفية.

لضمان حصول كل مؤشر ترابط على المعلمات الصحيحة (ملف الفيديو، والنموذج المراد استخدامه وفهرس الملف)، فإننا نحدد دالة run_tracker_in_thread تقبل هذه المعلمات وتحتوي على حلقة التتبع الرئيسية. تقرأ هذه الدالة الفيديو إطارًا تلو الآخر، وتشغل المتعقب، وتعرض النتائج.

يتم استخدام نموذجين مختلفين في هذا المثال: yolo26n.pt و yolo26n-seg.pt، يتتبع كل منهما كائنات في ملف فيديو مختلف. يتم تحديد ملفات الفيديو في SOURCES.

في daemon=True المعلمة في threading.Thread يعني أن هذه الخيوط سيتم إغلاقها بمجرد انتهاء البرنامج الرئيسي. ثم نبدأ الخيوط بـ start() ونستخدم join() لجعل الخيط الرئيسي ينتظر حتى تنتهي خيوط المتعقب.

أخيرًا، بعد أن تكمل جميع الخيوط مهمتها، يتم إغلاق النوافذ التي تعرض النتائج باستخدام cv2.destroyAllWindows().

تنفيذ تتبع متعدد الخيوط

يمكن بسهولة توسيع هذا المثال للتعامل مع المزيد من ملفات الفيديو والنماذج عن طريق إنشاء المزيد من الخيوط وتطبيق نفس المنهجية.

هل أنت ماهر في تتبع الأجسام المتعددة وهل قمت بتنفيذ أو تكييف خوارزمية تتبع بنجاح باستخدام Ultralytics YOLO؟ نحن ندعوك للمساهمة في قسم المتعقبات الخاص بنا في ultralytics/cfg/trackers! يمكن أن تكون تطبيقاتك وحلولك الواقعية لا تقدر بثمن للمستخدمين الذين يعملون على مهام التتبع.

من خلال المساهمة في هذا القسم، فإنك تساعد في توسيع نطاق حلول التتبع المتاحة داخل إطار عمل Ultralytics YOLO، مما يضيف طبقة أخرى من الوظائف والأدوات المساعدة للمجتمع.

لبدء مساهمتك، يرجى الرجوع إلى دليل المساهمة للحصول على إرشادات شاملة حول إرسال طلب سحب (PR) 🛠️. نحن متحمسون لرؤية ما تقدمه!

معًا، دعنا نعزز قدرات التتبع في النظام البيئي Ultralytics YOLO 🙏!

يتضمن تتبع الأجسام المتعددة في تحليلات الفيديو تحديد الأجسام والحفاظ على مُعرّف فريد لكل جسم يتم اكتشافه عبر إطارات الفيديو. يدعم Ultralytics YOLO ذلك من خلال توفير تتبع في الوقت الفعلي مع مُعرّفات الأجسام، مما يسهل مهام مثل المراقبة الأمنية والتحليلات الرياضية. يستخدم النظام أدوات تتبع مثل BoT-SORT و ByteTrack، والتي يمكن تهيئتها عبر ملفات YAML.

يمكنك تكوين متتبع مخصص عن طريق نسخ ملف تكوين متتبع موجود (على سبيل المثال، custom_tracker.yaml) من دليل تكوين متتبعات Ultralytics وتعديل المعلمات حسب الحاجة، باستثناء tracker_type. استخدم هذا الملف في نموذج التتبع الخاص بك كما يلي:

لتشغيل تتبع الكائنات على عدة تدفقات فيديو في وقت واحد، يمكنك استخدام وحدة threading python. سيتعامل كل مؤشر ترابط مع دفق فيديو منفصل. إليك مثال على كيفية إعداد ذلك:

تتبع الأجسام المتعددة باستخدام Ultralytics YOLO له تطبيقات عديدة، بما في ذلك:

تستفيد هذه التطبيقات من قدرة Ultralytics YOLO على معالجة مقاطع الفيديو ذات معدل الإطارات العالي في الوقت الفعلي بدقة استثنائية.

لتصور مسارات الكائنات عبر إطارات فيديو متعددة، يمكنك استخدام ميزات التتبع الخاصة بنموذج YOLO جنبًا إلى جنب مع OpenCV لرسم مسارات الكائنات التي تم الكشف عنها. إليك مثال لبرنامج نصي يوضح ذلك:

رسم المسارات عبر إطارات فيديو متعددة

سيقوم هذا البرنامج النصي برسم خطوط التتبع التي تعرض مسارات حركة الكائنات التي يتم تتبعها بمرور الوقت، مما يوفر رؤى قيمة حول سلوك الكائن وأنماطه.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load an official or custom model
model = YOLO("yolo26n.pt")  # Load an official Detect model
model = YOLO("yolo26n-seg.pt")  # Load an official Segment model
model = YOLO("yolo26n-pose.pt")  # Load an official Pose model
model = YOLO("path/to/best.pt")  # Load a custom-trained model

# Perform tracking with the model
results = model.track("https://youtu.be/LNwODJXcvt4", show=True)  # Tracking with default tracker
results = model.track("https://youtu.be/LNwODJXcvt4", show=True, tracker="bytetrack.yaml")  # with ByteTrack
```

Example 2 (julia):
```julia
# Perform tracking with various models using the command line interface
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4"      # Official Detect model
yolo track model=yolo26n-seg.pt source="https://youtu.be/LNwODJXcvt4"  # Official Segment model
yolo track model=yolo26n-pose.pt source="https://youtu.be/LNwODJXcvt4" # Official Pose model
yolo track model=path/to/best.pt source="https://youtu.be/LNwODJXcvt4" # Custom trained model

# Track using ByteTrack tracker
yolo track model=path/to/best.pt source="https://youtu.be/LNwODJXcvt4" tracker="bytetrack.yaml"
```

Example 3 (python):
```python
from ultralytics import YOLO

# Configure the tracking parameters and run the tracker
model = YOLO("yolo26n.pt")
results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.1, iou=0.7, show=True)
```

Example 4 (julia):
```julia
# Configure tracking parameters and run the tracker using the command line interface
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4" conf=0.1 iou=0.7 show
```

---

## تثبيت Ultralytics

**URL:** https://docs.ultralytics.com/ar/quickstart/

**Contents:**
- تثبيت Ultralytics
  - صورة Conda Docker
- تثبيت الخادم بدون واجهة رسومية
- التثبيت المتقدم
- استخدام Ultralytics مع CLI
- استخدام Ultralytics مع Python
- إعدادات Ultralytics
  - فحص الإعدادات
  - تعديل الإعدادات
  - فهم الإعدادات

تقدم Ultralytics مجموعة متنوعة من طرق التثبيت، بما في ذلك pip و conda و Docker. يمكنك تثبيت YOLO عبر ultralytics حزمة pip لأحدث إصدار مستقر، أو عن طريق استنساخ مستودع Ultralytics GitHub للحصول على أحدث إصدار. Docker هو أيضًا خيار لتشغيل الحزمة في حاوية معزولة، مما يتجنب التثبيت المحلي.

شاهد: دليل البدء السريع لـ Ultralytics YOLO

تثبيت أو تحديث ultralytics باستخدام pip عن طريق تشغيل pip install -U ultralytics. لمزيد من التفاصيل حول ultralytics ، قم بزيارة فهرس حزمة python ‏(PyPI).

يمكنك أيضًا تثبيت ultralytics مباشرة من مستودع Ultralytics GitHub. يمكن أن يكون هذا مفيدًا إذا كنت تريد أحدث إصدار تطوير. تأكد من تثبيت أداة سطر الأوامر Git، ثم قم بتشغيل:

يمكن استخدام Conda كبديل لـ pip في إدارة الحزم. لمزيد من التفاصيل، قم بزيارة Anaconda. يتوفر مستودع Ultralytics لتحديث حزمة conda على GitHub.

إذا كنت تقوم بالتثبيت في بيئة CUDA، فمن الأفضل تثبيت ultralytics, pytorch، و pytorch-cuda في نفس الأمر. يتيح ذلك لمدير حزم conda حل أي تعارضات. بدلاً من ذلك، قم بتثبيت pytorch-cuda آخر ما يتم تجاوزه خاص بوحدة المعالجة المركزية CPU pytorch حزمة CPU إذا لزم الأمر.

تتوفر أيضًا صور Ultralytics Conda Docker على Docker Hub. تعتمد هذه الصور على Miniconda3 وتوفر طريقة مباشرة لبدء استخدام ultralytics في بيئة Conda.

استنسخ (Clone) مستودع مستودع Ultralytics GitHub إذا كنت مهتمًا بالمساهمة في التطوير أو ترغب في تجربة أحدث التعليمات البرمجية المصدر. بعد الاستنساخ، انتقل إلى الدليل وقم بتثبيت الحزمة في وضع قابل للتحرير -e باستخدام pip.

استخدم Docker لتنفيذ ultralytics في حاوية معزولة، مما يضمن أداءً ثابتًا عبر البيئات المختلفة. عن طريق اختيار أحد ultralytics الرسمية من Docker Hub، يمكنك تجنب تعقيد التثبيت المحلي والوصول إلى بيئة عمل تم التحقق منها. تقدم Ultralytics خمس صور Docker رئيسية مدعومة، تم تصميم كل منها لتحقيق توافق وكفاءة عالية:

فيما يلي أوامر الحصول على أحدث صورة وتنفيذها:

يقوم الأمر أعلاه بتهيئة حاوية Docker بأحدث ultralytics صورة. تحدد العلامة -it تعيّن العلامات TTY زائفًا وتحافظ على فتح stdin، مما يسمح بالتفاعل مع الحاوية. إن --ipc=host مساحة اسم IPC (الاتصال بين العمليات) للمضيف، وهو أمر ضروري لمشاركة الذاكرة بين العمليات. تتيح العلامة --gpus all تتيح العلامة الوصول إلى جميع وحدات معالجة الرسوميات (GPUs) المتاحة داخل الحاوية، وهو أمر بالغ الأهمية للمهام التي تتطلب حسابات GPU.

ملاحظة: للعمل مع الملفات الموجودة على جهازك المحلي داخل الحاوية، استخدم وحدات تخزين Docker لتركيب دليل محلي في الحاوية:

استبدل /path/on/host مع مسار الدليل على جهازك المحلي، و /path/in/container بالمسار المطلوب داخل حاوية Docker.

لاستخدام Docker المتقدم، استكشف دليل Ultralytics Docker.

انظر إلى ultralytics pyproject.toml ملف للحصول على قائمة بالتبعيات. لاحظ أن جميع الأمثلة أعلاه تقوم بتثبيت جميع التبعيات المطلوبة.

تختلف متطلبات PyTorch حسب نظام التشغيل ومتطلبات CUDA، لذا قم بتثبيت PyTorch أولاً باتباع الإرشادات الموجودة في PyTorch.

لبيئات الخادم التي لا تحتوي على شاشة عرض (مثل الأجهزة الافتراضية السحابية، حاويات Docker، مسارات CI/CD)، استخدم ultralytics-opencv-headless الحزمة. هذا مطابق للحزمة القياسية ultralytics ولكنه يعتمد على opencv-python-headless بدلاً من opencv-python، لتجنب تبعيات واجهة المستخدم الرسومية غير الضرورية ومخاطر libGL الأخطاء.

تثبيت بدون واجهة رسومية

توفر كلتا الحزمتين نفس الوظائف وواجهة برمجة التطبيقات. يستبعد الإصدار بدون واجهة رسومية ببساطة مكونات واجهة المستخدم الرسومية لـ OpenCV التي تتطلب مكتبات عرض.

بينما تغطي طرق التثبيت القياسية معظم حالات الاستخدام، قد تحتاج إلى إعداد أكثر تخصيصًا للتطوير أو التكوينات المخصصة.

إذا كنت بحاجة إلى تعديلات مخصصة دائمة، يمكنك عمل نسخة متفرعة (fork) من مستودع Ultralytics، وإجراء تغييرات على pyproject.toml أو التعليمات البرمجية الأخرى، والتثبيت من نسختك المتفرعة.

استنسخ المستودع محليًا، عدّل الملفات حسب الحاجة، وثبّت في الوضع القابل للتعديل.

هذا النهج مفيد للتطوير أو اختبار التغييرات المحلية قبل الالتزام بها.

حدد نسخة مخصصة من Ultralytics في ملفك requirements.txt لضمان تثبيتات متسقة عبر فريقك.

تثبيت التبعيات من الملف:

تتيح واجهة سطر الأوامر (CLI) الخاصة بـ Ultralytics أوامر بسيطة من سطر واحد دون الحاجة إلى بيئة Python. لا تتطلب CLI أي تخصيص أو كود Python؛ قم بتشغيل جميع المهام من الجهاز الطرفي باستخدام yolo الأمر. لمزيد من المعلومات حول استخدام YOLO من سطر الأوامر، راجع دليل CLI.

تستخدم Ultralytics yolo الأوامر بناء الجملة التالي:

اطلع على جميع ARGS في دليل التهيئة الكامل أو باستخدام yolo cfg أمر سطر الأوامر CLI.

تدريب نموذج الكشف لـ 10 حقبات بمعدل تعلم أولي قدره 0.01:

توقع فيديو YouTube باستخدام نموذج تجزئة مدرب مسبقًا بحجم صورة 320:

التحقق من صحة نموذج الكشف المدرب مسبقًا بحجم دفعة 1 وحجم صورة 640:

تصدير نموذج تصنيف YOLO26n إلى تنسيق ONNX بحجم صورة 224x128 (لا يتطلب TASK):

عد الكائنات في مقطع فيديو أو بث مباشر باستخدام YOLO26:

مراقبة تمارين اللياقة البدنية باستخدام نموذج وضعيات YOLO26:

استخدم YOLO26 لعد الكائنات في قائمة انتظار أو منطقة محددة:

إجراء الكشف عن الكائنات، أو تجزئة المثيلات، أو تقدير الوضعية في متصفح الويب باستخدام Streamlit:

قم بتشغيل أوامر خاصة لرؤية الإصدار، وعرض الإعدادات، وتشغيل الفحوصات، والمزيد:

يجب تمرير الوسائط كـ arg=value أزواج، مفصولة بعلامة يساوي = إشارة ومحددة بمسافات. لا تستخدم -- بادئات الوسائط أو الفواصل , بين الوسائط.

توفر واجهة Python الخاصة بـ Ultralytics YOLO تكاملًا سلسًا في مشاريع Python، مما يسهل تحميل وتشغيل ومعالجة مخرجات النموذج. تم تصميم واجهة Python ببساطة، وتسمح للمستخدمين بتنفيذ الكشف عن الأجسام والتجزئة والتصنيف بسرعة. وهذا يجعل واجهة YOLO Python أداة لا تقدر بثمن لدمج هذه الوظائف في مشاريع Python.

على سبيل المثال، يمكن للمستخدمين تحميل نموذج وتدريبه وتقييم أدائه وتصديره إلى تنسيق ONNX ببضعة أسطر فقط من التعليمات البرمجية. استكشف دليل Python لمعرفة المزيد حول استخدام YOLO داخل مشاريع Python الخاصة بك.

تتضمن مكتبة Ultralytics SettingsManager للحصول على تحكم دقيق في التجارب، مما يسمح للمستخدمين بالوصول إلى الإعدادات وتعديلها بسهولة. يتم تخزين هذه الإعدادات في ملف JSON داخل دليل تكوين المستخدم الخاص بالبيئة، ويمكن عرضها أو تعديلها في بيئة Python أو عبر واجهة سطر الأوامر (CLI).

لعرض التكوين الحالي لإعداداتك:

استخدم Python لعرض إعداداتك عن طريق استيراد settings من الوحدة ultralytics الوحدة النمطية. اطبع وأرجع الإعدادات بهذه الأوامر:

تتيح لك واجهة سطر الأوامر التحقق من إعداداتك باستخدام:

تسهل Ultralytics تعديل الإعدادات بالطرق التالية:

في Python، استخدم update على الكائن settings كائن:

لتعديل الإعدادات باستخدام واجهة سطر الأوامر:

يستعرض الجدول أدناه الإعدادات القابلة للتعديل داخل Ultralytics، بما في ذلك القيم النموذجية وأنواع البيانات والأوصاف.

أعد النظر في هذه الإعدادات كلما تقدمت في المشاريع أو التجارب لضمان التكوين الأمثل.

لتثبيت Ultralytics باستخدام pip:

يقوم هذا بتثبيت أحدث إصدار ثابت من ultralytics حزمة من PyPIلتثبيت نسخة التطوير مباشرة من GitHub:

تأكد من تثبيت أداة سطر الأوامر Git على نظامك.

نعم، قم بتثبيت Ultralytics YOLO باستخدام conda مع:

تُعد هذه الطريقة بديلاً رائعًا لـ pip، مما يضمن التوافق مع الحزم الأخرى. لبيئات CUDA، قم بالتثبيت ultralytics, pytorch، و pytorch-cuda معًا لحل النزاعات:

لمزيد من التعليمات، راجع دليل البدء السريع لـ Conda.

توفر Docker بيئة معزولة ومتسقة لـ Ultralytics YOLO، مما يضمن أداءً سلسًا عبر الأنظمة وتجنب تعقيدات التثبيت المحلية. تتوفر صور Docker الرسمية على Docker Hub، مع وجود متغيرات لـ GPU و CPU و ARM64 و NVIDIA Jetson و Conda. لسحب وتشغيل أحدث صورة:

للحصول على تعليمات Docker مفصلة، راجع دليل البدء السريع لـ Docker.

استنسخ مستودع Ultralytics وقم بإعداد بيئة تطوير باستخدام:

يسمح هذا بالمساهمات في المشروع أو التجريب بأحدث التعليمات البرمجية المصدر. للحصول على التفاصيل، قم بزيارة مستودع Ultralytics على GitHub.

تعمل واجهة سطر الأوامر (CLI) الخاصة بـ Ultralytics YOLO على تبسيط مهام تشغيل الكشف عن الأجسام دون الحاجة إلى أكواد Python، مما يتيح استخدام أوامر من سطر واحد للتدريب والتحقق والتنبؤ مباشرةً من جهازك الطرفي. والصيغة الأساسية هي:

على سبيل المثال، لتدريب نموذج الكشف:

استكشف المزيد من الأوامر وأمثلة الاستخدام في دليل CLI الكامل.

**Examples:**

Example 1 (go):
```go
# Install or upgrade the ultralytics package from PyPI
pip install -U ultralytics
```

Example 2 (swift):
```swift
# Install the ultralytics package from GitHub
pip install git+https://github.com/ultralytics/ultralytics.git@main
```

Example 3 (go):
```go
# Install the ultralytics package using conda
conda install -c conda-forge ultralytics
```

Example 4 (julia):
```julia
# Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=11.8 ultralytics
```

---

## تجزئة المثيل

**URL:** https://docs.ultralytics.com/ar/tasks/segment/

**Contents:**
- تجزئة المثيل
- النماذج
- تدريب
  - تنسيق مجموعة البيانات
- التحقق
- توقع
- تصدير
- الأسئلة الشائعة
  - كيف أقوم بتدريب نموذج YOLO26 segmentation على مجموعة بيانات مخصصة؟
  - ما الفرق بين اكتشاف الكائنات وتجزئة الكائنات (instance segmentation) في YOLO26؟

تجزئة المثيل تتجاوز الكشف عن الكائنات وتتضمن تحديد الكائنات الفردية في الصورة وفصلها عن بقية الصورة.

إنّ مُخرجات نموذج تجزئة المثيل هي مجموعة من الأقنعة أو الخطوط التي تحدد شكل كل كائن في الصورة، بالإضافة إلى تصنيفات الفئات ودرجات الثقة لكل كائن. تجزئة المثيل مفيدة عندما تحتاج إلى معرفة ليس فقط مكان وجود الكائنات في الصورة، ولكن أيضًا شكلها الدقيق.

شاهد: قم بتشغيل التجزئة باستخدام نموذج Ultralytics YOLO المدرب مسبقًا في Python.

تستخدم نماذج YOLO26 segment -seg لاحقة، أي، yolo26n-seg.pt، ويتم تدريبها مسبقًا على COCO.

تُعرض هنا نماذج segment المدربة مسبقًا من YOLO26. نماذج detect و segment و pose مدربة مسبقًا على مجموعة بيانات COCO، بينما نماذج classify مدربة مسبقًا على مجموعة بيانات ImageNet.

يتم تنزيل النماذج تلقائيًا من أحدث إصدارات Ultralytics release عند الاستخدام الأول.

تدريب YOLO26n-seg على مجموعة بيانات COCO8-seg لمدة 100 epoch بحجم صورة 640. للاطلاع على قائمة كاملة بالوسائط المتاحة، راجع صفحة التكوين.

يمكن العثور على تنسيق مجموعة بيانات تجزئة YOLO بالتفصيل في دليل مجموعة البيانات. لتحويل مجموعة البيانات الحالية الخاصة بك من تنسيقات أخرى (مثل COCO وما إلى ذلك) إلى تنسيق YOLO، يرجى استخدام أداة JSON2YOLO بواسطة Ultralytics.

التحقق من صحة نموذج YOLO26n-seg المدرب الدقة على مجموعة بيانات COCO8-seg. لا توجد حاجة إلى وسيطات حيث أن model يحتفظ بالتدريب الخاص به data والوسائط كسمات للنموذج.

استخدم نموذج YOLO26n-seg مدربًا لتشغيل التنبؤات على الصور.

اطلع على التفاصيل الكاملة predict لأوضاع التشغيل في صفحة توقع التنبؤ.

صدّر نموذج YOLO26n-seg إلى تنسيق مختلف مثل ONNX، CoreML، إلخ.

تنسيقات تصدير YOLO26-seg المتاحة موجودة في الجدول أدناه. يمكنك التصدير إلى أي تنسيق باستخدام الـ format الوسيطة، أي format='onnx' أو format='engine'. يمكنك التنبؤ أو التحقق مباشرة على النماذج المصدرة، أي، yolo predict model=yolo26n-seg.onnx. يتم عرض أمثلة الاستخدام لنموذجك بعد اكتمال التصدير.

اطلع على التفاصيل الكاملة export التفاصيل في تصدير التنبؤ.

لتدريب نموذج تجزئة YOLO26 على مجموعة بيانات مخصصة، تحتاج أولاً إلى إعداد مجموعة البيانات الخاصة بك بتنسيق تجزئة YOLO. يمكنك استخدام أدوات مثل JSON2YOLO لتحويل مجموعات البيانات من تنسيقات أخرى. بمجرد أن تصبح مجموعة البيانات جاهزة، يمكنك تدريب النموذج باستخدام أوامر python أو CLI:

تحقق من صفحة التكوين لمزيد من الوسائط المتاحة.

يحدد اكتشاف الكائنات ويحدد موقعها داخل الصورة عن طريق رسم مربعات إحاطة حولها، بينما تجزئة الكائنات لا تحدد مربعات الإحاطة فحسب، بل تحدد أيضًا الشكل الدقيق لكل كائن. توفر نماذج تجزئة الكائنات YOLO26 أقنعة أو خطوطًا محيطية تحدد كل كائن مكتشف، وهو أمر مفيد بشكل خاص للمهام التي يكون فيها معرفة الشكل الدقيق للكائنات أمرًا مهمًا، مثل التصوير الطبي أو القيادة الذاتية.

Ultralytics YOLO26 هو نموذج متطور معروف بدقته العالية وأدائه في الوقت الفعلي، مما يجعله مثاليًا لمهام تجزئة الكائنات (instance segmentation). تأتي نماذج YOLO26 Segment مدربة مسبقًا على مجموعة بيانات COCO، مما يضمن أداءً قويًا عبر مجموعة متنوعة من الكائنات. بالإضافة إلى ذلك، يدعم YOLO وظائف التدريب والتحقق والتنبؤ والتصدير مع تكامل سلس، مما يجعله متعدد الاستخدامات للغاية لكل من تطبيقات البحث والصناعة.

يعد تحميل والتحقق من صحة نموذج تجزئة YOLO المدرب مسبقًا أمرًا واضحًا ومباشرًا. إليك كيفية القيام بذلك باستخدام كل من Python و CLI:

ستوفر لك هذه الخطوات مقاييس التحقق مثل متوسط الدقة المتوسطة (mAP)، وهي ضرورية لتقييم أداء النموذج.

يعد تصدير نموذج تجزئة YOLO إلى تنسيق ONNX أمرًا بسيطًا ويمكن القيام به باستخدام أوامر Python أو CLI:

لمزيد من التفاصيل حول التصدير إلى تنسيقات مختلفة، راجع صفحة التصدير.

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

## تدريب النماذج باستخدام Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/modes/train/

**Contents:**
- تدريب النماذج باستخدام Ultralytics YOLO
- مقدمة
- لماذا تختار Ultralytics YOLO للتدريب؟
  - الميزات الرئيسية لوضع التدريب
- أمثلة الاستخدام
  - التدريب متعدد وحدات معالجة الرسومات (GPU)
  - تدريب GPU في وضع الخمول
  - التدريب على Apple Silicon MPS
  - استئناف التدريبات المتوقفة
- إعدادات التدريب

يتضمن تدريب نموذج تعلم عميق تزويده بالبيانات وتعديل معلماته بحيث يمكنه إجراء تنبؤات دقيقة. تم تصميم وضع التدريب في Ultralytics YOLO26 لتدريب نماذج اكتشاف الكائنات بفعالية وكفاءة، مع الاستفادة الكاملة من قدرات الأجهزة الحديثة. يهدف هذا الدليل إلى تغطية جميع التفاصيل التي تحتاجها للبدء في تدريب نماذجك الخاصة باستخدام مجموعة ميزات YOLO26 القوية.

شاهد: كيفية تدريب نموذج YOLO على مجموعة البيانات المخصصة الخاصة بك في Google Colab.

فيما يلي بعض الأسباب المقنعة لاختيار وضع التدريب في YOLO26:

فيما يلي بعض الميزات البارزة لوضع التدريب في YOLO26:

تدريب YOLO26n على مجموعة بيانات COCO8 لـ 100 حقبة بحجم صورة 640. يمكن تحديد جهاز التدريب باستخدام الوسيطة device الوسيطة. إذا لم يتم تمرير أي وسيطة، فسيتم استخدام GPU device=0 عند توفرها؛ وإلا device='cpu' سيتم استخدامها. راجع قسم الوسائط أدناه للحصول على قائمة كاملة بوسائط التدريب.

خطأ تعدد العمليات في نظام التشغيل Windows

في نظام التشغيل Windows، قد تتلقى RuntimeError عند إطلاق التدريب كنص برمجي. أضف if __name__ == "__main__": ضع هذا الأمر قبل رمز التدريب الخاص بك لحل المشكلة.

مثال على التدريب باستخدام وحدة معالجة رسومات واحدة و CPU

يتم تحديد الجهاز تلقائيًا. إذا كانت وحدة GPU متاحة، فسيتم استخدامها (جهاز CUDA الافتراضي 0)؛ وإلا سيبدأ التدريب على CPU.

يتيح التدريب باستخدام وحدات معالجة رسومات متعددة الاستخدام الأكثر كفاءة لموارد الأجهزة المتاحة عن طريق توزيع حمل التدريب عبر وحدات معالجة رسومات متعددة. هذه الميزة متاحة من خلال واجهة python API وسطح الأوامر. لتمكين التدريب متعدد وحدات معالجة الرسومات، حدد معرفات أجهزة GPU التي ترغب في استخدامها.

مثال على التدريب باستخدام وحدات معالجة رسومات متعددة

للتدريب باستخدام وحدتي معالجة رسومات، CUDA الجهازين 0 و 1، استخدم الأوامر التالية. قم بالتوسيع ليشمل وحدات معالجة رسومات إضافية حسب الحاجة.

يمكّن تدريب GPU في وضع الخمول الاختيار التلقائي لوحدات معالجة الرسومات الأقل استخدامًا في الأنظمة متعددة وحدات معالجة الرسومات، مما يحسن استخدام الموارد دون تحديد GPU يدويًا. تحدد هذه الميزة وحدات معالجة الرسومات المتاحة بناءً على مقاييس الاستخدام وتوافر VRAM.

مثال على تدريب GPU في وضع الخمول

لتحديد واستخدام وحدات معالجة الرسوميات (GPU) الأكثر خمولًا للتدريب تلقائيًا، استخدم -1 معامل الجهاز. هذا مفيد بشكل خاص في بيئات الحوسبة المشتركة أو الخوادم التي بها العديد من المستخدمين.

تعطي خوارزمية الاختيار التلقائي الأولوية لوحدات معالجة الرسومات (GPUs) التي:

تعتبر هذه الميزة ذات قيمة خاصة في بيئات الحوسبة المشتركة أو عند تشغيل وظائف تدريب متعددة عبر نماذج مختلفة. تتكيف تلقائيًا مع الظروف المتغيرة للنظام، مما يضمن التخصيص الأمثل للموارد دون تدخل يدوي.

بدعم شرائح Apple silicon المدمجة في نماذج Ultralytics YOLO، أصبح من الممكن الآن تدريب النماذج الخاصة بك على الأجهزة التي تستخدم إطار عمل Metal Performance Shaders (MPS) القوي. يوفر MPS طريقة عالية الأداء لتنفيذ مهام الحساب ومعالجة الصور على شريحة Apple المخصصة.

لتمكين التدريب على شرائح Apple silicon، يجب عليك تحديد 'mps' كجهازك عند بدء عملية التدريب. فيما يلي مثال لكيفية القيام بذلك في python وعبر سطر الأوامر:

مثال على التدريب باستخدام MPS

مع الاستفادة من القوة الحسابية لشرائح Apple silicon، فإن هذا يتيح معالجة أكثر كفاءة لمهام التدريب. للحصول على إرشادات أكثر تفصيلاً وخيارات التكوين المتقدمة، يرجى الرجوع إلى وثائق PyTorch MPS.

يُعد استئناف التدريب من حالة محفوظة مسبقًا ميزة حاسمة عند العمل مع نماذج التعلم العميق. يمكن أن يكون هذا مفيدًا في سيناريوهات مختلفة، مثل عندما تنقطع عملية التدريب بشكل غير متوقع، أو عندما ترغب في متابعة تدريب نموذج ببيانات جديدة أو لمزيد من الحقب.

عند استئناف التدريب، يقوم Ultralytics YOLO بتحميل الأوزان من النموذج الذي تم حفظه مؤخرًا، كما يستعيد حالة المُحسِّن، وجدول معدل التعلم، ورقم الحقبة. يتيح لك ذلك متابعة عملية التدريب بسلاسة من حيث توقفت.

يمكنك بسهولة استئناف التدريب في Ultralytics YOLO عن طريق تعيين الوسيطة resume إلى True عند استدعاء الدالة train وتحديد المسار إلى ملف .pt الذي يحتوي على أوزان النموذج المدرب جزئيًا.

فيما يلي مثال لكيفية استئناف التدريب المتقطع باستخدام python وعبر سطر الأوامر:

مثال على استئناف التدريب

عن طريق تعيين resume=True، ستستمر دالة train في التدريب من حيث توقفت، باستخدام الحالة المخزنة في الملف 'path/to/last.pt'. إذا كان resume تم حذف الوسيطة أو تعيينها إلى False، ستستمر دالة train ستبدأ الدالة دورة تدريب جديدة.

تذكر أنه يتم حفظ نقاط التحقق في نهاية كل حقبة افتراضيًا، أو على فترات ثابتة باستخدام save_period لذلك يجب عليك إكمال حقبة واحدة على الأقل لاستئناف عملية التدريب.

تشمل إعدادات التدريب لنماذج YOLO مختلف المعلمات الفائقة والتكوينات المستخدمة أثناء عملية التدريب. تؤثر هذه الإعدادات على أداء النموذج وسرعته و دقته. تتضمن إعدادات التدريب الرئيسية حجم الدفعة ومعدل التعلم والزخم وتضاؤل الوزن. بالإضافة إلى ذلك، يمكن أن يؤثر اختيار المحسن و دالة الخسارة وتكوين مجموعة بيانات التدريب على عملية التدريب. يعد الضبط الدقيق والتجريب بهذه الإعدادات أمرًا بالغ الأهمية لتحسين الأداء.

ملاحظة حول إعدادات حجم الدفعة

في batch يمكن تهيئة وسيطة في ثلاث طرق:

تعتبر تقنيات الزيادة ضرورية لتحسين قوة وأداء نماذج YOLO من خلال إدخال تغييرات على بيانات التدريب، مما يساعد النموذج على التعميم بشكل أفضل على البيانات غير المرئية. يوضح الجدول التالي الغرض من كل وسيطة زيادة وتأثيرها:

يمكن تعديل هذه الإعدادات لتلبية المتطلبات المحددة لمجموعة البيانات والمهمة قيد التنفيذ. يمكن أن يساعد التجريب بقيم مختلفة في العثور على استراتيجية التوسيع المثالية التي تؤدي إلى أفضل أداء للنموذج.

لمزيد من المعلومات حول عمليات زيادة التدريب، راجع قسم المرجع.

عند تدريب نموذج YOLO26، قد تجد أنه من المفيد تتبع أداء النموذج بمرور الوقت. هنا يأتي دور التسجيل. يوفر Ultralytics YOLO دعمًا لثلاثة أنواع من المسجلات - Comet، ClearML، و TensorBoard.

لاستخدام مسجل، حدده من القائمة المنسدلة في مقتطف الشفرة أعلاه وقم بتشغيله. سيتم تثبيت المسجل المحدد وتهيئته.

Comet عبارة عن نظام أساسي يسمح لعلماء البيانات والمطورين بتتبع التجارب والنماذج ومقارنتها وشرحها وتحسينها. يوفر وظائف مثل المقاييس في الوقت الفعلي وفروق التعليمات البرمجية وتتبع المعلمات الفائقة.

تذكر تسجيل الدخول إلى حساب Comet الخاص بك على موقعه على الويب والحصول على مفتاح API الخاص بك. ستحتاج إلى إضافة هذا إلى متغيرات البيئة الخاصة بك أو البرنامج النصي الخاص بك لتسجيل تجاربك.

ClearML عبارة عن منصة مفتوحة المصدر تعمل على أتمتة تتبع التجارب وتساعد في المشاركة الفعالة للموارد. وهي مصممة لمساعدة الفرق على إدارة وتنفيذ وإعادة إنتاج أعمال تعلم الآلة الخاصة بهم بكفاءة أكبر.

بعد تشغيل هذا البرنامج النصي، ستحتاج إلى تسجيل الدخول إلى حساب ClearML الخاص بك على المتصفح ومصادقة جلستك.

TensorBoard عبارة عن مجموعة أدوات تصور لـ TensorFlow. يتيح لك تصور مخطط TensorFlow الخاص بك، ورسم المقاييس الكمية حول تنفيذ الرسم البياني الخاص بك، وإظهار بيانات إضافية مثل الصور التي تمر عبره.

لاستخدام TensorBoard في Google Colab:

لاستخدام TensorBoard محليًا، قم بتشغيل الأمر أدناه وعرض النتائج على http://localhost:6006/.

سيؤدي هذا إلى تحميل TensorBoard وتوجيهه إلى الدليل الذي تم فيه حفظ سجلات التدريب الخاصة بك.

بعد إعداد المسجل الخاص بك، يمكنك بعد ذلك المتابعة بتدريب النموذج الخاص بك. سيتم تسجيل جميع مقاييس التدريب تلقائيًا في النظام الأساسي الذي اخترته، ويمكنك الوصول إلى هذه السجلات لمراقبة أداء النموذج الخاص بك بمرور الوقت، ومقارنة النماذج المختلفة، وتحديد مجالات التحسين.

لتدريب نموذج اكتشاف الكائنات باستخدام Ultralytics YOLO26، يمكنك استخدام واجهة برمجة تطبيقات Python أو واجهة سطر الأوامر CLI. فيما يلي مثال لكليهما:

مثال على التدريب باستخدام وحدة معالجة رسومات واحدة و CPU

لمزيد من التفاصيل، راجع قسم إعدادات التدريب.

تشمل الميزات الرئيسية لوضع التدريب (Train mode) في Ultralytics YOLO26:

هذه الميزات تجعل التدريب فعالاً وقابلاً للتخصيص حسب احتياجاتك. لمزيد من التفاصيل، راجع قسم الميزات الرئيسية لوضع التدريب.

لاستئناف التدريب من جلسة متوقفة، قم بتعيين resume إلى True وحدد المسار إلى آخر نقطة تفتيش محفوظة.

مثال على استئناف التدريب

تحقق من القسم الخاص بـ استئناف التدريبات المتوقفة لمزيد من المعلومات.

نعم، يدعم Ultralytics YOLO26 التدريب على شرائح Apple Silicon بالاستفادة من إطار عمل Metal Performance Shaders (MPS). حدد 'mps' كجهاز التدريب الخاص بك.

مثال على التدريب باستخدام MPS

لمزيد من التفاصيل، راجع قسم التدريب على Apple Silicon MPS.

يتيح لك Ultralytics YOLO26 تهيئة مجموعة متنوعة من إعدادات التدريب مثل حجم الدفعة، ومعدل التعلم، وعدد الدورات، والمزيد عبر الوسائط. إليك نظرة عامة موجزة:

للحصول على دليل متعمق حول إعدادات التدريب، تحقق من قسم إعدادات التدريب.

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
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model with 2 GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[0, 1])

# Train the model with the two most idle GPUs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640, device=[-1, -1])
```

Example 4 (julia):
```julia
# Start training from a pretrained *.pt model using GPUs 0 and 1
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640 device=0,1

# Use the two most idle GPUs
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640 device=-1,-1
```

---

## تصدير النماذج باستخدام Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/modes/export/

**Contents:**
- تصدير النماذج باستخدام Ultralytics YOLO
- مقدمة
- لماذا تختار وضع التصدير (Export Mode) الخاص بـ YOLO26؟
  - الميزات الرئيسية لوضع التصدير
- أمثلة الاستخدام
- الوسائط
- صيغ التصدير
- الأسئلة الشائعة
  - كيف أقوم بتصدير نموذج YOLO26 إلى تنسيق ONNX؟
  - ما هي فوائد استخدام TensorRT لتصدير النماذج؟

الهدف الأسمى من تدريب النموذج هو نشره لتطبيقات العالم الحقيقي. يوفر وضع التصدير (Export mode) في Ultralytics YOLO26 مجموعة متنوعة من الخيارات لتصدير نموذجك المدرب إلى تنسيقات مختلفة، مما يجعله قابلاً للنشر عبر منصات وأجهزة متعددة. يهدف هذا الدليل الشامل إلى إرشادك عبر تفاصيل تصدير النموذج، مع عرض كيفية تحقيق أقصى قدر من التوافق والأداء.

شاهد: كيفية تصدير نموذج Ultralytics YOLO المدرب خصيصًا وتشغيل الاستدلال المباشر على كاميرا الويب.

فيما يلي بعض الوظائف البارزة:

قم بتصدير نموذج YOLO26n إلى تنسيق مختلف مثل ONNX أو TensorRT. راجع قسم الوسائط (Arguments) أدناه للحصول على قائمة كاملة بوسائط التصدير.

يوضح هذا الجدول بالتفصيل التكوينات والخيارات المتاحة لتصدير نماذج YOLO إلى تنسيقات مختلفة. هذه الإعدادات ضرورية لتحسين أداء النموذج المصدر وحجمه وتوافقه عبر الأنظمة الأساسية والبيئات المختلفة. يضمن التكوين الصحيح أن النموذج جاهز للنشر في التطبيق المقصود بأقصى قدر من الكفاءة.

يسمح تعديل هذه المعلمات بتخصيص عملية التصدير لتناسب متطلبات محددة، مثل بيئة النشر وقيود الأجهزة وأهداف الأداء. يعد اختيار التنسيق والإعدادات المناسبة أمرًا ضروريًا لتحقيق أفضل توازن بين حجم النموذج والسرعة و الدقة.

تتوفر تنسيقات تصدير YOLO26 في الجدول أدناه. يمكنك التصدير إلى أي تنسيق باستخدام format الوسيطة، أي format='onnx' أو format='engine'. يمكنك التنبؤ أو التحقق مباشرة على النماذج المصدرة، أي، yolo predict model=yolo26n.onnx. يتم عرض أمثلة الاستخدام لنموذجك بعد اكتمال التصدير.

يعد تصدير نموذج YOLO26 إلى تنسيق ONNX أمرًا سهلاً مع Ultralytics. يوفر كلاً من طرق python و CLI لتصدير النماذج.

لمزيد من التفاصيل حول العملية، بما في ذلك الخيارات المتقدمة مثل التعامل مع أحجام الإدخال المختلفة، راجع دليل تكامل ONNX.

يوفر استخدام TensorRT لتصدير النماذج تحسينات كبيرة في الأداء. يمكن لنماذج YOLO26 التي يتم تصديرها إلى TensorRT تحقيق تسريع يصل إلى 5 أضعاف في GPU، مما يجعلها مثالية لتطبيقات الاستدلال في الوقت الفعلي.

لمعرفة المزيد حول دمج TensorRT، راجع دليل دمج TensorRT.

يعد تكميم INT8 طريقة ممتازة لضغط النموذج وتسريع الاستدلال، خاصة على الأجهزة الطرفية. إليك كيفية تمكين تكميم INT8:

يمكن تطبيق تحديد الكميات INT8 على تنسيقات مختلفة، مثل TensorRT, OpenVINO، و CoreML. للحصول على أفضل نتائج للقياس الكمي، قم بتوفير مجموعة البيانات باستخدام data .

يسمح حجم الإدخال الديناميكي للنموذج المصدَّر بمعالجة أبعاد الصور المتغيرة، مما يوفر المرونة ويحسن كفاءة المعالجة لحالات الاستخدام المختلفة. عند التصدير إلى تنسيقات مثل ONNX أو TensorRT، يضمن تمكين حجم الإدخال الديناميكي قدرة النموذج على التكيف مع أشكال الإدخال المختلفة بسلاسة.

لتفعيل هذه الخاصية، استخدم dynamic=True علامة أثناء التصدير:

يكون تغيير حجم الإدخال الديناميكي مفيدًا بشكل خاص للتطبيقات التي قد تختلف فيها أبعاد الإدخال، مثل معالجة الفيديو أو عند التعامل مع الصور من مصادر مختلفة.

يُعد فهم وتكوين وسائط التصدير أمرًا بالغ الأهمية لتحسين أداء النموذج:

للنشر على منصات أجهزة معينة، ضع في اعتبارك استخدام تنسيقات تصدير متخصصة مثل TensorRT لوحدات معالجة الرسوميات NVIDIA، أو CoreML لأجهزة Apple، أو Edge TPU لأجهزة Google Coral.

عند تصدير نموذج YOLO إلى تنسيقات مثل ONNX أو TensorRT، يعتمد هيكل tensor الناتج على مهمة النموذج. يعد فهم هذه المخرجات أمرًا مهمًا لتطبيقات الاستدلال المخصصة.

ل نماذج detect (على سبيل المثال، yolo26n.pt)، يكون الناتج عادةً tensor واحدًا على شكل (batch_size, 4 + num_classes, num_predictions) حيث تمثل القنوات إحداثيات المربع بالإضافة إلى درجات كل فئة، و num_predictions يعتمد على دقة إدخال التصدير (ويمكن أن يكون ديناميكيًا).

ل نماذج segment (على سبيل المثال، yolo26n-seg.pt)، ستحصل عادةً على مخرجين: tensor الأول على شكل (batch_size, 4 + num_classes + mask_dim, num_predictions) (صناديق، درجات الفئة، ومعاملات القناع)، وtensor الثاني على شكل (batch_size, mask_dim, proto_h, proto_w) يحتوي على نماذج أولية للقناع تُستخدم مع المعاملات لتوليد أقنعة الكائنات. تعتمد الأحجام على دقة إدخال التصدير (ويمكن أن تكون ديناميكية).

ل نماذج الوضعيات (على سبيل المثال، yolo26n-pose.pt)، يكون tensor الناتج عادةً على شكل (batch_size, 4 + num_classes + keypoint_dims, num_predictions)، حيث keypoint_dims يعتمد على مواصفات الوضعية (مثل عدد النقاط الرئيسية وما إذا كانت الثقة متضمنة)، و num_predictions يعتمد على دقة إدخال التصدير (ويمكن أن يكون ديناميكيًا).

توضح الأمثلة في أمثلة استدلال ONNX كيفية معالجة هذه المخرجات لكل نوع نموذج.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom-trained model

# Export the model
model.export(format="onnx")
```

Example 2 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx      # export official model
yolo export model=path/to/best.pt format=onnx # export custom-trained model
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load an official model
model = YOLO("path/to/best.pt")  # load a custom-trained model

# Export the model
model.export(format="onnx")
```

Example 4 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx      # export official model
yolo export model=path/to/best.pt format=onnx # export custom-trained model
```

---

## تصنيف الصور

**URL:** https://docs.ultralytics.com/ar/tasks/classify/

**Contents:**
- تصنيف الصور
- النماذج
- تدريب
  - تنسيق مجموعة البيانات
- التحقق
- توقع
- تصدير
- الأسئلة الشائعة
  - ما هو الغرض من YOLO26 في تصنيف الصور؟
  - كيف أدرب نموذج YOLO26 لتصنيف الصور؟

تصنيف الصور هو أبسط المهام الثلاث ويتضمن تصنيف صورة كاملة إلى واحدة من مجموعة من الفئات المحددة مسبقًا.

ناتج مصنف الصور هو تسمية فئة واحدة ودرجة ثقة. يكون تصنيف الصور مفيدًا عندما تحتاج فقط إلى معرفة الفئة التي تنتمي إليها الصورة ولا تحتاج إلى معرفة مكان وجود كائنات تلك الفئة أو ما هو شكلها الدقيق.

شاهد: استكشف مهام Ultralytics YOLO: تصنيف الصور باستخدام منصة Ultralytics

نماذج YOLO26 classify تستخدم الـ -cls لاحقة، أي، yolo26n-cls.pt، ويتم تدريبها مسبقًا على ImageNet.

تُعرض هنا نماذج classify المدربة مسبقًا من YOLO26. نماذج detect و segment و pose مدربة مسبقًا على مجموعة بيانات COCO، بينما نماذج classify مدربة مسبقًا على مجموعة بيانات ImageNet.

يتم تنزيل النماذج تلقائيًا من أحدث إصدار Ultralytics عند الاستخدام الأول.

تدريب YOLO26n-cls على مجموعة بيانات MNIST160 لمدة 100 epoch بحجم صورة 64. للاطلاع على قائمة كاملة بالوسائط المتاحة، راجع صفحة التكوين.

يستخدم تصنيف Ultralytics YOLO torchvision.transforms.RandomResizedCrop للتدريب و torchvision.transforms.CenterCrop للتحقق والاستدلال. تفترض هذه التحويلات القائمة على الاقتصاص مدخلات مربعة وقد تقتطع عن غير قصد مناطق مهمة من الصور ذات نسب العرض إلى الارتفاع الشديدة، مما قد يتسبب في فقدان معلومات مرئية مهمة أثناء التدريب. للحفاظ على الصورة كاملة مع الحفاظ على نسبها، ضع في اعتبارك استخدام torchvision.transforms.Resize بدلاً من تحويلات الاقتصاص.

يمكنك تنفيذ ذلك عن طريق تخصيص خط أنابيب الزيادة الخاص بك من خلال ClassificationDataset و ClassificationTrainer.

يمكن العثور على تنسيق مجموعة بيانات تصنيف YOLO بالتفصيل في دليل مجموعة البيانات.

التحقق من صحة نموذج YOLO26n-cls المدرب الدقة على مجموعة بيانات MNIST160. لا توجد حاجة إلى وسائط حيث أن model يحتفظ بالتدريب الخاص به data والوسائط كسمات للنموذج.

كما ذكر في قسم التدريب، يمكنك التعامل مع نسب العرض إلى الارتفاع المتطرفة أثناء التدريب باستخدام ClassificationTrainer: تحتاج إلى تطبيق نفس النهج للحصول على نتائج تحقق متسقة من خلال تطبيق مخصص للـ ClassificationValidator عند استدعاء الدالة val() طريقة. ارجع إلى مثال التعليمات البرمجية الكامل في قسم التدريب للحصول على تفاصيل التنفيذ.

استخدم نموذج YOLO26n-cls مدربًا لتشغيل التنبؤات على الصور.

اطلع على التفاصيل الكاملة predict لأوضاع التشغيل في صفحة توقع التنبؤ.

تصدير نموذج YOLO26n-cls إلى تنسيق مختلف مثل ONNX، CoreML، إلخ.

تنسيقات تصدير YOLO26-cls المتاحة موجودة في الجدول أدناه. يمكنك التصدير إلى أي تنسيق باستخدام format الوسيطة، أي format='onnx' أو format='engine'. يمكنك التنبؤ أو التحقق مباشرة على النماذج المصدرة، أي، yolo predict model=yolo26n-cls.onnx. يتم عرض أمثلة الاستخدام لنموذجك بعد اكتمال التصدير.

اطلع على التفاصيل الكاملة export التفاصيل في تصدير التنبؤ.

نماذج YOLO26، مثل yolo26n-cls.pt، مُصممة لتصنيف الصور بكفاءة. فهي تُعيّن تصنيفًا واحدًا للصورة بأكملها بالإضافة إلى درجة ثقة. وهذا مفيد بشكل خاص للتطبيقات التي يكون فيها معرفة التصنيف المحدد للصورة كافيًا، بدلاً من تحديد موقع أو شكل الكائنات داخل الصورة.

لتدريب نموذج YOLO26، يمكنك استخدام أوامر python أو CLI. على سبيل المثال، لتدريب yolo26n-cls نموذج على مجموعة بيانات MNIST160 لـ 100 دورة تدريبية (epoch) بحجم صورة 64:

لمزيد من خيارات التكوين، قم بزيارة صفحة التكوين.

يمكن العثور على نماذج تصنيف YOLO26 المدربة مسبقًا في النماذج النماذج مثل yolo26n-cls.pt, yolo26s-cls.pt, yolo26m-cls.pt، إلخ، مدربة مسبقًا على ImageNet ويمكن تنزيلها واستخدامها بسهولة لمهام تصنيف الصور المختلفة.

يمكنك تصدير نموذج YOLO26 مدرب إلى تنسيقات مختلفة باستخدام أوامر python أو CLI. على سبيل المثال، لتصدير نموذج إلى تنسيق ONNX:

لخيارات التصدير التفصيلية، راجع صفحة التصدير.

للتحقق من دقة النموذج المدرب على مجموعة بيانات مثل MNIST160، يمكنك استخدام أوامر Python أو CLI التالية:

لمزيد من المعلومات، قم بزيارة قسم التحقق.

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

## تقدير الوضع

**URL:** https://docs.ultralytics.com/ar/tasks/pose/

**Contents:**
- تقدير الوضع
- النماذج
- تدريب
  - تنسيق مجموعة البيانات
- التحقق
- توقع
- تصدير
- الأسئلة الشائعة
  - ما هو تقدير الوضعيات باستخدام Ultralytics YOLO26 وكيف يعمل؟
  - كيف يمكنني تدريب نموذج YOLO26-pose على مجموعة بيانات مخصصة؟

تقدير وضعية الجسم هو مهمة تتضمن تحديد موقع نقاط معينة في الصورة، والتي يشار إليها عادةً باسم النقاط الرئيسية. يمكن أن تمثل النقاط الرئيسية أجزاء مختلفة من الكائن مثل المفاصل أو المعالم أو الميزات المميزة الأخرى. يتم تمثيل مواقع النقاط الرئيسية عادةً كمجموعة من ثنائية الأبعاد [x, y] أو ثلاثية الأبعاد [x, y, visible] الإحداثيات.

ناتج نموذج تقدير وضعية الجسم هو مجموعة من النقاط التي تمثل النقاط الرئيسية على كائن في الصورة، عادةً جنبًا إلى جنب مع درجات الثقة لكل نقطة. يعتبر تقدير وضعية الجسم خيارًا جيدًا عندما تحتاج إلى تحديد أجزاء معينة من كائن في مشهد، وموقعها بالنسبة لبعضها البعض.

شاهد: برنامج تعليمي لتقدير الوضعيات باستخدام Ultralytics YOLO26 | تتبع الكائنات في الوقت الفعلي واكتشاف وضعيات الإنسان

YOLO26 pose تستخدم نماذج -pose لاحقة، أي، yolo26n-pose.pt. يتم تدريب هذه النماذج على نقاط COCO الرئيسية وهي مناسبة لمجموعة متنوعة من مهام تقدير وضعية الجسم.

في نموذج YOLO26 الافتراضي للوضعيات، توجد 17 نقطة رئيسية (keypoints)، يمثل كل منها جزءًا مختلفًا من جسم الإنسان. إليك تعيين كل فهرس إلى مفصل الجسم الخاص به:

تُعرض هنا نماذج Pose المدربة مسبقًا من Ultralytics YOLO26. نماذج detect و segment و Pose مدربة مسبقًا على مجموعة بيانات COCO، بينما نماذج classify مدربة مسبقًا على مجموعة بيانات ImageNet.

يتم تنزيل النماذج تلقائيًا من أحدث إصدارات Ultralytics release عند الاستخدام الأول.

تدريب نموذج YOLO26-pose على مجموعة بيانات COCO8-pose. تُعد مجموعة بيانات COCO8-pose مجموعة بيانات عينة صغيرة مثالية لاختبار نماذج تقدير الوضع وتصحيح أخطائها.

يمكن العثور على تنسيق مجموعة بيانات وضع YOLO بالتفصيل في دليل مجموعة البيانات. لتحويل مجموعة البيانات الحالية الخاصة بك من تنسيقات أخرى (مثل COCO وما إلى ذلك) إلى تنسيق YOLO، يرجى استخدام أداة JSON2YOLO بواسطة Ultralytics.

بالنسبة لمهام تقدير الوضع المخصصة، يمكنك أيضًا استكشاف مجموعات البيانات المتخصصة مثل Tiger-Pose لتقدير وضع الحيوان، أو Hand Keypoints لتتبع اليد، أو Dog-Pose لتحليل وضع الكلاب.

التحقق من صحة نموذج YOLO26n-pose المدرب الدقة على مجموعة بيانات COCO8-pose. لا توجد حاجة إلى وسيطات حيث أن model يحتفظ بالتدريب الخاص به data والوسائط كسمات للنموذج.

استخدم نموذج YOLO26n-pose مدربًا لإجراء التنبؤات على الصور. يتيح لك وضع التنبؤ إجراء الاستدلال على الصور أو مقاطع الفيديو أو التدفقات في الوقت الفعلي.

اطلع على التفاصيل الكاملة predict لأوضاع التشغيل في صفحة توقع التنبؤ.

تصدير نموذج YOLO26n Pose إلى تنسيق مختلف مثل ONNX و CoreML، إلخ. يتيح لك هذا نشر نموذجك على منصات وأجهزة مختلفة لـ الاستدلال في الوقت الفعلي.

تنسيقات تصدير YOLO26-pose المتاحة موجودة في الجدول أدناه. يمكنك التصدير إلى أي تنسيق باستخدام format الوسيطة، أي format='onnx' أو format='engine'. يمكنك التنبؤ أو التحقق مباشرة على النماذج المصدرة، أي، yolo predict model=yolo26n-pose.onnx. يتم عرض أمثلة الاستخدام لنموذجك بعد اكتمال التصدير.

اطلع على التفاصيل الكاملة export التفاصيل في تصدير التنبؤ.

يتضمن تقدير الوضع باستخدام Ultralytics YOLO26 تحديد نقاط محددة، تُعرف باسم النقاط الرئيسية (keypoints)، في الصورة. تمثل هذه النقاط الرئيسية عادةً المفاصل أو الميزات الهامة الأخرى للكائن. يتضمن الإخراج [x, y] إحداثيات ونقاط ثقة لكل نقطة. تم تصميم نماذج YOLO26-pose خصيصًا لهذه المهمة وتستخدم -pose لاحقة، مثل yolo26n-pose.pt. يتم تدريب هذه النماذج مسبقًا على مجموعات بيانات مثل نقاط COCO الرئيسية ويمكن استخدامها لمهام تقدير الوضعية المختلفة. لمزيد من المعلومات، قم بزيارة صفحة تقدير الوضعية.

يتضمن تدريب نموذج YOLO26-pose على مجموعة بيانات مخصصة تحميل نموذج، سواء كان نموذجًا جديدًا معرفًا بملف yaml أو نموذجًا مدربًا مسبقًا. يمكنك بعد ذلك بدء عملية التدريب باستخدام مجموعة البيانات والمعلمات المحددة.

للحصول على تفاصيل شاملة حول التدريب، ارجع إلى قسم التدريب. يمكنك أيضًا استخدام منصة Ultralytics لنهج بدون تعليمات برمجية لتدريب نماذج تقدير الوضع المخصصة.

يتضمن التحقق من صحة نموذج YOLO26-pose تقييم دقته باستخدام نفس معلمات مجموعة البيانات المحتفظ بها أثناء التدريب. إليك مثال:

لمزيد من المعلومات، قم بزيارة قسم Val.

نعم، يمكنك تصدير نموذج YOLO26-pose إلى تنسيقات مختلفة مثل ONNX و CoreML و TensorRT والمزيد. يمكن القيام بذلك باستخدام python أو واجهة سطر الأوامر (CLI).

راجع قسم التصدير لمزيد من التفاصيل. يمكن نشر النماذج التي تم تصديرها على الأجهزة الطرفية للتطبيقات في الوقت الفعلي مثل تتبع اللياقة البدنية أو تحليل الرياضة أو الروبوتات.

تقدم Ultralytics YOLO26 نماذج Pose مدربة مسبقًا متنوعة مثل YOLO26n-pose و YOLO26s-pose و YOLO26m-pose، وغيرها. تختلف هذه النماذج في الحجم والدقة (mAP) والسرعة. على سبيل المثال، يحقق نموذج YOLO26n-pose قيمة mAPpose50-95 تبلغ 50.0 و mAPpose50 تبلغ 81.0. للحصول على قائمة كاملة وتفاصيل الأداء، قم بزيارة قسم النماذج.

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

## توقع النموذج باستخدام Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/modes/predict/

**Contents:**
- توقع النموذج باستخدام Ultralytics YOLO
- مقدمة
- تطبيقات واقعية
- لماذا نستخدم Ultralytics YOLO للاستدلال؟
  - الميزات الرئيسية لوضع التوقع (Predict)
- مصادر الاستدلال
- وسائط الاستدلال
- تنسيقات الصور والفيديو
  - الصور
  - مقاطع الفيديو

في عالم التعلم الآلي ورؤية الكمبيوتر، غالبًا ما تسمى عملية فهم البيانات المرئية بالاستدلال أو التنبؤ. يقدم Ultralytics YOLO26 ميزة قوية تُعرف باسم وضع التنبؤ، والمصممة خصيصًا للاستدلال عالي الأداء وفي الوقت الفعلي عبر مجموعة واسعة من مصادر البيانات.

شاهد: كيفية استخراج النتائج من مهام Ultralytics YOLO26 للمشاريع المخصصة 🚀

إليك سبب وجوب التفكير في وضع التنبؤ (predict mode) الخاص بـ YOLO26 لاحتياجات الاستدلال المتنوعة لديك:

تم تصميم وضع التنبؤ (predict mode) الخاص بـ YOLO26 ليكون قويًا ومتعدد الاستخدامات، ويتميز بـ:

تقوم نماذج Ultralytics YOLO بإرجاع إما قائمة Python بـ Results كائنات أو مولد فعال للذاكرة لـ Results الكائنات عندما stream=True يتم تمريرها إلى النموذج أثناء الاستدلال:

يمكن لـ YOLO26 معالجة أنواع مختلفة من مصادر الإدخال للاستدلال، كما هو موضح في الجدول أدناه. تشمل المصادر الصور الثابتة، وتدفقات الفيديو، وتنسيقات البيانات المختلفة. يشير الجدول أيضًا إلى ما إذا كان يمكن استخدام كل مصدر في وضع التدفق (streaming mode) مع الوسيطة stream=True ✅. يعتبر وضع البث مفيدًا لمعالجة مقاطع الفيديو أو البث المباشر لأنه ينشئ مولدًا للنتائج بدلاً من تحميل جميع الإطارات في الذاكرة.

استخدم stream=True لمعالجة مقاطع الفيديو الطويلة أو مجموعات البيانات الكبيرة لإدارة الذاكرة بكفاءة. عندما stream=False، يتم تخزين نتائج جميع الإطارات أو نقاط البيانات في الذاكرة، مما قد يتراكم بسرعة ويسبب أخطاء نفاد الذاكرة للإدخالات الكبيرة. في المقابل، stream=True يستخدم مولدًا، والذي يحتفظ فقط بنتائج الإطار الحالي أو نقطة البيانات في الذاكرة، مما يقلل بشكل كبير من استهلاك الذاكرة ويمنع مشكلات نفاد الذاكرة.

فيما يلي أمثلة التعليمات البرمجية لاستخدام كل نوع مصدر:

تشغيل الاستدلال على ملف صورة.

تشغيل الاستدلال على محتوى الشاشة الحالي كلقطة شاشة.

تشغيل الاستدلال على صورة أو فيديو مستضاف عن بعد عبر عنوان URL.

تشغيل الاستدلال على صورة تم فتحها باستخدام مكتبة تصوير python (PIL).

تشغيل الاستدلال على صورة تمت قراءتها باستخدام OpenCV.

تشغيل الاستدلال على صورة ممثلة كمصفوفة numpy.

تشغيل الاستدلال على صورة ممثلة كـ PyTorch tensor.

تشغيل الاستدلال على مجموعة من الصور وعناوين URL ومقاطع الفيديو والأدلة المدرجة في ملف CSV.

تشغيل الاستدلال على ملف فيديو. باستخدام stream=True، يمكنك إنشاء مولد لكائنات النتائج لتقليل استخدام الذاكرة.

تشغيل الاستدلال على جميع الصور ومقاطع الفيديو في دليل. لتضمين الأصول في الدلائل الفرعية، استخدم نمط glob مثل path/to/dir/**/*.

تشغيل الاستدلال على جميع الصور ومقاطع الفيديو التي تطابق تعبير glob مع * أحرف.

تشغيل الاستدلال على فيديو YouTube. باستخدام stream=True، يمكنك إنشاء مولد لكائنات النتائج لتقليل استخدام الذاكرة لمقاطع الفيديو الطويلة.

استخدم وضع البث لتشغيل الاستدلال على تدفقات الفيديو المباشرة باستخدام بروتوكولات RTSP أو RTMP أو TCP أو عنوان IP. إذا تم توفير دفق واحد، فسيقوم النموذج بتشغيل الاستدلال بـ حجم الدفعة 1. لدفقات متعددة، يمكن استخدام ملف .streams نصي لإجراء استدلال مجمّع، حيث يتم تحديد حجم الدفعة من خلال عدد التدفقات المتوفرة (على سبيل المثال، حجم الدفعة 8 لـ 8 تدفقات).

بالنسبة لاستخدام دفق واحد، يتم تعيين حجم الدفعة افتراضيًا على 1، مما يتيح معالجة فعالة في الوقت الفعلي لتغذية الفيديو.

للتعامل مع تدفقات فيديو متعددة في وقت واحد، استخدم ملف .streams ملف نصي يحتوي على مصدر واحد لكل سطر. سيقوم النموذج بتشغيل الاستدلال المجمّع حيث يساوي حجم الدفعة عدد التدفقات. يتيح هذا الإعداد معالجة فعالة لموجزات متعددة في وقت واحد.

مثال .streams ملف نصي:

يمثل كل صف في الملف مصدر بث، مما يسمح لك بمراقبة وإجراء الاستدلال على عدة تدفقات فيديو في وقت واحد.

يمكنك تشغيل الاستدلال على جهاز كاميرا متصل عن طريق تمرير فهرس تلك الكاميرا المعينة إلى source.

model.predict() يقبل وسيطات متعددة يمكن تمريرها في وقت الاستدلال لتجاوز الإعدادات الافتراضية:

تستخدم Ultralytics الحد الأدنى من المساحات المتروكة أثناء الاستدلال افتراضيًا (rect=True). في هذا الوضع، يتم تذييل الجانب الأقصر من كل صورة فقط بالقدر اللازم لجعله قابلاً للقسمة على أقصى خطوة للنموذج، بدلاً من تذييله بالكامل إلى imgsz. عند تشغيل الاستدلال على مجموعة من الصور، يعمل الحد الأدنى من الحشو فقط إذا كانت جميع الصور لها نفس الحجم. وإلا، يتم حشو الصور بشكل موحد إلى شكل مربع مع تساوي كلا الجانبين imgsz.

يدعم YOLO26 تنسيقات الصور والفيديو المختلفة، كما هو محدد في ultralytics/data/utils.py. راجع الجداول أدناه للتعرف على اللواحق الصالحة وأمثلة أوامر التنبؤ.

يحتوي الجدول أدناه على تنسيقات صور Ultralytics الصالحة.

يتم دعم صور HEIC للاستدلال فقط، وليس للتدريب.

يحتوي الجدول أدناه على تنسيقات فيديو Ultralytics الصالحة.

جميع استدعاءات Ultralytics predict() ستُرجع قائمة من Results الكائنات:

Results تحتوي الكائنات على السمات التالية:

Results تحتوي الكائنات على الطرق التالية:

لمزيد من التفاصيل، راجع Results توثيق الفئة.

Boxes يمكن استخدام الكائن لفهرسة مربعات الإحاطة ومعالجتها وتحويلها إلى تنسيقات مختلفة.

فيما يلي جدول لـ Boxes أساليب وخصائص الفئة، بما في ذلك الاسم والنوع والوصف:

لمزيد من التفاصيل، راجع Boxes توثيق الفئة.

Masks يمكن استخدام الكائن للفهرسة ومعالجة الأقنعة وتحويلها إلى أجزاء.

فيما يلي جدول لـ Masks أساليب وخصائص الفئة، بما في ذلك الاسم والنوع والوصف:

لمزيد من التفاصيل، راجع Masks توثيق الفئة.

Keypoints يمكن استخدام الكائن للفهرسة ومعالجة الإحداثيات وتطبيعها.

فيما يلي جدول لـ Keypoints أساليب وخصائص الفئة، بما في ذلك الاسم والنوع والوصف:

لمزيد من التفاصيل، راجع Keypoints توثيق الفئة.

Probs يمكن استخدام الكائن للفهرسة والحصول على top1 و top5 فهارس وعلامات التصنيف.

إليك جدول يلخص الطرق والخصائص الخاصة بـ Probs فئة:

لمزيد من التفاصيل، راجع Probs توثيق الفئة.

OBB يمكن استخدام الكائن للفهرسة ومعالجة وتحويل مربعات الإحاطة الموجهة إلى تنسيقات مختلفة.

فيما يلي جدول لـ OBB أساليب وخصائص الفئة، بما في ذلك الاسم والنوع والوصف:

لمزيد من التفاصيل، راجع OBB توثيق الفئة.

في plot() في method Results تسهل الكائنات تصور التنبؤات عن طريق تراكب الكائنات التي تم الكشف عنها (مثل المربعات المحيطة والأقنعة والنقاط الرئيسية والاحتمالات) على الصورة الأصلية. تُرجع هذه الطريقة الصورة المشروحة كمصفوفة NumPy، مما يسمح بسهولة العرض أو الحفظ.

في plot() تدعم method وسائط مختلفة لتخصيص الإخراج:

يعد ضمان سلامة سلاسل العمليات أثناء الاستدلال أمرًا بالغ الأهمية عندما تقوم بتشغيل نماذج YOLO متعددة بالتوازي عبر سلاسل عمليات مختلفة. يضمن الاستدلال الآمن لسلاسل العمليات أن تكون تنبؤات كل سلسلة عمليات معزولة ولا تتداخل مع بعضها البعض، مما يتجنب حالات التعارض ويضمن مخرجات متسقة وموثوقة.

عند استخدام نماذج YOLO في تطبيق متعدد السلاسل، من المهم إنشاء كائنات نموذج منفصلة لكل سلسلة عمليات أو استخدام وحدة تخزين محلية خاصة بسلسلة العمليات لمنع التعارضات:

الاستدلال الآمن لسير العمليات

قم بإنشاء نموذج واحد داخل كل سلسلة عمليات للاستدلال الآمن لسلسلة العمليات:

لإلقاء نظرة متعمقة على الاستدلال الآمن لسلاسل العمليات مع نماذج YOLO وتعليمات خطوة بخطوة، يرجى الرجوع إلى دليل الاستدلال الآمن لسلاسل العمليات YOLO الخاص بنا. سيوفر لك هذا الدليل جميع المعلومات الضرورية لتجنب المخاطر الشائعة والتأكد من أن الاستدلال متعدد السلاسل يعمل بسلاسة.

إليك برنامج python نصي يستخدم OpenCV (cv2) و YOLO لتشغيل الاستدلال على إطارات الفيديو. يفترض هذا البرنامج النصي أنك قمت بالفعل بتثبيت الحزم الضرورية (opencv-python و ultralytics).

سيقوم هذا البرنامج النصي بتشغيل التنبؤات على كل إطار من الفيديو، وتصور النتائج، وعرضها في نافذة. يمكن الخروج من الحلقة بالضغط على 'q'.

Ultralytics YOLO هو نموذج حديث للكشف عن الكائنات في الوقت الفعلي، والتقسيم، والتصنيف. يسمح وضع التنبؤ الخاص به للمستخدمين بإجراء استدلال عالي السرعة على مصادر بيانات مختلفة مثل الصور ومقاطع الفيديو والبث المباشر. تم تصميمه لتحقيق الأداء العالي وتعدد الاستخدامات، كما يوفر معالجة الدُفعات وأوضاع البث. لمزيد من التفاصيل حول ميزاته، تحقق من وضع التنبؤ Ultralytics YOLO.

يمكن لـ Ultralytics YOLO معالجة مجموعة واسعة من مصادر البيانات، بما في ذلك الصور ومقاطع الفيديو الفردية والأدلة وعناوين URL والبث. يمكنك تحديد مصدر البيانات في model.predict() مكالمة. على سبيل المثال، استخدم 'image.jpg' لصورة محلية أو 'https://ultralytics.com/images/bus.jpg' لعنوان URL. تحقق من الأمثلة التفصيلية لمختلف مصادر الاستدلال في الوثائق.

لتحسين سرعة الاستدلال وإدارة الذاكرة بكفاءة، يمكنك استخدام وضع التدفق عن طريق تعيين stream=True في طريقة استدعاء المتنبئ. يُنشئ وضع التدفق مُولِّدًا فعالًا للذاكرة لـ Results الكائنات بدلًا من تحميل جميع الإطارات في الذاكرة. لمعالجة مقاطع الفيديو الطويلة أو مجموعات البيانات الكبيرة، يكون وضع التدفق مفيدًا بشكل خاص. تعرف على المزيد حول وضع التدفق.

في model.predict() تدعم طريقة YOLO العديد من الوسائط مثل conf, iou, imgsz, device، والمزيد. تسمح لك هذه الوسائط بتخصيص عملية الاستدلال، وتعيين معلمات مثل عتبات الثقة وحجم الصورة والجهاز المستخدم للحساب. يمكن العثور على أوصاف تفصيلية لهذه الوسائط في وسائط الاستدلال القسم.

بعد تشغيل الاستدلال باستخدام YOLO، فإن Results تحتوي الكائنات على طرق لعرض وحفظ الصور المشروحة. يمكنك استخدام طرق مثل result.show() و result.save(filename="result.jpg") لتصور وحفظ النتائج. للحصول على قائمة شاملة بهذه الطرق، راجع العمل مع النتائج القسم.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model(["image1.jpg", "image2.jpg"])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # pretrained YOLO26n model

# Run batched inference on a list of images
results = model(["image1.jpg", "image2.jpg"], stream=True)  # return a generator of Results objects

# Process results generator
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Define path to the image file
source = "path/to/image.jpg"

# Run inference on the source
results = model(source)  # list of Results objects
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Define current screenshot as source
source = "screen"

# Run inference on the source
results = model(source)  # list of Results objects
```

---

## حلول Ultralytics: تسخير YOLO26 لحل المشكلات الواقعية

**URL:** https://docs.ultralytics.com/ar/solutions/

**Contents:**
- حلول Ultralytics: تسخير YOLO26 لحل المشكلات الواقعية
- الحلول
  - وسائط الحلول
  - استخدام SolutionAnnotator
  - العمل مع SolutionResults
  - استخدام الحلول عبر CLI
  - المساهمة في حلولنا
- الأسئلة الشائعة
  - كيف يمكنني استخدام Ultralytics YOLO لعد الكائنات في الوقت الفعلي؟
  - ما هي فوائد استخدام Ultralytics YOLO لأنظمة الأمان؟

توفر حلول Ultralytics تطبيقات متطورة لنماذج YOLO، وتقدم حلولًا واقعية مثل عد الكائنات، والتعتيم، وأنظمة الأمان، مما يعزز الكفاءة والدقة في مختلف الصناعات. اكتشف قوة YOLO26 للتطبيقات العملية والمؤثرة.

شاهد: كيفية تشغيل حلول Ultralytics من سطر الأوامر (CLI) | Ultralytics YOLO26 🚀

إليك قائمتنا المنسقة لحلول Ultralytics التي يمكن استخدامها لإنشاء مشاريع رؤية حاسوبية رائعة.

تدعم الحلول أيضًا بعض الوسائط من track، بما في ذلك معلمات مثل. conf, line_width, tracker, model, show, verbose و classes.

يمكنك استخدام show_conf, show_labels، وغيرها من الوسائط المذكورة لتخصيص التصور.

تستخدم جميع حلول Ultralytics الفئة المنفصلة SolutionAnnotator، الذي يمتد إلى Annotator class، ولديه الطرق التالية:

باستثناء Similarity Search، ترجع كل استدعاءات Solution قائمة بـ SolutionResults كائن.

نتائج الحل (SolutionResults)

SolutionResults للكائن السمات التالية:

لمزيد من التفاصيل، راجع SolutionResults توثيق الفئة.

يمكن استخدام معظم الحلول مباشرةً من خلال واجهة سطر الأوامر (command-line interface)، بما في ذلك:

Count, Crop, Blur, Workout, Heatmap, Isegment, Visioneye, Speed, Queue, Analytics, Inference

نحن نرحب بمساهمات المجتمع! إذا كنت قد أتقنت جانبًا معينًا من Ultralytics YOLO لم تتم تغطيته بعد في حلولنا، فنحن نشجعك على مشاركة خبراتك. يعد كتابة دليل طريقة رائعة لرد الجميل للمجتمع ومساعدتنا في جعل وثائقنا أكثر شمولاً وسهولة في الاستخدام.

للبدء، يرجى قراءة دليل المساهمة الخاص بنا للحصول على إرشادات حول كيفية فتح طلب سحب (PR) 🛠️. نحن نتطلع إلى مساهماتكم!

دعونا نعمل معًا لجعل نظام Ultralytics YOLO البيئي أكثر قوة وتنوعًا 🙏!

يمكن استخدام Ultralytics YOLO26 لعد الكائنات في الوقت الفعلي من خلال الاستفادة من قدراته المتقدمة في اكتشاف الكائنات. يمكنك اتباع دليلنا المفصل حول عد الكائنات لإعداد YOLO26 لتحليل تدفق الفيديو المباشر. ما عليك سوى تثبيت YOLO26، وتحميل نموذجك، ومعالجة إطارات الفيديو لعد الكائنات ديناميكيًا.

يعزز Ultralytics YOLO26 أنظمة الأمان من خلال توفير اكتشاف الكائنات في الوقت الفعلي وآليات التنبيه. باستخدام YOLO26، يمكنك إنشاء نظام إنذار أمني يقوم بتشغيل التنبيهات عند اكتشاف كائنات جديدة في منطقة المراقبة. تعرف على كيفية إعداد نظام إنذار أمني باستخدام YOLO26 لمراقبة أمنية قوية.

يمكن لـ Ultralytics YOLO26 تحسين أنظمة إدارة الطوابير بشكل كبير من خلال العد والتتبع الدقيق للأشخاص في الطوابير، مما يساعد على تقليل أوقات الانتظار وتحسين كفاءة الخدمة. اتبع دليلنا المفصل حول إدارة الطوابير لتعلم كيفية تطبيق YOLO26 لمراقبة وتحليل فعال للطوابير.

نعم، يمكن استخدام Ultralytics YOLO26 بفعالية لمراقبة التمارين الرياضية عن طريق تتبع وتحليل الروتينات الرياضية في الوقت الفعلي. يتيح ذلك تقييمًا دقيقًا لشكل التمرين والأداء. استكشف دليلنا حول مراقبة التمارين الرياضية لتعلم كيفية إعداد نظام مراقبة التمارين الرياضية المدعوم بالذكاء الاصطناعي باستخدام YOLO26.

يمكن لـ Ultralytics YOLO26 إنشاء خرائط حرارية لتصور كثافة البيانات عبر منطقة معينة، مما يبرز المناطق ذات النشاط أو الاهتمام العالي. هذه الميزة مفيدة بشكل خاص في فهم الأنماط والاتجاهات في مهام الرؤية الحاسوبية المختلفة. تعرف على المزيد حول إنشاء واستخدام الخرائط الحرارية مع YOLO26 لتحليل البيانات وتصورها بشكل شامل.

**Examples:**

Example 1 (python):
```python
import cv2

from ultralytics import solutions

im0 = cv2.imread("path/to/img")

region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]

counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",  # model="yolo26n-obb.pt" for object counting with OBB model.
    # classes=[0, 2],  # count specific classes i.e. person and car with COCO pretrained model.
    # tracker="botsort.yaml"  # Choose trackers i.e "bytetrack.yaml"
)
results = counter(im0)
print(results.in_count)  # display in_counts
print(results.out_count)  # display out_counts
print(results.classwise_count)  # display classwise_count
```

Example 2 (unknown):
```unknown
yolo SOLUTIONS SOLUTION_NAME ARGS
```

Example 3 (unknown):
```unknown
yolo solutions count show=True # for object counting

yolo solutions count source="path/to/video.mp4" # specify video file path
```

---

## دروس تعليمية شاملة لـ Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/guides/

**Contents:**
- دروس تعليمية شاملة لـ Ultralytics YOLO
- الأدلة
- ساهم في أدلتنا
- الأسئلة الشائعة
  - كيف يمكنني تدريب نموذج مخصص للكشف عن الكائنات باستخدام Ultralytics YOLO؟
  - ما هي مقاييس الأداء التي يجب أن أستخدمها لتقييم نموذج YOLO الخاص بي؟
  - لماذا يجب علي استخدام منصة Ultralytics لمشاريع الرؤية الحاسوبية الخاصة بي؟
  - ما هي المشكلات الشائعة التي تواجه أثناء تدريب نموذج YOLO، وكيف يمكنني حلها؟
  - كيف يمكنني نشر نموذج YOLO الخاص بي للكشف عن الكائنات في الوقت الفعلي على الأجهزة الطرفية؟
- تعليقات

مرحبًا بكم في أدلة YOLO من Ultralytics. تغطي برامجنا التعليمية الشاملة جوانب مختلفة من نموذج اكتشاف الكائنات YOLO، بدءًا من التدريب والتنبؤ وصولاً إلى النشر. تم بناء YOLO على PyTorch، ويتميز بسرعته ودقته الاستثنائيتين في مهام اكتشاف الكائنات في الوقت الفعلي.

سواء كنت مبتدئًا أو خبيرًا في التعلم العميق، تقدم برامجنا التعليمية رؤى قيمة حول تنفيذ وتحسين YOLO لمشاريع رؤية الكمبيوتر الخاصة بك.

شاهد: نظرة عامة على أدلة Ultralytics YOLO26

إليك مجموعة من الأدلة المتعمقة لمساعدتك على إتقان جوانب مختلفة من Ultralytics YOLO.

نحن نرحب بمساهمات المجتمع! إذا كنت قد أتقنت جانبًا معينًا من Ultralytics YOLO لم يتم تناوله بعد في أدلتنا، فنحن نشجعك على مشاركة خبرتك. يعد كتابة دليل طريقة رائعة لرد الجميل للمجتمع ومساعدتنا في جعل وثائقنا أكثر شمولاً وسهولة في الاستخدام.

للبدء، يرجى قراءة دليل المساهمة الخاص بنا للحصول على إرشادات حول كيفية فتح طلب سحب (PR). نحن نتطلع إلى مساهماتكم.

يعد تدريب نموذج مخصص للكشف عن الكائنات باستخدام Ultralytics YOLO أمرًا بسيطًا. ابدأ بإعداد مجموعة البيانات الخاصة بك بالتنسيق الصحيح وتثبيت حزمة Ultralytics. استخدم الكود التالي لبدء التدريب:

للحصول على تنسيق مفصل لمجموعة البيانات وخيارات إضافية، راجع دليل نصائح لتدريب النموذج الخاص بنا.

يُعد تقييم أداء نموذج YOLO الخاص بك أمرًا بالغ الأهمية لفهم فعاليته. تتضمن المقاييس الرئيسية متوسط الدقة (mAP)، و التقاطع فوق الاتحاد (IoU)، ودرجة F1. تساعد هذه المقاييس في تقييم دقة ودقة مهام اكتشاف الكائنات. يمكنك معرفة المزيد حول هذه المقاييس وكيفية تحسين النموذج الخاص بك في دليل مقاييس أداء YOLO الخاص بنا.

منصة Ultralytics هي منصة بدون تعليمات برمجية تبسط إدارة وتدريب ونشر نماذج YOLO. تدعم التكامل السلس، والتتبع في الوقت الفعلي، والتدريب السحابي، مما يجعلها مثالية للمبتدئين والمحترفين على حد سواء. اكتشف المزيد عن ميزاتها وكيف يمكنها تبسيط سير عملك من خلال دليل البدء السريع لـ منصة Ultralytics الخاص بنا.

تشمل المشكلات الشائعة أثناء تدريب نموذج YOLO أخطاء تنسيق البيانات، وعدم تطابق بنية النموذج، وعدم كفاية بيانات التدريب. لمعالجة هذه المشكلات، تأكد من تنسيق مجموعة البيانات الخاصة بك بشكل صحيح، وتحقق من وجود إصدارات نموذج متوافقة، وقم بزيادة بيانات التدريب الخاصة بك. للحصول على قائمة شاملة بالحلول، راجع دليل مشكلات YOLO الشائعة الخاص بنا.

يتطلب نشر نماذج YOLO على الأجهزة الطرفية مثل NVIDIA Jetson و Raspberry Pi تحويل النموذج إلى تنسيق متوافق مثل TensorRT أو TFLite. اتبع الإرشادات التفصيلية الخاصة بنا لعمليات النشر على NVIDIA Jetson و Raspberry Pi للبدء في الكشف عن العناصر في الوقت الفعلي على الأجهزة الطرفية. سترشدك هذه الأدلة خلال التثبيت والتكوين وتحسين الأداء.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # Load a pretrained YOLO model
model.train(data="path/to/dataset.yaml", epochs=50)  # Train on custom dataset
```

Example 2 (unknown):
```unknown
yolo task=detect mode=train model=yolo26n.pt data=path/to/dataset.yaml epochs=50
```

---

## عمليات تكامل Ultralytics

**URL:** https://docs.ultralytics.com/ar/integrations/

**Contents:**
- عمليات تكامل Ultralytics
- عمليات تكامل التدريب
- عمليات تكامل النشر
- عمليات تكامل مجموعات البيانات
  - صيغ التصدير
- المساهمة في عمليات التكامل الخاصة بنا
- الأسئلة الشائعة
  - ما هي منصة Ultralytics، وكيف تبسط سير عمل التعلم الآلي؟
  - هل يمكنني تتبع أداء نماذج Ultralytics الخاصة بي باستخدام MLFlow؟
  - ما هي فوائد استخدام Neural Magic لتحسين نماذج YOLO26؟

مرحبًا بك في صفحة عمليات تكامل Ultralytics! تقدم هذه الصفحة نظرة عامة على شراكاتنا مع الأدوات والمنصات المختلفة، المصممة لتبسيط سير عمل تعلم الآلة الخاص بك، وتعزيز إدارة مجموعات البيانات، وتبسيط تدريب النموذج، وتسهيل النشر الفعال.

شاهد: نشر وتكاملات Ultralytics YOLO

Albumentations: عزز نماذج Ultralytics الخاصة بك بتحسينات قوية للصور لتحسين قوة النموذج وتعميمه.

Amazon SageMaker: الاستفادة من Amazon SageMaker لإنشاء وتدريب ونشر نماذج Ultralytics بكفاءة، مما يوفر نظامًا أساسيًا شاملاً لدورة حياة تعلم الآلة.

ClearML: أتمتة سير عمل تعلم الآلة Ultralytics الخاص بك، ومراقبة التجارب، وتعزيز التعاون الجماعي.

Comet ML: عزز تطوير النموذج الخاص بك باستخدام Ultralytics من خلال تتبع ومقارنة وتحسين تجارب تعلم الآلة الخاصة بك.

DVC: تنفيذ التحكم في الإصدار لمشاريع تعلم الآلة Ultralytics الخاصة بك، ومزامنة البيانات والتعليمات البرمجية والنماذج بشكل فعال.

Google Colab: استخدم Google Colab لتدريب وتقييم نماذج Ultralytics في بيئة قائمة على السحابة تدعم التعاون والمشاركة.

IBM Watsonx: تعرف على كيف يبسط IBM Watsonx تدريب وتقييم نماذج Ultralytics بأدوات الذكاء الاصطناعي المتطورة والتكامل السهل ونظام إدارة النماذج المتقدم.

JupyterLab: اكتشف كيفية استخدام بيئة JupyterLab التفاعلية والقابلة للتخصيص لتدريب وتقييم نماذج Ultralytics بسهولة وكفاءة.

Kaggle: استكشف كيف يمكنك استخدام Kaggle لتدريب وتقييم نماذج Ultralytics في بيئة قائمة على السحابة مع مكتبات مثبتة مسبقًا ودعم GPU ومجتمع نابض بالحياة للتعاون والمشاركة.

MLFlow: تبسيط دورة حياة تعلم الآلة بأكملها لنماذج Ultralytics، من التجريب وإمكانية التكاثر إلى النشر.

Neptune: حافظ على سجل شامل لتجارب تعلم الآلة الخاصة بك مع Ultralytics في متجر البيانات الوصفية هذا المصمم لـ MLOps.

Paperspace Gradient: يبسط Paperspace Gradient العمل على مشاريع YOLO26 من خلال توفير أدوات سحابية سهلة الاستخدام لتدريب نماذجك واختبارها ونشرها بسرعة.

Ray Tune: قم بتحسين المعلمات الفائقة لنماذج Ultralytics الخاصة بك على أي نطاق.

TensorBoard: تصور سير عمل تعلم الآلة Ultralytics الخاص بك، وراقب مقاييس النموذج، وعزز التعاون الجماعي.

Ultralytics Platform: الوصول إلى مجتمع من نماذج Ultralytics المدربة مسبقًا والمساهمة فيه.

VS Code: إضافة لـ VS Code توفر مقتطفات التعليمات البرمجية لتسريع سير عمل تطوير Ultralytics وتقدم أمثلة لمساعدة أي شخص على التعلم أو البدء.

Weights & Biases (W&B): راقب التجارب، وتصور المقاييس، وعزز إمكانية التكاثر والتعاون في مشاريع Ultralytics.

Axelera: استكشف مسرّعات Metis و Voyager SDK لتشغيل نماذج Ultralytics باستدلال حافة فعال.

CoreML: CoreML، الذي طورته Apple، هو إطار عمل مصمم لدمج نماذج تعلم الآلة بكفاءة في التطبيقات عبر iOS و macOS و watchOS و tvOS، باستخدام أجهزة Apple لنشر النماذج بشكل فعال وآمن.

ExecuTorch: تم تطوير ExecuTorch بواسطة Meta، وهو الحل الموحد من PyTorch لنشر نماذج Ultralytics YOLO على الأجهزة الطرفية.

Gradio: انشر نماذج Ultralytics باستخدام Gradio لعروض توضيحية تفاعلية للكشف عن الأجسام في الوقت الفعلي.

MNN: تم تطوير MNN بواسطة Alibaba، وهو إطار عمل للتعلم العميق عالي الكفاءة وخفيف الوزن. وهو يدعم الاستدلال والتدريب على نماذج التعلم العميق ولديه أداء رائد في الصناعة للاستدلال والتدريب على الجهاز.

NCNN: تم تطوير NCNN بواسطة Tencent، وهو إطار عمل استنتاج شبكة عصبية فعال مصمم خصيصًا للأجهزة المحمولة. فهو يتيح النشر المباشر لنماذج الذكاء الاصطناعي في التطبيقات، وتحسين الأداء عبر مختلف الأنظمة الأساسية المحمولة.

Neural Magic: استفد من التدريب المدرك للقياس الكمي (QAT) وتقنيات التقليم لتحسين نماذج Ultralytics للحصول على أداء فائق وحجم أصغر.

ONNX: تنسيق مفتوح المصدر تم إنشاؤه بواسطة Microsoft لتسهيل نقل نماذج الذكاء الاصطناعي بين الأطر المختلفة، مما يعزز تنوع ومرونة نشر نماذج Ultralytics.

OpenVINO: مجموعة أدوات Intel لتحسين ونشر نماذج رؤية الكمبيوتر بكفاءة عبر مختلف منصات Intel CPU و GPU.

PaddlePaddle: منصة تعلم عميق مفتوحة المصدر بواسطة Baidu، تتيح PaddlePaddle النشر الفعال لنماذج الذكاء الاصطناعي وتركز على قابلية التوسع للتطبيقات الصناعية.

Rockchip RKNN: تم تطوير RKNN بواسطة Rockchip، وهو إطار عمل متخصص للاستدلال بالشبكات العصبية مُحسَّن لمنصات أجهزة Rockchip، وخاصة وحدات المعالجة العصبية (NPUs) الخاصة بها. فهو يسهل النشر الفعال لنماذج الذكاء الاصطناعي على الأجهزة الطرفية، مما يتيح استدلالًا عالي الأداء في التطبيقات في الوقت الفعلي.

Seeed Studio reCamera: تم تطوير reCamera بواسطة Seeed Studio، وهو جهاز متطور للذكاء الاصطناعي المتطور مصمم لتطبيقات رؤية الكمبيوتر في الوقت الفعلي. مدعوم بمعالج SG200X المستند إلى RISC-V، فهو يوفر استدلالًا عالي الأداء للذكاء الاصطناعي مع كفاءة في استخدام الطاقة. إن تصميمه المعياري وقدرات معالجة الفيديو المتقدمة ودعمه للنشر المرن يجعله خيارًا مثاليًا لحالات استخدام مختلفة، بما في ذلك مراقبة السلامة والتطبيقات البيئية والتصنيع.

SONY IMX500: قم بتحسين ونشر نماذج Ultralytics YOLO26 على كاميرات Raspberry Pi AI المزودة بمستشعر IMX500 للحصول على أداء سريع ومنخفض الطاقة.

TensorRT: تم تطوير إطار عمل الاستدلال للتعلم العميق عالي الأداء وتنسيق النموذج هذا بواسطة NVIDIA، وهو يحسن نماذج الذكاء الاصطناعي لتحقيق سرعة وكفاءة متسارعة على وحدات معالجة الرسومات NVIDIA، مما يضمن نشرًا مبسطًا.

TF GraphDef: تم تطوير GraphDef بواسطة Google، وهو تنسيق TensorFlow لتمثيل الرسوم البيانية للحساب، مما يتيح التنفيذ الأمثل لنماذج تعلم الآلة عبر أجهزة متنوعة.

TF SavedModel: تم تطوير TF SavedModel بواسطة Google، وهو تنسيق تسلسل عالمي لنماذج TensorFlow، مما يتيح سهولة المشاركة والنشر عبر مجموعة واسعة من الأنظمة الأساسية، من الخوادم إلى الأجهزة الطرفية.

TF.js: تم تطوير TF.js بواسطة Google لتسهيل تعلم الآلة في المتصفحات و Node.js، ويسمح بالنشر المستند إلى JavaScript لنماذج ML.

TFLite: تم تطوير TFLite بواسطة Google، وهو إطار عمل خفيف الوزن لنشر نماذج تعلم الآلة على الأجهزة المحمولة والأجهزة الطرفية، مما يضمن استدلالًا سريعًا وفعالًا مع الحد الأدنى من استهلاك الذاكرة.

TFLite Edge TPU: تم تطويره بواسطة Google لتحسين نماذج TensorFlow Lite على Edge TPUs، يضمن تنسيق النموذج هذا حوسبة متطورة عالية السرعة وفعالة.

TorchScript: تم تطوير TorchScript كجزء من إطار عمل PyTorch، وهو يتيح التنفيذ والنشر الفعالين لنماذج تعلم الآلة في بيئات إنتاج متنوعة دون الحاجة إلى تبعيات Python.

نحن ندعم أيضًا مجموعة متنوعة من تنسيقات تصدير النماذج للنشر في بيئات مختلفة. فيما يلي التنسيقات المتاحة:

استكشف الروابط لمعرفة المزيد حول كل تكامل وكيفية تحقيق أقصى استفادة منها مع Ultralytics. راجع export التفاصيل في تصدير التنبؤ.

نحن متحمسون دائمًا لرؤية كيف يدمج المجتمع Ultralytics YOLO مع التقنيات والأدوات والمنصات الأخرى! إذا نجحت في دمج YOLO مع نظام جديد أو لديك رؤى قيمة لمشاركتها، ففكر في المساهمة في وثائق التكامل الخاصة بنا.

من خلال كتابة دليل أو برنامج تعليمي، يمكنك المساعدة في توسيع وثائقنا وتقديم أمثلة واقعية تفيد المجتمع. إنها طريقة ممتازة للمساهمة في النظام البيئي المتنامي حول Ultralytics YOLO.

للمساهمة، يرجى الاطلاع على دليل المساهمة الخاص بنا للحصول على إرشادات حول كيفية إرسال طلب سحب (PR) 🛠️. نحن في انتظار مساهماتكم بفارغ الصبر!

دعونا نتعاون لجعل النظام البيئي Ultralytics YOLO أكثر اتساعًا وغنى بالميزات 🙏!

Ultralytics Platform هي منصة سحابية مصممة لجعل سير عمل التعلم الآلي لنماذج Ultralytics سلسًا وفعالًا. باستخدام هذه الأداة، يمكنك بسهولة تحميل مجموعات البيانات، وتدريب النماذج، وإجراء real-time tracking، ونشر نماذج YOLO دون الحاجة إلى مهارات برمجة واسعة. تعمل المنصة كمساحة عمل مركزية حيث يمكنك إدارة خط أنابيب التعلم الآلي بالكامل من إعداد البيانات إلى النشر. يمكنك استكشاف الميزات الرئيسية على صفحة Ultralytics Platform والبدء بسرعة باستخدام دليل Quickstart الخاص بنا.

نعم يمكنك ذلك. يتيح دمج MLFlow مع نماذج Ultralytics تتبع التجارب وتحسين إمكانية التكرار وتبسيط دورة حياة تعلم الآلة بأكملها. يمكن العثور على إرشادات مفصلة لإعداد هذا التكامل على صفحة تكامل MLFlow. هذا التكامل مفيد بشكل خاص لمراقبة مقاييس النموذج ومقارنة عمليات التدريب المختلفة وإدارة سير عمل تعلم الآلة بكفاءة. يوفر MLFlow نظامًا أساسيًا مركزيًا لتسجيل المعلمات والمقاييس والتحف، مما يسهل فهم سلوك النموذج وإجراء تحسينات تعتمد على البيانات.

Neural Magic تعمل على تحسين نماذج YOLO26 من خلال الاستفادة من تقنيات مثل التدريب المدرك للكمية (QAT) والتقليم، مما ينتج عنه نماذج أصغر حجمًا وذات كفاءة عالية تعمل بشكل أفضل على الأجهزة محدودة الموارد. تحقق من صفحة تكامل Neural Magic لمعرفة كيفية تنفيذ هذه التحسينات للحصول على أداء فائق ونماذج أكثر رشاقة. وهذا مفيد بشكل خاص للنشر على الأجهزة الطرفية حيث تكون الموارد الحاسوبية مقيدة. يمكن لمحرك DeepSparse من Neural Magic أن يوفر استدلالًا أسرع بما يصل إلى 6 أضعاف على وحدات CPU، مما يجعل من الممكن تشغيل النماذج المعقدة دون الحاجة إلى أجهزة متخصصة.

لنشر نماذج Ultralytics YOLO باستخدام Gradio لعروض الكشف عن الكائنات التفاعلية، يمكنك اتباع الخطوات الموضحة في صفحة تكامل Gradio. يتيح لك Gradio إنشاء واجهات ويب سهلة الاستخدام للاستدلال على النماذج في الوقت الفعلي، مما يجعله أداة ممتازة لعرض قدرات نموذج YOLO الخاص بك بتنسيق سهل الاستخدام مناسب لكل من المطورين والمستخدمين النهائيين. باستخدام بضعة أسطر فقط من التعليمات البرمجية، يمكنك إنشاء تطبيقات تفاعلية توضح أداء النموذج الخاص بك على مدخلات مخصصة، مما يسهل فهم وتقييم حلول رؤية الكمبيوتر الخاصة بك بشكل أفضل.

---

## قياس أداء النموذج باستخدام Ultralytics YOLO

**URL:** https://docs.ultralytics.com/ar/modes/benchmark/

**Contents:**
- قياس أداء النموذج باستخدام Ultralytics YOLO
- تصور المقارنة المعيارية
- مقدمة
- لماذا تعتبر المقارنة المعيارية حاسمة؟
  - المقاييس الرئيسية في وضع المقارنة المعيارية
  - تنسيقات التصدير المدعومة
- أمثلة الاستخدام
- الوسائط
- صيغ التصدير
- الأسئلة الشائعة

قد تحتاج إلى تحديث الصفحة لعرض الرسوم البيانية بشكل صحيح بسبب مشكلات محتملة في ملفات تعريف الارتباط.

بمجرد تدريب نموذجك والتحقق منه، فإن الخطوة المنطقية التالية هي تقييم أدائه في سيناريوهات واقعية مختلفة. يخدم وضع اختبار الأداء في Ultralytics YOLO26 هذا الغرض من خلال توفير إطار عمل قوي لتقييم سرعة ودقة نموذجك عبر مجموعة من صيغ التصدير.

شاهد: اختبار أداء نماذج Ultralytics YOLO26 | كيفية مقارنة أداء النموذج على أجهزة مختلفة؟

شغّل اختبارات أداء YOLO26n عبر جميع صيغ التصدير المدعومة (ONNX، TensorRT، إلخ.). راجع قسم الوسائط أدناه للحصول على قائمة كاملة بخيارات التصدير.

وسائط مثل model, data, imgsz, half, device, verbose و format تمنح المستخدمين المرونة اللازمة لضبط المعايير بدقة لتلبية احتياجاتهم الخاصة ومقارنة أداء تنسيقات التصدير المختلفة بسهولة.

ستحاول القياسات التشغيل تلقائيًا على جميع تنسيقات التصدير الممكنة المدرجة أدناه. بدلاً من ذلك، يمكنك تشغيل القياسات لتنسيق معين باستخدام format الوسيطة، التي تقبل أيًا من التنسيقات المذكورة أدناه.

اطلع على التفاصيل الكاملة export التفاصيل في تصدير التنبؤ.

توفر Ultralytics YOLO26 وضع اختبار الأداء لتقييم أداء نموذجك عبر صيغ تصدير مختلفة. يوفر هذا الوضع رؤى حول المقاييس الرئيسية مثل متوسط الدقة المتوسطة (mAP50-95)، والدقة، ووقت الاستدلال بالمللي ثانية. لتشغيل اختبارات الأداء، يمكنك استخدام أوامر python أو CLI. على سبيل المثال، لاختبار الأداء على GPU:

لمزيد من التفاصيل حول وسائط القياس، قم بزيارة قسم الوسائط Arguments.

يسمح لك تصدير نماذج YOLO26 إلى صيغ مختلفة مثل ONNX و TensorRT و OpenVINO بتحسين الأداء بناءً على بيئة النشر الخاصة بك. على سبيل المثال:

تعزز هذه التنسيقات كلاً من سرعة ودقة النماذج الخاصة بك، مما يجعلها أكثر كفاءة لمختلف التطبيقات الواقعية. قم بزيارة صفحة تصدير للحصول على تفاصيل كاملة.

يعد تقييم أداء نماذج YOLO26 الخاصة بك أمرًا ضروريًا لعدة أسباب:

تساعد المقاييس الرئيسية مثل mAP50-95 ودقة Top-5 ووقت الاستدلال في إجراء هذه التقييمات. راجع قسم Key Metrics لمزيد من المعلومات.

يدعم YOLO26 مجموعة متنوعة من تنسيقات التصدير، كل منها مصمم خصيصًا لأجهزة وحالات استخدام معينة:

للحصول على قائمة كاملة بالتنسيقات المدعومة ومزاياها، تحقق من قسم تنسيقات التصدير المدعومة.

عند تشغيل المعايير، يمكن تخصيص العديد من الحجج لتناسب الاحتياجات المحددة:

للحصول على قائمة كاملة بالوسائط، ارجع إلى قسم الوسائط.

**Examples:**

Example 1 (sql):
```sql
from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)

# Benchmark specific export format
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, format="onnx")
```

Example 2 (markdown):
```markdown
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 half=False device=0

# Benchmark specific export format
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 format=onnx
```

Example 3 (sql):
```sql
from ultralytics.utils.benchmarks import benchmark

# Benchmark on GPU
benchmark(model="yolo26n.pt", data="coco8.yaml", imgsz=640, half=False, device=0)
```

Example 4 (unknown):
```unknown
yolo benchmark model=yolo26n.pt data='coco8.yaml' imgsz=640 half=False device=0
```

---

## مربعات الإحاطة الموجهة الكشف عن الكائنات

**URL:** https://docs.ultralytics.com/ar/tasks/obb/

**Contents:**
- مربعات الإحاطة الموجهة الكشف عن الكائنات
- عينات مرئية
- النماذج
- تدريب
  - تنسيق مجموعة البيانات
- التحقق
- توقع
- تصدير
- تطبيقات عملية في أرض الواقع
- الأسئلة الشائعة

يتجاوز الكشف عن الكائنات الموجهة خطوة أخرى الكشف القياسي عن الكائنات من خلال إدخال زاوية إضافية لتحديد مواقع الكائنات بدقة أكبر في الصورة.

إن ناتج كاشف الكائنات الموجهة هو مجموعة من المربعات المحيطة المدورة التي تحيط بدقة بالكائنات الموجودة في الصورة، جنبًا إلى جنب مع تسميات الفئات ودرجات الثقة لكل مربع. تكون المربعات المحيطة الموجهة مفيدة بشكل خاص عندما تظهر الكائنات بزوايا مختلفة، كما هو الحال في الصور الجوية، حيث قد تتضمن المربعات المحيطة التقليدية المحاذية للمحور خلفية غير ضرورية.

تستخدم نماذج YOLO26 OBB الـ -obb لاحقة، أي، yolo26n-obb.pt، ويتم تدريبها مسبقًا على DOTAv1.

شاهد: اكتشاف الأجسام باستخدام صناديق الإحاطة الموجهة Ultralytics YOLO (YOLO-OBB)

نماذج YOLO26 OBB المدربة مسبقًا معروضة هنا، والتي تم تدريبها مسبقًا على مجموعة بيانات DOTAv1.

يتم تنزيل النماذج تلقائيًا من أحدث إصدارات Ultralytics release عند الاستخدام الأول.

درب YOLO26n-obb على مجموعة بيانات DOTA8 لمدة 100 epoch بحجم صورة 640. للحصول على قائمة كاملة بالوسائط المتاحة، راجع صفحة التكوين.

تقتصر زوايا OBB على النطاق 0-90 درجة (باستثناء 90). الزوايا الأكبر من أو تساوي 90 درجة غير مدعومة.

شاهد: كيفية تدريب نماذج Ultralytics YOLO-OBB (صناديق الإحاطة الموجهة) على مجموعة بيانات DOTA باستخدام منصة Ultralytics

يمكن العثور على تنسيق مجموعة بيانات OBB بالتفصيل في دليل مجموعة البيانات. يحدد تنسيق YOLO OBB المربعات المحيطة بنقاط الزاوية الأربعة الخاصة بهم مع إحداثيات طبيعية بين 0 و 1، باتباع هذا الهيكل:

داخليًا، تعالج YOLO الخسائر والمخرجات في xywhr التنسيق، الذي يمثل مربع إحاطةنقطة المركز (xy)، والعرض، والارتفاع، والدوران.

تحقق من صحة نموذج YOLO26n-obb المدرب الدقة على مجموعة بيانات DOTA8. لا توجد حاجة إلى وسائط حيث أن model يحتفظ بالتدريب الخاص به data والوسائط كسمات للنموذج.

استخدم نموذج YOLO26n-obb مدربًا لتشغيل التنبؤات على الصور.

شاهد: كيفية الكشف عن خزانات التخزين وتتبعها باستخدام Ultralytics YOLO-OBB | مربعات الإحاطة الموجهة | DOTA

اطلع على التفاصيل الكاملة predict لأوضاع التشغيل في صفحة توقع التنبؤ.

صدّر نموذج YOLO26n-obb إلى تنسيق مختلف مثل ONNX، CoreML، إلخ.

تنسيقات تصدير YOLO26-obb المتاحة موجودة في الجدول أدناه. يمكنك التصدير إلى أي تنسيق باستخدام الـ format الوسيطة، أي format='onnx' أو format='engine'. يمكنك التنبؤ أو التحقق مباشرة على النماذج المصدرة، أي، yolo predict model=yolo26n-obb.onnx. يتم عرض أمثلة الاستخدام لنموذجك بعد اكتمال التصدير.

اطلع على التفاصيل الكاملة export التفاصيل في تصدير التنبؤ.

اكتشاف OBB باستخدام YOLO26 له العديد من التطبيقات العملية عبر مختلف الصناعات:

تستفيد هذه التطبيقات من قدرة OBB على احتواء الأجسام بدقة في أي زاوية، مما يوفر كشفًا أكثر دقة من الصناديق المحيطة التقليدية.

تتضمن مربعات الإحاطة الموجهة (OBB) زاوية إضافية لتحسين دقة تحديد موقع الكائن في الصور. على عكس مربعات الإحاطة العادية، وهي مستطيلات محاذاة للمحاور، يمكن أن تدور OBBs لتناسب اتجاه الكائن بشكل أفضل. وهذا مفيد بشكل خاص للتطبيقات التي تتطلب تحديد موضع دقيق للكائن، مثل الصور الجوية أو صور الأقمار الصناعية (دليل مجموعة البيانات).

لتدريب نموذج YOLO26n-obb باستخدام مجموعة بيانات مخصصة، اتبع المثال أدناه باستخدام python أو CLI:

لمزيد من وسائط التدريب، تحقق من قسم التكوين.

نماذج YOLO26-OBB مدربة مسبقًا على مجموعات بيانات مثل DOTAv1، ولكن يمكنك استخدام أي مجموعة بيانات منسقة لـ obb. يمكن العثور على معلومات مفصلة حول تنسيقات مجموعات بيانات obb في دليل مجموعات البيانات.

تصدير نموذج YOLO26-OBB إلى تنسيق ONNX أمر مباشر باستخدام python أو CLI:

لمزيد من تنسيقات وتفاصيل التصدير، راجع صفحة تصدير.

للتحقق من صحة نموذج YOLO26n-obb، يمكنك استخدام أوامر python أو CLI كما هو موضح أدناه:

راجع تفاصيل التحقق الكاملة في قسم Val.

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

## مساعدة

**URL:** https://docs.ultralytics.com/ar/help/

**Contents:**
- مساعدة
- الأسئلة الشائعة
  - ما هو Ultralytics YOLO وكيف يفيد مشاريع تعلم الآلة الخاصة بي؟
  - كيف يمكنني المساهمة في مستودعات Ultralytics YOLO؟
  - لماذا يجب علي استخدام منصة Ultralytics لمشاريع التعلم الآلي الخاصة بي؟
  - ما هو التكامل المستمر (CI) في Ultralytics، وكيف يضمن جودة عالية للكود؟
  - كيف تتعامل Ultralytics مع خصوصية البيانات؟
- تعليقات

مرحبًا بك في صفحة مساعدة Ultralytics. تجمع هذه الصفحة أدلة عملية وسياسات وأسئلة متكررة لدعم عملك مع نماذج ومستودعات Ultralytics YOLO.

نحن نشجعك على مراجعة هذه الموارد لتجربة سلسة ومثمرة. إذا كنت بحاجة إلى دعم إضافي، تواصل معنا عبر GitHub Issues أو مجتمع Ultralytics.

Ultralytics YOLO (You Only Look Once) هو نموذج متطور لكشف الكائنات في الوقت الفعلي. يقدم أحدث إصدار له، YOLO26، استدلالًا أسرع وأخف وزنًا وخاليًا من NMS من البداية إلى النهاية، ومُحسّنًا للأجهزة الطرفية ومنخفضة الطاقة، مما يجعله مثاليًا لمجموعة واسعة من التطبيقات، بدءًا من تحليلات الفيديو في الوقت الفعلي وصولًا إلى أبحاث التعلم الآلي المتقدمة. لقد جعلت كفاءة YOLO في كشف الكائنات في الصور ومقاطع الفيديو منه الحل الأمثل للشركات والباحثين الذين يتطلعون إلى دمج قدرات الرؤية الحاسوبية القوية في مشاريعهم.

لمزيد من التفاصيل حول YOLO26، قم بزيارة وثائق YOLO26.

تعتبر المساهمة في مستودعات Ultralytics YOLO أمرًا مباشرًا. ابدأ بمراجعة دليل المساهمة لفهم البروتوكولات الخاصة بتقديم طلبات السحب والإبلاغ عن الأخطاء والمزيد. ستحتاج أيضًا إلى توقيع اتفاقية ترخيص المساهم (CLA) لضمان الاعتراف القانوني بمساهماتك. للإبلاغ الفعال عن الأخطاء، راجع دليل الحد الأدنى من الأمثلة القابلة لإعادة الإنتاج (MRE).

تقدم منصة Ultralytics حلاً سلسًا وبدون تعليمات برمجية لإدارة مشاريع التعلم الآلي الخاصة بك. تمكنك من إنشاء نماذج الذكاء الاصطناعي مثل YOLO26 وتدريبها ونشرها بسهولة. تشمل الميزات الفريدة التدريب السحابي، والتتبع في الوقت الفعلي، وإدارة مجموعات البيانات البديهية. تبسط منصة Ultralytics سير العمل بأكمله، من معالجة البيانات إلى نشر النماذج، مما يجعلها أداة لا غنى عنها لكل من المبتدئين والمستخدمين المتقدمين.

للبدء، قم بزيارة دليل البدء السريع لمنصة Ultralytics.

يتضمن التكامل المستمر (CI) في Ultralytics عمليات مؤتمتة تضمن سلامة وجودة قاعدة التعليمات البرمجية. يتضمن إعداد CI الخاص بنا نشر Docker، وفحوصات الروابط المعطلة، وتحليل CodeQL، ونشر PyPI. تساعد هذه العمليات في الحفاظ على مستودعات مستقرة وآمنة عن طريق التشغيل التلقائي للاختبارات والتحقق من التعليمات البرمجية الجديدة.

تعرف على المزيد في دليل التكامل المستمر (CI).

تأخذ Ultralytics خصوصية البيانات على محمل الجد. تحدد سياسة الخصوصية الخاصة بنا كيف نجمع ونستخدم البيانات المجهولة لتحسين حزمة YOLO مع إعطاء الأولوية لخصوصية المستخدم والتحكم فيه. نحن نلتزم بلوائح حماية البيانات الصارمة لضمان أمان معلوماتك في جميع الأوقات.

لمزيد من المعلومات، راجع سياسة الخصوصية الخاصة بنا.

---

## منصة Ultralytics

**URL:** https://docs.ultralytics.com/ar/platform/

**Contents:**
- منصة Ultralytics
- ما هي منصة Ultralytics؟
- سير العمل: البيانات ← التدريب ← النشر
- البنية التحتية متعددة المناطق
- الميزات الرئيسية
  - إعداد البيانات
  - تدريب النماذج
  - النشر
  - إدارة الحساب
- روابط سريعة

منصة Ultralytics هي منصة رؤية حاسوبية شاملة ومتكاملة تبسط سير عمل التعلم الآلي (ML) بالكامل، بدءًا من إعداد البيانات وصولاً إلى نشر النماذج. مصممة للفرق والأفراد الذين يحتاجون إلى حلول رؤية حاسوبية جاهزة للإنتاج دون تعقيدات البنية التحتية.

شاهد: البدء باستخدام منصة Ultralytics

صُممت منصة Ultralytics لتحل محل أدوات تعلم الآلة المجزأة بحل موحد. وهي تجمع إمكانيات كل من:

منصة شاملة تدعم YOLO11 YOLO26 و YOLO11 بشكل أصلي.

تتبع المنصة سير عمل مبسطًا من ثلاث مراحل:

تبقى بياناتك في منطقتك. تدير منصة Ultralytics البنية التحتية في ثلاث مناطق عالمية:

تختار منطقتك أثناء عملية الإعداد، وتبقى جميع بياناتك ونماذجك وعمليات النشر في تلك المنطقة.

ابدأ باستخدام هذه الموارد:

للبدء باستخدام منصة Ultralytics:

للحصول على دليل مفصل، راجع صفحة البدء السريع.

منصة Ultralytics تقدم:

منصة Ultralytics تدعم أنواعًا متعددة من وحدات GPU للتدريب السحابي:

انظر تدريب السحابة للحصول على الأسعار الكاملة GPU .

يمكنك تدريب النماذج في أي مكان وبث المقاييس إلى المنصة.

يتطلب دمج المنصة ultralytics>=8.4.0. الإصدارات الأقدم لن تعمل مع المنصة.

راجع التدريب السحابي لمزيد من التفاصيل حول التدريب عن بُعد.

تتضمن المنصة محرر تعليقات توضيحية كامل الميزات يدعم:

راجع التعليق التوضيحي للدليل الكامل.

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

## مهام الرؤية الحاسوبية المدعومة من Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/ar/tasks/

**Contents:**
- مهام الرؤية الحاسوبية المدعومة من Ultralytics YOLO26
- اكتشاف
- تجزئة الصور
- التصنيف
- تقدير الوضعية
- OBB
- الخلاصة
- الأسئلة الشائعة
  - ما هي مهام الرؤية الحاسوبية التي يمكن لـ Ultralytics YOLO26 أداؤها؟
  - كيف أستخدم Ultralytics YOLO26 للكشف عن الكائنات؟

Ultralytics YOLO26 هو إطار عمل ذكاء اصطناعي متعدد الاستخدامات يدعم العديد من مهام الرؤية الحاسوبية. يمكن استخدام الإطار لأداء الكشف، التجزئة، OBB، التصنيف، وتقدير الوضعيات. لكل من هذه المهام هدف وحالة استخدام مختلفين، مما يتيح لك معالجة تحديات رؤية حاسوبية متنوعة بإطار عمل واحد.

شاهد: استكشف مهام Ultralytics YOLO: الكشف عن الكائنات، التجزئة، OBB، التتبع، وتقدير الوضع.

الكشف هو المهمة الأساسية المدعومة من قبل YOLO26. تتضمن تحديد الكائنات في صورة أو إطار فيديو ورسم مربعات إحاطة حولها. يتم تصنيف الكائنات المكتشفة إلى فئات مختلفة بناءً على ميزاتها. يمكن لـ YOLO26 الكشف عن كائنات متعددة في صورة أو إطار فيديو واحد بدقة وسرعة عاليتين، مما يجعلها مثالية للتطبيقات في الوقت الفعلي مثل أنظمة المراقبة والمركبات ذاتية القيادة.

تأخذ الـ segmentation عملية detect الكائنات إلى أبعد من ذلك من خلال إنتاج أقنعة على مستوى البكسل لكل كائن. هذه الدقة مفيدة لتطبيقات مثل التصوير الطبي، والتحليل الزراعي، ومراقبة جودة التصنيع.

يتضمن التصنيف تصنيف الصور بأكملها بناءً على محتواها. هذه المهمة ضرورية لتطبيقات مثل تصنيف المنتجات في التجارة الإلكترونية، والإشراف على المحتوى، ومراقبة الحياة البرية.

تقدير الوضعيات تكتشف نقاطًا رئيسية محددة في الصور أو إطارات الفيديو لتتبع الحركات أو تقدير الوضعيات. يمكن لهذه النقاط الرئيسية أن تمثل مفاصل بشرية، ملامح وجه، أو نقاط اهتمام أخرى مهمة. تتفوق YOLO26 في الكشف عن النقاط الرئيسية بدقة وسرعة عاليتين، مما يجعلها ذات قيمة لـ تطبيقات اللياقة البدنية، تحليلات الرياضة، والتفاعل بين الإنسان والحاسوب.

الكشف عن مربعات الإحاطة الموجهة (OBB) يعزز الكشف التقليدي عن الكائنات بإضافة زاوية توجيه لتحديد موقع الكائنات الدوارة بشكل أفضل. هذه القدرة ذات قيمة خاصة لـ تحليل الصور الجوية، معالجة المستندات، والتطبيقات الصناعية حيث تظهر الكائنات بزوايا مختلفة. توفر YOLO26 دقة وسرعة عاليتين للكشف عن الكائنات الدوارة في سيناريوهات متنوعة.

يدعم Ultralytics YOLO26 مهام رؤية حاسوبية متعددة، بما في ذلك الكشف، التجزئة، التصنيف، الكشف عن الكائنات الموجهة، والكشف عن النقاط الرئيسية. تتناول كل مهمة احتياجات محددة في مشهد الرؤية الحاسوبية، بدءًا من تحديد الكائنات الأساسي وصولاً إلى تحليل الوضعيات المفصل. من خلال فهم قدرات وتطبيقات كل مهمة، يمكنك اختيار النهج الأنسب لتحديات الرؤية الحاسوبية الخاصة بك والاستفادة من ميزات YOLO26 القوية لبناء حلول فعالة.

Ultralytics YOLO26 هو إطار عمل ذكاء اصطناعي متعدد الاستخدامات قادر على أداء مهام رؤية حاسوبية متنوعة بدقة وسرعة عاليتين. تشمل هذه المهام:

لاستخدام Ultralytics YOLO26 للكشف عن الكائنات، اتبع الخطوات التالية:

للحصول على تعليمات أكثر تفصيلاً، تحقق من أمثلة الكشف الخاصة بنا.

يوفر استخدام YOLO26 لمهام التجزئة العديد من المزايا:

تعرّف على المزيد حول فوائد وحالات استخدام YOLO26 للتجزئة في قسم تجزئة الصور.

نعم، يمكن لـ Ultralytics YOLO26 أن يؤدي تقدير الوضعيات واكتشاف النقاط الرئيسية بفعالية بدقة وسرعة عالية. هذه الميزة مفيدة بشكل خاص لتتبع الحركات في تحليلات الرياضة، والرعاية الصحية، وتطبيقات التفاعل بين الإنسان والحاسوب. يكتشف YOLO26 النقاط الرئيسية في صورة أو إطار فيديو، مما يسمح بتقدير دقيق للوضعيات.

لمزيد من التفاصيل ونصائح التنفيذ، قم بزيارة أمثلة تقدير الوضع الخاصة بنا.

يوفر اكتشاف الكائنات الموجهة (OBB) باستخدام YOLO26 دقة مُعززة من خلال اكتشاف الكائنات بمعامل زاوية إضافي. هذه الميزة مفيدة للتطبيقات التي تتطلب تحديدًا دقيقًا لمواقع الكائنات الدوارة، مثل تحليل الصور الجوية وأتمتة المستودعات.

تحقق من قسم الكشف عن الكائنات الموجهة لمزيد من التفاصيل والأمثلة.

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
