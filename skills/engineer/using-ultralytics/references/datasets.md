# Raw-Ultralytics - Datasets

**Pages:** 54

---

## African Wildlife Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/african-wildlife/

**Contents:**
- African Wildlife Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations, License and Acknowledgments
- FAQ
  - What is the African Wildlife Dataset, and how can it be used in computer vision projects?
  - How do I train a YOLO26 model using the African Wildlife Dataset?

This dataset showcases four common animal classes typically found in South African nature reserves. It includes images of African wildlife such as buffalo, elephant, rhino, and zebra, providing valuable insights into their characteristics. Essential for training computer vision algorithms, this dataset aids in identifying animals in various habitats, from zoos to forests, and supports wildlife research.

Watch: African Wildlife Animals Detection using Ultralytics YOLO26

The African wildlife objects detection dataset is split into three subsets:

This dataset can be applied in various computer vision tasks such as object detection, object tracking, and research. Specifically, it can be used to train and evaluate models for identifying African wildlife objects in images, which can have applications in wildlife conservation, ecological research, and monitoring efforts in natural reserves and protected areas. Additionally, it can serve as a valuable resource for educational purposes, enabling students and researchers to study and understand the characteristics and behaviors of different animal species.

A YAML (Yet Another Markup Language) file defines the dataset configuration, including paths, classes, and other pertinent details. For the African wildlife dataset, the african-wildlife.yaml file is located at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/african-wildlife.yaml.

ultralytics/cfg/datasets/african-wildlife.yaml

To train a YOLO26n model on the African wildlife dataset for 100 epochs with an image size of 640, use the provided code samples. For a comprehensive list of available parameters, refer to the model's Training page.

The African wildlife dataset comprises a wide variety of images showcasing diverse animal species and their natural habitats. Below are examples of images from the dataset, each accompanied by its corresponding annotations.

This example illustrates the variety and complexity of images in the African wildlife dataset, emphasizing the benefits of including mosaicing during the training process.

We'd like to thank the original dataset author, Bianca Ferreira, for releasing this dataset to the community. The Ultralytics team has updated and adapted it internally so it can be used seamlessly with Ultralytics YOLO models. This dataset is available under the AGPL-3.0 License.

If you use this dataset in your research, please cite it using the mentioned details:

The African Wildlife Dataset includes images of four common animal species found in South African nature reserves: buffalo, elephant, rhino, and zebra. It is a valuable resource for training computer vision algorithms in object detection and animal identification. The dataset supports various tasks like object tracking, research, and conservation efforts. For more information on its structure and applications, refer to the Dataset Structure section and Applications of the dataset.

You can train a YOLO26 model on the African Wildlife Dataset by using the african-wildlife.yaml configuration file. Below is an example of how to train the YOLO26n model for 100 epochs with an image size of 640:

For additional training parameters and options, refer to the Training documentation.

The YAML configuration file for the African Wildlife Dataset, named african-wildlife.yaml, can be found at this GitHub link. This file defines the dataset configuration, including paths, classes, and other details crucial for training machine learning models. See the Dataset YAML section for more details.

Yes, the African Wildlife Dataset includes a wide variety of images showcasing diverse animal species in their natural habitats. You can view sample images and their corresponding annotations in the Sample Images and Annotations section. This section also illustrates the use of mosaicing technique to combine multiple images into one for enriched batch diversity, enhancing the model's generalization ability.

The African Wildlife Dataset is ideal for supporting wildlife conservation and research by enabling the training and evaluation of models to identify African wildlife in different habitats. These models can assist in monitoring animal populations, studying their behavior, and recognizing conservation needs. Additionally, the dataset can be utilized for educational purposes, helping students and researchers understand the characteristics and behaviors of different animal species. More details can be found in the Applications section.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# African Wildlife dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/african-wildlife/
# Example usage: yolo train data=african-wildlife.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── african-wildlife ← downloads here (100 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: african-wildlife # dataset root dir
train: images/train # train images (relative to 'path') 1052 images
val: images/val # val images (relative to 'path') 225 images
test: images/test # test images (relative to 'path') 227 images

# Classes
names:
  0: buffalo
  1: elephant
  2: rhino
  3: zebra

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/african-wildlife.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="african-wildlife.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=african-wildlife.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load an African wildlife fine-tuned model

# Inference using the model
results = model.predict("https://ultralytics.com/assets/african-wildlife-sample.jpg")
```

---

## Argoverse Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/argoverse/

**Contents:**
- Argoverse Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Argoverse dataset and its key features?

The Argoverse dataset is a collection of data designed to support research in autonomous driving tasks, such as 3D tracking, motion forecasting, and stereo depth estimation. Developed by Argo AI, the dataset provides a wide range of high-quality sensor data, including high-resolution images, LiDAR point clouds, and map data.

The Argoverse dataset *.zip file required for training was removed from Amazon S3 after the shutdown of Argo AI by Ford, but we have made it available for manual download on Google Drive.

The Argoverse dataset is organized into three main subsets:

The Argoverse dataset is widely used for training and evaluating deep learning models in autonomous driving tasks such as 3D object tracking, motion forecasting, and stereo depth estimation. The dataset's diverse set of sensor data, object annotations, and map information make it a valuable resource for researchers and practitioners in the field of autonomous driving.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. For the case of the Argoverse dataset, the Argoverse.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/Argoverse.yaml.

ultralytics/cfg/datasets/Argoverse.yaml

To train a YOLO26n model on the Argoverse dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Argoverse dataset contains a diverse set of sensor data, including camera images, LiDAR point clouds, and HD map information, providing rich context for autonomous driving tasks. Here are some examples of data from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the data in the Argoverse dataset and highlights the importance of high-quality sensor data for autonomous driving tasks.

If you use the Argoverse dataset in your research or development work, please cite the following paper:

We would like to acknowledge Argo AI for creating and maintaining the Argoverse dataset as a valuable resource for the autonomous driving research community. For more information about the Argoverse dataset and its creators, visit the Argoverse dataset website.

The Argoverse dataset, developed by Argo AI, supports autonomous driving research. It includes over 290K labeled 3D object tracks and 5 million object instances across 1,263 distinct scenes. The dataset provides high-resolution camera images, LiDAR point clouds, and annotated HD maps, making it valuable for tasks like 3D tracking, motion forecasting, and stereo depth estimation.

To train a YOLO26 model with the Argoverse dataset, use the provided YAML configuration file and the following code:

For a detailed explanation of the arguments, refer to the model Training page.

The Argoverse dataset includes various sensor data types such as high-resolution camera images, LiDAR point clouds, and HD map data. Annotations include 3D bounding boxes, object tracks, and trajectory information. These comprehensive annotations are essential for accurate model training in tasks like 3D object tracking, motion forecasting, and stereo depth estimation.

The dataset is divided into three main subsets:

The Argoverse dataset *.zip file, previously available on Amazon S3, can now be manually downloaded from Google Drive.

A YAML file contains the dataset's paths, classes, and other essential information. For the Argoverse dataset, the configuration file, Argoverse.yaml, can be found at the following link: Argoverse.yaml.

For more information about YAML configurations, see our datasets guide.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Argoverse-HD dataset (ring-front-center camera) by Argo AI: https://www.cs.cmu.edu/~mengtial/proj/streaming/
# Documentation: https://docs.ultralytics.com/datasets/detect/argoverse/
# Example usage: yolo train data=Argoverse.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── Argoverse ← downloads here (31.5 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: Argoverse # dataset root dir
train: Argoverse-1.1/images/train/ # train images (relative to 'path') 39384 images
val: Argoverse-1.1/images/val/ # val images (relative to 'path') 15062 images
test: Argoverse-1.1/images/test/ # test images (optional) https://eval.ai/web/challenges/challenge-page/800/overview

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: bus
  5: truck
  6: traffic_light
  7: stop_sign

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  import json
  from pathlib import Path

  from ultralytics.utils import TQDM
  from ultralytics.utils.downloads import download

  def argoverse2yolo(annotation_file):
      """Convert Argoverse dataset annotations to YOLO format for object detection tasks."""
      labels = {}
      with open(annotation_file, encoding="utf-8") as f:
          a = json.load(f)
      for annot in TQDM(a["annotations"], desc=f"Converting {annotation_file} to YOLO format..."):
          img_id = annot["image_id"]
          img_name = a["images"][img_id]["name"]
          img_label_name = f"{Path(img_name).stem}.txt"

          cls = annot["category_id"]  # instance class id
          x_center, y_center, width, height = annot["bbox"]
          x_center = (x_center + width / 2) / 1920.0  # offset and scale
          y_center = (y_center + height / 2) / 1200.0  # offset and scale
          width /= 1920.0  # scale
          height /= 1200.0  # scale

          img_dir = annotation_file.parents[2] / "Argoverse-1.1" / "labels" / a["seq_dirs"][a["images"][annot["image_id"]]["sid"]]
          if not img_dir.exists():
              img_dir.mkdir(parents=True, exist_ok=True)

          k = str(img_dir / img_label_name)
          if k not in labels:
              labels[k] = []
          labels[k].append(f"{cls} {x_center} {y_center} {width} {height}\n")

      for k in labels:
          with open(k, "w", encoding="utf-8") as f:
              f.writelines(labels[k])


  # Download 'https://argoverse-hd.s3.us-east-2.amazonaws.com/Argoverse-HD-Full.zip' (deprecated S3 link)
  dir = Path(yaml["path"])  # dataset root dir
  urls = ["https://drive.google.com/file/d/1st9qW3BeIwQsnR0t8mRpvbsSWIo16ACi/view?usp=drive_link"]
  print("\n\nWARNING: Argoverse dataset MUST be downloaded manually, autodownload will NOT work.")
  print(f"WARNING: Manually download Argoverse dataset '{urls[0]}' to '{dir}' and re-run your command.\n\n")
  # download(urls, dir=dir)

  # Convert
  annotations_dir = "Argoverse-HD/annotations/"
  (dir / "Argoverse-1.1" / "tracking").rename(dir / "Argoverse-1.1" / "images")  # rename 'tracking' to 'images'
  for d in "train.json", "val.json":
      argoverse2yolo(dir / annotations_dir / d)  # convert Argoverse annotations to YOLO labels
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="Argoverse.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=Argoverse.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (css):
```css
@inproceedings{chang2019argoverse,
  title={Argoverse: 3D Tracking and Forecasting with Rich Maps},
  author={Chang, Ming-Fang and Lambert, John and Sangkloy, Patsorn and Singh, Jagjeet and Bak, Slawomir and Hartnett, Andrew and Wang, Dequan and Carr, Peter and Lucey, Simon and Ramanan, Deva and others},
  booktitle={Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition},
  pages={8748--8757},
  year={2019}
}
```

---

## Brain Tumor Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/brain-tumor/

**Contents:**
- Brain Tumor Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the structure of the brain tumor dataset available in Ultralytics documentation?
  - How can I train a YOLO26 model on the brain tumor dataset using Ultralytics?

A brain tumor detection dataset consists of medical images from MRI or CT scans, containing information about brain tumor presence, location, and characteristics. This dataset is essential for training computer vision algorithms to automate brain tumor identification, aiding in early diagnosis and treatment planning in healthcare applications.

Watch: Brain Tumor Detection using Ultralytics Platform

The brain tumor dataset is divided into two subsets:

The dataset contains two classes:

The application of brain tumor detection using computer vision enables early diagnosis, treatment planning, and monitoring of tumor progression. By analyzing medical imaging data like MRI or CT scans, computer vision systems assist in accurately identifying brain tumors, aiding in timely medical intervention and personalized treatment strategies.

Medical professionals can leverage this technology to:

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the brain tumor dataset, the brain-tumor.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/brain-tumor.yaml.

ultralytics/cfg/datasets/brain-tumor.yaml

To train a YOLO26 model on the brain tumor dataset for 100 epochs with an image size of 640, utilize the provided code snippets. For a detailed list of available arguments, consult the model's Training page.

The brain tumor dataset encompasses a wide array of medical images featuring brain scans with and without tumors. Presented below are examples of images from the dataset, accompanied by their respective annotations.

This example highlights the diversity and intricacy of images within the brain tumor dataset, underscoring the advantages of incorporating mosaicing during the training phase for medical image analysis.

The dataset has been made available under the AGPL-3.0 License.

If you use this dataset in your research or development work, please cite it appropriately:

The brain tumor dataset is divided into two subsets: the training set consists of 893 images with corresponding annotations, while the testing set comprises 223 images with paired annotations. This structured division aids in developing robust and accurate computer vision models for detecting brain tumors. For more information on the dataset structure, visit the Dataset Structure section.

You can train a YOLO26 model on the brain tumor dataset for 100 epochs with an image size of 640px using both Python and CLI methods. Below are the examples for both:

For a detailed list of available arguments, refer to the Training page.

Using the brain tumor dataset in AI projects enables early diagnosis and treatment planning for brain tumors. It helps in automating brain tumor identification through computer vision, facilitating accurate and timely medical interventions, and supporting personalized treatment strategies. This application holds significant potential in improving patient outcomes and medical efficiencies. For more insights on AI applications in healthcare, see Ultralytics' healthcare solutions.

Inference using a fine-tuned YOLO26 model can be performed with either Python or CLI approaches. Here are the examples:

The YAML configuration file for the brain tumor dataset can be found at brain-tumor.yaml. This file includes paths, classes, and additional relevant information necessary for training and evaluating models on this dataset.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Brain-tumor dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/brain-tumor/
# Example usage: yolo train data=brain-tumor.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── brain-tumor ← downloads here (4.21 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: brain-tumor # dataset root dir
train: images/train # train images (relative to 'path') 893 images
val: images/val # val images (relative to 'path') 223 images

# Classes
names:
  0: negative
  1: positive

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/brain-tumor.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="brain-tumor.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=brain-tumor.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load a brain-tumor fine-tuned model

# Inference using the model
results = model.predict("https://ultralytics.com/assets/brain-tumor-sample.jpg")
```

---

## Caltech-101 Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/caltech101/

**Contents:**
- Caltech-101 Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Caltech-101 dataset used for in machine learning?
  - How can I train an Ultralytics YOLO model on the Caltech-101 dataset?

The Caltech-101 dataset is a widely used dataset for object recognition tasks, containing around 9,000 images from 101 object categories. The categories were chosen to reflect a variety of real-world objects, and the images themselves were carefully selected and annotated to provide a challenging benchmark for object recognition algorithms.

Watch: How to Train Image Classification Model using Caltech-256 Dataset with Ultralytics Platform

Automatic Data Splitting

The Caltech-101 dataset, as provided, does not come with pre-defined train/validation splits. However, when you use the training commands provided in the usage examples below, the Ultralytics framework will automatically split the dataset for you. The default split used is 80% for the training set and 20% for the validation set.

Unlike many other datasets, the Caltech-101 dataset is not formally split into training and testing sets. Users typically create their own splits based on their specific needs. However, a common practice is to use a random subset of images for training (e.g., 30 images per category) and the remaining images for testing.

The Caltech-101 dataset is extensively used for training and evaluating deep learning models in object recognition tasks, such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning algorithms. Its wide variety of categories and high-quality images make it an excellent dataset for research and development in the field of machine learning and computer vision.

To train a YOLO model on the Caltech-101 dataset for 100 epochs, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Caltech-101 dataset contains high-quality color images of various objects, providing a well-structured dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the objects in the Caltech-101 dataset, emphasizing the significance of a diverse dataset for training robust object recognition models.

If you use the Caltech-101 dataset in your research or development work, please cite the following paper:

We would like to acknowledge Li Fei-Fei, Rob Fergus, and Pietro Perona for creating and maintaining the Caltech-101 dataset as a valuable resource for the machine learning and computer vision research community. For more information about the Caltech-101 dataset and its creators, visit the Caltech-101 dataset website.

The Caltech-101 dataset is widely used in machine learning for object recognition tasks. It contains around 9,000 images across 101 categories, providing a challenging benchmark for evaluating object recognition algorithms. Researchers leverage it to train and test models, especially Convolutional Neural Networks (CNNs) and Support Vector Machines (SVMs), in computer vision.

To train an Ultralytics YOLO model on the Caltech-101 dataset, you can use the provided code snippets. For example, to train for 100 epochs:

For more detailed arguments and options, refer to the model Training page.

The Caltech-101 dataset includes:

These features make it an excellent choice for training and evaluating object recognition models in machine learning and computer vision.

Citing the Caltech-101 dataset in your research acknowledges the creators' contributions and provides a reference for others who might use the dataset. The recommended citation is:

Citing helps in maintaining the integrity of academic work and assists peers in locating the original resource.

Yes, you can use Ultralytics Platform for training models on the Caltech-101 dataset. Ultralytics Platform provides an intuitive platform for managing datasets, training models, and deploying them without extensive coding. For a detailed guide, refer to the how to train your custom models with Ultralytics Platform blog post.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="caltech101", epochs=100, imgsz=416)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=caltech101 model=yolo26n-cls.pt epochs=100 imgsz=416
```

Example 3 (swift):
```swift
@article{fei2007learning,
  title={Learning generative visual models from few training examples: An incremental Bayesian approach tested on 101 object categories},
  author={Fei-Fei, Li and Fergus, Rob and Perona, Pietro},
  journal={Computer vision and Image understanding},
  volume={106},
  number={1},
  pages={59--70},
  year={2007},
  publisher={Elsevier}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="caltech101", epochs=100, imgsz=416)
```

---

## Caltech-256 Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/caltech256/

**Contents:**
- Caltech-256 Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Caltech-256 dataset and why is it important for machine learning?
  - How can I train a YOLO model on the Caltech-256 dataset using Python or CLI?

The Caltech-256 dataset is an extensive collection of images used for object classification tasks. It contains around 30,000 images divided into 257 categories (256 object categories and 1 background category). The images are carefully curated and annotated to provide a challenging and diverse benchmark for object recognition algorithms.

Watch: How to Train Image Classification Model using Caltech-256 Dataset with Ultralytics Platform

Automatic Data Splitting

The Caltech-256 dataset, as provided, does not come with pre-defined train/validation splits. However, when you use the training commands provided in the usage examples below, the Ultralytics framework will automatically split the dataset for you. The default split used is 80% for the training set and 20% for the validation set.

Like Caltech-101, the Caltech-256 dataset does not have a formal split between training and testing sets. Users typically create their own splits according to their specific needs. A common practice is to use a random subset of images for training and the remaining images for testing.

The Caltech-256 dataset is extensively used for training and evaluating deep learning models in object recognition tasks, such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning algorithms. Its diverse set of categories and high-quality images make it an invaluable dataset for research and development in the field of machine learning and computer vision.

To train a YOLO model on the Caltech-256 dataset for 100 epochs, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Caltech-256 dataset contains high-quality color images of various objects, providing a comprehensive dataset for object recognition tasks. Here are some examples of images from the dataset (credit):

The example showcases the diversity and complexity of the objects in the Caltech-256 dataset, emphasizing the importance of a varied dataset for training robust object recognition models.

If you use the Caltech-256 dataset in your research or development work, please cite the following paper:

We would like to acknowledge Gregory Griffin, Alex Holub, and Pietro Perona for creating and maintaining the Caltech-256 dataset as a valuable resource for the machine learning and computer vision research community. For more information about the Caltech-256 dataset and its creators, visit the Caltech-256 dataset website.

The Caltech-256 dataset is a large image dataset used primarily for object classification tasks in machine learning and computer vision. It consists of around 30,000 color images divided into 257 categories, covering a wide range of real-world objects. The dataset's diverse and high-quality images make it an excellent benchmark for evaluating object recognition algorithms, which is crucial for developing robust machine learning models.

To train a YOLO model on the Caltech-256 dataset for 100 epochs, you can use the following code snippets. Refer to the model Training page for additional options.

The Caltech-256 dataset is widely used for various object recognition tasks such as:

Its diversity and comprehensive annotations make it ideal for research and development in machine learning and computer vision.

The Caltech-256 dataset does not come with a predefined split for training and testing. Users typically create their own splits according to their specific needs. A common approach is to randomly select a subset of images for training and use the remaining images for testing. This flexibility allows users to tailor the dataset to their specific project requirements and experimental setups.

Ultralytics YOLO models offer several advantages for training on the Caltech-256 dataset:

For more details, explore our comprehensive training guide and learn about image classification with Ultralytics YOLO.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="caltech256", epochs=100, imgsz=416)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=caltech256 model=yolo26n-cls.pt epochs=100 imgsz=416
```

Example 3 (python):
```python
@article{griffin2007caltech,
         title={Caltech-256 object category dataset},
         author={Griffin, Gregory and Holub, Alex and Perona, Pietro},
         year={2007}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model

# Train the model
results = model.train(data="caltech256", epochs=100, imgsz=416)
```

---

## Carparts Segmentation Dataset

**URL:** https://docs.ultralytics.com/datasets/segment/carparts-seg/

**Contents:**
- Carparts Segmentation Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Carparts Segmentation Dataset?
  - How can I use the Carparts Segmentation Dataset with Ultralytics YOLO26?

The Carparts Segmentation Dataset, available on Roboflow Universe, is a curated collection of images and videos designed for computer vision applications, specifically focusing on segmentation tasks. Hosted on Roboflow Universe, this dataset provides a diverse set of visuals captured from multiple perspectives, offering valuable annotated examples for training and testing segmentation models.

Whether you're working on automotive research, developing AI solutions for vehicle maintenance, or exploring computer vision applications, the Carparts Segmentation Dataset serves as a valuable resource for enhancing the accuracy and efficiency of your projects using models like Ultralytics YOLO.

Watch: Carparts Instance Segmentation with Ultralytics YOLO26.

The data distribution within the Carparts Segmentation Dataset is organized as follows:

Carparts Segmentation finds applications in various domains including:

By accurately identifying and categorizing different vehicle components, carparts segmentation streamlines processes and contributes to increased efficiency and automation across these industries.

A YAML (Yet Another Markup Language) file defines the dataset configuration, including paths, class names, and other essential details. For the Carparts Segmentation dataset, the carparts-seg.yaml file is available at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/carparts-seg.yaml. You can learn more about the YAML format at yaml.org.

ultralytics/cfg/datasets/carparts-seg.yaml

To train an Ultralytics YOLO26 model on the Carparts Segmentation dataset for 100 epochs with an image size of 640, use the following code snippets. Refer to the model Training guide for a comprehensive list of available arguments and explore model training tips for best practices.

The Carparts Segmentation dataset includes a diverse array of images and videos captured from various perspectives. Below are examples showcasing the data and its corresponding annotations:

If you utilize the Carparts Segmentation dataset in your research or development efforts, please cite the original source:

We acknowledge the contribution of Gianmarco Russo and the Roboflow team in creating and maintaining this valuable dataset for the computer vision community. For more datasets, visit the Ultralytics Datasets collection.

The Carparts Segmentation Dataset is a specialized collection of images and videos for training computer vision models to perform segmentation on car parts. It includes diverse visuals with detailed annotations, suitable for automotive AI applications.

You can train an Ultralytics YOLO26 segmentation model using this dataset. Load a pretrained model (e.g., yolo26n-seg.pt) and initiate training using the provided Python or CLI examples, referencing the carparts-seg.yaml configuration file. Check the Training Guide for detailed instructions.

Train Example Snippet

Carparts Segmentation is useful in:

The dataset configuration file, carparts-seg.yaml, which contains details about the dataset paths and classes, is located in the Ultralytics GitHub repository: carparts-seg.yaml.

This dataset offers rich, annotated data crucial for developing accurate segmentation models for automotive applications. Its diversity helps improve model robustness and performance in real-world scenarios like automated vehicle inspection, enhancing safety systems, and supporting autonomous driving technology. Using high-quality, domain-specific datasets like this accelerates AI development.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Carparts-seg dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/segment/carparts-seg/
# Example usage: yolo train data=carparts-seg.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── carparts-seg ← downloads here (133 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: carparts-seg # dataset root dir
train: images/train # train images (relative to 'path') 3516 images
val: images/val # val images (relative to 'path') 276 images
test: images/test # test images (relative to 'path') 401 images

# Classes
names:
  0: back_bumper
  1: back_door
  2: back_glass
  3: back_left_door
  4: back_left_light
  5: back_light
  6: back_right_door
  7: back_right_light
  8: front_bumper
  9: front_door
  10: front_glass
  11: front_left_door
  12: front_left_light
  13: front_light
  14: front_right_door
  15: front_right_light
  16: hood
  17: left_mirror
  18: object
  19: right_mirror
  20: tailgate
  21: trunk
  22: wheel

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/carparts-seg.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained segmentation model like YOLO26n-seg
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model on the Carparts Segmentation dataset
results = model.train(data="carparts-seg.yaml", epochs=100, imgsz=640)

# After training, you can validate the model's performance on the validation set
results = model.val()

# Or perform prediction on new images or videos
results = model.predict("path/to/your/image.jpg")
```

Example 3 (julia):
```julia
# Start training from a pretrained *.pt model using the Command Line Interface
# Specify the dataset config file, model, number of epochs, and image size
yolo segment train data=carparts-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640

# Validate the trained model using the validation set
yolo segment val data=carparts-seg.yaml model=path/to/best.pt

# Predict using the trained model on a specific image source
yolo segment predict model=path/to/best.pt source=path/to/your/image.jpg
```

Example 4 (swift):
```swift
@misc{ car-seg-un1pm_dataset,
        title = { car-seg Dataset },
        type = { Open Source Dataset },
        author = { Gianmarco Russo },
        url = { https://universe.roboflow.com/gianmarco-russo-vt9xr/car-seg-un1pm },
        journal = { Roboflow Universe },
        publisher = { Roboflow },
        year = { 2023 },
        month = { nov },
        note = { visited on 2024-01-24 },
    }
```

---

## CIFAR-100 Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/cifar100/

**Contents:**
- CIFAR-100 Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the CIFAR-100 dataset and why is it significant?
  - How do I train a YOLO model on the CIFAR-100 dataset?

The CIFAR-100 (Canadian Institute For Advanced Research) dataset is a significant extension of the CIFAR-10 dataset, composed of 60,000 32x32 color images in 100 different classes. It was developed by researchers at the CIFAR institute, offering a more challenging dataset for more complex machine learning and computer vision tasks.

Watch: How to Train Ultralytics YOLO26 on CIFAR-100 | Step-by-Step Image Classification Tutorial 🚀

The CIFAR-100 dataset is split into two subsets:

The CIFAR-100 dataset is extensively used for training and evaluating deep learning models in image classification tasks, such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning algorithms. The diversity of the dataset in terms of classes and the presence of color images make it a more challenging and comprehensive dataset for research and development in the field of machine learning and computer vision.

To train a YOLO model on the CIFAR-100 dataset for 100 epochs with an image size of 32x32, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The CIFAR-100 dataset contains color images of various objects, providing a well-structured dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the objects in the CIFAR-100 dataset, highlighting the importance of a diverse dataset for training robust image classification models.

If you use the CIFAR-100 dataset in your research or development work, please cite the following paper:

We would like to acknowledge Alex Krizhevsky for creating and maintaining the CIFAR-100 dataset as a valuable resource for the machine learning and computer vision research community. For more information about the CIFAR-100 dataset and its creator, visit the CIFAR-100 dataset website.

The CIFAR-100 dataset is a large collection of 60,000 32x32 color images classified into 100 classes. Developed by the Canadian Institute For Advanced Research (CIFAR), it provides a challenging dataset ideal for complex machine learning and computer vision tasks. Its significance lies in the diversity of classes and the small size of the images, making it a valuable resource for training and testing deep learning models, like Convolutional Neural Networks (CNNs), using frameworks such as Ultralytics YOLO.

You can train a YOLO model on the CIFAR-100 dataset using either Python or CLI commands. Here's how:

For a comprehensive list of available arguments, please refer to the model Training page.

The CIFAR-100 dataset is extensively used in training and evaluating deep learning models for image classification. Its diverse set of 100 classes, grouped into 20 coarse categories, provides a challenging environment for testing algorithms such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning approaches. This dataset is a key resource in research and development within machine learning and computer vision fields, particularly for object recognition and classification tasks.

The CIFAR-100 dataset is split into two main subsets:

Each of the 100 classes contains 600 images, with 500 images for training and 100 for testing, making it uniquely suited for rigorous academic and industrial research.

The CIFAR-100 dataset includes a variety of color images of various objects, making it a structured dataset for image classification tasks. You can refer to the documentation page to see sample images and annotations. These examples highlight the dataset's diversity and complexity, important for training robust image classification models. For more datasets suitable for classification tasks, check out Ultralytics' classification datasets overview.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="cifar100", epochs=100, imgsz=32)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=cifar100 model=yolo26n-cls.pt epochs=100 imgsz=32
```

Example 3 (sql):
```sql
@TECHREPORT{Krizhevsky09learningmultiple,
            author={Alex Krizhevsky},
            title={Learning multiple layers of features from tiny images},
            institution={},
            year={2009}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="cifar100", epochs=100, imgsz=32)
```

---

## CIFAR-10 Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/cifar10/

**Contents:**
- CIFAR-10 Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - How can I train a YOLO model on the CIFAR-10 dataset?
  - What are the key features of the CIFAR-10 dataset?

The CIFAR-10 (Canadian Institute For Advanced Research) dataset is a collection of images used widely for machine learning and computer vision algorithms. It was developed by researchers at the CIFAR institute and consists of 60,000 32x32 color images in 10 different classes.

Watch: How to Train an Image Classification Model with CIFAR-10 Dataset using Ultralytics YOLO26

The CIFAR-10 dataset is split into two subsets:

The CIFAR-10 dataset is widely used for training and evaluating deep learning models in image classification tasks, such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning algorithms. The diversity of the dataset in terms of classes and the presence of color images make it a well-rounded dataset for research and development in the field of machine learning and computer vision.

To train a YOLO model on the CIFAR-10 dataset for 100 epochs with an image size of 32x32, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The CIFAR-10 dataset contains color images of various objects, providing a well-structured dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the objects in the CIFAR-10 dataset, highlighting the importance of a diverse dataset for training robust image classification models.

If you use the CIFAR-10 dataset in your research or development work, please cite the following paper:

We would like to acknowledge Alex Krizhevsky for creating and maintaining the CIFAR-10 dataset as a valuable resource for the machine learning and computer vision research community. For more information about the CIFAR-10 dataset and its creator, visit the CIFAR-10 dataset website.

To train a YOLO model on the CIFAR-10 dataset using Ultralytics, you can follow the examples provided for both Python and CLI. Here is a basic example to train your model for 100 epochs with an image size of 32x32 pixels:

For more details, refer to the model Training page.

The CIFAR-10 dataset consists of 60,000 color images divided into 10 classes. Each class contains 6,000 images, with 5,000 for training and 1,000 for testing. The images are 32x32 pixels in size and vary across the following categories:

This diverse dataset is essential for training image classification models in fields such as machine learning and computer vision. For more information, visit the CIFAR-10 sections on dataset structure and applications.

The CIFAR-10 dataset is an excellent benchmark for image classification due to its diversity and structure. It contains a balanced mix of 60,000 labeled images across 10 different categories, which helps in training robust and generalized models. It is widely used for evaluating deep learning models, including Convolutional Neural Networks (CNNs) and other machine learning algorithms. The dataset is relatively small, making it suitable for quick experimentation and algorithm development. Explore its numerous applications in the applications section.

The CIFAR-10 dataset is structured into two main subsets:

Each subset comprises images categorized into 10 classes, with their annotations readily available for model training and evaluation. For more detailed information, refer to the dataset structure section.

If you use the CIFAR-10 dataset in your research or development projects, make sure to cite the following paper:

Acknowledging the dataset's creators helps support continued research and development in the field. For more details, see the citations and acknowledgments section.

The CIFAR-10 dataset is often used for training image classification models, such as Convolutional Neural Networks (CNNs) and Support Vector Machines (SVMs). These models can be employed in various computer vision tasks including object detection, image recognition, and automated tagging. To see some practical examples, check the code snippets in the usage section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="cifar10", epochs=100, imgsz=32)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=cifar10 model=yolo26n-cls.pt epochs=100 imgsz=32
```

Example 3 (sql):
```sql
@TECHREPORT{Krizhevsky09learningmultiple,
            author={Alex Krizhevsky},
            title={Learning multiple layers of features from tiny images},
            institution={},
            year={2009}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="cifar10", epochs=100, imgsz=32)
```

---

## COCO128 Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/coco128/

**Contents:**
- COCO128 Dataset
- Introduction
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Ultralytics COCO128 dataset used for?
  - How do I train a YOLO26 model using the COCO128 dataset?
  - What are the benefits of using mosaic augmentation with COCO128?

Ultralytics COCO128 is a small, but versatile object detection dataset composed of the first 128 images of the COCO train 2017 set. This dataset is ideal for testing and debugging object detection models, or for experimenting with new detection approaches. With 128 images, it is small enough to be easily manageable, yet diverse enough to test training pipelines for errors and act as a sanity check before training larger datasets.

Watch: Ultralytics COCO Dataset Overview

This dataset is intended for use with Ultralytics Platform and YOLO26.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO128 dataset, the coco128.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco128.yaml.

ultralytics/cfg/datasets/coco128.yaml

To train a YOLO26n model on the COCO128 dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the COCO128 dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the COCO128 dataset and the benefits of using mosaicing during the training process.

If you use the COCO dataset in your research or development work, please cite the following paper:

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the COCO dataset website.

The Ultralytics COCO128 dataset is a compact subset containing the first 128 images from the COCO train 2017 dataset. It's primarily used for testing and debugging object detection models, experimenting with new detection approaches, and validating training pipelines before scaling to larger datasets. Its manageable size makes it perfect for quick iterations while still providing enough diversity to be a meaningful test case.

To train a YOLO26 model on the COCO128 dataset, you can use either Python or CLI commands. Here's how:

For more training options and parameters, refer to the Training documentation.

Mosaic augmentation, as shown in the sample images, combines multiple training images into a single composite image. This technique offers several benefits when training with COCO128:

This technique is particularly valuable for smaller datasets like COCO128, helping models learn more robust features from limited data.

COCO128 (128 images) sits between COCO8 (8 images) and the full COCO dataset (118K+ images) in terms of size:

COCO128 provides a good middle ground, offering more diversity than COCO8 while remaining much more manageable than the full COCO dataset for experimentation and initial model development.

While COCO128 is primarily designed for object detection, the dataset's annotations can be adapted for other computer vision tasks:

For specialized tasks like segmentation, consider using purpose-built variants like COCO8-seg which include the appropriate annotations.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO128 dataset https://www.kaggle.com/datasets/ultralytics/coco128 (first 128 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/coco/
# Example usage: yolo train data=coco128.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco128 ← downloads here (7 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco128 # dataset root dir
train: images/train2017 # train images (relative to 'path') 128 images
val: images/train2017 # val images (relative to 'path') 128 images
test: # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco128.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco128.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=coco128.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO128-Seg Dataset

**URL:** https://docs.ultralytics.com/datasets/segment/coco128-seg/

**Contents:**
- COCO128-Seg Dataset
- Introduction
- Dataset Structure
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the COCO128-Seg dataset, and how is it used in Ultralytics YOLO26?
  - How can I train a YOLO26n-seg model using the COCO128-Seg dataset?

Ultralytics COCO128-Seg is a small but versatile instance segmentation dataset composed of the first 128 images of the COCO train 2017 set. This dataset is ideal for testing and debugging segmentation models, or for experimenting with new detection approaches. With 128 images, it is small enough to be easily manageable, yet diverse enough to test training pipelines for errors and act as a sanity check before training larger datasets.

This dataset is intended for use with Ultralytics Platform and YOLO26.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO128-Seg dataset, the coco128-seg.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco128-seg.yaml.

ultralytics/cfg/datasets/coco128-seg.yaml

To train a YOLO26n-seg model on the COCO128-Seg dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the COCO128-Seg dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the COCO128-Seg dataset and the benefits of using mosaicing during the training process.

If you use the COCO dataset in your research or development work, please cite the following paper:

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the COCO dataset website.

The COCO128-Seg dataset is a compact instance segmentation dataset by Ultralytics, consisting of the first 128 images from the COCO train 2017 set. This dataset is tailored for testing and debugging segmentation models or experimenting with new detection methods. It is particularly useful with Ultralytics YOLO26 and Platform for rapid iteration and pipeline error-checking before scaling to larger datasets. For detailed usage, refer to the model Training page.

To train a YOLO26n-seg model on the COCO128-Seg dataset for 100 epochs with an image size of 640, you can use Python or CLI commands. Here's a quick example:

For a thorough explanation of available arguments and configuration options, you can check the Training documentation.

The COCO128-Seg dataset offers a balanced combination of manageability and diversity with 128 images, making it perfect for quickly testing and debugging segmentation models or experimenting with new detection techniques. Its moderate size allows for fast training iterations while providing enough diversity to validate training pipelines before scaling to larger datasets. Learn more about supported dataset formats in the Ultralytics segmentation dataset guide.

The YAML configuration file for the COCO128-Seg dataset is available in the Ultralytics repository. You can access the file directly at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco128-seg.yaml. The YAML file includes essential information about dataset paths, classes, and configuration settings required for model training and validation.

Using mosaicing during training helps increase the diversity and variety of objects and scenes in each training batch. This technique combines multiple images into a single composite image, enhancing the model's ability to generalize to different object sizes, aspect ratios, and contexts within the scene. Mosaicing is beneficial for improving a model's robustness and accuracy, especially when working with moderately-sized datasets like COCO128-Seg. For an example of mosaiced images, see the Sample Images and Annotations section.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO128-seg dataset https://www.kaggle.com/datasets/ultralytics/coco128 (first 128 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/segment/coco/
# Example usage: yolo train data=coco128-seg.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco128-seg ← downloads here (7 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco128-seg # dataset root dir
train: images/train2017 # train images (relative to 'path') 128 images
val: images/train2017 # val images (relative to 'path') 128 images
test: # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco128-seg.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco128-seg.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo segment train data=coco128-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO8 Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/coco8/

**Contents:**
- COCO8 Dataset
- Introduction
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What Is the Ultralytics COCO8 Dataset Used For?
  - How Do I Train a YOLO26 Model Using the COCO8 Dataset?
  - Why Should I Use Ultralytics Platform for Managing My COCO8 Training?

The Ultralytics COCO8 dataset is a compact yet powerful object detection dataset, consisting of the first 8 images from the COCO train 2017 set—4 for training and 4 for validation. This dataset is specifically designed for rapid testing, debugging, and experimentation with YOLO models and training pipelines. Its small size makes it highly manageable, while its diversity ensures it serves as an effective sanity check before scaling up to larger datasets.

Watch: Ultralytics COCO Dataset Overview

COCO8 is fully compatible with Ultralytics Platform and YOLO26, enabling seamless integration into your computer vision workflows.

The COCO8 dataset configuration is defined in a YAML (Yet Another Markup Language) file, which specifies dataset paths, class names, and other essential metadata. You can review the official coco8.yaml file in the Ultralytics GitHub repository.

ultralytics/cfg/datasets/coco8.yaml

To train a YOLO26n model on the COCO8 dataset for 100 epochs with an image size of 640, use the following examples. For a full list of training options, see the YOLO Training documentation.

Below is an example of a mosaiced training batch from the COCO8 dataset:

This technique is especially useful for small datasets like COCO8, as it maximizes the value of each image during training.

If you use the COCO dataset in your research or development, please cite the following paper:

Special thanks to the COCO Consortium for their ongoing contributions to the computer vision community.

The Ultralytics COCO8 dataset is designed for rapid testing and debugging of object detection models. With only 8 images (4 for training, 4 for validation), it is ideal for verifying your YOLO training pipelines and ensuring everything works as expected before scaling to larger datasets. Explore the COCO8 YAML configuration for more details.

You can train a YOLO26 model on COCO8 using either Python or the CLI:

For additional training options, refer to the YOLO Training documentation.

Ultralytics Platform streamlines dataset management, training, and deployment for YOLO models—including COCO8. With features like cloud training, real-time monitoring, and intuitive dataset handling, HUB enables you to launch experiments with a single click and eliminates manual setup hassles. Learn more about Ultralytics Platform and how it can accelerate your computer vision projects.

Mosaic augmentation, as used in COCO8 training, combines multiple images into one during each batch. This increases the diversity of objects and backgrounds, helping your YOLO model generalize better to new scenarios. Mosaic augmentation is especially valuable for small datasets, as it maximizes the information available in each training step. For more on this, see the training guide.

To validate your YOLO26 model after training on COCO8, use the model's validation commands in either Python or CLI. This evaluates your model's performance using standard metrics. For step-by-step instructions, visit the YOLO Validation documentation.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8 dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/coco8/
# Example usage: yolo train data=coco8.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8 ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8 # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on COCO8
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 3 (julia):
```julia
# Train YOLO26n on COCO8 using the command line
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO8-Grayscale Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/coco8-grayscale/

**Contents:**
- COCO8-Grayscale Dataset
- Introduction
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What Is the Ultralytics COCO8-Grayscale Dataset Used For?
  - How Do I Train a YOLO26 Model Using the COCO8-Grayscale Dataset?
  - Why Should I Use Ultralytics Platform for Managing My COCO8-Grayscale Training?

The Ultralytics COCO8-Grayscale dataset is a compact yet powerful object detection dataset, consisting of the first 8 images from the COCO train 2017 set and converted to grayscale format—4 for training and 4 for validation. This dataset is specifically designed for rapid testing, debugging, and experimentation with YOLO grayscale models and training pipelines. Its small size makes it highly manageable, while its diversity ensures it serves as an effective sanity check before scaling up to larger datasets.

Watch: How to Train Ultralytics YOLO26 on Grayscale Datasets 🚀

COCO8-Grayscale is fully compatible with Ultralytics Platform and YOLO26, enabling seamless integration into your computer vision workflows.

The COCO8-Grayscale dataset configuration is defined in a YAML (Yet Another Markup Language) file, which specifies dataset paths, class names, and other essential metadata. You can review the official coco8-grayscale.yaml file in the Ultralytics GitHub repository.

To train your RGB images in grayscale, you could simply add channels: 1 to your dataset YAML file. This converts all images to grayscale during training, enabling you to utilize grayscale benefits without requiring a separate dataset.

ultralytics/cfg/datasets/coco8-grayscale.yaml

To train a YOLO26n model on the COCO8-Grayscale dataset for 100 epochs with an image size of 640, use the following examples. For a full list of training options, see the YOLO Training documentation.

Below is an example of a mosaiced training batch from the COCO8-Grayscale dataset:

This technique is especially useful for small datasets like COCO8-Grayscale, as it maximizes the value of each image during training.

If you use the COCO dataset in your research or development, please cite the following paper:

Special thanks to the COCO Consortium for their ongoing contributions to the computer vision community.

The Ultralytics COCO8-Grayscale dataset is designed for rapid testing and debugging of object detection models. With only 8 images (4 for training, 4 for validation), it is ideal for verifying your YOLO training pipelines and ensuring everything works as expected before scaling to larger datasets. Explore the COCO8-Grayscale YAML configuration for more details.

You can train a YOLO26 model on COCO8-Grayscale using either Python or the CLI:

For additional training options, refer to the YOLO Training documentation.

Ultralytics Platform streamlines dataset management, training, and deployment for YOLO models—including COCO8-Grayscale. With features like cloud training, real-time monitoring, and intuitive dataset handling, HUB enables you to launch experiments with a single click and eliminates manual setup hassles. Learn more about Ultralytics Platform and how it can accelerate your computer vision projects.

Mosaic augmentation, as used in COCO8-Grayscale training, combines multiple images into one during each batch. This increases the diversity of objects and backgrounds, helping your YOLO model generalize better to new scenarios. Mosaic augmentation is especially valuable for small datasets, as it maximizes the information available in each training step. For more on this, see the training guide.

To validate your YOLO26 model after training on COCO8-Grayscale, use the model's validation commands in either Python or CLI. This evaluates your model's performance using standard metrics. For step-by-step instructions, visit the YOLO Validation documentation.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8-Grayscale dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/coco8-grayscale/
# Example usage: yolo train data=coco8-grayscale.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8-grayscale ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8-grayscale # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

channels: 1

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8-grayscale.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on COCO8-Grayscale
results = model.train(data="coco8-grayscale.yaml", epochs=100, imgsz=640)
```

Example 3 (julia):
```julia
# Train YOLO26n on COCO8-Grayscale using the command line
yolo detect train data=coco8-grayscale.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO8-Multispectral Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/coco8-multispectral/

**Contents:**
- COCO8-Multispectral Dataset
- Introduction
- Dataset Generation
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What Is the Ultralytics COCO8-Multispectral Dataset Used For?
  - How Does Multispectral Data Improve Object Detection?

The Ultralytics COCO8-Multispectral dataset is an advanced variant of the original COCO8 dataset, designed to facilitate experimentation with multispectral object detection models. It consists of the same 8 images from the COCO train 2017 set—4 for training and 4 for validation—but with each image transformed into a 10-channel multispectral format. By expanding beyond standard RGB channels, COCO8-Multispectral enables the development and evaluation of models that can leverage richer spectral information.

COCO8-Multispectral is fully compatible with Ultralytics Platform and YOLO26, ensuring seamless integration into your computer vision workflows.

Watch: How to Train Ultralytics YOLO26 on Multispectral Datasets | Multi-Channel VisionAI 🚀

The multispectral images in COCO8-Multispectral were created by interpolating the original RGB images across 10 evenly spaced spectral channels within the visible spectrum. The process includes:

This approach simulates a multispectral imaging process, providing a more diverse set of data for model training and evaluation. For further reading on multispectral imaging, see the Multispectral Imaging Wikipedia article.

The COCO8-Multispectral dataset is configured using a YAML file, which defines dataset paths, class names, and essential metadata. You can review the official coco8-multispectral.yaml file in the Ultralytics GitHub repository.

ultralytics/cfg/datasets/coco8-multispectral.yaml

Prepare your TIFF images in (channel, height, width) order, saved with .tiff or .tif extension, and ensure they are uint8 for use with Ultralytics:

To train a YOLO26n model on the COCO8-Multispectral dataset for 100 epochs with an image size of 640, use the following examples. For a comprehensive list of training options, refer to the YOLO Training documentation.

For more details on model selection and best practices, explore the Ultralytics YOLO model documentation and the YOLO Model Training Tips guide.

Below is an example of a mosaiced training batch from the COCO8-Multispectral dataset:

This technique is especially valuable for small datasets like COCO8-Multispectral, as it maximizes the utility of each image during training.

If you use the COCO dataset in your research or development, please cite the following paper:

Special thanks to the COCO Consortium for their ongoing contributions to the computer vision community.

The Ultralytics COCO8-Multispectral dataset is designed for rapid testing and debugging of multispectral object detection models. With only 8 images (4 for training, 4 for validation), it is ideal for verifying your YOLO26 training pipelines and ensuring everything works as expected before scaling to larger datasets. For more datasets to experiment with, visit the Ultralytics Datasets Catalog.

Multispectral data provides additional spectral information beyond standard RGB, enabling models to distinguish objects based on subtle differences in reflectance across wavelengths. This can enhance detection accuracy, especially in challenging scenarios. Learn more about multispectral imaging and its applications in advanced computer vision.

Yes, COCO8-Multispectral is fully compatible with Ultralytics Platform and all YOLO models, including the latest YOLO26. This allows you to easily integrate the dataset into your training and validation workflows.

For a deeper understanding of data augmentation methods such as mosaic and their impact on model performance, refer to the YOLO Data Augmentation Guide and the Ultralytics Blog on Data Augmentation.

Absolutely! The small size and multispectral nature of COCO8-Multispectral make it ideal for benchmarking, educational demonstrations, and prototyping new model architectures. For more benchmarking datasets, see the Ultralytics Benchmark Dataset Collection.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8-Multispectral dataset (COCO8 images interpolated across 10 channels in the visual spectrum) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/coco8-multispectral/
# Example usage: yolo train data=coco8-multispectral.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8-multispectral ← downloads here (20.2 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8-multispectral # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Number of multispectral image channels
channels: 10

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8-multispectral.zip
```

Example 2 (swift):
```swift
import cv2
import numpy as np

# Create and write 10-channel TIFF
image = np.ones((10, 640, 640), dtype=np.uint8)  # CHW-order
cv2.imwritemulti("example.tiff", image)

# Read TIFF
success, frames_list = cv2.imreadmulti("example.tiff")
image = np.stack(frames_list, axis=2)
print(image.shape)  # (640, 640, 10)  HWC-order for training and inference
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on COCO8-Multispectral
results = model.train(data="coco8-multispectral.yaml", epochs=100, imgsz=640)
```

Example 4 (julia):
```julia
# Train YOLO26n on COCO8-Multispectral using the command line
yolo detect train data=coco8-multispectral.yaml model=yolo26n.pt epochs=100 imgsz=640
```

---

## COCO8-Pose Dataset

**URL:** https://docs.ultralytics.com/datasets/pose/coco8-pose/

**Contents:**
- COCO8-Pose Dataset
- Introduction
- Dataset Structure
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the COCO8-Pose dataset, and how is it used with Ultralytics YOLO26?
  - How do I train a YOLO26 model using the COCO8-Pose dataset in Ultralytics?

Ultralytics COCO8-Pose is a small but versatile pose detection dataset composed of the first 8 images of the COCO train 2017 set, 4 for training and 4 for validation. This dataset is ideal for testing and debugging object detection models, or for experimenting with new detection approaches. With 8 images, it is small enough to be easily manageable, yet diverse enough to test training pipelines for errors and act as a sanity check before training larger datasets.

This dataset is intended for use with Ultralytics Platform and YOLO26.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO8-Pose dataset, the coco8-pose.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8-pose.yaml.

ultralytics/cfg/datasets/coco8-pose.yaml

To train a YOLO26n-pose model on the COCO8-Pose dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the COCO8-Pose dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the COCO8-Pose dataset and the benefits of using mosaicing during the training process.

If you use the COCO dataset in your research or development work, please cite the following paper:

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the COCO dataset website.

The COCO8-Pose dataset is a small, versatile pose detection dataset that includes the first 8 images from the COCO train 2017 set, with 4 images for training and 4 for validation. It's designed for testing and debugging object detection models and experimenting with new detection approaches. This dataset is ideal for quick experiments with Ultralytics YOLO26. For more details on dataset configuration, check out the dataset YAML file.

To train a YOLO26n-pose model on the COCO8-Pose dataset for 100 epochs with an image size of 640, follow these examples:

For a comprehensive list of training arguments, refer to the model Training page.

The COCO8-Pose dataset offers several benefits:

For more about its features and usage, see the Dataset Introduction section.

Mosaicing, demonstrated in the sample images of the COCO8-Pose dataset, combines multiple images into one, increasing the variety of objects and scenes within each training batch. This technique helps improve the model's ability to generalize across various object sizes, aspect ratios, and contexts, ultimately enhancing model performance. See the Sample Images and Annotations section for example images.

The COCO8-Pose dataset YAML file can be found at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8-pose.yaml. This file defines the dataset configuration, including paths, classes, and other relevant information. Use this file with the YOLO26 training scripts as mentioned in the Train Example section.

For more FAQs and detailed documentation, visit the Ultralytics Documentation.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8-pose dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/pose/coco8-pose/
# Example usage: yolo train data=coco8-pose.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8-pose ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8-pose # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Keypoints
kpt_shape: [17, 3] # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
flip_idx: [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

# Classes
names:
  0: person

# Keypoint names per class
kpt_names:
  0:
    - nose
    - left_eye
    - right_eye
    - left_ear
    - right_ear
    - left_shoulder
    - right_shoulder
    - left_elbow
    - right_elbow
    - left_wrist
    - right_wrist
    - left_hip
    - right_hip
    - left_knee
    - right_knee
    - left_ankle
    - right_ankle

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8-pose.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco8-pose.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo pose train data=coco8-pose.yaml model=yolo26n-pose.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO8-Seg Dataset

**URL:** https://docs.ultralytics.com/datasets/segment/coco8-seg/

**Contents:**
- COCO8-Seg Dataset
- Introduction
- Dataset Structure
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the COCO8-Seg dataset, and how is it used in Ultralytics YOLO26?
  - How can I train a YOLO26n-seg model using the COCO8-Seg dataset?

Ultralytics COCO8-Seg is a small but versatile instance segmentation dataset composed of the first 8 images of the COCO train 2017 set, 4 for training and 4 for validation. This dataset is ideal for testing and debugging segmentation models, or for experimenting with new detection approaches. With 8 images, it is small enough to be easily manageable, yet diverse enough to test training pipelines for errors and act as a sanity check before training larger datasets.

This dataset is intended for use with Ultralytics Platform and YOLO26.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO8-Seg dataset, the coco8-seg.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8-seg.yaml.

ultralytics/cfg/datasets/coco8-seg.yaml

To train a YOLO26n-seg model on the COCO8-Seg dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the COCO8-Seg dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the COCO8-Seg dataset and the benefits of using mosaicing during the training process.

If you use the COCO dataset in your research or development work, please cite the following paper:

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the COCO dataset website.

The COCO8-Seg dataset is a compact instance segmentation dataset by Ultralytics, consisting of the first 8 images from the COCO train 2017 set—4 images for training and 4 for validation. This dataset is tailored for testing and debugging segmentation models or experimenting with new detection methods. It is particularly useful with Ultralytics YOLO26 and Platform for rapid iteration and pipeline error-checking before scaling to larger datasets. For detailed usage, refer to the model Training page.

To train a YOLO26n-seg model on the COCO8-Seg dataset for 100 epochs with an image size of 640, you can use Python or CLI commands. Here's a quick example:

For a thorough explanation of available arguments and configuration options, you can check the Training documentation.

The COCO8-Seg dataset offers a compact yet diverse set of 8 images, making it perfect for quickly testing and debugging segmentation models or experimenting with new detection techniques. Its small size allows for fast sanity checks and early pipeline validation, helping identify issues before scaling to larger datasets. Learn more about supported dataset formats in the Ultralytics segmentation dataset guide.

The YAML configuration file for the COCO8-Seg dataset is available in the Ultralytics repository. You can access the file directly at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco8-seg.yaml. The YAML file includes essential information about dataset paths, classes, and configuration settings required for model training and validation.

Using mosaicing during training helps increase the diversity and variety of objects and scenes in each training batch. This technique combines multiple images into a single composite image, enhancing the model's ability to generalize to different object sizes, aspect ratios, and contexts within the scene. Mosaicing is beneficial for improving a model's robustness and accuracy, especially when working with small datasets like COCO8-Seg. For an example of mosaiced images, see the Sample Images and Annotations section.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8-seg dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/segment/coco8-seg/
# Example usage: yolo train data=coco8-seg.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8-seg ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8-seg # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8-seg.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo segment train data=coco8-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/coco/

**Contents:**
- COCO Dataset
- COCO Pretrained Models
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ

The COCO (Common Objects in Context) dataset is a large-scale object detection, segmentation, and captioning dataset. It is designed to encourage research on a wide variety of object categories and is commonly used for benchmarking computer vision models. It is an essential dataset for researchers and developers working on object detection, segmentation, and pose estimation tasks.

Watch: Ultralytics COCO Dataset Overview

The COCO dataset is split into three subsets:

The COCO dataset is widely used for training and evaluating deep learning models in object detection (such as Ultralytics YOLO, Faster R-CNN, and SSD), instance segmentation (such as Mask R-CNN), and keypoint detection (such as OpenPose). The dataset's diverse set of object categories, large number of annotated images, and standardized evaluation metrics make it an essential resource for computer vision researchers and practitioners.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO dataset, the coco.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml.

ultralytics/cfg/datasets/coco.yaml

To train a YOLO26n model on the COCO dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The COCO dataset contains a diverse set of images with various object categories and complex scenes. Here are some examples of images from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the COCO dataset and the benefits of using mosaicing during the training process.

If you use the COCO dataset in your research or development work, please cite the following paper:

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the COCO dataset website.

The COCO dataset (Common Objects in Context) is a large-scale dataset used for object detection, segmentation, and captioning. It contains 330K images with detailed annotations for 80 object categories, making it essential for benchmarking and training computer vision models. Researchers use COCO due to its diverse categories and standardized evaluation metrics like mean Average Precision (mAP).

To train a YOLO26 model using the COCO dataset, you can use the following code snippets:

Refer to the Training page for more details on available arguments.

The COCO dataset includes:

Pretrained YOLO26 models on the COCO dataset can be downloaded from the links provided in the documentation. Examples include:

These models vary in size, mAP, and inference speed, providing options for different performance and resource requirements.

The COCO dataset is split into three subsets:

The dataset's YAML configuration file is available at coco.yaml, which defines paths, classes, and dataset details.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO 2017 dataset https://cocodataset.org by Microsoft
# Documentation: https://docs.ultralytics.com/datasets/detect/coco/
# Example usage: yolo train data=coco.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco ← downloads here (20.1 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco # dataset root dir
train: train2017.txt # train images (relative to 'path') 118287 images
val: val2017.txt # val images (relative to 'path') 5000 images
test: test-dev2017.txt # 20288 of 40670 images, submit to https://competitions.codalab.org/competitions/20794

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: |
  from pathlib import Path

  from ultralytics.utils import ASSETS_URL
  from ultralytics.utils.downloads import download

  # Download labels
  segments = True  # segment or box labels
  dir = Path(yaml["path"])  # dataset root dir
  urls = [ASSETS_URL + ("/coco2017labels-segments.zip" if segments else "/coco2017labels.zip")]  # labels
  download(urls, dir=dir.parent)
  # Download data
  urls = [
      "http://images.cocodataset.org/zips/train2017.zip",  # 19G, 118k images
      "http://images.cocodataset.org/zips/val2017.zip",  # 1G, 5k images
      "http://images.cocodataset.org/zips/test2017.zip",  # 7G, 41k images (optional)
  ]
  download(urls, dir=dir / "images", threads=3)
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=coco.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO-Pose Dataset

**URL:** https://docs.ultralytics.com/datasets/pose/coco/

**Contents:**
- COCO-Pose Dataset
- COCO-Pose Pretrained Models
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ

The COCO-Pose dataset is a specialized version of the COCO (Common Objects in Context) dataset, designed for pose estimation tasks. It leverages the COCO Keypoints 2017 images and labels to enable the training of models like YOLO for pose estimation tasks.

The COCO-Pose dataset is split into three subsets:

The COCO-Pose dataset is specifically used for training and evaluating deep learning models in keypoint detection and pose estimation tasks, such as OpenPose. The dataset's large number of annotated images and standardized evaluation metrics make it an essential resource for computer vision researchers and practitioners focused on pose estimation.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO-Pose dataset, the coco-pose.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco-pose.yaml.

ultralytics/cfg/datasets/coco-pose.yaml

To train a YOLO26n-pose model on the COCO-Pose dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The COCO-Pose dataset contains a diverse set of images with human figures annotated with keypoints. Here are some examples of images from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the COCO-Pose dataset and the benefits of using mosaicing during the training process.

If you use the COCO-Pose dataset in your research or development work, please cite the following paper:

We would like to acknowledge the COCO Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the COCO-Pose dataset and its creators, visit the COCO dataset website.

The COCO-Pose dataset is a specialized version of the COCO (Common Objects in Context) dataset designed for pose estimation tasks. It builds upon the COCO Keypoints 2017 images and annotations, allowing for the training of models like Ultralytics YOLO for detailed pose estimation. For instance, you can use the COCO-Pose dataset to train a YOLO26n-pose model by loading a pretrained model and training it with a YAML configuration. For training examples, refer to the Training documentation.

Training a YOLO26 model on the COCO-Pose dataset can be accomplished using either Python or CLI commands. For example, to train a YOLO26n-pose model for 100 epochs with an image size of 640, you can follow the steps below:

For more details on the training process and available arguments, check the training page.

The COCO-Pose dataset provides several standardized evaluation metrics for pose estimation tasks, similar to the original COCO dataset. Key metrics include the Object Keypoint Similarity (OKS), which evaluates the accuracy of predicted keypoints against ground truth annotations. These metrics allow for thorough performance comparisons between different models. For instance, the COCO-Pose pretrained models such as YOLO26n-pose, YOLO26s-pose, and others have specific performance metrics listed in the documentation, like mAPpose50-95 and mAPpose50.

The COCO-Pose dataset is split into three subsets:

These subsets help organize the training, validation, and testing phases effectively. For configuration details, explore the coco-pose.yaml file available on GitHub.

The COCO-Pose dataset extends the COCO Keypoints 2017 annotations to include 17 keypoints for human figures, enabling detailed pose estimation. Standardized evaluation metrics (e.g., OKS) facilitate comparisons across different models. Applications of the COCO-Pose dataset span various domains, such as sports analytics, healthcare, and human-computer interaction, wherever detailed pose estimation of human figures is required. For practical use, leveraging pretrained models like those provided in the documentation (e.g., YOLO26n-pose) can significantly streamline the process (Key Features).

If you use the COCO-Pose dataset in your research or development work, please cite the paper with the following BibTeX entry.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO 2017 Keypoints dataset https://cocodataset.org by Microsoft
# Documentation: https://docs.ultralytics.com/datasets/pose/coco/
# Example usage: yolo train data=coco-pose.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco-pose ← downloads here (20.1 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco-pose # dataset root dir
train: train2017.txt # train images (relative to 'path') 56599 images
val: val2017.txt # val images (relative to 'path') 2346 images
test: test-dev2017.txt # 20288 of 40670 images, submit to https://codalab.lisn.upsaclay.fr/competitions/7403

# Keypoints
kpt_shape: [17, 3] # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
flip_idx: [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

# Classes
names:
  0: person

# Keypoint names per class
kpt_names:
  0:
    - nose
    - left_eye
    - right_eye
    - left_ear
    - right_ear
    - left_shoulder
    - right_shoulder
    - left_elbow
    - right_elbow
    - left_wrist
    - right_wrist
    - left_hip
    - right_hip
    - left_knee
    - right_knee
    - left_ankle
    - right_ankle

# Download script/URL (optional)
download: |
  from pathlib import Path

  from ultralytics.utils import ASSETS_URL
  from ultralytics.utils.downloads import download

  # Download labels
  dir = Path(yaml["path"])  # dataset root dir

  urls = [f"{ASSETS_URL}/coco2017labels-pose.zip"]
  download(urls, dir=dir.parent)
  # Download data
  urls = [
      "http://images.cocodataset.org/zips/train2017.zip",  # 19G, 118k images
      "http://images.cocodataset.org/zips/val2017.zip",  # 1G, 5k images
      "http://images.cocodataset.org/zips/test2017.zip",  # 7G, 41k images (optional)
  ]
  download(urls, dir=dir / "images", threads=3)
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco-pose.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo pose train data=coco-pose.yaml model=yolo26n-pose.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## COCO-Seg Dataset

**URL:** https://docs.ultralytics.com/datasets/segment/coco/

**Contents:**
- COCO-Seg Dataset
- COCO-Seg Pretrained Models
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ

The COCO-Seg dataset, an extension of the COCO (Common Objects in Context) dataset, is specially designed to aid research in object instance segmentation. It uses the same images as COCO but introduces more detailed segmentation annotations. This dataset is a crucial resource for researchers and developers working on instance segmentation tasks, especially for training Ultralytics YOLO models.

The COCO-Seg dataset is partitioned into three subsets:

COCO-Seg is widely used for training and evaluating deep learning models in instance segmentation, such as the YOLO models. The large number of annotated images, the diversity of object categories, and the standardized evaluation metrics make it an indispensable resource for computer vision researchers and practitioners.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the COCO-Seg dataset, the coco.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/coco.yaml.

ultralytics/cfg/datasets/coco.yaml

To train a YOLO26n-seg model on the COCO-Seg dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

COCO-Seg, like its predecessor COCO, contains a diverse set of images with various object categories and complex scenes. However, COCO-Seg introduces more detailed instance segmentation masks for each object in the images. Here are some examples of images from the dataset, along with their corresponding instance segmentation masks:

The example showcases the variety and complexity of the images in the COCO-Seg dataset and the benefits of using mosaicing during the training process.

If you use the COCO-Seg dataset in your research or development work, please cite the original COCO paper and acknowledge the extension to COCO-Seg:

We extend our thanks to the COCO Consortium for creating and maintaining this invaluable resource for the computer vision community. For more information about the COCO dataset and its creators, visit the COCO dataset website.

The COCO-Seg dataset is an extension of the original COCO (Common Objects in Context) dataset, specifically designed for instance segmentation tasks. While it uses the same images as the COCO dataset, COCO-Seg includes more detailed segmentation annotations, making it a powerful resource for researchers and developers focusing on object instance segmentation.

To train a YOLO26n-seg model on the COCO-Seg dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a detailed list of available arguments, refer to the model Training page.

The COCO-Seg dataset includes several key features:

The COCO-Seg dataset supports multiple pretrained YOLO26 segmentation models with varying performance metrics. Here's a summary of the available models and their key metrics:

These models range from the lightweight YOLO26n-seg to the more powerful YOLO26x-seg, offering different trade-offs between speed and accuracy to suit various application requirements. For more information on model selection, visit the Ultralytics models page.

The COCO-Seg dataset is partitioned into three subsets for specific training and evaluation needs:

For smaller experimentation needs, you might also consider using the COCO8-seg dataset, which is a compact version containing just 8 images from the COCO train 2017 set.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO 2017 dataset https://cocodataset.org by Microsoft
# Documentation: https://docs.ultralytics.com/datasets/detect/coco/
# Example usage: yolo train data=coco.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco ← downloads here (20.1 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco # dataset root dir
train: train2017.txt # train images (relative to 'path') 118287 images
val: val2017.txt # val images (relative to 'path') 5000 images
test: test-dev2017.txt # 20288 of 40670 images, submit to https://competitions.codalab.org/competitions/20794

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: |
  from pathlib import Path

  from ultralytics.utils import ASSETS_URL
  from ultralytics.utils.downloads import download

  # Download labels
  segments = True  # segment or box labels
  dir = Path(yaml["path"])  # dataset root dir
  urls = [ASSETS_URL + ("/coco2017labels-segments.zip" if segments else "/coco2017labels.zip")]  # labels
  download(urls, dir=dir.parent)
  # Download data
  urls = [
      "http://images.cocodataset.org/zips/train2017.zip",  # 19G, 118k images
      "http://images.cocodataset.org/zips/val2017.zip",  # 1G, 5k images
      "http://images.cocodataset.org/zips/test2017.zip",  # 7G, 41k images (optional)
  ]
  download(urls, dir=dir / "images", threads=3)
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo segment train data=coco.yaml model=yolo26n-seg.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{lin2015microsoft,
      title={Microsoft COCO: Common Objects in Context},
      author={Tsung-Yi Lin and Michael Maire and Serge Belongie and Lubomir Bourdev and Ross Girshick and James Hays and Pietro Perona and Deva Ramanan and C. Lawrence Zitnick and Piotr Dollár},
      year={2015},
      eprint={1405.0312},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## Construction-PPE Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/construction-ppe/

**Contents:**
- Construction-PPE Dataset
- Dataset Structure
- Business Value
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- License and Attribution
- FAQ
  - What makes the Construction-PPE dataset unique?

The Construction-PPE dataset is designed to improve safety compliance in construction sites by enabling detection of essential protective gear such as helmets, vests, gloves, boots, and goggles, along with annotations for missing equipment. Curated from real construction environments, it includes both compliant and non-compliant cases, making it a valuable resource for training AI models that monitor workplace safety.

Watch: How to train Ultralytics YOLO on Personal Protective Equipment Dataset | VisionAI in Construction 👷

The Construction-PPE dataset is organized into three main subsets:

Each image is annotated in the Ultralytics YOLO format ensuring compatibility with state-of-the-art object detection and tracking pipelines.

The dataset provides 11 classes divided into positive (worn PPE) and negative (missing PPE) categories. This dual-positive/negative structure enables models to detect properly worn gear and identify safety violations.

Construction-PPE powers a variety of safety-focused computer vision applications:

The Construction-PPE dataset includes a YAML configuration file that defines the training and validation image paths along with the full list of object classes. You can access the construction-ppe.yaml file directly in the Ultralytics repository here: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/construction-ppe.yaml

ultralytics/cfg/datasets/construction-ppe.yaml

You can train a YOLO26n model on the Construction-PPE dataset for 100 epochs with an image size of 640. The following examples show how to get started quickly. For more options and advanced configurations, see the Training guide.

The dataset captures construction workers across varied environments, lighting conditions, and postures. Both compliant and non-compliant cases are included.

Construction-PPE is developed and released under the AGPL-3.0 License, supporting open-source research and commercial applications with proper attribution.

If you use this dataset in your research, please cite it:

Unlike generic construction datasets, Construction-PPE explicitly includes missing equipment classes. This dual-labeling approach allows models to not only detect PPE but also flag violations in real-time.

The dataset covers helmets, vests, gloves, boots, goggles, and workers, along with their “missing PPE” counterparts. This ensures comprehensive compliance coverage.

To train a YOLO26 model using the Construction-PPE dataset, you can use the following code snippets:

Yes. Images are curated from real construction sites under diverse conditions. This makes it highly effective for building deployable workplace safety monitoring systems.

The dataset enables real-time detection of personal protective equipment, helping monitor worker safety on construction sites. With classes for both worn and missing gear, it supports AI systems that can automatically flag safety violations, generate compliance insights, and reduce risks. It also provides a practical resource for developing computer vision solutions in workplace safety, robotics, and academic research.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Construction-PPE dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/construction-ppe/
# Example usage: yolo train data=construction-ppe.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── construction-ppe ← downloads here (178.4 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: construction-ppe # dataset root dir
train: images/train # train images (relative to 'path') 1132 images
val: images/val # val images (relative to 'path') 143 images
test: images/test # test images (relative to 'path') 141 images

# Classes
names:
  0: helmet
  1: gloves
  2: vest
  3: boots
  4: goggles
  5: none
  6: Person
  7: no_helmet
  8: no_goggle
  9: no_gloves
  10: no_boots

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/construction-ppe.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolo26n.pt")

# Train the model on Construction-PPE dataset
model.train(data="construction-ppe.yaml", epochs=100, imgsz=640)
```

Example 3 (unknown):
```unknown
yolo detect train data=construction-ppe.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (swift):
```swift
@dataset{Dalvi_Construction_PPE_Dataset_2025,
    author = {Mrunmayee Dalvi and Niyati Singh and Sahil Bhingarde and Ketaki Chalke},
    title = {Construction-PPE: Personal Protective Equipment Detection Dataset},
    month = {January},
    year = {2025},
    version = {1.0.0},
    license = {AGPL-3.0},
    url = {https://docs.ultralytics.com/datasets/detect/construction-ppe/},
    publisher = {Ultralytics}
}
```

---

## Crack Segmentation Dataset

**URL:** https://docs.ultralytics.com/datasets/segment/crack-seg/

**Contents:**
- Crack Segmentation Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Crack Segmentation Dataset?
  - How do I train a model using the Crack Segmentation Dataset with Ultralytics YOLO26?

The Crack Segmentation Dataset, available on Roboflow Universe, is an extensive resource designed for individuals involved in transportation and public safety studies. It is also beneficial for developing self-driving car models or exploring various computer vision applications. This dataset is part of the broader collection available on the Ultralytics Datasets Hub.

Watch: Crack segmentation using Ultralytics YOLOv9.

Comprising 4029 static images captured from diverse road and wall scenarios, this dataset is a valuable asset for crack segmentation tasks. Whether you are researching transportation infrastructure or aiming to enhance the accuracy of autonomous driving systems, this dataset provides a rich collection of images for training deep learning models.

The Crack Segmentation Dataset is organized into three subsets:

Crack segmentation finds practical applications in infrastructure maintenance, aiding in the identification and assessment of structural damage in buildings, bridges, and roads. It also plays a crucial role in enhancing road safety by enabling automated systems to detect pavement cracks for timely repairs.

In industrial settings, crack detection using deep learning models like Ultralytics YOLO26 helps ensure building integrity in construction, prevents costly downtimes in manufacturing, and makes road inspections safer and more effective. Automatically identifying and classifying cracks allows maintenance teams to prioritize repairs efficiently, contributing to better model evaluation insights.

A YAML (Yet Another Markup Language) file defines the dataset configuration. It includes details about the dataset's paths, classes, and other relevant information. For the Crack Segmentation dataset, the crack-seg.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/crack-seg.yaml.

ultralytics/cfg/datasets/crack-seg.yaml

To train the Ultralytics YOLO26n-seg model on the Crack Segmentation dataset for 100 epochs with an image size of 640, use the following Python or CLI snippets. Refer to the model Training documentation page for a comprehensive list of available arguments and configurations like hyperparameter tuning.

The Crack Segmentation dataset contains a diverse collection of images captured from various perspectives, showcasing different types of cracks on roads and walls. Here are some examples:

This image demonstrates instance segmentation, featuring annotated bounding boxes with masks outlining identified cracks. The dataset includes images from different locations and environments, making it a comprehensive resource for developing robust models for this task. Techniques like data augmentation can further enhance dataset diversity. Learn more about instance segmentation and tracking in our guide.

The example highlights the diversity within the Crack Segmentation dataset, emphasizing the importance of high-quality data for training effective computer vision models.

If you use the Crack Segmentation dataset in your research or development work, please cite the source appropriately. The dataset was made available via Roboflow:

We acknowledge the team at Roboflow for making the Crack Segmentation dataset available, providing a valuable resource for the computer vision community, particularly for projects related to road safety and infrastructure assessment.

The Crack Segmentation Dataset is a collection of 4029 static images designed for transportation and public safety studies. It's suitable for tasks like self-driving car model development and infrastructure maintenance. It includes training, testing, and validation sets for crack detection and segmentation tasks.

To train an Ultralytics YOLO26 model on this dataset, use the provided Python or CLI examples. Detailed instructions and parameters are available on the model Training page. You can manage your training process using tools like Ultralytics Platform.

This dataset is valuable for self-driving car projects due to its diverse images of roads and walls, covering various real-world scenarios. This diversity improves the robustness of models trained for crack detection, which is crucial for road safety and infrastructure assessment. The detailed annotations aid in developing models that can accurately identify potential road hazards.

Ultralytics YOLO provides real-time object detection, segmentation, and classification capabilities, making it highly suitable for crack segmentation tasks. It efficiently handles large datasets and complex scenarios. The framework includes comprehensive modes for Training, Prediction, and Exporting models. YOLO's anchor-free detection approach can improve performance on irregular shapes like cracks, and performance can be measured using standard metrics.

If using this dataset in your work, please cite it using the provided BibTeX entry above to give appropriate credit to the creators.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Crack-seg dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/segment/crack-seg/
# Example usage: yolo train data=crack-seg.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── crack-seg ← downloads here (91.6 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: crack-seg # dataset root dir
train: images/train # train images (relative to 'path') 3717 images
val: images/val # val images (relative to 'path') 112 images
test: images/test # test images (relative to 'path') 200 images

# Classes
names:
  0: crack

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/crack-seg.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
# Using a pretrained model like yolo26n-seg.pt is recommended for faster convergence
model = YOLO("yolo26n-seg.pt")

# Train the model on the Crack Segmentation dataset
# Ensure 'crack-seg.yaml' is accessible or provide the full path
results = model.train(data="crack-seg.yaml", epochs=100, imgsz=640)

# After training, the model can be used for prediction or exported
# results = model.predict(source='path/to/your/images')
```

Example 3 (julia):
```julia
# Start training from a pretrained *.pt model using the Command Line Interface
# Ensure the dataset YAML file 'crack-seg.yaml' is correctly configured and accessible
yolo segment train data=crack-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640
```

Example 4 (swift):
```swift
@misc{ crack-bphdr_dataset,
    title = { crack Dataset },
    type = { Open Source Dataset },
    author = { University },
    url = { https://universe.roboflow.com/university-bswxt/crack-bphdr },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2022 },
    month = { dec },
    note = { visited on 2024-01-23 },
}
```

---

## Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/

**Contents:**
- Datasets Overview
- Object Detection
- Instance Segmentation
- Pose Estimation
- Classification
- Oriented Bounding Boxes (OBB)
- Multi-Object Tracking
- Contribute New Datasets
  - Steps to Contribute a New Dataset
  - Example Code to Optimize and Zip a Dataset

Ultralytics provides support for various datasets to facilitate computer vision tasks such as detection, instance segmentation, pose estimation, classification, and multi-object tracking. Below is a list of the main Ultralytics datasets, followed by a summary of each computer vision task and the respective datasets.

Watch: Ultralytics Datasets Overview

Bounding box object detection is a computer vision technique that involves detecting and localizing objects in an image by drawing a bounding box around each object.

Instance segmentation is a computer vision technique that involves identifying and localizing objects in an image at the pixel level. Unlike semantic segmentation which only classifies each pixel, instance segmentation distinguishes between different instances of the same class.

Pose estimation is a technique used to determine the pose of the object relative to the camera or the world coordinate system. This involves identifying key points or joints on objects, particularly humans or animals.

Image classification is a computer vision task that involves categorizing an image into one or more predefined classes or categories based on its visual content.

Oriented Bounding Boxes (OBB) is a method in computer vision for detecting angled objects in images using rotated bounding boxes, often applied to aerial and satellite imagery. Unlike traditional bounding boxes, OBB can better fit objects at various orientations.

Multi-object tracking is a computer vision technique that involves detecting and tracking multiple objects over time in a video sequence. This task extends object detection by maintaining consistent identities of objects across frames.

Contributing a new dataset involves several steps to ensure that it aligns well with the existing infrastructure. Below are the necessary steps:

Watch: How to Contribute to Ultralytics Datasets

Organize Dataset: Arrange your dataset into the correct folder structure. You should have images/ and labels/ top-level directories, and within each, a train/ and val/ subdirectory.

Create a data.yaml File: In your dataset's root directory, create a data.yaml file that describes the dataset, classes, and other necessary information.

Optimize and Zip a Dataset

By following these steps, you can contribute a new dataset that integrates well with Ultralytics' existing structure.

Ultralytics supports a wide variety of datasets for object detection, including:

These datasets facilitate training robust Ultralytics YOLO models for various object detection applications.

Contributing a new dataset involves several steps:

Visit Contribute New Datasets for a comprehensive guide.

Ultralytics Platform offers powerful features for dataset management and analysis, including:

The platform streamlines the transition from dataset management to model training, making the entire process more efficient. Learn more about Ultralytics Platform Datasets.

Ultralytics YOLO models provide several unique features for computer vision tasks:

Discover more about YOLO models on the Ultralytics Models page.

To optimize and zip a dataset using Ultralytics tools, follow this example code:

Optimize and Zip a Dataset

This process helps reduce dataset size for more efficient storage and faster download speeds. Learn more on how to Optimize and Zip a Dataset.

**Examples:**

Example 1 (unknown):
```unknown
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Example 2 (python):
```python
from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("path/to/dataset")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)
```

Example 3 (python):
```python
from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("path/to/dataset")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)
```

---

## Dog-Pose Dataset

**URL:** https://docs.ultralytics.com/datasets/pose/dog-pose/

**Contents:**
- Dog-Pose Dataset
- Introduction
- Dataset Structure
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Dog-pose dataset, and how is it used with Ultralytics YOLO26?
  - How do I train a YOLO26 model using the Dog-pose dataset in Ultralytics?

The Ultralytics Dog-Pose dataset is a high-quality and extensive dataset specifically curated for dog keypoint estimation. With 6,773 training images and 1,703 test images, this dataset provides a solid foundation for training robust pose estimation models.

Watch: How to Train Ultralytics YOLO26 on the Stanford Dog Pose Estimation Dataset | Step-by-Step Tutorial

Each annotated image includes 24 keypoints with 3 dimensions per keypoint (x, y, visibility), making it a valuable resource for advanced research and development in computer vision.

This dataset is intended for use with Ultralytics Platform and YOLO26.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It includes paths, keypoint details, and other relevant information. In the case of the Dog-pose dataset, The dog-pose.yaml is available at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/dog-pose.yaml.

ultralytics/cfg/datasets/dog-pose.yaml

To train a YOLO26n-pose model on the Dog-pose dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the Dog-pose dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the Dog-pose dataset and the benefits of using mosaicing during the training process.

If you use the Dog-pose dataset in your research or development work, please cite the following paper:

We would like to acknowledge the Stanford team for creating and maintaining this valuable resource for the computer vision community. For more information about the Dog-pose dataset and its creators, visit the Stanford Dogs Dataset website.

The Dog-Pose dataset features 6,773 training and 1,703 test images annotated with 24 keypoints for dog pose estimation. It's designed for training and validating models with Ultralytics YOLO26, supporting applications like animal behavior analysis, pet monitoring, and veterinary studies. The dataset's comprehensive annotations make it ideal for developing accurate pose estimation models for canines.

To train a YOLO26n-pose model on the Dog-pose dataset for 100 epochs with an image size of 640, follow these examples:

For a comprehensive list of training arguments, refer to the model Training page.

The Dog-pose dataset offers several benefits:

Large and Diverse Dataset: With over 8,400 images, it provides substantial data covering a wide range of dog poses, breeds, and contexts, enabling robust model training and evaluation.

Detailed Keypoint Annotations: Each image includes 24 keypoints with 3 dimensions per keypoint (x, y, visibility), offering precise annotations for training accurate pose detection models.

Real-World Scenarios: Includes images from varied environments, enhancing the model's ability to generalize to real-world applications like pet monitoring and behavior analysis.

Transfer Learning Advantage: The dataset works well with transfer learning techniques, allowing models pretrained on human pose datasets to adapt to dog-specific features.

For more about its features and usage, see the Dataset Introduction section.

Mosaicing, as illustrated in the sample images from the Dog-pose dataset, merges multiple images into a single composite, enriching the diversity of objects and scenes in each training batch. This technique offers several benefits:

This approach leads to more robust models that perform better in real-world scenarios. For example images, refer to the Sample Images and Annotations section.

The Dog-pose dataset YAML file can be found at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/dog-pose.yaml. This file defines the dataset configuration, including paths, classes, keypoint details, and other relevant information. The YAML specifies 24 keypoints with 3 dimensions per keypoint, making it suitable for detailed pose estimation tasks.

To use this file with YOLO26 training scripts, simply reference it in your training command as shown in the Usage section. The dataset will be automatically downloaded when first used, making setup straightforward.

For more FAQs and detailed documentation, visit the Ultralytics Documentation.

**Examples:**

Example 1 (unknown):
```unknown
datasets/dog-pose/
├── images/{train,test}
└── labels/{train,test}
```

Example 2 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Dogs dataset http://vision.stanford.edu/aditya86/ImageNetDogs/ by Stanford
# Documentation: https://docs.ultralytics.com/datasets/pose/dog-pose/
# Example usage: yolo train data=dog-pose.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── dog-pose ← downloads here (337 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: dog-pose # dataset root dir
train: images/train # train images (relative to 'path') 6773 images
val: images/val # val images (relative to 'path') 1703 images

# Keypoints
kpt_shape: [24, 3] # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)

# Classes
names:
  0: dog

# Keypoint names per class
kpt_names:
  0:
    - front_left_paw
    - front_left_knee
    - front_left_elbow
    - rear_left_paw
    - rear_left_knee
    - rear_left_elbow
    - front_right_paw
    - front_right_knee
    - front_right_elbow
    - rear_right_paw
    - rear_right_knee
    - rear_right_elbow
    - tail_start
    - tail_end
    - left_ear_base
    - right_ear_base
    - nose
    - chin
    - left_ear_tip
    - right_ear_tip
    - left_eye
    - right_eye
    - withers
    - throat

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/dog-pose.zip
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="dog-pose.yaml", epochs=100, imgsz=640)
```

Example 4 (sql):
```sql
# Start training from a pretrained *.pt model
yolo pose train data=dog-pose.yaml model=yolo26n-pose.pt epochs=100 imgsz=640
```

---

## DOTA8 Dataset

**URL:** https://docs.ultralytics.com/datasets/obb/dota8/

**Contents:**
- DOTA8 Dataset
- Introduction
- Dataset Structure
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the DOTA8 dataset and how can it be used?
  - How do I train a YOLO26 model using the DOTA8 dataset?

Ultralytics DOTA8 is a small but versatile oriented object detection dataset composed of the first 8 images of the split DOTAv1 set, 4 for training and 4 for validation. This dataset is ideal for testing and debugging object detection models, or for experimenting with new detection approaches. With 8 images, it is small enough to be easily manageable, yet diverse enough to test training pipelines for errors and act as a sanity check before training larger datasets.

This dataset is intended for use with Ultralytics Platform and YOLO26.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the DOTA8 dataset, the dota8.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/dota8.yaml.

ultralytics/cfg/datasets/dota8.yaml

To train a YOLO26n-obb model on the DOTA8 dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the DOTA8 dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the DOTA8 dataset and the benefits of using mosaicing during the training process.

If you use the DOTA dataset in your research or development work, please cite the following paper:

A special note of gratitude to the team behind the DOTA datasets for their commendable effort in curating this dataset. For an exhaustive understanding of the dataset and its nuances, please visit the official DOTA website.

The DOTA8 dataset is a small, versatile oriented object detection dataset made up of the first 8 images from the DOTAv1 split set, with 4 images designated for training and 4 for validation. It's ideal for testing and debugging object detection models like Ultralytics YOLO26. Due to its manageable size and diversity, it helps in identifying pipeline errors and running sanity checks before deploying larger datasets. Learn more about object detection with Ultralytics YOLO26.

To train a YOLO26n-obb model on the DOTA8 dataset for 100 epochs with an image size of 640, you can use the following code snippets. For comprehensive argument options, refer to the model Training page.

The DOTA dataset is known for its large-scale benchmark and the challenges it presents for object detection in aerial images. The DOTA8 subset is a smaller, manageable dataset ideal for initial tests. You can access the dota8.yaml file, which contains paths, classes, and configuration details, at this GitHub link.

Mosaicing combines multiple images into one during training, increasing the variety of objects and contexts within each batch. This improves a model's ability to generalize to different object sizes, aspect ratios, and scenes. This technique can be visually demonstrated through a training batch composed of mosaiced DOTA8 dataset images, helping in robust model development. Explore more about mosaicing and training techniques on our Training page.

Ultralytics YOLO26 provides state-of-the-art real-time object detection capabilities, including features like oriented bounding boxes (OBB), instance segmentation, and a highly versatile training pipeline. It's suitable for various applications and offers pretrained models for efficient fine-tuning. Explore further about the advantages and usage in the Ultralytics YOLO26 documentation.

**Examples:**

Example 1 (unknown):
```unknown
datasets/dota8/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Example 2 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# DOTA8 dataset (8 images from the DOTAv1 split) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/obb/dota8/
# Example usage: yolo train model=yolov8n-obb.pt data=dota8.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── dota8 ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: dota8 # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images

# Classes for DOTA 1.0
names:
  0: plane
  1: ship
  2: storage tank
  3: baseball diamond
  4: tennis court
  5: basketball court
  6: ground track field
  7: harbor
  8: bridge
  9: large vehicle
  10: small vehicle
  11: helicopter
  12: roundabout
  13: soccer ball field
  14: swimming pool

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/dota8.zip
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-obb.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="dota8.yaml", epochs=100, imgsz=640)
```

Example 4 (sql):
```sql
# Start training from a pretrained *.pt model
yolo obb train data=dota8.yaml model=yolo26n-obb.pt epochs=100 imgsz=640
```

---

## DOTA Dataset with OBB

**URL:** https://docs.ultralytics.com/datasets/obb/dota-v2/

**Contents:**
- DOTA Dataset with OBB
- Key Features
- Dataset Versions
  - DOTA-v1.0
  - DOTA-v1.5
  - DOTA-v2.0
- Dataset Structure
- Applications
- Dataset YAML
- Split DOTA images

DOTA stands as a specialized dataset, emphasizing object detection in aerial images. Originating from the DOTA series of datasets, it offers annotated images capturing a diverse array of aerial scenes with Oriented Bounding Boxes (OBB).

Watch: How to Train Ultralytics YOLO26 on the DOTA Dataset for Oriented Bounding Boxes in Google Colab

DOTA exhibits a structured layout tailored for OBB object detection challenges:

DOTA serves as a benchmark for training and evaluating models specifically tailored for aerial image analysis. With the inclusion of OBB annotations, it provides a unique challenge, enabling the development of specialized object detection models that cater to aerial imagery's nuances. The dataset is particularly valuable for applications in remote sensing, surveillance, and environmental monitoring.

A dataset YAML (Yet Another Markup Language) file specifies image/label roots, class names, and other important metadata. Ultralytics maintains official YAML files for the two most commonly used releases:

Use the YAML that matches the release you downloaded, or author a custom YAML if you are working with DOTA-v2 or another derivative.

The raw imagery routinely exceeds 10,000 pixels on a side, so tiling is required before feeding the data to YOLO. Use the helper below to slice the source imagery into overlapping 1024 × 1024 crops at multiple scales while keeping the annotations in sync.

Keep the output directory organized in the standard YOLO layout (images/train, labels/train, etc.) so you can reference it directly from the dataset YAML.

To train a model on the DOTA v1 dataset, you can utilize the following code snippets. Always refer to your model's documentation for a thorough list of available arguments. For those looking to experiment with a smaller subset first, consider using the DOTA8 dataset, which contains just 8 images for quick testing.

Please note that all images and associated annotations in the DOTAv1 dataset can be used for academic purposes, but commercial use is prohibited. Your understanding and respect for the dataset creators' wishes are greatly appreciated!

Having a glance at the dataset illustrates its depth:

The dataset's richness offers invaluable insights into object detection challenges exclusive to aerial imagery. The DOTA-v2.0 dataset has become particularly popular for remote sensing and aerial surveillance projects due to its comprehensive annotations and diverse object categories.

If you use DOTA in your work, please cite the relevant research papers:

A special note of gratitude to the team behind the DOTA datasets for their commendable effort in curating this dataset. For an exhaustive understanding of the dataset and its nuances, please visit the official DOTA website.

The DOTA dataset is a specialized dataset focused on object detection in aerial images. It features Oriented Bounding Boxes (OBB), providing annotated images from diverse aerial scenes. DOTA's diversity in object orientation, scale, and shape across its 1.7M annotations and 18 categories makes it ideal for developing and evaluating models tailored for aerial imagery analysis, such as those used in surveillance, environmental monitoring, and disaster management.

DOTA utilizes Oriented Bounding Boxes (OBB) for annotation, which are represented by rotated rectangles encapsulating objects regardless of their orientation. This method ensures that objects, whether small or at different angles, are accurately captured. The dataset's multiscale images, ranging from 800 × 800 to 20,000 × 20,000 pixels, further allow for the detection of both small and large objects effectively. This approach is particularly valuable for aerial imagery where objects appear at various angles and scales.

To train a model on the DOTA dataset, you can use the following example with Ultralytics YOLO:

For more details on how to split and preprocess the DOTA images, refer to the split DOTA images section.

For a detailed comparison and additional specifics, check the dataset versions section.

DOTA images, which can be very large, are split into smaller resolutions for manageable training. Here's a Python snippet to split images:

This process facilitates better training efficiency and model performance. For detailed instructions, visit the split DOTA images section.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# DOTA 1.0 dataset https://captain-whu.github.io/DOTA/index.html for object detection in aerial images by Wuhan University
# Documentation: https://docs.ultralytics.com/datasets/obb/dota-v2/
# Example usage: yolo train model=yolov8n-obb.pt data=DOTAv1.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── dota1 ← downloads here (2 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: DOTAv1 # dataset root dir
train: images/train # train images (relative to 'path') 1411 images
val: images/val # val images (relative to 'path') 458 images
test: images/test # test images (optional) 937 images

# Classes for DOTA 1.0
names:
  0: plane
  1: ship
  2: storage tank
  3: baseball diamond
  4: tennis court
  5: basketball court
  6: ground track field
  7: harbor
  8: bridge
  9: large vehicle
  10: small vehicle
  11: helicopter
  12: roundabout
  13: soccer ball field
  14: swimming pool

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/DOTAv1.zip
```

Example 2 (sql):
```sql
from ultralytics.data.split_dota import split_test, split_trainval

# Split train and val set, with labels.
split_trainval(
    data_root="path/to/DOTAv1.0/",
    save_dir="path/to/DOTAv1.0-split/",
    rates=[0.5, 1.0, 1.5],  # multiscale
    gap=500,
)
# Split test set, without labels.
split_test(
    data_root="path/to/DOTAv1.0/",
    save_dir="path/to/DOTAv1.0-split/",
    rates=[0.5, 1.0, 1.5],  # multiscale
    gap=500,
)
```

Example 3 (python):
```python
from ultralytics import YOLO

# Create a new YOLO26n-OBB model from scratch
model = YOLO("yolo26n-obb.yaml")

# Train the model on the DOTAv1 dataset
results = model.train(data="DOTAv1.yaml", epochs=100, imgsz=1024)
```

Example 4 (markdown):
```markdown
# Train a new YOLO26n-OBB model on the DOTAv1 dataset
yolo obb train data=DOTAv1.yaml model=yolo26n-obb.pt epochs=100 imgsz=1024
```

---

## Fashion-MNIST Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/fashion-mnist/

**Contents:**
- Fashion-MNIST Dataset
- Key Features
- Dataset Structure
- Labels
- Applications
- Usage
- Sample Images and Annotations
- Acknowledgments
- FAQ
  - What is the Fashion-MNIST dataset and how is it different from MNIST?

The Fashion-MNIST dataset is a database of Zalando's article images—consisting of a training set of 60,000 examples and a test set of 10,000 examples. Each example is a 28x28 grayscale image, associated with a label from 10 classes. Fashion-MNIST is intended to serve as a direct drop-in replacement for the original MNIST dataset for benchmarking machine learning algorithms.

Watch: How to do Image Classification on Fashion MNIST Dataset using Ultralytics YOLO26

The Fashion-MNIST dataset is split into two subsets:

Each training and test example is assigned to one of the following labels:

The Fashion-MNIST dataset is widely used for training and evaluating deep learning models in image classification tasks, such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning algorithms. The dataset's simple and well-structured format makes it an essential resource for researchers and practitioners in the field of machine learning and computer vision.

To train a CNN model on the Fashion-MNIST dataset for 100 epochs with an image size of 28x28, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Fashion-MNIST dataset contains grayscale images of Zalando's article images, providing a well-structured dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the images in the Fashion-MNIST dataset, highlighting the importance of a diverse dataset for training robust image classification models.

If you use the Fashion-MNIST dataset in your research or development work, please acknowledge the dataset by linking to the GitHub repository. This dataset was made available by Zalando Research.

The Fashion-MNIST dataset is a collection of 70,000 grayscale images of Zalando's article images, intended as a modern replacement for the original MNIST dataset. It serves as a benchmark for machine learning models in the context of image classification tasks. Unlike MNIST, which contains handwritten digits, Fashion-MNIST consists of 28x28-pixel images categorized into 10 fashion-related classes, such as T-shirt/top, trouser, and ankle boot.

To train an Ultralytics YOLO model on the Fashion-MNIST dataset, you can use both Python and CLI commands. Here's a quick example to get you started:

For more detailed training parameters, refer to the Training page.

The Fashion-MNIST dataset is widely recognized in the deep learning community as a robust alternative to MNIST. It offers a more complex and varied set of images, making it an excellent choice for benchmarking image classification models. The dataset's structure, comprising 60,000 training images and 10,000 testing images, each labeled with one of 10 classes, makes it ideal for evaluating the performance of different machine learning algorithms in a more challenging context.

Yes, Ultralytics YOLO models can be used for image classification tasks, including those involving the Fashion-MNIST dataset. YOLO26, for example, supports various vision tasks such as detection, segmentation, and classification. To get started with image classification tasks, refer to the Classification page.

The Fashion-MNIST dataset is divided into two main subsets: 60,000 training images and 10,000 testing images. Each image is a 28x28-pixel grayscale picture representing one of 10 fashion-related classes. The simplicity and well-structured format make it ideal for training and evaluating models in machine learning and computer vision tasks. For more details on the dataset structure, see the Dataset Structure section.

If you utilize the Fashion-MNIST dataset in your research or development projects, it's important to acknowledge it by linking to the GitHub repository. This helps in attributing the data to Zalando Research, who made the dataset available for public use.

**Examples:**

Example 1 (unknown):
```unknown
0. T-shirt/top
1. Trouser
2. Pullover
3. Dress
4. Coat
5. Sandal
6. Shirt
7. Sneaker
8. Bag
9. Ankle boot
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="fashion-mnist", epochs=100, imgsz=28)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=fashion-mnist model=yolo26n-cls.pt epochs=100 imgsz=28
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a pretrained model
model = YOLO("yolo26n-cls.pt")

# Train the model on Fashion-MNIST
results = model.train(data="fashion-mnist", epochs=100, imgsz=28)
```

---

## Global Wheat Head Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/globalwheat2020/

**Contents:**
- Global Wheat Head Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Global Wheat Head Dataset used for?

The Global Wheat Head Dataset is a collection of images designed to support the development of accurate wheat head detection models for applications in wheat phenotyping and crop management. Wheat heads, also known as spikes, are the grain-bearing parts of the wheat plant. Accurate estimation of wheat head density and size is essential for assessing crop health, maturity, and yield potential. The dataset, created by a collaboration of nine research institutes from seven countries, covers multiple growing regions to ensure models generalize well across different environments.

The Global Wheat Head Dataset is organized into two main subsets:

The Global Wheat Head Dataset is widely used for training and evaluating deep learning models in wheat head detection tasks. The dataset's diverse set of images, capturing a wide range of appearances, environments, and conditions, make it a valuable resource for researchers and practitioners in the field of plant phenotyping and crop management.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. For the case of the Global Wheat Head Dataset, the GlobalWheat2020.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/GlobalWheat2020.yaml.

ultralytics/cfg/datasets/GlobalWheat2020.yaml

To train a YOLO26n model on the Global Wheat Head Dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Global Wheat Head Dataset contains a diverse set of outdoor field images, capturing the natural variability in wheat head appearances, environments, and conditions. Here are some examples of data from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the data in the Global Wheat Head Dataset and highlights the importance of accurate wheat head detection for applications in wheat phenotyping and crop management.

If you use the Global Wheat Head Dataset in your research or development work, please cite the following paper:

We would like to acknowledge the researchers and institutions that contributed to the creation and maintenance of the Global Wheat Head Dataset as a valuable resource for the plant phenotyping and crop management research community. For more information about the dataset and its creators, visit the Global Wheat Head Dataset website.

The Global Wheat Head Dataset is primarily used for developing and training deep learning models aimed at wheat head detection. This is crucial for applications in wheat phenotyping and crop management, allowing for more accurate estimations of wheat head density, size, and overall crop yield potential. Accurate detection methods help in assessing crop health and maturity, essential for efficient crop management.

To train a YOLO26n model on the Global Wheat Head Dataset, you can use the following code snippets. Make sure you have the GlobalWheat2020.yaml configuration file specifying dataset paths and classes:

For a comprehensive list of available arguments, refer to the model Training page.

Key features of the Global Wheat Head Dataset include:

These features facilitate the development of robust models capable of generalization across multiple regions.

The configuration YAML file for the Global Wheat Head Dataset, named GlobalWheat2020.yaml, is available on GitHub. You can access it at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/GlobalWheat2020.yaml. This file contains necessary information about dataset paths, classes, and other configuration details needed for model training in Ultralytics YOLO.

Wheat head detection is critical in crop management because it enables accurate estimation of wheat head density and size, which are essential for evaluating crop health, maturity, and yield potential. By leveraging deep learning models trained on datasets like the Global Wheat Head Dataset, farmers and researchers can better monitor and manage crops, leading to improved productivity and optimized resource use in agricultural practices. This technological advancement supports sustainable agriculture and food security initiatives.

For more information on applications of AI in agriculture, visit AI in Agriculture.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Global Wheat 2020 dataset https://www.global-wheat.com/ by University of Saskatchewan
# Documentation: https://docs.ultralytics.com/datasets/detect/globalwheat2020/
# Example usage: yolo train data=GlobalWheat2020.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── GlobalWheat2020 ← downloads here (7.0 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: GlobalWheat2020 # dataset root dir
train: # train images (relative to 'path') 3422 images
  - images/arvalis_1
  - images/arvalis_2
  - images/arvalis_3
  - images/ethz_1
  - images/rres_1
  - images/inrae_1
  - images/usask_1
val: # val images (relative to 'path') 748 images (WARNING: train set contains ethz_1)
  - images/ethz_1
test: # test images (optional) 1276 images
  - images/utokyo_1
  - images/utokyo_2
  - images/nau_1
  - images/uq_1

# Classes
names:
  0: wheat_head

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  from pathlib import Path

  from ultralytics.utils.downloads import download

  # Download
  dir = Path(yaml["path"])  # dataset root dir
  urls = [
      "https://zenodo.org/record/4298502/files/global-wheat-codalab-official.zip",
      "https://github.com/ultralytics/assets/releases/download/v0.0.0/GlobalWheat2020_labels.zip",
  ]
  download(urls, dir=dir)

  # Make Directories
  for p in "annotations", "images", "labels":
      (dir / p).mkdir(parents=True, exist_ok=True)

  # Move
  for p in (
      "arvalis_1",
      "arvalis_2",
      "arvalis_3",
      "ethz_1",
      "rres_1",
      "inrae_1",
      "usask_1",
      "utokyo_1",
      "utokyo_2",
      "nau_1",
      "uq_1",
  ):
      (dir / "global-wheat-codalab-official" / p).rename(dir / "images" / p)  # move to /images
      f = (dir / "global-wheat-codalab-official" / p).with_suffix(".json")  # json file
      if f.exists():
          f.rename((dir / "annotations" / p).with_suffix(".json"))  # move to /annotations
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="GlobalWheat2020.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=GlobalWheat2020.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@article{david2020global,
         title={Global Wheat Head Detection (GWHD) Dataset: A Large and Diverse Dataset of High-Resolution RGB-Labelled Images to Develop and Benchmark Wheat Head Detection Methods},
         author={David, Etienne and Madec, Simon and Sadeghi-Tehran, Pouria and Aasen, Helge and Zheng, Bangyou and Liu, Shouyang and Kirchgessner, Norbert and Ishikawa, Goro and Nagasawa, Koichi and Badhon, Minhajul and others},
         journal={arXiv preprint arXiv:2005.02162},
         year={2020}
}
```

---

## Hand Keypoints Dataset

**URL:** https://docs.ultralytics.com/datasets/pose/hand-keypoints/

**Contents:**
- Hand Keypoints Dataset
- Introduction
- Hand Landmarks
- Keypoints
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations

The hand-keypoints dataset contains 26,768 images of hands annotated with keypoints, making it suitable for training models like Ultralytics YOLO for pose estimation tasks. The annotations were generated using the Google MediaPipe library, ensuring high accuracy and consistency, and the dataset is compatible with Ultralytics YOLO26 formats.

Watch: Hand Keypoints Estimation with Ultralytics YOLO26 | Human Hand Pose Estimation Tutorial

The dataset includes keypoints for hand detection. The keypoints are annotated as follows:

Each hand has a total of 21 keypoints.

The hand keypoint dataset is split into two subsets:

Hand keypoints can be used for gesture recognition, AR/VR controls, robotic manipulation, and hand movement analysis in healthcare. They can also be applied in animation for motion capture and biometric authentication systems for security. The detailed tracking of finger positions enables precise interaction with virtual objects and touchless control interfaces.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the Hand Keypoints dataset, the hand-keypoints.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/hand-keypoints.yaml.

ultralytics/cfg/datasets/hand-keypoints.yaml

To train a YOLO26n-pose model on the Hand Keypoints dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Hand keypoints dataset contains a diverse set of images with human hands annotated with keypoints. Here are some examples of images from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the Hand Keypoints dataset and the benefits of using mosaicing during the training process.

If you use the hand-keypoints dataset in your research or development work, please acknowledge the following sources:

We would like to thank the following sources for providing the images used in this dataset:

The images were collected and used under the respective licenses provided by each platform and are distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

We would also like to acknowledge the creator of this dataset, Rion Dsilva, for his great contribution to Vision AI research.

To train a YOLO26 model on the Hand Keypoints dataset, you can use either Python or the command line interface (CLI). Here's an example for training a YOLO26n-pose model for 100 epochs with an image size of 640:

For a comprehensive list of available arguments, refer to the model Training page.

The Hand Keypoints dataset is designed for advanced pose estimation tasks and includes several key features:

For more details, you can explore the Hand Keypoints Dataset section.

The Hand Keypoints dataset can be applied in various fields, including:

For more information, refer to the Applications section.

The Hand Keypoints dataset is divided into two subsets:

This structure ensures a comprehensive training and validation process. For more details, see the Dataset Structure section.

The dataset configuration is defined in a YAML file, which includes paths, classes, and other relevant information. The hand-keypoints.yaml file can be found at hand-keypoints.yaml.

To use this YAML file for training, specify it in your training script or CLI command as shown in the training example above. For more details, refer to the Dataset YAML section.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Hand Keypoints dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/pose/hand-keypoints/
# Example usage: yolo train data=hand-keypoints.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── hand-keypoints ← downloads here (369 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: hand-keypoints # dataset root dir
train: images/train # train images (relative to 'path') 18776 images
val: images/val # val images (relative to 'path') 7992 images

# Keypoints
kpt_shape: [21, 3] # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
flip_idx: [0, 1, 2, 4, 3, 10, 11, 12, 13, 14, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19, 20]

# Classes
names:
  0: hand

# Keypoint names per class
kpt_names:
  0:
    - wrist
    - thumb_cmc
    - thumb_mcp
    - thumb_ip
    - thumb_tip
    - index_mcp
    - index_pip
    - index_dip
    - index_tip
    - middle_mcp
    - middle_pip
    - middle_dip
    - middle_tip
    - ring_mcp
    - ring_pip
    - ring_dip
    - ring_tip
    - pinky_mcp
    - pinky_pip
    - pinky_dip
    - pinky_tip

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/hand-keypoints.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="hand-keypoints.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo pose train data=hand-keypoints.yaml model=yolo26n-pose.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="hand-keypoints.yaml", epochs=100, imgsz=640)
```

---

## HomeObjects-3K Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/homeobjects-3k/

**Contents:**
- HomeObjects-3K Dataset
- Dataset Structure
- Object Classes
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- License and Attribution
- FAQ
  - What is the HomeObjects-3K dataset designed for?

The HomeObjects-3K dataset is a curated collection of common household object images, designed for training, testing, and benchmarkingcomputer vision models. Featuring ~3,000 images and 12 distinct object classes, this dataset is ideal for research and applications in indoor scene understanding, smart home devices, robotics, and augmented reality.

Watch: How to Train Ultralytics YOLO26 on HomeObjects-3K Dataset | Detection, Validation & ONNX Export 🚀

The HomeObjects-3K dataset is organized into the following subsets:

Each image is labeled using bounding boxes aligned with the Ultralytics YOLO format. The diversity of indoor lighting, object scale, and orientations makes it robust for real-world deployment scenarios.

The dataset supports 12 everyday object categories, covering furniture, electronics, and decorative items. These classes are chosen to reflect common items encountered in indoor domestic environments and support vision tasks like object detection and object tracking.

HomeObjects-3K classes

HomeObjects-3K enables a wide spectrum of applications in indoor computer vision, spanning both research and real-world product development:

Indoor object detection: Use models like Ultralytics YOLO26 to find and locate common home items like beds, chairs, lamps, and laptops in images. This helps with real-time understanding of indoor scenes.

Scene layout parsing: In robotics and smart home systems, this helps devices understand how rooms are arranged, where objects like doors, windows, and furniture are, so they can navigate safely and interact with their environment properly.

AR applications: Power object recognition features in apps that use augmented reality. For example, detect TVs or wardrobes and show extra information or effects on them.

Education and research: Support learning and academic projects by giving students and researchers a ready-to-use dataset for practicing indoor object detection with real-world examples.

Home inventory and asset tracking: Automatically detect and list home items in photos or videos, useful for managing belongings, organizing spaces, or visualizing furniture in real estate.

The configuration for the HomeObjects-3K dataset is provided through a YAML file. This file outlines essential information such as image paths for train and validation directories, and the list of object classes. You can access the HomeObjects-3K.yaml file directly from the Ultralytics repository at: https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/HomeObjects-3K.yaml

ultralytics/cfg/datasets/HomeObjects-3K.yaml

You can train a YOLO26n model on the HomeObjects-3K dataset for 100 epochs using an image size of 640. The examples below show how to get started. For more training options and detailed settings, check the Training guide.

The dataset features a rich collection of indoor scene images that capture a wide range of household objects in natural home environments. Below are sample visuals from the dataset, each paired with its corresponding annotations to illustrate object positions, scales, and spatial relationships.

HomeObjects-3K is developed and released by the Ultralytics team under the AGPL-3.0 License, supporting open-source research and commercial use with proper attribution.

If you use this dataset in your research, please cite it using the mentioned details:

HomeObjects-3K is crafted for advancing AI understanding of indoor scenes. It focuses on detecting everyday household items—like beds, sofas, TVs, and lamps—making it ideal for applications in smart homes, robotics, augmented reality, and interior monitoring systems. Whether you're training models for real-time edge devices or academic research, this dataset provides a balanced foundation.

The dataset includes 12 of the most commonly encountered household items: bed, sofa, chair, table, lamp, tv, laptop, wardrobe, window, door, potted plant, and photo frame. These objects were chosen to reflect realistic indoor environments and to support multipurpose tasks such as robotic navigation, or scene generation in AR/VR applications.

To train a YOLO model like YOLO26n, you'll just need the HomeObjects-3K.yaml configuration file and the pretrained model weights. Whether you're using Python or the CLI, training can be launched with a single command. You can customize parameters such as epochs, image size, and batch size depending on your target performance and hardware setup.

Absolutely. With clean labeling, and standardized YOLO-compatible annotations, HomeObjects-3K is an excellent entry point for students and hobbyists who want to explore real-world object detection in indoor scenarios. It also scales well for more complex applications in commercial environments.

Refer to the Dataset YAML section. The format is standard YOLO, making it compatible with most object detection pipelines.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# HomeObjects-3K dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/homeobjects-3k/
# Example usage: yolo train data=HomeObjects-3K.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── homeobjects-3K ← downloads here (390 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: homeobjects-3K # dataset root dir
train: images/train # train images (relative to 'path') 2285 images
val: images/val # val images (relative to 'path') 404 images

# Classes
names:
  0: bed
  1: sofa
  2: chair
  3: table
  4: lamp
  5: tv
  6: laptop
  7: wardrobe
  8: window
  9: door
  10: potted plant
  11: photo frame

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/homeobjects-3K.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolo26n.pt")

# Train the model on HomeObjects-3K dataset
model.train(data="HomeObjects-3K.yaml", epochs=100, imgsz=640)
```

Example 3 (unknown):
```unknown
yolo detect train data=HomeObjects-3K.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (css):
```css
@dataset{Jocher_Ultralytics_Datasets_2025,
    author = {Jocher, Glenn and Rizwan, Muhammad},
    license = {AGPL-3.0},
    month = {May},
    title = {Ultralytics Datasets: HomeObjects-3K Detection Dataset},
    url = {https://docs.ultralytics.com/datasets/detect/homeobjects-3k/},
    version = {1.0.0},
    year = {2025}
}
```

---

## ImageNet10 Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/imagenet10/

**Contents:**
- ImageNet10 Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the ImageNet10 dataset and how is it different from the full ImageNet dataset?
  - How can I use the ImageNet10 dataset to test my deep learning model?

The ImageNet10 dataset is a small-scale subset of the ImageNet database, developed by Ultralytics and designed for CI tests, sanity checks, and fast testing of training pipelines. This dataset is composed of the first image in the training set and the first image from the validation set of the first 10 classes in ImageNet. Although significantly smaller, it retains the structure and diversity of the original ImageNet dataset.

The ImageNet10 dataset, like the original ImageNet, is organized using the WordNet hierarchy. Each of the 10 classes in ImageNet10 is described by a synset (a collection of synonymous terms). The images in ImageNet10 are annotated with one or more synsets, providing a compact resource for testing models to recognize various objects and their relationships.

The ImageNet10 dataset is useful for quickly testing and debugging computer vision models and pipelines. Its small size allows for rapid iteration, making it ideal for continuous integration tests and sanity checks. It can also be used for fast preliminary testing of new models or changes to existing models before moving on to full-scale testing with the complete ImageNet dataset.

To test a deep learning model on the ImageNet10 dataset with an image size of 224x224, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The ImageNet10 dataset contains a subset of images from the original ImageNet dataset. These images are chosen to represent the first 10 classes in the dataset, providing a diverse yet compact dataset for quick testing and evaluation.

The example showcases the variety and complexity of the images in the ImageNet10 dataset, highlighting its usefulness for sanity checks and quick testing of computer vision models.

If you use the ImageNet10 dataset in your research or development work, please cite the original ImageNet paper:

We would like to acknowledge the ImageNet team, led by Olga Russakovsky, Jia Deng, and Li Fei-Fei, for creating and maintaining the ImageNet dataset. The ImageNet10 dataset, while a compact subset, is a valuable resource for quick testing and debugging in the machine learning and computer vision research community. For more information about the ImageNet dataset and its creators, visit the ImageNet website.

The ImageNet10 dataset is a compact subset of the original ImageNet database, created by Ultralytics for rapid CI tests, sanity checks, and training pipeline evaluations. ImageNet10 comprises only 20 images, representing the first image in the training and validation sets of the first 10 classes in ImageNet. Despite its small size, it maintains the structure and diversity of the full dataset, making it ideal for quick testing but not for benchmarking models.

To test your deep learning model on the ImageNet10 dataset with an image size of 224x224, use the following code snippets.

Refer to the Training page for a comprehensive list of available arguments.

The ImageNet10 dataset is designed specifically for CI tests, sanity checks, and quick evaluations in deep learning pipelines. Its small size allows for rapid iteration and testing, making it perfect for continuous integration processes where speed is crucial. By maintaining the structural complexity and diversity of the original ImageNet dataset, ImageNet10 provides a reliable indication of a model's basic functionality and correctness without the overhead of processing a large dataset.

The ImageNet10 dataset has several key features:

While both ImageNet10 and ImageNette are subsets of ImageNet, they serve different purposes. ImageNet10 contains just 20 images (2 per class) from the first 10 classes of ImageNet, making it extremely lightweight for CI testing and quick sanity checks. In contrast, ImageNette contains thousands of images across 10 easily distinguishable classes, making it more suitable for actual model training and development. ImageNet10 is designed for verification of pipeline functionality, while ImageNette is better for meaningful but faster-than-full-ImageNet training experiments.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="imagenet10", epochs=5, imgsz=224)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=imagenet10 model=yolo26n-cls.pt epochs=5 imgsz=224
```

Example 3 (python):
```python
@article{ILSVRC15,
         author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
         title={ImageNet Large Scale Visual Recognition Challenge},
         year={2015},
         journal={International Journal of Computer Vision (IJCV)},
         volume={115},
         number={3},
         pages={211-252}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="imagenet10", epochs=5, imgsz=224)
```

---

## ImageNette Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/imagenette/

**Contents:**
- ImageNette Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Sample Images and Annotations
- ImageNette160 and ImageNette320
- Citations and Acknowledgments
- FAQ
  - What is the ImageNette dataset?

The ImageNette dataset is a subset of the larger ImageNet dataset, but it only includes 10 easily distinguishable classes. It was created to provide a quicker, easier-to-use version of ImageNet for software development and education.

The ImageNette dataset is split into two subsets:

The ImageNette dataset is widely used for training and evaluating deep learning models in image classification tasks, such as Convolutional Neural Networks (CNNs), and various other machine learning algorithms. The dataset's straightforward format and well-chosen classes make it a handy resource for both beginner and experienced practitioners in the field of machine learning and computer vision.

To train a model on the ImageNette dataset for 100 epochs with a standard image size of 224x224, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The ImageNette dataset contains colored images of various objects and scenes, providing a diverse dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the images in the ImageNette dataset, highlighting the importance of a diverse dataset for training robust image classification models.

For faster prototyping and training, the ImageNette dataset is also available in two reduced sizes: ImageNette160 and ImageNette320. These datasets maintain the same classes and structure as the full ImageNette dataset, but the images are resized to a smaller dimension. As such, these versions of the dataset are particularly useful for preliminary model testing, or when computational resources are limited.

To use these datasets, simply replace 'imagenette' with 'imagenette160' or 'imagenette320' in the training command. The following code snippets illustrate this:

Train Example with ImageNette160

Train Example with ImageNette320

These smaller versions of the dataset allow for rapid iterations during the development process while still providing valuable and realistic image classification tasks.

If you use the ImageNette dataset in your research or development work, please acknowledge it appropriately. For more information about the ImageNette dataset, visit the ImageNette dataset GitHub page.

The ImageNette dataset is a simplified subset of the larger ImageNet dataset, featuring only 10 easily distinguishable classes such as tench, English springer, and French horn. It was created to offer a more manageable dataset for efficient training and evaluation of image classification models. This dataset is particularly useful for quick software development and educational purposes in machine learning and computer vision.

To train a YOLO model on the ImageNette dataset for 100 epochs, you can use the following commands. Make sure to have the Ultralytics YOLO environment set up.

For more details, see the Training documentation page.

The ImageNette dataset is advantageous for several reasons:

For more details on model training and dataset management, explore the Dataset Structure section.

Yes, the ImageNette dataset is also available in two resized versions: ImageNette160 and ImageNette320. These versions help in faster prototyping and are especially useful when computational resources are limited.

Train Example with ImageNette160

For more information, refer to Training with ImageNette160 and ImageNette320.

The ImageNette dataset is extensively used in:

Explore the Applications section for detailed use cases.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="imagenette", epochs=100, imgsz=224)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=imagenette model=yolo26n-cls.pt epochs=100 imgsz=224
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model with ImageNette160
results = model.train(data="imagenette160", epochs=100, imgsz=160)
```

Example 4 (sql):
```sql
# Start training from a pretrained *.pt model with ImageNette160
yolo classify train data=imagenette160 model=yolo26n-cls.pt epochs=100 imgsz=160
```

---

## ImageNet Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/imagenet/

**Contents:**
- ImageNet Dataset
- ImageNet Pretrained Models
- Key Features
- Dataset Structure
- ImageNet Large Scale Visual Recognition Challenge (ILSVRC)
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ

ImageNet is a large-scale database of annotated images designed for use in visual object recognition research. It contains over 14 million images, with each image annotated using WordNet synsets, making it one of the most extensive resources available for training deep learning models in computer vision tasks.

The ImageNet dataset is organized using the WordNet hierarchy. Each node in the hierarchy represents a category, and each category is described by a synset (a collection of synonymous terms). The images in ImageNet are annotated with one or more synsets, providing a rich resource for training models to recognize various objects and their relationships.

The annual ImageNet Large Scale Visual Recognition Challenge (ILSVRC) has been an important event in the field of computer vision. It has provided a platform for researchers and developers to evaluate their algorithms and models on a large-scale dataset with standardized evaluation metrics. The ILSVRC has led to significant advancements in the development of deep learning models for image classification, object detection, and other computer vision tasks.

The ImageNet dataset is widely used for training and evaluating deep learning models in various computer vision tasks, such as image classification, object detection, and object localization. Some popular deep learning architectures, such as AlexNet, VGG, and ResNet, were developed and benchmarked using the ImageNet dataset.

To train a deep learning model on the ImageNet dataset for 100 epochs with an image size of 224x224, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The ImageNet dataset contains high-resolution images spanning thousands of object categories, providing a diverse and extensive dataset for training and evaluating computer vision models. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the images in the ImageNet dataset, highlighting the importance of a diverse dataset for training robust computer vision models.

If you use the ImageNet dataset in your research or development work, please cite the following paper:

We would like to acknowledge the ImageNet team, led by Olga Russakovsky, Jia Deng, and Li Fei-Fei, for creating and maintaining the ImageNet dataset as a valuable resource for the machine learning and computer vision research community. For more information about the ImageNet dataset and its creators, visit the ImageNet website.

The ImageNet dataset is a large-scale database consisting of over 14 million high-resolution images categorized using WordNet synsets. It is extensively used in visual object recognition research, including image classification and object detection. The dataset's annotations and sheer volume provide a rich resource for training deep learning models. Notably, models like AlexNet, VGG, and ResNet have been trained and benchmarked using ImageNet, showcasing its role in advancing computer vision.

To use a pretrained Ultralytics YOLO model for image classification on the ImageNet dataset, follow these steps:

For more in-depth training instruction, refer to our Training page.

Ultralytics YOLO26 pretrained models offer state-of-the-art performance in terms of speed and accuracy for various computer vision tasks. For example, the YOLO26n-cls model, with a top-1 accuracy of 70.0% and a top-5 accuracy of 89.4%, is optimized for real-time applications. Pretrained models reduce the computational resources required for training from scratch and accelerate development cycles. Learn more about the performance metrics of YOLO26 models in the ImageNet Pretrained Models section.

The ImageNet dataset is organized using the WordNet hierarchy, where each node in the hierarchy represents a category described by a synset (a collection of synonymous terms). This structure allows for detailed annotations, making it ideal for training models to recognize a wide variety of objects. The diversity and annotation richness of ImageNet make it a valuable dataset for developing robust and generalizable deep learning models. More about this organization can be found in the Dataset Structure section.

The annual ImageNet Large Scale Visual Recognition Challenge (ILSVRC) has been pivotal in driving advancements in computer vision by providing a competitive platform for evaluating algorithms on a large-scale, standardized dataset. It offers standardized evaluation metrics, fostering innovation and development in areas such as image classification, object detection, and image segmentation. The challenge has continuously pushed the boundaries of what is possible with deep learning and computer vision technologies.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="imagenet", epochs=100, imgsz=224)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=imagenet model=yolo26n-cls.pt epochs=100 imgsz=224
```

Example 3 (python):
```python
@article{ILSVRC15,
         author = {Olga Russakovsky and Jia Deng and Hao Su and Jonathan Krause and Sanjeev Satheesh and Sean Ma and Zhiheng Huang and Andrej Karpathy and Aditya Khosla and Michael Bernstein and Alexander C. Berg and Li Fei-Fei},
         title={ImageNet Large Scale Visual Recognition Challenge},
         year={2015},
         journal={International Journal of Computer Vision (IJCV)},
         volume={115},
         number={3},
         pages={211-252}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="imagenet", epochs=100, imgsz=224)
```

---

## ImageWoof Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/imagewoof/

**Contents:**
- ImageWoof Dataset
- Key Features
- Dataset Structure
- Applications
- Usage
- Dataset Variants
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the ImageWoof dataset in Ultralytics?

The ImageWoof dataset is a subset of the ImageNet consisting of 10 classes that are challenging to classify, since they're all dog breeds. It was created as a more difficult task for image classification algorithms to solve, aiming at encouraging development of more advanced models.

The ImageWoof dataset structure is based on the dog breed classes, with each breed having its own directory of images. Similar to other classification datasets, it follows a split-directory format with separate folders for training and validation sets.

The ImageWoof dataset is widely used for training and evaluating deep learning models in image classification tasks, especially when it comes to more complex and similar classes. The dataset's challenge lies in the subtle differences between the dog breeds, pushing the limits of model's performance and generalization. It's particularly valuable for:

To train a CNN model on the ImageWoof dataset for 100 epochs with an image size of 224x224, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

ImageWoof dataset comes in three different sizes to accommodate various research needs and computational capabilities:

Full Size (imagewoof): This is the original version of the ImageWoof dataset. It contains full-sized images and is ideal for final training and performance benchmarking.

Medium Size (imagewoof320): This version contains images resized to have a maximum edge length of 320 pixels. It's suitable for faster training without significantly sacrificing model performance.

Small Size (imagewoof160): This version contains images resized to have a maximum edge length of 160 pixels. It's designed for rapid prototyping and experimentation where training speed is a priority.

To use these variants in your training, simply replace 'imagewoof' in the dataset argument with 'imagewoof320' or 'imagewoof160'. For example:

It's important to note that using smaller images will likely yield lower performance in terms of classification accuracy. However, it's an excellent way to iterate quickly in the early stages of model development and prototyping.

The ImageWoof dataset contains colorful images of various dog breeds, providing a challenging dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the subtle differences and similarities among the different dog breeds in the ImageWoof dataset, highlighting the complexity and difficulty of the classification task.

If you use the ImageWoof dataset in your research or development work, please make sure to acknowledge the creators of the dataset by linking to the official dataset repository.

We would like to acknowledge the FastAI team for creating and maintaining the ImageWoof dataset as a valuable resource for the machine learning and computer vision research community. For more information about the ImageWoof dataset, visit the ImageWoof dataset repository.

The ImageWoof dataset is a challenging subset of ImageNet focusing on 10 specific dog breeds. Created to push the limits of image classification models, it features breeds like Beagle, Shih-Tzu, and Golden Retriever. The dataset includes images at various resolutions (full size, 320px, 160px) and even noisy labels for more realistic training scenarios. This complexity makes ImageWoof ideal for developing more advanced deep learning models.

To train a Convolutional Neural Network (CNN) model on the ImageWoof dataset using Ultralytics YOLO for 100 epochs at an image size of 224x224, you can use the following code:

For more details on available training arguments, refer to the Training page.

The ImageWoof dataset comes in three sizes:

Use these versions by replacing 'imagewoof' in the dataset argument accordingly. Note, however, that smaller images may yield lower classification accuracy but can be useful for quicker iterations.

Noisy labels in the ImageWoof dataset simulate real-world conditions where labels might not always be accurate. Training models with this data helps develop robustness and generalization in image classification tasks. This prepares the models to handle ambiguous or mislabeled data effectively, which is often encountered in practical applications.

The primary challenge of the ImageWoof dataset lies in the subtle differences among the dog breeds it includes. Since it focuses on 10 closely related breeds, distinguishing between them requires more advanced and fine-tuned image classification models. This makes ImageWoof an excellent benchmark to test the capabilities and improvements of deep learning models.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="imagewoof", epochs=100, imgsz=224)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=imagewoof model=yolo26n-cls.pt epochs=100 imgsz=224
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# For medium-sized dataset
model.train(data="imagewoof320", epochs=100, imgsz=224)

# For small-sized dataset
model.train(data="imagewoof160", epochs=100, imgsz=224)
```

Example 4 (markdown):
```markdown
# Load a pretrained model and train on the medium-sized dataset
yolo classify train model=yolo26n-cls.pt data=imagewoof320 epochs=100 imgsz=224
```

---

## Image Classification Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/classify/

**Contents:**
- Image Classification Datasets Overview
- Dataset Structure for YOLO Classification Tasks
  - Folder Structure Example
- Usage
- Supported Datasets
  - Adding your own dataset
- FAQ
  - How do I structure my dataset for YOLO classification tasks?
  - What datasets are supported by Ultralytics YOLO for image classification?
  - How do I add my own dataset for YOLO image classification?

For Ultralytics YOLO classification tasks, the dataset must be organized in a specific split-directory structure under the root directory to facilitate proper training, testing, and optional validation processes. This structure includes separate directories for training (train) and testing (test) phases, with an optional directory for validation (val).

Each of these directories should contain one subdirectory for each class in the dataset. The subdirectories are named after the corresponding class and contain all the images for that class. Ensure that each image file is named uniquely and stored in a common format such as JPEG or PNG.

Consider the CIFAR-10 dataset as an example. The folder structure should look like this:

This structured approach ensures that the model can effectively learn from well-organized classes during the training phase and accurately evaluate performance during testing and validation phases.

Most built-in dataset names (for example cifar10, imagenette, or mnist160) will automatically download and cache the data the first time you reference them. Point data to a folder path only when you have curated a custom dataset.

Ultralytics supports the following datasets with automatic download:

If you have your own dataset and would like to use it for training classification models with Ultralytics YOLO, ensure that it follows the format specified above under "Dataset Structure" and then point your data argument to the dataset directory when initializing your training script.

To structure your dataset for Ultralytics YOLO classification tasks, you should follow a specific split-directory format. Organize your dataset into separate directories for train, test, and optionally val. Each of these directories should contain subdirectories named after each class, with the corresponding images inside. This facilitates smooth training and evaluation processes. For an example, consider the CIFAR-10 dataset format:

For more details, visit the Dataset Structure for YOLO Classification Tasks section.

Ultralytics YOLO supports automatic downloading of several datasets for image classification, including Caltech 101, Caltech 256, CIFAR-10, CIFAR-100, Fashion-MNIST, ImageNet, ImageNet-10, Imagenette, Imagewoof, and MNIST. These datasets are structured in a way that makes them easy to use with YOLO. Each dataset's page provides further details about its structure and applications.

To use your own dataset with Ultralytics YOLO, ensure it follows the specified directory format required for the classification task, with separate train, test, and optionally val directories, and subdirectories for each class containing the respective images. Once your dataset is structured correctly, point the data argument to your dataset's root directory when initializing the training script. Here's an example in Python:

More details can be found in the Adding your own dataset section.

Ultralytics YOLO offers several benefits for image classification, including:

For additional insights and real-world applications, you can explore Ultralytics YOLO.

Training a model using Ultralytics YOLO can be done easily in both Python and CLI. Here's an example:

These examples demonstrate the straightforward process of training a YOLO model using either approach. For more information, visit the Usage section and the Train page for classification tasks.

**Examples:**

Example 1 (unknown):
```unknown
cifar-10-/
|
|-- train/
|   |-- airplane/
|   |   |-- 10008_airplane.png
|   |   |-- 10009_airplane.png
|   |   |-- ...
|   |
|   |-- automobile/
|   |   |-- 1000_automobile.png
|   |   |-- 1001_automobile.png
|   |   |-- ...
|   |
|   |-- bird/
|   |   |-- 10014_bird.png
|   |   |-- 10015_bird.png
|   |   |-- ...
|   |
|   |-- ...
|
|-- test/
|   |-- airplane/
|   |   |-- 10_airplane.png
|   |   |-- 11_airplane.png
|   |   |-- ...
|   |
|   |-- automobile/
|   |   |-- 100_automobile.png
|   |   |-- 101_automobile.png
|   |   |-- ...
|   |
|   |-- bird/
|   |   |-- 1000_bird.png
|   |   |-- 1001_bird.png
|   |   |-- ...
|   |
|   |-- ...
|
|-- val/ (optional)
|   |-- airplane/
|   |   |-- 105_airplane.png
|   |   |-- 106_airplane.png
|   |   |-- ...
|   |
|   |-- automobile/
|   |   |-- 102_automobile.png
|   |   |-- 103_automobile.png
|   |   |-- ...
|   |
|   |-- bird/
|   |   |-- 1045_bird.png
|   |   |-- 1046_bird.png
|   |   |-- ...
|   |
|   |-- ...
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="path/to/dataset", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=path/to/data model=yolo26n-cls.pt epochs=100 imgsz=640
```

Example 4 (unknown):
```unknown
cifar-10-/
|-- train/
|   |-- airplane/
|   |-- automobile/
|   |-- bird/
|   ...
|-- test/
|   |-- airplane/
|   |-- automobile/
|   |-- bird/
|   ...
|-- val/ (optional)
|   |-- airplane/
|   |-- automobile/
|   |-- bird/
|   ...
```

---

## Instance Segmentation Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/segment/

**Contents:**
- Instance Segmentation Datasets Overview
- Supported Dataset Formats
  - Ultralytics YOLO format
  - Dataset YAML format
- Usage
- Supported Datasets
  - Adding your own dataset
- Port or Convert Label Formats
  - COCO Dataset Format to YOLO Format
- Auto-Annotation

Instance segmentation is a computer vision task that involves identifying and delineating individual objects within an image. This guide provides an overview of dataset formats supported by Ultralytics YOLO for instance segmentation tasks, along with instructions on how to prepare, convert, and use these datasets for training your models.

The dataset label format used for training YOLO segmentation models is as follows:

The format for a single row in the segmentation dataset file is as follows:

In this format, <class-index> is the index of the class for the object, and <x1> <y1> <x2> <y2> ... <xn> <yn> are the normalized polygon coordinates of the object's segmentation mask (values are in [0, 1] relative to image width and height). The coordinates are separated by spaces.

Here is an example of the YOLO dataset format for a single image with two objects made up of a 3-point segment and a 5-point segment.

The Ultralytics framework uses a YAML file format to define the dataset and model configuration for training Segmentation Models. Here is an example of the YAML format used for defining a segmentation dataset:

ultralytics/cfg/datasets/coco8-seg.yaml

The train and val fields specify the paths to the directories containing the training and validation images, respectively.

names is a dictionary of class names. The order of the names should match the order of the object class indices in the YOLO dataset files.

Ultralytics YOLO supports various datasets for instance segmentation tasks. Here's a list of the most commonly used ones:

If you have your own dataset and would like to use it for training segmentation models with Ultralytics YOLO format, ensure that it follows the format specified above under "Ultralytics YOLO format". Convert your annotations to the required format and specify the paths, number of classes, and class names in the YAML configuration file. Keep images/ and labels/ as separate folders at the same level, with matching subfolder structure; placing label .txt files in the image folder can cause the model to miss labels.

You can easily convert labels from the popular COCO dataset format to the YOLO format using the following code snippet:

This conversion tool can be used to convert the COCO dataset or any dataset in the COCO format to the Ultralytics YOLO format.

Remember to double-check if the dataset you want to use is compatible with your model and follows the necessary format conventions. Properly formatted datasets are crucial for training successful segmentation models.

Auto-annotation is an essential feature that allows you to generate a segmentation dataset using a pretrained detection model. It enables you to quickly and accurately annotate a large number of images without the need for manual labeling, saving time and effort.

To auto-annotate your dataset using the Ultralytics framework, you can use the auto_annotate function as shown below:

The auto_annotate function takes the path to your images, along with optional arguments for specifying the pretrained detection models i.e. YOLO26, YOLO11 or other models and segmentation models i.e, SAM, SAM2 or MobileSAM, the device to run the models on, and the output directory for saving the annotated results.

By leveraging the power of pretrained models, auto-annotation can significantly reduce the time and effort required for creating high-quality segmentation datasets. This feature is particularly useful for researchers and developers working with large image collections, as it allows them to focus on model development and evaluation rather than manual annotation.

Before training your model, it's often helpful to visualize your dataset annotations to ensure they're correct. Ultralytics provides a utility function for this purpose:

This function draws bounding boxes, labels objects with class names, and adjusts text color for better readability, helping you identify and correct any annotation errors before training.

If you have segmentation masks in binary format, you can convert them to the YOLO segmentation format using:

This utility converts binary mask images into the YOLO segmentation format and saves them in the specified output directory.

Ultralytics YOLO supports several dataset formats for instance segmentation, with the primary format being its own Ultralytics YOLO format. Each image in your dataset needs a corresponding text file with object information segmented into multiple rows (one row per object), listing the class index and normalized bounding coordinates. For more detailed instructions on the YOLO dataset format, visit the Instance Segmentation Datasets Overview.

Converting COCO format annotations to YOLO format is straightforward using Ultralytics tools. You can use the convert_coco function from the ultralytics.data.converter module:

This script converts your COCO dataset annotations to the required YOLO format, making it suitable for training your YOLO models. For more details, refer to Port or Convert Label Formats.

To prepare a YAML file for training YOLO models with Ultralytics, you need to define the dataset paths and class names. Here's an example YAML configuration:

Ensure you update the paths and class names according to your dataset. For more information, check the Dataset YAML Format section.

Auto-annotation in Ultralytics YOLO allows you to generate segmentation annotations for your dataset using a pretrained detection model. This significantly reduces the need for manual labeling. You can use the auto_annotate function as follows:

This function automates the annotation process, making it faster and more efficient. For more details, explore the Auto-Annotate Reference.

**Examples:**

Example 1 (typescript):
```typescript
<class-index> <x1> <y1> <x2> <y2> ... <xn> <yn>
```

Example 2 (unknown):
```unknown
0 0.681 0.485 0.670 0.487 0.676 0.487
1 0.504 0.000 0.501 0.004 0.498 0.004 0.493 0.010 0.492 0.0104
```

Example 3 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8-seg dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/segment/coco8-seg/
# Example usage: yolo train data=coco8-seg.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8-seg ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8-seg # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8-seg.zip
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco8-seg.yaml", epochs=100, imgsz=640)
```

---

## KITTI Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/kitti/

**Contents:**
- KITTI Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQs
  - What is the kitti dataset used for?
  - How many images are included in the kitti dataset?

The kitti dataset is one of the most influential benchmark datasets for autonomous driving and computer vision. Released by the Karlsruhe Institute of Technology and Toyota Technological Institute at Chicago, it contains stereo camera, LiDAR, and GPS/IMU data collected from real-world driving scenarios.

Watch: How to Train Ultralytics YOLO26 on the KITTI Dataset 🚀

It is widely used for evaluating algorithms in object detection, depth estimation, optical flow, and visual odometry. The dataset is fully compatible with Ultralytics YOLO26 for 2D object detection tasks and can be easily integrated into the Ultralytics platform for training and evaluation.

Kitti original test set is excluded here since it does not contain ground-truth annotations.

In total, the dataset includes 7,481 images, each paired with detailed annotations for objects such as cars, pedestrians, cyclists, and other road elements. The dataset is divided into two main subsets:

Kitti dataset enables advancements in autonomous driving and robotics, supporting tasks like:

Ultralytics defines the kitti dataset configuration using a YAML file. This file specifies dataset paths, class labels, and metadata required for training. The configuration file is available at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/kitti.yaml.

ultralytics/cfg/datasets/kitti.yaml

To train a YOLO26n model on the kitti dataset for 100 epochs with an image size of 640, use the following commands. For more details, refer to the Training page.

You can also perform evaluation, inference, and export tasks directly from the command line or Python API using the same configuration file.

The kitti dataset provides diverse driving scenarios. Each image includes bounding box annotations for 2D object detection tasks. The example showcase the dataset rich variety, enabling robust model generalization across diverse real-world conditions.

If you use the kitti dataset in your research, please cite the following paper:

We acknowledge the KITTI Vision Benchmark Suite for providing this comprehensive dataset that continues to shape progress in computer vision, robotics, and autonomous systems. Visit the kitti website for more information.

The kitti dataset is primarily used for computer vision research in autonomous driving, supporting tasks like object detection, depth estimation, optical flow, and 3D localization.

The dataset includes 5,985 labeled training images and 1,496 validation images captured across urban, rural, and highway scenes. The original test set is excluded here since it does not contain ground-truth annotations.

kitti includes annotations for objects such as cars, pedestrians, cyclists, trucks, trams, and miscellaneous road users.

Yes, kitti is fully compatible with Ultralytics YOLO26. You can train and validate, models directly using the provided YAML configuration file.

You can access the YAML file at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/kitti.yaml.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# KITTI dataset by Karlsruhe Institute of Technology and Toyota Technological Institute at Chicago
# Documentation: https://docs.ultralytics.com/datasets/detect/kitti/
# Example usage: yolo train data=kitti.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── kitti ← downloads here (390.5 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: kitti # dataset root dir
train: images/train # train images (relative to 'path') 5985 images
val: images/val # val images (relative to 'path') 1496 images

names:
  0: car
  1: van
  2: truck
  3: pedestrian
  4: person_sitting
  5: cyclist
  6: tram
  7: misc

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/kitti.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLO26 model
model = YOLO("yolo26n.pt")

# Train on kitti dataset
results = model.train(data="kitti.yaml", epochs=100, imgsz=640)
```

Example 3 (unknown):
```unknown
yolo detect train data=kitti.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@article{Geiger2013IJRR,
  author = {Andreas Geiger and Philip Lenz and Christoph Stiller and Raquel Urtasun},
  title = {Vision meets Robotics: The KITTI Dataset},
  journal = {International Journal of Robotics Research (IJRR)},
  year = {2013}
}
```

---

## LVIS Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/lvis/

**Contents:**
- LVIS Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the LVIS dataset, and how is it used in computer vision?

The LVIS dataset is a large-scale, fine-grained vocabulary-level annotation dataset developed and released by Facebook AI Research (FAIR). It is primarily used as a research benchmark for object detection and instance segmentation with a large vocabulary of categories, aiming to drive further advancements in computer vision field.

Watch: YOLO World training workflow with LVIS dataset

The LVIS dataset is split into three subsets:

The LVIS dataset is widely used for training and evaluating deep learning models in object detection (such as YOLO, Faster R-CNN, and SSD), instance segmentation (such as Mask R-CNN). The dataset's diverse set of object categories, large number of annotated images, and standardized evaluation metrics make it an essential resource for computer vision researchers and practitioners.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the LVIS dataset, the lvis.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/lvis.yaml.

ultralytics/cfg/datasets/lvis.yaml

To train a YOLO26n model on the LVIS dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The LVIS dataset contains a diverse set of images with various object categories and complex scenes. Here are some examples of images from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the LVIS dataset and the benefits of using mosaicing during the training process.

If you use the LVIS dataset in your research or development work, please cite the following paper:

We would like to acknowledge the LVIS Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the LVIS dataset and its creators, visit the LVIS dataset website.

The LVIS dataset is a large-scale dataset with fine-grained vocabulary-level annotations developed by Facebook AI Research (FAIR). It is primarily used for object detection and instance segmentation, featuring over 1203 object categories and 2 million instance annotations. Researchers and practitioners use it to train and benchmark models like Ultralytics YOLO for advanced computer vision tasks. The dataset's extensive size and diversity make it an essential resource for pushing the boundaries of model performance in detection and segmentation.

To train a YOLO26n model on the LVIS dataset for 100 epochs with an image size of 640, follow the example below. This process utilizes Ultralytics' framework, which offers comprehensive training features.

For detailed training configurations, refer to the Training documentation.

The images in the LVIS dataset are the same as those in the COCO dataset, but the two differ in terms of splitting and annotations. LVIS provides a larger and more detailed vocabulary with 1203 object categories compared to COCO's 80 categories. Additionally, LVIS focuses on annotation completeness and diversity, aiming to push the limits of object detection and instance segmentation models by offering more nuanced and comprehensive data.

Ultralytics YOLO models, including the latest YOLO26, are optimized for real-time object detection with state-of-the-art accuracy and speed. They support a wide range of annotations, such as the fine-grained ones provided by the LVIS dataset, making them ideal for advanced computer vision applications. Moreover, Ultralytics offers seamless integration with various training, validation, and prediction modes, ensuring efficient model development and deployment.

Yes, the LVIS dataset includes a variety of images with diverse object categories and complex scenes. Here is an example of a sample image along with its annotations:

This mosaiced image demonstrates a training batch composed of multiple dataset images combined into one. Mosaicing increases the variety of objects and scenes within each training batch, enhancing the model's ability to generalize across different contexts. For more details on the LVIS dataset, explore the LVIS dataset documentation.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# LVIS dataset http://www.lvisdataset.org by Facebook AI Research.
# Documentation: https://docs.ultralytics.com/datasets/detect/lvis/
# Example usage: yolo train data=lvis.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── lvis ← downloads here (20.1 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: lvis # dataset root dir
train: train.txt # train images (relative to 'path') 100170 images
val: val.txt # val images (relative to 'path') 19809 images
minival: minival.txt # minival images (relative to 'path') 5000 images

names:
  0: aerosol can/spray can
  1: air conditioner
  2: airplane/aeroplane
  3: alarm clock
  4: alcohol/alcoholic beverage
  5: alligator/gator
  6: almond
  7: ambulance
  8: amplifier
  9: anklet/ankle bracelet
  10: antenna/aerial/transmitting aerial
  11: apple
  12: applesauce
  13: apricot
  14: apron
  15: aquarium/fish tank
  16: arctic/arctic type of shoe/galosh/golosh/rubber/rubber type of shoe/gumshoe
  17: armband
  18: armchair
  19: armoire
  20: armor
  21: artichoke
  22: trash can/garbage can/wastebin/dustbin/trash barrel/trash bin
  23: ashtray
  24: asparagus
  25: atomizer/atomiser/spray/sprayer/nebulizer/nebuliser
  26: avocado
  27: award/accolade
  28: awning
  29: ax/axe
  30: baboon
  31: baby buggy/baby carriage/perambulator/pram/stroller
  32: basketball backboard
  33: backpack/knapsack/packsack/rucksack/haversack
  34: handbag/purse/pocketbook
  35: suitcase/baggage/luggage
  36: bagel/beigel
  37: bagpipe
  38: baguet/baguette
  39: bait/lure
  40: ball
  41: ballet skirt/tutu
  42: balloon
  43: bamboo
  44: banana
  45: Band Aid
  46: bandage
  47: bandanna/bandana
  48: banjo
  49: banner/streamer
  50: barbell
  51: barge
  52: barrel/cask
  53: barrette
  54: barrow/garden cart/lawn cart/wheelbarrow
  55: baseball base
  56: baseball
  57: baseball bat
  58: baseball cap/jockey cap/golf cap
  59: baseball glove/baseball mitt
  60: basket/handbasket
  61: basketball
  62: bass horn/sousaphone/tuba
  63: bat/bat animal
  64: bath mat
  65: bath towel
  66: bathrobe
  67: bathtub/bathing tub
  68: batter/batter food
  69: battery
  70: beachball
  71: bead
  72: bean curd/tofu
  73: beanbag
  74: beanie/beany
  75: bear
  76: bed
  77: bedpan
  78: bedspread/bedcover/bed covering/counterpane/spread
  79: cow
  80: beef/beef food/boeuf/boeuf food
  81: beeper/pager
  82: beer bottle
  83: beer can
  84: beetle
  85: bell
  86: bell pepper/capsicum
  87: belt
  88: belt buckle
  89: bench
  90: beret
  91: bib
  92: Bible
  93: bicycle/bike/bike bicycle
  94: visor/vizor
  95: billboard
  96: binder/ring-binder
  97: binoculars/field glasses/opera glasses
  98: bird
  99: birdfeeder
  100: birdbath
  101: birdcage
  102: birdhouse
  103: birthday cake
  104: birthday card
  105: pirate flag
  106: black sheep
  107: blackberry
  108: blackboard/chalkboard
  109: blanket
  110: blazer/sport jacket/sport coat/sports jacket/sports coat
  111: blender/liquidizer/liquidiser
  112: blimp
  113: blinker/flasher
  114: blouse
  115: blueberry
  116: gameboard
  117: boat/ship/ship boat
  118: bob/bobber/bobfloat
  119: bobbin/spool/reel
  120: bobby pin/hairgrip
  121: boiled egg/coddled egg
  122: bolo tie/bolo/bola tie/bola
  123: deadbolt
  124: bolt
  125: bonnet
  126: book
  127: bookcase
  128: booklet/brochure/leaflet/pamphlet
  129: bookmark/bookmarker
  130: boom microphone/microphone boom
  131: boot
  132: bottle
  133: bottle opener
  134: bouquet
  135: bow/bow weapon
  136: bow/bow decorative ribbons
  137: bow-tie/bowtie
  138: bowl
  139: pipe bowl
  140: bowler hat/bowler/derby hat/derby/plug hat
  141: bowling ball
  142: box
  143: boxing glove
  144: suspenders
  145: bracelet/bangle
  146: brass plaque
  147: brassiere/bra/bandeau
  148: bread-bin/breadbox
  149: bread
  150: breechcloth/breechclout/loincloth
  151: bridal gown/wedding gown/wedding dress
  152: briefcase
  153: broccoli
  154: broach
  155: broom
  156: brownie
  157: brussels sprouts
  158: bubble gum
  159: bucket/pail
  160: horse buggy
  161: horned cow
  162: bulldog
  163: bulldozer/dozer
  164: bullet train
  165: bulletin board/notice board
  166: bulletproof vest
  167: bullhorn/megaphone
  168: bun/roll
  169: bunk bed
  170: buoy
  171: burrito
  172: bus/bus vehicle/autobus/charabanc/double-decker/motorbus/motorcoach
  173: business card
  174: butter
  175: butterfly
  176: button
  177: cab/cab taxi/taxi/taxicab
  178: cabana
  179: cabin car/caboose
  180: cabinet
  181: locker/storage locker
  182: cake
  183: calculator
  184: calendar
  185: calf
  186: camcorder
  187: camel
  188: camera
  189: camera lens
  190: camper/camper vehicle/camping bus/motor home
  191: can/tin can
  192: can opener/tin opener
  193: candle/candlestick
  194: candle holder
  195: candy bar
  196: candy cane
  197: walking cane
  198: canister/canister
  199: canoe
  200: cantaloup/cantaloupe
  201: canteen
  202: cap/cap headwear
  203: bottle cap/cap/cap container lid
  204: cape
  205: cappuccino/coffee cappuccino
  206: car/car automobile/auto/auto automobile/automobile
  207: railcar/railcar part of a train/railway car/railway car part of a train/railroad car/railroad car part of a train
  208: elevator car
  209: car battery/automobile battery
  210: identity card
  211: card
  212: cardigan
  213: cargo ship/cargo vessel
  214: carnation
  215: horse carriage
  216: carrot
  217: tote bag
  218: cart
  219: carton
  220: cash register/register/register for cash transactions
  221: casserole
  222: cassette
  223: cast/plaster cast/plaster bandage
  224: cat
  225: cauliflower
  226: cayenne/cayenne spice/cayenne pepper/cayenne pepper spice/red pepper/red pepper spice
  227: CD player
  228: celery
  229: cellular telephone/cellular phone/cellphone/mobile phone/smart phone
  230: chain mail/ring mail/chain armor/ring armor
  231: chair
  232: chaise longue/chaise/daybed
  233: chalice
  234: chandelier
  235: chap
  236: checkbook/chequebook
  237: checkerboard
  238: cherry
  239: chessboard
  240: chicken/chicken animal
  241: chickpea/garbanzo
  242: chili/chili vegetable/chili pepper/chili pepper vegetable/chilli/chilli vegetable/chilly/chilly vegetable/chile/chile vegetable
  243: chime/gong
  244: chinaware
  245: crisp/crisp potato chip/potato chip
  246: poker chip
  247: chocolate bar
  248: chocolate cake
  249: chocolate milk
  250: chocolate mousse
  251: choker/collar/neckband
  252: chopping board/cutting board/chopping block
  253: chopstick
  254: Christmas tree
  255: slide
  256: cider/cyder
  257: cigar box
  258: cigarette
  259: cigarette case/cigarette pack
  260: cistern/water tank
  261: clarinet
  262: clasp
  263: cleansing agent/cleanser/cleaner
  264: cleat/cleat for securing rope
  265: clementine
  266: clip
  267: clipboard
  268: clippers/clippers for plants
  269: cloak
  270: clock/timepiece/timekeeper
  271: clock tower
  272: clothes hamper/laundry basket/clothes basket
  273: clothespin/clothes peg
  274: clutch bag
  275: coaster
  276: coat
  277: coat hanger/clothes hanger/dress hanger
  278: coatrack/hatrack
  279: cock/rooster
  280: cockroach
  281: cocoa/cocoa beverage/hot chocolate/hot chocolate beverage/drinking chocolate
  282: coconut/cocoanut
  283: coffee maker/coffee machine
  284: coffee table/cocktail table
  285: coffeepot
  286: coil
  287: coin
  288: colander/cullender
  289: coleslaw/slaw
  290: coloring material
  291: combination lock
  292: pacifier/teething ring
  293: comic book
  294: compass
  295: computer keyboard/keyboard/keyboard computer
  296: condiment
  297: cone/traffic cone
  298: control/controller
  299: convertible/convertible automobile
  300: sofa bed
  301: cooker
  302: cookie/cooky/biscuit/biscuit cookie
  303: cooking utensil
  304: cooler/cooler for food/ice chest
  305: cork/cork bottle plug/bottle cork
  306: corkboard
  307: corkscrew/bottle screw
  308: edible corn/corn/maize
  309: cornbread
  310: cornet/horn/trumpet
  311: cornice/valance/valance board/pelmet
  312: cornmeal
  313: corset/girdle
  314: costume
  315: cougar/puma/catamount/mountain lion/panther
  316: coverall
  317: cowbell
  318: cowboy hat/ten-gallon hat
  319: crab/crab animal
  320: crabmeat
  321: cracker
  322: crape/crepe/French pancake
  323: crate
  324: crayon/wax crayon
  325: cream pitcher
  326: crescent roll/croissant
  327: crib/cot
  328: crock pot/earthenware jar
  329: crossbar
  330: crouton
  331: crow
  332: crowbar/wrecking bar/pry bar
  333: crown
  334: crucifix
  335: cruise ship/cruise liner
  336: police cruiser/patrol car/police car/squad car
  337: crumb
  338: crutch
  339: cub/cub animal
  340: cube/square block
  341: cucumber/cuke
  342: cufflink
  343: cup
  344: trophy cup
  345: cupboard/closet
  346: cupcake
  347: hair curler/hair roller/hair crimper
  348: curling iron
  349: curtain/drapery
  350: cushion
  351: cylinder
  352: cymbal
  353: dagger
  354: dalmatian
  355: dartboard
  356: date/date fruit
  357: deck chair/beach chair
  358: deer/cervid
  359: dental floss/floss
  360: desk
  361: detergent
  362: diaper
  363: diary/journal
  364: die/dice
  365: dinghy/dory/rowboat
  366: dining table
  367: tux/tuxedo
  368: dish
  369: dish antenna
  370: dishrag/dishcloth
  371: dishtowel/tea towel
  372: dishwasher/dishwashing machine
  373: dishwasher detergent/dishwashing detergent/dishwashing liquid/dishsoap
  374: dispenser
  375: diving board
  376: Dixie cup/paper cup
  377: dog
  378: dog collar
  379: doll
  380: dollar/dollar bill/one dollar bill
  381: dollhouse/doll's house
  382: dolphin
  383: domestic ass/donkey
  384: doorknob/doorhandle
  385: doormat/welcome mat
  386: donut
  387: dove
  388: dragonfly
  389: drawer
  390: underdrawers/boxers/boxershorts
  391: dress/frock
  392: dress hat/high hat/opera hat/silk hat/top hat
  393: dress suit
  394: dresser
  395: drill
  396: drone
  397: dropper/eye dropper
  398: drum/drum musical instrument
  399: drumstick
  400: duck
  401: duckling
  402: duct tape
  403: duffel bag/duffle bag/duffel/duffle
  404: dumbbell
  405: dumpster
  406: dustpan
  407: eagle
  408: earphone/earpiece/headphone
  409: earplug
  410: earring
  411: easel
  412: eclair
  413: eel
  414: egg/eggs
  415: egg roll/spring roll
  416: egg yolk/yolk/yolk egg
  417: eggbeater/eggwhisk
  418: eggplant/aubergine
  419: electric chair
  420: refrigerator
  421: elephant
  422: elk/moose
  423: envelope
  424: eraser
  425: escargot
  426: eyepatch
  427: falcon
  428: fan
  429: faucet/spigot/tap
  430: fedora
  431: ferret
  432: Ferris wheel
  433: ferry/ferryboat
  434: fig/fig fruit
  435: fighter jet/fighter aircraft/attack aircraft
  436: figurine
  437: file cabinet/filing cabinet
  438: file/file tool
  439: fire alarm/smoke alarm
  440: fire engine/fire truck
  441: fire extinguisher/extinguisher
  442: fire hose
  443: fireplace
  444: fireplug/fire hydrant/hydrant
  445: first-aid kit
  446: fish
  447: fish/fish food
  448: fishbowl/goldfish bowl
  449: fishing rod/fishing pole
  450: flag
  451: flagpole/flagstaff
  452: flamingo
  453: flannel
  454: flap
  455: flash/flashbulb
  456: flashlight/torch
  457: fleece
  458: flip-flop/flip-flop sandal
  459: flipper/flipper footwear/fin/fin footwear
  460: flower arrangement/floral arrangement
  461: flute glass/champagne flute
  462: foal
  463: folding chair
  464: food processor
  465: football/football American
  466: football helmet
  467: footstool/footrest
  468: fork
  469: forklift
  470: freight car
  471: French toast
  472: freshener/air freshener
  473: frisbee
  474: frog/toad/toad frog
  475: fruit juice
  476: frying pan/frypan/skillet
  477: fudge
  478: funnel
  479: futon
  480: gag/muzzle
  481: garbage
  482: garbage truck
  483: garden hose
  484: gargle/mouthwash
  485: gargoyle
  486: garlic/ail
  487: gasmask/respirator/gas helmet
  488: gazelle
  489: gelatin/jelly
  490: gemstone
  491: generator
  492: giant panda/panda/panda bear
  493: gift wrap
  494: ginger/gingerroot
  495: giraffe
  496: cincture/sash/waistband/waistcloth
  497: glass/glass drink container/drinking glass
  498: globe
  499: glove
  500: goat
  501: goggles
  502: goldfish
  503: golf club/golf-club
  504: golfcart
  505: gondola/gondola boat
  506: goose
  507: gorilla
  508: gourd
  509: grape
  510: grater
  511: gravestone/headstone/tombstone
  512: gravy boat/gravy holder
  513: green bean
  514: green onion/spring onion/scallion
  515: griddle
  516: grill/grille/grillwork/radiator grille
  517: grits/hominy grits
  518: grizzly/grizzly bear
  519: grocery bag
  520: guitar
  521: gull/seagull
  522: gun
  523: hairbrush
  524: hairnet
  525: hairpin
  526: halter top
  527: ham/jambon/gammon
  528: hamburger/beefburger/burger
  529: hammer
  530: hammock
  531: hamper
  532: hamster
  533: hair dryer
  534: hand glass/hand mirror
  535: hand towel/face towel
  536: handcart/pushcart/hand truck
  537: handcuff
  538: handkerchief
  539: handle/grip/handgrip
  540: handsaw/carpenter's saw
  541: hardback book/hardcover book
  542: harmonium/organ/organ musical instrument/reed organ/reed organ musical instrument
  543: hat
  544: hatbox
  545: veil
  546: headband
  547: headboard
  548: headlight/headlamp
  549: headscarf
  550: headset
  551: headstall/headstall for horses/headpiece/headpiece for horses
  552: heart
  553: heater/warmer
  554: helicopter
  555: helmet
  556: heron
  557: highchair/feeding chair
  558: hinge
  559: hippopotamus
  560: hockey stick
  561: hog/pig
  562: home plate/home plate baseball/home base/home base baseball
  563: honey
  564: fume hood/exhaust hood
  565: hook
  566: hookah/narghile/nargileh/sheesha/shisha/water pipe
  567: hornet
  568: horse
  569: hose/hosepipe
  570: hot-air balloon
  571: hotplate
  572: hot sauce
  573: hourglass
  574: houseboat
  575: hummingbird
  576: hummus/humus/hommos/hoummos/humous
  577: polar bear
  578: icecream
  579: popsicle
  580: ice maker
  581: ice pack/ice bag
  582: ice skate
  583: igniter/ignitor/lighter
  584: inhaler/inhalator
  585: iPod
  586: iron/iron for clothing/smoothing iron/smoothing iron for clothing
  587: ironing board
  588: jacket
  589: jam
  590: jar
  591: jean/blue jean/denim
  592: jeep/landrover
  593: jelly bean/jelly egg
  594: jersey/T-shirt/tee shirt
  595: jet plane/jet-propelled plane
  596: jewel/gem/precious stone
  597: jewelry/jewellery
  598: joystick
  599: jumpsuit
  600: kayak
  601: keg
  602: kennel/doghouse
  603: kettle/boiler
  604: key
  605: keycard
  606: kilt
  607: kimono
  608: kitchen sink
  609: kitchen table
  610: kite
  611: kitten/kitty
  612: kiwi fruit
  613: knee pad
  614: knife
  615: knitting needle
  616: knob
  617: knocker/knocker on a door/doorknocker
  618: koala/koala bear
  619: lab coat/laboratory coat
  620: ladder
  621: ladle
  622: ladybug/ladybeetle/ladybird beetle
  623: lamb/lamb animal
  624: lamb-chop/lambchop
  625: lamp
  626: lamppost
  627: lampshade
  628: lantern
  629: lanyard/laniard
  630: laptop computer/notebook computer
  631: lasagna/lasagne
  632: latch
  633: lawn mower
  634: leather
  635: legging/legging clothing/leging/leging clothing/leg covering
  636: Lego/Lego set
  637: legume
  638: lemon
  639: lemonade
  640: lettuce
  641: license plate/numberplate
  642: life buoy/lifesaver/life belt/life ring
  643: life jacket/life vest
  644: lightbulb
  645: lightning rod/lightning conductor
  646: lime
  647: limousine
  648: lion
  649: lip balm
  650: liquor/spirits/hard liquor/liqueur/cordial
  651: lizard
  652: log
  653: lollipop
  654: speaker/speaker stereo equipment
  655: loveseat
  656: machine gun
  657: magazine
  658: magnet
  659: mail slot
  660: mailbox/mailbox at home/letter box/letter box at home
  661: mallard
  662: mallet
  663: mammoth
  664: manatee
  665: mandarin orange
  666: manager/through
  667: manhole
  668: map
  669: marker
  670: martini
  671: mascot
  672: mashed potato
  673: masher
  674: mask/facemask
  675: mast
  676: mat/mat gym equipment/gym mat
  677: matchbox
  678: mattress
  679: measuring cup
  680: measuring stick/ruler/ruler measuring stick/measuring rod
  681: meatball
  682: medicine
  683: melon
  684: microphone
  685: microscope
  686: microwave oven
  687: milestone/milepost
  688: milk
  689: milk can
  690: milkshake
  691: minivan
  692: mint candy
  693: mirror
  694: mitten
  695: mixer/mixer kitchen tool/stand mixer
  696: money
  697: monitor/monitor computer equipment
  698: monkey
  699: motor
  700: motor scooter/scooter
  701: motor vehicle/automotive vehicle
  702: motorcycle
  703: mound/mound baseball/pitcher's mound
  704: mouse/mouse computer equipment/computer mouse
  705: mousepad
  706: muffin
  707: mug
  708: mushroom
  709: music stool/piano stool
  710: musical instrument/instrument/instrument musical
  711: nailfile
  712: napkin/table napkin/serviette
  713: neckerchief
  714: necklace
  715: necktie/tie/tie necktie
  716: needle
  717: nest
  718: newspaper/paper/paper newspaper
  719: newsstand
  720: nightshirt/nightwear/sleepwear/nightclothes
  721: nosebag/nosebag for animals/feedbag
  722: noseband/noseband for animals/nosepiece/nosepiece for animals
  723: notebook
  724: notepad
  725: nut
  726: nutcracker
  727: oar
  728: octopus/octopus food
  729: octopus/octopus animal
  730: oil lamp/kerosene lamp/kerosine lamp
  731: olive oil
  732: omelet/omelette
  733: onion
  734: orange/orange fruit
  735: orange juice
  736: ostrich
  737: ottoman/pouf/pouffe/hassock
  738: oven
  739: overalls/overalls clothing
  740: owl
  741: packet
  742: inkpad/inking pad/stamp pad
  743: pad
  744: paddle/boat paddle
  745: padlock
  746: paintbrush
  747: painting
  748: pajamas/pyjamas
  749: palette/pallet
  750: pan/pan for cooking/cooking pan
  751: pan/pan metal container
  752: pancake
  753: pantyhose
  754: papaya
  755: paper plate
  756: paper towel
  757: paperback book/paper-back book/softback book/soft-cover book
  758: paperweight
  759: parachute
  760: parakeet/parrakeet/parroket/paraquet/paroquet/parroquet
  761: parasail/parasail sports
  762: parasol/sunshade
  763: parchment
  764: parka/anorak
  765: parking meter
  766: parrot
  767: passenger car/passenger car part of a train/coach/coach part of a train
  768: passenger ship
  769: passport
  770: pastry
  771: patty/patty food
  772: pea/pea food
  773: peach
  774: peanut butter
  775: pear
  776: peeler/peeler tool for fruit and vegetables
  777: wooden leg/pegleg
  778: pegboard
  779: pelican
  780: pen
  781: pencil
  782: pencil box/pencil case
  783: pencil sharpener
  784: pendulum
  785: penguin
  786: pennant
  787: penny/penny coin
  788: pepper/peppercorn
  789: pepper mill/pepper grinder
  790: perfume
  791: persimmon
  792: person/baby/child/boy/girl/man/woman/human
  793: pet
  794: pew/pew church bench/church bench
  795: phonebook/telephone book/telephone directory
  796: phonograph record/phonograph recording/record/record phonograph recording
  797: piano
  798: pickle
  799: pickup truck
  800: pie
  801: pigeon
  802: piggy bank/penny bank
  803: pillow
  804: pin/pin non jewelry
  805: pineapple
  806: pinecone
  807: ping-pong ball
  808: pinwheel
  809: tobacco pipe
  810: pipe/piping
  811: pistol/handgun
  812: pita/pita bread/pocket bread
  813: pitcher/pitcher vessel for liquid/ewer
  814: pitchfork
  815: pizza
  816: place mat
  817: plate
  818: platter
  819: playpen
  820: pliers/plyers
  821: plow/plow farm equipment/plough/plough farm equipment
  822: plume
  823: pocket watch
  824: pocketknife
  825: poker/poker fire stirring tool/stove poker/fire hook
  826: pole/post
  827: polo shirt/sport shirt
  828: poncho
  829: pony
  830: pool table/billiard table/snooker table
  831: pop/pop soda/soda/soda pop/tonic/soft drink
  832: postbox/postbox public/mailbox/mailbox public
  833: postcard/postal card/mailing-card
  834: poster/placard
  835: pot
  836: flowerpot
  837: potato
  838: potholder
  839: pottery/clayware
  840: pouch
  841: power shovel/excavator/digger
  842: prawn/shrimp
  843: pretzel
  844: printer/printing machine
  845: projectile/projectile weapon/missile
  846: projector
  847: propeller/propellor
  848: prune
  849: pudding
  850: puffer/puffer fish/pufferfish/blowfish/globefish
  851: puffin
  852: pug-dog
  853: pumpkin
  854: puncher
  855: puppet/marionette
  856: puppy
  857: quesadilla
  858: quiche
  859: quilt/comforter
  860: rabbit
  861: race car/racing car
  862: racket/racquet
  863: radar
  864: radiator
  865: radio receiver/radio set/radio/tuner/tuner radio
  866: radish/daikon
  867: raft
  868: rag doll
  869: raincoat/waterproof jacket
  870: ram/ram animal
  871: raspberry
  872: rat
  873: razorblade
  874: reamer/reamer juicer/juicer/juice reamer
  875: rearview mirror
  876: receipt
  877: recliner/reclining chair/lounger/lounger chair
  878: record player/phonograph/phonograph record player/turntable
  879: reflector
  880: remote control
  881: rhinoceros
  882: rib/rib food
  883: rifle
  884: ring
  885: river boat
  886: road map
  887: robe
  888: rocking chair
  889: rodent
  890: roller skate
  891: Rollerblade
  892: rolling pin
  893: root beer
  894: router/router computer equipment
  895: rubber band/elastic band
  896: runner/runner carpet
  897: plastic bag/paper bag
  898: saddle/saddle on an animal
  899: saddle blanket/saddlecloth/horse blanket
  900: saddlebag
  901: safety pin
  902: sail
  903: salad
  904: salad plate/salad bowl
  905: salami
  906: salmon/salmon fish
  907: salmon/salmon food
  908: salsa
  909: saltshaker
  910: sandal/sandal type of shoe
  911: sandwich
  912: satchel
  913: saucepan
  914: saucer
  915: sausage
  916: sawhorse/sawbuck
  917: saxophone
  918: scale/scale measuring instrument
  919: scarecrow/strawman
  920: scarf
  921: school bus
  922: scissors
  923: scoreboard
  924: scraper
  925: screwdriver
  926: scrubbing brush
  927: sculpture
  928: seabird/seafowl
  929: seahorse
  930: seaplane/hydroplane
  931: seashell
  932: sewing machine
  933: shaker
  934: shampoo
  935: shark
  936: sharpener
  937: Sharpie
  938: shaver/shaver electric/electric shaver/electric razor
  939: shaving cream/shaving soap
  940: shawl
  941: shears
  942: sheep
  943: shepherd dog/sheepdog
  944: sherbert/sherbet
  945: shield
  946: shirt
  947: shoe/sneaker/sneaker type of shoe/tennis shoe
  948: shopping bag
  949: shopping cart
  950: short pants/shorts/shorts clothing/trunks/trunks clothing
  951: shot glass
  952: shoulder bag
  953: shovel
  954: shower head
  955: shower cap
  956: shower curtain
  957: shredder/shredder for paper
  958: signboard
  959: silo
  960: sink
  961: skateboard
  962: skewer
  963: ski
  964: ski boot
  965: ski parka/ski jacket
  966: ski pole
  967: skirt
  968: skullcap
  969: sled/sledge/sleigh
  970: sleeping bag
  971: sling/sling bandage/triangular bandage
  972: slipper/slipper footwear/carpet slipper/carpet slipper footwear
  973: smoothie
  974: snake/serpent
  975: snowboard
  976: snowman
  977: snowmobile
  978: soap
  979: soccer ball
  980: sock
  981: sofa/couch/lounge
  982: softball
  983: solar array/solar battery/solar panel
  984: sombrero
  985: soup
  986: soup bowl
  987: soupspoon
  988: sour cream/soured cream
  989: soya milk/soybean milk/soymilk
  990: space shuttle
  991: sparkler/sparkler fireworks
  992: spatula
  993: spear/lance
  994: spectacles/specs/eyeglasses/glasses
  995: spice rack
  996: spider
  997: crawfish/crayfish
  998: sponge
  999: spoon
  1000: sportswear/athletic wear/activewear
  1001: spotlight
  1002: squid/squid food/calamari/calamary
  1003: squirrel
  1004: stagecoach
  1005: stapler/stapler stapling machine
  1006: starfish/sea star
  1007: statue/statue sculpture
  1008: steak/steak food
  1009: steak knife
  1010: steering wheel
  1011: stepladder
  1012: step stool
  1013: stereo/stereo sound system
  1014: stew
  1015: stirrer
  1016: stirrup
  1017: stool
  1018: stop sign
  1019: brake light
  1020: stove/kitchen stove/range/range kitchen appliance/kitchen range/cooking stove
  1021: strainer
  1022: strap
  1023: straw/straw for drinking/drinking straw
  1024: strawberry
  1025: street sign
  1026: streetlight/street lamp
  1027: string cheese
  1028: stylus
  1029: subwoofer
  1030: sugar bowl
  1031: sugarcane/sugarcane plant
  1032: suit/suit clothing
  1033: sunflower
  1034: sunglasses
  1035: sunhat
  1036: surfboard
  1037: sushi
  1038: mop
  1039: sweat pants
  1040: sweatband
  1041: sweater
  1042: sweatshirt
  1043: sweet potato
  1044: swimsuit/swimwear/bathing suit/swimming costume/bathing costume/swimming trunks/bathing trunks
  1045: sword
  1046: syringe
  1047: Tabasco sauce
  1048: table-tennis table/ping-pong table
  1049: table
  1050: table lamp
  1051: tablecloth
  1052: tachometer
  1053: taco
  1054: tag
  1055: taillight/rear light
  1056: tambourine
  1057: army tank/armored combat vehicle
  1058: tank/tank storage vessel/storage tank
  1059: tank top/tank top clothing
  1060: tape/tape sticky cloth or paper
  1061: tape measure/measuring tape
  1062: tapestry
  1063: tarp
  1064: tartan/plaid
  1065: tassel
  1066: tea bag
  1067: teacup
  1068: teakettle
  1069: teapot
  1070: teddy bear
  1071: telephone/phone/telephone set
  1072: telephone booth/phone booth/call box/telephone box/telephone kiosk
  1073: telephone pole/telegraph pole/telegraph post
  1074: telephoto lens/zoom lens
  1075: television camera/tv camera
  1076: television set/tv/tv set
  1077: tennis ball
  1078: tennis racket
  1079: tequila
  1080: thermometer
  1081: thermos bottle
  1082: thermostat
  1083: thimble
  1084: thread/yarn
  1085: thumbtack/drawing pin/pushpin
  1086: tiara
  1087: tiger
  1088: tights/tights clothing/leotards
  1089: timer/stopwatch
  1090: tinfoil
  1091: tinsel
  1092: tissue paper
  1093: toast/toast food
  1094: toaster
  1095: toaster oven
  1096: toilet
  1097: toilet tissue/toilet paper/bathroom tissue
  1098: tomato
  1099: tongs
  1100: toolbox
  1101: toothbrush
  1102: toothpaste
  1103: toothpick
  1104: cover
  1105: tortilla
  1106: tow truck
  1107: towel
  1108: towel rack/towel rail/towel bar
  1109: toy
  1110: tractor/tractor farm equipment
  1111: traffic light
  1112: dirt bike
  1113: trailer truck/tractor trailer/trucking rig/articulated lorry/semi truck
  1114: train/train railroad vehicle/railroad train
  1115: trampoline
  1116: tray
  1117: trench coat
  1118: triangle/triangle musical instrument
  1119: tricycle
  1120: tripod
  1121: trousers/pants/pants clothing
  1122: truck
  1123: truffle/truffle chocolate/chocolate truffle
  1124: trunk
  1125: vat
  1126: turban
  1127: turkey/turkey food
  1128: turnip
  1129: turtle
  1130: turtleneck/turtleneck clothing/polo-neck
  1131: typewriter
  1132: umbrella
  1133: underwear/underclothes/underclothing/underpants
  1134: unicycle
  1135: urinal
  1136: urn
  1137: vacuum cleaner
  1138: vase
  1139: vending machine
  1140: vent/blowhole/air vent
  1141: vest/waistcoat
  1142: videotape
  1143: vinegar
  1144: violin/fiddle
  1145: vodka
  1146: volleyball
  1147: vulture
  1148: waffle
  1149: waffle iron
  1150: wagon
  1151: wagon wheel
  1152: walking stick
  1153: wall clock
  1154: wall socket/wall plug/electric outlet/electrical outlet/outlet/electric receptacle
  1155: wallet/billfold
  1156: walrus
  1157: wardrobe
  1158: washbasin/basin/basin for washing/washbowl/washstand/handbasin
  1159: automatic washer/washing machine
  1160: watch/wristwatch
  1161: water bottle
  1162: water cooler
  1163: water faucet/water tap/tap/tap water faucet
  1164: water heater/hot-water heater
  1165: water jug
  1166: water gun/squirt gun
  1167: water scooter/sea scooter/jet ski
  1168: water ski
  1169: water tower
  1170: watering can
  1171: watermelon
  1172: weathervane/vane/vane weathervane/wind vane
  1173: webcam
  1174: wedding cake/bridecake
  1175: wedding ring/wedding band
  1176: wet suit
  1177: wheel
  1178: wheelchair
  1179: whipped cream
  1180: whistle
  1181: wig
  1182: wind chime
  1183: windmill
  1184: window box/window box for plants
  1185: windshield wiper/windscreen wiper/wiper/wiper for windshield or screen
  1186: windsock/air sock/air-sleeve/wind sleeve/wind cone
  1187: wine bottle
  1188: wine bucket/wine cooler
  1189: wineglass
  1190: blinder/blinder for horses
  1191: wok
  1192: wolf
  1193: wooden spoon
  1194: wreath
  1195: wrench/spanner
  1196: wristband
  1197: wristlet/wrist band
  1198: yacht
  1199: yogurt/yoghurt/yoghourt
  1200: yoke/yoke animal equipment
  1201: zebra
  1202: zucchini/courgette

# Download script/URL (optional)
download: |
  from pathlib import Path

  from ultralytics.utils import ASSETS_URL
  from ultralytics.utils.downloads import download

  # Download labels
  dir = Path(yaml["path"])  # dataset root dir
  urls = [f"{ASSETS_URL}/lvis-labels-segments.zip"]
  download(urls, dir=dir.parent)

  # Download data
  urls = [
      "http://images.cocodataset.org/zips/train2017.zip",  # 19G, 118k images
      "http://images.cocodataset.org/zips/val2017.zip",  # 1G, 5k images
      "http://images.cocodataset.org/zips/test2017.zip",  # 7G, 41k images (optional)
  ]
  download(urls, dir=dir / "images", threads=3)
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="lvis.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=lvis.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (css):
```css
@inproceedings{gupta2019lvis,
  title={LVIS: A Dataset for Large Vocabulary Instance Segmentation},
  author={Gupta, Agrim and Dollar, Piotr and Girshick, Ross},
  booktitle={Proceedings of the {IEEE} Conference on Computer Vision and Pattern Recognition},
  year={2019}
}
```

---

## Medical Pills Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/medical-pills/

**Contents:**
- Medical Pills Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Integration with Other Datasets
- Citations and Acknowledgments
- FAQ
  - What is the structure of the medical-pills dataset?

The medical-pills detection dataset is a proof-of-concept (POC) dataset, carefully curated to demonstrate the potential of AI in pharmaceutical applications. It contains labeled images specifically designed to train computer visionmodels for identifying medical-pills.

Watch: How to train Ultralytics YOLO26 Model on Medical Pills Detection Dataset in Google Colab

This dataset serves as a foundational resource for automating essential tasks such as quality control, packaging automation, and efficient sorting in pharmaceutical workflows. By integrating this dataset into projects, researchers and developers can explore innovative solutions that enhance accuracy, streamline operations, and ultimately contribute to improved healthcare outcomes.

The medical-pills dataset is divided into two subsets:

Using computer vision for medical-pills detection enables automation in the pharmaceutical industry, supporting tasks like:

A YAML configuration file is provided to define the dataset's structure, including paths and classes. For the medical-pills dataset, the medical-pills.yaml file can be accessed at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/medical-pills.yaml.

ultralytics/cfg/datasets/medical-pills.yaml

To train a YOLO26n model on the medical-pills dataset for 100 epochs with an image size of 640, use the following examples. For detailed arguments, refer to the model's Training page.

The medical-pills dataset features labeled images showcasing the diversity of pills. Below is an example of a labeled image from the dataset:

For more comprehensive pharmaceutical analysis, consider combining the medical-pills dataset with other related datasets like package-seg for packaging identification or medical imaging datasets like brain-tumor to develop end-to-end healthcare AI solutions.

The dataset is available under the AGPL-3.0 License.

If you use the Medical-pills dataset in your research or development work, please cite it using the mentioned details:

The dataset includes 92 images for training and 23 images for validation. Each image is annotated with the class pill, enabling effective training and evaluation of models for pharmaceutical applications.

You can train a YOLO26 model for 100 epochs with an image size of 640px using the Python or CLI methods provided. Refer to the Training Example section for detailed instructions and check the YOLO26 documentation for more information on model capabilities.

The dataset enables automation in pill detection, contributing to counterfeit prevention, quality assurance, and pharmaceutical process optimization. It also serves as a valuable resource for developing AI solutions that can improve medication safety and supply chain efficiency.

Inference can be done using Python or CLI methods with a fine-tuned YOLO26 model. Refer to the Inference Example section for code snippets and the Predict mode documentation for additional options.

The YAML file is available at medical-pills.yaml, containing dataset paths, classes, and additional configuration details essential for training models on this dataset.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Medical-pills dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/medical-pills/
# Example usage: yolo train data=medical-pills.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── medical-pills ← downloads here (8.19 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: medical-pills # dataset root dir
train: images/train # train images (relative to 'path') 92 images
val: images/val # val images (relative to 'path') 23 images

# Classes
names:
  0: pill

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/medical-pills.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="medical-pills.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=medical-pills.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load a fine-tuned model

# Inference using the model
results = model.predict("https://ultralytics.com/assets/medical-pills-sample.jpg")
```

---

## MNIST Dataset

**URL:** https://docs.ultralytics.com/datasets/classify/mnist/

**Contents:**
- MNIST Dataset
- Key Features
- Dataset Structure
- Dataset Access
- Extended MNIST (EMNIST)
- Applications
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- MNIST160 Quick Tests

The MNIST (Modified National Institute of Standards and Technology) dataset is a large database of handwritten digits that is commonly used for training various image processing systems and machine learning models. It was created by "re-mixing" the samples from NIST's original datasets and has become a benchmark for evaluating the performance of image classification algorithms.

The MNIST dataset is split into two subsets:

Each image in the dataset is labeled with the corresponding digit (0-9), making it a supervised learning dataset ideal for classification tasks.

Extended MNIST (EMNIST) is a newer dataset developed and released by NIST to be the successor to MNIST. While MNIST included images only of handwritten digits, EMNIST includes all the images from NIST Special Database 19, which is a large database of handwritten uppercase and lowercase letters as well as digits. The images in EMNIST were converted into the same 28×28 pixel format, by the same process, as were the MNIST images. Accordingly, tools that work with the older, smaller MNIST dataset will likely work unmodified with EMNIST.

The MNIST dataset is widely used for training and evaluating deep learning models in image classification tasks, such as Convolutional Neural Networks (CNNs), Support Vector Machines (SVMs), and various other machine learning algorithms. The dataset's simple and well-structured format makes it an essential resource for researchers and practitioners in the field of machine learning and computer vision.

Some common applications include:

To train a CNN model on the MNIST dataset for 100 epochs with an image size of 28×28, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The MNIST dataset contains grayscale images of handwritten digits, providing a well-structured dataset for image classification tasks. Here are some examples of images from the dataset:

The example showcases the variety and complexity of the handwritten digits in the MNIST dataset, highlighting the importance of a diverse dataset for training robust image classification models.

If you use the MNIST dataset in your research or development work, please cite the following paper:

We would like to acknowledge Yann LeCun, Corinna Cortes, and Christopher J.C. Burges for creating and maintaining the MNIST dataset as a valuable resource for the machine learning and computer vision research community. For more information about the MNIST dataset and its creators, visit the MNIST dataset website.

Need a lightning-fast regression test? Ultralytics also exposes data="mnist160", a 160-image slice containing the first eight samples from each digit class. It mirrors the MNIST directory structure, so you can swap datasets without changing any other arguments:

Train Example with MNIST160

Use this subset for CI pipelines or sanity checks before committing to the full 70,000-image dataset.

The MNIST dataset, or Modified National Institute of Standards and Technology dataset, is a widely-used collection of handwritten digits designed for training and testing image classification systems. It includes 60,000 training images and 10,000 testing images, all of which are grayscale and 28×28 pixels in size. The dataset's importance lies in its role as a standard benchmark for evaluating image classification algorithms, helping researchers and engineers to compare methods and track progress in the field.

To train a model on the MNIST dataset using Ultralytics YOLO, you can follow these steps:

For a detailed list of available training arguments, refer to the Training page.

The MNIST dataset contains only handwritten digits, whereas the Extended MNIST (EMNIST) dataset includes both digits and uppercase and lowercase letters. EMNIST was developed as a successor to MNIST and utilizes the same 28×28 pixel format for the images, making it compatible with tools and models designed for the original MNIST dataset. This broader range of characters in EMNIST makes it useful for a wider variety of machine learning applications.

Yes, you can use Ultralytics Platform to train models on custom datasets like MNIST. Ultralytics Platform offers a user-friendly interface for uploading datasets, training models, and managing projects without needing extensive coding knowledge. For more details on how to get started, check out the Ultralytics Platform Quickstart page.

MNIST is simpler than many modern datasets like CIFAR-10 or ImageNet, making it ideal for beginners and quick experimentation. While more complex datasets offer greater challenges with color images and diverse object categories, MNIST remains valuable for its simplicity, small file size, and historical significance in the development of machine learning algorithms. For more advanced classification tasks, consider using Fashion-MNIST, which maintains the same structure but features clothing items instead of digits.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-cls.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="mnist", epochs=100, imgsz=28)
```

Example 2 (sql):
```sql
# Start training from a pretrained *.pt model
yolo classify train data=mnist model=yolo26n-cls.pt epochs=100 imgsz=28
```

Example 3 (python):
```python
@article{lecun2010mnist,
         title={MNIST handwritten digit database},
         author={LeCun, Yann and Cortes, Corinna and Burges, CJ},
         journal={ATT Labs [Online]. Available: http://yann.lecun.com/exdb/mnist},
         volume={2},
         year={2010}
}
```

Example 4 (unknown):
```unknown
yolo classify train data=mnist160 model=yolo26n-cls.pt epochs=5 imgsz=28
```

---

## Multi-object Tracking Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/track/

**Contents:**
- Multi-object Tracking Datasets Overview
- Dataset Format (Coming Soon)
- Available Trackers
- Usage
- Persisting Tracks Between Frames
- FAQ
  - How do I use Multi-Object Tracking with Ultralytics YOLO?
  - What are the upcoming features for training trackers in Ultralytics?
  - Why should I use Ultralytics YOLO for multi-object tracking?
  - Can I use custom datasets for multi-object tracking with Ultralytics YOLO?

Multi-object tracking is a critical component in video analytics that identifies objects and maintains unique IDs for each detected object across video frames. Ultralytics YOLO provides powerful tracking capabilities that can be applied to various domains including surveillance, sports analytics, and traffic monitoring.

Ultralytics tracking currently reuses detection, segmentation, or pose models without requiring tracker-specific training. Native tracker-training support is under active development.

Ultralytics YOLO supports the following tracking algorithms:

For continuous tracking across video frames, you can use the persist=True parameter:

To use Multi-Object Tracking with Ultralytics YOLO, you can start by using the Python or CLI examples provided. Here is how you can get started:

These commands load the YOLO26 model and use it for tracking objects in the given video source with specific confidence (conf) and Intersection over Union (iou) thresholds. For more details, refer to the track mode documentation.

Ultralytics is continuously enhancing its AI models. An upcoming feature will enable the training of standalone trackers. Until then, Multi-Object Detector leverages pretrained detection, segmentation, or Pose models for tracking without requiring standalone training. Stay updated by following our blog or checking the upcoming features.

Ultralytics YOLO is a state-of-the-art object detection model known for its real-time performance and high accuracy. Using YOLO for multi-object tracking provides several advantages:

For more details on setting up and using YOLO for tracking, visit our track usage guide.

Yes, you can use custom datasets for multi-object tracking with Ultralytics YOLO. While support for standalone tracker training is an upcoming feature, you can already use pretrained models on your custom datasets. Prepare your datasets in the appropriate format compatible with YOLO and follow the documentation to integrate them.

After running a tracking job with Ultralytics YOLO, the results include various data points such as tracked object IDs, their bounding boxes, and the confidence scores. Here's a brief overview of how to interpret these results:

For detailed guidance on interpreting and visualizing these results, refer to the results handling guide.

You can customize the tracker by creating a modified version of the tracker configuration file. Copy an existing tracker config file from ultralytics/cfg/trackers, modify the parameters as needed, and specify this file when running the tracker:

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")
results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.1, iou=0.7, show=True)
```

Example 2 (unknown):
```unknown
yolo track model=yolo26n.pt source="https://youtu.be/LNwODJXcvt4" conf=0.1 iou=0.7 show=True
```

Example 3 (python):
```python
import cv2

from ultralytics import YOLO

# Load the YOLO model
model = YOLO("yolo26n.pt")

# Open the video file
cap = cv2.VideoCapture("path/to/video.mp4")

while cap.isOpened():
    success, frame = cap.read()
    if success:
        # Run tracking with persistence between frames
        results = model.track(frame, persist=True)

        # Visualize the results
        annotated_frame = results[0].plot()
        cv2.imshow("Tracking", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
```

Example 4 (python):
```python
from ultralytics import YOLO

model = YOLO("yolo26n.pt")  # Load the YOLO26 model
results = model.track(source="https://youtu.be/LNwODJXcvt4", conf=0.1, iou=0.7, show=True)
```

---

## Objects365 Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/objects365/

**Contents:**
- Objects365 Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Objects365 dataset used for?

The Objects365 dataset is a large-scale, high-quality dataset designed to foster object detection research with a focus on diverse objects in the wild. Created by a team of Megvii researchers, the dataset offers a wide range of high-resolution images with a comprehensive set of annotated bounding boxes covering 365 object categories.

Watch: How to Train Ultralytics YOLO26 on the Objects365 Dataset with Ultralytics | 2M Annotations 🚀

The Objects365 dataset is organized into a single set of images with corresponding annotations:

The Objects365 dataset is widely used for training and evaluating deep learning models in object detection tasks. The dataset's diverse set of object categories and high-quality annotations make it a valuable resource for researchers and practitioners in the field of computer vision.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. For the case of the Objects365 Dataset, the Objects365.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/Objects365.yaml.

ultralytics/cfg/datasets/Objects365.yaml

To train a YOLO26n model on the Objects365 dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Objects365 dataset contains a diverse set of high-resolution images with objects from 365 categories, providing rich context for object detection tasks. Here are some examples of the images in the dataset:

The example showcases the variety and complexity of the data in the Objects365 dataset and highlights the importance of accurate object detection for computer vision applications.

If you use the Objects365 dataset in your research or development work, please cite the following paper:

We would like to acknowledge the team of researchers who created and maintain the Objects365 dataset as a valuable resource for the computer vision research community. For more information about the Objects365 dataset and its creators, visit the Objects365 dataset website.

The Objects365 dataset is designed for object detection tasks in machine learning and computer vision. It provides a large-scale, high-quality dataset with 2 million annotated images and 30 million bounding boxes across 365 categories. Leveraging such a diverse dataset helps improve the performance and generalization of object detection models, making it invaluable for research and development in the field.

To train a YOLO26n model using the Objects365 dataset for 100 epochs with an image size of 640, follow these instructions:

Refer to the Training page for a comprehensive list of available arguments.

The Objects365 dataset offers several advantages for object detection tasks:

The YAML configuration file for the Objects365 dataset is available at Objects365.yaml. This file contains essential information such as dataset paths and class labels, crucial for setting up your training environment.

The Objects365 dataset is organized with 2 million high-resolution images and comprehensive annotations of over 30 million bounding boxes. This structure ensures a robust dataset for training deep learning models in object detection, offering a wide variety of objects and scenarios. Such diversity and volume help in developing models that are more accurate and capable of generalizing well to real-world applications. For more details on the dataset structure, refer to the Dataset YAML section.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Objects365 dataset https://www.objects365.org/ by Megvii
# Documentation: https://docs.ultralytics.com/datasets/detect/objects365/
# Example usage: yolo train data=Objects365.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── Objects365 ← downloads here (712 GB = 367G data + 345G zips)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: Objects365 # dataset root dir
train: images/train # train images (relative to 'path') 1742289 images
val: images/val # val images (relative to 'path') 80000 images
test: # test images (optional)

# Classes
names:
  0: Person
  1: Sneakers
  2: Chair
  3: Other Shoes
  4: Hat
  5: Car
  6: Lamp
  7: Glasses
  8: Bottle
  9: Desk
  10: Cup
  11: Street Lights
  12: Cabinet/shelf
  13: Handbag/Satchel
  14: Bracelet
  15: Plate
  16: Picture/Frame
  17: Helmet
  18: Book
  19: Gloves
  20: Storage box
  21: Boat
  22: Leather Shoes
  23: Flower
  24: Bench
  25: Potted Plant
  26: Bowl/Basin
  27: Flag
  28: Pillow
  29: Boots
  30: Vase
  31: Microphone
  32: Necklace
  33: Ring
  34: SUV
  35: Wine Glass
  36: Belt
  37: Monitor/TV
  38: Backpack
  39: Umbrella
  40: Traffic Light
  41: Speaker
  42: Watch
  43: Tie
  44: Trash bin Can
  45: Slippers
  46: Bicycle
  47: Stool
  48: Barrel/bucket
  49: Van
  50: Couch
  51: Sandals
  52: Basket
  53: Drum
  54: Pen/Pencil
  55: Bus
  56: Wild Bird
  57: High Heels
  58: Motorcycle
  59: Guitar
  60: Carpet
  61: Cell Phone
  62: Bread
  63: Camera
  64: Canned
  65: Truck
  66: Traffic cone
  67: Cymbal
  68: Lifesaver
  69: Towel
  70: Stuffed Toy
  71: Candle
  72: Sailboat
  73: Laptop
  74: Awning
  75: Bed
  76: Faucet
  77: Tent
  78: Horse
  79: Mirror
  80: Power outlet
  81: Sink
  82: Apple
  83: Air Conditioner
  84: Knife
  85: Hockey Stick
  86: Paddle
  87: Pickup Truck
  88: Fork
  89: Traffic Sign
  90: Balloon
  91: Tripod
  92: Dog
  93: Spoon
  94: Clock
  95: Pot
  96: Cow
  97: Cake
  98: Dining Table
  99: Sheep
  100: Hanger
  101: Blackboard/Whiteboard
  102: Napkin
  103: Other Fish
  104: Orange/Tangerine
  105: Toiletry
  106: Keyboard
  107: Tomato
  108: Lantern
  109: Machinery Vehicle
  110: Fan
  111: Green Vegetables
  112: Banana
  113: Baseball Glove
  114: Airplane
  115: Mouse
  116: Train
  117: Pumpkin
  118: Soccer
  119: Skiboard
  120: Luggage
  121: Nightstand
  122: Tea pot
  123: Telephone
  124: Trolley
  125: Head Phone
  126: Sports Car
  127: Stop Sign
  128: Dessert
  129: Scooter
  130: Stroller
  131: Crane
  132: Remote
  133: Refrigerator
  134: Oven
  135: Lemon
  136: Duck
  137: Baseball Bat
  138: Surveillance Camera
  139: Cat
  140: Jug
  141: Broccoli
  142: Piano
  143: Pizza
  144: Elephant
  145: Skateboard
  146: Surfboard
  147: Gun
  148: Skating and Skiing shoes
  149: Gas stove
  150: Donut
  151: Bow Tie
  152: Carrot
  153: Toilet
  154: Kite
  155: Strawberry
  156: Other Balls
  157: Shovel
  158: Pepper
  159: Computer Box
  160: Toilet Paper
  161: Cleaning Products
  162: Chopsticks
  163: Microwave
  164: Pigeon
  165: Baseball
  166: Cutting/chopping Board
  167: Coffee Table
  168: Side Table
  169: Scissors
  170: Marker
  171: Pie
  172: Ladder
  173: Snowboard
  174: Cookies
  175: Radiator
  176: Fire Hydrant
  177: Basketball
  178: Zebra
  179: Grape
  180: Giraffe
  181: Potato
  182: Sausage
  183: Tricycle
  184: Violin
  185: Egg
  186: Fire Extinguisher
  187: Candy
  188: Fire Truck
  189: Billiards
  190: Converter
  191: Bathtub
  192: Wheelchair
  193: Golf Club
  194: Briefcase
  195: Cucumber
  196: Cigar/Cigarette
  197: Paint Brush
  198: Pear
  199: Heavy Truck
  200: Hamburger
  201: Extractor
  202: Extension Cord
  203: Tong
  204: Tennis Racket
  205: Folder
  206: American Football
  207: earphone
  208: Mask
  209: Kettle
  210: Tennis
  211: Ship
  212: Swing
  213: Coffee Machine
  214: Slide
  215: Carriage
  216: Onion
  217: Green beans
  218: Projector
  219: Frisbee
  220: Washing Machine/Drying Machine
  221: Chicken
  222: Printer
  223: Watermelon
  224: Saxophone
  225: Tissue
  226: Toothbrush
  227: Ice cream
  228: Hot-air balloon
  229: Cello
  230: French Fries
  231: Scale
  232: Trophy
  233: Cabbage
  234: Hot dog
  235: Blender
  236: Peach
  237: Rice
  238: Wallet/Purse
  239: Volleyball
  240: Deer
  241: Goose
  242: Tape
  243: Tablet
  244: Cosmetics
  245: Trumpet
  246: Pineapple
  247: Golf Ball
  248: Ambulance
  249: Parking meter
  250: Mango
  251: Key
  252: Hurdle
  253: Fishing Rod
  254: Medal
  255: Flute
  256: Brush
  257: Penguin
  258: Megaphone
  259: Corn
  260: Lettuce
  261: Garlic
  262: Swan
  263: Helicopter
  264: Green Onion
  265: Sandwich
  266: Nuts
  267: Speed Limit Sign
  268: Induction Cooker
  269: Broom
  270: Trombone
  271: Plum
  272: Rickshaw
  273: Goldfish
  274: Kiwi fruit
  275: Router/modem
  276: Poker Card
  277: Toaster
  278: Shrimp
  279: Sushi
  280: Cheese
  281: Notepaper
  282: Cherry
  283: Pliers
  284: CD
  285: Pasta
  286: Hammer
  287: Cue
  288: Avocado
  289: Hami melon
  290: Flask
  291: Mushroom
  292: Screwdriver
  293: Soap
  294: Recorder
  295: Bear
  296: Eggplant
  297: Board Eraser
  298: Coconut
  299: Tape Measure/Ruler
  300: Pig
  301: Showerhead
  302: Globe
  303: Chips
  304: Steak
  305: Crosswalk Sign
  306: Stapler
  307: Camel
  308: Formula 1
  309: Pomegranate
  310: Dishwasher
  311: Crab
  312: Hoverboard
  313: Meatball
  314: Rice Cooker
  315: Tuba
  316: Calculator
  317: Papaya
  318: Antelope
  319: Parrot
  320: Seal
  321: Butterfly
  322: Dumbbell
  323: Donkey
  324: Lion
  325: Urinal
  326: Dolphin
  327: Electric Drill
  328: Hair Dryer
  329: Egg tart
  330: Jellyfish
  331: Treadmill
  332: Lighter
  333: Grapefruit
  334: Game board
  335: Mop
  336: Radish
  337: Baozi
  338: Target
  339: French
  340: Spring Rolls
  341: Monkey
  342: Rabbit
  343: Pencil Case
  344: Yak
  345: Red Cabbage
  346: Binoculars
  347: Asparagus
  348: Barbell
  349: Scallop
  350: Noddles
  351: Comb
  352: Dumpling
  353: Oyster
  354: Table Tennis paddle
  355: Cosmetics Brush/Eyeliner Pencil
  356: Chainsaw
  357: Eraser
  358: Lobster
  359: Durian
  360: Okra
  361: Lipstick
  362: Cosmetics Mirror
  363: Curling
  364: Table Tennis

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  from concurrent.futures import ThreadPoolExecutor
  from pathlib import Path

  import numpy as np

  from ultralytics.utils import TQDM
  from ultralytics.utils.checks import check_requirements
  from ultralytics.utils.downloads import download
  from ultralytics.utils.ops import xyxy2xywhn

  check_requirements("faster-coco-eval")
  from faster_coco_eval import COCO

  # Train, Val Splits
  dir = Path(yaml["path"])
  for split, patches in [("train", 50 + 1), ("val", 43 + 1)]:
      print(f"Processing {split} in {patches} patches ...")
      images, labels = dir / "images" / split, dir / "labels" / split
      images.mkdir(parents=True, exist_ok=True)
      labels.mkdir(parents=True, exist_ok=True)

      # Download
      url = f"https://dorc.ks3-cn-beijing.ksyun.com/data-set/2020Objects365%E6%95%B0%E6%8D%AE%E9%9B%86/{split}/"
      if split == "train":
          download([f"{url}zhiyuan_objv2_{split}.tar.gz"], dir=dir)  # annotations json
          download([f"{url}patch{i}.tar.gz" for i in range(patches)], dir=images, threads=17)  # 51 patches / 17 threads = 3
      elif split == "val":
          download([f"{url}zhiyuan_objv2_{split}.json"], dir=dir)  # annotations json
          download([f"{url}images/v1/patch{i}.tar.gz" for i in range(15 + 1)], dir=images, threads=16)
          download([f"{url}images/v2/patch{i}.tar.gz" for i in range(16, patches)], dir=images, threads=16)

      # Move
      files = list(images.rglob("*.jpg"))
      with ThreadPoolExecutor(max_workers=16) as executor:
          list(TQDM(executor.map(lambda f: f.rename(images / f.name), files), total=len(files), desc=f"Moving {split} images"))

      # Labels
      coco = COCO(dir / f"zhiyuan_objv2_{split}.json")
      names = [x["name"] for x in coco.loadCats(coco.getCatIds())]
      for cid, cat in enumerate(names):
          catIds = coco.getCatIds(catNms=[cat])
          imgIds = coco.getImgIds(catIds=catIds)

          def process_annotation(im):
              """Process and write annotations for a single image."""
              try:
                  width, height = im["width"], im["height"]
                  path = Path(im["file_name"])
                  with open(labels / path.with_suffix(".txt").name, "a", encoding="utf-8") as file:
                      annIds = coco.getAnnIds(imgIds=im["id"], catIds=catIds, iscrowd=None)
                      for a in coco.loadAnns(annIds):
                          x, y, w, h = a["bbox"]  # bounding box in xywh (xy top-left corner)
                          xyxy = np.array([x, y, x + w, y + h])[None]  # pixels(1,4)
                          x, y, w, h = xyxy2xywhn(xyxy, w=width, h=height, clip=True)[0]  # normalized and clipped
                          file.write(f"{cid} {x:.5f} {y:.5f} {w:.5f} {h:.5f}\n")
              except Exception as e:
                  print(e)

          images_list = coco.loadImgs(imgIds)
          with ThreadPoolExecutor(max_workers=16) as executor:
              list(TQDM(executor.map(process_annotation, images_list), total=len(images_list), desc=f"Class {cid + 1}/{len(names)} {cat}"))
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="Objects365.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=Objects365.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (css):
```css
@inproceedings{shao2019objects365,
  title={Objects365: A Large-scale, High-quality Dataset for Object Detection},
  author={Shao, Shuai and Li, Zeming and Zhang, Tianyuan and Peng, Chao and Yu, Gang and Li, Jing and Zhang, Xiangyu and Sun, Jian},
  booktitle={Proceedings of the IEEE/CVF International Conference on Computer Vision},
  pages={8425--8434},
  year={2019}
}
```

---

## Object Detection Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/detect/

**Contents:**
- Object Detection Datasets Overview
- Supported Dataset Formats
  - Ultralytics YOLO format
    - Usage Example
  - Ultralytics NDJSON format
    - Usage Example
    - Advantages of NDJSON format
- Supported Datasets
  - Adding your own dataset
- Port or Convert Label Formats

Training a robust and accurate object detection model requires a comprehensive dataset. This guide introduces various formats of datasets that are compatible with the Ultralytics YOLO model and provides insights into their structure, usage, and how to convert between different formats.

The Ultralytics YOLO format is a dataset configuration format that allows you to define the dataset root directory, the relative paths to training/validation/testing image directories or *.txt files containing image paths, and a dictionary of class names. Here is an example:

ultralytics/cfg/datasets/coco8.yaml

Labels for this format should be exported to YOLO format with one *.txt file per image. If there are no objects in an image, no *.txt file is required. The *.txt file should be formatted with one row per object in class x_center y_center width height format. Box coordinates must be in normalized xywh format (from 0 to 1). If your boxes are in pixels, you should divide x_center and width by image width, and y_center and height by image height. Class numbers should be zero-indexed (start with 0).

The label file corresponding to the above image contains 2 persons (class 0) and a tie (class 27):

When using the Ultralytics YOLO format, organize your training and validation images and labels as shown in the COCO8 dataset example below.

Here's how you can use YOLO format datasets to train your model:

The NDJSON (Newline Delimited JSON) format provides an alternative way to define datasets for Ultralytics YOLO models. This format stores dataset metadata and annotations in a single file where each line contains a separate JSON object.

An NDJSON dataset file contains:

Format: [class_id, x_center, y_center, width, height]

Format: [class_id, x1, y1, x2, y2, x3, y3, ...]

Format: [class_id, x_center, y_center, width, height, x1, y1, v1, x2, y2, v2, ...]

Keypoints follow bbox as repeated (x, y, v) triplets where v is visibility: 0=not labeled, 1=labeled but occluded, 2=labeled and visible. The keypoint count is dataset-specific (e.g., COCO pose has 17 keypoints = 51 values after bbox).

Format: [class_id, x1, y1, x2, y2, x3, y3, x4, y4]

The four corner points define the oriented bounding box in clockwise order starting from the top-left corner. All coordinates are normalized (0-1).

To use an NDJSON dataset with YOLO26, simply specify the path to the .ndjson file:

Here is a list of the supported datasets and a brief description for each:

If you have your own dataset and would like to use it for training detection models with Ultralytics YOLO format, ensure that it follows the format specified above under "Ultralytics YOLO format". Convert your annotations to the required format and specify the paths, number of classes, and class names in the YAML configuration file.

You can easily convert labels from the popular COCO dataset format to the YOLO format using the following code snippet:

This conversion tool can be used to convert the COCO dataset or any dataset in the COCO format to the Ultralytics YOLO format. The process transforms the JSON-based COCO annotations into the simpler text-based YOLO format, making it compatible with Ultralytics YOLO models.

Remember to double-check if the dataset you want to use is compatible with your model and follows the necessary format conventions. Properly formatted datasets are crucial for training successful object detection models.

The Ultralytics YOLO format is a structured configuration for defining datasets in your training projects. It involves setting paths to your training, validation, and testing images and corresponding labels. For example:

Labels are saved in *.txt files with one file per image, formatted as class x_center y_center width height with normalized coordinates. For a detailed guide, see the COCO8 dataset example.

You can convert a COCO dataset to the YOLO format using the Ultralytics conversion tools. Here's a quick method:

This code will convert your COCO annotations to YOLO format, enabling seamless integration with Ultralytics YOLO models. For additional details, visit the Port or Convert Label Formats section.

Ultralytics YOLO supports a wide range of datasets, including:

Each dataset page provides detailed information on the structure and usage tailored for efficient YOLO26 training. Explore the full list in the Supported Datasets section.

To start training a YOLO26 model, ensure your dataset is formatted correctly and the paths are defined in a YAML file. Use the following script to begin training:

Refer to the Usage section for more details on utilizing different modes, including CLI commands.

Ultralytics provides numerous examples and practical guides for using YOLO26 in diverse applications. For a comprehensive overview, visit the Ultralytics Blog where you can find case studies, detailed tutorials, and community stories showcasing object detection, segmentation, and more with YOLO26. For specific examples, check the Usage section in the documentation.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8 dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/coco8/
# Example usage: yolo train data=coco8.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8 ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8 # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Classes
names:
  0: person
  1: bicycle
  2: car
  3: motorcycle
  4: airplane
  5: bus
  6: train
  7: truck
  8: boat
  9: traffic light
  10: fire hydrant
  11: stop sign
  12: parking meter
  13: bench
  14: bird
  15: cat
  16: dog
  17: horse
  18: sheep
  19: cow
  20: elephant
  21: bear
  22: zebra
  23: giraffe
  24: backpack
  25: umbrella
  26: handbag
  27: tie
  28: suitcase
  29: frisbee
  30: skis
  31: snowboard
  32: sports ball
  33: kite
  34: baseball bat
  35: baseball glove
  36: skateboard
  37: surfboard
  38: tennis racket
  39: bottle
  40: wine glass
  41: cup
  42: fork
  43: knife
  44: spoon
  45: bowl
  46: banana
  47: apple
  48: sandwich
  49: orange
  50: broccoli
  51: carrot
  52: hot dog
  53: pizza
  54: donut
  55: cake
  56: chair
  57: couch
  58: potted plant
  59: bed
  60: dining table
  61: toilet
  62: tv
  63: laptop
  64: mouse
  65: remote
  66: keyboard
  67: cell phone
  68: microwave
  69: oven
  70: toaster
  71: sink
  72: refrigerator
  73: book
  74: clock
  75: vase
  76: scissors
  77: teddy bear
  78: hair drier
  79: toothbrush

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=coco8.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (json):
```json
{
    "type": "dataset",
    "task": "detect",
    "name": "Example",
    "description": "COCO NDJSON example dataset",
    "url": "https://app.ultralytics.com/user/datasets/example",
    "class_names": { "0": "person", "1": "bicycle", "2": "car" },
    "bytes": 426342,
    "version": 0,
    "created_at": "2024-01-01T00:00:00Z",
    "updated_at": "2025-01-01T00:00:00Z"
}
```

---

## Open Images V7 Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/open-images-v7/

**Contents:**
- Open Images V7 Dataset
- Open Images V7 Pretrained Models
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ

Open Images V7 is a versatile and expansive dataset championed by Google. Aimed at propelling research in the realm of computer vision, it boasts a vast collection of images annotated with a plethora of data, including image-level labels, object bounding boxes, object segmentation masks, visual relationships, and localized narratives.

Watch:Object Detection using OpenImagesV7 Pretrained Model

You can use these pretrained models for inference or fine-tuning as follows.

Pretrained Model Usage Example

Open Images V7 is structured in multiple components catering to varied computer vision challenges:

Open Images V7 is a cornerstone for training and evaluating state-of-the-art models in various computer vision tasks. The dataset's broad scope and high-quality annotations make it indispensable for researchers and developers specializing in computer vision.

Some key applications include:

Ultralytics maintains an open-images-v7.yaml file that specifies the dataset paths, class names, and other configuration details required for training.

To train a YOLO26n model on the Open Images V7 dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The complete Open Images V7 dataset comprises 1,743,042 training images and 41,620 validation images, requiring approximately 561 GB of storage space upon download.

Executing the commands provided below will trigger an automatic download of the full dataset if it's not already present locally. Before running the below example it's crucial to:

Illustrations of the dataset help provide insights into its richness:

Researchers can gain invaluable insights into the array of computer vision challenges that the dataset addresses, from basic object detection to intricate relationship identification. The diversity of annotations makes Open Images V7 particularly valuable for developing models that can understand complex visual scenes.

For those employing Open Images V7 in their work, it's prudent to cite the relevant papers and acknowledge the creators:

A heartfelt acknowledgment goes out to the Google AI team for creating and maintaining the Open Images V7 dataset. For a deep dive into the dataset and its offerings, navigate to the official Open Images V7 website.

Open Images V7 is an extensive and versatile dataset created by Google, designed to advance research in computer vision. It includes image-level labels, object bounding boxes, object segmentation masks, visual relationships, and localized narratives, making it ideal for various computer vision tasks such as object detection, segmentation, and relationship detection.

To train a YOLO26 model on the Open Images V7 dataset, you can use both Python and CLI commands. Here's an example of training the YOLO26n model for 100 epochs with an image size of 640:

For more details on arguments and settings, refer to the Training page.

The Open Images V7 dataset includes approximately 9 million images with various annotations:

Ultralytics provides several YOLOv8 pretrained models for the Open Images V7 dataset, each with different sizes and performance metrics:

The Open Images V7 dataset supports a variety of computer vision tasks including:

Its comprehensive annotations and broad scope make it suitable for training and evaluating advanced machine learning models, as highlighted in practical use cases detailed in our applications section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load an Open Images Dataset V7 pretrained YOLOv8n model
model = YOLO("yolov8n-oiv7.pt")

# Run prediction
results = model.predict(source="image.jpg")

# Start training from the pretrained checkpoint
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 2 (julia):
```julia
# Predict using an Open Images Dataset V7 pretrained model
yolo detect predict source=image.jpg model=yolov8n-oiv7.pt

# Start training from an Open Images Dataset V7 pretrained checkpoint
yolo detect train data=coco8.yaml model=yolov8n-oiv7.pt epochs=100 imgsz=640
```

Example 3 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Open Images v7 dataset https://storage.googleapis.com/openimages/web/index.html by Google
# Documentation: https://docs.ultralytics.com/datasets/detect/open-images-v7/
# Example usage: yolo train data=open-images-v7.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── open-images-v7 ← downloads here (561 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: open-images-v7 # dataset root dir
train: images/train # train images (relative to 'path') 1743042 images
val: images/val # val images (relative to 'path') 41620 images
test: # test images (optional)

# Classes
names:
  0: Accordion
  1: Adhesive tape
  2: Aircraft
  3: Airplane
  4: Alarm clock
  5: Alpaca
  6: Ambulance
  7: Animal
  8: Ant
  9: Antelope
  10: Apple
  11: Armadillo
  12: Artichoke
  13: Auto part
  14: Axe
  15: Backpack
  16: Bagel
  17: Baked goods
  18: Balance beam
  19: Ball
  20: Balloon
  21: Banana
  22: Band-aid
  23: Banjo
  24: Barge
  25: Barrel
  26: Baseball bat
  27: Baseball glove
  28: Bat (Animal)
  29: Bathroom accessory
  30: Bathroom cabinet
  31: Bathtub
  32: Beaker
  33: Bear
  34: Bed
  35: Bee
  36: Beehive
  37: Beer
  38: Beetle
  39: Bell pepper
  40: Belt
  41: Bench
  42: Bicycle
  43: Bicycle helmet
  44: Bicycle wheel
  45: Bidet
  46: Billboard
  47: Billiard table
  48: Binoculars
  49: Bird
  50: Blender
  51: Blue jay
  52: Boat
  53: Bomb
  54: Book
  55: Bookcase
  56: Boot
  57: Bottle
  58: Bottle opener
  59: Bow and arrow
  60: Bowl
  61: Bowling equipment
  62: Box
  63: Boy
  64: Brassiere
  65: Bread
  66: Briefcase
  67: Broccoli
  68: Bronze sculpture
  69: Brown bear
  70: Building
  71: Bull
  72: Burrito
  73: Bus
  74: Bust
  75: Butterfly
  76: Cabbage
  77: Cabinetry
  78: Cake
  79: Cake stand
  80: Calculator
  81: Camel
  82: Camera
  83: Can opener
  84: Canary
  85: Candle
  86: Candy
  87: Cannon
  88: Canoe
  89: Cantaloupe
  90: Car
  91: Carnivore
  92: Carrot
  93: Cart
  94: Cassette deck
  95: Castle
  96: Cat
  97: Cat furniture
  98: Caterpillar
  99: Cattle
  100: Ceiling fan
  101: Cello
  102: Centipede
  103: Chainsaw
  104: Chair
  105: Cheese
  106: Cheetah
  107: Chest of drawers
  108: Chicken
  109: Chime
  110: Chisel
  111: Chopsticks
  112: Christmas tree
  113: Clock
  114: Closet
  115: Clothing
  116: Coat
  117: Cocktail
  118: Cocktail shaker
  119: Coconut
  120: Coffee
  121: Coffee cup
  122: Coffee table
  123: Coffeemaker
  124: Coin
  125: Common fig
  126: Common sunflower
  127: Computer keyboard
  128: Computer monitor
  129: Computer mouse
  130: Container
  131: Convenience store
  132: Cookie
  133: Cooking spray
  134: Corded phone
  135: Cosmetics
  136: Couch
  137: Countertop
  138: Cowboy hat
  139: Crab
  140: Cream
  141: Cricket ball
  142: Crocodile
  143: Croissant
  144: Crown
  145: Crutch
  146: Cucumber
  147: Cupboard
  148: Curtain
  149: Cutting board
  150: Dagger
  151: Dairy Product
  152: Deer
  153: Desk
  154: Dessert
  155: Diaper
  156: Dice
  157: Digital clock
  158: Dinosaur
  159: Dishwasher
  160: Dog
  161: Dog bed
  162: Doll
  163: Dolphin
  164: Door
  165: Door handle
  166: Donut
  167: Dragonfly
  168: Drawer
  169: Dress
  170: Drill (Tool)
  171: Drink
  172: Drinking straw
  173: Drum
  174: Duck
  175: Dumbbell
  176: Eagle
  177: Earrings
  178: Egg (Food)
  179: Elephant
  180: Envelope
  181: Eraser
  182: Face powder
  183: Facial tissue holder
  184: Falcon
  185: Fashion accessory
  186: Fast food
  187: Fax
  188: Fedora
  189: Filing cabinet
  190: Fire hydrant
  191: Fireplace
  192: Fish
  193: Flag
  194: Flashlight
  195: Flower
  196: Flowerpot
  197: Flute
  198: Flying disc
  199: Food
  200: Food processor
  201: Football
  202: Football helmet
  203: Footwear
  204: Fork
  205: Fountain
  206: Fox
  207: French fries
  208: French horn
  209: Frog
  210: Fruit
  211: Frying pan
  212: Furniture
  213: Garden Asparagus
  214: Gas stove
  215: Giraffe
  216: Girl
  217: Glasses
  218: Glove
  219: Goat
  220: Goggles
  221: Goldfish
  222: Golf ball
  223: Golf cart
  224: Gondola
  225: Goose
  226: Grape
  227: Grapefruit
  228: Grinder
  229: Guacamole
  230: Guitar
  231: Hair dryer
  232: Hair spray
  233: Hamburger
  234: Hammer
  235: Hamster
  236: Hand dryer
  237: Handbag
  238: Handgun
  239: Harbor seal
  240: Harmonica
  241: Harp
  242: Harpsichord
  243: Hat
  244: Headphones
  245: Heater
  246: Hedgehog
  247: Helicopter
  248: Helmet
  249: High heels
  250: Hiking equipment
  251: Hippopotamus
  252: Home appliance
  253: Honeycomb
  254: Horizontal bar
  255: Horse
  256: Hot dog
  257: House
  258: Houseplant
  259: Human arm
  260: Human beard
  261: Human body
  262: Human ear
  263: Human eye
  264: Human face
  265: Human foot
  266: Human hair
  267: Human hand
  268: Human head
  269: Human leg
  270: Human mouth
  271: Human nose
  272: Humidifier
  273: Ice cream
  274: Indoor rower
  275: Infant bed
  276: Insect
  277: Invertebrate
  278: Ipod
  279: Isopod
  280: Jacket
  281: Jacuzzi
  282: Jaguar (Animal)
  283: Jeans
  284: Jellyfish
  285: Jet ski
  286: Jug
  287: Juice
  288: Kangaroo
  289: Kettle
  290: Kitchen & dining room table
  291: Kitchen appliance
  292: Kitchen knife
  293: Kitchen utensil
  294: Kitchenware
  295: Kite
  296: Knife
  297: Koala
  298: Ladder
  299: Ladle
  300: Ladybug
  301: Lamp
  302: Land vehicle
  303: Lantern
  304: Laptop
  305: Lavender (Plant)
  306: Lemon
  307: Leopard
  308: Light bulb
  309: Light switch
  310: Lighthouse
  311: Lily
  312: Limousine
  313: Lion
  314: Lipstick
  315: Lizard
  316: Lobster
  317: Loveseat
  318: Luggage and bags
  319: Lynx
  320: Magpie
  321: Mammal
  322: Man
  323: Mango
  324: Maple
  325: Maracas
  326: Marine invertebrates
  327: Marine mammal
  328: Measuring cup
  329: Mechanical fan
  330: Medical equipment
  331: Microphone
  332: Microwave oven
  333: Milk
  334: Miniskirt
  335: Mirror
  336: Missile
  337: Mixer
  338: Mixing bowl
  339: Mobile phone
  340: Monkey
  341: Moths and butterflies
  342: Motorcycle
  343: Mouse
  344: Muffin
  345: Mug
  346: Mule
  347: Mushroom
  348: Musical instrument
  349: Musical keyboard
  350: Nail (Construction)
  351: Necklace
  352: Nightstand
  353: Oboe
  354: Office building
  355: Office supplies
  356: Orange
  357: Organ (Musical Instrument)
  358: Ostrich
  359: Otter
  360: Oven
  361: Owl
  362: Oyster
  363: Paddle
  364: Palm tree
  365: Pancake
  366: Panda
  367: Paper cutter
  368: Paper towel
  369: Parachute
  370: Parking meter
  371: Parrot
  372: Pasta
  373: Pastry
  374: Peach
  375: Pear
  376: Pen
  377: Pencil case
  378: Pencil sharpener
  379: Penguin
  380: Perfume
  381: Person
  382: Personal care
  383: Personal flotation device
  384: Piano
  385: Picnic basket
  386: Picture frame
  387: Pig
  388: Pillow
  389: Pineapple
  390: Pitcher (Container)
  391: Pizza
  392: Pizza cutter
  393: Plant
  394: Plastic bag
  395: Plate
  396: Platter
  397: Plumbing fixture
  398: Polar bear
  399: Pomegranate
  400: Popcorn
  401: Porch
  402: Porcupine
  403: Poster
  404: Potato
  405: Power plugs and sockets
  406: Pressure cooker
  407: Pretzel
  408: Printer
  409: Pumpkin
  410: Punching bag
  411: Rabbit
  412: Raccoon
  413: Racket
  414: Radish
  415: Ratchet (Device)
  416: Raven
  417: Rays and skates
  418: Red panda
  419: Refrigerator
  420: Remote control
  421: Reptile
  422: Rhinoceros
  423: Rifle
  424: Ring binder
  425: Rocket
  426: Roller skates
  427: Rose
  428: Rugby ball
  429: Ruler
  430: Salad
  431: Salt and pepper shakers
  432: Sandal
  433: Sandwich
  434: Saucer
  435: Saxophone
  436: Scale
  437: Scarf
  438: Scissors
  439: Scoreboard
  440: Scorpion
  441: Screwdriver
  442: Sculpture
  443: Sea lion
  444: Sea turtle
  445: Seafood
  446: Seahorse
  447: Seat belt
  448: Segway
  449: Serving tray
  450: Sewing machine
  451: Shark
  452: Sheep
  453: Shelf
  454: Shellfish
  455: Shirt
  456: Shorts
  457: Shotgun
  458: Shower
  459: Shrimp
  460: Sink
  461: Skateboard
  462: Ski
  463: Skirt
  464: Skull
  465: Skunk
  466: Skyscraper
  467: Slow cooker
  468: Snack
  469: Snail
  470: Snake
  471: Snowboard
  472: Snowman
  473: Snowmobile
  474: Snowplow
  475: Soap dispenser
  476: Sock
  477: Sofa bed
  478: Sombrero
  479: Sparrow
  480: Spatula
  481: Spice rack
  482: Spider
  483: Spoon
  484: Sports equipment
  485: Sports uniform
  486: Squash (Plant)
  487: Squid
  488: Squirrel
  489: Stairs
  490: Stapler
  491: Starfish
  492: Stationary bicycle
  493: Stethoscope
  494: Stool
  495: Stop sign
  496: Strawberry
  497: Street light
  498: Stretcher
  499: Studio couch
  500: Submarine
  501: Submarine sandwich
  502: Suit
  503: Suitcase
  504: Sun hat
  505: Sunglasses
  506: Surfboard
  507: Sushi
  508: Swan
  509: Swim cap
  510: Swimming pool
  511: Swimwear
  512: Sword
  513: Syringe
  514: Table
  515: Table tennis racket
  516: Tablet computer
  517: Tableware
  518: Taco
  519: Tank
  520: Tap
  521: Tart
  522: Taxi
  523: Tea
  524: Teapot
  525: Teddy bear
  526: Telephone
  527: Television
  528: Tennis ball
  529: Tennis racket
  530: Tent
  531: Tiara
  532: Tick
  533: Tie
  534: Tiger
  535: Tin can
  536: Tire
  537: Toaster
  538: Toilet
  539: Toilet paper
  540: Tomato
  541: Tool
  542: Toothbrush
  543: Torch
  544: Tortoise
  545: Towel
  546: Tower
  547: Toy
  548: Traffic light
  549: Traffic sign
  550: Train
  551: Training bench
  552: Treadmill
  553: Tree
  554: Tree house
  555: Tripod
  556: Trombone
  557: Trousers
  558: Truck
  559: Trumpet
  560: Turkey
  561: Turtle
  562: Umbrella
  563: Unicycle
  564: Van
  565: Vase
  566: Vegetable
  567: Vehicle
  568: Vehicle registration plate
  569: Violin
  570: Volleyball (Ball)
  571: Waffle
  572: Waffle iron
  573: Wall clock
  574: Wardrobe
  575: Washing machine
  576: Waste container
  577: Watch
  578: Watercraft
  579: Watermelon
  580: Weapon
  581: Whale
  582: Wheel
  583: Wheelchair
  584: Whisk
  585: Whiteboard
  586: Willow
  587: Window
  588: Window blind
  589: Wine
  590: Wine glass
  591: Wine rack
  592: Winter melon
  593: Wok
  594: Woman
  595: Wood-burning stove
  596: Woodpecker
  597: Worm
  598: Wrench
  599: Zebra
  600: Zucchini

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  import warnings

  from ultralytics.utils import LOGGER, SETTINGS, Path
  from ultralytics.utils.checks import check_requirements

  check_requirements("fiftyone")

  import fiftyone as fo
  import fiftyone.zoo as foz

  name = "open-images-v7"
  fo.config.dataset_zoo_dir = Path(SETTINGS["datasets_dir"]) / "fiftyone" / name
  fraction = 1.0  # fraction of full dataset to use
  LOGGER.warning("Open Images V7 dataset requires at least **561 GB of free space. Starting download...")
  for split in "train", "validation":  # 1743042 train, 41620 val images
      train = split == "train"

      # Load Open Images dataset
      dataset = foz.load_zoo_dataset(
          name,
          split=split,
          label_types=["detections"],
          max_samples=round((1743042 if train else 41620) * fraction),
      )

      # Define classes
      if train:
          classes = dataset.default_classes  # all classes
          # classes = dataset.distinct('ground_truth.detections.label')  # only observed classes

      # Export to YOLO format
      with warnings.catch_warnings():
          warnings.filterwarnings("ignore", category=UserWarning, module="fiftyone.utils.yolo")
          dataset.export(
              export_dir=str(Path(SETTINGS["datasets_dir"]) / name),
              dataset_type=fo.types.YOLOv5Dataset,
              label_field="ground_truth",
              split="val" if split == "validation" else split,
              classes=classes,
              overwrite=train,
          )
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the Open Images V7 dataset
results = model.train(data="open-images-v7.yaml", epochs=100, imgsz=640)
```

---

## Oriented Bounding Box (OBB) Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/obb/

**Contents:**
- Oriented Bounding Box (OBB) Datasets Overview
- Supported OBB Dataset Formats
  - YOLO OBB Format
  - Dataset YAML format
- Usage
- Supported Datasets
  - Incorporating your own OBB dataset
- Convert Label Formats
  - DOTA Dataset Format to YOLO OBB Format
- FAQ

Training a precise object detection model with oriented bounding boxes (OBB) requires a thorough dataset. This guide explains the various OBB dataset formats compatible with Ultralytics YOLO models, offering insights into their structure, application, and methods for format conversions.

The YOLO OBB format designates bounding boxes by their four corner points with coordinates normalized between 0 and 1. It follows this format:

Internally, YOLO processes losses and outputs in the xywhr format, which represents the bounding box's center point (xy), width, height, and rotation.

An example of a *.txt label file for the above image, which contains an object of class 0 in OBB format, could look like:

The Ultralytics framework uses a YAML file format to define the dataset and model configuration for training OBB models. Here is an example of the YAML format used for defining an OBB dataset:

ultralytics/cfg/datasets/dota8.yaml

To train a model using these OBB formats:

Currently, the following datasets with oriented bounding boxes are supported:

For those looking to introduce their own datasets with oriented bounding boxes, ensure compatibility with the "YOLO OBB format" mentioned above. Convert your annotations to this required format and detail the paths, classes, and class names in a corresponding YAML configuration file.

Transitioning labels from the DOTA dataset format to the YOLO OBB format can be achieved with this script:

This conversion mechanism is instrumental for datasets in the DOTA format, ensuring alignment with the Ultralytics YOLO OBB format.

It's imperative to validate the compatibility of the dataset with your model and adhere to the necessary format conventions. Properly structured datasets are pivotal for training efficient object detection models with oriented bounding boxes.

Oriented Bounding Boxes (OBB) are a type of bounding box annotation where the box can be rotated to align more closely with the object being detected, rather than just being axis-aligned. This is particularly useful in aerial or satellite imagery where objects might not be aligned with the image axes. In Ultralytics YOLO models, OBBs are represented by their four corner points in the YOLO OBB format. This allows for more accurate object detection since the bounding boxes can rotate to fit the objects better.

You can convert DOTA dataset labels to YOLO OBB format using the convert_dota_to_yolo_obb function from Ultralytics. This conversion ensures compatibility with the Ultralytics YOLO models, enabling you to leverage the OBB capabilities for enhanced object detection. Here's a quick example:

This script will reformat your DOTA annotations into a YOLO-compatible format.

Training a YOLO26 model with OBBs involves ensuring your dataset is in the YOLO OBB format and then using the Ultralytics API to train the model. Here's an example in both Python and CLI:

This ensures your model leverages the detailed OBB annotations for improved detection accuracy.

Currently, Ultralytics supports the following datasets for OBB training:

These datasets are tailored for scenarios where OBBs offer a significant advantage, such as aerial and satellite image analysis.

Yes, you can use your own dataset with oriented bounding boxes for YOLO26 training. Ensure your dataset annotations are converted to the YOLO OBB format, which involves defining bounding boxes by their four corner points. You can then create a YAML configuration file specifying the dataset paths, classes, and other necessary details. For more information on creating and configuring your datasets, refer to the Supported Datasets section.

**Examples:**

Example 1 (unknown):
```unknown
class_index x1 y1 x2 y2 x3 y3 x4 y4
```

Example 2 (unknown):
```unknown
0 0.780811 0.743961 0.782371 0.74686 0.777691 0.752174 0.776131 0.749758
```

Example 3 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# DOTA8 dataset (8 images from the DOTAv1 split) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/obb/dota8/
# Example usage: yolo train model=yolov8n-obb.pt data=dota8.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── dota8 ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: dota8 # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images

# Classes for DOTA 1.0
names:
  0: plane
  1: ship
  2: storage tank
  3: baseball diamond
  4: tennis court
  5: basketball court
  6: ground track field
  7: harbor
  8: bridge
  9: large vehicle
  10: small vehicle
  11: helicopter
  12: roundabout
  13: soccer ball field
  14: swimming pool

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/dota8.zip
```

Example 4 (python):
```python
from ultralytics import YOLO

# Create a new YOLO26n-OBB model from scratch
model = YOLO("yolo26n-obb.yaml")

# Train the model on the DOTAv1 dataset
results = model.train(data="DOTAv1.yaml", epochs=100, imgsz=1024)
```

---

## Package Segmentation Dataset

**URL:** https://docs.ultralytics.com/datasets/segment/package-seg/

**Contents:**
- Package Segmentation Dataset
- Dataset Structure
- Applications
  - Smart Warehouses and Logistics
  - Quality Control and Damage Detection
- Dataset YAML
- Usage
- Sample Data and Annotations
- Benefits of Using YOLO26 for Package Segmentation
- Citations and Acknowledgments

The Package Segmentation Dataset, available on Roboflow Universe, is a curated collection of images specifically tailored for tasks related to package segmentation within the field of computer vision. This dataset is designed to assist researchers, developers, and enthusiasts working on projects involving package identification, sorting, and handling, primarily focusing on image segmentation tasks.

Watch: Train Package Segmentation Model using Ultralytics YOLO26 | Industrial Packages 🎉

Containing a diverse set of images showcasing various packages in different contexts and environments, the dataset serves as a valuable resource for training and evaluating segmentation models. Whether you are engaged in logistics, warehouse automation, or any application requiring precise package analysis, the Package Segmentation Dataset provides a targeted and comprehensive set of images to enhance the performance of your computer vision algorithms. Explore more datasets for segmentation tasks on our datasets overview page.

The distribution of data in the Package Segmentation Dataset is structured as follows:

Package segmentation, facilitated by the Package Segmentation Dataset, is crucial for optimizing logistics, enhancing last-mile delivery, improving manufacturing quality control, and contributing to smart city solutions. From e-commerce to security applications, this dataset is a key resource, fostering innovation in computer vision for diverse and efficient package analysis applications.

In modern warehouses, vision AI solutions can streamline operations by automating package identification and sorting. Computer vision models trained on this dataset can quickly detect and segment packages in real-time, even in challenging environments with dim lighting or cluttered spaces. This leads to faster processing times, reduced errors, and improved overall efficiency in logistics operations.

Package segmentation models can be used to identify damaged packages by analyzing their shape and appearance. By detecting irregularities or deformations in package outlines, these models help ensure that only intact packages proceed through the supply chain, reducing customer complaints and return rates. This is a key aspect of quality control in manufacturing and is vital for maintaining product integrity.

A YAML (Yet Another Markup Language) file defines the dataset configuration, including paths, classes, and other essential details. For the Package Segmentation dataset, the package-seg.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/package-seg.yaml.

ultralytics/cfg/datasets/package-seg.yaml

To train an Ultralytics YOLO26n model on the Package Segmentation dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The Package Segmentation dataset comprises a varied collection of images captured from multiple perspectives. Below are instances of data from the dataset, accompanied by their respective segmentation masks:

Ultralytics YOLO26 offers several advantages for package segmentation tasks:

Speed and Accuracy Balance: YOLO26 achieves high precision and efficiency, making it ideal for real-time inference in fast-paced logistics environments. It provides a strong balance compared to models like YOLOv8.

Adaptability: Models trained with YOLO26 can adapt to various warehouse conditions, from dim lighting to cluttered spaces, ensuring robust performance.

Scalability: During peak periods like holiday seasons, YOLO26 models can efficiently scale to handle increased package volumes without compromising performance or accuracy.

Integration Capabilities: YOLO26 can be easily integrated with existing warehouse management systems and deployed across various platforms using formats like ONNX or TensorRT, facilitating end-to-end automated solutions.

If you integrate the Package Segmentation dataset into your research or development initiatives, please cite the source appropriately:

We express our gratitude to the creators of the Package Segmentation dataset for their contribution to the computer vision community. For further exploration of datasets and model training, consider visiting our Ultralytics Datasets page and our guide on model training tips.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Package-seg dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/segment/package-seg/
# Example usage: yolo train data=package-seg.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── package-seg ← downloads here (103 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: package-seg # dataset root dir
train: images/train # train images (relative to 'path') 1920 images
val: images/val # val images (relative to 'path') 89 images
test: images/test # test images (relative to 'path') 188 images

# Classes
names:
  0: package

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/package-seg.zip
```

Example 2 (go):
```go
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-seg.pt")  # load a pretrained segmentation model (recommended for training)

# Train the model on the Package Segmentation dataset
results = model.train(data="package-seg.yaml", epochs=100, imgsz=640)

# Validate the model
results = model.val()

# Perform inference on an image
results = model("path/to/image.jpg")
```

Example 3 (julia):
```julia
# Load a pretrained segmentation model and start training
yolo segment train data=package-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640

# Resume training from the last checkpoint
yolo segment train data=package-seg.yaml model=path/to/last.pt resume=True

# Validate the trained model
yolo segment val data=package-seg.yaml model=path/to/best.pt

# Perform inference using the trained model
yolo segment predict model=path/to/best.pt source=path/to/image.jpg
```

Example 4 (swift):
```swift
@misc{ factory_package_dataset,
    title = { factory_package Dataset },
    type = { Open Source Dataset },
    author = { factorypackage },
    url = { https://universe.roboflow.com/factorypackage/factory_package },
    journal = { Roboflow Universe },
    publisher = { Roboflow },
    year = { 2024 },
    month = { jan },
    note = { visited on 2024-01-24 },
}
```

---

## Panoramica dei dataset

**URL:** https://docs.ultralytics.com/it/datasets/

**Contents:**
- Panoramica dei dataset
- Rilevamento di oggetti
- Segmentazione delle istanze
- Stima della posa
- Classificazione
- Oriented Bounding Boxes (OBB)
- Multi-Object Tracking
- Contribuisci nuovi dataset
  - Passaggi per contribuire con un nuovo dataset
  - Codice di esempio per ottimizzare e comprimere un dataset

Ultralytics fornisce supporto per vari set di dati per facilitare attività di computer vision come il rilevamento, la segmentazione di istanze, la stima della posa, la classificazione e il tracciamento multi-oggetto. Di seguito è riportato un elenco dei principali set di dati Ultralytics, seguito da un riepilogo di ciascuna attività di computer vision e dei rispettivi set di dati.

Guarda: Panoramica dei set di dati Ultralytics

Il rilevamento di oggetti tramite bounding box è una tecnica di computer vision che prevede il rilevamento e la localizzazione di oggetti in un'immagine disegnando un riquadro di delimitazione attorno a ciascun oggetto.

La segmentazione delle istanze è una tecnica di visione artificiale che implica l'identificazione e la localizzazione degli oggetti in un'immagine a livello di pixel. A differenza della segmentazione semantica che classifica solo ogni pixel, la segmentazione delle istanze distingue tra diverse istanze della stessa classe.

La stima della posa è una tecnica utilizzata per determinare la posa dell'oggetto rispetto alla telecamera o al sistema di coordinate del mondo. Ciò comporta l'identificazione di punti chiave o articolazioni sugli oggetti, in particolare umani o animali.

La classificazione delle immagini è un'attività di computer vision che implica la categorizzazione di un'immagine in una o più classi o categorie predefinite in base al suo contenuto visivo.

Gli Oriented Bounding Boxes (OBB) sono un metodo di computer vision per rilevare oggetti angolati nelle immagini utilizzando bounding box ruotati, spesso applicato a immagini aeree e satellitari. A differenza dei bounding box tradizionali, gli OBB possono adattarsi meglio a oggetti con orientamenti diversi.

Il tracciamento multi-oggetto è una tecnica di visione artificiale che prevede il rilevamento e il tracciamento di più oggetti nel tempo in una sequenza video. Questa attività estende il rilevamento degli oggetti mantenendo identità coerenti degli oggetti attraverso i fotogrammi.

La contribuzione di un nuovo dataset prevede diversi passaggi per garantire che si allinei bene con l'infrastruttura esistente. Di seguito sono riportati i passaggi necessari:

Guarda: Come Contribuire ai Dataset Ultralytics

Organizza il Dataset: Disponi il tuo dataset nella struttura di cartelle corretta. Dovresti avere images/ e labels/ directory di livello superiore e, all'interno di ciascuna, una train/ e val/ sottodirectory.

Crea un data.yaml File: Nella directory principale del tuo dataset, crea un data.yaml file che descriva il dataset, le classi e altre informazioni necessarie.

Ottimizza e comprimi in formato Zip un dataset

Seguendo questi passaggi, puoi contribuire con un nuovo dataset che si integra bene con la struttura esistente di Ultralytics.

Ultralytics supporta un'ampia varietà di set di dati per il rilevamento di oggetti, tra cui:

Questi dataset facilitano l'addestramento di modelli Ultralytics YOLO robusti per diverse applicazioni di object detection.

La contribuzione di un nuovo dataset prevede diversi passaggi:

Visita Contribuisci con nuovi dataset per una guida completa.

La Piattaforma Ultralytics offre potenti funzionalità per la gestione e l'analisi dei dataset, tra cui:

La piattaforma semplifica la transizione dalla gestione dei dataset all'addestramento dei modelli, rendendo l'intero processo più efficiente. Scopri di più sui Dataset della Piattaforma Ultralytics.

I modelli Ultralytics YOLO offrono diverse caratteristiche uniche per le attività di computer vision:

Scopri di più sui modelli YOLO nella pagina Modelli Ultralytics.

Per ottimizzare e comprimere un set di dati utilizzando gli strumenti Ultralytics, segui questo codice di esempio:

Ottimizza e comprimi in formato Zip un dataset

Questo processo aiuta a ridurre le dimensioni del dataset per uno storage più efficiente e velocità di download più elevate. Scopri di più su come ottimizzare e comprimere un dataset.

**Examples:**

Example 1 (unknown):
```unknown
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Example 2 (python):
```python
from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("path/to/dataset")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)
```

Example 3 (python):
```python
from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("path/to/dataset")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)
```

---

## Pose Estimation Datasets Overview

**URL:** https://docs.ultralytics.com/datasets/pose/

**Contents:**
- Pose Estimation Datasets Overview
- Supported Dataset Formats
  - Ultralytics YOLO format
  - Dataset YAML format
- Usage
- Supported Datasets
  - COCO-Pose
  - COCO8-Pose
  - Dog-Pose
  - Hand Keypoints

The dataset label format used for training YOLO pose models is as follows:

Here is an example of the label format for a pose estimation task:

Format with 2D keypoints

Format with 3D keypoints (includes visibility per point)

In this format, <class-index> is the index of the class for the object, <x> <y> <width> <height> are the normalized coordinates of the bounding box, and <px1> <py1> <px2> <py2> ... <pxn> <pyn> are the normalized keypoint coordinates. The visibility channel is optional but useful for datasets that annotate occlusion.

The Ultralytics framework uses a YAML file format to define the dataset and model configuration for training pose estimation models. Here is an example of the YAML format used for defining a pose dataset:

ultralytics/cfg/datasets/coco8-pose.yaml

The train and val fields specify the paths to the directories containing the training and validation images, respectively.

names is a dictionary of class names. The order of the names should match the order of the object class indices in the YOLO dataset files.

(Optional) if the points are symmetric then need flip_idx, like left-right side of human or face. For example if we assume five keypoints of facial landmark: [left eye, right eye, nose, left mouth, right mouth], and the original index is [0, 1, 2, 3, 4], then flip_idx is [1, 0, 2, 4, 3] (just exchange the left-right index, i.e. 0-1 and 3-4, and do not modify others like nose in this example).

This section outlines the datasets that are compatible with Ultralytics YOLO format and can be used for training pose estimation models:

If you have your own dataset and would like to use it for training pose estimation models with Ultralytics YOLO format, ensure that it follows the format specified above under "Ultralytics YOLO format". Convert your annotations to the required format and specify the paths, number of classes, and class names in the YAML configuration file.

Ultralytics provides a convenient conversion tool to convert labels from the popular COCO dataset format to YOLO format:

This conversion tool can be used to convert the COCO dataset or any dataset in the COCO format to the Ultralytics YOLO format. The use_keypoints parameter specifies whether to include keypoints (for pose estimation) in the converted labels.

The Ultralytics YOLO format for pose estimation datasets involves labeling each image with a corresponding text file. Each row of the text file stores information about an object instance:

For 2D poses, keypoints include pixel coordinates. For 3D, each keypoint also has a visibility flag. For more details, see Ultralytics YOLO format.

To use the COCO-Pose dataset with Ultralytics YOLO:

Use the configuration file for training:

For more information, visit COCO-Pose and train sections.

Use the configuration file to train your model:

For complete steps, check the Adding your own dataset section.

The dataset YAML file in Ultralytics YOLO defines the dataset and model configuration for training. It specifies paths to training, validation, and test images, keypoint shapes, class names, and other configuration options. This structured format helps streamline dataset management and model training. Here is an example YAML format:

Read more about creating YAML configuration files in Dataset YAML format.

Ultralytics provides a conversion tool to convert COCO dataset labels to the YOLO format, including keypoint information:

This tool helps seamlessly integrate COCO datasets into YOLO projects. For details, refer to the Conversion Tool section and the data preprocessing guide.

**Examples:**

Example 1 (typescript):
```typescript
<class-index> <x> <y> <width> <height> <px1> <py1> <px2> <py2> ... <pxn> <pyn>
```

Example 2 (typescript):
```typescript
<class-index> <x> <y> <width> <height> <px1> <py1> <p1-visibility> <px2> <py2> <p2-visibility> <pxn> <pyn> <pn-visibility>
```

Example 3 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# COCO8-pose dataset (first 8 images from COCO train2017) by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/pose/coco8-pose/
# Example usage: yolo train data=coco8-pose.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── coco8-pose ← downloads here (1 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: coco8-pose # dataset root dir
train: images/train # train images (relative to 'path') 4 images
val: images/val # val images (relative to 'path') 4 images
test: # test images (optional)

# Keypoints
kpt_shape: [17, 3] # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
flip_idx: [0, 2, 1, 4, 3, 6, 5, 8, 7, 10, 9, 12, 11, 14, 13, 16, 15]

# Classes
names:
  0: person

# Keypoint names per class
kpt_names:
  0:
    - nose
    - left_eye
    - right_eye
    - left_ear
    - right_ear
    - left_shoulder
    - right_shoulder
    - left_elbow
    - right_elbow
    - left_wrist
    - right_wrist
    - left_hip
    - right_hip
    - left_knee
    - right_knee
    - left_ankle
    - right_ankle

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/coco8-pose.zip
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="coco8-pose.yaml", epochs=100, imgsz=640)
```

---

## Roboflow 100 Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/roboflow-100/

**Contents:**
- Roboflow 100 Dataset
- Key Features
- Dataset Structure
- Benchmarking
- Applications
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Roboflow 100 dataset, and why is it significant for object detection?

Roboflow 100, sponsored by Intel, is a groundbreaking object detection benchmark dataset. It includes 100 diverse datasets sampled from over 90,000 public datasets available on Roboflow Universe. This benchmark is specifically designed to test the adaptability of computer vision models, like Ultralytics YOLO models, to various domains, including healthcare, aerial imagery, and video games.

Ultralytics offers two licensing options to accommodate different use cases:

The Roboflow 100 dataset is organized into seven categories, each containing a unique collection of datasets, images, and classes:

This structure provides a diverse and extensive testing ground for object detection models, reflecting a wide array of real-world application scenarios found in various Ultralytics Solutions.

Dataset benchmarking involves evaluating the performance of machine learning models on specific datasets using standardized metrics. Common metrics include accuracy, mean Average Precision (mAP), and F1-score. You can learn more about these in our YOLO Performance Metrics guide.

Benchmarking results using the provided script will be stored in the ultralytics-benchmarks/ directory, specifically in evaluation.txt.

The following script demonstrates how to programmatically benchmark an Ultralytics YOLO model (e.g., YOLO26n) on all 100 datasets within the Roboflow 100 benchmark using the RF100Benchmark class.

Roboflow 100 is invaluable for various applications related to computer vision and deep learning. Researchers and engineers can leverage this benchmark to:

For more ideas and inspiration on real-world applications, explore our guides on practical projects or check out Ultralytics Platform for streamlined model training and deployment.

The Roboflow 100 dataset, including metadata and download links, is available on the official Roboflow 100 GitHub repository. You can access and utilize the dataset directly from there for your benchmarking needs. The Ultralytics RF100Benchmark utility simplifies the process of downloading and preparing these datasets for use with Ultralytics models.

Roboflow 100 consists of datasets with diverse images captured from various angles and domains. Below are examples of annotated images included in the RF100 benchmark, showcasing the variety of objects and scenes. Techniques like data augmentation can further enhance the diversity during training.

The diversity seen in the Roboflow 100 benchmark represents a significant advancement from traditional benchmarks, which often focus on optimizing a single metric within a limited domain. This comprehensive approach aids in developing more robust and versatile computer vision models capable of performing well across a multitude of different scenarios.

If you use the Roboflow 100 dataset in your research or development work, please cite the original paper:

We extend our gratitude to the Roboflow team and all contributors for their significant efforts in creating and maintaining the Roboflow 100 dataset as a valuable resource for the computer vision community.

If you are interested in exploring more datasets to enhance your object detection and machine learning projects, feel free to visit our comprehensive dataset collection, which includes a variety of other detection datasets.

The Roboflow 100 dataset is a benchmark for object detection models. It comprises 100 diverse datasets sourced from Roboflow Universe, covering domains like healthcare, aerial imagery, and video games. Its significance lies in providing a standardized way to test model adaptability and robustness across a wide range of real-world scenarios, moving beyond traditional, often domain-limited, benchmarks.

The Roboflow 100 dataset spans seven diverse domains, offering unique challenges for object detection models:

This variety makes RF100 an excellent resource for assessing the generalizability of computer vision models.

When using the Roboflow 100 dataset, please cite the original paper to give credit to the creators. Here is the recommended BibTeX citation:

For further exploration, consider visiting our comprehensive dataset collection or browsing other detection datasets compatible with Ultralytics models.

**Examples:**

Example 1 (python):
```python
import os
import shutil
from pathlib import Path

from ultralytics.utils.benchmarks import RF100Benchmark

# Initialize RF100Benchmark and set API key
benchmark = RF100Benchmark()
benchmark.set_key(api_key="YOUR_ROBOFLOW_API_KEY")

# Parse dataset and define file paths
names, cfg_yamls = benchmark.parse_dataset()
val_log_file = Path("ultralytics-benchmarks") / "validation.txt"
eval_log_file = Path("ultralytics-benchmarks") / "evaluation.txt"

# Run benchmarks on each dataset in RF100
for ind, path in enumerate(cfg_yamls):
    path = Path(path)
    if path.exists():
        # Fix YAML file and run training
        benchmark.fix_yaml(str(path))
        os.system(f"yolo detect train data={path} model=yolo26s.pt epochs=1 batch=16")

        # Run validation and evaluate
        os.system(f"yolo detect val data={path} model=runs/detect/train/weights/best.pt > {val_log_file} 2>&1")
        benchmark.evaluate(str(path), str(val_log_file), str(eval_log_file), ind)

        # Remove the 'runs' directory
        runs_dir = Path.cwd() / "runs"
        shutil.rmtree(runs_dir)
    else:
        print("YAML file path does not exist")
        continue

print("RF100 Benchmarking completed!")
```

Example 2 (css):
```css
@misc{rf100benchmark,
    Author = {Floriana Ciaglia and Francesco Saverio Zuppichini and Paul Guerrie and Mark McQuade and Jacob Solawetz},
    Title = {Roboflow 100: A Rich, Multi-Domain Object Detection Benchmark},
    Year = {2022},
    Eprint = {arXiv:2211.13523},
    url = {https://arxiv.org/abs/2211.13523}
}
```

Example 3 (css):
```css
@misc{rf100benchmark,
    Author = {Floriana Ciaglia and Francesco Saverio Zuppichini and Paul Guerrie and Mark McQuade and Jacob Solawetz},
    Title = {Roboflow 100: A Rich, Multi-Domain Object Detection Benchmark},
    Year = {2022},
    Eprint = {arXiv:2211.13523},
    url = {https://arxiv.org/abs/2211.13523}
}
```

---

## Signature Detection Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/signature/

**Contents:**
- Signature Detection Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the Signature Detection Dataset, and how can it be used?
  - How do I train a YOLO26n model on the Signature Detection Dataset?

This dataset focuses on detecting human written signatures within documents. It includes a variety of document types with annotated signatures, providing valuable insights for applications in document verification and fraud detection. Essential for training computer vision algorithms, this dataset aids in identifying signatures in various document formats, supporting research and practical applications in document analysis.

The signature detection dataset is split into two subsets:

This dataset can be applied in various computer vision tasks such as object detection, object tracking, and document analysis. Specifically, it can be used to train and evaluate models for identifying signatures in documents, which has significant applications in:

Additionally, it serves as a valuable resource for educational purposes, enabling students and researchers to study signature characteristics across different document types.

A YAML (Yet Another Markup Language) file defines the dataset configuration, including paths and classes information. For the signature detection dataset, the signature.yaml file is located at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/signature.yaml.

ultralytics/cfg/datasets/signature.yaml

To train a YOLO26n model on the signature detection dataset for 100 epochs with an image size of 640, use the provided code samples. For a comprehensive list of available parameters, refer to the model's Training page.

The signature detection dataset comprises a wide variety of images showcasing different document types and annotated signatures. Below are examples of images from the dataset, each accompanied by its corresponding annotations.

This example illustrates the variety and complexity of images in the signature Detection Dataset, emphasizing the benefits of including mosaicing during the training process.

The dataset has been released available under the AGPL-3.0 License.

The Signature Detection Dataset is a collection of annotated images aimed at detecting human signatures within various document types. It can be applied in computer vision tasks such as object detection and tracking, primarily for document verification, fraud detection, and archival research. This dataset helps train models to recognize signatures in different contexts, making it valuable for both research and practical applications in smart document analysis.

To train a YOLO26n model on the Signature Detection Dataset, follow these steps:

For more details, refer to the Training page.

The Signature Detection Dataset can be used for:

To perform inference using a model trained on the Signature Detection Dataset, follow these steps:

The Signature Detection Dataset is divided into two subsets:

For detailed information, you can refer to the Dataset Structure section. Additionally, view the complete dataset configuration in the signature.yaml file located at signature.yaml.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Signature dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/detect/signature/
# Example usage: yolo train data=signature.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── signature ← downloads here (11.3 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: signature # dataset root dir
train: images/train # train images (relative to 'path') 143 images
val: images/val # val images (relative to 'path') 35 images

# Classes
names:
  0: signature

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/signature.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="signature.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=signature.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load a signature-detection fine-tuned model

# Inference using the model
results = model.predict("https://ultralytics.com/assets/signature-s.mp4", conf=0.75)
```

---

## SKU-110k Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/sku-110k/

**Contents:**
- SKU-110k Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the SKU-110k dataset and why is it important for object detection?

The SKU-110k dataset is a collection of densely packed retail shelf images, designed to support research in object detection tasks. Developed by Eran Goldman et al., the dataset contains over 110,000 unique store keeping unit (SKU) categories with densely packed objects, often looking similar or even identical, positioned in proximity.

Watch: How to Train YOLOv10 on SKU-110k Dataset using Ultralytics | Retail Dataset

The SKU-110k dataset is organized into three main subsets:

The SKU-110k dataset is widely used for training and evaluating deep learning models in object detection tasks, especially in densely packed scenes such as retail shelf displays. Its applications include:

The dataset's diverse set of SKU categories and densely packed object arrangements make it a valuable resource for researchers and practitioners in the field of computer vision.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. For the case of the SKU-110K dataset, the SKU-110K.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/SKU-110K.yaml.

ultralytics/cfg/datasets/SKU-110K.yaml

To train a YOLO26n model on the SKU-110K dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The SKU-110k dataset contains a diverse set of retail shelf images with densely packed objects, providing rich context for object detection tasks. Here are some examples of data from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the data in the SKU-110k dataset and highlights the importance of high-quality data for object detection tasks. The dense arrangement of products presents unique challenges for detection algorithms, making this dataset particularly valuable for developing robust retail-focused computer vision solutions.

If you use the SKU-110k dataset in your research or development work, please cite the following paper:

We would like to acknowledge Eran Goldman et al. for creating and maintaining the SKU-110k dataset as a valuable resource for the computer vision research community. For more information about the SKU-110k dataset and its creators, visit the SKU-110k dataset GitHub repository.

The SKU-110k dataset consists of densely packed retail shelf images designed to aid research in object detection tasks. Developed by Eran Goldman et al., it includes over 110,000 unique SKU categories. Its importance lies in its ability to challenge state-of-the-art object detectors with diverse object appearances and proximity, making it an invaluable resource for researchers and practitioners in computer vision. Learn more about the dataset's structure and applications in our SKU-110k Dataset section.

Training a YOLO26 model on the SKU-110k dataset is straightforward. Here's an example to train a YOLO26n model for 100 epochs with an image size of 640:

For a comprehensive list of available arguments, refer to the model Training page.

The SKU-110k dataset is organized into three main subsets:

Refer to the Dataset Structure section for more details.

The SKU-110k dataset configuration is defined in a YAML file, which includes details about the dataset's paths, classes, and other relevant information. The SKU-110K.yaml file is maintained at SKU-110K.yaml. For example, you can train a model using this configuration as shown in our Usage section.

The SKU-110k dataset features images of store shelves from around the world, showcasing densely packed objects that pose significant challenges for object detectors:

These features make the SKU-110k dataset particularly valuable for training and evaluating deep learning models in object detection tasks. For more details, see the Key Features section.

If you use the SKU-110k dataset in your research or development work, please cite the following paper:

More information about the dataset can be found in the Citations and Acknowledgments section.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# SKU-110K retail items dataset https://github.com/eg4000/SKU110K_CVPR19 by Trax Retail
# Documentation: https://docs.ultralytics.com/datasets/detect/sku-110k/
# Example usage: yolo train data=SKU-110K.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── SKU-110K ← downloads here (13.6 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: SKU-110K # dataset root dir
train: train.txt # train images (relative to 'path') 8219 images
val: val.txt # val images (relative to 'path') 588 images
test: test.txt # test images (optional) 2936 images

# Classes
names:
  0: object

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  import shutil
  from pathlib import Path

  import numpy as np
  import polars as pl

  from ultralytics.utils import TQDM
  from ultralytics.utils.downloads import download
  from ultralytics.utils.ops import xyxy2xywh

  # Download
  dir = Path(yaml["path"])  # dataset root dir
  parent = Path(dir.parent)  # download dir
  urls = ["http://trax-geometry.s3.amazonaws.com/cvpr_challenge/SKU110K_fixed.tar.gz"]
  download(urls, dir=parent)

  # Rename directories
  if dir.exists():
      shutil.rmtree(dir)
  (parent / "SKU110K_fixed").rename(dir)  # rename dir
  (dir / "labels").mkdir(parents=True, exist_ok=True)  # create labels dir

  # Convert labels
  names = "image", "x1", "y1", "x2", "y2", "class", "image_width", "image_height"  # column names
  for d in "annotations_train.csv", "annotations_val.csv", "annotations_test.csv":
      x = pl.read_csv(dir / "annotations" / d, has_header=False, new_columns=names, infer_schema_length=None).to_numpy()  # annotations
      images, unique_images = x[:, 0], np.unique(x[:, 0])
      with open((dir / d).with_suffix(".txt").__str__().replace("annotations_", ""), "w", encoding="utf-8") as f:
          f.writelines(f"./images/{s}\n" for s in unique_images)
      for im in TQDM(unique_images, desc=f"Converting {dir / d}"):
          cls = 0  # single-class dataset
          with open((dir / "labels" / im).with_suffix(".txt"), "a", encoding="utf-8") as f:
              for r in x[images == im]:
                  w, h = r[6], r[7]  # image width, height
                  xywh = xyxy2xywh(np.array([[r[1] / w, r[2] / h, r[3] / w, r[4] / h]]))[0]  # instance
                  f.write(f"{cls} {xywh[0]:.5f} {xywh[1]:.5f} {xywh[2]:.5f} {xywh[3]:.5f}\n")  # write label
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="SKU-110K.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=SKU-110K.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@inproceedings{goldman2019dense,
  author    = {Eran Goldman and Roei Herzig and Aviv Eisenschtat and Jacob Goldberger and Tal Hassner},
  title     = {Precise Detection in Densely Packed Scenes},
  booktitle = {Proc. Conf. Comput. Vision Pattern Recognition (CVPR)},
  year      = {2019}
}
```

---

## Tiger-Pose Dataset

**URL:** https://docs.ultralytics.com/datasets/pose/tiger-pose/

**Contents:**
- Tiger-Pose Dataset
- Introduction
- Dataset Structure
- Dataset YAML
- Usage
- Sample Images and Annotations
- Inference Example
- Citations and Acknowledgments
- FAQ
  - What is the Ultralytics Tiger-Pose dataset used for?

Ultralytics introduces the Tiger-Pose dataset, a versatile collection designed for pose estimation tasks. This dataset comprises 263 images sourced from a YouTube video, with 210 images allocated for training and 53 for validation. It serves as an excellent resource for testing and troubleshooting pose estimation algorithms.

Despite its manageable training split of 210 images, the Tiger-Pose dataset offers diversity, making it suitable for assessing training pipelines, identifying potential errors, and serving as a valuable preliminary step before working with larger datasets for pose estimation.

This dataset is intended for use with Ultralytics Platform and YOLO26.

Watch: Train YOLO26 Pose Model on Tiger-Pose Dataset Using Ultralytics Platform

A YAML (Yet Another Markup Language) file serves as the means to specify the configuration details of a dataset. It encompasses crucial data such as file paths, class definitions, and other pertinent information. Specifically, for the tiger-pose.yaml file, you can check Ultralytics Tiger-Pose Dataset Configuration File.

ultralytics/cfg/datasets/tiger-pose.yaml

To train a YOLO26n-pose model on the Tiger-Pose dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

Here are some examples of images from the Tiger-Pose dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the Tiger-Pose dataset and the benefits of using mosaicing during the training process.

The dataset has been released available under the AGPL-3.0 License.

The Ultralytics Tiger-Pose dataset is designed for pose estimation tasks, consisting of 263 images sourced from a YouTube video. The dataset is divided into 210 training images and 53 validation images. It is particularly useful for testing, training, and refining pose estimation algorithms using Ultralytics Platform and YOLO26.

To train a YOLO26n-pose model on the Tiger-Pose dataset for 100 epochs with an image size of 640, use the following code snippets. For more details, visit the Training page:

The tiger-pose.yaml file is used to specify the configuration details of the Tiger-Pose dataset. It includes crucial data such as file paths and class definitions. To see the exact configuration, you can check out the Ultralytics Tiger-Pose Dataset Configuration File.

To perform inference using a YOLO26 model trained on the Tiger-Pose dataset, you can use the following code snippets. For a detailed guide, visit the Prediction page:

The Tiger-Pose dataset, despite its manageable size of 210 images for training, provides a diverse collection of images that are ideal for testing pose estimation pipelines. The dataset helps identify potential errors and acts as a preliminary step before working with larger datasets. Additionally, the dataset supports the training and refinement of pose estimation algorithms using advanced tools like Ultralytics Platform and YOLO26, enhancing model performance and accuracy.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# Tiger Pose dataset by Ultralytics
# Documentation: https://docs.ultralytics.com/datasets/pose/tiger-pose/
# Example usage: yolo train data=tiger-pose.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── tiger-pose ← downloads here (49.8 MB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: tiger-pose # dataset root dir
train: images/train # train images (relative to 'path') 210 images
val: images/val # val images (relative to 'path') 53 images

# Keypoints
kpt_shape: [12, 2] # number of keypoints, number of dims (2 for x,y or 3 for x,y,visible)
flip_idx: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# Classes
names:
  0: tiger

# Keypoint names per class
kpt_names:
  0:
    - nose
    - head
    - withers
    - tail_base
    - right_hind_hock
    - right_hind_paw
    - left_hind_paw
    - left_hind_hock
    - right_front_wrist
    - right_front_paw
    - left_front_wrist
    - left_front_paw

# Download script/URL (optional)
download: https://github.com/ultralytics/assets/releases/download/v0.0.0/tiger-pose.zip
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n-pose.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="tiger-pose.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo pose train data=tiger-pose.yaml model=yolo26n-pose.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("path/to/best.pt")  # load a tiger-pose trained model

# Run inference
results = model.predict(source="https://youtu.be/MIBAT6BGE6U", show=True)
```

---

## VisDrone Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/visdrone/

**Contents:**
- VisDrone Dataset
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the VisDrone Dataset and what are its key features?
  - How can I use the VisDrone Dataset to train a YOLO26 model with Ultralytics?

The VisDrone Dataset is a large-scale benchmark created by the AISKYEYE team at the Lab of Machine Learning and Data Mining, Tianjin University, China. It contains carefully annotated ground truth data for various computer vision tasks related to drone-based image and video analysis.

Watch: How to Train Ultralytics YOLO26 on the VisDrone Dataset | Aerial Detection | Complete Tutorial 🚀

VisDrone is composed of 288 video clips with 261,908 frames and 10,209 static images, captured by various drone-mounted cameras. The dataset covers a wide range of aspects, including location (14 different cities across China), environment (urban and rural), objects (pedestrians, vehicles, bicycles, etc.), and density (sparse and crowded scenes). The dataset was collected using various drone platforms under different scenarios and weather and lighting conditions. These frames are manually annotated with over 2.6 million bounding boxes of targets such as pedestrians, cars, bicycles, and tricycles. Attributes like scene visibility, object class, and occlusion are also provided for better data utilization.

The VisDrone dataset is organized into five main subsets, each focusing on a specific task:

The VisDrone dataset is widely used for training and evaluating deep learning models in drone-based computer vision tasks such as object detection, object tracking, and crowd counting. The dataset's diverse set of sensor data, object annotations, and attributes make it a valuable resource for researchers and practitioners in the field of drone-based computer vision.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the Visdrone dataset, the VisDrone.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/VisDrone.yaml.

ultralytics/cfg/datasets/VisDrone.yaml

To train a YOLO26n model on the VisDrone dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The VisDrone dataset contains a diverse set of images and videos captured by drone-mounted cameras. Here are some examples of data from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the data in the VisDrone dataset and highlights the importance of high-quality sensor data for drone-based computer vision tasks.

If you use the VisDrone dataset in your research or development work, please cite the following paper:

We would like to acknowledge the AISKYEYE team at the Lab of Machine Learning and Data Mining, Tianjin University, China, for creating and maintaining the VisDrone dataset as a valuable resource for the drone-based computer vision research community. For more information about the VisDrone dataset and its creators, visit the VisDrone Dataset GitHub repository.

The VisDrone Dataset is a large-scale benchmark created by the AISKYEYE team at Tianjin University, China. It is designed for various computer vision tasks related to drone-based image and video analysis. Key features include:

To train a YOLO26 model on the VisDrone dataset for 100 epochs with an image size of 640, you can follow these steps:

For additional configuration options, please refer to the model Training page.

The VisDrone dataset is divided into five main subsets, each tailored for a specific computer vision task:

These subsets are widely used for training and evaluating deep learning models in drone-based applications such as surveillance, traffic monitoring, and public safety.

The configuration file for the VisDrone dataset, VisDrone.yaml, can be found in the Ultralytics repository at the following link: VisDrone.yaml.

If you use the VisDrone dataset in your research or development work, please cite the following paper:

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# VisDrone2019-DET dataset https://github.com/VisDrone/VisDrone-Dataset by Tianjin University
# Documentation: https://docs.ultralytics.com/datasets/detect/visdrone/
# Example usage: yolo train data=VisDrone.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── VisDrone ← downloads here (2.3 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: VisDrone # dataset root dir
train: images/train # train images (relative to 'path') 6471 images
val: images/val # val images (relative to 'path') 548 images
test: images/test # test-dev images (optional) 1610 images

# Classes
names:
  0: pedestrian
  1: people
  2: bicycle
  3: car
  4: van
  5: truck
  6: tricycle
  7: awning-tricycle
  8: bus
  9: motor

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  import os
  from pathlib import Path
  import shutil

  from ultralytics.utils.downloads import download
  from ultralytics.utils import ASSETS_URL, TQDM


  def visdrone2yolo(dir, split, source_name=None):
      """Convert VisDrone annotations to YOLO format with images/{split} and labels/{split} structure."""
      from PIL import Image

      source_dir = dir / (source_name or f"VisDrone2019-DET-{split}")
      images_dir = dir / "images" / split
      labels_dir = dir / "labels" / split
      labels_dir.mkdir(parents=True, exist_ok=True)

      # Move images to new structure
      if (source_images_dir := source_dir / "images").exists():
          images_dir.mkdir(parents=True, exist_ok=True)
          for img in source_images_dir.glob("*.jpg"):
              img.rename(images_dir / img.name)

      for f in TQDM((source_dir / "annotations").glob("*.txt"), desc=f"Converting {split}"):
          img_size = Image.open(images_dir / f.with_suffix(".jpg").name).size
          dw, dh = 1.0 / img_size[0], 1.0 / img_size[1]
          lines = []

          with open(f, encoding="utf-8") as file:
              for row in [x.split(",") for x in file.read().strip().splitlines()]:
                  if row[4] != "0":  # Skip ignored regions
                      x, y, w, h = map(int, row[:4])
                      cls = int(row[5]) - 1
                      # Convert to YOLO format
                      x_center, y_center = (x + w / 2) * dw, (y + h / 2) * dh
                      w_norm, h_norm = w * dw, h * dh
                      lines.append(f"{cls} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f}\n")

          (labels_dir / f.name).write_text("".join(lines), encoding="utf-8")


  # Download (ignores test-challenge split)
  dir = Path(yaml["path"])  # dataset root dir
  urls = [
      f"{ASSETS_URL}/VisDrone2019-DET-train.zip",
      f"{ASSETS_URL}/VisDrone2019-DET-val.zip",
      f"{ASSETS_URL}/VisDrone2019-DET-test-dev.zip",
      # f"{ASSETS_URL}/VisDrone2019-DET-test-challenge.zip",
  ]
  download(urls, dir=dir, threads=4)

  # Convert
  splits = {"VisDrone2019-DET-train": "train", "VisDrone2019-DET-val": "val", "VisDrone2019-DET-test-dev": "test"}
  for folder, split in splits.items():
      visdrone2yolo(dir, split, folder)  # convert VisDrone annotations to YOLO labels
      shutil.rmtree(dir / folder)  # cleanup original directory
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="VisDrone.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=VisDrone.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@ARTICLE{9573394,
  author={Zhu, Pengfei and Wen, Longyin and Du, Dawei and Bian, Xiao and Fan, Heng and Hu, Qinghua and Ling, Haibin},
  journal={IEEE Transactions on Pattern Analysis and Machine Intelligence},
  title={Detection and Tracking Meet Drones Challenge},
  year={2021},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/TPAMI.2021.3119563}}
```

---

## VOC Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/voc/

**Contents:**
- VOC Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Images and Annotations
- Citations and Acknowledgments
- FAQ
  - What is the PASCAL VOC dataset and why is it important for computer vision tasks?

The PASCAL VOC (Visual Object Classes) dataset is a well-known object detection, segmentation, and classification dataset. It is designed to encourage research on a wide variety of object categories and is commonly used for benchmarking computer vision models. It is an essential dataset for researchers and developers working on object detection, segmentation, and classification tasks.

Watch: How to Train Ultralytics YOLO26 on the Pascal VOC Dataset | Object Detection 🚀

The VOC dataset is split into three subsets:

The VOC dataset is widely used for training and evaluating deep learning models in object detection (such as Ultralytics YOLO, Faster R-CNN, and SSD), instance segmentation (such as Mask R-CNN), and image classification. The dataset's diverse set of object categories, large number of annotated images, and standardized evaluation metrics make it an essential resource for computer vision researchers and practitioners.

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the VOC dataset, the VOC.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/VOC.yaml.

ultralytics/cfg/datasets/VOC.yaml

To train a YOLO26n model on the VOC dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The VOC dataset contains a diverse set of images with various object categories and complex scenes. Here are some examples of images from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the images in the VOC dataset and the benefits of using mosaicing during the training process.

If you use the VOC dataset in your research or development work, please cite the following paper:

We would like to acknowledge the PASCAL VOC Consortium for creating and maintaining this valuable resource for the computer vision community. For more information about the VOC dataset and its creators, visit the PASCAL VOC dataset website.

The PASCAL VOC (Visual Object Classes) dataset is a renowned benchmark for object detection, segmentation, and classification in computer vision. It includes comprehensive annotations like bounding boxes, class labels, and segmentation masks across 20 different object categories. Researchers use it widely to evaluate the performance of models like Faster R-CNN, YOLO, and Mask R-CNN due to its standardized evaluation metrics such as mean Average Precision (mAP).

To train a YOLO26 model with the VOC dataset, you need the dataset configuration in a YAML file. Here's an example to start training a YOLO26n model for 100 epochs with an image size of 640:

The VOC dataset includes two main challenges: VOC2007 and VOC2012. These challenges test object detection, segmentation, and classification across 20 diverse object categories. Each image is meticulously annotated with bounding boxes, class labels, and segmentation masks. The challenges provide standardized metrics like mAP, facilitating the comparison and benchmarking of different computer vision models.

The PASCAL VOC dataset enhances model benchmarking and evaluation through its detailed annotations and standardized metrics like mean Average Precision (mAP). These metrics are crucial for assessing the performance of object detection and classification models. The dataset's diverse and complex images ensure comprehensive model evaluation across various real-world scenarios.

To use the VOC dataset for semantic segmentation tasks with YOLO models, you need to configure the dataset properly in a YAML file. The YAML file defines paths and classes needed for training segmentation models. Check the VOC dataset YAML configuration file at VOC.yaml for detailed setups. For segmentation tasks, you would use a segmentation-specific model like yolo26n-seg.pt instead of the detection model.

**Examples:**

Example 1 (yaml):
```yaml
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# PASCAL VOC dataset http://host.robots.ox.ac.uk/pascal/VOC by University of Oxford
# Documentation: https://docs.ultralytics.com/datasets/detect/voc/
# Example usage: yolo train data=VOC.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── VOC ← downloads here (2.8 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: VOC
train: # train images (relative to 'path') 16551 images
  - images/train2012
  - images/train2007
  - images/val2012
  - images/val2007
val: # val images (relative to 'path') 4952 images
  - images/test2007
test: # test images (optional)
  - images/test2007

# Classes
names:
  0: aeroplane
  1: bicycle
  2: bird
  3: boat
  4: bottle
  5: bus
  6: car
  7: cat
  8: chair
  9: cow
  10: diningtable
  11: dog
  12: horse
  13: motorbike
  14: person
  15: pottedplant
  16: sheep
  17: sofa
  18: train
  19: tvmonitor

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  import xml.etree.ElementTree as ET
  from pathlib import Path

  from ultralytics.utils.downloads import download
  from ultralytics.utils import ASSETS_URL, TQDM

  def convert_label(path, lb_path, year, image_id):
      """Converts XML annotations from VOC format to YOLO format by extracting bounding boxes and class IDs."""

      def convert_box(size, box):
          dw, dh = 1.0 / size[0], 1.0 / size[1]
          x, y, w, h = (box[0] + box[1]) / 2.0 - 1, (box[2] + box[3]) / 2.0 - 1, box[1] - box[0], box[3] - box[2]
          return x * dw, y * dh, w * dw, h * dh

      with open(path / f"VOC{year}/Annotations/{image_id}.xml") as in_file, open(lb_path, "w", encoding="utf-8") as out_file:
          tree = ET.parse(in_file)
          root = tree.getroot()
          size = root.find("size")
          w = int(size.find("width").text)
          h = int(size.find("height").text)

          names = list(yaml["names"].values())  # names list
          for obj in root.iter("object"):
              cls = obj.find("name").text
              if cls in names and int(obj.find("difficult").text) != 1:
                  xmlbox = obj.find("bndbox")
                  bb = convert_box((w, h), [float(xmlbox.find(x).text) for x in ("xmin", "xmax", "ymin", "ymax")])
                  cls_id = names.index(cls)  # class id
                  out_file.write(" ".join(str(a) for a in (cls_id, *bb)) + "\n")


  # Download
  dir = Path(yaml["path"])  # dataset root dir
  urls = [
      f"{ASSETS_URL}/VOCtrainval_06-Nov-2007.zip",  # 446MB, 5012 images
      f"{ASSETS_URL}/VOCtest_06-Nov-2007.zip",  # 438MB, 4953 images
      f"{ASSETS_URL}/VOCtrainval_11-May-2012.zip",  # 1.95GB, 17126 images
  ]
  download(urls, dir=dir / "images", threads=3, exist_ok=True)  # download and unzip over existing (required)

  # Convert
  path = dir / "images/VOCdevkit"
  for year, image_set in ("2012", "train"), ("2012", "val"), ("2007", "train"), ("2007", "val"), ("2007", "test"):
      imgs_path = dir / "images" / f"{image_set}{year}"
      lbs_path = dir / "labels" / f"{image_set}{year}"
      imgs_path.mkdir(exist_ok=True, parents=True)
      lbs_path.mkdir(exist_ok=True, parents=True)

      with open(path / f"VOC{year}/ImageSets/Main/{image_set}.txt") as f:
          image_ids = f.read().strip().split()
      for id in TQDM(image_ids, desc=f"{image_set}{year}"):
          f = path / f"VOC{year}/JPEGImages/{id}.jpg"  # old img path
          lb_path = (lbs_path / f.name).with_suffix(".txt")  # new label path
          f.rename(imgs_path / f.name)  # move image
          convert_label(path, lb_path, year, id)  # convert labels to YOLO format
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="VOC.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=VOC.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (python):
```python
@misc{everingham2010pascal,
      title={The PASCAL Visual Object Classes (VOC) Challenge},
      author={Mark Everingham and Luc Van Gool and Christopher K. I. Williams and John Winn and Andrew Zisserman},
      year={2010},
      eprint={0909.5206},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## xView Dataset

**URL:** https://docs.ultralytics.com/datasets/detect/xview/

**Contents:**
- xView Dataset
- Key Features
- Dataset Structure
- Applications
- Dataset YAML
- Usage
- Sample Data and Annotations
- Related Datasets
- Citations and Acknowledgments
- FAQ

The xView dataset is one of the largest publicly available datasets of overhead imagery, containing images from complex scenes around the world annotated using bounding boxes. The goal of the xView dataset is to accelerate progress in four computer vision frontiers:

xView builds on the success of challenges like Common Objects in Context (COCO) and aims to leverage computer vision to analyze the growing amount of available imagery from space in order to understand the visual world in new ways and address a range of important applications.

Manual Download Required

The xView dataset is not automatically downloaded by Ultralytics scripts. You must manually download the dataset first from the official source:

Important: After downloading the necessary files (e.g., train_images.tif, val_images.tif, xView_train.geojson), you need to extract them and place them into the correct directory structure, typically expected under a datasets/xView/ folder, before running the training commands provided below. Ensure the dataset is properly set up as per the challenge instructions.

The xView dataset is composed of satellite images collected from WorldView-3 satellites at a 0.3m ground sample distance. It contains over 1 million objects across 60 classes in over 1,400 km² of imagery. The dataset is particularly valuable for remote sensing applications and environmental monitoring.

The xView dataset is widely used for training and evaluating deep learning models for object detection in overhead imagery. The dataset's diverse set of object classes and high-resolution imagery make it a valuable resource for researchers and practitioners in the field of computer vision, especially for satellite imagery analysis. Applications include:

A YAML (Yet Another Markup Language) file is used to define the dataset configuration. It contains information about the dataset's paths, classes, and other relevant information. In the case of the xView dataset, the xView.yaml file is maintained at https://github.com/ultralytics/ultralytics/blob/main/ultralytics/cfg/datasets/xView.yaml.

ultralytics/cfg/datasets/xView.yaml

To train a model on the xView dataset for 100 epochs with an image size of 640, you can use the following code snippets. For a comprehensive list of available arguments, refer to the model Training page.

The xView dataset contains high-resolution satellite images with a diverse set of objects annotated using bounding boxes. Here are some examples of data from the dataset, along with their corresponding annotations:

The example showcases the variety and complexity of the data in the xView dataset and highlights the importance of high-quality satellite imagery for object detection tasks.

If you're working with satellite imagery, you might also be interested in exploring these related datasets:

If you use the xView dataset in your research or development work, please cite the following paper:

We would like to acknowledge the Defense Innovation Unit (DIU) and the creators of the xView dataset for their valuable contribution to the computer vision research community. For more information about the xView dataset and its creators, visit the xView dataset website.

The xView dataset is one of the largest publicly available collections of high-resolution overhead imagery, containing over 1 million object instances across 60 classes. It is designed to enhance various facets of computer vision research such as reducing the minimum resolution for detection, improving learning efficiency, discovering more object classes, and advancing fine-grained object detection.

To train a model on the xView dataset using Ultralytics YOLO, follow these steps:

For detailed arguments and settings, refer to the model Training page.

The xView dataset stands out due to its comprehensive set of features:

The xView dataset contains high-resolution satellite imagery captured by WorldView-3 satellites at a 0.3m ground sample distance, covering over 1 million objects across 60 distinct classes within approximately 1,400 km² of annotated imagery. Each object is labeled with bounding boxes, making the dataset highly suitable for training and evaluating deep learning models for object detection in overhead views. For a detailed breakdown, refer to the Dataset Structure section.

If you utilize the xView dataset in your research, please cite the following paper:

For more information about the xView dataset, visit the official xView dataset website.

**Examples:**

Example 1 (python):
```python
# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

# DIUx xView 2018 Challenge dataset https://challenge.xviewdataset.org by U.S. National Geospatial-Intelligence Agency (NGA)
# --------  Download and extract data manually to `datasets/xView` before running the train command.  --------
# Documentation: https://docs.ultralytics.com/datasets/detect/xview/
# Example usage: yolo train data=xView.yaml
# parent
# ├── ultralytics
# └── datasets
#     └── xView ← downloads here (20.7 GB)

# Train/val/test sets as 1) dir: path/to/imgs, 2) file: path/to/imgs.txt, or 3) list: [path/to/imgs1, path/to/imgs2, ..]
path: xView # dataset root dir
train: images/autosplit_train.txt # train images (relative to 'path') 90% of 847 train images
val: images/autosplit_val.txt # val images (relative to 'path') 10% of 847 train images

# Classes
names:
  0: Fixed-wing Aircraft
  1: Small Aircraft
  2: Cargo Plane
  3: Helicopter
  4: Passenger Vehicle
  5: Small Car
  6: Bus
  7: Pickup Truck
  8: Utility Truck
  9: Truck
  10: Cargo Truck
  11: Truck w/Box
  12: Truck Tractor
  13: Trailer
  14: Truck w/Flatbed
  15: Truck w/Liquid
  16: Crane Truck
  17: Railway Vehicle
  18: Passenger Car
  19: Cargo Car
  20: Flat Car
  21: Tank car
  22: Locomotive
  23: Maritime Vessel
  24: Motorboat
  25: Sailboat
  26: Tugboat
  27: Barge
  28: Fishing Vessel
  29: Ferry
  30: Yacht
  31: Container Ship
  32: Oil Tanker
  33: Engineering Vehicle
  34: Tower crane
  35: Container Crane
  36: Reach Stacker
  37: Straddle Carrier
  38: Mobile Crane
  39: Dump Truck
  40: Haul Truck
  41: Scraper/Tractor
  42: Front loader/Bulldozer
  43: Excavator
  44: Cement Mixer
  45: Ground Grader
  46: Hut/Tent
  47: Shed
  48: Building
  49: Aircraft Hangar
  50: Damaged Building
  51: Facility
  52: Construction Site
  53: Vehicle Lot
  54: Helipad
  55: Storage Tank
  56: Shipping container lot
  57: Shipping Container
  58: Pylon
  59: Tower

# Download script/URL (optional) ---------------------------------------------------------------------------------------
download: |
  import json
  from pathlib import Path
  import shutil

  import numpy as np
  from PIL import Image

  from ultralytics.utils import TQDM
  from ultralytics.data.split import autosplit
  from ultralytics.utils.ops import xyxy2xywhn


  def convert_labels(fname=Path("xView/xView_train.geojson")):
      """Convert xView GeoJSON labels to YOLO format (classes 0-59) and save them as text files."""
      path = fname.parent
      with open(fname, encoding="utf-8") as f:
          print(f"Loading {fname}...")
          data = json.load(f)

      # Make dirs
      labels = path / "labels" / "train"
      shutil.rmtree(labels, ignore_errors=True)
      labels.mkdir(parents=True, exist_ok=True)

      # xView classes 11-94 to 0-59
      xview_class2index = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 1, 2, -1, 3, -1, 4, 5, 6, 7, 8, -1, 9, 10, 11,
                           12, 13, 14, 15, -1, -1, 16, 17, 18, 19, 20, 21, 22, -1, 23, 24, 25, -1, 26, 27, -1, 28, -1,
                           29, 30, 31, 32, 33, 34, 35, 36, 37, -1, 38, 39, 40, 41, 42, 43, 44, 45, -1, -1, -1, -1, 46,
                           47, 48, 49, -1, 50, 51, -1, 52, -1, -1, -1, 53, 54, -1, 55, -1, -1, 56, -1, 57, -1, 58, 59]

      shapes = {}
      for feature in TQDM(data["features"], desc=f"Converting {fname}"):
          p = feature["properties"]
          if p["bounds_imcoords"]:
              image_id = p["image_id"]
              image_file = path / "train_images" / image_id
              if image_file.exists():  # 1395.tif missing
                  try:
                      box = np.array([int(num) for num in p["bounds_imcoords"].split(",")])
                      assert box.shape[0] == 4, f"incorrect box shape {box.shape[0]}"
                      cls = p["type_id"]
                      cls = xview_class2index[int(cls)]  # xView class to 0-59
                      assert 59 >= cls >= 0, f"incorrect class index {cls}"

                      # Write YOLO label
                      if image_id not in shapes:
                          shapes[image_id] = Image.open(image_file).size
                      box = xyxy2xywhn(box[None].astype(float), w=shapes[image_id][0], h=shapes[image_id][1], clip=True)
                      with open((labels / image_id).with_suffix(".txt"), "a", encoding="utf-8") as f:
                          f.write(f"{cls} {' '.join(f'{x:.6f}' for x in box[0])}\n")  # write label.txt
                  except Exception as e:
                      print(f"WARNING: skipping one label for {image_file}: {e}")


  # Download manually from https://challenge.xviewdataset.org
  dir = Path(yaml["path"])  # dataset root dir
  # urls = [
  #     "https://d307kc0mrhucc3.cloudfront.net/train_labels.zip",  # train labels
  #     "https://d307kc0mrhucc3.cloudfront.net/train_images.zip",  # 15G, 847 train images
  #     "https://d307kc0mrhucc3.cloudfront.net/val_images.zip",  # 5G, 282 val images (no labels)
  # ]
  # download(urls, dir=dir)

  # Convert labels
  convert_labels(dir / "xView_train.geojson")

  # Move images
  images = Path(dir / "images")
  images.mkdir(parents=True, exist_ok=True)
  Path(dir / "train_images").rename(dir / "images" / "train")
  Path(dir / "val_images").rename(dir / "images" / "val")

  # Split
  autosplit(dir / "images" / "train")
```

Example 2 (python):
```python
from ultralytics import YOLO

# Load a model
model = YOLO("yolo26n.pt")  # load a pretrained model (recommended for training)

# Train the model
results = model.train(data="xView.yaml", epochs=100, imgsz=640)
```

Example 3 (sql):
```sql
# Start training from a pretrained *.pt model
yolo detect train data=xView.yaml model=yolo26n.pt epochs=100 imgsz=640
```

Example 4 (css):
```css
@misc{lam2018xview,
      title={xView: Objects in Context in Overhead Imagery},
      author={Darius Lam and Richard Kuzma and Kevin McGee and Samuel Dooley and Michael Laielli and Matthew Klaric and Yaroslav Bulatov and Brendan McCord},
      year={2018},
      eprint={1802.07856},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## نظرة عامة على مجموعات البيانات

**URL:** https://docs.ultralytics.com/ar/datasets/

**Contents:**
- نظرة عامة على مجموعات البيانات
- الكشف عن الكائنات
- تجزئة المثيل
- تقدير الوضع
- التصنيف
- مربعات الإحاطة الموجهة (OBB)
- تتبع الأجسام المتعددة
- المساهمة بمجموعات بيانات جديدة
  - خطوات المساهمة بمجموعة بيانات جديدة
  - مثال على التعليمات البرمجية لتحسين مجموعة البيانات وضغطها

توفر Ultralytics دعمًا لمجموعات بيانات متنوعة لتسهيل مهام الرؤية الحاسوبية مثل الكشف عن الأجسام، و تقسيم المثيلات، وتقدير الوضعية، والتصنيف، وتتبع الأجسام المتعددة. فيما يلي قائمة بمجموعات بيانات Ultralytics الرئيسية، متبوعة بملخص لكل مهمة من مهام الرؤية الحاسوبية ومجموعات البيانات الخاصة بها.

شاهد: نظرة عامة على مجموعات بيانات Ultralytics

الكشف عن الأجسام باستخدام المربعات المحيطة هو أسلوب رؤية حاسوبية يتضمن اكتشاف وتحديد مواقع الأجسام في صورة عن طريق رسم مربع محيط حول كل جسم.

تجزئة المثيل هي تقنية رؤية حاسوبية تتضمن تحديد وتوطين الكائنات في الصورة على مستوى البكسل. على عكس التجزئة الدلالية التي تصنف كل بكسل فقط، فإن تجزئة المثيل تميز بين الحالات المختلفة من نفس الفئة.

تقدير الوضعية هو أسلوب يستخدم لتحديد وضعية الكائن بالنسبة للكاميرا أو نظام الإحداثيات العالمي. يتضمن ذلك تحديد النقاط أو المفاصل الرئيسية على الكائنات، وخاصة البشر أو الحيوانات.

Image classification هي مهمة رؤية حاسوبية تتضمن تصنيف صورة إلى فئة أو أكثر من الفئات المحددة مسبقًا بناءً على محتواها المرئي.

الصناديق المحيطة الموجهة (OBB) هي طريقة في رؤية الكمبيوتر لاكتشاف الكائنات الزاوية في الصور باستخدام صناديق محيطة مدورة، وغالبًا ما يتم تطبيقها على الصور الجوية وصور الأقمار الصناعية. على عكس الصناديق المحيطة التقليدية، يمكن لـ OBB أن تناسب بشكل أفضل الكائنات في اتجاهات مختلفة.

تتبع الأجسام المتعددة هو تقنية رؤية حاسوبية تتضمن اكتشاف وتتبع أجسام متعددة بمرور الوقت في تسلسل فيديو. توسع هذه المهمة اكتشاف الأجسام عن طريق الحفاظ على هويات متسقة للأجسام عبر الإطارات.

يتضمن المساهمة بمجموعة بيانات جديدة عدة خطوات لضمان توافقها جيدًا مع البنية التحتية الحالية. فيما يلي الخطوات الضرورية:

شاهد: كيفية المساهمة في مجموعات بيانات Ultralytics.

تنظيم مجموعة البيانات: رتب مجموعة البيانات الخاصة بك في هيكل المجلد الصحيح. يجب أن يكون لديك images/ و labels/ الدلائل ذات المستوى الأعلى، وداخل كل منها، train/ و val/ دليل فرعي.

إنشاء data.yaml ملف: في الدليل الجذر لمجموعة البيانات الخاصة بك، قم بإنشاء data.yaml ملف يصف مجموعة البيانات والفئات والمعلومات الضرورية الأخرى.

تحسين وضغط مجموعة البيانات

باتباع هذه الخطوات، يمكنك المساهمة بمجموعة بيانات جديدة تتكامل بشكل جيد مع هيكل Ultralytics الحالي.

تدعم Ultralytics مجموعة واسعة من مجموعات البيانات لـ اكتشاف الكائنات، بما في ذلك:

تسهل مجموعات البيانات هذه تدريب نماذج Ultralytics YOLO قوية لمختلف تطبيقات الكشف عن الأجسام.

تتضمن المساهمة بمجموعة بيانات جديدة عدة خطوات:

تفضل بزيارة المساهمة بمجموعات بيانات جديدة للحصول على دليل شامل.

منصة Ultralytics تقدم ميزات قوية لإدارة وتحليل مجموعات البيانات، بما في ذلك:

تعمل المنصة على تبسيط الانتقال من إدارة مجموعات البيانات إلى تدريب النماذج، مما يجعل العملية بأكملها أكثر كفاءة. تعرف على المزيد حول مجموعات بيانات منصة Ultralytics.

توفر نماذج Ultralytics YOLO العديد من الميزات الفريدة لمهام الرؤية الحاسوبية:

اكتشف المزيد حول نماذج YOLO في صفحة نماذج Ultralytics.

لتحسين مجموعة بيانات وضغطها باستخدام أدوات Ultralytics، اتبع مثال التعليمات البرمجية التالي:

تحسين وضغط مجموعة البيانات

تساعد هذه العملية على تقليل حجم مجموعة البيانات لتخزين أكثر كفاءة وسرعات تنزيل أسرع. تعرف على المزيد حول كيفية تحسين مجموعة البيانات وضغطها.

**Examples:**

Example 1 (unknown):
```unknown
dataset/
├── images/
│   ├── train/
│   └── val/
└── labels/
    ├── train/
    └── val/
```

Example 2 (python):
```python
from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("path/to/dataset")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)
```

Example 3 (python):
```python
from pathlib import Path

from ultralytics.data.utils import compress_one_image
from ultralytics.utils.downloads import zip_directory

# Define dataset directory
path = Path("path/to/dataset")

# Optimize images in dataset (optional)
for f in path.rglob("*.jpg"):
    compress_one_image(f)

# Zip dataset into 'path/to/dataset.zip'
zip_directory(path)
```

---
