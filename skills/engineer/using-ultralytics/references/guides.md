# Raw-Ultralytics - Guides

**Pages:** 13

---

## Advanced Data Visualization: Heatmaps using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/heatmaps/

**Contents:**
- Advanced Data Visualization: Heatmaps using Ultralytics YOLO26 🚀
- Introduction to Heatmaps
- Why Choose Heatmaps for Data Analysis?
- Real World Applications
  - Heatmap() Arguments
    - Heatmap COLORMAPs
- How Heatmaps Work in Ultralytics YOLO26
- FAQ
  - How does Ultralytics YOLO26 generate heatmaps and what are their benefits?
  - Can I use Ultralytics YOLO26 to perform object tracking and generate a heatmap simultaneously?

A heatmap generated with Ultralytics YOLO26 transforms complex data into a vibrant, color-coded matrix. This visual tool employs a spectrum of colors to represent varying data values, where warmer hues indicate higher intensities and cooler tones signify lower values. Heatmaps excel in visualizing intricate data patterns, correlations, and anomalies, offering an accessible and engaging approach to data interpretation across diverse domains.

Watch: Heatmaps using Ultralytics YOLO26

Heatmaps using Ultralytics YOLO

Here's a table with the Heatmap arguments:

You can also apply different track arguments in the Heatmap solution.

Additionally, the supported visualization arguments are listed below:

These colormaps are commonly used for visualizing data with different color representations.

The Heatmap solution in Ultralytics YOLO26 extends the ObjectCounter class to generate and visualize movement patterns in video streams. When initialized, the solution creates a blank heatmap layer that gets updated as objects move through the frame.

For each detected object, the solution:

The result is a dynamic visualization that builds up over time, revealing traffic patterns, crowd movements, or other spatial behaviors in your video data.

Ultralytics YOLO26 generates heatmaps by transforming complex data into a color-coded matrix where different hues represent data intensities. Heatmaps make it easier to visualize patterns, correlations, and anomalies in the data. Warmer hues indicate higher values, while cooler tones represent lower values. The primary benefits include intuitive visualization of data distribution, efficient pattern detection, and enhanced spatial analysis for decision-making. For more details and configuration options, refer to the Heatmap Configuration section.

Yes, Ultralytics YOLO26 supports object tracking and heatmap generation concurrently. This can be achieved through its Heatmap solution integrated with object tracking models. To do so, you need to initialize the heatmap object and use YOLO26's tracking capabilities. Here's a simple example:

For further guidance, check the Tracking Mode page.

Ultralytics YOLO26 heatmaps are specifically designed for integration with its object detection and tracking models, providing an end-to-end solution for real-time data analysis. Unlike generic visualization tools like OpenCV or Matplotlib, YOLO26 heatmaps are optimized for performance and automated processing, supporting features like persistent tracking, decay factor adjustment, and real-time video overlay. For more information on YOLO26's unique features, visit the Ultralytics YOLO26 Introduction.

You can visualize specific object classes by specifying the desired classes in the track() method of the YOLO model. For instance, if you only want to visualize cars and persons (assuming their class indices are 0 and 2), you can set the classes parameter accordingly.

Ultralytics YOLO26 offers seamless integration of advanced object detection and real-time heatmap generation, making it an ideal choice for businesses looking to visualize data more effectively. The key advantages include intuitive data distribution visualization, efficient pattern detection, and enhanced spatial analysis for better decision-making. Additionally, YOLO26's cutting-edge features such as persistent tracking, customizable colormaps, and support for various export formats make it superior to other tools like TensorFlow and OpenCV for comprehensive data analysis. Learn more about business applications at Ultralytics Plans.

**Examples:**

Example 1 (markdown):
```markdown
# Run a heatmap example
yolo solutions heatmap show=True

# Pass a source video
yolo solutions heatmap source="path/to/video.mp4"

# Pass a custom colormap
yolo solutions heatmap colormap=cv2.COLORMAP_INFERNO

# Heatmaps + object counting
yolo solutions heatmap region="[(20, 400), (1080, 400), (1080, 360), (20, 360)]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("heatmap_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# For object counting with heatmap, you can pass region points.
# region_points = [(20, 400), (1080, 400)]                                      # line points
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]              # rectangle region
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360), (20, 400)]   # polygon points

# Initialize heatmap object
heatmap = solutions.Heatmap(
    show=True,  # display the output
    model="yolo26n.pt",  # path to the YOLO26 model file
    colormap=cv2.COLORMAP_PARULA,  # colormap of heatmap
    # region=region_points,  # object counting with heatmaps, you can pass region_points
    # classes=[0, 2],  # generate heatmap for specific classes, e.g., person and car.
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = heatmap(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
heatmap = solutions.Heatmap(colormap=cv2.COLORMAP_PARULA, show=True, model="yolo26n.pt")

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        break
    results = heatmap(im0)
cap.release()
cv2.destroyAllWindows()
```

Example 4 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
heatmap = solutions.Heatmap(show=True, model="yolo26n.pt", classes=[0, 2])

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        break
    results = heatmap(im0)
cap.release()
cv2.destroyAllWindows()
```

---

## Analytics using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/analytics/

**Contents:**
- Analytics using Ultralytics YOLO26
- Introduction
  - Visual Samples
  - Why Graphs are Important
  - Analytics Arguments
- Conclusion
- FAQ
  - How do I create a line graph using Ultralytics YOLO26 Analytics?
  - What are the benefits of using Ultralytics YOLO26 for creating bar plots?
  - Why should I use Ultralytics YOLO26 for creating pie charts in my data visualization projects?

This guide provides a comprehensive overview of three fundamental types of data visualizations: line graphs, bar plots, and pie charts. Each section includes step-by-step instructions and code snippets on how to create these visualizations using Python.

Watch: How to generate Analytical Graphs using Ultralytics | Line Graphs, Bar Plots, Area and Pie Charts

Analytics using Ultralytics YOLO

Here's a table outlining the Analytics arguments:

You can also leverage different track arguments in the Analytics solution.

Additionally, the following visualization arguments are supported:

Understanding when and how to use different types of visualizations is crucial for effective data analysis. Line graphs, bar plots, and pie charts are fundamental tools that can help you convey your data's story more clearly and effectively. The Ultralytics YOLO26 Analytics solution provides a streamlined way to generate these visualizations from your object detection and tracking results, making it easier to extract meaningful insights from your visual data.

To create a line graph using Ultralytics YOLO26 Analytics, follow these steps:

For further details on configuring the Analytics class, visit the Analytics using Ultralytics YOLO26 section.

Using Ultralytics YOLO26 for creating bar plots offers several benefits:

Use the following example to generate a bar plot:

To learn more, visit the Bar Plot section in the guide.

Ultralytics YOLO26 is an excellent choice for creating pie charts because:

Here's a quick example:

For more information, refer to the Pie Chart section in the guide.

Yes, Ultralytics YOLO26 can be used to track objects and dynamically update visualizations. It supports tracking multiple objects in real-time and can update various visualizations like line graphs, bar plots, and pie charts based on the tracked objects' data.

Example for tracking and updating a line graph:

To learn about the complete functionality, see the Tracking section.

Ultralytics YOLO26 stands out from other object detection solutions like OpenCV and TensorFlow for multiple reasons:

For more detailed comparisons and use cases, explore our Ultralytics Blog.

**Examples:**

Example 1 (markdown):
```markdown
yolo solutions analytics show=True

# Pass the source
yolo solutions analytics source="path/to/video.mp4"

# Generate the pie chart
yolo solutions analytics analytics_type="pie" show=True

# Generate the bar plots
yolo solutions analytics analytics_type="bar" show=True

# Generate the area plots
yolo solutions analytics analytics_type="area" show=True
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
out = cv2.VideoWriter(
    "analytics_output.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (1280, 720),  # this is fixed
)

# Initialize analytics object
analytics = solutions.Analytics(
    show=True,  # display the output
    analytics_type="line",  # pass the analytics type, could be "pie", "bar" or "area".
    model="yolo26n.pt",  # path to the YOLO26 model file
    # classes=[0, 2],  # display analytics for specific detection classes
)

# Process video
frame_count = 0
while cap.isOpened():
    success, im0 = cap.read()
    if success:
        frame_count += 1
        results = analytics(im0, frame_count)  # update analytics graph every frame

        # print(results)  # access the output

        out.write(results.plot_im)  # write the video file
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (sql):
```sql
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

out = cv2.VideoWriter(
    "ultralytics_analytics.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (1280, 720),  # this is fixed
)

analytics = solutions.Analytics(
    analytics_type="line",
    show=True,
)

frame_count = 0
while cap.isOpened():
    success, im0 = cap.read()
    if success:
        frame_count += 1
        results = analytics(im0, frame_count)  # update analytics graph every frame
        out.write(results.plot_im)  # write the video file
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```

Example 4 (sql):
```sql
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

out = cv2.VideoWriter(
    "ultralytics_analytics.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (1280, 720),  # this is fixed
)

analytics = solutions.Analytics(
    analytics_type="bar",
    show=True,
)

frame_count = 0
while cap.isOpened():
    success, im0 = cap.read()
    if success:
        frame_count += 1
        results = analytics(im0, frame_count)  # update analytics graph every frame
        out.write(results.plot_im)  # write the video file
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
```

---

## Comprehensive Tutorials for Ultralytics YOLO

**URL:** https://docs.ultralytics.com/guides/

**Contents:**
- Comprehensive Tutorials for Ultralytics YOLO
- Guides
- Contribute to Our Guides
- FAQ
  - How do I train a custom object detection model using Ultralytics YOLO?
  - What performance metrics should I use to evaluate my YOLO model?
  - Why should I use Ultralytics Platform for my computer vision projects?
  - What are the common issues faced during YOLO model training, and how can I resolve them?
  - How can I deploy my YOLO model for real-time object detection on edge devices?
- Comments

Welcome to Ultralytics' YOLO Guides. Our comprehensive tutorials cover various aspects of the YOLO object detection model, ranging from training and prediction to deployment. Built on PyTorch, YOLO stands out for its exceptional speed and accuracy in real-time object detection tasks.

Whether you're a beginner or an expert in deep learning, our tutorials offer valuable insights into the implementation and optimization of YOLO for your computer vision projects.

Watch: Ultralytics YOLO26 Guides Overview

Here's a compilation of in-depth guides to help you master different aspects of Ultralytics YOLO.

We welcome contributions from the community! If you've mastered a particular aspect of Ultralytics YOLO that's not yet covered in our guides, we encourage you to share your expertise. Writing a guide is a great way to give back to the community and help us make our documentation more comprehensive and user-friendly.

To get started, please read our Contributing Guide for guidelines on how to open a Pull Request (PR). We look forward to your contributions.

Training a custom object detection model with Ultralytics YOLO is straightforward. Start by preparing your dataset in the correct format and installing the Ultralytics package. Use the following code to initiate training:

For detailed dataset formatting and additional options, refer to our Tips for Model Training guide.

Evaluating your YOLO model performance is crucial to understanding its efficacy. Key metrics include Mean Average Precision (mAP), Intersection over Union (IoU), and F1 score. These metrics help assess the accuracy and precision of object detection tasks. You can learn more about these metrics and how to improve your model in our YOLO Performance Metrics guide.

Ultralytics Platform is a no-code platform that simplifies managing, training, and deploying YOLO models. It supports seamless integration, real-time tracking, and cloud training, making it ideal for both beginners and professionals. Discover more about its features and how it can streamline your workflow with our Ultralytics Platform quickstart guide.

Common issues during YOLO model training include data formatting errors, model architecture mismatches, and insufficient training data. To address these, ensure your dataset is correctly formatted, check for compatible model versions, and augment your training data. For a comprehensive list of solutions, refer to our YOLO Common Issues guide.

Deploying YOLO models on edge devices like NVIDIA Jetson and Raspberry Pi requires converting the model to a compatible format such as TensorRT or TFLite. Follow our step-by-step guides for NVIDIA Jetson and Raspberry Pi deployments to get started with real-time object detection on edge hardware. These guides will walk you through installation, configuration, and performance optimization.

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

## Distance Calculation using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/distance-calculation/

**Contents:**
- Distance Calculation using Ultralytics YOLO26
- What is Distance Calculation?
- Visuals
- Advantages of Distance Calculation
  - DistanceCalculation() Arguments
- Implementation Details
- Applications
- FAQ
  - How do I calculate distances between objects using Ultralytics YOLO26?
  - What are the advantages of using distance calculation with Ultralytics YOLO26?

Measuring the gap between two objects is known as distance calculation within a specified space. In the case of Ultralytics YOLO26, the bounding box centroid is employed to calculate the distance for bounding boxes highlighted by the user.

Watch: How to estimate distance between detected objects with Ultralytics YOLO in Pixels 🚀

Distance is an estimate and may not be fully accurate because it is calculated using 2D data, which lacks depth information.

Distance Calculation using Ultralytics YOLO

Here's a table with the DistanceCalculation arguments:

You can also make use of various track arguments in the DistanceCalculation solution.

Moreover, the following visualization arguments are available:

The DistanceCalculation class works by tracking objects across video frames and calculating the Euclidean distance between the centroids of selected bounding boxes. When you click on two objects, the solution:

The implementation uses the mouse_event_for_distance method to handle mouse interactions, allowing users to select objects and clear selections as needed. The process method handles the frame-by-frame processing, tracking objects, and calculating distances.

Distance calculation with YOLO26 has numerous practical applications:

To calculate distances between objects using Ultralytics YOLO26, you need to identify the bounding box centroids of the detected objects. This process involves initializing the DistanceCalculation class from Ultralytics' solutions module and using the model's tracking outputs to calculate the distances.

Using distance calculation with Ultralytics YOLO26 offers several advantages:

Yes, you can perform distance calculation in real-time video streams with Ultralytics YOLO26. The process involves capturing video frames using OpenCV, running YOLO26 object detection, and using the DistanceCalculation class to calculate distances between objects in successive frames. For a detailed implementation, see the video stream example.

To delete points drawn during distance calculation with Ultralytics YOLO26, you can use a right mouse click. This action will clear all the points you have drawn. For more details, refer to the note section under the distance calculation example.

The key arguments for initializing the DistanceCalculation class in Ultralytics YOLO26 include:

For an exhaustive list and default values, see the arguments of DistanceCalculation.

**Examples:**

Example 1 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("distance_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize distance calculation object
distancecalculator = solutions.DistanceCalculation(
    model="yolo26n.pt",  # path to the YOLO26 model file.
    show=True,  # display the output
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = distancecalculator(im0)

    print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

---

## Instance Segmentation and Tracking using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/instance-segmentation-and-tracking/

**Contents:**
- Instance Segmentation and Tracking using Ultralytics YOLO26 🚀
- What is Instance Segmentation?
- Samples
  - InstanceSegmentation Arguments
- Applications of Instance Segmentation
  - Waste Management and Recycling
  - Autonomous Vehicles
  - Medical Imaging
  - Construction Site Monitoring
- Note

Instance segmentation is a computer vision task that involves identifying and outlining individual objects in an image at the pixel level. Unlike semantic segmentation which only classifies pixels by category, instance segmentation uniquely labels and precisely delineates each object instance, making it crucial for applications requiring detailed spatial understanding like medical imaging, autonomous driving, and industrial automation.

Ultralytics YOLO26 provides powerful instance segmentation capabilities that enable precise object boundary detection while maintaining the speed and efficiency YOLO models are known for.

There are two types of instance segmentation tracking available in the Ultralytics package:

Instance Segmentation with Class Objects: Each class object is assigned a unique color for clear visual separation.

Instance Segmentation with Object Tracks: Every track is represented by a distinct color, facilitating easy identification and tracking across video frames.

Watch: Instance Segmentation with Object Tracking using Ultralytics YOLO26

Instance segmentation using Ultralytics YOLO

Here's a table with the InstanceSegmentation arguments:

You can also take advantage of track arguments within the InstanceSegmentation solution:

Moreover, the following visualization arguments are available:

Instance segmentation with YOLO26 has numerous real-world applications across various industries:

YOLO26 can be used in waste management facilities to identify and sort different types of materials. The model can segment plastic waste, cardboard, metal, and other recyclables with high precision, enabling automated sorting systems to process waste more efficiently. This is particularly valuable considering that only about 10% of the 7 billion tonnes of plastic waste generated globally gets recycled.

In self-driving cars, instance segmentation helps identify and track pedestrians, vehicles, traffic signs, and other road elements at the pixel level. This precise understanding of the environment is crucial for navigation and safety decisions. YOLO26's real-time performance makes it ideal for these time-sensitive applications.

Instance segmentation can identify and outline tumors, organs, or cellular structures in medical scans. YOLO26's ability to precisely delineate object boundaries makes it valuable for medical diagnostics and treatment planning.

At construction sites, instance segmentation can track heavy machinery, workers, and materials. This helps ensure safety by monitoring equipment positions and detecting when workers enter hazardous areas, while also optimizing workflow and resource allocation.

For any inquiries, feel free to post your questions in the Ultralytics Issue Section or the discussion section mentioned below.

To perform instance segmentation using Ultralytics YOLO26, initialize the YOLO model with a segmentation version of YOLO26 and process video frames through it. Here's a simplified code example:

Learn more about instance segmentation in the Ultralytics YOLO26 guide.

Instance segmentation identifies and outlines individual objects within an image, giving each object a unique label and mask. Object tracking extends this by assigning consistent IDs to objects across video frames, facilitating continuous tracking of the same objects over time. When combined, as in YOLO26's implementation, you get powerful capabilities for analyzing object movement and behavior in videos while maintaining precise boundary information.

Ultralytics YOLO26 offers real-time performance, superior accuracy, and ease of use compared to other models like Mask R-CNN or Faster R-CNN. YOLO26 processes images in a single pass (one-stage detection), making it significantly faster while maintaining high precision. It also provides seamless integration with Ultralytics Platform, allowing users to manage models, datasets, and training pipelines efficiently. For applications requiring both speed and accuracy, YOLO26 provides an optimal balance.

Yes, Ultralytics offers several datasets suitable for training YOLO26 models for instance segmentation, including COCO-Seg, COCO8-Seg (a smaller subset for quick testing), Package-Seg, and Crack-Seg. These datasets come with pixel-level annotations needed for instance segmentation tasks. For more specialized applications, you can also create custom datasets following the Ultralytics format. Complete dataset information and usage instructions can be found in the Ultralytics Datasets documentation.

**Examples:**

Example 1 (julia):
```julia
# Instance segmentation using Ultralytics YOLO26
yolo solutions isegment show=True

# Pass a source video
yolo solutions isegment source="path/to/video.mp4"

# Monitor the specific classes
yolo solutions isegment classes="[0, 5]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("isegment_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize instance segmentation object
isegment = solutions.InstanceSegmentation(
    show=True,  # display the output
    model="yolo26n-seg.pt",  # model="yolo26n-seg.pt" for object segmentation using YOLO26.
    # classes=[0, 2],  # segment specific classes, e.g., person and car with the pretrained model.
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = isegment(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("instance-segmentation.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init InstanceSegmentation
isegment = solutions.InstanceSegmentation(
    show=True,  # display the output
    model="yolo26n-seg.pt",  # model="yolo26n-seg.pt" for object segmentation using YOLO26.
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break
    results = isegment(im0)
    video_writer.write(results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
```

---

## Object Blurring using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/object-blurring/

**Contents:**
- Object Blurring using Ultralytics YOLO26 🚀
- What is Object Blurring?
- Advantages of Object Blurring
  - ObjectBlurrer Arguments
- Real-World Applications
  - Privacy Protection in Surveillance
  - Healthcare Data Anonymization
  - Document Redaction
  - Media and Content Creation
- FAQ

Object blurring with Ultralytics YOLO26 involves applying a blurring effect to specific detected objects in an image or video. This can be achieved using the YOLO26 model capabilities to identify and manipulate objects within a given scene.

Watch: Object Blurring using Ultralytics YOLO26

Object Blurring using Ultralytics YOLO

Here's a table with the ObjectBlurrer arguments:

The ObjectBlurrer solution also supports a range of track arguments:

Moreover, the following visualization arguments can be used:

Security cameras and surveillance systems can use YOLO26 to automatically blur faces, license plates, or other identifying information while still capturing important activity. This helps maintain security while respecting privacy rights in public spaces.

In medical imaging, patient information often appears in scans or photos. YOLO26 can detect and blur this information to comply with regulations like HIPAA when sharing medical data for research or educational purposes.

When sharing documents that contain sensitive information, YOLO26 can automatically detect and blur specific elements like signatures, account numbers, or personal details, streamlining the redaction process while maintaining document integrity.

Content creators can use YOLO26 to blur brand logos, copyrighted material, or inappropriate content in videos and images, helping avoid legal issues while preserving the overall content quality.

Object blurring with Ultralytics YOLO26 involves automatically detecting and applying a blurring effect to specific objects in images or videos. This technique enhances privacy by concealing sensitive information while retaining relevant visual data. YOLO26's real-time processing capabilities make it suitable for applications requiring immediate privacy protection and selective focus adjustments.

To implement real-time object blurring with YOLO26, follow the provided Python example. This involves using YOLO26 for object detection and OpenCV for applying the blur effect. Here's a simplified version:

Ultralytics YOLO26 offers several advantages for object blurring:

For more detailed applications, check the advantages of object blurring section.

Yes, Ultralytics YOLO26 can be configured to detect and blur faces in videos to protect privacy. By training or using a pretrained model to specifically recognize faces, the detection results can be processed with OpenCV to apply a blur effect. Refer to our guide on object detection with YOLO26 and modify the code to target face detection.

Ultralytics YOLO26 typically outperforms models like Faster R-CNN in terms of speed, making it more suitable for real-time applications. While both models offer accurate detection, YOLO26's architecture is optimized for rapid inference, which is critical for tasks like real-time object blurring. Learn more about the technical differences and performance metrics in our YOLO26 documentation.

**Examples:**

Example 1 (markdown):
```markdown
# Blur the objects
yolo solutions blur show=True

# Pass a source video
yolo solutions blur source="path/to/video.mp4"

# Blur the specific classes
yolo solutions blur classes="[0, 5]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_blurring_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize object blurrer
blurrer = solutions.ObjectBlurrer(
    show=True,  # display the output
    model="yolo26n.pt",  # model for object blurring, e.g., yolo26m.pt
    # line_width=2,  # width of bounding box.
    # classes=[0, 2],  # blur specific classes, e.g., person and car with the COCO pretrained model.
    # blur_ratio=0.5,  # adjust percentage of blur intensity, value in range 0.1 - 1.0
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = blurrer(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Video writer
video_writer = cv2.VideoWriter("object_blurring_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init ObjectBlurrer
blurrer = solutions.ObjectBlurrer(
    show=True,  # display the output
    model="yolo26n.pt",  # model="yolo26n-obb.pt" for object blurring using YOLO26 OBB model.
    blur_ratio=0.5,  # set blur percentage, e.g., 0.7 for 70% blur on detected objects
    # line_width=2,  # width of bounding box.
    # classes=[0, 2],  # count specific classes, e.g., person and car with the COCO pretrained model.
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break
    results = blurrer(im0)
    video_writer.write(results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
```

---

## Object Counting in Different Regions using Ultralytics YOLO 🚀

**URL:** https://docs.ultralytics.com/guides/region-counting/

**Contents:**
- Object Counting in Different Regions using Ultralytics YOLO 🚀
- What is Object Counting in Regions?
- Advantages of Object Counting in Regions
- Real World Applications
- Usage Examples
  - RegionCounter Arguments
- FAQ
  - What is object counting in specified regions using Ultralytics YOLO26?
  - How do I run the region based object counting script with Ultralytics YOLO26?
  - Why should I use Ultralytics YOLO26 for object counting in regions?

Object counting in regions with Ultralytics YOLO26 involves precisely determining the number of objects within specified areas using advanced computer vision. This approach is valuable for optimizing processes, enhancing security, and improving efficiency in various applications.

Watch: Object Counting in Different Regions using Ultralytics YOLO26 | Ultralytics Solutions 🚀

Region counting using Ultralytics YOLO

Ultralytics Example Code

The Ultralytics region counting module is available in our examples section. You can explore this example for code customization and modify it to suit your specific use case.

Here's a table with the RegionCounter arguments:

The RegionCounter solution enables the use of object tracking parameters:

Additionally, the following visualization settings are supported:

Object counting in specified regions with Ultralytics YOLO26 involves detecting and tallying the number of objects within defined areas using advanced computer vision. This precise method enhances efficiency and accuracy across various applications like manufacturing, surveillance, and traffic monitoring.

Follow these steps to run object counting in Ultralytics YOLO26:

Clone the Ultralytics repository and navigate to the directory:

Execute the region counting script:

For more options, visit the Usage Examples section.

Using Ultralytics YOLO26 for object counting in regions offers several advantages:

Explore deeper benefits in the Advantages section.

Object counting with Ultralytics YOLO26 can be applied to numerous real-world scenarios:

Explore more examples in the Real World Applications section and the TrackZone solution for additional zone-based monitoring capabilities.

**Examples:**

Example 1 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Pass region as list
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]

# Pass region as dictionary
region_points = {
    "region-01": [(50, 50), (250, 50), (250, 250), (50, 250)],
    "region-02": [(640, 640), (780, 640), (780, 720), (640, 720)],
}

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("region_counting.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize region counter object
regioncounter = solutions.RegionCounter(
    show=True,  # display the frame
    region=region_points,  # pass region points
    model="yolo26n.pt",  # model for counting in regions, e.g., yolo26s.pt
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = regioncounter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 2 (unknown):
```unknown
git clone https://github.com/ultralytics/ultralytics
cd ultralytics/examples/YOLOv8-Region-Counter
```

Example 3 (unknown):
```unknown
python yolov8_region_counter.py --source "path/to/video.mp4" --save-img
```

---

## Object Counting using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/object-counting/

**Contents:**
- Object Counting using Ultralytics YOLO26
- What is Object Counting?
- Advantages of Object Counting
- Real World Applications
  - ObjectCounter Arguments
- FAQ
  - How do I count objects in a video using Ultralytics YOLO26?
  - What are the advantages of using Ultralytics YOLO26 for object counting?
  - How can I count specific classes of objects using Ultralytics YOLO26?
  - Why should I use YOLO26 over other object detection models for real-time applications?

Object counting with Ultralytics YOLO26 involves accurate identification and counting of specific objects in videos and camera streams. YOLO26 excels in real-time applications, providing efficient and precise object counting for various scenarios like crowd analysis and surveillance, thanks to its state-of-the-art algorithms and deep learning capabilities.

Watch: How to Perform Real-Time Object Counting with Ultralytics YOLO26 🍏

Object Counting using Ultralytics YOLO

The region argument accepts either two points (for a line) or a polygon with three or more points. Define the coordinates in the order they should be connected so the counter knows exactly where entries and exits occur.

Here's a table with the ObjectCounter arguments:

The ObjectCounter solution allows the use of several track arguments:

Additionally, the visualization arguments listed below are supported:

To count objects in a video using Ultralytics YOLO26, you can follow these steps:

Here's a simple example for counting in a region:

For more advanced configurations and options, check out the RegionCounter solution for counting objects in multiple regions simultaneously.

Using Ultralytics YOLO26 for object counting offers several advantages:

For implementation examples and practical applications, explore the TrackZone solution for tracking objects in specific zones.

To count specific classes of objects using Ultralytics YOLO26, you need to specify the classes you are interested in during the tracking phase. Below is a Python example:

In this example, classes_to_count=[0, 2] means it counts objects of class 0 and 2 (e.g., person and car in the COCO dataset). You can find more information about class indices in the COCO dataset documentation.

Ultralytics YOLO26 provides several advantages over other object detection models like Faster R-CNN, SSD, and previous YOLO versions:

Check out Ultralytics YOLO26 Documentation for a deeper dive into its features and performance comparisons.

Yes, Ultralytics YOLO26 is perfectly suited for advanced applications like crowd analysis and traffic management due to its real-time detection capabilities, scalability, and integration flexibility. Its advanced features allow for high-accuracy object tracking, counting, and classification in dynamic environments. Example use cases include:

For more specialized applications, explore Ultralytics Solutions for a comprehensive set of tools designed for real-world computer vision challenges.

**Examples:**

Example 1 (markdown):
```markdown
# Run a counting example
yolo solutions count show=True

# Pass a source video
yolo solutions count source="path/to/video.mp4"

# Pass region coordinates
yolo solutions count region="[(20, 400), (1080, 400), (1080, 360), (20, 360)]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# region_points = [(20, 400), (1080, 400)]                                      # line counting
region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # rectangular region
# region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360), (20, 400)]   # polygon region

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize object counter object
counter = solutions.ObjectCounter(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",  # model="yolo26n-obb.pt" for object counting with OBB model.
    # classes=[0, 2],  # count specific classes, e.g., person and car with the COCO pretrained model.
    # tracker="botsort.yaml",  # choose trackers, e.g., "bytetrack.yaml"
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = counter(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions


def count_objects_in_region(video_path, output_video_path, model_path):
    """Count objects in a specific region within a video."""
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    region_points = [(20, 400), (1080, 400), (1080, 360), (20, 360)]
    counter = solutions.ObjectCounter(show=True, region=region_points, model=model_path)

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or processing is complete.")
            break
        results = counter(im0)
        video_writer.write(results.plot_im)

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()


count_objects_in_region("path/to/video.mp4", "output_video.avi", "yolo26n.pt")
```

Example 4 (python):
```python
import cv2

from ultralytics import solutions


def count_specific_classes(video_path, output_video_path, model_path, classes_to_count):
    """Count specific classes of objects in a video."""
    cap = cv2.VideoCapture(video_path)
    assert cap.isOpened(), "Error reading video file"
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    video_writer = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

    line_points = [(20, 400), (1080, 400)]
    counter = solutions.ObjectCounter(show=True, region=line_points, model=model_path, classes=classes_to_count)

    while cap.isOpened():
        success, im0 = cap.read()
        if not success:
            print("Video frame is empty or processing is complete.")
            break
        results = counter(im0)
        video_writer.write(results.plot_im)

    cap.release()
    video_writer.release()
    cv2.destroyAllWindows()


count_specific_classes("path/to/video.mp4", "output_specific_classes.avi", "yolo26n.pt", [0, 2])
```

---

## Object Cropping using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/object-cropping/

**Contents:**
- Object Cropping using Ultralytics YOLO26
- What is Object Cropping?
- Advantages of Object Cropping
- Visuals
  - ObjectCropper Arguments
- FAQ
  - What is object cropping in Ultralytics YOLO26 and how does it work?
  - Why should I use Ultralytics YOLO26 for object cropping over other solutions?
  - How can I reduce the data volume of my dataset using object cropping?
  - Can I use Ultralytics YOLO26 for real-time video analysis and object cropping?

Object cropping with Ultralytics YOLO26 involves isolating and extracting specific detected objects from an image or video. The YOLO26 model capabilities are utilized to accurately identify and delineate objects, enabling precise cropping for further analysis or manipulation.

Watch: Object Cropping using Ultralytics YOLO

Object Cropping using Ultralytics YOLO

When you provide the optional crop_dir argument, every cropped object is written to that folder with filenames that include the source image name and class. This makes it easy to inspect detections or build downstream datasets without writing extra code.

Here's a table with the ObjectCropper arguments:

Moreover, the following visualization arguments are available for use:

Object cropping using Ultralytics YOLO26 involves isolating and extracting specific objects from an image or video based on YOLO26's detection capabilities. This process allows for focused analysis, reduced data volume, and enhanced precision by leveraging YOLO26 to identify objects with high accuracy and crop them accordingly. For an in-depth tutorial, refer to the object cropping example.

Ultralytics YOLO26 stands out due to its precision, speed, and ease of use. It allows detailed and accurate object detection and cropping, essential for focused analysis and applications needing high data integrity. Moreover, YOLO26 integrates seamlessly with tools like OpenVINO and TensorRT for deployments requiring real-time capabilities and optimization on diverse hardware. Explore the benefits in the guide on model export.

By using Ultralytics YOLO26 to crop only relevant objects from your images or videos, you can significantly reduce the data size, making it more efficient for storage and processing. This process involves training the model to detect specific objects and then using the results to crop and save these portions only. For more information on exploiting Ultralytics YOLO26's capabilities, visit our quickstart guide.

Yes, Ultralytics YOLO26 can process real-time video feeds to detect and crop objects dynamically. The model's high-speed inference capabilities make it ideal for real-time applications such as surveillance, sports analysis, and automated inspection systems. Check out the tracking and prediction modes to understand how to implement real-time processing.

Ultralytics YOLO26 is optimized for both CPU and GPU environments, but to achieve optimal performance, especially for real-time or high-volume inference, a dedicated GPU (e.g., NVIDIA Tesla, RTX series) is recommended. For deployment on lightweight devices, consider using CoreML for iOS or TFLite for Android. More details on supported devices and formats can be found in our model deployment options.

**Examples:**

Example 1 (markdown):
```markdown
# Crop the objects
yolo solutions crop show=True

# Pass a source video
yolo solutions crop source="path/to/video.mp4"

# Crop specific classes
yolo solutions crop classes="[0, 2]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Initialize object cropper
cropper = solutions.ObjectCropper(
    show=True,  # display the output
    model="yolo26n.pt",  # model for object cropping, e.g., yolo26x.pt.
    classes=[0, 2],  # crop specific classes such as person and car with the COCO pretrained model.
    # conf=0.5,  # adjust confidence threshold for the objects.
    # crop_dir="cropped-detections",  # set the directory name for cropped detections
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = cropper(im0)

    # print(results)  # access the output

cap.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

---

## Queue Management using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/queue-management/

**Contents:**
- Queue Management using Ultralytics YOLO26 🚀
- What is Queue Management?
- Advantages of Queue Management
- Real World Applications
  - QueueManager Arguments
- Implementation Strategies
- FAQ
  - How can I use Ultralytics YOLO26 for real-time queue management?
  - What are the key advantages of using Ultralytics YOLO26 for queue management?
  - Why should I choose Ultralytics YOLO26 over competitors like TensorFlow or Detectron2 for queue management?

Queue management using Ultralytics YOLO26 involves organizing and controlling lines of people or vehicles to reduce wait times and enhance efficiency. It's about optimizing queues to improve customer satisfaction and system performance in various settings like retail, banks, airports, and healthcare facilities.

Watch: How to Build a Queue Management System with Ultralytics YOLO | Retail, Bank & Crowd Use Cases 🚀

Queue Management using Ultralytics YOLO

Here's a table with the QueueManager arguments:

The QueueManagement solution also support some track arguments:

Additionally, the following visualization parameters are available:

When implementing queue management with YOLO26, consider these best practices:

To use Ultralytics YOLO26 for real-time queue management, you can follow these steps:

Here's a minimal example:

Leveraging Ultralytics Platform can streamline this process by providing a user-friendly platform for deploying and managing your queue management solution.

Using Ultralytics YOLO26 for queue management offers several benefits:

For more details, explore our Queue Management solutions.

Ultralytics YOLO26 has several advantages over TensorFlow and Detectron2 for queue management:

Learn how to get started with Ultralytics YOLO.

Yes, Ultralytics YOLO26 can manage various types of queues, including those in airports and retail environments. By configuring the QueueManager with specific regions and settings, YOLO26 can adapt to different queue layouts and densities.

Example for airports:

For more information on diverse applications, check out our Real World Applications section.

Ultralytics YOLO26 is used in various real-world applications for queue management:

Check our blog on real-world queue management to learn more about how computer vision is transforming queue monitoring across industries.

**Examples:**

Example 1 (markdown):
```markdown
# Run a queue example
yolo solutions queue show=True

# Pass a source video
yolo solutions queue source="path/to/video.mp4"

# Pass queue coordinates
yolo solutions queue region="[(20, 400), (1080, 400), (1080, 360), (20, 360)]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("queue_management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Define queue points
queue_region = [(20, 400), (1080, 400), (1080, 360), (20, 360)]  # region points
# queue_region = [(20, 400), (1080, 400), (1080, 360), (20, 360), (20, 400)]    # polygon points

# Initialize queue manager object
queuemanager = solutions.QueueManager(
    show=True,  # display the output
    model="yolo26n.pt",  # path to the YOLO26 model file
    region=queue_region,  # pass queue region points
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break
    results = queuemanager(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
queue_region = [(20, 400), (1080, 400), (1080, 360), (20, 360)]

queuemanager = solutions.QueueManager(
    model="yolo26n.pt",
    region=queue_region,
    line_width=3,
    show=True,
)

while cap.isOpened():
    success, im0 = cap.read()
    if success:
        results = queuemanager(im0)

cap.release()
cv2.destroyAllWindows()
```

Example 4 (unknown):
```unknown
queue_region_airport = [(50, 600), (1200, 600), (1200, 550), (50, 550)]
queue_airport = solutions.QueueManager(
    model="yolo26n.pt",
    region=queue_region_airport,
    line_width=3,
)
```

---

## Speed Estimation using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/speed-estimation/

**Contents:**
- Speed Estimation using Ultralytics YOLO26 🚀
- What is Speed Estimation?
- Advantages of Speed Estimation
- Real World Applications
  - SpeedEstimator Arguments
- FAQ
  - How do I estimate object speed using Ultralytics YOLO26?
  - What are the benefits of using Ultralytics YOLO26 for speed estimation in traffic management?
  - Can YOLO26 be integrated with other AI frameworks like TensorFlow or PyTorch?
  - How accurate is the speed estimation using Ultralytics YOLO26?

Speed estimation is the process of calculating the rate of movement of an object within a given context, often employed in computer vision applications. Using Ultralytics YOLO26 you can now calculate the speed of objects using object tracking alongside distance and time data, crucial for tasks like traffic monitoring and surveillance. The accuracy of speed estimation directly influences the efficiency and reliability of various applications, making it a key component in the advancement of intelligent systems and real-time decision-making processes.

Watch: Speed Estimation using Ultralytics YOLO26

For deeper insights into speed estimation, check out our blog post: Ultralytics YOLO for Speed Estimation in Computer Vision Projects

Speed will be an estimate and may not be completely accurate. Additionally, the estimation can vary on camera specifications and related factors.

Speed Estimation using Ultralytics YOLO

Here's a table with the SpeedEstimator arguments:

The SpeedEstimator solution allows the use of track parameters:

Additionally, the following visualization options are supported:

Estimating object speed with Ultralytics YOLO26 involves combining object detection and tracking techniques. First, you need to detect objects in each frame using the YOLO26 model. Then, track these objects across frames to calculate their movement over time. Finally, use the distance traveled by the object between frames and the frame rate to estimate its speed.

For more details, refer to our official blog post.

Using Ultralytics YOLO26 for speed estimation offers significant advantages in traffic management:

For more applications, see advantages of speed estimation.

Yes, YOLO26 can be integrated with other AI frameworks like TensorFlow and PyTorch. Ultralytics provides support for exporting YOLO26 models to various formats like ONNX, TensorRT, and CoreML, ensuring smooth interoperability with other ML frameworks.

To export a YOLO26 model to ONNX format:

Learn more about exporting models in our guide on export.

The accuracy of speed estimation using Ultralytics YOLO26 depends on several factors, including the quality of the object tracking, the resolution and frame rate of the video, and environmental variables. While the speed estimator provides reliable estimates, it may not be 100% accurate due to variances in frame processing speed and object occlusion.

Note: Always consider margin of error and validate the estimates with ground truth data when possible.

For further accuracy improvement tips, check the Arguments SpeedEstimator section.

**Examples:**

Example 1 (markdown):
```markdown
# Run a speed example
yolo solutions speed show=True

# Pass a source video
yolo solutions speed source="path/to/video.mp4"

# Adjust meter per pixel value based on camera configuration
yolo solutions speed meter_per_pixel=0.05
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("speed_management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize speed estimation object
speedestimator = solutions.SpeedEstimator(
    show=True,  # display the output
    model="yolo26n.pt",  # path to the YOLO26 model file.
    fps=fps,  # adjust speed based on frame per second
    # max_speed=120,  # cap speed to a max value (km/h) to avoid outliers
    # max_hist=5,  # minimum frames object tracked before computing speed
    # meter_per_pixel=0.05,  # highly depends on the camera configuration
    # classes=[0, 2],  # estimate speed of specific classes.
    # line_width=2,  # adjust the line width for bounding boxes
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = speedestimator(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the processed frame.

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("speed_estimation.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize SpeedEstimator
speedestimator = solutions.SpeedEstimator(
    model="yolo26n.pt",
    show=True,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        break
    results = speedestimator(im0)
    video_writer.write(results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
```

Example 4 (unknown):
```unknown
yolo export model=yolo26n.pt format=onnx
```

---

## TrackZone using Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/guides/trackzone/

**Contents:**
- TrackZone using Ultralytics YOLO26
- What is TrackZone?
- Advantages of Object Tracking in Zones (TrackZone)
- Real World Applications
  - TrackZone Arguments
- FAQ
  - How do I track objects in a specific area or zone of a video frame using Ultralytics YOLO26?
  - How can I use TrackZone in Python with Ultralytics YOLO26?
  - How do I configure the zone points for video processing using Ultralytics TrackZone?
- Comments

TrackZone specializes in monitoring objects within designated areas of a frame instead of the whole frame. Built on Ultralytics YOLO26, it integrates object detection and tracking specifically within zones for videos and live camera feeds. YOLO26's advanced algorithms and deep learning technologies make it a perfect choice for real-time use cases, offering precise and efficient object tracking in applications like crowd monitoring and surveillance.

Watch: How to Track Objects in Region using Ultralytics YOLO26 | TrackZone 🚀

TrackZone using Ultralytics YOLO

TrackZone relies on the region list to know which part of the frame to monitor. Define the polygon to match the physical zone you care about (doors, gates, etc.), and keep show=True enabled while configuring so you can verify the overlay aligns with the video feed.

Here's a table with the TrackZone arguments:

The TrackZone solution includes support for track parameters:

Moreover, the following visualization options are available:

Tracking objects in a defined area or zone of a video frame is straightforward with Ultralytics YOLO26. Simply use the command provided below to initiate tracking. This approach ensures efficient analysis and accurate results, making it ideal for applications like surveillance, crowd management, or any scenario requiring zonal tracking.

With just a few lines of code, you can set up object tracking in specific zones, making it easy to integrate into your projects.

Configuring zone points for video processing with Ultralytics TrackZone is simple and customizable. You can directly define and adjust the zones through a Python script, allowing precise control over the areas you want to monitor.

**Examples:**

Example 1 (markdown):
```markdown
# Run a trackzone example
yolo solutions trackzone show=True

# Pass a source video
yolo solutions trackzone source="path/to/video.mp4" show=True

# Pass region coordinates
yolo solutions trackzone show=True region="[(150, 150), (1130, 150), (1130, 570), (150, 570)]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Define region points
region_points = [(150, 150), (1130, 150), (1130, 570), (150, 570)]

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("trackzone_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init trackzone (object tracking in zones, not complete frame)
trackzone = solutions.TrackZone(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",  # use any model that Ultralytics supports, e.g., YOLOv9, YOLOv10
    # line_width=2,  # adjust the line width for bounding boxes and text display
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or processing is complete.")
        break

    results = trackzone(im0)

    # print(results)  # access the output

    video_writer.write(results.plot_im)  # write the video file

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (unknown):
```unknown
yolo solutions trackzone source="path/to/video.mp4" show=True
```

Example 4 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Define region points
region_points = [(150, 150), (1130, 150), (1130, 570), (150, 570)]

# Video writer
video_writer = cv2.VideoWriter("object_counting_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init trackzone (object tracking in zones, not complete frame)
trackzone = solutions.TrackZone(
    show=True,  # display the output
    region=region_points,  # pass region points
    model="yolo26n.pt",
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break
    results = trackzone(im0)
    video_writer.write(results.plot_im)

cap.release()
video_writer.release()
cv2.destroyAllWindows()
```

---

## VisionEye View Object Mapping using Ultralytics YOLO26 🚀

**URL:** https://docs.ultralytics.com/guides/vision-eye/

**Contents:**
- VisionEye View Object Mapping using Ultralytics YOLO26 🚀
- What is VisionEye Object Mapping?
  - VisionEye Arguments
- How VisionEye Works
- Applications of VisionEye
- Note
- FAQ
  - How do I start using VisionEye Object Mapping with Ultralytics YOLO26?
  - Why should I use Ultralytics YOLO26 for object mapping and tracking?
  - How can I integrate VisionEye with other machine learning tools like Comet or ClearML?

Ultralytics YOLO26 VisionEye offers the capability for computers to identify and pinpoint objects, simulating the observational precision of the human eye. This functionality enables computers to discern and focus on specific objects, much like the way the human eye observes details from a particular viewpoint.

VisionEye Mapping using Ultralytics YOLO

The vision_point tuple represents the observer's position in pixel coordinates. Adjust it to match the camera perspective so the rendered rays correctly illustrate how objects relate to the chosen viewpoint.

Here's a table with the VisionEye arguments:

You can also utilize various track arguments within the VisionEye solution:

Furthermore, some visualization arguments are supported, as listed below:

VisionEye works by establishing a fixed vision point in the frame and drawing lines from this point to detected objects. This simulates how human vision focuses on multiple objects from a single viewpoint. The solution uses object tracking to maintain consistent identification of objects across frames, creating a visual representation of the spatial relationship between the observer (vision point) and the objects in the scene.

The process method in the VisionEye class performs several key operations:

This approach is particularly useful for applications requiring spatial awareness and object relationship visualization, such as surveillance systems, autonomous navigation, and interactive installations.

VisionEye object mapping has numerous practical applications across various industries:

By combining VisionEye with other Ultralytics solutions like distance calculation or speed estimation, you can build comprehensive systems that not only track objects but also understand their spatial relationships and behaviors.

For any inquiries, feel free to post your questions in the Ultralytics Issue Section or the discussion section mentioned below.

To start using VisionEye Object Mapping with Ultralytics YOLO26, first, you'll need to install the Ultralytics YOLO package via pip. Then, you can use the sample code provided in the documentation to set up object detection with VisionEye. Here's a simple example to get you started:

Ultralytics YOLO26 is renowned for its speed, accuracy, and ease of integration, making it a top choice for object mapping and tracking. Key advantages include:

For more information on applications and benefits, check out the Ultralytics YOLO26 documentation.

Ultralytics YOLO26 can integrate seamlessly with various machine learning tools like Comet and ClearML, enhancing experiment tracking, collaboration, and reproducibility. Follow the detailed guides on how to use YOLOv5 with Comet and integrate YOLO26 with ClearML to get started.

For further exploration and integration examples, check our Ultralytics Integrations Guide.

**Examples:**

Example 1 (markdown):
```markdown
# Monitor objects position with visioneye
yolo solutions visioneye show=True

# Pass a source video
yolo solutions visioneye source="path/to/video.mp4"

# Monitor the specific classes
yolo solutions visioneye classes="[0, 5]"
```

Example 2 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("visioneye_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Initialize vision eye object
visioneye = solutions.VisionEye(
    show=True,  # display the output
    model="yolo26n.pt",  # use any model that Ultralytics supports, e.g., YOLOv10
    classes=[0, 2],  # generate visioneye view for specific classes
    vision_point=(50, 50),  # the point where VisionEye will view objects and draw tracks
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = visioneye(im0)

    print(results)  # access the output

    video_writer.write(results.plot_im)  # write the video file

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

Example 3 (python):
```python
import cv2

from ultralytics import solutions

cap = cv2.VideoCapture("path/to/video.mp4")
assert cap.isOpened(), "Error reading video file"

# Video writer
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
video_writer = cv2.VideoWriter("vision-eye-mapping.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Init vision eye object
visioneye = solutions.VisionEye(
    show=True,  # display the output
    model="yolo26n.pt",  # use any model that Ultralytics supports, e.g., YOLOv10
    classes=[0, 2],  # generate visioneye view for specific classes
)

# Process video
while cap.isOpened():
    success, im0 = cap.read()

    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = visioneye(im0)

    print(results)  # access the output

    video_writer.write(results.plot_im)  # write the video file

cap.release()
video_writer.release()
cv2.destroyAllWindows()  # destroy all opened windows
```

---
