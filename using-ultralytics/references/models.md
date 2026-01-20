# Raw-Ultralytics - Models

**Pages:** 47

---

## Baidu's RT-DETR: A Vision Transformer-Based Real-Time Object Detector

**URL:** https://docs.ultralytics.com/models/rtdetr/

**Contents:**
- Baidu's RT-DETR: A Vision Transformer-Based Real-Time Object Detector
- Overview
  - Key Features
- Pretrained Models
- Usage Examples
- Supported Tasks and Modes
- Ideal Use Cases
- Citations and Acknowledgments
- FAQ
  - What is Baidu's RT-DETR model and how does it work?

Real-Time Detection Transformer (RT-DETR), developed by Baidu, is a cutting-edge end-to-end object detector that provides real-time performance while maintaining high accuracy. It is based on the idea of DETR (the NMS-free framework), meanwhile introducing conv-based backbone and an efficient hybrid encoder to gain real-time speed. RT-DETR efficiently processes multiscale features by decoupling intra-scale interaction and cross-scale fusion. The model is highly adaptable, supporting flexible adjustment of inference speed using different decoder layers without retraining. RT-DETR excels on accelerated backends like CUDA with TensorRT, outperforming many other real-time object detectors.

Watch: How to Use Baidu's RT-DETR for Object Detection | Inference and Benchmarking with Ultralytics 🚀

Overview of Baidu's RT-DETR. The RT-DETR model architecture diagram shows the last three stages of the backbone {S3, S4, S5} as the input to the encoder. The efficient hybrid encoder transforms multiscale features into a sequence of image features through intrascale feature interaction (AIFI) and cross-scale feature-fusion module (CCFM). The IoU-aware query selection is employed to select a fixed number of image features to serve as initial object queries for the decoder. Finally, the decoder with auxiliary prediction heads iteratively optimizes object queries to generate boxes and confidence scores (source).

The Ultralytics Python API provides pretrained PaddlePaddle RT-DETR models with different scales:

Additionally, Baidu has released RTDETRv2 in July 2024, which further improves upon the original architecture with enhanced performance metrics.

This example provides simple RT-DETR training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

This table presents the model types, the specific pretrained weights, the tasks supported by each model, and the various modes (Train , Val, Predict, Export) that are supported, indicated by ✅ emojis.

RT-DETR is particularly well-suited for applications requiring both high accuracy and real-time performance:

If you use Baidu's RT-DETR in your research or development work, please cite the original paper:

For RTDETRv2, you can cite the 2024 paper:

We would like to acknowledge Baidu and the PaddlePaddle team for creating and maintaining this valuable resource for the computer vision community. Their contribution to the field with the development of the Vision Transformers-based real-time object detector, RT-DETR, is greatly appreciated.

Baidu's RT-DETR (Real-Time Detection Transformer) is an advanced real-time object detector built upon the Vision Transformer architecture. It efficiently processes multiscale features by decoupling intra-scale interaction and cross-scale fusion through its efficient hybrid encoder. By employing IoU-aware query selection, the model focuses on the most relevant objects, enhancing detection accuracy. Its adaptable inference speed, achieved by adjusting decoder layers without retraining, makes RT-DETR suitable for various real-time object detection scenarios. Learn more about RT-DETR features in the RT-DETR Arxiv paper.

You can leverage Ultralytics Python API to use pretrained PaddlePaddle RT-DETR models. For instance, to load an RT-DETR-l model pretrained on COCO val2017 and achieve high FPS on T4 GPU, you can utilize the following example:

Baidu's RT-DETR stands out due to its efficient hybrid encoder and IoU-aware query selection, which drastically reduce computational costs while maintaining high accuracy. Its unique ability to adjust inference speed by using different decoder layers without retraining adds significant flexibility. This makes it particularly advantageous for applications requiring real-time performance on accelerated backends like CUDA with TensorRT, outclassing many other real-time object detectors. The transformer architecture also provides better global context understanding compared to traditional CNN-based detectors.

Baidu's RT-DETR allows flexible adjustments of inference speed by using different decoder layers without requiring retraining. This adaptability is crucial for scaling performance across various real-time object detection tasks. Whether you need faster processing for lower precision needs or slower, more accurate detections, RT-DETR can be tailored to meet your specific requirements. This feature is particularly valuable when deploying models across devices with varying computational capabilities.

Yes, RT-DETR models are compatible with various Ultralytics modes including training, validation, prediction, and export. You can refer to the respective documentation for detailed instructions on how to utilize these modes: Train, Val, Predict, and Export. This ensures a comprehensive workflow for developing and deploying your object detection solutions. The Ultralytics framework provides a consistent API across different model architectures, making it easy to work with RT-DETR models.

**Examples:**

Example 1 (python):
```python
from ultralytics import RTDETR

# Load a COCO-pretrained RT-DETR-l model
model = RTDETR("rtdetr-l.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the RT-DETR-l model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained RT-DETR-l model and train it on the COCO8 example dataset for 100 epochs
yolo train model=rtdetr-l.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained RT-DETR-l model and run inference on the 'bus.jpg' image
yolo predict model=rtdetr-l.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
@misc{lv2023detrs,
      title={DETRs Beat YOLOs on Real-time Object Detection},
      author={Wenyu Lv and Shangliang Xu and Yian Zhao and Guanzhong Wang and Jinman Wei and Cheng Cui and Yuning Du and Qingqing Dang and Yi Liu},
      year={2023},
      eprint={2304.08069},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

Example 4 (css):
```css
@misc{lv2024rtdetrv2,
      title={RTDETRv2: All-in-One Detection Transformer Beats YOLO and DINO},
      author={Wenyu Lv and Yian Zhao and Qinyao Chang and Kui Huang and Guanzhong Wang and Yi Liu},
      year={2024},
      eprint={2407.17140},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## Esplora Ultralytics YOLOv8

**URL:** https://docs.ultralytics.com/it/models/yolov8/

**Contents:**
- Esplora Ultralytics YOLOv8
- Panoramica
- Caratteristiche principali di YOLOv8
- Attività e modalità supportate
- Metriche di performance
- Esempi di utilizzo di YOLOv8
- Citazioni e ringraziamenti
- FAQ
  - Cos'è YOLOv8 e in cosa differisce dalle versioni precedenti di YOLO?
  - Come posso usare YOLOv8 per diversi task di computer vision?

YOLOv8 è stato rilasciato da Ultralytics il 10 gennaio 2023, offrendo prestazioni all'avanguardia in termini di precisione e velocità. Basandosi sui progressi delle precedenti versioni di YOLO, YOLOv8 ha introdotto nuove funzionalità e ottimizzazioni che lo rendono una scelta ideale per varie attività di rilevamento di oggetti in un'ampia gamma di applicazioni.

Guarda: Panoramica del modello Ultralytics YOLOv8

Esplora ed esegui YOLOv8 direttamente sulla Ultralytics .

La serie YOLOv8 offre una vasta gamma di modelli, ciascuno specializzato per attività specifiche nella computer vision. Questi modelli sono progettati per soddisfare varie esigenze, dal rilevamento di oggetti a compiti più complessi come la segmentazione di istanze, il rilevamento di pose/keypoint, il rilevamento di oggetti orientati e la classificazione.

Ogni variante della serie YOLOv8 è ottimizzata per la rispettiva attività, garantendo alte prestazioni e accuratezza. Inoltre, questi modelli sono compatibili con varie modalità operative tra cui Inference, Validation, Training ed Export, facilitandone l'uso in diverse fasi di implementazione e sviluppo.

Questa tabella fornisce una panoramica delle varianti del modello YOLOv8, evidenziando la loro applicabilità in attività specifiche e la loro compatibilità con varie modalità operative come Inferenza, Validazione, Addestramento ed Esportazione. Mostra la versatilità e la robustezza della serie YOLOv8, rendendola adatta a una varietà di applicazioni nella computer vision.

Vedere la Documentazione sulla Detection per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Detection per esempi di utilizzo con questi modelli addestrati su Open Image V7, che includono 600 classi pre-addestrate.

Vedere la Documentazione sulla Segmentazione per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Classificazione per esempi di utilizzo con questi modelli addestrati su ImageNet, che includono 1000 classi pre-addestrate.

Vedere la Documentazione sulla Stima della Posa per esempi di utilizzo con questi modelli addestrati su COCO, che includono 1 classe pre-addestrata, 'persona'.

Vedere la Documentazione sulla Detection Orientata per esempi di utilizzo con questi modelli addestrati su DOTAv1, che includono 15 classi pre-addestrate.

Questo esempio fornisce semplici esempi di addestramento e inferenza di YOLOv8. Per la documentazione completa su queste e altre modalità, consultare le pagine di documentazione Predict, Train, Val ed Export.

Si noti che l'esempio seguente è per i modelli YOLOv8 Detect per il rilevamento di oggetti. Per ulteriori attività supportate, consultare i documenti Segment, Classify, OBB e i documenti Pose.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

Pubblicazione di Ultralytics YOLOv8

Ultralytics non ha pubblicato un documento di ricerca formale per YOLOv8 a causa della rapida evoluzione dei modelli. Ci concentriamo sul progresso della tecnologia e sul renderla più facile da usare, piuttosto che sulla produzione di documentazione statica. Per le informazioni più aggiornate sull'architettura, le caratteristiche e l'utilizzo di YOLO, fare riferimento al nostro repository GitHub e alla documentazione.

Se utilizzi il modello YOLOv8 o qualsiasi altro software da questo repository nel tuo lavoro, citalo utilizzando il seguente formato:

Si prega di notare che il DOI è in sospeso e verrà aggiunto alla citazione non appena sarà disponibile. I modelli YOLOv8 sono forniti con licenze AGPL-3.0 ed Enterprise.

YOLOv8 è progettato per migliorare le prestazioni dell'object detection in tempo reale con funzionalità avanzate. A differenza delle versioni precedenti, YOLOv8 incorpora un head Ultralytics split anchor-free, architetture backbone e neck all'avanguardia e offre un tradeoff accuratezza-velocità ottimizzato, rendendolo ideale per diverse applicazioni. Per maggiori dettagli, consulta le sezioni Panoramica e Funzionalità chiave.

YOLOv8 supporta una vasta gamma di attività di computer vision, tra cui il rilevamento di oggetti, la segmentazione di istanze, il rilevamento di pose/keypoint, il rilevamento di oggetti orientati e la classificazione. Ogni variante del modello è ottimizzata per la sua specifica attività ed è compatibile con varie modalità operative come Inference, Validation, Training ed Export. Fare riferimento alla sezione Attività e modalità supportate per ulteriori informazioni.

I modelli YOLOv8 raggiungono prestazioni all'avanguardia su vari dataset di benchmarking. Ad esempio, il modello YOLOv8n raggiunge una mAP (precisione media media) di 37.3 sul dataset COCO e una velocità di 0.99 ms su A100 TensorRT. Metriche di performance dettagliate per ogni variante del modello su diverse attività e dataset sono disponibili nella sezione Metriche di performance.

L'addestramento di un modello YOLOv8 può essere eseguito tramite Python o CLI. Di seguito sono riportati esempi di addestramento di un modello utilizzando un modello YOLOv8 pre-addestrato su COCO sul dataset COCO8 per 100 epoche:

Per maggiori dettagli, consulta la documentazione relativa al Training.

Sì, è possibile valutare i modelli YOLOv8 in termini di velocità e accuratezza in vari formati di esportazione. È possibile utilizzare PyTorch, ONNX, TensorRT e altro per il benchmarking. Di seguito sono riportati comandi di esempio per il benchmarking tramite Python e CLI:

Per ulteriori informazioni, consultare la sezione Metriche di performance.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv8n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov8n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv8n model and run inference on the 'bus.jpg' image
yolo predict model=yolov8n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Explore Ultralytics YOLOv8

**URL:** https://docs.ultralytics.com/models/yolov8/

**Contents:**
- Explore Ultralytics YOLOv8
- Overview
- Key Features of YOLOv8
- Supported Tasks and Modes
- Performance Metrics
- YOLOv8 Usage Examples
- Citations and Acknowledgments
- FAQ
  - What is YOLOv8 and how does it differ from previous YOLO versions?
  - How can I use YOLOv8 for different computer vision tasks?

YOLOv8 was released by Ultralytics on January 10, 2023, offering cutting-edge performance in terms of accuracy and speed. Building upon the advancements of previous YOLO versions, YOLOv8 introduced new features and optimizations that make it an ideal choice for various object detection tasks in a wide range of applications.

Watch: Ultralytics YOLOv8 Model Overview

Try on Ultralytics Platform

Explore and run YOLOv8 models directly on Ultralytics Platform.

The YOLOv8 series offers a diverse range of models, each specialized for specific tasks in computer vision. These models are designed to cater to various requirements, from object detection to more complex tasks like instance segmentation, pose/keypoints detection, oriented object detection, and classification.

Each variant of the YOLOv8 series is optimized for its respective task, ensuring high performance and accuracy. Additionally, these models are compatible with various operational modes including Inference, Validation, Training, and Export, facilitating their use in different stages of deployment and development.

This table provides an overview of the YOLOv8 model variants, highlighting their applicability in specific tasks and their compatibility with various operational modes such as Inference, Validation, Training, and Export. It showcases the versatility and robustness of the YOLOv8 series, making them suitable for a variety of applications in computer vision.

See Detection Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Detection Docs for usage examples with these models trained on Open Image V7, which include 600 pretrained classes.

See Segmentation Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Classification Docs for usage examples with these models trained on ImageNet, which include 1000 pretrained classes.

See Pose Estimation Docs for usage examples with these models trained on COCO, which include 1 pretrained class, 'person'.

See Oriented Detection Docs for usage examples with these models trained on DOTAv1, which include 15 pretrained classes.

This example provides simple YOLOv8 training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

Note the below example is for YOLOv8 Detect models for object detection. For additional supported tasks see the Segment, Classify, OBB docs and Pose docs.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in python:

CLI commands are available to directly run the models:

Ultralytics YOLOv8 Publication

Ultralytics has not published a formal research paper for YOLOv8 due to the rapidly evolving nature of the models. We focus on advancing the technology and making it easier to use, rather than producing static documentation. For the most up-to-date information on YOLO architecture, features, and usage, please refer to our GitHub repository and documentation.

If you use the YOLOv8 model or any other software from this repository in your work, please cite it using the following format:

Please note that the DOI is pending and will be added to the citation once it is available. YOLOv8 models are provided under AGPL-3.0 and Enterprise licenses.

YOLOv8 is designed to improve real-time object detection performance with advanced features. Unlike earlier versions, YOLOv8 incorporates an anchor-free split Ultralytics head, state-of-the-art backbone and neck architectures, and offers optimized accuracy-speed tradeoff, making it ideal for diverse applications. For more details, check the Overview and Key Features sections.

YOLOv8 supports a wide range of computer vision tasks, including object detection, instance segmentation, pose/keypoints detection, oriented object detection, and classification. Each model variant is optimized for its specific task and compatible with various operational modes like Inference, Validation, Training, and Export. Refer to the Supported Tasks and Modes section for more information.

YOLOv8 models achieve state-of-the-art performance across various benchmarking datasets. For instance, the YOLOv8n model achieves a mAP (mean Average Precision) of 37.3 on the COCO dataset and a speed of 0.99 ms on A100 TensorRT. Detailed performance metrics for each model variant across different tasks and datasets can be found in the Performance Metrics section.

Training a YOLOv8 model can be done using either Python or CLI. Below are examples for training a model using a COCO-pretrained YOLOv8 model on the COCO8 dataset for 100 epochs:

For further details, visit the Training documentation.

Yes, YOLOv8 models can be benchmarked for performance in terms of speed and accuracy across various export formats. You can use PyTorch, ONNX, TensorRT, and more for benchmarking. Below are example commands for benchmarking using Python and CLI:

For additional information, check the Performance Metrics section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv8n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov8n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv8n model and run inference on the 'bus.jpg' image
yolo predict model=yolov8n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Fast Segment Anything Model (FastSAM)

**URL:** https://docs.ultralytics.com/models/fast-sam/

**Contents:**
- Fast Segment Anything Model (FastSAM)
- Model Architecture
- Overview
- Key Features
- Available Models, Supported Tasks, and Operating Modes
- FastSAM Comparison vs YOLO
- Usage Examples
  - Predict Usage
  - Val Usage
  - Track Usage

The Fast Segment Anything Model (FastSAM) is a novel, real-time CNN-based solution for the Segment Anything task. This task is designed to segment any object within an image based on various possible user interaction prompts. FastSAM significantly reduces computational demands while maintaining competitive performance, making it a practical choice for a variety of vision tasks.

Watch: Object Tracking using FastSAM with Ultralytics

FastSAM is designed to address the limitations of the Segment Anything Model (SAM), a heavy Transformer model with substantial computational resource requirements. The FastSAM decouples the segment anything task into two sequential stages: all-instance segmentation and prompt-guided selection. The first stage uses YOLOv8-seg to produce the segmentation masks of all instances in the image. In the second stage, it outputs the region-of-interest corresponding to the prompt.

Real-time Solution: By leveraging the computational efficiency of CNNs, FastSAM provides a real-time solution for the segment anything task, making it valuable for industrial applications that require quick results.

Efficiency and Performance: FastSAM offers a significant reduction in computational and resource demands without compromising on performance quality. It achieves comparable performance to SAM but with drastically reduced computational resources, enabling real-time application.

Prompt-guided Segmentation: FastSAM can segment any object within an image guided by various possible user interaction prompts, providing flexibility and adaptability in different scenarios.

Based on YOLOv8-seg: FastSAM is based on YOLOv8-seg, an object detector equipped with an instance segmentation branch. This allows it to effectively produce the segmentation masks of all instances in an image.

Competitive Results on Benchmarks: On the object proposal task on MS COCO, FastSAM achieves high scores at a significantly faster speed than SAM on a single NVIDIA RTX 3090, demonstrating its efficiency and capability.

Practical Applications: The proposed approach provides a new, practical solution for a large number of vision tasks at a really high speed, tens or hundreds of times faster than current methods.

Model Compression Feasibility: FastSAM demonstrates the feasibility of a path that can significantly reduce the computational effort by introducing an artificial prior to the structure, thus opening new possibilities for large model architecture for general vision tasks.

This table presents the available models with their specific pretrained weights, the tasks they support, and their compatibility with different operating modes like Inference, Validation, Training, and Export, indicated by ✅ emojis for supported modes and ❌ emojis for unsupported modes.

Here we compare Meta's SAM 2 models, including the smallest SAM2-t variant, with Ultralytics smallest segmentation model, YOLO11n-seg:

This comparison demonstrates the substantial differences in model sizes and speeds between SAM variants and YOLO segmentation models. While SAM provides unique automatic segmentation capabilities, YOLO models, particularly YOLOv8n-seg and YOLO11n-seg, are significantly smaller, faster, and more computationally efficient.

Tests run on a 2025 Apple M4 Pro with 24GB of RAM using torch==2.6.0 and ultralytics==8.3.90. To reproduce this test:

The FastSAM models are easy to integrate into your Python applications. Ultralytics provides user-friendly Python API and CLI commands to streamline development.

To perform object detection on an image, use the predict method as shown below:

This snippet demonstrates the simplicity of loading a pretrained model and running a prediction on an image.

FastSAMPredictor example

This way you can run inference on image and get all the segment results once and run prompts inference multiple times without running inference multiple times.

All the returned results in above examples are Results object which allows access predicted masks and source image easily.

Validation of the model on a dataset can be done as follows:

Please note that FastSAM only supports detection and segmentation of a single class of object. This means it will recognize and segment all objects as the same class. Therefore, when preparing the dataset, you need to convert all object category IDs to 0.

To perform object tracking on an image, use the track method as shown below:

FastSAM is also available directly from the https://github.com/CASIA-IVA-Lab/FastSAM repository. Here is a brief overview of the typical steps you might take to use FastSAM:

Clone the FastSAM repository:

Create and activate a Conda environment with Python 3.9:

Navigate to the cloned repository and install the required packages:

Install the CLIP model:

Download a model checkpoint.

Use FastSAM for inference. Example commands:

Segment everything in an image:

Segment specific objects using text prompt:

Segment objects within a bounding box (provide box coordinates in xywh format):

Segment objects near specific points:

Additionally, you can try FastSAM through the CASIA-IVA-Lab Colab demo.

We would like to acknowledge the FastSAM authors for their significant contributions in the field of real-time instance segmentation:

The original FastSAM paper can be found on arXiv. The authors have made their work publicly available, and the codebase can be accessed on GitHub. We appreciate their efforts in advancing the field and making their work accessible to the broader community.

FastSAM, short for Fast Segment Anything Model, is a real-time convolutional neural network (CNN)-based solution designed to reduce computational demands while maintaining high performance in object segmentation tasks. Unlike the Segment Anything Model (SAM), which uses a heavier Transformer-based architecture, FastSAM leverages Ultralytics YOLOv8-seg for efficient instance segmentation in two stages: all-instance segmentation followed by prompt-guided selection.

FastSAM achieves real-time segmentation by decoupling the segmentation task into all-instance segmentation with YOLOv8-seg and prompt-guided selection stages. By utilizing the computational efficiency of CNNs, FastSAM offers significant reductions in computational and resource demands while maintaining competitive performance. This dual-stage approach enables FastSAM to deliver fast and efficient segmentation suitable for applications requiring quick results.

FastSAM is practical for a variety of computer vision tasks that require real-time segmentation performance. Applications include:

Its ability to handle various user interaction prompts makes FastSAM adaptable and flexible for diverse scenarios.

To use FastSAM for inference in Python, you can follow the example below:

For more details on inference methods, check the Predict Usage section of the documentation.

FastSAM supports multiple prompt types for guiding the segmentation tasks:

This flexibility allows FastSAM to adapt to a wide range of user interaction scenarios, enhancing its utility across different applications. For more information on using these prompts, refer to the Key Features section.

**Examples:**

Example 1 (python):
```python
from ultralytics import ASSETS, SAM, YOLO, FastSAM

# Profile SAM2-t, SAM2-b, SAM-b, MobileSAM
for file in ["sam_b.pt", "sam2_b.pt", "sam2_t.pt", "mobile_sam.pt"]:
    model = SAM(file)
    model.info()
    model(ASSETS)

# Profile FastSAM-s
model = FastSAM("FastSAM-s.pt")
model.info()
model(ASSETS)

# Profile YOLO models
for file_name in ["yolov8n-seg.pt", "yolo11n-seg.pt"]:
    model = YOLO(file_name)
    model.info()
    model(ASSETS)
```

Example 2 (python):
```python
from ultralytics import FastSAM

# Define an inference source
source = "path/to/bus.jpg"

# Create a FastSAM model
model = FastSAM("FastSAM-s.pt")  # or FastSAM-x.pt

# Run inference on an image
everything_results = model(source, device="cpu", retina_masks=True, imgsz=1024, conf=0.4, iou=0.9)

# Run inference with bboxes prompt
results = model(source, bboxes=[439, 437, 524, 709])

# Run inference with points prompt
results = model(source, points=[[200, 200]], labels=[1])

# Run inference with texts prompt
results = model(source, texts="a photo of a dog")

# Run inference with bboxes and points and texts prompt at the same time
results = model(source, bboxes=[439, 437, 524, 709], points=[[200, 200]], labels=[1], texts="a photo of a dog")
```

Example 3 (markdown):
```markdown
# Load a FastSAM model and segment everything with it
yolo segment predict model=FastSAM-s.pt source=path/to/bus.jpg imgsz=640
```

Example 4 (sql):
```sql
from ultralytics.models.fastsam import FastSAMPredictor

# Create FastSAMPredictor
overrides = dict(conf=0.25, task="segment", mode="predict", model="FastSAM-s.pt", save=False, imgsz=1024)
predictor = FastSAMPredictor(overrides=overrides)

# Segment everything
everything_results = predictor("ultralytics/assets/bus.jpg")

# Prompt inference
bbox_results = predictor.prompt(everything_results, bboxes=[[200, 200, 300, 300]])
point_results = predictor.prompt(everything_results, points=[200, 200])
text_results = predictor.prompt(everything_results, texts="a photo of a dog")
```

---

## Meituan YOLOv6

**URL:** https://docs.ultralytics.com/models/yolov6/

**Contents:**
- Meituan YOLOv6
- Overview
  - Key Features
- Performance Metrics
- Usage Examples
- Supported Tasks and Modes
- Citations and Acknowledgments
- FAQ
  - What is Meituan YOLOv6 and what makes it unique?
  - How does the Bi-directional Concatenation (BiC) Module in YOLOv6 improve performance?

Meituan YOLOv6, released in 2022, offers a strong balance between speed and accuracy, making it a popular choice for real-time applications. This model introduces several notable enhancements on its architecture and training scheme, including the implementation of a Bi-directional Concatenation (BiC) module, an anchor-aided training (AAT) strategy, and an improved backbone and neck design for high accuracy on the COCO dataset.

Overview of YOLOv6. Model architecture diagram showing the redesigned network components and training strategies that have led to significant performance improvements. (a) The neck of YOLOv6 (N and S are shown). Note for M/L, RepBlocks is replaced with CSPStackRep. (b) The structure of a BiC module. (c) A SimCSPSPPF block. (source).

YOLOv6 provides various pretrained models with different scales:

YOLOv6 also provides quantized models for different precisions and models optimized for mobile platforms.

This example provides simple YOLOv6 training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

YOLOv6 *.yaml files can be passed to the YOLO() class to build the corresponding model in Python:

CLI commands are available to directly run the models:

The YOLOv6 series offers a range of models, each optimized for high-performance Object Detection. These models cater to varying computational needs and accuracy requirements, making them versatile for a wide array of applications.

This table provides a detailed overview of the YOLOv6 model variants, highlighting their capabilities in object detection tasks and their compatibility with various operational modes such as Inference, Validation, Training, and Export. This comprehensive support ensures that users can fully leverage the capabilities of YOLOv6 models in a broad range of object detection scenarios.

We would like to acknowledge the authors for their significant contributions in the field of real-time object detection:

The original YOLOv6 paper can be found on arXiv. The authors have made their work publicly available, and the codebase can be accessed on GitHub. We appreciate their efforts in advancing the field and making their work accessible to the broader community.

Meituan YOLOv6, released in 2022, is an object detector that balances speed and accuracy, designed for real-time applications. It features notable architectural enhancements like the Bi-directional Concatenation (BiC) module and an Anchor-Aided Training (AAT) strategy. These innovations provide substantial performance gains with minimal speed degradation, making YOLOv6 a competitive choice for object detection tasks.

The Bi-directional Concatenation (BiC) module in YOLOv6 enhances localization signals in the detector's neck, delivering performance improvements with negligible speed impact. This module effectively combines different feature maps, increasing the model's ability to detect objects accurately. For more details on YOLOv6's features, refer to the Key Features section.

You can train a YOLOv6 model using Ultralytics with simple Python or CLI commands. For instance:

For more information, visit the Train page.

YOLOv6 offers multiple versions, each optimized for different performance requirements:

These models are evaluated on the COCO dataset using an NVIDIA T4 GPU. For more on performance metrics, see the Performance Metrics section.

Anchor-Aided Training (AAT) in YOLOv6 combines elements of anchor-based and anchor-free approaches, enhancing the model's detection capabilities without compromising inference efficiency. This strategy leverages anchors during training to improve bounding box predictions, making YOLOv6 effective in diverse object detection tasks.

YOLOv6 supports various operational modes including Inference, Validation, Training, and Export. This flexibility allows users to fully exploit the model's capabilities in different scenarios. Check out the Supported Tasks and Modes section for a detailed overview of each mode.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Build a YOLOv6n model from scratch
model = YOLO("yolov6n.yaml")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv6n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (sql):
```sql
# Build a YOLOv6n model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov6n.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv6n model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov6n.yaml source=path/to/bus.jpg
```

Example 3 (python):
```python
@misc{li2023yolov6,
      title={YOLOv6 v3.0: A Full-Scale Reloading},
      author={Chuyi Li and Lulu Li and Yifei Geng and Hongliang Jiang and Meng Cheng and Bo Zhang and Zaidan Ke and Xiaoming Xu and Xiangxiang Chu},
      year={2023},
      eprint={2301.05586},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Build a YOLOv6n model from scratch
model = YOLO("yolov6n.yaml")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Meituan YOLOv6

**URL:** https://docs.ultralytics.com/it/models/yolov6/

**Contents:**
- Meituan YOLOv6
- Panoramica
  - Caratteristiche principali
- Metriche di performance
- Esempi di utilizzo
- Attività e modalità supportate
- Citazioni e ringraziamenti
- FAQ
  - Cos'è Meituan YOLOv6 e cosa lo rende unico?
  - In che modo il modulo Bi-directional Concatenation (BiC) in YOLOv6 migliora le prestazioni?

Meituan YOLOv6, rilasciato nel 2022, offre un forte equilibrio tra velocità e precisione, rendendolo una scelta popolare per le applicazioni in tempo reale. Questo modello introduce diversi notevoli miglioramenti alla sua architettura e schema di addestramento, inclusa l'implementazione di un modulo di concatenazione bidirezionale (BiC), una strategia di addestramento assistito da ancore (AAT) e un design migliorato di backbone e neck per un'elevata precisione sul dataset COCO.

Panoramica di YOLOv6. Diagramma dell'architettura del modello che mostra i componenti di rete riprogettati e le strategie di addestramento che hanno portato a significativi miglioramenti delle prestazioni. (a) Il neck di YOLOv6 (sono mostrati N e S). Nota: per M/L, RepBlocks è sostituito con CSPStackRep. (b) La struttura di un modulo BiC. (c) Un blocco SimCSPSPPF. (source).

YOLOv6 fornisce vari modelli pre-addestrati con diverse scale:

YOLOv6 fornisce anche modelli quantizzati per diverse precisioni e modelli ottimizzati per piattaforme mobili.

Questo esempio fornisce semplici esempi di addestramento e inferenza di YOLOv6. Per la documentazione completa su queste e altre modalità, consultare le pagine di documentazione Predict, Train, Val ed Export.

YOLOv6 *.yaml file possono essere passati alla YOLO() classe per costruire il modello corrispondente in Python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

La serie YOLOv6 offre una gamma di modelli, ciascuno ottimizzato per Object Detection ad alte prestazioni. Questi modelli soddisfano diverse esigenze computazionali e requisiti di accuratezza, rendendoli versatili per una vasta gamma di applicazioni.

Questa tabella fornisce una panoramica dettagliata delle varianti del modello YOLOv6, evidenziandone le capacità nelle attività di object detection e la loro compatibilità con varie modalità operative come Inference, Validation, Training ed Export. Questo supporto completo garantisce che gli utenti possano sfruttare appieno le capacità dei modelli YOLOv6 in un'ampia gamma di scenari di object detection.

Desideriamo ringraziare gli autori per i loro significativi contributi nel campo del rilevamento di oggetti in tempo reale:

Il paper originale di YOLOv6 è disponibile su arXiv. Gli autori hanno reso il loro lavoro pubblicamente disponibile e il codice può essere consultato su GitHub. Apprezziamo i loro sforzi nel far progredire il settore e nel rendere il loro lavoro accessibile alla comunità più ampia.

Meituan YOLOv6, rilasciato nel 2022, è un rilevatore di oggetti che bilancia velocità e precisione, progettato per applicazioni in tempo reale. Presenta notevoli miglioramenti architetturali come il modulo di concatenazione bidirezionale (BiC) e una strategia di addestramento assistito da ancore (AAT). Queste innovazioni forniscono guadagni prestazionali sostanziali con un degrado minimo della velocità, rendendo YOLOv6 una scelta competitiva per i compiti di rilevamento di oggetti.

Il modulo Bi-directional Concatenation (BiC) in YOLOv6 migliora i segnali di localizzazione nel neck del rivelatore, offrendo miglioramenti delle prestazioni con un impatto trascurabile sulla velocità. Questo modulo combina efficacemente diverse feature maps, aumentando la capacità del modello di detectare accuratamente gli oggetti. Per maggiori dettagli sulle caratteristiche di YOLOv6, fare riferimento alla sezione Caratteristiche principali.

Puoi addestrare un modello YOLOv6 usando Ultralytics con semplici comandi Python o CLI. Ad esempio:

Per maggiori informazioni, visitare la pagina Train.

YOLOv6 offre diverse versioni, ciascuna ottimizzata per differenti requisiti di performance:

Questi modelli sono valutati sul COCO dataset utilizzando una GPU NVIDIA T4. Per maggiori informazioni sulle metriche di performance, consulta la sezione Performance Metrics.

L'Anchor-Aided Training (AAT) in YOLOv6 combina elementi degli approcci anchor-based e anchor-free, migliorando le capacità di detect del modello senza compromettere l'efficienza dell'inferenza. Questa strategia sfrutta gli anchor durante l'addestramento per migliorare le previsioni dei bounding box, rendendo YOLOv6 efficace in diverse attività di object detection.

YOLOv6 supporta diverse modalità operative, tra cui Inference, Validation, Training ed Export. Questa flessibilità consente agli utenti di sfruttare appieno le capacità del modello in diversi scenari. Consulta la sezione Supported Tasks and Modes per una panoramica dettagliata di ciascuna modalità.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Build a YOLOv6n model from scratch
model = YOLO("yolov6n.yaml")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv6n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (sql):
```sql
# Build a YOLOv6n model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov6n.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv6n model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov6n.yaml source=path/to/bus.jpg
```

Example 3 (python):
```python
@misc{li2023yolov6,
      title={YOLOv6 v3.0: A Full-Scale Reloading},
      author={Chuyi Li and Lulu Li and Yifei Geng and Hongliang Jiang and Meng Cheng and Bo Zhang and Zaidan Ke and Xiaoming Xu and Xiangxiang Chu},
      year={2023},
      eprint={2301.05586},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Build a YOLOv6n model from scratch
model = YOLO("yolov6n.yaml")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Meituan YOLOv6

**URL:** https://docs.ultralytics.com/ar/models/yolov6/

**Contents:**
- Meituan YOLOv6
- نظرة عامة
  - الميزات الرئيسية
- مقاييس الأداء
- أمثلة الاستخدام
- المهام والأوضاع المدعومة
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هو Meituan YOLOv6 وما الذي يجعله فريدًا؟
  - كيف تعمل وحدة الربط ثنائية الاتجاه (BiC) في YOLOv6 على تحسين الأداء؟

Meituan YOLOv6، الذي صدر في عام 2022، يوفر توازنًا قويًا بين السرعة والدقة، مما يجعله خيارًا شائعًا للتطبيقات في الوقت الفعلي. يقدم هذا النموذج العديد من التحسينات الملحوظة على بنيته ونظام تدريبه، بما في ذلك تطبيق وحدة التجميع ثنائي الاتجاه (BiC)، واستراتيجية التدريب المدعوم بالمرتكزات (AAT)، وتصميم محسّن لـ العمود الفقري والرقبة لتحقيق دقة عالية على مجموعة بيانات COCO.

نظرة عامة على YOLOv6. رسم تخطيطي لهندسة النموذج يوضح مكونات الشبكة المعاد تصميمها واستراتيجيات التدريب التي أدت إلى تحسينات كبيرة في الأداء. (أ) عنق YOLOv6 (يظهر N و S). لاحظ أنه بالنسبة لـ M/L، يتم استبدال RepBlocks بـ CSPStackRep. (ب) هيكل وحدة BiC. (ج) كتلة SimCSPSPPF.المصدر).

يوفر YOLOv6 نماذج متنوعة مدربة مسبقًا بمقاييس مختلفة:

توفر YOLOv6 أيضًا نماذج كمية لدقة مختلفة ونماذج محسّنة لمنصات الأجهزة المحمولة.

يقدم هذا المثال أمثلة بسيطة لتدريب واستدلال YOLOv6. للاطلاع على الوثائق الكاملة لهذه الأنماط وغيرها، راجع صفحات الوثائق الخاصة بـ Predict وTrain وVal وExport.

YOLOv6 *.yaml يمكن تمرير الملفات إلى YOLO() فئة لإنشاء النموذج المقابل في Python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

تقدم سلسلة YOLOv6 مجموعة من النماذج، تم تحسين كل منها للكشف عن الكائنات عالي الأداء. تلبي هذه النماذج الاحتياجات الحسابية المختلفة ومتطلبات الدقة، مما يجعلها متعددة الاستخدامات لمجموعة واسعة من التطبيقات.

يقدم هذا الجدول نظرة عامة مفصلة عن متغيرات نموذج YOLOv6، مع تسليط الضوء على قدراتها في مهام object detection وتوافقها مع أوضاع التشغيل المختلفة مثل Inference و Validation و Training و Export. يضمن هذا الدعم الشامل أن يتمكن المستخدمون من الاستفادة الكاملة من قدرات نماذج YOLOv6 في مجموعة واسعة من سيناريوهات object detection.

نود أن نعرب عن تقديرنا للمؤلفين لمساهماتهم الكبيرة في مجال اكتشاف الكائنات في الوقت الفعلي:

يمكن العثور على ورقة YOLOv6 الأصلية على arXiv. لقد أتاح المؤلفون عملهم للجمهور، ويمكن الوصول إلى قاعدة التعليمات البرمجية على GitHub. نحن نقدر جهودهم في تطوير هذا المجال وإتاحة عملهم للمجتمع الأوسع.

Meituan YOLOv6، الذي صدر في عام 2022، هو كاشف كائنات يوازن بين السرعة والدقة، ومصمم لتطبيقات الوقت الفعلي. يتميز بتحسينات معمارية ملحوظة مثل وحدة التجميع ثنائي الاتجاه (BiC) واستراتيجية التدريب المدعوم بالمرتكزات (AAT). توفر هذه الابتكارات مكاسب كبيرة في الأداء مع الحد الأدنى من تدهور السرعة، مما يجعل YOLOv6 خيارًا تنافسيًا لمهام الكشف عن الكائنات.

تعمل وحدة Bi-directional Concatenation (BiC) في YOLOv6 على تحسين إشارات تحديد الموقع في عنق الكاشف، مما يوفر تحسينات في الأداء مع تأثير ضئيل على السرعة. تجمع هذه الوحدة بشكل فعال بين خرائط الميزات المختلفة، مما يزيد من قدرة النموذج على اكتشاف الكائنات بدقة. لمزيد من التفاصيل حول ميزات YOLOv6، راجع قسم الميزات الرئيسية.

يمكنك تدريب نموذج YOLOv6 باستخدام Ultralytics بأوامر Python أو CLI بسيطة. على سبيل المثال:

لمزيد من المعلومات، قم بزيارة صفحة التدريب.

تقدم YOLOv6 إصدارات متعددة، كل منها مُحسَّن لمتطلبات أداء مختلفة:

يتم تقييم هذه النماذج على مجموعة بيانات COCO باستخدام وحدة GPU من NVIDIA T4. لمزيد من المعلومات حول مقاييس الأداء، راجع قسم مقاييس الأداء.

تجمع استراتيجية التدريب المدعوم بالمرتكزات (AAT) في YOLOv6 بين عناصر المناهج القائمة على المرتكزات والخالية من المرتكزات، مما يعزز قدرات الكشف للنموذج دون المساس بكفاءة الاستدلال. تستفيد هذه الاستراتيجية من المرتكزات أثناء التدريب لتحسين توقعات الصناديق المحيطة، مما يجعل YOLOv6 فعالاً في مهام اكتشاف الكائنات المتنوعة.

تدعم YOLOv6 أوضاع التشغيل المختلفة بما في ذلك الاستدلال والتحقق والتدريب والتصدير. تتيح هذه المرونة للمستخدمين الاستفادة الكاملة من قدرات النموذج في سيناريوهات مختلفة. تحقق من قسم المهام والأوضاع المدعومة للحصول على نظرة عامة مفصلة عن كل وضع.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Build a YOLOv6n model from scratch
model = YOLO("yolov6n.yaml")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv6n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (sql):
```sql
# Build a YOLOv6n model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov6n.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv6n model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov6n.yaml source=path/to/bus.jpg
```

Example 3 (python):
```python
@misc{li2023yolov6,
      title={YOLOv6 v3.0: A Full-Scale Reloading},
      author={Chuyi Li and Lulu Li and Yifei Geng and Hongliang Jiang and Meng Cheng and Bo Zhang and Zaidan Ke and Xiaoming Xu and Xiangxiang Chu},
      year={2023},
      eprint={2301.05586},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Build a YOLOv6n model from scratch
model = YOLO("yolov6n.yaml")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Mobile Segment Anything (MobileSAM)

**URL:** https://docs.ultralytics.com/models/mobile-sam/

**Contents:**
- Mobile Segment Anything (MobileSAM)
- Available Models, Supported Tasks, and Operating Modes
- MobileSAM Comparison vs YOLO
- Adapting from SAM to MobileSAM
  - ViT-Based Image Encoder Comparison
  - Prompt-Guided Mask Decoder
  - Whole Pipeline Comparison
- Testing MobileSAM in Ultralytics
  - Model Download
  - Point Prompt

MobileSAM is a compact, efficient image segmentation model purpose-built for mobile and edge devices. Designed to bring the power of Meta's Segment Anything Model (SAM) to environments with limited compute, MobileSAM delivers near-instant segmentation while maintaining compatibility with the original SAM pipeline. Whether you're developing real-time applications or lightweight deployments, MobileSAM provides impressive segmentation results with a fraction of the size and speed requirements of its predecessors.

Watch: How to Run Inference with MobileSAM using Ultralytics | Step-by-Step Guide 🎉

MobileSAM has been adopted in a variety of projects, including Grounding-SAM, AnyLabeling, and Segment Anything in 3D.

MobileSAM was trained on a single GPU using a 100k image dataset (1% of the original images) in less than a day. The training code will be released in the future.

The table below outlines the available MobileSAM model, its pretrained weights, supported tasks, and compatibility with different operating modes such as Inference, Validation, Training, and Export. Supported modes are indicated by ✅ and unsupported modes by ❌.

The following comparison highlights the differences between Meta's SAM variants, MobileSAM, and Ultralytics' smallest segmentation models, including YOLO11n-seg:

This comparison demonstrates the substantial differences in model size and speed between SAM variants and YOLO segmentation models. While SAM models offer unique automatic segmentation capabilities, YOLO models—especially YOLOv8n-seg and YOLO11n-seg—are significantly smaller, faster, and more computationally efficient.

Tests were conducted on a 2025 Apple M4 Pro with 24GB RAM using torch==2.6.0 and ultralytics==8.3.90. To reproduce these results:

MobileSAM retains the same pipeline as the original SAM, including pre-processing, post-processing, and all interfaces. This means you can transition from SAM to MobileSAM with minimal changes to your workflow.

The key difference is the image encoder: MobileSAM replaces the original ViT-H encoder (632M parameters) with a much smaller Tiny-ViT encoder (5M parameters). On a single GPU, MobileSAM processes an image in about 12ms (8ms for the encoder, 4ms for the mask decoder).

The performance of MobileSAM and the original SAM is illustrated below using both point and box prompts.

MobileSAM is approximately 7 times smaller and 5 times faster than FastSAM. For further details, visit the MobileSAM project page.

Just like the original SAM, Ultralytics provides a simple interface for testing MobileSAM, supporting both Point and Box prompts.

Download the MobileSAM pretrained weights from Ultralytics assets.

Both MobileSAM and SAM share the same API. For more usage details, see the SAM documentation.

To automatically annotate your dataset with the Ultralytics framework, use the auto_annotate function as shown below:

If MobileSAM is helpful in your research or development, please consider citing the following paper:

Read the full MobileSAM paper on arXiv.

MobileSAM is a lightweight, fast image segmentation model optimized for mobile and edge applications. It maintains the same pipeline as the original SAM but replaces the large ViT-H encoder (632M parameters) with a compact Tiny-ViT encoder (5M parameters). This results in MobileSAM being about 5 times smaller and 7 times faster than the original SAM, operating at roughly 12ms per image versus SAM's 456ms. Explore more about MobileSAM's implementation on the MobileSAM GitHub repository.

Testing MobileSAM in Ultralytics is straightforward. You can use Point and Box prompts to predict segments. For example, using a Point prompt:

For more details, see the Testing MobileSAM in Ultralytics section.

MobileSAM is ideal for mobile and edge applications due to its lightweight design and rapid inference speed. Compared to the original SAM, MobileSAM is about 5 times smaller and 7 times faster, making it suitable for real-time segmentation on devices with limited computational resources. Its efficiency enables mobile devices to perform real-time image segmentation without significant latency. Additionally, MobileSAM supports Inference mode optimized for mobile performance.

MobileSAM was trained on a single GPU with a 100k image dataset (1% of the original images) in under a day. While the training code will be released in the future, you can currently access pretrained weights and implementation details from the MobileSAM GitHub repository.

MobileSAM is designed for fast, efficient image segmentation in mobile and edge environments. Primary use cases include:

For more details on use cases and performance, see Adapting from SAM to MobileSAM and the Ultralytics blog on MobileSAM applications.

**Examples:**

Example 1 (python):
```python
from ultralytics import ASSETS, SAM, YOLO, FastSAM

# Profile SAM2-t, SAM2-b, SAM-b, MobileSAM
for file in ["sam_b.pt", "sam2_b.pt", "sam2_t.pt", "mobile_sam.pt"]:
    model = SAM(file)
    model.info()
    model(ASSETS)

# Profile FastSAM-s
model = FastSAM("FastSAM-s.pt")
model.info()
model(ASSETS)

# Profile YOLO models
for file_name in ["yolov8n-seg.pt", "yolo11n-seg.pt"]:
    model = YOLO(file_name)
    model.info()
    model(ASSETS)
```

Example 2 (python):
```python
from ultralytics import SAM

# Load the model
model = SAM("mobile_sam.pt")

# Predict a segment based on a single point prompt
model.predict("ultralytics/assets/zidane.jpg", points=[900, 370], labels=[1])

# Predict multiple segments based on multiple points prompt
model.predict("ultralytics/assets/zidane.jpg", points=[[400, 370], [900, 370]], labels=[1, 1])

# Predict a segment based on multiple points prompt per object
model.predict("ultralytics/assets/zidane.jpg", points=[[[400, 370], [900, 370]]], labels=[[1, 1]])

# Predict a segment using both positive and negative prompts.
model.predict("ultralytics/assets/zidane.jpg", points=[[[400, 370], [900, 370]]], labels=[[1, 0]])
```

Example 3 (python):
```python
from ultralytics import SAM

# Load the model
model = SAM("mobile_sam.pt")

# Predict a segment based on a single point prompt
model.predict("ultralytics/assets/zidane.jpg", points=[900, 370], labels=[1])

# Predict multiple segments based on multiple points prompt
model.predict("ultralytics/assets/zidane.jpg", points=[[400, 370], [900, 370]], labels=[1, 1])

# Predict a segment based on multiple points prompt per object
model.predict("ultralytics/assets/zidane.jpg", points=[[[400, 370], [900, 370]]], labels=[[1, 1]])

# Predict a segment using both positive and negative prompts.
model.predict("ultralytics/assets/zidane.jpg", points=[[[400, 370], [900, 370]]], labels=[[1, 0]])
```

Example 4 (sql):
```sql
from ultralytics.data.annotator import auto_annotate

auto_annotate(data="path/to/images", det_model="yolo11x.pt", sam_model="mobile_sam.pt")
```

---

## Modelli supportati da Ultralytics

**URL:** https://docs.ultralytics.com/it/models/

**Contents:**
- Modelli supportati da Ultralytics
- Modelli in evidenza
- Introduzione: esempi di utilizzo
- Contributo di nuovi modelli
- FAQ
  - Qual è l'ultimo modello Ultralytics YOLO?
  - Come posso addestrare un modello YOLO su dati personalizzati?
  - Quali versioni di YOLO sono supportate da Ultralytics?
  - Perché dovrei usare Ultralytics Platform per progetti di machine learning?
  - Che tipi di attività possono eseguire i modelli Ultralytics YOLO?

Benvenuti nella documentazione del modello di Ultralytics! Offriamo supporto per una vasta gamma di modelli, ognuno dei quali è adattato a compiti specifici come il rilevamento di oggetti, la segmentazione di istanze, la classificazione di immagini, la stima della posa e il tracciamento multi-oggetto. Se sei interessato a contribuire con la tua architettura di modello a Ultralytics, consulta la nostra Guida per i contributi.

Ecco alcuni dei modelli chiave supportati:

Guarda: Esegui i modelli Ultralytics YOLO con poche righe di codice.

Questo esempio fornisce semplici esempi di addestramento e inferenza YOLO. Per la documentazione completa su questi e altri modi, consultare le pagine della documentazione di Predict, Train, Val ed Export.

Si noti che l'esempio seguente mette in evidenza i modelli YOLO11 Detect per il rilevamento di oggetti. Per ulteriori attività supportate, consultare i documenti Segment, Classify e Pose.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO(), SAM(), NAS() e RTDETR() classi per creare un'istanza del modello in python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

Sei interessato a contribuire con il tuo modello a Ultralytics? Ottimo! Siamo sempre aperti ad ampliare il nostro portafoglio di modelli.

Fork del Repository: Inizia effettuando il fork del repository GitHub di Ultralytics.

Clona il tuo Fork: Clona il tuo fork sulla tua macchina locale e crea un nuovo branch su cui lavorare.

Implementa il tuo Modello: Aggiungi il tuo modello seguendo gli standard di codifica e le linee guida fornite nella nostra Guida per i Contributori.

Test Approfonditi: Assicurati di testare a fondo il tuo modello, sia isolatamente che come parte della pipeline.

Crea una Pull Request: Una volta che sei soddisfatto del tuo modello, crea una pull request al repository principale per la revisione.

Revisione del Codice e Unione: Dopo la revisione, se il tuo modello soddisfa i nostri criteri, verrà unito nel repository principale.

Per passaggi dettagliati, consulta la nostra Guida per i Contributori.

L'ultimo modello Ultralytics YOLO è YOLO26, rilasciato a gennaio 2026. YOLO26 offre inferenza end-to-end NMS-free, deployment ottimizzato per l'edge e supporta tutte e cinque le attività (detection, segmentation, classificazione, stima della posa e OBB) oltre alle versioni a vocabolario aperto. Per carichi di lavoro di produzione stabili, sia YOLO26 che YOLO11 sono scelte raccomandate.

L'addestramento di un modello YOLO su dati personalizzati può essere facilmente realizzato utilizzando le librerie di Ultralytics. Ecco un rapido esempio:

Per istruzioni più dettagliate, visita la pagina di documentazione Train.

Ultralytics supporta una gamma completa di versioni YOLO (You Only Look Once) da YOLOv3 a YOLO11, insieme a modelli come YOLO-NAS, SAM e RT-DETR. Ogni versione è ottimizzata per varie attività come detection, segmentation e classificazione. Per informazioni dettagliate su ciascun modello, consultare la documentazione Modelli supportati da Ultralytics.

Ultralytics Platform fornisce una piattaforma no-code end-to-end per l'addestramento, il deployment e la gestione dei modelli YOLO. Semplifica i flussi di lavoro complessi, consentendo agli utenti di concentrarsi sulle prestazioni e sull'applicazione del modello. La piattaforma offre anche capacità di addestramento su cloud, una gestione completa dei dataset e interfacce intuitive sia per i principianti che per gli sviluppatori esperti.

I modelli Ultralytics YOLO sono versatili e possono eseguire compiti quali il rilevamento di oggetti, la segmentazione di istanze, la classificazione, la stima della posa e il rilevamento di oggetti orientati (OBB). L'ultimo modello, YOLO26, supporta tutte e cinque le attività più il rilevamento a vocabolario aperto. Per i dettagli sulle attività specifiche, fare riferimento alle pagine delle attività.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a YOLO model
model = YOLO("yolo26n.pt")  # or any other YOLO model

# Train the model on custom dataset
results = model.train(data="custom_data.yaml", epochs=100, imgsz=640)
```

Example 4 (unknown):
```unknown
yolo train model=yolo26n.pt data='custom_data.yaml' epochs=100 imgsz=640
```

---

## Models Supported by Ultralytics

**URL:** https://docs.ultralytics.com/models/

**Contents:**
- Models Supported by Ultralytics
- Featured Models
- Getting Started: Usage Examples
- Contributing New Models
- FAQ
  - What is the latest Ultralytics YOLO model?
  - How can I train a YOLO model on custom data?
  - Which YOLO versions are supported by Ultralytics?
  - Why should I use Ultralytics Platform for machine learning projects?
  - What types of tasks can Ultralytics YOLO models perform?

Welcome to Ultralytics' model documentation! We offer support for a wide range of models, each tailored to specific tasks like object detection, instance segmentation, image classification, pose estimation, and multi-object tracking. If you're interested in contributing your model architecture to Ultralytics, check out our Contributing Guide.

Here are some of the key models supported:

Watch: Run Ultralytics YOLO models in just a few lines of code.

This example provides simple YOLO training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

Note the below example spotlights YOLO11 Detect models for object detection. For additional supported tasks see the Segment, Classify and Pose docs.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO(), SAM(), NAS() and RTDETR() classes to create a model instance in Python:

CLI commands are available to directly run the models:

Interested in contributing your model to Ultralytics? Great! We're always open to expanding our model portfolio.

Fork the Repository: Start by forking the Ultralytics GitHub repository.

Clone Your Fork: Clone your fork to your local machine and create a new branch to work on.

Implement Your Model: Add your model following the coding standards and guidelines provided in our Contributing Guide.

Test Thoroughly: Make sure to test your model rigorously, both in isolation and as part of the pipeline.

Create a Pull Request: Once you're satisfied with your model, create a pull request to the main repository for review.

Code Review & Merging: After review, if your model meets our criteria, it will be merged into the main repository.

For detailed steps, consult our Contributing Guide.

The latest Ultralytics YOLO model is YOLO26, released in January 2026. YOLO26 features end-to-end NMS-free inference, optimized edge deployment, and supports all five tasks (detection, segmentation, classification, pose estimation, and OBB) plus open-vocabulary versions. For stable production workloads, both YOLO26 and YOLO11 are recommended choices.

Training a YOLO model on custom data can be easily accomplished using Ultralytics' libraries. Here's a quick example:

For more detailed instructions, visit the Train documentation page.

Ultralytics supports a comprehensive range of YOLO (You Only Look Once) versions from YOLOv3 to YOLO11, along with models like YOLO-NAS, SAM, and RT-DETR. Each version is optimized for various tasks such as detection, segmentation, and classification. For detailed information on each model, refer to the Models Supported by Ultralytics documentation.

Ultralytics Platform provides a no-code, end-to-end platform for training, deploying, and managing YOLO models. It simplifies complex workflows, enabling users to focus on model performance and application. The HUB also offers cloud training capabilities, comprehensive dataset management, and user-friendly interfaces for both beginners and experienced developers.

Ultralytics YOLO models are versatile and can perform tasks including object detection, instance segmentation, classification, pose estimation, and oriented object detection (OBB). The latest model, YOLO26, supports all five tasks plus open-vocabulary detection. For details on specific tasks, refer to the Task pages.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a YOLO model
model = YOLO("yolo26n.pt")  # or any other YOLO model

# Train the model on custom dataset
results = model.train(data="custom_data.yaml", epochs=100, imgsz=640)
```

Example 4 (unknown):
```unknown
yolo train model=yolo26n.pt data='custom_data.yaml' epochs=100 imgsz=640
```

---

## SAM 2: Segment Anything Model 2

**URL:** https://docs.ultralytics.com/models/sam-2/

**Contents:**
- SAM 2: Segment Anything Model 2
- Key Features
  - Unified Model Architecture
  - Real-Time Performance
  - Zero-Shot Generalization
  - Interactive Refinement
  - Advanced Handling of Visual Challenges
- Performance and Technical Details
- Model Architecture
  - Core Components

SAM 2 builds upon the original SAM with video segmentation capabilities. For Promptable Concept Segmentation with text and image exemplar prompts, see SAM 3.

SAM 2, the successor to Meta's Segment Anything Model (SAM), is a cutting-edge tool designed for comprehensive object segmentation in both images and videos. It excels in handling complex visual data through a unified, promptable model architecture that supports real-time processing and zero-shot generalization.

Watch: How to Run Inference with Meta's SAM2 using Ultralytics | Step-by-Step Guide 🎉

SAM 2 combines the capabilities of image and video segmentation in a single model. This unification simplifies deployment and allows for consistent performance across different media types. It leverages a flexible prompt-based interface, enabling users to specify objects of interest through various prompt types, such as points, bounding boxes, or masks.

The model achieves real-time inference speeds, processing approximately 44 frames per second. This makes SAM 2 suitable for applications requiring immediate feedback, such as video editing and augmented reality.

SAM 2 can segment objects it has never encountered before, demonstrating strong zero-shot generalization. This is particularly useful in diverse or evolving visual domains where pre-defined categories may not cover all possible objects.

Users can iteratively refine the segmentation results by providing additional prompts, allowing for precise control over the output. This interactivity is essential for fine-tuning results in applications like video annotation or medical imaging.

SAM 2 includes mechanisms to manage common video segmentation challenges, such as object occlusion and reappearance. It uses a sophisticated memory mechanism to keep track of objects across frames, ensuring continuity even when objects are temporarily obscured or exit and re-enter the scene.

For a deeper understanding of SAM 2's architecture and capabilities, explore the SAM 2 research paper.

SAM 2 sets a new benchmark in the field, outperforming previous models on various metrics:

The memory mechanism allows SAM 2 to handle temporal dependencies and occlusions in video data. As objects move and interact, SAM 2 records their features in a memory bank. When an object becomes occluded, the model can rely on this memory to predict its position and appearance when it reappears. The occlusion head specifically handles scenarios where objects are not visible, predicting the likelihood of an object being occluded.

In situations with ambiguity (e.g., overlapping objects), SAM 2 can generate multiple mask predictions. This feature is crucial for accurately representing complex scenes where a single mask might not sufficiently describe the scene's nuances.

The SA-V dataset, developed for SAM 2's training, is one of the largest and most diverse video segmentation datasets available. It includes:

SAM 2 has demonstrated superior performance across major video segmentation benchmarks:

In interactive segmentation tasks, SAM 2 shows significant efficiency and accuracy:

To install SAM 2, use the following command. All SAM 2 models will automatically download on first use.

The following table details the available SAM 2 models, their pretrained weights, supported tasks, and compatibility with different operating modes like Inference, Validation, Training, and Export.

SAM 2 can be utilized across a broad spectrum of tasks, including real-time video editing, medical imaging, and autonomous systems. Its ability to segment both static and dynamic visual data makes it a versatile tool for researchers and developers.

Use prompts to segment specific objects in images or videos.

Segment the entire image or video content without specific prompts.

Segment the entire video content with specific prompts and track objects.

SAM2DynamicInteractivePredictor is an advanced training-free extension of SAM2 that enables dynamic interaction with multiple frames and continual learning capabilities. This predictor supports real-time prompt updates and memory management for improved tracking performance across a sequence of images. Compared to the original SAM2, SAM2DynamicInteractivePredictor rebuilds the inference flow to make the best use of pretrained SAM2 models without requiring additional training.

It offers three significant enhancements:

Dynamic Object Addition

The SAM2DynamicInteractivePredictor is designed to work with SAM2 models, and support adding/refining categories by all the box/point/mask prompts natively that SAM2 supports. It is particularly useful for scenarios where objects appear or change over time, such as in video annotation or interactive editing tasks.

SAM2DynamicInteractivePredictor is ideal for:

Here we compare Meta's SAM 2 models, including the smallest SAM2-t variant, with Ultralytics smallest segmentation model, YOLO11n-seg:

This comparison demonstrates the substantial differences in model sizes and speeds between SAM variants and YOLO segmentation models. While SAM provides unique automatic segmentation capabilities, YOLO models, particularly YOLOv8n-seg and YOLO11n-seg, are significantly smaller, faster, and more computationally efficient.

Tests run on a 2025 Apple M4 Pro with 24GB of RAM using torch==2.6.0 and ultralytics==8.3.90. To reproduce this test:

Auto-annotation is a powerful feature of SAM 2, enabling users to generate segmentation datasets quickly and accurately by leveraging pretrained models. This capability is particularly useful for creating large, high-quality datasets without extensive manual effort.

Watch: Auto Annotation with Meta's Segment Anything 2 Model using Ultralytics | Data Labeling

To auto-annotate your dataset using SAM 2, follow this example:

Auto-Annotation Example

This function facilitates the rapid creation of high-quality segmentation datasets, ideal for researchers and developers aiming to accelerate their projects.

Despite its strengths, SAM 2 has certain limitations:

If SAM 2 is a crucial part of your research or development work, please cite it using the following reference:

We extend our gratitude to Meta AI for their contributions to the AI community with this groundbreaking model and dataset.

SAM 2, the successor to Meta's Segment Anything Model (SAM), is a cutting-edge tool designed for comprehensive object segmentation in both images and videos. It excels in handling complex visual data through a unified, promptable model architecture that supports real-time processing and zero-shot generalization. SAM 2 offers several improvements over the original SAM, including:

For more details on SAM 2's architecture and capabilities, explore the SAM 2 research paper.

SAM 2 can be utilized for real-time video segmentation by leveraging its promptable interface and real-time inference capabilities. Here's a basic example:

Use prompts to segment specific objects in images or videos.

For more comprehensive usage, refer to the How to Use SAM 2 section.

SAM 2 is trained on the SA-V dataset, one of the largest and most diverse video segmentation datasets available. The SA-V dataset includes:

This extensive dataset allows SAM 2 to achieve superior performance across major video segmentation benchmarks and enhances its zero-shot generalization capabilities. For more information, see the SA-V Dataset section.

SAM 2 includes a sophisticated memory mechanism to manage temporal dependencies and occlusions in video data. The memory mechanism consists of:

This mechanism ensures continuity even when objects are temporarily obscured or exit and re-enter the scene. For more details, refer to the Memory Mechanism and Occlusion Handling section.

SAM 2 models, such as Meta's SAM2-t and SAM2-b, offer powerful zero-shot segmentation capabilities but are significantly larger and slower compared to YOLO11 models. For instance, YOLO11n-seg is approximately 13 times smaller and over 860 times faster than SAM2-b. While SAM 2 excels in versatile, prompt-based, and zero-shot segmentation scenarios, YOLO11 is optimized for speed, efficiency, and real-time applications, making it better suited for deployment in resource-constrained environments.

**Examples:**

Example 1 (unknown):
```unknown
pip install ultralytics
```

Example 2 (python):
```python
from ultralytics import SAM

# Load a model
model = SAM("sam2.1_b.pt")

# Display model information (optional)
model.info()

# Run inference with bboxes prompt
results = model("path/to/image.jpg", bboxes=[100, 100, 200, 200])

# Run inference with single point
results = model(points=[900, 370], labels=[1])

# Run inference with multiple points
results = model(points=[[400, 370], [900, 370]], labels=[1, 1])

# Run inference with multiple points prompt per object
results = model(points=[[[400, 370], [900, 370]]], labels=[[1, 1]])

# Run inference with negative points prompt
results = model(points=[[[400, 370], [900, 370]]], labels=[[1, 0]])
```

Example 3 (python):
```python
from ultralytics import SAM

# Load a model
model = SAM("sam2.1_b.pt")

# Display model information (optional)
model.info()

# Run inference
model("path/to/video.mp4")
```

Example 4 (markdown):
```markdown
# Run inference with a SAM 2 model
yolo predict model=sam2.1_b.pt source=path/to/video.mp4
```

---

## SAM 3: Segmenta qualsiasi cosa con i concetti

**URL:** https://docs.ultralytics.com/it/models/sam-3/

**Contents:**
- SAM 3: Segmenta qualsiasi cosa con i concetti
- Panoramica
  - Cos'è la Segmentazione Concettuale Richiedibile (Promptable Concept Segmentation, PCS)?
  - Principali Metriche di Performance
- Architettura
  - Componenti Principali
  - Innovazioni Chiave
- Dataset SA-Co
  - Dati di addestramento
  - Dati di benchmark

Ora Disponibile in Ultralytics

SAM 3 è completamente integrato nel pacchetto Ultralytics a partire da versione 8.3.237 (PR #22897). Installa o aggiorna con pip install -U ultralytics per accedere a tutte le funzionalità di SAM 3, inclusa la segmentazione concettuale basata su testo, i prompt di esempio di immagini e il tracciamento video.

SAM 3 (Segment Anything Model 3) è il modello di base rilasciato da Meta per la Promptable Concept Segmentation (PCS). Basato su SAM 2, SAM 3 introduce una funzionalità fondamentalmente nuova: il detect, la segmentazione e il track di tutte le istanze di un concetto visivo specificato da prompt testuali, esemplari di immagini o entrambi. A differenza delle versioni precedenti di SAM che segmentano singoli oggetti per prompt, SAM 3 può trovare e segmentare ogni occorrenza di un concetto che appare ovunque in immagini o video, allineandosi con gli obiettivi di open-vocabulary nella moderna instance segmentation.

Guarda: Come usare Meta Segment Anything 3 con Ultralytics | Segmentation basata su prompt testuali su immagini e video

SAM 3 è ora completamente integrato nel ultralytics pacchetto, fornendo supporto nativo per la segmentazione concettuale con prompt testuali, prompt di esempio di immagini e funzionalità di tracciamento video.

SAM 3 ottiene un guadagno di prestazioni di 2× rispetto ai sistemi esistenti nella Promptable Concept Segmentation, mantenendo e migliorando le capacità di SAM 2 per la segmentazione visuale interattiva. Il modello eccelle nella segmentazione a vocabolario aperto, consentendo agli utenti di specificare i concetti utilizzando semplici sintagmi nominali (ad esempio, "scuolabus giallo", "gatto a strisce") o fornendo immagini di esempio dell'oggetto target. Queste funzionalità completano le pipeline pronte per la produzione che si basano su flussi di lavoro semplificati di predict e track.

L'attività PCS prende un concept prompt come input e restituisce maschere di segmentazione con identità univoche per tutte le istanze di oggetti corrispondenti. I concept prompt possono essere:

Questo si differenzia dai tradizionali prompt visivi (punti, riquadri, maschere) che segmentano solo una singola istanza specifica di un oggetto, come reso popolare dalla famiglia SAM originale.

Per il contesto sulle metriche del modello e i compromessi nella produzione, consulta approfondimenti sulla valutazione del modello e metriche di performance YOLO.

SAM 3 è composto da un detector e un tracker che condividono un backbone di visione Perception Encoder (PE). Questo design disaccoppiato evita conflitti tra compiti, consentendo sia il detection a livello di immagine che il track a livello di video, con un'interfaccia compatibile con l'utilizzo di Ultralytics Python e l'CLI.

Detector: Architettura basata su DETR per la concept detection a livello di immagine

Tracker: Segmentazione video basata sulla memoria ereditata da SAM 2

Token di Presenza: Un token globale appreso che prevede se il concetto target è presente nell'immagine/frame, migliorando la detection separando il riconoscimento dalla localizzazione.

SAM 3 è addestrato su Segment Anything with Concepts (SA-Co), il set di dati di segmentazione più grande e diversificato di Meta fino ad oggi, che si espande oltre i benchmark comuni come COCO e LVIS.

Il benchmark di valutazione SA-Co contiene 214.000 frasi uniche in 126.000 immagini e video, fornendo oltre 50 volte più concetti rispetto ai benchmark esistenti. Include:

Il motore dati scalabile human- and model-in-the-loop di SAM 3 raggiunge una produttività di annotazione 2× tramite:

SAM 3 è disponibile in Ultralytics versione 8.3.237 e successive. Installa o aggiorna con:

Pesi del Modello SAM 3 Richiesti

A differenza di altri modelli Ultralytics, i pesi di SAM 3 (sam3.pt) non sono scaricati automaticamente. È necessario prima richiedere l'accesso ai pesi del modello sulla pagina del modello SAM 3 su Hugging Face e poi, una volta approvato, scaricare il sam3.pt file. Posizionare il file scaricato sam3.pt nella directory di lavoro o specificare il percorso completo durante il caricamento del modello.

SAM 3 supporta sia i compiti di Promptable Concept Segmentation (PCS) che di Promptable Visual Segmentation (PVS) tramite diverse interfacce predittive:

Segmentazione concettuale basata su testo

Trova e segmenta tutte le istanze di un concetto utilizzando una descrizione testuale. I prompt testuali richiedono l' SAM3SemanticPredictor interfaccia.

Segmentazione basata su esemplari di immagini

Utilizza i bounding box come prompt visivi per trovare tutte le istanze simili. Questo richiede anche SAM3SemanticPredictor per la corrispondenza basata su concetti.

Riutilizzo delle Caratteristiche dell'Immagine per Query Multiple

Estrai le caratteristiche dell'immagine una volta e riutilizzale per query di segmentazione multiple per migliorare l'efficienza.

Tracciamento Video con Prompt Visivi

detect e track istanze di oggetti attraverso i fotogrammi video utilizzando prompt di bounding box.

Tracking Video con Query Semantiche

track tutte le istanze di concetti specificati dal testo attraverso i fotogrammi video.

SAM 3 mantiene la piena compatibilità retroattiva con il prompting visivo di SAM 2 per la segmentazione di oggetti singoli:

Prompt visivi di stile SAM 2

L'interfaccia base SAM si comporta esattamente come SAM 2, segmentando solo l'area specifica indicata da prompt visivi (punti, box o maschere).

Prompt Visivi vs Segmentazione di Concetti

L'utilizzo di SAM("sam3.pt") con prompt visivi (punti/box/maschere) segmenterà solo l'oggetto specifico in quella posizione, proprio come SAM 2. Per segment tutte le istanze di un concetto, usa SAM3SemanticPredictor con prompt testuali o esemplari come mostrato sopra.

SAM 3 ottiene risultati all'avanguardia in diversi benchmark, inclusi set di dati del mondo reale come LVIS e COCO per la segmentazione:

Esplora le opzioni di dataset per una rapida sperimentazione nei dataset Ultralytics.

SAM 3 mostra miglioramenti significativi rispetto a SAM 2 e allo stato dell'arte precedente nei benchmark video come DAVIS 2017 e YouTube-VOS:

SAM 3 eccelle nell'adattarsi a nuovi domini con esempi minimi, rilevante per i flussi di lavoro di AI incentrata sui dati:

Il prompting basato su concetti di SAM 3 con esemplari converge molto più velocemente del prompting visivo:

SAM 3 fornisce un conteggio accurato segmentando tutte le istanze, un requisito comune nel conteggio degli oggetti:

Qui confrontiamo le capacità di SAM 3 con i modelli SAM 2 e YOLO11:

SAM 3 introduce nuove metriche progettate per il compito PCS, che completano le misure familiari come il punteggio F1, la precisione e il richiamo.

La metrica principale che combina localizzazione e classificazione:

CGF1 = 100 × pmF1 × IL_MCC

Le metriche AP tradizionali non tengono conto della calibrazione, rendendo i modelli difficili da usare nella pratica. Valutando solo le predizioni con un livello di confidenza superiore a 0.5, le metriche di SAM 3 impongono una buona calibrazione e simulano i modelli di utilizzo nel mondo reale nei loop interattivi di predict e track.

L'head di presenza disaccoppia il riconoscimento dalla localizzazione, fornendo miglioramenti significativi:

L'head di presenza fornisce un aumento di +5,7 CGF1 (+9,9%), migliorando principalmente la capacità di riconoscimento (IL_MCC +6,5%).

I negativi difficili sono fondamentali per il riconoscimento a vocabolario aperto, migliorando IL_MCC del 54,5% (0,44 → 0,68).

Annotazioni umane di alta qualità forniscono grandi vantaggi rispetto ai soli dati sintetici o esterni. Per informazioni di base sulle pratiche di qualità dei dati, consultare raccolta e annotazione dei dati.

La capacità di segmentazione concettuale di SAM 3 abilita nuovi casi d'uso:

SAM 3 può essere combinato con modelli linguistici di grandi dimensioni multimodali (MLLM) per gestire query complesse che richiedono ragionamento, in modo simile ai sistemi a vocabolario aperto come OWLv2 e T-Rex.

SAM 3 Agent è in grado di gestire query che richiedono ragionamento:

L'MLLM propone semplici query di sintagmi nominali a SAM 3, analizza le maschere restituite e itera fino a quando non è soddisfatto.

Sebbene SAM 3 rappresenti un importante progresso, presenta alcune limitazioni:

SAM 3 è stato rilasciato da Meta il 20 novembre 2025 ed è completamente integrato in Ultralytics a partire dalla versione 8.3.237 (PR #22897). Il supporto completo è disponibile per la modalità predict e la modalità track.

Sì! SAM 3 è completamente integrato nel pacchetto Python Ultralytics, inclusa la segmentation concettuale, i prompt visivi in stile SAM 2 e il track di oggetti multipli in video.

PCS è una nuova attività introdotta in SAM 3 che segmenta tutte le istanze di un concetto visivo in un'immagine o in un video. A differenza della segmentazione tradizionale che mira a una specifica istanza di oggetto, PCS trova ogni occorrenza di una categoria. Per esempio:

Vedi informazioni di background correlate su object detection e instance segmentation.

SAM 3 mantiene la compatibilità con le versioni precedenti con il prompting visivo di SAM 2 aggiungendo al contempo funzionalità basate su concetti.

SAM 3 è addestrato sul set di dati Segment Anything with Concepts (SA-Co):

Dati di addestramento:

Questa massiccia scala e diversità consente la generalizzazione zero-shot superiore di SAM 3 attraverso concetti di vocabolario aperto.

SAM 3 e YOLO11 servono casi d'uso diversi:

SAM 3 è progettato per semplici sintagmi nominali (ad esempio, "mela rossa", "persona che indossa un cappello"). Per query complesse che richiedono ragionamento, combina SAM 3 con un MLLM come SAM 3 Agent:

Query semplici (SAM 3 nativo):

Query complesse (SAM 3 Agent con MLLM):

SAM 3 Agent ottiene 76.0 gIoU sulla convalida ReasonSeg (vs 65.0 il miglior risultato precedente, +16.9% di miglioramento) combinando la segmentazione di SAM 3 con le capacità di ragionamento MLLM.

Sul benchmark SA-Co/Gold con tripla annotazione umana:

SAM 3 ottiene prestazioni elevate, avvicinandosi all'accuratezza del livello umano nella segmentazione di concetti a vocabolario aperto, con il divario principalmente su concetti ambigui o soggettivi (ad esempio, "finestra piccola", "stanza accogliente").

**Examples:**

Example 1 (unknown):
```unknown
pip install -U ultralytics
```

Example 2 (sql):
```sql
from ultralytics.models.sam import SAM3SemanticPredictor

# Initialize predictor with configuration
overrides = dict(
    conf=0.25,
    task="segment",
    mode="predict",
    model="sam3.pt",
    half=True,  # Use FP16 for faster inference
    save=True,
)
predictor = SAM3SemanticPredictor(overrides=overrides)

# Set image once for multiple queries
predictor.set_image("path/to/image.jpg")

# Query with multiple text prompts
results = predictor(text=["person", "bus", "glasses"])

# Works with descriptive phrases
results = predictor(text=["person with red cloth", "person with blue cloth"])

# Query with a single concept
results = predictor(text=["a person"])
```

Example 3 (sql):
```sql
from ultralytics.models.sam import SAM3SemanticPredictor

# Initialize predictor
overrides = dict(conf=0.25, task="segment", mode="predict", model="sam3.pt", half=True, save=True)
predictor = SAM3SemanticPredictor(overrides=overrides)

# Set image
predictor.set_image("path/to/image.jpg")

# Provide bounding box examples to segment similar objects
results = predictor(bboxes=[[480.0, 290.0, 590.0, 650.0]])

# Multiple bounding boxes for different concepts
results = predictor(bboxes=[[539, 599, 589, 639], [343, 267, 499, 662]])
```

Example 4 (python):
```python
import cv2

from ultralytics.models.sam import SAM3SemanticPredictor
from ultralytics.utils.plotting import Annotator, colors

# Initialize predictors
overrides = dict(conf=0.50, task="segment", mode="predict", model="sam3.pt", verbose=False)
predictor = SAM3SemanticPredictor(overrides=overrides)
predictor2 = SAM3SemanticPredictor(overrides=overrides)

# Extract features from the first predictor
source = "path/to/image.jpg"
predictor.set_image(source)
src_shape = cv2.imread(source).shape[:2]

# Setup second predictor and reuse features
predictor2.setup_model()

# Perform inference using shared features with text prompt
masks, boxes = predictor2.inference_features(predictor.features, src_shape=src_shape, text=["person"])

# Perform inference using shared features with bounding box prompt
masks, boxes = predictor2.inference_features(predictor.features, src_shape=src_shape, bboxes=[[439, 437, 524, 709]])

# Visualize results
if masks is not None:
    masks, boxes = masks.cpu().numpy(), boxes.cpu().numpy()
    im = cv2.imread(source)
    annotator = Annotator(im, pil=False)
    annotator.masks(masks, [colors(x, True) for x in range(len(masks))])

    cv2.imshow("result", annotator.result())
    cv2.waitKey(0)
```

---

## SAM 3: Segment Anything with Concepts

**URL:** https://docs.ultralytics.com/models/sam-3/

**Contents:**
- SAM 3: Segment Anything with Concepts
- Overview
  - What is Promptable Concept Segmentation (PCS)?
  - Key Performance Metrics
- Architecture
  - Core Components
  - Key Innovations
- SA-Co Dataset
  - Training Data
  - Benchmark Data

Now Available in Ultralytics

SAM 3 is fully integrated into the Ultralytics package as of version 8.3.237 (PR #22897). Install or upgrade with pip install -U ultralytics to access all SAM 3 features including text-based concept segmentation, image exemplar prompts, and video tracking.

SAM 3 (Segment Anything Model 3) is Meta's released foundation model for Promptable Concept Segmentation (PCS). Building upon SAM 2, SAM 3 introduces a fundamentally new capability: detecting, segmenting, and tracking all instances of a visual concept specified by text prompts, image exemplars, or both. Unlike previous SAM versions that segment single objects per prompt, SAM 3 can find and segment every occurrence of a concept appearing anywhere in images or videos, aligning with open-vocabulary goals in modern instance segmentation.

Watch: How to Use Meta Segment Anything 3 with Ultralytics | Text-Prompt Segmentation on Images & Videos

SAM 3 is now fully integrated into the ultralytics package, providing native support for concept segmentation with text prompts, image exemplar prompts, and video tracking capabilities.

SAM 3 achieves a 2× performance gain over existing systems in Promptable Concept Segmentation while maintaining and improving SAM 2's capabilities for interactive visual segmentation. The model excels at open-vocabulary segmentation, allowing users to specify concepts using simple noun phrases (e.g., "yellow school bus", "striped cat") or by providing example images of the target object. These capabilities complement production-ready pipelines that rely on streamlined predict and track workflows.

The PCS task takes a concept prompt as input and returns segmentation masks with unique identities for all matching object instances. Concept prompts can be:

This differs from traditional visual prompts (points, boxes, masks) which segment only a single specific object instance, as popularized by the original SAM family.

For context on model metrics and trade-offs in production, see model evaluation insights and YOLO performance metrics.

SAM 3 consists of a detector and tracker that share a Perception Encoder (PE) vision backbone. This decoupled design avoids task conflicts while enabling both image-level detection and video-level tracking, with an interface compatible with Ultralytics Python usage and CLI usage.

Detector: DETR-based architecture for image-level concept detection

Tracker: Memory-based video segmentation inherited from SAM 2

Presence Token: A learned global token that predicts whether the target concept is present in the image/frame, improving detection by separating recognition from localization.

SAM 3 is trained on Segment Anything with Concepts (SA-Co), Meta's largest and most diverse segmentation dataset to date, expanding beyond common benchmarks like COCO and LVIS.

The SA-Co evaluation benchmark contains 214K unique phrases across 126K images and videos, providing over 50× more concepts than existing benchmarks. It includes:

SAM 3's scalable human- and model-in-the-loop data engine achieves 2× annotation throughput through:

SAM 3 is available in Ultralytics version 8.3.237 and later. Install or upgrade with:

SAM 3 Model Weights Required

Unlike other Ultralytics models, SAM 3 weights (sam3.pt) are not automatically downloaded. You must first request access for the model weights on the SAM 3 model page on Hugging Face and then, once approved, download the sam3.pt file. Place the downloaded sam3.pt file in your working directory or specify the full path when loading the model.

SAM 3 supports both Promptable Concept Segmentation (PCS) and Promptable Visual Segmentation (PVS) tasks through different predictor interfaces:

Text-based Concept Segmentation

Find and segment all instances of a concept using a text description. Text prompts require the SAM3SemanticPredictor interface.

Image Exemplar-based Segmentation

Use bounding boxes as visual prompts to find all similar instances. This also requires SAM3SemanticPredictor for concept-based matching.

Reusing Image Features for Multiple Queries

Extract image features once and reuse them for multiple segmentation queries to improve efficiency.

Video Tracking with Visual Prompts

Detect and track object instances across video frames using bounding box prompts.

Video Tracking with Semantic Queries

Track all instances of concepts specified by text across video frames.

SAM 3 maintains full backward compatibility with SAM 2's visual prompting for single-object segmentation:

SAM 2 Style Visual Prompts

The basic SAM interface behaves exactly like SAM 2, segmenting only the specific area indicated by visual prompts (points, boxes, or masks).

Visual Prompts vs Concept Segmentation

Using SAM("sam3.pt") with visual prompts (points/boxes/masks) will segment only the specific object at that location, just like SAM 2. To segment all instances of a concept, use SAM3SemanticPredictor with text or exemplar prompts as shown above.

SAM 3 achieves state-of-the-art results across multiple benchmarks, including real-world datasets like LVIS and COCO for segmentation:

Explore dataset options for quick experimentation in Ultralytics datasets.

SAM 3 shows significant improvements over SAM 2 and prior state-of-the-art across video benchmarks such as DAVIS 2017 and YouTube-VOS:

SAM 3 excels at adapting to new domains with minimal examples, relevant for data-centric AI workflows:

SAM 3's concept-based prompting with exemplars converges much faster than visual prompting:

SAM 3 provides accurate counting by segmenting all instances, a common requirement in object counting:

Here we compare SAM 3's capabilities with SAM 2 and YOLO11 models:

SAM 3 introduces new metrics designed for the PCS task, complementing familiar measures like F1 score, precision, and recall.

The primary metric combining localization and classification:

CGF1 = 100 × pmF1 × IL_MCC

Traditional AP metrics don't account for calibration, making models difficult to use in practice. By evaluating only predictions above 0.5 confidence, SAM 3's metrics enforce good calibration and mimic real-world usage patterns in interactive predict and track loops.

The presence head decouples recognition from localization, providing significant improvements:

The presence head provides a +5.7 CGF1 boost (+9.9%), primarily improving recognition ability (IL_MCC +6.5%).

Hard negatives are crucial for open-vocabulary recognition, improving IL_MCC by 54.5% (0.44 → 0.68).

High-quality human annotations provide large gains over synthetic or external data alone. For background on data quality practices, see data collection and annotation.

SAM 3's concept segmentation capability enables new use cases:

SAM 3 can be combined with Multimodal Large Language Models (MLLMs) to handle complex queries requiring reasoning, similar in spirit to open-vocabulary systems like OWLv2 and T-Rex.

SAM 3 Agent can handle queries requiring reasoning:

The MLLM proposes simple noun phrase queries to SAM 3, analyzes returned masks, and iterates until satisfied.

While SAM 3 represents a major advancement, it has certain limitations:

SAM 3 was released by Meta on November 20th, 2025 and is fully integrated into Ultralytics as of version 8.3.237 (PR #22897). Full support is available for predict mode and track mode.

Yes! SAM 3 is fully integrated into the Ultralytics Python package, including concept segmentation, SAM 2–style visual prompts, and multi-object video tracking.

PCS is a new task introduced in SAM 3 that segments all instances of a visual concept in an image or video. Unlike traditional segmentation that targets a specific object instance, PCS finds every occurrence of a category. For example:

See related background on object detection and instance segmentation.

SAM 3 maintains backward compatibility with SAM 2 visual prompting while adding concept-based capabilities.

SAM 3 is trained on the Segment Anything with Concepts (SA-Co) dataset:

This massive scale and diversity enables SAM 3's superior zero-shot generalization across open-vocabulary concepts.

SAM 3 and YOLO11 serve different use cases:

SAM 3 is designed for simple noun phrases (e.g., "red apple", "person wearing hat"). For complex queries requiring reasoning, combine SAM 3 with an MLLM as SAM 3 Agent:

Simple queries (native SAM 3):

Complex queries (SAM 3 Agent with MLLM):

SAM 3 Agent achieves 76.0 gIoU on ReasonSeg validation (vs 65.0 previous best, +16.9% improvement) by combining SAM 3's segmentation with MLLM reasoning capabilities.

On the SA-Co/Gold benchmark with triple human annotation:

SAM 3 achieves strong performance approaching human-level accuracy on open-vocabulary concept segmentation, with the gap primarily on ambiguous or subjective concepts (e.g., "small window", "cozy room").

**Examples:**

Example 1 (unknown):
```unknown
pip install -U ultralytics
```

Example 2 (sql):
```sql
from ultralytics.models.sam import SAM3SemanticPredictor

# Initialize predictor with configuration
overrides = dict(
    conf=0.25,
    task="segment",
    mode="predict",
    model="sam3.pt",
    half=True,  # Use FP16 for faster inference
    save=True,
)
predictor = SAM3SemanticPredictor(overrides=overrides)

# Set image once for multiple queries
predictor.set_image("path/to/image.jpg")

# Query with multiple text prompts
results = predictor(text=["person", "bus", "glasses"])

# Works with descriptive phrases
results = predictor(text=["person with red cloth", "person with blue cloth"])

# Query with a single concept
results = predictor(text=["a person"])
```

Example 3 (sql):
```sql
from ultralytics.models.sam import SAM3SemanticPredictor

# Initialize predictor
overrides = dict(conf=0.25, task="segment", mode="predict", model="sam3.pt", half=True, save=True)
predictor = SAM3SemanticPredictor(overrides=overrides)

# Set image
predictor.set_image("path/to/image.jpg")

# Provide bounding box examples to segment similar objects
results = predictor(bboxes=[[480.0, 290.0, 590.0, 650.0]])

# Multiple bounding boxes for different concepts
results = predictor(bboxes=[[539, 599, 589, 639], [343, 267, 499, 662]])
```

Example 4 (python):
```python
import cv2

from ultralytics.models.sam import SAM3SemanticPredictor
from ultralytics.utils.plotting import Annotator, colors

# Initialize predictors
overrides = dict(conf=0.50, task="segment", mode="predict", model="sam3.pt", verbose=False)
predictor = SAM3SemanticPredictor(overrides=overrides)
predictor2 = SAM3SemanticPredictor(overrides=overrides)

# Extract features from the first predictor
source = "path/to/image.jpg"
predictor.set_image(source)
src_shape = cv2.imread(source).shape[:2]

# Setup second predictor and reuse features
predictor2.setup_model()

# Perform inference using shared features with text prompt
masks, boxes = predictor2.inference_features(predictor.features, src_shape=src_shape, text=["person"])

# Perform inference using shared features with bounding box prompt
masks, boxes = predictor2.inference_features(predictor.features, src_shape=src_shape, bboxes=[[439, 437, 524, 709]])

# Visualize results
if masks is not None:
    masks, boxes = masks.cpu().numpy(), boxes.cpu().numpy()
    im = cv2.imread(source)
    annotator = Annotator(im, pil=False)
    annotator.masks(masks, [colors(x, True) for x in range(len(masks))])

    cv2.imshow("result", annotator.result())
    cv2.waitKey(0)
```

---

## SAM 3: segment أي شيء باستخدام المفاهيم

**URL:** https://docs.ultralytics.com/ar/models/sam-3/

**Contents:**
- SAM 3: segment أي شيء باستخدام المفاهيم
- نظرة عامة
  - ما هو تجزئة المفهوم القابل للتوجيه (PCS)؟
  - مقاييس الأداء الرئيسية
- البنية
  - المكونات الأساسية
  - الابتكارات الرئيسية
- مجموعة بيانات SA-Co
  - بيانات التدريب
  - بيانات مرجعية

متوفر الآن في Ultralytics

تم دمج SAM 3 بالكامل في حزمة Ultralytics اعتبارًا من الإصدار 8.3.237 (PR #22897). قم بالتثبيت أو الترقية باستخدام pip install -U ultralytics للوصول إلى جميع ميزات SAM 3 بما في ذلك تجزئة المفاهيم المستندة إلى النص، ومطالبات أمثلة الصور، وتتبع الفيديو.

SAM 3 (نموذج تجزئة أي شيء 3) هو النموذج الأساسي الذي أصدرته Meta لـ تجزئة المفاهيم القابلة للتوجيه (PCS). بناءً على SAM 2، يقدم SAM 3 قدرة جديدة جوهرية: detect، segment، وtrack جميع حالات المفهوم البصري المحدد بواسطة مطالبات نصية، أو أمثلة صور، أو كليهما. على عكس إصدارات SAM السابقة التي تقوم بتجزئة كائنات فردية لكل مطالبة، يمكن لـ SAM 3 العثور على كل تكرار لمفهوم يظهر في أي مكان في الصور أو مقاطع الفيديو وتجزئته، بما يتماشى مع أهداف المفردات المفتوحة في تجزئة الحالات الحديثة.

شاهد: كيفية استخدام Meta Segment Anything 3 مع Ultralytics | تجزئة الصور ومقاطع الفيديو بناءً على المطالبات النصية

تم دمج SAM 3 الآن بالكامل في ultralytics الحزمة، مما يوفر دعمًا أصليًا لتجزئة المفاهيم باستخدام المطالبات النصية، ومطالبات أمثلة الصور، وقدرات تتبع الفيديو.

يحقق SAM 3 مكسبًا في الأداء بمقدار الضعف مقارنة بالأنظمة الحالية في تقسيم المفاهيم القابلة للمطالبة مع الحفاظ على قدرات SAM 2 وتحسينها للـ تقسيم المرئي التفاعلي. يتفوق النموذج في تقسيم المفردات المفتوحة، مما يسمح للمستخدمين بتحديد المفاهيم باستخدام عبارات اسمية بسيطة (مثل "حافلة مدرسية صفراء"، "قطة مخططة") أو عن طريق تقديم أمثلة لصور الجسم المستهدف. تكمل هذه القدرات خطوط الإنتاج الجاهزة التي تعتمد على التنبؤ و تتبع سير العمل المبسط.

تأخذ مهمة PCS موجه مفهوم كمدخل وتعيد أقنعة تجزئة بهويات فريدة لـ جميع مثيلات الكائنات المطابقة. يمكن أن تكون مطالبات المفهوم:

يختلف هذا عن المطالبات المرئية التقليدية (النقاط والمربعات والأقنعة) التي تقوم بتقسيم مثيل كائن معين واحد فقط، كما هو شائع في عائلة SAM الأصلية.

للاطلاع على سياق حول مقاييس النموذج والمفاضلات في الإنتاج، راجع رؤى تقييم النموذج و مقاييس أداء YOLO.

يتكون SAM 3 من detector و tracker يشتركان في العمود الفقري للرؤية Perception Encoder (PE). يتجنب هذا التصميم المنفصل تعارضات المهام مع تمكين كل من الكشف على مستوى الصورة وتتبع الفيديو على مستوى الفيديو، مع واجهة متوافقة مع استخدام python و استخدام CLI من Ultralytics.

الكاشف: بنية تعتمد على DETR للكشف عن المفاهيم على مستوى الصورة

أداة التتبع: تجزئة الفيديو المستندة إلى الذاكرة والموروثة من SAM 2

رمز الحضور: رمز عام مُدرَّب يتنبأ بما إذا كان المفهوم المستهدف موجودًا في الصورة/الإطار، مما يحسن الـ detect عن طريق فصل التعرف على الموقع.

تم تدريب SAM 3 على Segment Anything with Concepts (SA-Co)، وهي أكبر مجموعة بيانات تجزئة وأكثرها تنوعًا حتى الآن من Meta، والتي تتوسع لتتجاوز المعايير الشائعة مثل COCO و LVIS.

يحتوي معيار التقييم SA-Co على 214 ألف عبارة فريدة عبر 126 ألف صورة ومقطع فيديو، مما يوفر أكثر من 50 ضعفًا من المفاهيم مقارنة بالمعايير الحالية. ويشمل:

محرك بيانات SAM 3 القابل للتطوير الذي يعتمد على الإنسان والنموذج في الحلقة يحقق إنتاجية تعليقات توضيحية مضاعفة من خلال:

يتوفر SAM 3 في Ultralytics الإصدار 8.3.237 والإصدارات الأحدث. قم بالتثبيت أو الترقية باستخدام:

أوزان نموذج SAM 3 مطلوبة

على عكس نماذج Ultralytics الأخرى، أوزان SAM 3 (sam3.pt) لا يتم تنزيلها تلقائيًا. يجب عليك أولاً طلب الوصول إلى أوزان النموذج على صفحة نموذج SAM 3 على Hugging Face ثم، بمجرد الموافقة، قم بتنزيل sam3.pt ملف. ضع الملف الذي تم تنزيله sam3.pt في دليل العمل الخاص بك أو حدد المسار الكامل عند تحميل النموذج.

يدعم SAM 3 كلاً من مهام تجزئة المفاهيم القابلة للتوجيه (PCS) وتجزئة المرئيات القابلة للتوجيه (PVS) من خلال واجهات تنبؤ مختلفة:

تقسيم المفاهيم المستندة إلى النصوص

ابحث و سيجمنت جميع حالات المفهوم باستخدام وصف نصي. تتطلب المطالبات النصية SAM3SemanticPredictor الواجهة.

تقطيع قائم على نموذج الصورة

استخدم مربعات الإحاطة كموجهات بصرية للعثور على جميع الكائنات المتشابهة. يتطلب هذا أيضًا SAM3SemanticPredictor للمطابقة القائمة على المفاهيم.

إعادة استخدام ميزات الصورة لاستعلامات متعددة

استخرج ميزات الصورة مرة واحدة وأعد استخدامها لاستعلامات segment متعددة لتحسين الكفاءة.

تتبع الفيديو باستخدام الموجهات البصرية

detect و track كائنات عبر إطارات الفيديو باستخدام موجهات مربعات الإحاطة.

تتبع الفيديو باستعلامات دلالية

track جميع كائنات المفاهيم المحددة بالنص عبر إطارات الفيديو.

يحافظ SAM 3 على التوافق الكامل مع الإصدارات السابقة مع التوجيه البصري لـ SAM 2 لـ segment الكائن الواحد:

مطالبات مرئية بنمط SAM 2

الواجهة الأساسية SAM تتصرف تمامًا مثل SAM 2، حيث تقوم بـ segment المنطقة المحددة فقط المشار إليها بواسطة الموجهات البصرية (النقاط، المربعات، أو الأقنعة).

الموجهات البصرية مقابل segment المفاهيم

استخدام SAM("sam3.pt") باستخدام الموجهات البصرية (النقاط/المربعات/الأقنعة) ستقوم بـ segment الكائن المحدد فقط في ذلك الموقع، تمامًا مثل SAM 2. لـ segment جميع كائنات المفهوم، استخدم SAM3SemanticPredictor باستخدام موجهات نصية أو أمثلة كما هو موضح أعلاه.

يحقق SAM 3 نتائج متطورة عبر معايير متعددة، بما في ذلك مجموعات البيانات الواقعية مثل LVIS و COCO للتقسيم:

استكشف خيارات مجموعة البيانات للتجربة السريعة في مجموعات بيانات Ultralytics.

يُظهر SAM 3 تحسينات كبيرة مقارنة بـ SAM 2 وأحدث التقنيات عبر معايير الفيديو مثل DAVIS 2017 و YouTube-VOS:

يتفوق SAM 3 في التكيف مع المجالات الجديدة بأقل عدد ممكن من الأمثلة، وهو أمر ذو صلة بسير عمل الذكاء الاصطناعي المرتكز على البيانات:

التحفيز المفهومي في SAM 3 مع النماذج يتقارب بسرعة أكبر بكثير من التحفيز البصري:

يوفر SAM 3 عدًا دقيقًا عن طريق تقسيم جميع الحالات، وهو مطلب شائع في عد الكائنات:

هنا نقارن قدرات SAM 3 مع SAM 2 ونماذج YOLO11:

يقدم SAM 3 مقاييس جديدة مصممة لمهمة PCS، تكمل المقاييس المألوفة مثل F1 score و precision و recall.

المقياس الأساسي الذي يجمع بين التوطين والتصنيف:

CGF1 = 100 × pmF1 × IL_MCC

لا تأخذ مقاييس AP التقليدية في الاعتبار المعايرة، مما يجعل استخدام النماذج صعبًا في الممارسة العملية. من خلال تقييم التوقعات التي تزيد عن 0.5 من الثقة فقط، تفرض مقاييس SAM 3 معايرة جيدة وتحاكي أنماط الاستخدام الواقعية في حلقات predict و track التفاعلية.

يفصل رأس التواجد بين التعرف والتموضع، مما يوفر تحسينات كبيرة:

يوفر رأس التواجد +5.7 CGF1 boost (+9.9%)، مما يحسن بشكل أساسي قدرة التعرف (IL_MCC +6.5%).

تعتبر السلبيات الصعبة ضرورية للتعرف على المفردات المفتوحة، مما يحسن IL_MCC بنسبة 54.5% (0.44 → 0.68).

توفر التعليقات التوضيحية البشرية عالية الجودة مكاسب كبيرة مقارنة بالبيانات الاصطناعية أو الخارجية وحدها. للحصول على معلومات أساسية حول ممارسات جودة البيانات، راجع جمع البيانات والتعليق عليها.

تتيح إمكانية تجزئة المفاهيم في SAM 3 حالات استخدام جديدة:

يمكن دمج SAM 3 مع نماذج اللغة الكبيرة متعددة الوسائط (MLLMs) للتعامل مع الاستعلامات المعقدة التي تتطلب الاستدلال، على غرار الأنظمة مفتوحة المفردات مثل OWLv2 و T-Rex.

يمكن لوكيل SAM 3 التعامل مع الاستعلامات التي تتطلب الاستدلال:

يقترح MLLM استعلامات بسيطة للعبارة الاسمية إلى SAM 3، ويحلل الأقنعة التي تم إرجاعها، ويكرر حتى يتم تحقيق الرضا.

في حين أن SAM 3 يمثل تقدمًا كبيرًا، إلا أن لديه بعض القيود:

تم إصدار SAM 3 بواسطة ميتا في 20 نوفمبر 2025 وتم دمجه بالكامل في Ultralytics اعتبارًا من الإصدار 8.3.237 (PR #22897). يتوفر الدعم الكامل لـ وضع التنبؤ ووضع التتبع.

نعم! تم دمج SAM 3 بالكامل في حزمة Ultralytics python، بما في ذلك تجزئة المفاهيم، والمطالبات المرئية على غرار SAM 2، و track الفيديو متعدد الكائنات.

PCS هي مهمة جديدة تم تقديمها في SAM 3 والتي تقوم بعملية segment لـ جميع الحالات لمفهوم مرئي في صورة أو مقطع فيديو. على عكس عملية segmentation التقليدية التي تستهدف مثيل كائن معين، تجد PCS كل تكرار لفئة. على سبيل المثال:

اطلع على معلومات أساسية ذات صلة حول الكشف عن الأجسام و تقسيم المثيلات.

يحافظ SAM 3 على التوافق مع الإصدارات السابقة مع المطالبة المرئية SAM 2 مع إضافة إمكانات قائمة على المفهوم.

تم تدريب SAM 3 على مجموعة البيانات Segment Anything with Concepts (SA-Co):

يمكّن هذا الحجم والتنوع الهائلان التعميم الصفري الفائق لـ SAM 3 عبر مفاهيم المفردات المفتوحة.

يخدم SAM 3 و YOLO11 حالات استخدام مختلفة:

تم تصميم SAM 3 لعبارات اسمية بسيطة (مثل "تفاحة حمراء"، "شخص يرتدي قبعة"). للاستعلامات المعقدة التي تتطلب الاستدلال، ادمج SAM 3 مع MLLM كـ SAM 3 Agent:

استعلامات بسيطة (SAM 3 الأصلي):

استعلامات معقدة (SAM 3 Agent مع MLLM):

يحقق وكيل SAM 3 76.0 gIoU في التحقق من صحة ReasonSeg (مقابل 65.0 الأفضل سابقًا، تحسن بنسبة +16.9٪) من خلال الجمع بين تقسيم SAM 3 وقدرات الاستدلال MLLM.

في معيار SA-Co/Gold مع التعليقات التوضيحية البشرية الثلاثية:

يحقق SAM 3 أداءً قويًا يقترب من دقة المستوى البشري في تقسيم المفاهيم ذات المفردات المفتوحة، مع وجود فجوة في المقام الأول في المفاهيم الغامضة أو الذاتية (مثل "نافذة صغيرة"، "غرفة مريحة").

**Examples:**

Example 1 (unknown):
```unknown
pip install -U ultralytics
```

Example 2 (sql):
```sql
from ultralytics.models.sam import SAM3SemanticPredictor

# Initialize predictor with configuration
overrides = dict(
    conf=0.25,
    task="segment",
    mode="predict",
    model="sam3.pt",
    half=True,  # Use FP16 for faster inference
    save=True,
)
predictor = SAM3SemanticPredictor(overrides=overrides)

# Set image once for multiple queries
predictor.set_image("path/to/image.jpg")

# Query with multiple text prompts
results = predictor(text=["person", "bus", "glasses"])

# Works with descriptive phrases
results = predictor(text=["person with red cloth", "person with blue cloth"])

# Query with a single concept
results = predictor(text=["a person"])
```

Example 3 (sql):
```sql
from ultralytics.models.sam import SAM3SemanticPredictor

# Initialize predictor
overrides = dict(conf=0.25, task="segment", mode="predict", model="sam3.pt", half=True, save=True)
predictor = SAM3SemanticPredictor(overrides=overrides)

# Set image
predictor.set_image("path/to/image.jpg")

# Provide bounding box examples to segment similar objects
results = predictor(bboxes=[[480.0, 290.0, 590.0, 650.0]])

# Multiple bounding boxes for different concepts
results = predictor(bboxes=[[539, 599, 589, 639], [343, 267, 499, 662]])
```

Example 4 (python):
```python
import cv2

from ultralytics.models.sam import SAM3SemanticPredictor
from ultralytics.utils.plotting import Annotator, colors

# Initialize predictors
overrides = dict(conf=0.50, task="segment", mode="predict", model="sam3.pt", verbose=False)
predictor = SAM3SemanticPredictor(overrides=overrides)
predictor2 = SAM3SemanticPredictor(overrides=overrides)

# Extract features from the first predictor
source = "path/to/image.jpg"
predictor.set_image(source)
src_shape = cv2.imread(source).shape[:2]

# Setup second predictor and reuse features
predictor2.setup_model()

# Perform inference using shared features with text prompt
masks, boxes = predictor2.inference_features(predictor.features, src_shape=src_shape, text=["person"])

# Perform inference using shared features with bounding box prompt
masks, boxes = predictor2.inference_features(predictor.features, src_shape=src_shape, bboxes=[[439, 437, 524, 709]])

# Visualize results
if masks is not None:
    masks, boxes = masks.cpu().numpy(), boxes.cpu().numpy()
    im = cv2.imread(source)
    annotator = Annotator(im, pil=False)
    annotator.masks(masks, [colors(x, True) for x in range(len(masks))])

    cv2.imshow("result", annotator.result())
    cv2.waitKey(0)
```

---

## Segment Anything Model (SAM)

**URL:** https://docs.ultralytics.com/models/sam/

**Contents:**
- Segment Anything Model (SAM)
- Introduction to SAM: The Segment Anything Model
- Key Features of the Segment Anything Model (SAM)
- Available Models, Supported Tasks, and Operating Modes
- How to Use SAM: Versatility and Power in Image Segmentation
  - SAM prediction example
- SAM Comparison vs YOLO
- Auto-Annotation: A Quick Path to Segmentation Datasets
  - Generate Your Segmentation Dataset Using a Detection Model
- Citations and Acknowledgments

This is the original SAM model from Meta. For improved capabilities, see SAM 2 for video segmentation or SAM 3 for Promptable Concept Segmentation with text and image exemplar prompts.

Welcome to the frontier of image segmentation with the Segment Anything Model, or SAM. This revolutionary model has changed the game by introducing promptable image segmentation with real-time performance, setting new standards in the field.

The Segment Anything Model, or SAM, is a cutting-edge image segmentation model that allows for promptable segmentation, providing unparalleled versatility in image analysis tasks. SAM forms the heart of the Segment Anything initiative, a groundbreaking project that introduces a novel model, task, and dataset for image segmentation.

SAM's advanced design allows it to adapt to new image distributions and tasks without prior knowledge, a feature known as zero-shot transfer. Trained on the expansive SA-1B dataset, which contains more than 1 billion masks spread over 11 million carefully curated images, SAM has displayed impressive zero-shot performance, surpassing previous fully supervised results in many cases.

SA-1B Example images. Dataset images overlaid masks from the newly introduced SA-1B dataset. SA-1B contains 11M diverse, high-resolution, licensed, and privacy protecting images and 1.1B high-quality segmentation masks. These masks were annotated fully automatically by SAM, and as verified by human ratings and numerous experiments, are of high quality and diversity. Images are grouped by number of masks per image for visualization (there are ∼100 masks per image on average).

For an in-depth look at the Segment Anything Model and the SA-1B dataset, please visit the Segment Anything GitHub and check out the research paper Segment Anything.

This table presents the available models with their specific pretrained weights, the tasks they support, and their compatibility with different operating modes like Inference, Validation, Training, and Export, indicated by ✅ emojis for supported modes and ❌ emojis for unsupported modes.

The Segment Anything Model can be employed for a multitude of downstream tasks that go beyond its training data. This includes edge detection, object proposal generation, instance segmentation, and preliminary text-to-mask prediction. With prompt engineering, SAM can swiftly adapt to new tasks and data distributions in a zero-shot manner, establishing it as a versatile and potent tool for all your image segmentation needs.

Segment image with given prompts.

Segment the whole image.

This way you can set image once and run prompts inference multiple times without running image encoder multiple times.

Segment everything with additional args.

All the returned results in above examples are Results object which allows access predicted masks and source image easily.

Here we compare Meta's SAM-b model with Ultralytics smallest segmentation model, YOLO11n-seg:

This comparison demonstrates the substantial differences in model sizes and speeds between SAM variants and YOLO segmentation models. While SAM provides unique automatic segmentation capabilities, YOLO models, particularly YOLOv8n-seg and YOLO11n-seg, are significantly smaller, faster, and more computationally efficient.

Tests run on a 2025 Apple M4 Pro with 24GB of RAM using torch==2.6.0 and ultralytics==8.3.90. To reproduce this test:

Auto-annotation is a key feature of SAM, allowing users to generate a segmentation dataset using a pretrained detection model. This feature enables rapid and accurate annotation of a large number of images, bypassing the need for time-consuming manual labeling.

To auto-annotate your dataset with the Ultralytics framework, use the auto_annotate function as shown below:

The auto_annotate function takes the path to your images, with optional arguments for specifying the pretrained detection and SAM segmentation models, the device to run the models on, and the output directory for saving the annotated results.

Auto-annotation with pretrained models can dramatically cut down the time and effort required for creating high-quality segmentation datasets. This feature is especially beneficial for researchers and developers dealing with large image collections, as it allows them to focus on model development and evaluation rather than manual annotation.

If you find SAM useful in your research or development work, please consider citing our paper:

We would like to express our gratitude to Meta AI for creating and maintaining this valuable resource for the computer vision community.

The Segment Anything Model (SAM) by Ultralytics is a revolutionary image segmentation model designed for promptable segmentation tasks. It leverages advanced architecture, including image and prompt encoders combined with a lightweight mask decoder, to generate high-quality segmentation masks from various prompts such as spatial or text cues. Trained on the expansive SA-1B dataset, SAM excels in zero-shot performance, adapting to new image distributions and tasks without prior knowledge.

You can use the Segment Anything Model (SAM) for image segmentation by running inference with various prompts such as bounding boxes or points. Here's an example using Python:

Alternatively, you can run inference with SAM in the command line interface (CLI):

For more detailed usage instructions, visit the Segmentation section.

Compared to YOLO models, SAM variants like SAM-b, SAM2-t, MobileSAM, and FastSAM-s are typically larger and slower but offer unique zero-shot segmentation capabilities. For example, Ultralytics YOLOv8n-seg is 11.7x smaller and 1069x faster than Meta's original SAM-b model, highlighting YOLO's significant advantage in speed and efficiency. Similarly, the newer YOLO11n-seg provides even smaller size and maintains impressive inference speed. This makes YOLO models ideal for applications requiring rapid, lightweight, and computationally efficient segmentation, while SAM models excel in flexible, promptable, and zero-shot segmentation tasks.

Ultralytics' SAM offers an auto-annotation feature that allows generating segmentation datasets using a pretrained detection model. Here's an example in Python:

This function takes the path to your images and optional arguments for pretrained detection and SAM segmentation models, along with device and output directory specifications. For a complete guide, see Auto-Annotation.

SAM is trained on the extensive SA-1B dataset which comprises over 1 billion masks across 11 million images. SA-1B is the largest segmentation dataset to date, providing high-quality and diverse training data, ensuring impressive zero-shot performance in varied segmentation tasks. For more details, visit the Dataset section.

**Examples:**

Example 1 (python):
```python
from ultralytics import SAM

# Load a model
model = SAM("sam_b.pt")

# Display model information (optional)
model.info()

# Run inference with bboxes prompt
results = model("ultralytics/assets/zidane.jpg", bboxes=[439, 437, 524, 709])

# Run inference with single point
results = model(points=[900, 370], labels=[1])

# Run inference with multiple points
results = model(points=[[400, 370], [900, 370]], labels=[1, 1])

# Run inference with multiple points prompt per object
results = model(points=[[[400, 370], [900, 370]]], labels=[[1, 1]])

# Run inference with negative points prompt
results = model(points=[[[400, 370], [900, 370]]], labels=[[1, 0]])
```

Example 2 (python):
```python
from ultralytics import SAM

# Load a model
model = SAM("sam_b.pt")

# Display model information (optional)
model.info()

# Run inference
model("path/to/image.jpg")
```

Example 3 (markdown):
```markdown
# Run inference with a SAM model
yolo predict model=sam_b.pt source=path/to/image.jpg
```

Example 4 (sql):
```sql
from ultralytics.models.sam import Predictor as SAMPredictor

# Create SAMPredictor
overrides = dict(conf=0.25, task="segment", mode="predict", imgsz=1024, model="mobile_sam.pt")
predictor = SAMPredictor(overrides=overrides)

# Set image
predictor.set_image("ultralytics/assets/zidane.jpg")  # set with image file
predictor.set_image(cv2.imread("ultralytics/assets/zidane.jpg"))  # set with np.ndarray
results = predictor(bboxes=[439, 437, 524, 709])

# Run inference with single point prompt
results = predictor(points=[900, 370], labels=[1])

# Run inference with multiple points prompt
results = predictor(points=[[400, 370], [900, 370]], labels=[1, 1])

# Run inference with negative points prompt
results = predictor(points=[[[400, 370], [900, 370]]], labels=[[1, 0]])

# Reset image
predictor.reset_image()
```

---

## Ultralytics YOLO11

**URL:** https://docs.ultralytics.com/ar/models/yolo11/

**Contents:**
- Ultralytics YOLO11
- نظرة عامة
- الميزات الرئيسية
- المهام والأوضاع المدعومة
- مقاييس الأداء
- أمثلة الاستخدام
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هي التحسينات الرئيسية في Ultralytics YOLO11 مقارنة بـ YOLOv8؟
  - كيف يمكنني تدريب نموذج YOLO11 للكشف عن الأجسام؟

تم إصدار YOLO11 بواسطة Ultralytics في 10 سبتمبر 2024، مقدمًا دقة وسرعة وكفاءة ممتازة. بناءً على التطورات الرائعة لإصدارات YOLO السابقة، يقدم YOLO11 تحسينات كبيرة في البنية وطرق التدريب، مما يجعله خيارًا متعدد الاستخدامات لمجموعة واسعة من مهام الرؤية الحاسوبية. للحصول على أحدث نموذج من Ultralytics مع استدلال خالٍ من NMS من البداية إلى النهاية ونشر مُحسّن على الحافة، راجع YOLO26.

Ultralytics YOLO11 🚀 تم إنشاء البودكاست بواسطة NotebookLM

شاهد: كيفية استخدام Ultralytics YOLO11 للكشف عن الأجسام وتتبعها | كيفية القياس | تم إصدار YOLO11 🚀

استكشف ونفذ YOLO11 مباشرة على Ultralytics .

يعتمد YOLO11 على مجموعة النماذج متعددة الاستخدامات التي أنشأتها إصدارات Ultralytics YOLO السابقة، مما يوفر دعمًا محسنًا عبر مهام رؤية الكمبيوتر المختلفة:

يقدم هذا الجدول نظرة عامة على متغيرات نموذج YOLO11، ويعرض قابليتها للتطبيق في مهام محددة وتوافقها مع أوضاع التشغيل مثل الاستدلال والتحقق والتدريب والتصدير. هذه المرونة تجعل YOLO11 مناسبًا لمجموعة واسعة من التطبيقات في رؤية الكمبيوتر، من الكشف في الوقت الفعلي إلى مهام التقسيم المعقدة.

راجع وثائق الكشف لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التجزئة لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التصنيف لأمثلة الاستخدام مع هذه النماذج المدربة على ImageNet، والتي تتضمن 1000 فئة مدربة مسبقًا.

راجع وثائق تقدير الوضعيات لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن فئة واحدة مدربة مسبقًا، وهي 'شخص'.

راجع وثائق الكشف الموجه لأمثلة الاستخدام مع هذه النماذج المدربة على DOTAv1، والتي تتضمن 15 فئة مدربة مسبقًا.

يوفر هذا القسم أمثلة بسيطة لتدريب واستدلال YOLO11. للحصول على وثائق كاملة حول هذه الأوضاع وغيرها، راجع صفحات وثائق التوقع و التدريب و التقييم و التصدير.

لاحظ أن المثال أدناه خاص بنماذج YOLO11 للكشف عن الأجسام. للحصول على مهام إضافية مدعومة، راجع وثائق التقسيم و التصنيف و OBB و الوضعية.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في Python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

منشور Ultralytics YOLO11

لم تنشر Ultralytics ورقة بحثية رسمية لـ YOLO11 نظرًا للطبيعة سريعة التطور للنماذج. نحن نركز على تطوير التكنولوجيا وتسهيل استخدامها، بدلاً من إنتاج وثائق ثابتة. للحصول على أحدث المعلومات حول بنية YOLO وميزاته واستخدامه، يرجى الرجوع إلى مستودع GitHub الخاص بنا و الوثائق.

إذا كنت تستخدم YOLO11 أو أي برنامج آخر من هذا المستودع في عملك، فيرجى الاستشهاد به باستخدام التنسيق التالي:

يرجى ملاحظة أن رقم DOI معلق وسيتم إضافته إلى الاقتباس بمجرد توفره. يتم توفير نماذج YOLO11 بموجب تراخيص AGPL-3.0 و Enterprise.

تقدم Ultralytics YOLO11 العديد من التطورات الهامة مقارنة بـ YOLOv8. تشمل التحسينات الرئيسية ما يلي:

يمكن تدريب نموذج YOLO11 للكشف عن الأجسام باستخدام أوامر Python أو CLI. فيما يلي أمثلة للطريقتين:

للحصول على تعليمات أكثر تفصيلاً، راجع وثائق التدريب.

تتميز نماذج YOLO11 بأنها متعددة الاستخدامات وتدعم مجموعة واسعة من مهام رؤية الكمبيوتر، بما في ذلك:

لمزيد من المعلومات حول كل مهمة، راجع وثائق الكشف، وتجزئة المثيلات، والتصنيف، وتقدير الوضعية، والكشف الموجه.

يحقق YOLO11 دقة أكبر مع عدد أقل من المعلمات من خلال التطورات في تصميم النموذج وتقنيات التحسين. تسمح البنية المحسنة باستخراج الميزات ومعالجتها بكفاءة، مما يؤدي إلى متوسط دقة أعلى (mAP) على مجموعات البيانات مثل COCO مع استخدام معلمات أقل بنسبة 22٪ من YOLOv8m. هذا يجعل YOLO11 فعالاً من الناحية الحسابية دون المساومة على الدقة، مما يجعله مناسبًا للنشر على الأجهزة ذات الموارد المحدودة.

نعم، تم تصميم YOLO11 للتكيف عبر بيئات مختلفة، بما في ذلك الأجهزة الطرفية. إن بنيتها المحسّنة وقدرات المعالجة الفعالة تجعلها مناسبة للنشر على الأجهزة الطرفية والمنصات السحابية والأنظمة التي تدعم وحدات معالجة الرسوميات NVIDIA GPUs. تضمن هذه المرونة إمكانية استخدام YOLO11 في تطبيقات متنوعة، بدءًا من الكشف في الوقت الفعلي على الأجهزة المحمولة وحتى مهام التجزئة المعقدة في البيئات السحابية. لمزيد من التفاصيل حول خيارات النشر، راجع وثائق التصدير.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO11n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo11n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO11n model and run inference on the 'bus.jpg' image
yolo predict model=yolo11n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolo11_ultralytics,
  author = {Glenn Jocher and Jing Qiu},
  title = {Ultralytics YOLO11},
  version = {11.0.0},
  year = {2024},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Ultralytics YOLO11

**URL:** https://docs.ultralytics.com/models/yolo11/

**Contents:**
- Ultralytics YOLO11
- Overview
- Key Features
- Supported Tasks and Modes
- Performance Metrics
- Usage Examples
- Citations and Acknowledgments
- FAQ
  - What are the key improvements in Ultralytics YOLO11 compared to YOLOv8?
  - How do I train a YOLO11 model for object detection?

YOLO11 was released by Ultralytics on September 10, 2024, delivering excellent accuracy, speed, and efficiency. Building upon the impressive advancements of previous YOLO versions, YOLO11 introduces significant improvements in architecture and training methods, making it a versatile choice for a wide range of computer vision tasks. For the latest Ultralytics model with end-to-end NMS-free inference and optimized edge deployment, see YOLO26.

Ultralytics YOLO11 🚀 Podcast generated by NotebookLM

Watch: How to Use Ultralytics YOLO11 for Object Detection and Tracking | How to Benchmark | YOLO11 RELEASED🚀

Try on Ultralytics Platform

Explore and run YOLO11 models directly on Ultralytics Platform.

YOLO11 builds upon the versatile model range established by earlier Ultralytics YOLO releases, offering enhanced support across various computer vision tasks:

This table provides an overview of the YOLO11 model variants, showcasing their applicability in specific tasks and compatibility with operational modes such as Inference, Validation, Training, and Export. This flexibility makes YOLO11 suitable for a wide range of applications in computer vision, from real-time detection to complex segmentation tasks.

See Detection Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Segmentation Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Classification Docs for usage examples with these models trained on ImageNet, which include 1000 pretrained classes.

See Pose Estimation Docs for usage examples with these models trained on COCO, which include 1 pretrained class, 'person'.

See Oriented Detection Docs for usage examples with these models trained on DOTAv1, which include 15 pretrained classes.

This section provides simple YOLO11 training and inference examples. For full documentation on these and other modes, see the Predict, Train, Val, and Export docs pages.

Note that the example below is for YOLO11 Detect models for object detection. For additional supported tasks, see the Segment, Classify, OBB, and Pose docs.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in Python:

CLI commands are available to directly run the models:

Ultralytics YOLO11 Publication

Ultralytics has not published a formal research paper for YOLO11 due to the rapidly evolving nature of the models. We focus on advancing the technology and making it easier to use, rather than producing static documentation. For the most up-to-date information on YOLO architecture, features, and usage, please refer to our GitHub repository and documentation.

If you use YOLO11 or any other software from this repository in your work, please cite it using the following format:

Please note that the DOI is pending and will be added to the citation once it is available. YOLO11 models are provided under AGPL-3.0 and Enterprise licenses.

Ultralytics YOLO11 introduces several significant advancements over YOLOv8. Key improvements include:

Training a YOLO11 model for object detection can be done using Python or CLI commands. Below are examples for both methods:

For more detailed instructions, refer to the Train documentation.

YOLO11 models are versatile and support a wide range of computer vision tasks, including:

For more information on each task, see the Detection, Instance Segmentation, Classification, Pose Estimation, and Oriented Detection documentation.

YOLO11 achieves greater accuracy with fewer parameters through advancements in model design and optimization techniques. The improved architecture allows for efficient feature extraction and processing, resulting in higher mean Average Precision (mAP) on datasets like COCO while using 22% fewer parameters than YOLOv8m. This makes YOLO11 computationally efficient without compromising on accuracy, making it suitable for deployment on resource-constrained devices.

Yes, YOLO11 is designed for adaptability across various environments, including edge devices. Its optimized architecture and efficient processing capabilities make it suitable for deployment on edge devices, cloud platforms, and systems supporting NVIDIA GPUs. This flexibility ensures that YOLO11 can be used in diverse applications, from real-time detection on mobile devices to complex segmentation tasks in cloud environments. For more details on deployment options, refer to the Export documentation.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO11n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo11n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO11n model and run inference on the 'bus.jpg' image
yolo predict model=yolo11n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolo11_ultralytics,
  author = {Glenn Jocher and Jing Qiu},
  title = {Ultralytics YOLO11},
  version = {11.0.0},
  year = {2024},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Ultralytics YOLO11

**URL:** https://docs.ultralytics.com/it/models/yolo11/

**Contents:**
- Ultralytics YOLO11
- Panoramica
- Caratteristiche principali
- Attività e modalità supportate
- Metriche di performance
- Esempi di utilizzo
- Citazioni e ringraziamenti
- FAQ
  - Quali sono i miglioramenti chiave in Ultralytics YOLO11 rispetto a YOLOv8?
  - Come posso addestrare un modello YOLO11 per il rilevamento di oggetti?

YOLO11 è stato rilasciato da Ultralytics il 10 settembre 2024, offrendo eccellente accuratezza, velocità ed efficienza. Basandosi sugli impressionanti progressi delle precedenti versioni di YOLO, YOLO11 introduce significativi miglioramenti nell'architettura e nei metodi di addestramento, rendendolo una scelta versatile per un'ampia gamma di attività di visione artificiale. Per l'ultimo modello Ultralytics con inferenza end-to-end senza NMS e deployment edge ottimizzato, vedi YOLO26.

Ultralytics YOLO11 🚀 Podcast generato da NotebookLM

Guarda: Come utilizzare Ultralytics YOLO11 per il rilevamento e il tracciamento di oggetti | Come effettuare il benchmark | YOLO11 RILASCIATO🚀

Esplora ed esegui YOLO11 direttamente sulla Ultralytics .

YOLO11 si basa sulla versatile gamma di modelli stabilita dalle precedenti versioni di Ultralytics YOLO, offrendo un supporto avanzato per varie attività di computer vision:

Questa tabella fornisce una panoramica delle varianti del modello YOLO11, mostrando la loro applicabilità in attività specifiche e la compatibilità con modalità operative come Inferenza, Validazione, Addestramento ed Esportazione. Questa flessibilità rende YOLO11 adatto a un'ampia gamma di applicazioni nella visione artificiale, dal rilevamento in tempo reale a complesse attività di segmentazione.

Vedere la Documentazione sulla Detection per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Segmentazione per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Classificazione per esempi di utilizzo con questi modelli addestrati su ImageNet, che includono 1000 classi pre-addestrate.

Vedere la Documentazione sulla Stima della Posa per esempi di utilizzo con questi modelli addestrati su COCO, che includono 1 classe pre-addestrata, 'persona'.

Vedere la Documentazione sulla Detection Orientata per esempi di utilizzo con questi modelli addestrati su DOTAv1, che includono 15 classi pre-addestrate.

Questa sezione fornisce semplici esempi di addestramento e inferenza YOLO11. Per la documentazione completa su queste e altre modalità, consulta le pagine della documentazione Predict, Train, Val ed Export.

Si noti che l'esempio seguente è per i modelli YOLO11 Detect per il rilevamento di oggetti. Per ulteriori attività supportate, consultare i documenti Segment, Classify, OBB e Pose.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in Python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

Pubblicazione Ultralytics YOLO11

Ultralytics non ha pubblicato un documento di ricerca formale per YOLO11 a causa della rapida evoluzione dei modelli. Ci concentriamo sul progresso della tecnologia e sul renderla più facile da usare, piuttosto che sulla produzione di documentazione statica. Per le informazioni più aggiornate sull'architettura, le caratteristiche e l'utilizzo di YOLO, fare riferimento al nostro repository GitHub e alla documentazione.

Se utilizzi YOLO11 o qualsiasi altro software da questo repository nel tuo lavoro, citalo utilizzando il seguente formato:

Si prega di notare che il DOI è in sospeso e verrà aggiunto alla citazione non appena sarà disponibile. I modelli YOLO11 sono forniti con licenze AGPL-3.0 ed Enterprise.

Ultralytics YOLO11 introduce diversi significativi progressi rispetto a YOLOv8. I miglioramenti chiave includono:

L'addestramento di un modello YOLO11 per l'object detection può essere eseguito utilizzando comandi Python o CLI. Di seguito sono riportati esempi per entrambi i metodi:

Per istruzioni più dettagliate, fare riferimento alla documentazione Addestramento.

I modelli YOLO11 sono versatili e supportano un'ampia gamma di attività di computer vision, tra cui:

Per maggiori informazioni su ciascuna attività, consulta la documentazione relativa a Rilevamento, Segmentazione delle istanze, Classificazione, Stima della posa e Rilevamento orientato.

YOLO11 raggiunge una maggiore accuratezza con meno parametri grazie ai progressi nella progettazione del modello e nelle tecniche di ottimizzazione. L'architettura migliorata consente un'estrazione e un'elaborazione efficienti delle feature, ottenendo una media di precisione media (mAP) più elevata su dataset come COCO, utilizzando il 22% in meno di parametri rispetto a YOLOv8m. Ciò rende YOLO11 efficiente dal punto di vista computazionale senza compromettere l'accuratezza, rendendolo adatto per l'implementazione su dispositivi con risorse limitate.

Sì, YOLO11 è progettato per l'adattabilità in vari ambienti, inclusi i dispositivi edge. La sua architettura ottimizzata e le efficienti capacità di elaborazione lo rendono adatto per la distribuzione su dispositivi edge, piattaforme cloud e sistemi che supportano GPU NVIDIA. Questa flessibilità garantisce che YOLO11 possa essere utilizzato in diverse applicazioni, dal rilevamento in tempo reale su dispositivi mobili a complesse attività di segmentazione in ambienti cloud. Per maggiori dettagli sulle opzioni di implementazione, fare riferimento alla documentazione di Esportazione.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO11n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO11n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo11n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO11n model and run inference on the 'bus.jpg' image
yolo predict model=yolo11n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolo11_ultralytics,
  author = {Glenn Jocher and Jing Qiu},
  title = {Ultralytics YOLO11},
  version = {11.0.0},
  year = {2024},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO11n model
model = YOLO("yolo11n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/it/models/yolo26/

**Contents:**
- Ultralytics YOLO26
- Panoramica
- Caratteristiche principali
- Attività e modalità supportate
- Metriche di performance
- Esempi di utilizzo
- YOLOE-26: Segmentazione di Istanza a Vocabolario Aperto
  - Esempio di utilizzo
- Citazioni e ringraziamenti
- FAQ

Ultralytics YOLO26 è l'ultima evoluzione della serie YOLO di rilevatori di oggetti in tempo reale, progettata da zero per dispositivi edge e a bassa potenza. Introduce un design semplificato che elimina la complessità non necessaria integrando al contempo innovazioni mirate per offrire una distribuzione più rapida, leggera e accessibile.

Esplora ed esegui i modelli YOLO26 direttamente sulla Ultralytics .

L'architettura di YOLO26 è guidata da tre principi fondamentali:

Insieme, queste innovazioni offrono una famiglia di modelli che raggiunge una maggiore accuratezza su piccoli oggetti, fornisce un'implementazione senza interruzioni e funziona fino al 43% più velocemente sulle CPU — rendendo YOLO26 uno dei modelli YOLO più pratici e implementabili fino ad oggi per ambienti con risorse limitate.

Rimozione di DFL Il modulo Distribution Focal Loss (DFL), sebbene efficace, spesso complicava l'esportazione e limitava la compatibilità hardware. YOLO26 rimuove completamente DFL, semplificando l'inferenza e ampliando il supporto per dispositivi edge e a bassa potenza.

Inferenza End-to-End NMS-Free A differenza dei rivelatori tradizionali che si affidano a NMS come fase di post-elaborazione separata, YOLO26 è nativamente end-to-end. Le previsioni vengono generate direttamente, riducendo la latenza e rendendo l'integrazione nei sistemi di produzione più veloce, leggera e affidabile.

ProgLoss + STAL Funzioni di perdita migliorate aumentano l'accuratezza del detection, con notevoli miglioramenti nel riconoscimento di oggetti piccoli, un requisito fondamentale per IoT, robotica, immagini aeree e altre applicazioni edge.

Ottimizzatore MuSGD Un nuovo ottimizzatore ibrido che combina SGD con Muon. Ispirato a Kimi K2 di Moonshot AI, MuSGD introduce metodi di ottimizzazione avanzati dall'addestramento LLM nella computer vision, consentendo un addestramento più stabile e una convergenza più rapida.

Inferenza CPU fino al 43% più veloce Specificamente ottimizzato per l'edge computing, YOLO26 offre un'inferenza CPU significativamente più veloce, garantendo prestazioni in tempo reale su dispositivi senza GPU.

Miglioramenti nella Segmentazione di Istanza Introduce la loss di segmentazione semantica per migliorare la convergenza del modello e un modulo proto aggiornato che sfrutta le informazioni multiscala per una qualità superiore delle maschere.

Stima Precisa della Posa Integra la Stima della Log-Verosimiglianza Residua (RLE) per una localizzazione più accurata dei keypoint e ottimizza il processo di decodifica per una maggiore velocità di inferenza.

Decodifica OBB Raffinata Introduce una loss angolare specializzata per migliorare la precisione di detect per oggetti di forma quadrata e ottimizza la decodifica OBB per risolvere i problemi di discontinuità dei bordi.

YOLO26 si basa sulla versatile gamma di modelli stabilita dalle precedenti release di Ultralytics YOLO, offrendo un supporto migliorato per diverse attività di visione artificiale:

Questo framework unificato garantisce che YOLO26 sia applicabile al rilevamento in tempo reale, alla segmentazione, alla classificazione, alla stima della posa e al rilevamento di oggetti orientati — il tutto con supporto per addestramento, convalida, inferenza ed esportazione.

Vedere la Documentazione sulla Detection per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Segmentazione per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Classificazione per esempi di utilizzo con questi modelli addestrati su ImageNet, che includono 1000 classi pre-addestrate.

Vedere la Documentazione sulla Stima della Posa per esempi di utilizzo con questi modelli addestrati su COCO, che includono 1 classe pre-addestrata, 'persona'.

Vedere la Documentazione sulla Detection Orientata per esempi di utilizzo con questi modelli addestrati su DOTAv1, che includono 15 classi pre-addestrate.

Questa sezione fornisce semplici esempi di training e inferenza YOLO26. Per la documentazione completa su queste e altre modalità, consultare le pagine della documentazione Predict, Train, Val ed Export.

Si noti che l'esempio seguente è per i modelli YOLO26 Detect per il rilevamento di oggetti. Per ulteriori attività supportate, consultare la documentazione Segment, Classify, OBB e Pose.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in Python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

YOLOE-26 integra l'architettura ad alte prestazioni YOLO26 con le capacità di vocabolario aperto della serie YOLOE. Consente il rilevamento e la segmentazione in tempo reale di qualsiasi classe di oggetti utilizzando prompt testuali, prompt visivi o una modalità senza prompt per l'inferenza zero-shot, rimuovendo efficacemente i vincoli del training a categoria fissa.

Sfruttando il design NMS-free e end-to-end di YOLO26, YOLOE-26 offre un'inferenza open-world rapida. Ciò lo rende una soluzione potente per applicazioni edge in ambienti dinamici, dove gli oggetti di interesse rappresentano un vocabolario ampio e in evoluzione.

Vedere la documentazione YOLOE per esempi di utilizzo con questi modelli addestrati sui dataset Objects365v1, GQA e Flickr30k.

Vedere la documentazione YOLOE per esempi di utilizzo con questi modelli addestrati sui dataset Objects365v1, GQA e Flickr30k.

YOLOE-26 supporta il prompting sia testuale che visivo. L'utilizzo dei prompt è semplice: basta passarli attraverso il predict method come mostrato di seguito:

I prompt testuali consentono di specificare le classi che si desidera detectare tramite descrizioni testuali. Il seguente codice mostra come utilizzare YOLOE-26 per detectare persone e autobus in un'immagine:

I prompt visivi ti consentono di guidare il modello mostrandogli esempi visivi delle classi target, anziché descriverle nel testo.

YOLOE-26 include varianti senza prompt che dispongono di un vocabolario integrato. Questi modelli non richiedono alcun prompt e funzionano come i modelli YOLO tradizionali. Invece di affidarsi a etichette fornite dall'utente o esempi visivi, detectano oggetti da un elenco predefinito di 4.585 classi basato sul set di tag utilizzato dal Recognize Anything Model Plus (RAM++).

Per un'analisi approfondita delle tecniche di prompting, dell'addestramento da zero e degli esempi di utilizzo completi, visita la documentazione di YOLOE.

Pubblicazione Ultralytics YOLO26

Ultralytics non ha pubblicato un articolo di ricerca formale per YOLO26 a causa della rapida evoluzione dei modelli. Ci concentriamo invece sulla fornitura di modelli all'avanguardia e sulla loro facilità d'uso. Per gli ultimi aggiornamenti sulle funzionalità, le architetture e l'utilizzo di YOLO, visita il nostro repository GitHub e la documentazione.

Se utilizzi YOLO26 o altro software Ultralytics nel tuo lavoro, cita il progetto come:

DOI in sospeso. YOLO26 è disponibile con licenze AGPL-3.0 ed Enterprise.

YOLO26 è una famiglia di modelli unificata, che fornisce supporto end-to-end per molteplici attività di visione artificiale:

Ogni variante di dimensione (n, s, m, l, x) supporta tutte le attività, oltre alle versioni a vocabolario aperto tramite YOLOE-26.

YOLO26 offre prestazioni edge all'avanguardia con:

I modelli YOLO26 sono stati rilasciati il 14 gennaio 2026 e sono disponibili per il download. Installa o aggiorna il ultralytics pacchetto e carica un modello:

Consulta la sezione Esempi di utilizzo per le istruzioni di addestramento, validazione ed esportazione.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (sql):
```sql
from ultralytics import YOLO

# Initialize model
model = YOLO("yoloe-26l-seg.pt")  # or select yoloe-26s/m-seg.pt for different sizes

# Set text prompt to detect person and bus. You only need to do this once after you load the model.
names = ["person", "bus"]
model.set_classes(names, model.get_text_pe(names))

# Run detection on the given image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (python):
```python
import numpy as np

from ultralytics import YOLO
from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# Initialize model
model = YOLO("yoloe-26l-seg.pt")

# Define visual prompts using bounding boxes and their corresponding class IDs.
# Each box highlights an example of the object you want the model to detect.
visual_prompts = dict(
    bboxes=np.array(
        [
            [221.52, 405.8, 344.98, 857.54],  # Box enclosing person
            [120, 425, 160, 445],  # Box enclosing glasses
        ],
    ),
    cls=np.array(
        [
            0,  # ID to be assigned for person
            1,  # ID to be assigned for glasses
        ]
    ),
)

# Run inference on an image, using the provided visual prompts as guidance
results = model.predict(
    "ultralytics/assets/bus.jpg",
    visual_prompts=visual_prompts,
    predictor=YOLOEVPSegPredictor,
)

# Show results
results[0].show()
```

---

## Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/ar/models/yolo26

**Contents:**
- Ultralytics YOLO26
- نظرة عامة
- الميزات الرئيسية
- المهام والأوضاع المدعومة
- مقاييس الأداء
- أمثلة الاستخدام
- YOLOE-26: تجزئة الكائنات ذات المفردات المفتوحة
  - مثال على الاستخدام
- الاقتباسات والإقرارات
- الأسئلة الشائعة

Ultralytics YOLO26 هو أحدث تطور في سلسلة YOLO لكاشفات الأجسام في الوقت الفعلي، وقد تم تصميمه من الألف إلى الياء من أجل الأجهزة الطرفية والأجهزة منخفضة الطاقة. يقدم تصميمًا مبسطًا يزيل التعقيد غير الضروري مع دمج الابتكارات المستهدفة لتقديم نشر أسرع وأخف وزنًا وأكثر سهولة.

استكشف ونفذ نماذج YOLO26 مباشرة على Ultralytics .

تسترشد بنية YOLO26 بثلاثة مبادئ أساسية:

تجتمع هذه الابتكارات لتقديم عائلة نماذج تحقق دقة أعلى على الكائنات الصغيرة، وتوفر نشرًا سلسًا، وتعمل بسرعة أكبر بنسبة تصل إلى 43٪ على وحدات المعالجة المركزية (CPUs) - مما يجعل YOLO26 أحد نماذج YOLO الأكثر عملية وقابلية للنشر حتى الآن للبيئات ذات الموارد المحدودة.

إزالة DFL في حين أن وحدة Distribution Focal Loss (DFL) فعالة، إلا أنها غالبًا ما تعقد عملية التصدير وتحد من توافق الأجهزة. يزيل YOLO26 وحدة DFL تمامًا، مما يبسط الاستدلال ويوسع الدعم لـ الأجهزة الطرفية ومنخفضة الطاقة.

الاستدلال الشامل الخالي من NMS على عكس الكاشفات التقليدية التي تعتمد على NMS كخطوة معالجة لاحقة منفصلة، فإن YOLO26 شامل أصليًا. يتم إنشاء التنبؤات مباشرةً، مما يقلل من زمن الوصول ويجعل التكامل في أنظمة الإنتاج أسرع وأخف وزنًا وأكثر موثوقية.

ProgLoss + STAL تحسين وظائف الخسارة يزيد من دقة الـ detect، مع تحسينات ملحوظة في التعرف على الأجسام الصغيرة، وهو مطلب حاسم لتطبيقات إنترنت الأشياء والروبوتات والتصوير الجوي وغيرها من التطبيقات الطرفية.

محسن MuSGD مُحسِّن هجين جديد يجمع بين SGD و Muon. مُستوحى من Kimi K2 من Moonshot AI، يُدخل MuSGD طرق تحسين متقدمة من تدريب LLM في رؤية الكمبيوتر، مما يُمكّن تدريبًا أكثر استقرارًا وتقاربًا أسرع.

استدلال أسرع لوحدة المعالجة المركزية CPU بنسبة تصل إلى 43٪ تم تحسين YOLO26 خصيصًا للحوسبة الطرفية، ويوفر استدلالًا أسرع لوحدة المعالجة المركزية CPU بشكل ملحوظ، مما يضمن أداءً في الوقت الفعلي على الأجهزة التي لا تحتوي على وحدات معالجة الرسوميات GPUs.

تحسينات تجزئة الكائنات يقدم فقدان التجزئة الدلالية لتحسين تقارب النموذج ووحدة بروتو مطورة تستفيد من المعلومات متعددة المقاييس لجودة قناع فائقة.

تقدير الوضعية الدقيق يدمج تقدير الاحتمالية اللوغاريتمية المتبقية (RLE) لتحديد مواقع النقاط الرئيسية بدقة أكبر ويحسن عملية فك التشفير لزيادة سرعة الاستدلال.

فك تشفير OBB المحسن يقدم خسارة زاوية متخصصة لتحسين دقة detect الكائنات مربعة الشكل ويحسن فك تشفير OBB لحل مشكلات عدم استمرارية الحدود.

يعتمد YOLO26 على مجموعة النماذج المتنوعة التي أرستها إصدارات Ultralytics YOLO السابقة، مقدمًا دعمًا معززًا عبر مهام رؤية الكمبيوتر المختلفة:

يضمن هذا الإطار الموحد أن يكون YOLO26 قابلاً للتطبيق عبر الكشف في الوقت الفعلي، و segmentation، و classification، و pose estimation، و oriented object detection — كل ذلك مع دعم التدريب والتحقق والاستدلال والتصدير.

راجع وثائق الكشف لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التجزئة لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التصنيف لأمثلة الاستخدام مع هذه النماذج المدربة على ImageNet، والتي تتضمن 1000 فئة مدربة مسبقًا.

راجع وثائق تقدير الوضعيات لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن فئة واحدة مدربة مسبقًا، وهي 'شخص'.

راجع وثائق الكشف الموجه لأمثلة الاستخدام مع هذه النماذج المدربة على DOTAv1، والتي تتضمن 15 فئة مدربة مسبقًا.

يقدم هذا القسم أمثلة بسيطة لتدريب YOLO26 والاستدلال. للاطلاع على الوثائق الكاملة حول هذه الأنماط وغيرها، راجع صفحات وثائق Predict وTrain وVal وExport.

لاحظ أن المثال أدناه هو لنماذج YOLO26 Detect لـ object detection. للمهام المدعومة الإضافية، راجع وثائق Segment وClassify وOBB وPose.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في Python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

يدمج YOLOE-26 بنية YOLO26 عالية الأداء مع قدرات المفردات المفتوحة لسلسلة YOLOE. إنه يتيح الكشف والتجزئة في الوقت الفعلي لأي فئة كائن باستخدام المطالبات النصية، أو المطالبات المرئية، أو وضع خالٍ من المطالبات للاستدلال بدون تدريب مسبق، مما يزيل بشكل فعال قيود التدريب على فئات ثابتة.

من خلال الاستفادة من تصميم YOLO26 الشامل والخالي من NMS، يقدم YOLOE-26 استدلالًا سريعًا للعالم المفتوح. وهذا يجعله حلاً قويًا لتطبيقات الحافة في البيئات الديناميكية حيث تمثل الكائنات محل الاهتمام مفردات واسعة ومتطورة.

راجع وثائق YOLOE لأمثلة الاستخدام مع هذه النماذج المدربة على مجموعات بيانات Objects365v1 وGQA وFlickr30k.

راجع وثائق YOLOE لأمثلة الاستخدام مع هذه النماذج المدربة على مجموعات بيانات Objects365v1 وGQA وFlickr30k.

يدعم YOLOE-26 كلًا من التوجيه النصي والمرئي. يُعد استخدام الموجهات أمرًا مباشرًا—فقط قم بتمريرها عبر predict الطريقة كما هو موضح أدناه:

تتيح لك الموجهات النصية تحديد الفئات التي ترغب في detectها من خلال الأوصاف النصية. يوضح الكود التالي كيف يمكنك استخدام YOLOE-26 لـ detect الأشخاص والحافلات في صورة:

تتيح لك المطالبات المرئية توجيه النموذج عن طريق عرض أمثلة مرئية للفئات المستهدفة، بدلاً من وصفها بالنص.

يتضمن YOLOE-26 إصدارات خالية من الموجهات تأتي مع مفردات مدمجة. لا تتطلب هذه النماذج أي موجهات وتعمل مثل نماذج YOLO التقليدية. بدلاً من الاعتماد على التسميات المقدمة من المستخدم أو الأمثلة المرئية، فإنها detect الكائنات من قائمة محددة مسبقًا تضم 4,585 فئة بناءً على مجموعة العلامات المستخدمة بواسطة Recognize Anything Model Plus (RAM++).

للاطلاع المتعمق على تقنيات التوجيه، والتدريب من الصفر، وأمثلة الاستخدام الكاملة، قم بزيارة وثائق YOLOE.

منشور Ultralytics YOLO26

لم تنشر Ultralytics ورقة بحثية رسمية لـ YOLO26 نظرًا للطبيعة سريعة التطور للنماذج. بدلاً من ذلك، نركز على تقديم نماذج متطورة وتسهيل استخدامها. للحصول على آخر التحديثات حول ميزات وهياكل واستخدام YOLO، تفضل بزيارة مستودع GitHub الخاص بنا و الوثائق.

إذا كنت تستخدم YOLO26 أو برامج Ultralytics أخرى في عملك، فيرجى الاستشهاد بها على النحو التالي:

DOI معلق. يتوفر YOLO26 بموجب تراخيص AGPL-3.0 و Enterprise.

YOLO26 هي عائلة نماذج موحدة، توفر دعمًا شاملاً لمهام رؤية الكمبيوتر المتعددة:

يدعم كل متغير حجم (n, s, m, l, x) جميع المهام، بالإضافة إلى إصدارات المفردات المفتوحة عبر YOLOE-26.

يوفر YOLO26 أداءً متطورًا على الحافة من خلال:

تم إصدار نماذج YOLO26 في 14 يناير 2026، وهي متاحة للتنزيل. قم بتثبيت أو تحديث ultralytics الحزمة وقم بتحميل نموذج:

راجع قسم أمثلة الاستخدام للحصول على تعليمات التدريب والتحقق والتصدير.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (sql):
```sql
from ultralytics import YOLO

# Initialize model
model = YOLO("yoloe-26l-seg.pt")  # or select yoloe-26s/m-seg.pt for different sizes

# Set text prompt to detect person and bus. You only need to do this once after you load the model.
names = ["person", "bus"]
model.set_classes(names, model.get_text_pe(names))

# Run detection on the given image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (python):
```python
import numpy as np

from ultralytics import YOLO
from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# Initialize model
model = YOLO("yoloe-26l-seg.pt")

# Define visual prompts using bounding boxes and their corresponding class IDs.
# Each box highlights an example of the object you want the model to detect.
visual_prompts = dict(
    bboxes=np.array(
        [
            [221.52, 405.8, 344.98, 857.54],  # Box enclosing person
            [120, 425, 160, 445],  # Box enclosing glasses
        ],
    ),
    cls=np.array(
        [
            0,  # ID to be assigned for person
            1,  # ID to be assigned for glasses
        ]
    ),
)

# Run inference on an image, using the provided visual prompts as guidance
results = model.predict(
    "ultralytics/assets/bus.jpg",
    visual_prompts=visual_prompts,
    predictor=YOLOEVPSegPredictor,
)

# Show results
results[0].show()
```

---

## Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/models/yolo26/

**Contents:**
- Ultralytics YOLO26
- Overview
- Key Features
- Supported Tasks and Modes
- Performance Metrics
- Usage Examples
- YOLOE-26: Open-Vocabulary Instance Segmentation
  - Usage Example
- Citations and Acknowledgments
- FAQ

Ultralytics YOLO26 is the latest evolution in the YOLO series of real-time object detectors, engineered from the ground up for edge and low-power devices. It introduces a streamlined design that removes unnecessary complexity while integrating targeted innovations to deliver faster, lighter, and more accessible deployment.

Try on Ultralytics Platform

Explore and run YOLO26 models directly on Ultralytics Platform.

The architecture of YOLO26 is guided by three core principles:

Together, these innovations deliver a model family that achieves higher accuracy on small objects, provides seamless deployment, and runs up to 43% faster on CPUs — making YOLO26 one of the most practical and deployable YOLO models to date for resource-constrained environments.

DFL Removal The Distribution Focal Loss (DFL) module, while effective, often complicated export and limited hardware compatibility. YOLO26 removes DFL entirely, simplifying inference and broadening support for edge and low-power devices.

End-to-End NMS-Free Inference Unlike traditional detectors that rely on NMS as a separate post-processing step, YOLO26 is natively end-to-end. Predictions are generated directly, reducing latency and making integration into production systems faster, lighter, and more reliable.

ProgLoss + STAL Improved loss functions increase detection accuracy, with notable improvements in small-object recognition, a critical requirement for IoT, robotics, aerial imagery, and other edge applications.

MuSGD Optimizer A new hybrid optimizer that combines SGD with Muon. Inspired by Moonshot AI's Kimi K2, MuSGD introduces advanced optimization methods from LLM training into computer vision, enabling more stable training and faster convergence.

Up to 43% Faster CPU Inference Specifically optimized for edge computing, YOLO26 delivers significantly faster CPU inference, ensuring real-time performance on devices without GPUs.

Instance Segmentation Enhancements Introduces semantic segmentation loss to improve model convergence and an upgraded proto module that leverages multi-scale information for superior mask quality.

Precision Pose Estimation Integrates Residual Log-Likelihood Estimation (RLE) for more accurate keypoint localization and optimizes the decoding process for increased inference speed.

Refined OBB Decoding Introduces a specialized angle loss to improve detection accuracy for square-shaped objects and optimizes OBB decoding to resolve boundary discontinuity issues.

YOLO26 builds upon the versatile model range established by earlier Ultralytics YOLO releases, offering enhanced support across various computer vision tasks:

This unified framework ensures YOLO26 is applicable across real-time detection, segmentation, classification, pose estimation, and oriented object detection — all with training, validation, inference, and export support.

See Detection Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Segmentation Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Classification Docs for usage examples with these models trained on ImageNet, which include 1000 pretrained classes.

See Pose Estimation Docs for usage examples with these models trained on COCO, which include 1 pretrained class, 'person'.

See Oriented Detection Docs for usage examples with these models trained on DOTAv1, which include 15 pretrained classes.

This section provides simple YOLO26 training and inference examples. For full documentation on these and other modes, see the Predict, Train, Val, and Export docs pages.

Note that the example below is for YOLO26 Detect models for object detection. For additional supported tasks, see the Segment, Classify, OBB, and Pose docs.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in Python:

CLI commands are available to directly run the models:

YOLOE-26 integrates the high-performance YOLO26 architecture with the open-vocabulary capabilities of the YOLOE series. It enables real-time detection and segmentation of any object class using text prompts, visual prompts, or a prompt-free mode for zero-shot inference, effectively removing the constraints of fixed-category training.

By leveraging YOLO26's NMS-free, end-to-end design, YOLOE-26 delivers fast open-world inference. This makes it a powerful solution for edge applications in dynamic environments where the objects of interest represent a broad and evolving vocabulary.

See YOLOE Docs for usage examples with these models trained on Objects365v1, GQA and Flickr30k datasets.

See YOLOE Docs for usage examples with these models trained on Objects365v1, GQA and Flickr30k datasets.

YOLOE-26 supports both text-based and visual prompting. Using prompts is straightforward—just pass them through the predict method as shown below:

Text prompts allow you to specify the classes that you wish to detect through textual descriptions. The following code shows how you can use YOLOE-26 to detect people and buses in an image:

Visual prompts allow you to guide the model by showing it visual examples of the target classes, rather than describing them in text.

YOLOE-26 includes prompt-free variants that come with a built-in vocabulary. These models don't require any prompts and work like traditional YOLO models. Instead of relying on user-provided labels or visual examples, they detect objects from a predefined list of 4,585 classes based on the tag set used by the Recognize Anything Model Plus (RAM++).

For a deep dive into prompting techniques, training from scratch, and full usage examples, visit the YOLOE Documentation.

Ultralytics YOLO26 Publication

Ultralytics has not published a formal research paper for YOLO26 due to the rapidly evolving nature of the models. Instead, we focus on delivering cutting-edge models and making them easy to use. For the latest updates on YOLO features, architectures, and usage, visit our GitHub repository and documentation.

If you use YOLO26 or other Ultralytics software in your work, please cite it as:

DOI pending. YOLO26 is available under AGPL-3.0 and Enterprise licenses.

YOLO26 is a unified model family, providing end-to-end support for multiple computer vision tasks:

Each size variant (n, s, m, l, x) supports all tasks, plus open-vocabulary versions via YOLOE-26.

YOLO26 delivers state-of-the-art edge performance with:

YOLO26 models were released on January 14, 2026, and are available for download. Install or update the ultralytics package and load a model:

See the Usage Examples section for training, validation, and export instructions.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (sql):
```sql
from ultralytics import YOLO

# Initialize model
model = YOLO("yoloe-26l-seg.pt")  # or select yoloe-26s/m-seg.pt for different sizes

# Set text prompt to detect person and bus. You only need to do this once after you load the model.
names = ["person", "bus"]
model.set_classes(names, model.get_text_pe(names))

# Run detection on the given image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (python):
```python
import numpy as np

from ultralytics import YOLO
from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# Initialize model
model = YOLO("yoloe-26l-seg.pt")

# Define visual prompts using bounding boxes and their corresponding class IDs.
# Each box highlights an example of the object you want the model to detect.
visual_prompts = dict(
    bboxes=np.array(
        [
            [221.52, 405.8, 344.98, 857.54],  # Box enclosing person
            [120, 425, 160, 445],  # Box enclosing glasses
        ],
    ),
    cls=np.array(
        [
            0,  # ID to be assigned for person
            1,  # ID to be assigned for glasses
        ]
    ),
)

# Run inference on an image, using the provided visual prompts as guidance
results = model.predict(
    "ultralytics/assets/bus.jpg",
    visual_prompts=visual_prompts,
    predictor=YOLOEVPSegPredictor,
)

# Show results
results[0].show()
```

---

## Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/ar/models/yolo26/

**Contents:**
- Ultralytics YOLO26
- نظرة عامة
- الميزات الرئيسية
- المهام والأوضاع المدعومة
- مقاييس الأداء
- أمثلة الاستخدام
- YOLOE-26: تجزئة الكائنات ذات المفردات المفتوحة
  - مثال على الاستخدام
- الاقتباسات والإقرارات
- الأسئلة الشائعة

Ultralytics YOLO26 هو أحدث تطور في سلسلة YOLO لكاشفات الأجسام في الوقت الفعلي، وقد تم تصميمه من الألف إلى الياء من أجل الأجهزة الطرفية والأجهزة منخفضة الطاقة. يقدم تصميمًا مبسطًا يزيل التعقيد غير الضروري مع دمج الابتكارات المستهدفة لتقديم نشر أسرع وأخف وزنًا وأكثر سهولة.

استكشف ونفذ نماذج YOLO26 مباشرة على Ultralytics .

تسترشد بنية YOLO26 بثلاثة مبادئ أساسية:

تجتمع هذه الابتكارات لتقديم عائلة نماذج تحقق دقة أعلى على الكائنات الصغيرة، وتوفر نشرًا سلسًا، وتعمل بسرعة أكبر بنسبة تصل إلى 43٪ على وحدات المعالجة المركزية (CPUs) - مما يجعل YOLO26 أحد نماذج YOLO الأكثر عملية وقابلية للنشر حتى الآن للبيئات ذات الموارد المحدودة.

إزالة DFL في حين أن وحدة Distribution Focal Loss (DFL) فعالة، إلا أنها غالبًا ما تعقد عملية التصدير وتحد من توافق الأجهزة. يزيل YOLO26 وحدة DFL تمامًا، مما يبسط الاستدلال ويوسع الدعم لـ الأجهزة الطرفية ومنخفضة الطاقة.

الاستدلال الشامل الخالي من NMS على عكس الكاشفات التقليدية التي تعتمد على NMS كخطوة معالجة لاحقة منفصلة، فإن YOLO26 شامل أصليًا. يتم إنشاء التنبؤات مباشرةً، مما يقلل من زمن الوصول ويجعل التكامل في أنظمة الإنتاج أسرع وأخف وزنًا وأكثر موثوقية.

ProgLoss + STAL تحسين وظائف الخسارة يزيد من دقة الـ detect، مع تحسينات ملحوظة في التعرف على الأجسام الصغيرة، وهو مطلب حاسم لتطبيقات إنترنت الأشياء والروبوتات والتصوير الجوي وغيرها من التطبيقات الطرفية.

محسن MuSGD مُحسِّن هجين جديد يجمع بين SGD و Muon. مُستوحى من Kimi K2 من Moonshot AI، يُدخل MuSGD طرق تحسين متقدمة من تدريب LLM في رؤية الكمبيوتر، مما يُمكّن تدريبًا أكثر استقرارًا وتقاربًا أسرع.

استدلال أسرع لوحدة المعالجة المركزية CPU بنسبة تصل إلى 43٪ تم تحسين YOLO26 خصيصًا للحوسبة الطرفية، ويوفر استدلالًا أسرع لوحدة المعالجة المركزية CPU بشكل ملحوظ، مما يضمن أداءً في الوقت الفعلي على الأجهزة التي لا تحتوي على وحدات معالجة الرسوميات GPUs.

تحسينات تجزئة الكائنات يقدم فقدان التجزئة الدلالية لتحسين تقارب النموذج ووحدة بروتو مطورة تستفيد من المعلومات متعددة المقاييس لجودة قناع فائقة.

تقدير الوضعية الدقيق يدمج تقدير الاحتمالية اللوغاريتمية المتبقية (RLE) لتحديد مواقع النقاط الرئيسية بدقة أكبر ويحسن عملية فك التشفير لزيادة سرعة الاستدلال.

فك تشفير OBB المحسن يقدم خسارة زاوية متخصصة لتحسين دقة detect الكائنات مربعة الشكل ويحسن فك تشفير OBB لحل مشكلات عدم استمرارية الحدود.

يعتمد YOLO26 على مجموعة النماذج المتنوعة التي أرستها إصدارات Ultralytics YOLO السابقة، مقدمًا دعمًا معززًا عبر مهام رؤية الكمبيوتر المختلفة:

يضمن هذا الإطار الموحد أن يكون YOLO26 قابلاً للتطبيق عبر الكشف في الوقت الفعلي، و segmentation، و classification، و pose estimation، و oriented object detection — كل ذلك مع دعم التدريب والتحقق والاستدلال والتصدير.

راجع وثائق الكشف لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التجزئة لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التصنيف لأمثلة الاستخدام مع هذه النماذج المدربة على ImageNet، والتي تتضمن 1000 فئة مدربة مسبقًا.

راجع وثائق تقدير الوضعيات لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن فئة واحدة مدربة مسبقًا، وهي 'شخص'.

راجع وثائق الكشف الموجه لأمثلة الاستخدام مع هذه النماذج المدربة على DOTAv1، والتي تتضمن 15 فئة مدربة مسبقًا.

يقدم هذا القسم أمثلة بسيطة لتدريب YOLO26 والاستدلال. للاطلاع على الوثائق الكاملة حول هذه الأنماط وغيرها، راجع صفحات وثائق Predict وTrain وVal وExport.

لاحظ أن المثال أدناه هو لنماذج YOLO26 Detect لـ object detection. للمهام المدعومة الإضافية، راجع وثائق Segment وClassify وOBB وPose.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في Python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

يدمج YOLOE-26 بنية YOLO26 عالية الأداء مع قدرات المفردات المفتوحة لسلسلة YOLOE. إنه يتيح الكشف والتجزئة في الوقت الفعلي لأي فئة كائن باستخدام المطالبات النصية، أو المطالبات المرئية، أو وضع خالٍ من المطالبات للاستدلال بدون تدريب مسبق، مما يزيل بشكل فعال قيود التدريب على فئات ثابتة.

من خلال الاستفادة من تصميم YOLO26 الشامل والخالي من NMS، يقدم YOLOE-26 استدلالًا سريعًا للعالم المفتوح. وهذا يجعله حلاً قويًا لتطبيقات الحافة في البيئات الديناميكية حيث تمثل الكائنات محل الاهتمام مفردات واسعة ومتطورة.

راجع وثائق YOLOE لأمثلة الاستخدام مع هذه النماذج المدربة على مجموعات بيانات Objects365v1 وGQA وFlickr30k.

راجع وثائق YOLOE لأمثلة الاستخدام مع هذه النماذج المدربة على مجموعات بيانات Objects365v1 وGQA وFlickr30k.

يدعم YOLOE-26 كلًا من التوجيه النصي والمرئي. يُعد استخدام الموجهات أمرًا مباشرًا—فقط قم بتمريرها عبر predict الطريقة كما هو موضح أدناه:

تتيح لك الموجهات النصية تحديد الفئات التي ترغب في detectها من خلال الأوصاف النصية. يوضح الكود التالي كيف يمكنك استخدام YOLOE-26 لـ detect الأشخاص والحافلات في صورة:

تتيح لك المطالبات المرئية توجيه النموذج عن طريق عرض أمثلة مرئية للفئات المستهدفة، بدلاً من وصفها بالنص.

يتضمن YOLOE-26 إصدارات خالية من الموجهات تأتي مع مفردات مدمجة. لا تتطلب هذه النماذج أي موجهات وتعمل مثل نماذج YOLO التقليدية. بدلاً من الاعتماد على التسميات المقدمة من المستخدم أو الأمثلة المرئية، فإنها detect الكائنات من قائمة محددة مسبقًا تضم 4,585 فئة بناءً على مجموعة العلامات المستخدمة بواسطة Recognize Anything Model Plus (RAM++).

للاطلاع المتعمق على تقنيات التوجيه، والتدريب من الصفر، وأمثلة الاستخدام الكاملة، قم بزيارة وثائق YOLOE.

منشور Ultralytics YOLO26

لم تنشر Ultralytics ورقة بحثية رسمية لـ YOLO26 نظرًا للطبيعة سريعة التطور للنماذج. بدلاً من ذلك، نركز على تقديم نماذج متطورة وتسهيل استخدامها. للحصول على آخر التحديثات حول ميزات وهياكل واستخدام YOLO، تفضل بزيارة مستودع GitHub الخاص بنا و الوثائق.

إذا كنت تستخدم YOLO26 أو برامج Ultralytics أخرى في عملك، فيرجى الاستشهاد بها على النحو التالي:

DOI معلق. يتوفر YOLO26 بموجب تراخيص AGPL-3.0 و Enterprise.

YOLO26 هي عائلة نماذج موحدة، توفر دعمًا شاملاً لمهام رؤية الكمبيوتر المتعددة:

يدعم كل متغير حجم (n, s, m, l, x) جميع المهام، بالإضافة إلى إصدارات المفردات المفتوحة عبر YOLOE-26.

يوفر YOLO26 أداءً متطورًا على الحافة من خلال:

تم إصدار نماذج YOLO26 في 14 يناير 2026، وهي متاحة للتنزيل. قم بتثبيت أو تحديث ultralytics الحزمة وقم بتحميل نموذج:

راجع قسم أمثلة الاستخدام للحصول على تعليمات التدريب والتحقق والتصدير.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (sql):
```sql
from ultralytics import YOLO

# Initialize model
model = YOLO("yoloe-26l-seg.pt")  # or select yoloe-26s/m-seg.pt for different sizes

# Set text prompt to detect person and bus. You only need to do this once after you load the model.
names = ["person", "bus"]
model.set_classes(names, model.get_text_pe(names))

# Run detection on the given image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (python):
```python
import numpy as np

from ultralytics import YOLO
from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# Initialize model
model = YOLO("yoloe-26l-seg.pt")

# Define visual prompts using bounding boxes and their corresponding class IDs.
# Each box highlights an example of the object you want the model to detect.
visual_prompts = dict(
    bboxes=np.array(
        [
            [221.52, 405.8, 344.98, 857.54],  # Box enclosing person
            [120, 425, 160, 445],  # Box enclosing glasses
        ],
    ),
    cls=np.array(
        [
            0,  # ID to be assigned for person
            1,  # ID to be assigned for glasses
        ]
    ),
)

# Run inference on an image, using the provided visual prompts as guidance
results = model.predict(
    "ultralytics/assets/bus.jpg",
    visual_prompts=visual_prompts,
    predictor=YOLOEVPSegPredictor,
)

# Show results
results[0].show()
```

---

## Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/models/yolo26

**Contents:**
- Ultralytics YOLO26
- Overview
- Key Features
- Supported Tasks and Modes
- Performance Metrics
- Usage Examples
- YOLOE-26: Open-Vocabulary Instance Segmentation
  - Usage Example
- Citations and Acknowledgments
- FAQ

Ultralytics YOLO26 is the latest evolution in the YOLO series of real-time object detectors, engineered from the ground up for edge and low-power devices. It introduces a streamlined design that removes unnecessary complexity while integrating targeted innovations to deliver faster, lighter, and more accessible deployment.

Try on Ultralytics Platform

Explore and run YOLO26 models directly on Ultralytics Platform.

The architecture of YOLO26 is guided by three core principles:

Together, these innovations deliver a model family that achieves higher accuracy on small objects, provides seamless deployment, and runs up to 43% faster on CPUs — making YOLO26 one of the most practical and deployable YOLO models to date for resource-constrained environments.

DFL Removal The Distribution Focal Loss (DFL) module, while effective, often complicated export and limited hardware compatibility. YOLO26 removes DFL entirely, simplifying inference and broadening support for edge and low-power devices.

End-to-End NMS-Free Inference Unlike traditional detectors that rely on NMS as a separate post-processing step, YOLO26 is natively end-to-end. Predictions are generated directly, reducing latency and making integration into production systems faster, lighter, and more reliable.

ProgLoss + STAL Improved loss functions increase detection accuracy, with notable improvements in small-object recognition, a critical requirement for IoT, robotics, aerial imagery, and other edge applications.

MuSGD Optimizer A new hybrid optimizer that combines SGD with Muon. Inspired by Moonshot AI's Kimi K2, MuSGD introduces advanced optimization methods from LLM training into computer vision, enabling more stable training and faster convergence.

Up to 43% Faster CPU Inference Specifically optimized for edge computing, YOLO26 delivers significantly faster CPU inference, ensuring real-time performance on devices without GPUs.

Instance Segmentation Enhancements Introduces semantic segmentation loss to improve model convergence and an upgraded proto module that leverages multi-scale information for superior mask quality.

Precision Pose Estimation Integrates Residual Log-Likelihood Estimation (RLE) for more accurate keypoint localization and optimizes the decoding process for increased inference speed.

Refined OBB Decoding Introduces a specialized angle loss to improve detection accuracy for square-shaped objects and optimizes OBB decoding to resolve boundary discontinuity issues.

YOLO26 builds upon the versatile model range established by earlier Ultralytics YOLO releases, offering enhanced support across various computer vision tasks:

This unified framework ensures YOLO26 is applicable across real-time detection, segmentation, classification, pose estimation, and oriented object detection — all with training, validation, inference, and export support.

See Detection Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Segmentation Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

See Classification Docs for usage examples with these models trained on ImageNet, which include 1000 pretrained classes.

See Pose Estimation Docs for usage examples with these models trained on COCO, which include 1 pretrained class, 'person'.

See Oriented Detection Docs for usage examples with these models trained on DOTAv1, which include 15 pretrained classes.

This section provides simple YOLO26 training and inference examples. For full documentation on these and other modes, see the Predict, Train, Val, and Export docs pages.

Note that the example below is for YOLO26 Detect models for object detection. For additional supported tasks, see the Segment, Classify, OBB, and Pose docs.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in Python:

CLI commands are available to directly run the models:

YOLOE-26 integrates the high-performance YOLO26 architecture with the open-vocabulary capabilities of the YOLOE series. It enables real-time detection and segmentation of any object class using text prompts, visual prompts, or a prompt-free mode for zero-shot inference, effectively removing the constraints of fixed-category training.

By leveraging YOLO26's NMS-free, end-to-end design, YOLOE-26 delivers fast open-world inference. This makes it a powerful solution for edge applications in dynamic environments where the objects of interest represent a broad and evolving vocabulary.

See YOLOE Docs for usage examples with these models trained on Objects365v1, GQA and Flickr30k datasets.

See YOLOE Docs for usage examples with these models trained on Objects365v1, GQA and Flickr30k datasets.

YOLOE-26 supports both text-based and visual prompting. Using prompts is straightforward—just pass them through the predict method as shown below:

Text prompts allow you to specify the classes that you wish to detect through textual descriptions. The following code shows how you can use YOLOE-26 to detect people and buses in an image:

Visual prompts allow you to guide the model by showing it visual examples of the target classes, rather than describing them in text.

YOLOE-26 includes prompt-free variants that come with a built-in vocabulary. These models don't require any prompts and work like traditional YOLO models. Instead of relying on user-provided labels or visual examples, they detect objects from a predefined list of 4,585 classes based on the tag set used by the Recognize Anything Model Plus (RAM++).

For a deep dive into prompting techniques, training from scratch, and full usage examples, visit the YOLOE Documentation.

Ultralytics YOLO26 Publication

Ultralytics has not published a formal research paper for YOLO26 due to the rapidly evolving nature of the models. Instead, we focus on delivering cutting-edge models and making them easy to use. For the latest updates on YOLO features, architectures, and usage, visit our GitHub repository and documentation.

If you use YOLO26 or other Ultralytics software in your work, please cite it as:

DOI pending. YOLO26 is available under AGPL-3.0 and Enterprise licenses.

YOLO26 is a unified model family, providing end-to-end support for multiple computer vision tasks:

Each size variant (n, s, m, l, x) supports all tasks, plus open-vocabulary versions via YOLOE-26.

YOLO26 delivers state-of-the-art edge performance with:

YOLO26 models were released on January 14, 2026, and are available for download. Install or update the ultralytics package and load a model:

See the Usage Examples section for training, validation, and export instructions.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (sql):
```sql
from ultralytics import YOLO

# Initialize model
model = YOLO("yoloe-26l-seg.pt")  # or select yoloe-26s/m-seg.pt for different sizes

# Set text prompt to detect person and bus. You only need to do this once after you load the model.
names = ["person", "bus"]
model.set_classes(names, model.get_text_pe(names))

# Run detection on the given image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (python):
```python
import numpy as np

from ultralytics import YOLO
from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# Initialize model
model = YOLO("yoloe-26l-seg.pt")

# Define visual prompts using bounding boxes and their corresponding class IDs.
# Each box highlights an example of the object you want the model to detect.
visual_prompts = dict(
    bboxes=np.array(
        [
            [221.52, 405.8, 344.98, 857.54],  # Box enclosing person
            [120, 425, 160, 445],  # Box enclosing glasses
        ],
    ),
    cls=np.array(
        [
            0,  # ID to be assigned for person
            1,  # ID to be assigned for glasses
        ]
    ),
)

# Run inference on an image, using the provided visual prompts as guidance
results = model.predict(
    "ultralytics/assets/bus.jpg",
    visual_prompts=visual_prompts,
    predictor=YOLOEVPSegPredictor,
)

# Show results
results[0].show()
```

---

## Ultralytics YOLO26

**URL:** https://docs.ultralytics.com/it/models/yolo26

**Contents:**
- Ultralytics YOLO26
- Panoramica
- Caratteristiche principali
- Attività e modalità supportate
- Metriche di performance
- Esempi di utilizzo
- YOLOE-26: Segmentazione di Istanza a Vocabolario Aperto
  - Esempio di utilizzo
- Citazioni e ringraziamenti
- FAQ

Ultralytics YOLO26 è l'ultima evoluzione della serie YOLO di rilevatori di oggetti in tempo reale, progettata da zero per dispositivi edge e a bassa potenza. Introduce un design semplificato che elimina la complessità non necessaria integrando al contempo innovazioni mirate per offrire una distribuzione più rapida, leggera e accessibile.

Esplora ed esegui i modelli YOLO26 direttamente sulla Ultralytics .

L'architettura di YOLO26 è guidata da tre principi fondamentali:

Insieme, queste innovazioni offrono una famiglia di modelli che raggiunge una maggiore accuratezza su piccoli oggetti, fornisce un'implementazione senza interruzioni e funziona fino al 43% più velocemente sulle CPU — rendendo YOLO26 uno dei modelli YOLO più pratici e implementabili fino ad oggi per ambienti con risorse limitate.

Rimozione di DFL Il modulo Distribution Focal Loss (DFL), sebbene efficace, spesso complicava l'esportazione e limitava la compatibilità hardware. YOLO26 rimuove completamente DFL, semplificando l'inferenza e ampliando il supporto per dispositivi edge e a bassa potenza.

Inferenza End-to-End NMS-Free A differenza dei rivelatori tradizionali che si affidano a NMS come fase di post-elaborazione separata, YOLO26 è nativamente end-to-end. Le previsioni vengono generate direttamente, riducendo la latenza e rendendo l'integrazione nei sistemi di produzione più veloce, leggera e affidabile.

ProgLoss + STAL Funzioni di perdita migliorate aumentano l'accuratezza del detection, con notevoli miglioramenti nel riconoscimento di oggetti piccoli, un requisito fondamentale per IoT, robotica, immagini aeree e altre applicazioni edge.

Ottimizzatore MuSGD Un nuovo ottimizzatore ibrido che combina SGD con Muon. Ispirato a Kimi K2 di Moonshot AI, MuSGD introduce metodi di ottimizzazione avanzati dall'addestramento LLM nella computer vision, consentendo un addestramento più stabile e una convergenza più rapida.

Inferenza CPU fino al 43% più veloce Specificamente ottimizzato per l'edge computing, YOLO26 offre un'inferenza CPU significativamente più veloce, garantendo prestazioni in tempo reale su dispositivi senza GPU.

Miglioramenti nella Segmentazione di Istanza Introduce la loss di segmentazione semantica per migliorare la convergenza del modello e un modulo proto aggiornato che sfrutta le informazioni multiscala per una qualità superiore delle maschere.

Stima Precisa della Posa Integra la Stima della Log-Verosimiglianza Residua (RLE) per una localizzazione più accurata dei keypoint e ottimizza il processo di decodifica per una maggiore velocità di inferenza.

Decodifica OBB Raffinata Introduce una loss angolare specializzata per migliorare la precisione di detect per oggetti di forma quadrata e ottimizza la decodifica OBB per risolvere i problemi di discontinuità dei bordi.

YOLO26 si basa sulla versatile gamma di modelli stabilita dalle precedenti release di Ultralytics YOLO, offrendo un supporto migliorato per diverse attività di visione artificiale:

Questo framework unificato garantisce che YOLO26 sia applicabile al rilevamento in tempo reale, alla segmentazione, alla classificazione, alla stima della posa e al rilevamento di oggetti orientati — il tutto con supporto per addestramento, convalida, inferenza ed esportazione.

Vedere la Documentazione sulla Detection per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Segmentazione per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Vedere la Documentazione sulla Classificazione per esempi di utilizzo con questi modelli addestrati su ImageNet, che includono 1000 classi pre-addestrate.

Vedere la Documentazione sulla Stima della Posa per esempi di utilizzo con questi modelli addestrati su COCO, che includono 1 classe pre-addestrata, 'persona'.

Vedere la Documentazione sulla Detection Orientata per esempi di utilizzo con questi modelli addestrati su DOTAv1, che includono 15 classi pre-addestrate.

Questa sezione fornisce semplici esempi di training e inferenza YOLO26. Per la documentazione completa su queste e altre modalità, consultare le pagine della documentazione Predict, Train, Val ed Export.

Si noti che l'esempio seguente è per i modelli YOLO26 Detect per il rilevamento di oggetti. Per ulteriori attività supportate, consultare la documentazione Segment, Classify, OBB e Pose.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in Python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

YOLOE-26 integra l'architettura ad alte prestazioni YOLO26 con le capacità di vocabolario aperto della serie YOLOE. Consente il rilevamento e la segmentazione in tempo reale di qualsiasi classe di oggetti utilizzando prompt testuali, prompt visivi o una modalità senza prompt per l'inferenza zero-shot, rimuovendo efficacemente i vincoli del training a categoria fissa.

Sfruttando il design NMS-free e end-to-end di YOLO26, YOLOE-26 offre un'inferenza open-world rapida. Ciò lo rende una soluzione potente per applicazioni edge in ambienti dinamici, dove gli oggetti di interesse rappresentano un vocabolario ampio e in evoluzione.

Vedere la documentazione YOLOE per esempi di utilizzo con questi modelli addestrati sui dataset Objects365v1, GQA e Flickr30k.

Vedere la documentazione YOLOE per esempi di utilizzo con questi modelli addestrati sui dataset Objects365v1, GQA e Flickr30k.

YOLOE-26 supporta il prompting sia testuale che visivo. L'utilizzo dei prompt è semplice: basta passarli attraverso il predict method come mostrato di seguito:

I prompt testuali consentono di specificare le classi che si desidera detectare tramite descrizioni testuali. Il seguente codice mostra come utilizzare YOLOE-26 per detectare persone e autobus in un'immagine:

I prompt visivi ti consentono di guidare il modello mostrandogli esempi visivi delle classi target, anziché descriverle nel testo.

YOLOE-26 include varianti senza prompt che dispongono di un vocabolario integrato. Questi modelli non richiedono alcun prompt e funzionano come i modelli YOLO tradizionali. Invece di affidarsi a etichette fornite dall'utente o esempi visivi, detectano oggetti da un elenco predefinito di 4.585 classi basato sul set di tag utilizzato dal Recognize Anything Model Plus (RAM++).

Per un'analisi approfondita delle tecniche di prompting, dell'addestramento da zero e degli esempi di utilizzo completi, visita la documentazione di YOLOE.

Pubblicazione Ultralytics YOLO26

Ultralytics non ha pubblicato un articolo di ricerca formale per YOLO26 a causa della rapida evoluzione dei modelli. Ci concentriamo invece sulla fornitura di modelli all'avanguardia e sulla loro facilità d'uso. Per gli ultimi aggiornamenti sulle funzionalità, le architetture e l'utilizzo di YOLO, visita il nostro repository GitHub e la documentazione.

Se utilizzi YOLO26 o altro software Ultralytics nel tuo lavoro, cita il progetto come:

DOI in sospeso. YOLO26 è disponibile con licenze AGPL-3.0 ed Enterprise.

YOLO26 è una famiglia di modelli unificata, che fornisce supporto end-to-end per molteplici attività di visione artificiale:

Ogni variante di dimensione (n, s, m, l, x) supporta tutte le attività, oltre alle versioni a vocabolario aperto tramite YOLOE-26.

YOLO26 offre prestazioni edge all'avanguardia con:

I modelli YOLO26 sono stati rilasciati il 14 gennaio 2026 e sono disponibili per il download. Installa o aggiorna il ultralytics pacchetto e carica un modello:

Consulta la sezione Esempi di utilizzo per le istruzioni di addestramento, validazione ed esportazione.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (sql):
```sql
from ultralytics import YOLO

# Initialize model
model = YOLO("yoloe-26l-seg.pt")  # or select yoloe-26s/m-seg.pt for different sizes

# Set text prompt to detect person and bus. You only need to do this once after you load the model.
names = ["person", "bus"]
model.set_classes(names, model.get_text_pe(names))

# Run detection on the given image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (python):
```python
import numpy as np

from ultralytics import YOLO
from ultralytics.models.yolo.yoloe import YOLOEVPSegPredictor

# Initialize model
model = YOLO("yoloe-26l-seg.pt")

# Define visual prompts using bounding boxes and their corresponding class IDs.
# Each box highlights an example of the object you want the model to detect.
visual_prompts = dict(
    bboxes=np.array(
        [
            [221.52, 405.8, 344.98, 857.54],  # Box enclosing person
            [120, 425, 160, 445],  # Box enclosing glasses
        ],
    ),
    cls=np.array(
        [
            0,  # ID to be assigned for person
            1,  # ID to be assigned for glasses
        ]
    ),
)

# Run inference on an image, using the provided visual prompts as guidance
results = model.predict(
    "ultralytics/assets/bus.jpg",
    visual_prompts=visual_prompts,
    predictor=YOLOEVPSegPredictor,
)

# Show results
results[0].show()
```

---

## Ultralytics YOLOv5

**URL:** https://docs.ultralytics.com/ar/models/yolov5/

**Contents:**
- Ultralytics YOLOv5
- نظرة عامة
- الميزات الرئيسية
- المهام والأوضاع المدعومة
- مقاييس الأداء
- أمثلة الاستخدام
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هو Ultralytics YOLOv5u وكيف يختلف عن YOLOv5؟
  - كيف يحسن رأس Ultralytics الخالي من المرساة أداء الكشف عن الأجسام في YOLOv5u؟

يمثل YOLOv5u تطورًا في منهجيات الكشف عن الأجسام. انطلاقًا من البنية التأسيسية لنموذج YOLOv5 الذي طورته Ultralytics، يدمج YOLOv5u الرأس المنفصل الخالي من المرساة والخالي من الموضوعية، وهي ميزة تم تقديمها مسبقًا في نماذج YOLOv8. يعمل هذا التكيف على تحسين بنية النموذج، مما يؤدي إلى تحسين المفاضلة بين الدقة والسرعة في مهام الكشف عن الأجسام. بالنظر إلى النتائج التجريبية والميزات المشتقة منها، يوفر YOLOv5u بديلاً فعالاً لأولئك الذين يبحثون عن حلول قوية في كل من البحث والتطبيقات العملية.

نماذج YOLOv5 التي تم تدريبها بواسطة ultralytics/yolov5 غير متوافقة مع مكتبة ultralytics/ultralytics

توفر Ultralytics متغيرًا خاليًا من المرساة لنموذج YOLOv5. لا يمكن استخدام النماذج التي تم تدريبها باستخدام مستودع YOLOv5 الأصلي مع مكتبة Ultralytics.

استكشف ونفذ YOLOv5 مباشرة على Ultralytics .

رأس Ultralytics المنفصل الخالي من المرساة: تعتمد نماذج الكشف عن الأجسام التقليدية على مربعات مرساة محددة مسبقًا للتنبؤ بمواقع الأجسام. ومع ذلك، يقوم YOLOv5u بتحديث هذا النهج. من خلال اعتماد رأس Ultralytics منفصل خالي من المرساة، فإنه يضمن آلية كشف أكثر مرونة وقابلية للتكيف، وبالتالي تعزيز الأداء في سيناريوهات متنوعة.

موازنة مُحسَّنة بين الدقة والسرعة: غالبًا ما تتجاذب السرعة والدقة في اتجاهين متعاكسين. ولكن YOLOv5u تتحدى هذه الموازنة. إنها توفر توازنًا معايرًا، مما يضمن عمليات الكشف في الوقت الفعلي دون المساومة على الدقة. هذه الميزة لا تقدر بثمن بشكل خاص للتطبيقات التي تتطلب استجابات سريعة، مثل المركبات ذاتية القيادة، و الروبوتات، وتحليلات الفيديو في الوقت الفعلي.

مجموعة متنوعة من النماذج المدربة مسبقًا: إدراكًا بأن المهام المختلفة تتطلب مجموعات أدوات مختلفة، توفر YOLOv5u مجموعة كبيرة من النماذج المدربة مسبقًا. سواء كنت تركز على الاستدلال، أو التحقق، أو التدريب، فهناك نموذج مصمم خصيصًا في انتظارك. تضمن هذه التنوع أنك لا تستخدم حلاً واحدًا يناسب الجميع، بل نموذجًا تم ضبطه بدقة لتحديك الفريد.

تتفوق نماذج YOLOv5u، بأوزانها المتنوعة المدربة مسبقًا، في مهام اكتشاف الكائنات. وهي تدعم مجموعة شاملة من الأوضاع، مما يجعلها مناسبة للتطبيقات المتنوعة، من التطوير إلى النشر.

يوفر هذا الجدول نظرة عامة مفصلة عن متغيرات نموذج YOLOv5u، مع تسليط الضوء على قابليتها للتطبيق في مهام الكشف عن الأجسام ودعمها لأوضاع التشغيل المختلفة مثل الاستدلال و التحقق و التدريب و التصدير. يضمن هذا الدعم الشامل أن يتمكن المستخدمون من الاستفادة الكاملة من قدرات نماذج YOLOv5u في مجموعة واسعة من سيناريوهات الكشف عن الأجسام.

راجع وثائق الكشف لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

يقدم هذا المثال أمثلة بسيطة لتدريب واستدلال YOLOv5. للاطلاع على الوثائق الكاملة لهذه الأنماط وغيرها، راجع صفحات الوثائق الخاصة بـ Predict وTrain وVal وExport.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

منشور Ultralytics YOLOv5

لم تنشر Ultralytics ورقة بحثية رسمية لـ YOLOv5 بسبب الطبيعة سريعة التطور للنماذج. نحن نركز على تطوير التكنولوجيا وتسهيل استخدامها، بدلاً من إنتاج وثائق ثابتة. للحصول على أحدث المعلومات حول بنية YOLO وميزاتها واستخدامها، يرجى الرجوع إلى مستودع GitHub الخاص بنا و الوثائق.

إذا كنت تستخدم YOLOv5 أو YOLOv5u في بحثك، فيرجى الاستشهاد بمستودع Ultralytics YOLOv5 على النحو التالي:

يرجى ملاحظة أن نماذج YOLOv5 يتم توفيرها بموجب تراخيص AGPL-3.0 و Enterprise.

Ultralytics YOLOv5u هي نسخة متقدمة من YOLOv5، تدمج الرأس المنفصل الخالي من المرساة والخالي من الموضوعية الذي يعزز المفاضلة بين الدقة والسرعة لمهام الكشف عن الكائنات في الوقت الفعلي. على عكس YOLOv5 التقليدي، يعتمد YOLOv5u آلية كشف خالية من المرساة، مما يجعله أكثر مرونة وقدرة على التكيف في سيناريوهات متنوعة. لمزيد من المعلومات التفصيلية حول ميزاته، يمكنك الرجوع إلى نظرة عامة على YOLOv5.

يعمل رأس Ultralytics الخالي من المرساة في YOLOv5u على تحسين أداء الكشف عن الكائنات عن طريق إلغاء الاعتماد على مربعات المرساة المحددة مسبقًا. ينتج عن هذا آلية كشف أكثر مرونة وقدرة على التكيف يمكنها التعامل مع أحجام وأشكال الكائنات المختلفة بكفاءة أكبر. يساهم هذا التحسين بشكل مباشر في تحقيق توازن بين الدقة والسرعة، مما يجعل YOLOv5u مناسبًا للتطبيقات في الوقت الفعلي. تعرف على المزيد حول بنيته في قسم الميزات الرئيسية.

نعم، يمكنك استخدام نماذج YOLOv5u المدربة مسبقًا لمهام متنوعة مثل اكتشاف الكائنات. تدعم هذه النماذج أوضاعًا متعددة، بما في ذلك الاستدلال، والتحقق، والتدريب، والتصدير. تتيح هذه المرونة للمستخدمين الاستفادة من قدرات نماذج YOLOv5u عبر متطلبات تشغيل مختلفة. للحصول على نظرة عامة مفصلة، راجع قسم المهام والأوضاع المدعومة.

تختلف مقاييس أداء نماذج YOLOv5u اعتمادًا على النظام الأساسي والأجهزة المستخدمة. على سبيل المثال، يحقق نموذج YOLOv5nu معدل 34.3 mAP على مجموعة بيانات COCO بسرعة 73.6 مللي ثانية على وحدة المعالجة المركزية CPU ‏(ONNX) و 1.06 مللي ثانية على A100 TensorRT. يمكن العثور على مقاييس الأداء التفصيلية لنماذج YOLOv5u المختلفة في قسم مقاييس الأداء، والذي يوفر مقارنة شاملة عبر الأجهزة المختلفة.

يمكنك تدريب نموذج YOLOv5u عن طريق تحميل نموذج مدرب مسبقًا وتشغيل أمر التدريب مع مجموعة بياناتك. إليك مثال سريع:

لمزيد من الإرشادات التفصيلية، قم بزيارة قسم أمثلة الاستخدام.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov5n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv5n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv5n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov5n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv5n model and run inference on the 'bus.jpg' image
yolo predict model=yolov5n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolov5,
  title = {Ultralytics YOLOv5},
  author = {Glenn Jocher},
  year = {2020},
  version = {7.0},
  license = {AGPL-3.0},
  url = {https://github.com/ultralytics/yolov5},
  doi = {10.5281/zenodo.3908559},
  orcid = {0000-0001-5950-6979}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov5n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Ultralytics YOLOv5

**URL:** https://docs.ultralytics.com/models/yolov5/

**Contents:**
- Ultralytics YOLOv5
- Overview
- Key Features
- Supported Tasks and Modes
- Performance Metrics
- Usage Examples
- Citations and Acknowledgments
- FAQ
  - What is Ultralytics YOLOv5u and how does it differ from YOLOv5?
  - How does the anchor-free Ultralytics head improve object detection performance in YOLOv5u?

YOLOv5u represents an advancement in object detection methodologies. Originating from the foundational architecture of the YOLOv5 model developed by Ultralytics, YOLOv5u integrates the anchor-free, objectness-free split head, a feature previously introduced in the YOLOv8 models. This adaptation refines the model's architecture, leading to an improved accuracy-speed tradeoff in object detection tasks. Given the empirical results and its derived features, YOLOv5u provides an efficient alternative for those seeking robust solutions in both research and practical applications.

YOLOv5 models trained by ultralytics/yolov5 are not compatible with ultralytics/ultralytics library

Ultralytics provides an anchor-free variant of YOLOv5 model. Models trained with the original YOLOv5 repo cannot be used with the Ultralytics library.

Try on Ultralytics Platform

Explore and run YOLOv5 models directly on Ultralytics Platform.

Anchor-free Split Ultralytics Head: Traditional object detection models rely on predefined anchor boxes to predict object locations. However, YOLOv5u modernizes this approach. By adopting an anchor-free split Ultralytics head, it ensures a more flexible and adaptive detection mechanism, consequently enhancing the performance in diverse scenarios.

Optimized Accuracy-Speed Tradeoff: Speed and accuracy often pull in opposite directions. But YOLOv5u challenges this tradeoff. It offers a calibrated balance, ensuring real-time detections without compromising on accuracy. This feature is particularly invaluable for applications that demand swift responses, such as autonomous vehicles, robotics, and real-time video analytics.

Variety of Pretrained Models: Understanding that different tasks require different toolsets, YOLOv5u provides a plethora of pretrained models. Whether you're focusing on Inference, Validation, or Training, there's a tailor-made model awaiting you. This variety ensures you're not just using a one-size-fits-all solution, but a model specifically fine-tuned for your unique challenge.

The YOLOv5u models, with various pretrained weights, excel in Object Detection tasks. They support a comprehensive range of modes, making them suitable for diverse applications, from development to deployment.

This table provides a detailed overview of the YOLOv5u model variants, highlighting their applicability in object detection tasks and support for various operational modes such as Inference, Validation, Training, and Export. This comprehensive support ensures that users can fully leverage the capabilities of YOLOv5u models in a wide range of object detection scenarios.

See Detection Docs for usage examples with these models trained on COCO, which include 80 pretrained classes.

This example provides simple YOLOv5 training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in python:

CLI commands are available to directly run the models:

Ultralytics YOLOv5 Publication

Ultralytics has not published a formal research paper for YOLOv5 due to the rapidly evolving nature of the models. We focus on advancing the technology and making it easier to use, rather than producing static documentation. For the most up-to-date information on YOLO architecture, features, and usage, please refer to our GitHub repository and documentation.

If you use YOLOv5 or YOLOv5u in your research, please cite the Ultralytics YOLOv5 repository as follows:

Please note that YOLOv5 models are provided under AGPL-3.0 and Enterprise licenses.

Ultralytics YOLOv5u is an advanced version of YOLOv5, integrating the anchor-free, objectness-free split head that enhances the accuracy-speed tradeoff for real-time object detection tasks. Unlike the traditional YOLOv5, YOLOv5u adopts an anchor-free detection mechanism, making it more flexible and adaptive in diverse scenarios. For more detailed information on its features, you can refer to the YOLOv5 Overview.

The anchor-free Ultralytics head in YOLOv5u improves object detection performance by eliminating the dependency on predefined anchor boxes. This results in a more flexible and adaptive detection mechanism that can handle various object sizes and shapes with greater efficiency. This enhancement directly contributes to a balanced tradeoff between accuracy and speed, making YOLOv5u suitable for real-time applications. Learn more about its architecture in the Key Features section.

Yes, you can use pretrained YOLOv5u models for various tasks such as Object Detection. These models support multiple modes, including Inference, Validation, Training, and Export. This flexibility allows users to leverage the capabilities of YOLOv5u models across different operational requirements. For a detailed overview, check the Supported Tasks and Modes section.

The performance metrics of YOLOv5u models vary depending on the platform and hardware used. For example, the YOLOv5nu model achieves a 34.3 mAP on COCO dataset with a speed of 73.6 ms on CPU (ONNX) and 1.06 ms on A100 TensorRT. Detailed performance metrics for different YOLOv5u models can be found in the Performance Metrics section, which provides a comprehensive comparison across various devices.

You can train a YOLOv5u model by loading a pretrained model and running the training command with your dataset. Here's a quick example:

For more detailed instructions, visit the Usage Examples section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov5n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv5n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv5n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov5n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv5n model and run inference on the 'bus.jpg' image
yolo predict model=yolov5n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolov5,
  title = {Ultralytics YOLOv5},
  author = {Glenn Jocher},
  year = {2020},
  version = {7.0},
  license = {AGPL-3.0},
  url = {https://github.com/ultralytics/yolov5},
  doi = {10.5281/zenodo.3908559},
  orcid = {0000-0001-5950-6979}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov5n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## Ultralytics YOLOv5

**URL:** https://docs.ultralytics.com/it/models/yolov5/

**Contents:**
- Ultralytics YOLOv5
- Panoramica
- Caratteristiche principali
- Attività e modalità supportate
- Metriche di performance
- Esempi di utilizzo
- Citazioni e ringraziamenti
- FAQ
  - Cos'è Ultralytics YOLOv5u e in cosa differisce da YOLOv5?
  - In che modo l'head anchor-free di Ultralytics migliora le prestazioni di object detection in YOLOv5u?

YOLOv5u rappresenta un'evoluzione nelle metodologie di object detection. Derivato dall'architettura fondamentale del modello YOLOv5 sviluppato da Ultralytics, YOLOv5u integra l'head split anchor-free e objectness-free, una caratteristica precedentemente introdotta nei modelli YOLOv8. Questo adattamento perfeziona l'architettura del modello, portando a un miglior compromesso tra accuratezza e velocità nelle attività di object detection. Dati i risultati empirici e le sue caratteristiche derivate, YOLOv5u fornisce un'alternativa efficiente per coloro che cercano soluzioni robuste sia nella ricerca che nelle applicazioni pratiche.

I modelli YOLOv5 addestrati da ultralytics/yolov5 non sono compatibili con la libreria ultralytics/ultralytics

Ultralytics fornisce una variante anchor-free del modello YOLOv5. I modelli addestrati con il repository YOLOv5 originale non possono essere utilizzati con la libreria Ultralytics.

Esplora ed esegui YOLOv5 direttamente sulla Ultralytics .

Head Ultralytics split senza ancore: I modelli tradizionali di object detection si basano su anchor box predefinite per prevedere le posizioni degli oggetti. Tuttavia, YOLOv5u modernizza questo approccio. Adottando un head Ultralytics split senza ancore, garantisce un meccanismo di detection più flessibile e adattivo, migliorando di conseguenza le prestazioni in diversi scenari.

Compromesso Ottimizzato tra Accuratezza e Velocità: Velocità e accuratezza spesso tirano in direzioni opposte. Ma YOLOv5u sfida questo compromesso. Offre un bilanciamento calibrato, garantendo rilevamenti in tempo reale senza compromettere l'accuratezza. Questa caratteristica è particolarmente preziosa per le applicazioni che richiedono risposte rapide, come veicoli autonomi, robotica e analisi video in tempo reale.

Varietà di Modelli Pre-addestrati: Comprendendo che attività diverse richiedono set di strumenti differenti, YOLOv5u offre una vasta gamma di modelli pre-addestrati. Sia che tu ti stia concentrando su Inference, Validation o Training, c'è un modello su misura che ti aspetta. Questa varietà garantisce che tu non stia utilizzando una soluzione universale, ma un modello specificamente ottimizzato per la tua sfida unica.

I modelli YOLOv5u, con vari pesi pre-addestrati, eccellono nelle attività di Rilevamento Oggetti. Supportano una gamma completa di modalità, rendendoli adatti per diverse applicazioni, dallo sviluppo al deployment.

Questa tabella fornisce una panoramica dettagliata delle varianti del modello YOLOv5u, evidenziando la loro applicabilità nelle attività di rilevamento oggetti e il supporto per varie modalità operative come Inferenza, Validazione, Addestramento ed Esportazione. Questo supporto completo garantisce che gli utenti possano sfruttare appieno le capacità dei modelli YOLOv5u in un'ampia gamma di scenari di rilevamento oggetti.

Vedere la Documentazione sulla Detection per esempi di utilizzo con questi modelli addestrati su COCO, che includono 80 classi pre-addestrate.

Questo esempio fornisce semplici esempi di addestramento e inferenza di YOLOv5. Per la documentazione completa su queste e altre modalità, consultare le pagine di documentazione Predict, Train, Val ed Export.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

Pubblicazione di Ultralytics YOLOv5

Ultralytics non ha pubblicato un documento di ricerca formale per YOLOv5 a causa della rapida evoluzione dei modelli. Ci concentriamo sul progresso della tecnologia e sul renderla più facile da usare, piuttosto che sulla produzione di documentazione statica. Per le informazioni più aggiornate sull'architettura, le caratteristiche e l'utilizzo di YOLO, fare riferimento al nostro repository GitHub e alla documentazione.

Se utilizzi YOLOv5 o YOLOv5u nella tua ricerca, cita il repository Ultralytics YOLOv5 come segue:

Si prega di notare che i modelli YOLOv5 sono forniti con licenze AGPL-3.0 ed Enterprise.

Ultralytics YOLOv5u è una versione avanzata di YOLOv5, che integra l'head diviso anchor-free, objectness-free che migliora il tradeoff accuratezza-velocità per le attività di rilevamento di oggetti in tempo reale. A differenza del tradizionale YOLOv5, YOLOv5u adotta un meccanismo di rilevamento anchor-free, rendendolo più flessibile e adattabile in diversi scenari. Per informazioni più dettagliate sulle sue caratteristiche, è possibile consultare la Panoramica di YOLOv5.

L'head Ultralytics senza ancore in YOLOv5u migliora le prestazioni di object detection eliminando la dipendenza da anchor box predefinite. Ciò si traduce in un meccanismo di rilevamento più flessibile e adattivo in grado di gestire varie dimensioni e forme di oggetti con maggiore efficienza. Questo miglioramento contribuisce direttamente a un compromesso equilibrato tra accuratezza e velocità, rendendo YOLOv5u adatto per applicazioni in tempo reale. Scopri di più sulla sua architettura nella sezione Funzionalità chiave.

Sì, è possibile utilizzare modelli YOLOv5u pre-addestrati per varie attività come il Rilevamento Oggetti. Questi modelli supportano diverse modalità, tra cui Inference, Validation, Training ed Export. Questa flessibilità consente agli utenti di sfruttare le capacità dei modelli YOLOv5u per diverse esigenze operative. Per una panoramica dettagliata, consultare la sezione Attività e Modalità Supportate.

Le metriche di performance dei modelli YOLOv5u variano a seconda della piattaforma e dell'hardware utilizzati. Ad esempio, il modello YOLOv5nu raggiunge un mAP di 34,3 sul dataset COCO con una velocità di 73,6 ms su CPU (ONNX) e 1,06 ms su A100 TensorRT. Metriche di performance dettagliate per diversi modelli YOLOv5u sono disponibili nella sezione Metriche di performance, che fornisce un confronto completo tra vari dispositivi.

È possibile addestrare un modello YOLOv5u caricando un modello pre-addestrato ed eseguendo il comando di addestramento con il proprio dataset. Ecco un rapido esempio:

Per istruzioni più dettagliate, visitare la sezione Esempi di utilizzo.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov5n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv5n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv5n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov5n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv5n model and run inference on the 'bus.jpg' image
yolo predict model=yolov5n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolov5,
  title = {Ultralytics YOLOv5},
  author = {Glenn Jocher},
  year = {2020},
  version = {7.0},
  license = {AGPL-3.0},
  url = {https://github.com/ultralytics/yolov5},
  doi = {10.5281/zenodo.3908559},
  orcid = {0000-0001-5950-6979}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv5n model
model = YOLO("yolov5n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## YOLOE: Real-Time Seeing Anything

**URL:** https://docs.ultralytics.com/models/yoloe/

**Contents:**
- YOLOE: Real-Time Seeing Anything
- Introduction
- Architecture Overview
- Available Models, Supported Tasks, and Operating Modes
  - Text/Visual Prompt models
  - Prompt Free models
- Usage Examples
  - Train Usage
    - Fine-Tuning on custom dataset
  - Predict Usage

YOLOE (Real-Time Seeing Anything) is a new advancement in zero-shot, promptable YOLO models, designed for open-vocabulary detection and segmentation. Unlike previous YOLO models limited to fixed categories, YOLOE uses text, image, or internal vocabulary prompts, enabling real-time detection of any object class. Built upon YOLOv10 and inspired by YOLO-World, YOLOE achieves state-of-the-art zero-shot performance with minimal impact on speed and accuracy.

Watch: How to use YOLOE with Ultralytics Python package: Open Vocabulary & Real-Time Seeing Anything 🚀

Compared to earlier YOLO models, YOLOE significantly boosts efficiency and accuracy. It improves by +3.5 AP over YOLO-Worldv2 on LVIS while using just a third of the training resources and achieving 1.4× faster inference speeds. Fine-tuned on COCO, YOLOE-v8-large surpasses YOLOv8-L by 0.1 mAP, using nearly 4× less training time. This demonstrates YOLOE's exceptional balance of accuracy, efficiency, and versatility. The sections below explore YOLOE's architecture, benchmark comparisons, and integration with the Ultralytics framework.

YOLOE retains the standard YOLO structure—a convolutional backbone (e.g., CSP-Darknet) for feature extraction, a neck (e.g., PAN-FPN) for multi-scale fusion, and an anchor-free, decoupled detection head (as in YOLOv8/YOLO11) predicting objectness, classes, and boxes independently. YOLOE introduces three novel modules enabling open-vocabulary detection:

Re-parameterizable Region-Text Alignment (RepRTA): Supports text-prompted detection by refining text embeddings (e.g., from CLIP) via a small auxiliary network. At inference, this network is folded into the main model, ensuring zero overhead. YOLOE thus detects arbitrary text-labeled objects (e.g., unseen "traffic light") without runtime penalties.

Semantic-Activated Visual Prompt Encoder (SAVPE): Enables visual-prompted detection via a lightweight embedding branch. Given a reference image, SAVPE encodes semantic and activation features, conditioning the model to detect visually similar objects—a one-shot detection capability useful for logos or specific parts.

Lazy Region-Prompt Contrast (LRPC): In prompt-free mode, YOLOE performs open-set recognition using internal embeddings trained on large vocabularies (1200+ categories from LVIS and Objects365). Without external prompts or encoders, YOLOE identifies objects via embedding similarity lookup, efficiently handling large label spaces at inference.

Additionally, YOLOE integrates real-time instance segmentation by extending the detection head with a mask prediction branch (similar to YOLACT or YOLOv8-Seg), adding minimal overhead.

Crucially, YOLOE's open-world modules introduce no inference cost when used as a regular closed-set YOLO. Post-training, YOLOE parameters can be re-parameterized into a standard YOLO head, preserving identical FLOPs and speed (e.g., matching YOLO11 exactly).

This section details the models available with their specific pretrained weights, the tasks they support, and their compatibility with various operating modes such as Inference, Validation, Training, and Export, denoted by ✅ for supported modes and ❌ for unsupported modes.

For detailed performance benchmarks of YOLOE-26 models, see the YOLO26 Documentation.

The YOLOE models are easy to integrate into your Python applications. Ultralytics provides user-friendly Python API and CLI commands to streamline development.

You can fine-tune any pretrained YOLOE model on your custom YOLO dataset for both detection and instance segmentation tasks.

Watch: How to Train YOLOE on Car Parts Segmentation Dataset | Open-Vocabulary Model, Prediction & Export 🚀

Instance segmentation

Fine-tuning a YOLOE pretrained checkpoint mostly follows the standard YOLO training procedure. The key difference is explicitly passing YOLOEPESegTrainer as the trainer parameter to model.train():

All pretrained YOLOE models perform instance segmentation by default. To use these pretrained checkpoints for training a detection model, initialize a detection model from scratch using the YAML configuration, then load the pretrained segmentation checkpoint of the same scale. Note that we use YOLOEPETrainer instead of YOLOEPESegTrainer since we're training a detection model:

Linear probing fine-tunes only the classification branch while freezing the rest of the model. This approach is useful when working with limited data, as it prevents overfitting by leveraging previously learned features while adapting only the classification head.

Instance segmentation

For object detection task, the training process is almost the same as the instance segmentation example above but we use YOLOEPETrainer instead of YOLOEPESegTrainer, and initialize the object detection model using the YAML and then load the weights from the pretrained instance segmentation checkpoint.

YOLOE supports both text-based and visual prompting. Using prompts is straightforward—just pass them through the predict method as shown below:

Text prompts allow you to specify the classes that you wish to detect through textual descriptions. The following code shows how you can use YOLOE to detect people and buses in an image:

Visual prompts allow you to guide the model by showing it visual examples of the target classes, rather than describing them in text.

The visual_prompts argument takes a dictionary with two keys: bboxes and cls. Each bounding box in bboxes should tightly enclose an example of the object you want the model to detect, and the corresponding entry in cls specifies the class label for that box. This pairing tells the model, "This is what class X looks like—now find more like it."

Class IDs (cls) in visual_prompts are used to associate each bounding box with a specific category within your prompt. They aren't fixed labels, but temporary identifiers you assign to each example. The only requirement is that class IDs must be sequential, starting from 0. This helps the model correctly associate each box with its respective class.

You can provide visual prompts directly within the same image you want to run inference on. For example:

Or you can provide examples from a separate reference image using the refer_image argument. In that case, the bboxes and cls in visual_prompts should describe objects in the reference image, not the target image you're making predictions on:

If source is a video or stream, the model automatically uses the first frame as the refer_image. This means your visual_prompts are applied to that initial frame to help the model understand what to look for in the rest of the video. Alternatively, you can explicitly pass any specific frame as the refer_image to control which visual examples the model uses as reference.

Using refer_image also sets the classes permanently, so you can run predictions without having to supply the same visual prompts again, and export the model while retaining the ability to still detect the same classes after export:

You can also pass multiple target images to run prediction on:

YOLOE also includes prompt-free variants that come with a built-in vocabulary. These models don't require any prompts and work like traditional YOLO models. Instead of relying on user-provided labels or visual examples, they detect objects from a predefined list of 4,585 classes based on the tag set used by the Recognize Anything Model Plus (RAM++).

Model validation on a dataset is streamlined as follows:

By default it's using the provided dataset to extract visual embeddings for each category.

Alternatively we could use another dataset as a reference dataset to extract visual embeddings for each category. Note this reference dataset should have exactly the same categories as provided dataset.

The export process is similar to other YOLO models, with the added flexibility of handling text and visual prompts:

Training official YOLOE models needs segment annotations for train data, here's the script provided by official team that converts datasets to segment annotations, powered by SAM2.1 models. Or you can directly download the provided Processed Segment Annotations in following table provided by official team.

Visual Prompt models are fine-tuned based on trained-well Text Prompt models.

Since only the SAVPE module needs to be updating during training. Converting trained-well Text-prompt model to detection model and adopt detection pipeline with less training cost. Note this step is optional, you can directly start from segmentation as well.

Convert back to segmentation model after training. Only needed if you converted segmentation model to detection model before training.

Similar to visual prompt training, for prompt-free model there's only the specialized prompt embedding needs to be updating during training. Converting trained-well Text-prompt model to detection model and adopt detection pipeline with less training cost. Note this step is optional, you can directly start from segmentation as well.

Convert back to segmentation model after training. Only needed if you converted segmentation model to detection model before training.

YOLOE matches or exceeds the accuracy of closed-set YOLO models on standard benchmarks like COCO and LVIS, without compromising speed or model size. The table below compares YOLOE-L (built on YOLO11) and YOLOE26-L (built on YOLO26) against corresponding closed-set models:

†YOLOE-L shares YOLO11-L's architecture and YOLOE26-L shares YOLO26-L's architecture, resulting in similar inference speed and GFLOPs.

YOLOE26-L achieves 36.8% LVIS mAP with 32.3M parameters and 88.3B FLOPs, processing 640×640 images at 6.2 ms (161 FPS) on T4 GPU. This improves over YOLOE-L's 35.2% LVIS mAP while maintaining the same inference speed. Crucially, YOLOE's open-vocabulary modules incur no inference cost, demonstrating a "no free lunch trade-off" design.

For zero-shot tasks, YOLOE26 significantly outperforms prior open-vocabulary detectors: on LVIS, YOLOE26-S achieves 29.9% mAP, surpassing YOLO-World-S by +11.4 AP, while YOLOE26-L achieves 36.8% mAP, exceeding YOLO-World-L by +10.0 AP. YOLOE26 maintains efficient inference at 161 FPS on T4 GPU, ideal for real-time open-vocabulary applications.

Benchmark conditions: YOLOE results are from models pretrained on Objects365, GoldG, and LVIS, then fine-tuned or evaluated on COCO. YOLOE's slight mAP advantage over YOLOv8 comes from extensive pre-training. Without this open-vocab training, YOLOE matches similar-sized YOLO models, affirming its SOTA accuracy and open-world flexibility without performance penalties.

YOLOE introduces notable advancements over prior YOLO models and open-vocabulary detectors:

YOLOE vs YOLOv5:YOLOv5 offered good speed-accuracy balance but required retraining for new classes and used anchor-based heads. In contrast, YOLOE is anchor-free and dynamically detects new classes. YOLOE, building on YOLOv8's improvements, achieves higher accuracy (52.6% vs. YOLOv5's ~50% mAP on COCO) and integrates instance segmentation, unlike YOLOv5.

YOLOE vs YOLOv8: YOLOE extends YOLOv8's redesigned architecture, achieving similar or superior accuracy (52.6% mAP with ~26M parameters vs. YOLOv8-L's 52.9% with ~44M parameters). It significantly reduces training time due to stronger pre-training. The key advancement is YOLOE's open-world capability, detecting unseen objects (e.g., "bird scooter" or "peace symbol") via prompts, unlike YOLOv8's closed-set design.

YOLOE vs YOLO11:YOLO11 improves upon YOLOv8 with enhanced efficiency and fewer parameters (~22% reduction). YOLOE inherits these gains directly, matching YOLO11's inference speed and parameter count (~26M parameters), while adding open-vocabulary detection and segmentation. In closed-set scenarios, YOLOE is equivalent to YOLO11, but crucially adds adaptability to detect unseen classes, achieving YOLO11 + open-world capability without compromising speed.

YOLOE26 vs YOLOE (YOLO11-based): YOLOE26 builds upon YOLO26's architecture, inheriting its NMS-free end-to-end design for faster inference. On LVIS, YOLOE26-L achieves 36.8% mAP, improving over YOLOE-L's 35.2% mAP. YOLOE26 offers all five model scales (N/S/M/L/X) compared to YOLOE's three (S/M/L), providing more flexibility for different deployment scenarios.

YOLOE26 vs previous open-vocabulary detectors: Earlier open-vocab models (GLIP, OWL-ViT, YOLO-World) relied heavily on vision-language transformers, leading to slow inference. On LVIS, YOLOE26-S achieves 29.9% mAP (+11.4 AP over YOLO-World-S) and YOLOE26-L achieves 36.8% mAP (+10.0 AP over YOLO-World-L), while maintaining real-time inference at 161 FPS on T4 GPU. Compared to transformer-based approaches (e.g., GLIP), YOLOE26 offers orders-of-magnitude faster inference, effectively bridging the accuracy-efficiency gap in open-set detection.

In summary, YOLOE and YOLOE26 maintain YOLO's renowned speed and efficiency, surpass predecessors in accuracy, integrate segmentation, and introduce powerful open-world detection. YOLOE26 further advances the architecture with NMS-free end-to-end inference from YOLO26, making it ideal for real-time open-vocabulary applications.

YOLOE's open-vocabulary detection and segmentation enable diverse applications beyond traditional fixed-class models:

Open-World Object Detection: Ideal for dynamic scenarios like robotics, where robots recognize previously unseen objects using prompts, or security systems quickly adapting to new threats (e.g., hazardous items) without retraining.

Few-Shot and One-Shot Detection: Using visual prompts (SAVPE), YOLOE rapidly learns new objects from single reference images—perfect for industrial inspection (identifying parts or defects instantly) or custom surveillance, enabling visual searches with minimal setup.

Large-Vocabulary & Long-Tail Recognition: Equipped with a vocabulary of 1000+ classes, YOLOE excels in tasks like biodiversity monitoring (detecting rare species), museum collections, retail inventory, or e-commerce, reliably identifying many classes without extensive per-class training.

Interactive Detection and Segmentation: YOLOE supports real-time interactive applications such as searchable video/image retrieval, augmented reality (AR), and intuitive image editing, driven by natural inputs (text or visual prompts). Users can dynamically isolate, identify, or edit objects precisely using segmentation masks.

Automated Data Labeling and Bootstrapping: YOLOE facilitates rapid dataset creation by providing initial bounding box and segmentation annotations, significantly reducing human labeling efforts. Particularly valuable in analytics of large media collections, where it can auto-identify objects present, assisting in building specialized models faster.

Segmentation for Any Object: Extends segmentation capabilities to arbitrary objects through prompts—particularly beneficial for medical imaging, microscopy, or satellite imagery analysis, automatically identifying and precisely segmenting structures without specialized pretrained models. Unlike models like SAM, YOLOE simultaneously recognizes and segments objects automatically, aiding in tasks like content creation or scene understanding.

Across all these use cases, YOLOE's core advantage is versatility, providing a unified model for detection, recognition, and segmentation across dynamic scenarios. Its efficiency ensures real-time performance on resource-constrained devices, ideal for robotics, autonomous driving, defense, and beyond.

Choose YOLOE's mode based on your needs:

Often, combining modes—such as prompt-free discovery followed by targeted prompts—leverages YOLOE's full potential.

YOLOE integrates seamlessly with the Ultralytics Python API and CLI, similar to other YOLO models (YOLOv8, YOLO-World). Here's how to quickly get started:

Training and inference with YOLOE

Here, YOLOE behaves like a standard detector by default but easily switches to prompted detection by specifying classes (set_classes). Results contain bounding boxes, masks, and labels.

CLI prompts (classes) guide YOLOE similarly to Python's set_classes. Visual prompting (image-based queries) currently requires the Python API.

YOLOE automatically includes segmentation masks in inference results (results[0].masks), simplifying pixel-precise tasks like object extraction or measurement without needing separate models.

Quickly set up YOLOE with Ultralytics by following these steps:

Installation: Install or update the Ultralytics package:

Download YOLOE Weights: Pretrained YOLOE models (e.g., YOLOE-v8-S/L, YOLOE-11 variants) are available from the YOLOE GitHub releases. Simply download your desired .pt file to load into the Ultralytics YOLO class.

Hardware Requirements:

Configuration: YOLOE configurations use standard Ultralytics YAML files. Default configs (e.g., yoloe-26s-seg.yaml) typically suffice, but you can modify backbone, classes, or image size as needed.

Prompted detection (text prompt example):

The Ultralytics documentation provides further resources. YOLOE lets you easily explore powerful open-world capabilities within the familiar YOLO ecosystem.

Pro Tip: To maximize YOLOE's zero-shot accuracy, fine-tune from provided checkpoints rather than training from scratch. Use prompt words aligning with common training labels (see LVIS categories) to improve detection accuracy.

If YOLOE has contributed to your research or project, please cite the original paper by Ao Wang, Lihao Liu, Hui Chen, Zijia Lin, Jungong Han, and Guiguang Ding from Tsinghua University:

For further reading, the original YOLOE paper is available on arXiv. The project's source code and additional resources can be accessed via their GitHub repository.

While both YOLOE and YOLO-World enable open-vocabulary detection, YOLOE offers several advantages. YOLOE achieves +3.5 AP higher accuracy on LVIS while using 3× less training resources and running 1.4× faster than YOLO-Worldv2. YOLOE also supports three prompting modes (text, visual, and internal vocabulary), whereas YOLO-World primarily focuses on text prompts. Additionally, YOLOE includes built-in instance segmentation capabilities, providing pixel-precise masks for detected objects without additional overhead.

Yes, YOLOE can function exactly like a standard YOLO model with no performance penalty. When used in closed-set mode (without prompts), YOLOE's open-vocabulary modules are re-parameterized into the standard detection head, resulting in identical speed and accuracy to equivalent YOLO11 models. This makes YOLOE extremely versatile—you can use it as a traditional detector for maximum speed and then switch to open-vocabulary mode only when needed.

YOLOE supports three types of prompts:

This flexibility allows you to adapt YOLOE to various scenarios without retraining the model, making it particularly useful for dynamic environments where detection requirements change frequently.

YOLOE integrates instance segmentation directly into its architecture by extending the detection head with a mask prediction branch. This approach is similar to YOLOv8-Seg but works for any prompted object class. Segmentation masks are automatically included in inference results and can be accessed via results[0].masks. This unified approach eliminates the need for separate detection and segmentation models, streamlining workflows for applications requiring pixel-precise object boundaries.

Similar to YOLO-World, YOLOE supports a "prompt-then-detect" strategy that utilizes an offline vocabulary to enhance efficiency. Custom prompts like captions or specific object categories are pre-encoded and stored as offline vocabulary embeddings. This approach streamlines the detection process without requiring retraining. You can dynamically set these prompts within the model to tailor it to specific detection tasks:

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLOE
from ultralytics.models.yolo.yoloe import YOLOEPESegTrainer

model = YOLOE("yoloe-26s-seg.pt")

# Fine-tune on your segmentation dataset
results = model.train(
    data="coco128-seg.yaml",  # Segmentation dataset
    epochs=80,
    patience=10,
    trainer=YOLOEPESegTrainer,  # <- Important: use segmentation trainer
)
```

Example 2 (python):
```python
from ultralytics import YOLOE
from ultralytics.models.yolo.yoloe import YOLOEPETrainer

# Initialize a detection model from a config
model = YOLOE("yoloe-26s.yaml")

# Load weights from a pretrained segmentation checkpoint (same scale)
model.load("yoloe-26s-seg.pt")

# Fine-tune on your detection dataset
results = model.train(
    data="coco128.yaml",  # Detection dataset
    epochs=80,
    patience=10,
    trainer=YOLOEPETrainer,  # <- Important: use detection trainer
)
```

Example 3 (python):
```python
from ultralytics import YOLOE
from ultralytics.models.yolo.yoloe import YOLOEPESegTrainer

# Load a pretrained segmentation model
model = YOLOE("yoloe-26s-seg.pt")

# Identify the head layer index
head_index = len(model.model.model) - 1

# Freeze all backbone and neck layers (i.e., everything before the head)
freeze = [str(i) for i in range(0, head_index)]

# Freeze parts of the segmentation head, keeping only the classification branch trainable
for name, child in model.model.model[-1].named_children():
    if "cv3" not in name:
        freeze.append(f"{head_index}.{name}")

# Freeze detection branch components
freeze.extend(
    [
        f"{head_index}.cv3.0.0",
        f"{head_index}.cv3.0.1",
        f"{head_index}.cv3.1.0",
        f"{head_index}.cv3.1.1",
        f"{head_index}.cv3.2.0",
        f"{head_index}.cv3.2.1",
    ]
)

# Train only the classification branch
results = model.train(
    data="coco128-seg.yaml",  # Segmentation dataset
    epochs=80,
    patience=10,
    trainer=YOLOEPESegTrainer,  # <- Important: use segmentation trainer
    freeze=freeze,
)
```

Example 4 (python):
```python
from ultralytics import YOLOE
from ultralytics.models.yolo.yoloe import YOLOEPETrainer

# Initialize a detection model from a config
model = YOLOE("yoloe-26s.yaml")

# Load weights from a pretrained segmentation checkpoint (same scale)
model.load("yoloe-26s-seg.pt")

# Identify the head layer index
head_index = len(model.model.model) - 1

# Freeze all backbone and neck layers (i.e., everything before the head)
freeze = [str(i) for i in range(0, head_index)]

# Freeze parts of the segmentation head, keeping only the classification branch trainable
for name, child in model.model.model[-1].named_children():
    if "cv3" not in name:
        freeze.append(f"{head_index}.{name}")

# Freeze detection branch components
freeze.extend(
    [
        f"{head_index}.cv3.0.0",
        f"{head_index}.cv3.0.1",
        f"{head_index}.cv3.1.0",
        f"{head_index}.cv3.1.1",
        f"{head_index}.cv3.2.0",
        f"{head_index}.cv3.2.1",
    ]
)

# Train only the classification branch
results = model.train(
    data="coco128.yaml",  # Detection dataset
    epochs=80,
    patience=10,
    trainer=YOLOEPETrainer,  # <- Important: use detection trainer
    freeze=freeze,
)
```

---

## YOLOv10: Real-Time End-to-End Object Detection

**URL:** https://docs.ultralytics.com/models/yolov10/

**Contents:**
- YOLOv10: Real-Time End-to-End Object Detection
- Overview
  - Architecture
- Key Features
- Model Variants
- Performance
- Methodology
  - Consistent Dual Assignments for NMS-Free Training
  - Holistic Efficiency-Accuracy Driven Model Design
    - Efficiency Enhancements

YOLOv10, released in May 2024 and built on the UltralyticsPython package by researchers at Tsinghua University, introduces a new approach to real-time object detection, addressing both the post-processing and model architecture deficiencies found in previous YOLO versions. By eliminating non-maximum suppression (NMS) and optimizing various model components, YOLOv10 achieved excellent performance with significantly reduced computational overhead at its time of release. Its NMS-free end-to-end design pioneered an approach that has been further developed in YOLO26.

Watch: How to Train YOLOv10 on SKU-110k Dataset using Ultralytics | Retail Dataset

Real-time object detection aims to accurately predict object categories and positions in images with low latency. The YOLO series has been at the forefront of this research due to its balance between performance and efficiency. However, reliance on NMS and architectural inefficiencies have hindered optimal performance. YOLOv10 addresses these issues by introducing consistent dual assignments for NMS-free training and a holistic efficiency-accuracy driven model design strategy.

The architecture of YOLOv10 builds upon the strengths of previous YOLO models while introducing several key innovations. The model architecture consists of the following components:

YOLOv10 comes in various model scales to cater to different application needs:

YOLOv10 outperforms previous YOLO versions and other state-of-the-art models in terms of accuracy and efficiency. For example, YOLOv10s is 1.8x faster than RT-DETR-R18 with similar AP on the COCO dataset, and YOLOv10b has 46% less latency and 25% fewer parameters than YOLOv9-C with the same performance.

Latency measured with TensorRT FP16 on T4 GPU.

YOLOv10 employs dual label assignments, combining one-to-many and one-to-one strategies during training to ensure rich supervision and efficient end-to-end deployment. The consistent matching metric aligns the supervision between both strategies, enhancing the quality of predictions during inference.

YOLOv10 has been extensively tested on standard benchmarks like COCO, demonstrating superior performance and efficiency. The model achieves state-of-the-art results across different variants, showcasing significant improvements in latency and accuracy compared to previous versions and other contemporary detectors.

Compared to other state-of-the-art detectors:

Here is a detailed comparison of YOLOv10 variants with other state-of-the-art models:

For predicting new images with YOLOv10:

For training YOLOv10 on a custom dataset:

The YOLOv10 model series offers a range of models, each optimized for high-performance Object Detection. These models cater to varying computational needs and accuracy requirements, making them versatile for a wide array of applications.

Due to the new operations introduced with YOLOv10, not all export formats provided by Ultralytics are currently supported. The following table outlines which formats have been successfully converted using Ultralytics for YOLOv10. Feel free to open a pull request if you're able to provide a contribution change for adding export support of additional formats for YOLOv10.

YOLOv10 set a new standard in real-time object detection at its release by addressing the shortcomings of previous YOLO versions and incorporating innovative design strategies. Its NMS-free approach pioneered end-to-end object detection in the YOLO family. For the latest Ultralytics model with improved performance and NMS-free inference, see YOLO26.

We would like to acknowledge the YOLOv10 authors from Tsinghua University for their extensive research and significant contributions to the Ultralytics framework:

For detailed implementation, architectural innovations, and experimental results, please refer to the YOLOv10 research paper and GitHub repository by the Tsinghua University team.

YOLOv10, developed by researchers at Tsinghua University, introduces several key innovations to real-time object detection. It eliminates the need for non-maximum suppression (NMS) by employing consistent dual assignments during training and optimized model components for superior performance with reduced computational overhead. For more details on its architecture and key features, check out the YOLOv10 overview section.

For easy inference, you can use the Ultralytics YOLO Python library or the command line interface (CLI). Below are examples of predicting new images using YOLOv10:

For more usage examples, visit our Usage Examples section.

YOLOv10 offers several model variants to cater to different use cases:

Each variant is designed for different computational needs and accuracy requirements, making them versatile for a variety of applications. Explore the Model Variants section for more information.

YOLOv10 eliminates the need for non-maximum suppression (NMS) during inference by employing consistent dual assignments for training. This approach reduces inference latency and enhances prediction efficiency. The architecture also includes a one-to-one head for inference, ensuring that each object gets a single best prediction. For a detailed explanation, see the Consistent Dual Assignments for NMS-Free Training section.

YOLOv10 supports several export formats, including TorchScript, ONNX, OpenVINO, and TensorRT. However, not all export formats provided by Ultralytics are currently supported for YOLOv10 due to its new operations. For details on the supported formats and instructions on exporting, visit the Exporting YOLOv10 section.

YOLOv10 outperforms previous YOLO versions and other state-of-the-art models in both accuracy and efficiency. For example, YOLOv10s is 1.8x faster than RT-DETR-R18 with a similar AP on the COCO dataset. YOLOv10b shows 46% less latency and 25% fewer parameters than YOLOv9-C with the same performance. Detailed benchmarks can be found in the Comparisons section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLOv10n model
model = YOLO("yolov10n.pt")

# Perform object detection on an image
results = model("image.jpg")

# Display the results
results[0].show()
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv10n model and run inference on the 'bus.jpg' image
yolo detect predict model=yolov10n.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load YOLOv10n model from scratch
model = YOLO("yolov10n.yaml")

# Train the model
model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 4 (sql):
```sql
# Build a YOLOv10n model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov10n.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv10n model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov10n.yaml source=path/to/bus.jpg
```

---

## YOLOv10: Rilevamento di oggetti end-to-end in tempo reale

**URL:** https://docs.ultralytics.com/it/models/yolov10/

**Contents:**
- YOLOv10: Rilevamento di oggetti end-to-end in tempo reale
- Panoramica
  - Architettura
- Caratteristiche principali
- Varianti del modello
- Prestazioni
- Metodologia
  - Assegnazioni duali coerenti per l'addestramento senza NMS
  - Efficienza olistica - Progettazione del modello guidata dall'accuratezza
    - Miglioramenti dell'Efficienza

YOLOv10, rilasciato a maggio 2024 e basato sul pacchetto Python di Ultralytics sviluppato dai ricercatori della Tsinghua University, introduce un nuovo approccio al rilevamento di oggetti in tempo reale, affrontando sia le carenze di post-elaborazione che quelle dell'architettura del modello riscontrate nelle precedenti versioni di YOLO. Eliminando la soppressione non massima (NMS) e ottimizzando vari componenti del modello, YOLOv10 ha raggiunto prestazioni eccellenti con un overhead computazionale significativamente ridotto al momento del suo rilascio. Il suo design end-to-end senza NMS ha aperto la strada a un approccio che è stato ulteriormente sviluppato in YOLO26.

Guarda: Come addestrare YOLOv10 sul dataset SKU-110k utilizzando Ultralytics | Dataset per la vendita al dettaglio

Il rilevamento di oggetti in tempo reale mira a prevedere accuratamente le categorie di oggetti e le posizioni nelle immagini con bassa latenza. La serie YOLO è stata in prima linea in questa ricerca grazie al suo equilibrio tra prestazioni ed efficienza. Tuttavia, l'affidamento su NMS e le inefficienze architetturali hanno ostacolato le prestazioni ottimali. YOLOv10 affronta questi problemi introducendo assegnazioni duali coerenti per l'addestramento senza NMS e una strategia olistica di progettazione del modello guidata dall'efficienza e dalla precisione.

L'architettura di YOLOv10 si basa sui punti di forza dei precedenti modelli YOLO introducendo al contempo diverse innovazioni chiave. L'architettura del modello è composta dai seguenti componenti:

YOLOv10 è disponibile in varie scale di modello per soddisfare diverse esigenze applicative:

YOLOv10 supera le versioni precedenti di YOLO e altri modelli all'avanguardia in termini di accuratezza ed efficienza. Ad esempio, YOLOv10s è 1.8 volte più veloce di RT-DETR-R18 con un AP simile sul dataset COCO e YOLOv10b ha una latenza inferiore del 46% e il 25% in meno di parametri rispetto a YOLOv9-C con le stesse prestazioni.

Latenza misurata con TensorRT FP16 su GPU T4.

YOLOv10 impiega assegnazioni di etichette duali, combinando strategie one-to-many e one-to-one durante l'addestramento per garantire una supervisione ricca e un'implementazione end-to-end efficiente. La metrica di corrispondenza coerente allinea la supervisione tra entrambe le strategie, migliorando la qualità delle previsioni durante l'inferenza.

YOLOv10 è stato ampiamente testato su benchmark standard come COCO, dimostrando prestazioni ed efficienza superiori. Il modello raggiunge risultati all'avanguardia in diverse varianti, mostrando miglioramenti significativi in termini di latenza e accuratezza rispetto alle versioni precedenti e ad altri rilevatori contemporanei.

Rispetto ad altri rivelatori all'avanguardia:

Ecco un confronto dettagliato delle varianti di YOLOv10 con altri modelli all'avanguardia:

Per prevedere nuove immagini con YOLOv10:

Per l'addestramento di YOLOv10 su un dataset personalizzato:

La serie di modelli YOLOv10 offre una gamma di modelli, ciascuno ottimizzato per Object Detection ad alte prestazioni. Questi modelli soddisfano diverse esigenze computazionali e requisiti di accuratezza, rendendoli versatili per una vasta gamma di applicazioni.

A causa delle nuove operazioni introdotte con YOLOv10, non tutti i formati di esportazione forniti da Ultralytics sono attualmente supportati. La seguente tabella indica quali formati sono stati convertiti con successo utilizzando Ultralytics per YOLOv10. Sentiti libero di aprire una pull request se sei in grado di fornire una modifica di contributo per aggiungere il supporto all'esportazione di formati aggiuntivi per YOLOv10.

YOLOv10 ha stabilito un nuovo standard nel rilevamento di oggetti in tempo reale al momento del suo rilascio, affrontando le carenze delle precedenti versioni di YOLO e incorporando strategie di progettazione innovative. Il suo approccio senza NMS ha aperto la strada al rilevamento di oggetti end-to-end nella famiglia YOLO. Per l'ultimo modello Ultralytics con prestazioni migliorate e inferenza senza NMS, consulta YOLO26.

Desideriamo ringraziare gli autori di YOLOv10 della Tsinghua University per le loro approfondite ricerche e il significativo contributo al framework Ultralytics:

Per l'implementazione dettagliata, le innovazioni architettoniche e i risultati sperimentali, fare riferimento all'articolo di ricerca e al repository GitHub di YOLOv10 del team dell'Università di Tsinghua.

YOLOv10, sviluppato da ricercatori della Tsinghua University, introduce diverse innovazioni chiave nel rilevamento di oggetti in tempo reale. Elimina la necessità della soppressione non massima (NMS) impiegando assegnazioni duali coerenti durante l'addestramento e componenti del modello ottimizzati per prestazioni superiori con un overhead computazionale ridotto. Per maggiori dettagli sulla sua architettura e sulle caratteristiche principali, consulta la sezione panoramica di YOLOv10.

Per una facile inferenza, è possibile utilizzare la libreria Ultralytics YOLO python o l'interfaccia a riga di comando (CLI). Di seguito sono riportati esempi di previsione di nuove immagini utilizzando YOLOv10:

Per ulteriori esempi di utilizzo, visita la nostra sezione Esempi di utilizzo.

YOLOv10 offre diverse varianti di modello per soddisfare diversi casi d'uso:

Ogni variante è progettata per diverse esigenze computazionali e requisiti di accuratezza, rendendole versatili per una varietà di applicazioni. Esplora la sezione Varianti del modello per maggiori informazioni.

YOLOv10 elimina la necessità di soppressione non massima (NMS) durante l'inferenza impiegando assegnazioni duali coerenti per l'addestramento. Questo approccio riduce la latenza di inferenza e migliora l'efficienza della previsione. L'architettura include anche un head one-to-one per l'inferenza, assicurando che ogni oggetto ottenga una singola previsione migliore. Per una spiegazione dettagliata, vedere la sezione Assegnazioni Duali Coerenti per l'Addestramento Senza NMS.

YOLOv10 supporta diversi formati di esportazione, tra cui TorchScript, ONNX, OpenVINO e TensorRT. Tuttavia, non tutti i formati di esportazione forniti da Ultralytics sono attualmente supportati per YOLOv10 a causa delle sue nuove operazioni. Per dettagli sui formati supportati e istruzioni sull'esportazione, visitare la sezione Esportazione di YOLOv10.

YOLOv10 supera le versioni precedenti di YOLO e altri modelli all'avanguardia sia in termini di accuratezza che di efficienza. Ad esempio, YOLOv10s è 1.8 volte più veloce di RT-DETR-R18 con un AP simile sul dataset COCO. YOLOv10b mostra una latenza inferiore del 46% e il 25% in meno di parametri rispetto a YOLOv9-C con le stesse prestazioni. Benchmark dettagliati sono disponibili nella sezione Confronti.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLOv10n model
model = YOLO("yolov10n.pt")

# Perform object detection on an image
results = model("image.jpg")

# Display the results
results[0].show()
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv10n model and run inference on the 'bus.jpg' image
yolo detect predict model=yolov10n.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load YOLOv10n model from scratch
model = YOLO("yolov10n.yaml")

# Train the model
model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 4 (sql):
```sql
# Build a YOLOv10n model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov10n.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv10n model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov10n.yaml source=path/to/bus.jpg
```

---

## YOLOv10: الكشف الشامل عن الأجسام في الوقت الفعلي

**URL:** https://docs.ultralytics.com/ar/models/yolov10/

**Contents:**
- YOLOv10: الكشف الشامل عن الأجسام في الوقت الفعلي
- نظرة عامة
  - البنية
- الميزات الرئيسية
- متغيرات النموذج
- الأداء
- المنهجية
  - تعيينات مزدوجة متسقة للتدريب الخالي من NMS
  - تصميم النموذج الشامل المدفوع بالكفاءة-الدقة
    - تحسينات الكفاءة

يقدم YOLOv10، الذي صدر في مايو 2024 وبُني على حزمة Ultralyticspython بواسطة باحثين في جامعة تسينغهوا، نهجًا جديدًا للكشف عن الكائنات في الوقت الفعلي، معالجًا أوجه القصور في المعالجة اللاحقة وبنية النموذج الموجودة في إصدارات YOLO السابقة. من خلال التخلص من قمع غير الأقصى (NMS) وتحسين مكونات النموذج المختلفة، حقق YOLOv10 أداءً ممتازًا مع تقليل كبير في الحمل الحسابي وقت إصداره. لقد كان تصميمه الشامل الخالي من NMS رائدًا لنهج تم تطويره بشكل أكبر في YOLO26.

شاهد: كيفية تدريب YOLOv10 على مجموعة بيانات SKU-110k باستخدام Ultralytics | مجموعة بيانات البيع بالتجزئة

يهدف الكشف عن الكائنات في الوقت الفعلي إلى التنبؤ بدقة بفئات الكائنات ومواقعها في الصور بزمن انتقال منخفض. كانت سلسلة YOLO في طليعة هذا البحث نظرًا لتوازنها بين الأداء والكفاءة. ومع ذلك، فإن الاعتماد على NMS وأوجه القصور المعمارية أعاقت الأداء الأمثل. تعالج YOLOv10 هذه المشكلات من خلال تقديم تعيينات مزدوجة متسقة للتدريب الخالي من NMS واستراتيجية تصميم نموذج شاملة مدفوعة بالكفاءة والدقة.

تعتمد بنية YOLOv10 على نقاط القوة في نماذج YOLO السابقة مع تقديم العديد من الابتكارات الرئيسية. تتكون بنية النموذج من المكونات التالية:

تأتي YOLOv10 بمقاييس نماذج مختلفة لتلبية احتياجات التطبيقات المختلفة:

يتفوق YOLOv10 على إصدارات YOLO السابقة والنماذج الحديثة الأخرى من حيث الدقة والكفاءة. على سبيل المثال، YOLOv10s أسرع بـ 1.8 مرة من RT-DETR-R18 مع AP مماثل على مجموعة بيانات COCO، و YOLOv10b لديه زمن انتقال أقل بنسبة 46% وعدد معلمات أقل بنسبة 25% من YOLOv9-C مع نفس الأداء.

تم قياس زمن الوصول باستخدام TensorRT FP16 على T4 GPU.

يستخدم YOLOv10 تعيينات تسمية مزدوجة، تجمع بين استراتيجيات واحد إلى متعدد وواحد إلى واحد أثناء التدريب لضمان إشراف غني ونشر فعال من طرف إلى طرف. يتوافق مقياس المطابقة المتسق مع الإشراف بين كلتا الاستراتيجيتين، مما يعزز جودة التنبؤات أثناء الاستدلال.

تم اختبار YOLOv10 على نطاق واسع على المعايير القياسية مثل COCO، مما يدل على الأداء والكفاءة الفائقين. يحقق النموذج أحدث النتائج عبر متغيرات مختلفة، ويعرض تحسينات كبيرة في زمن الوصول والدقة مقارنة بالإصدارات السابقة وأجهزة الكشف المعاصرة الأخرى.

مقارنة بأحدث أجهزة الكشف الأخرى:

إليك مقارنة تفصيلية بين متغيرات YOLOv10 مع أحدث النماذج:

للتنبؤ بصور جديدة باستخدام YOLOv10:

لتدريب YOLOv10 على مجموعة بيانات مخصصة:

تقدم سلسلة نماذج YOLOv10 مجموعة من النماذج، تم تحسين كل منها للكشف عن الكائنات عالي الأداء. تلبي هذه النماذج الاحتياجات الحسابية المختلفة ومتطلبات الدقة، مما يجعلها متعددة الاستخدامات لمجموعة واسعة من التطبيقات.

نظرًا للعمليات الجديدة التي تم تقديمها مع YOLOv10، لا يتم دعم جميع تنسيقات التصدير التي توفرها Ultralytics حاليًا. يوضح الجدول التالي التنسيقات التي تم تحويلها بنجاح باستخدام Ultralytics لـ YOLOv10. لا تتردد في فتح طلب سحب إذا كنت قادرًا على تقديم تغيير مساهمة لإضافة دعم التصدير لتنسيقات إضافية لـ YOLOv10.

وضع YOLOv10 معيارًا جديدًا في الكشف عن الكائنات في الوقت الفعلي عند إصداره من خلال معالجة أوجه القصور في إصدارات YOLO السابقة ودمج استراتيجيات تصميم مبتكرة. لقد كان نهجه الخالي من NMS رائدًا في الكشف عن الكائنات الشامل في عائلة YOLO. للحصول على أحدث نموذج من Ultralytics مع أداء محسّن واستدلال خالٍ من NMS، راجع YOLO26.

نود أن نتقدم بالشكر لمؤلفي YOLOv10 من جامعة تسينغ هوا لأبحاثهم المكثفة ومساهماتهم الكبيرة في إطار عمل Ultralytics:

للحصول على تفاصيل التنفيذ والابتكارات المعمارية والنتائج التجريبية، يرجى الرجوع إلى الورقة البحثية و مستودع GitHub الخاص بـ YOLOv10 من قبل فريق جامعة Tsinghua.

يقدم YOLOv10، الذي تم تطويره بواسطة باحثين في جامعة تسينغ هوا، العديد من الابتكارات الرئيسية للكشف عن الأجسام في الوقت الفعلي. فهو يلغي الحاجة إلى Non-Maximum Suppression (NMS) من خلال استخدام تعيينات مزدوجة متسقة أثناء التدريب ومكونات نموذج محسّنة لتحقيق أداء فائق مع تقليل النفقات الحسابية. لمزيد من التفاصيل حول بنيته وميزاته الرئيسية، تحقق من قسم نظرة عامة على YOLOv10.

لتسهيل الاستدلال، يمكنك استخدام مكتبة Ultralytics YOLO Python أو واجهة سطر الأوامر (CLI). فيما يلي أمثلة على التنبؤ بصور جديدة باستخدام YOLOv10:

لمزيد من أمثلة الاستخدام، قم بزيارة قسم أمثلة الاستخدام الخاص بنا.

يقدم YOLOv10 العديد من متغيرات النماذج لتلبية حالات الاستخدام المختلفة:

تم تصميم كل متغير لتلبية احتياجات حسابية مختلفة ومتطلبات دقة، مما يجعلها متعددة الاستخدامات لمجموعة متنوعة من التطبيقات. استكشف قسم متغيرات النموذج لمزيد من المعلومات.

تزيل YOLOv10 الحاجة إلى التثبيط غير الأقصى (NMS) أثناء الاستدلال من خلال استخدام تعيينات مزدوجة متسقة للتدريب. يقلل هذا النهج من زمن انتقال الاستدلال ويعزز كفاءة التنبؤ. يتضمن الهيكل أيضًا رأسًا فرديًا للاستدلال، مما يضمن حصول كل كائن على أفضل تنبؤ واحد. للحصول على شرح مفصل، راجع قسم التعيينات المزدوجة المتسقة للتدريب بدون NMS.

يدعم YOLOv10 العديد من تنسيقات التصدير، بما في ذلك TorchScript و ONNX و OpenVINO و TensorRT. ومع ذلك، لا يتم دعم جميع تنسيقات التصدير التي توفرها Ultralytics حاليًا لـ YOLOv10 نظرًا لعملياته الجديدة. للحصول على تفاصيل حول التنسيقات المدعومة وإرشادات حول التصدير، تفضل بزيارة قسم تصدير YOLOv10.

يتفوق YOLOv10 على إصدارات YOLO السابقة والنماذج الحديثة الأخرى في كل من الدقة والكفاءة. على سبيل المثال، YOLOv10s أسرع بـ 1.8 مرة من RT-DETR-R18 مع AP مماثل على مجموعة بيانات COCO. يُظهر YOLOv10b زمن انتقال أقل بنسبة 46% وعدد معلمات أقل بنسبة 25% من YOLOv9-C مع نفس الأداء. يمكن العثور على معايير مفصلة في قسم المقارنات.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a pretrained YOLOv10n model
model = YOLO("yolov10n.pt")

# Perform object detection on an image
results = model("image.jpg")

# Display the results
results[0].show()
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv10n model and run inference on the 'bus.jpg' image
yolo detect predict model=yolov10n.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load YOLOv10n model from scratch
model = YOLO("yolov10n.yaml")

# Train the model
model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

Example 4 (sql):
```sql
# Build a YOLOv10n model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov10n.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv10n model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov10n.yaml source=path/to/bus.jpg
```

---

## YOLOv3, and YOLOv3u

**URL:** https://docs.ultralytics.com/models/yolov3/

**Contents:**
- YOLOv3, and YOLOv3u
- Overview
- Key Features
- Supported Tasks and Modes
- Usage Examples
- Citations and Acknowledgments
- FAQ
  - What are the differences between YOLOv3, YOLOv3-Ultralytics, and YOLOv3u?
  - How can I train a YOLOv3 model using Ultralytics?
  - What makes YOLOv3u more accurate for object detection tasks?

This document presents an overview of three closely related object detection models, namely YOLOv3, YOLOv3-Ultralytics, and YOLOv3u.

YOLOv3: This is the third version of the You Only Look Once (YOLO) object detection algorithm. Originally developed by Joseph Redmon, YOLOv3 improved on its predecessors by introducing features such as multiscale predictions and three different sizes of detection kernels.

YOLOv3u: This is an updated version of YOLOv3-Ultralytics that incorporates the anchor-free, objectness-free split head used in YOLOv8 models. YOLOv3u maintains the same backbone and neck architecture as YOLOv3 but with the updated detection head from YOLOv8.

YOLOv3: Introduced the use of three different scales for detection, leveraging three different sizes of detection kernels: 13x13, 26x26, and 52x52. This significantly improved detection accuracy for objects of different sizes. Additionally, YOLOv3 added features such as multi-label predictions for each bounding box and a better feature extractor network.

YOLOv3u: This updated model incorporates the anchor-free, objectness-free split head from YOLOv8. By eliminating the need for pre-defined anchor boxes and objectness scores, this detection head design can improve the model's ability to detect objects of varying sizes and shapes. This makes YOLOv3u more robust and accurate for object detection tasks.

YOLOv3 is designed specifically for object detection tasks. Ultralytics supports three variants of YOLOv3: yolov3u, yolov3-tinyu and yolov3-sppu. The u in the name signifies that these utilize the anchor-free head of YOLOv8, unlike their original architecture which is anchor-based. These models are renowned for their effectiveness in various real-world scenarios, balancing accuracy and speed. Each variant offers unique features and optimizations, making them suitable for a range of applications.

All three models support a comprehensive set of modes, ensuring versatility in various stages of model deployment and development. These modes include Inference, Validation, Training, and Export, providing users with a complete toolkit for effective object detection.

This table provides an at-a-glance view of the capabilities of each YOLOv3 variant, highlighting their versatility and suitability for various tasks and operational modes in object detection workflows.

This example provides simple YOLOv3 training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in python:

CLI commands are available to directly run the models:

If you use YOLOv3 in your research, please cite the original YOLO papers and the Ultralytics YOLOv3 repository:

Thank you to Joseph Redmon and Ali Farhadi for developing the original YOLOv3.

YOLOv3 is the third iteration of the YOLO (You Only Look Once) object detection algorithm developed by Joseph Redmon, known for its balance of accuracy and speed, utilizing three different scales (13x13, 26x26, and 52x52) for detections. YOLOv3-Ultralytics is Ultralytics' adaptation of YOLOv3 that adds support for more pretrained models and facilitates easier model customization. YOLOv3u is an upgraded variant of YOLOv3-Ultralytics, integrating the anchor-free, objectness-free split head from YOLOv8, improving detection robustness and accuracy for various object sizes. For more details on the variants, refer to the YOLOv3 series.

Training a YOLOv3 model with Ultralytics is straightforward. You can train the model using either Python or CLI:

For more comprehensive training options and guidelines, visit our Train mode documentation.

YOLOv3u improves upon YOLOv3 and YOLOv3-Ultralytics by incorporating the anchor-free, objectness-free split head used in YOLOv8 models. This upgrade eliminates the need for pre-defined anchor boxes and objectness scores, enhancing its capability to detect objects of varying sizes and shapes more precisely. This makes YOLOv3u a better choice for complex and diverse object detection tasks. For more information, refer to the Key Features section.

You can perform inference using YOLOv3 models by either Python scripts or CLI commands:

Refer to the Inference mode documentation for more details on running YOLO models.

YOLOv3, YOLOv3-Tiny and YOLOv3-SPP primarily support object detection tasks. These models can be used for various stages of model deployment and development, such as Inference, Validation, Training, and Export. For a comprehensive set of tasks supported and more in-depth details, visit our Object Detection tasks documentation.

If you use YOLOv3 in your research, please cite the original YOLO papers and the Ultralytics YOLOv3 repository. Example BibTeX citation:

For more citation details, refer to the Citations and Acknowledgments section.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3u model
model = YOLO("yolov3u.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv3u model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv3u model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov3u.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv3u model and run inference on the 'bus.jpg' image
yolo predict model=yolov3u.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@article{redmon2018yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal={arXiv preprint arXiv:1804.02767},
  year={2018}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3u model
model = YOLO("yolov3u.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## YOLOv3 e YOLOv3u

**URL:** https://docs.ultralytics.com/it/models/yolov3/

**Contents:**
- YOLOv3 e YOLOv3u
- Panoramica
- Caratteristiche principali
- Attività e modalità supportate
- Esempi di utilizzo
- Citazioni e ringraziamenti
- FAQ
  - Quali sono le differenze tra YOLOv3, YOLOv3-Ultralytics e YOLOv3u?
  - Come posso addestrare un modello YOLOv3 usando Ultralytics?
  - Cosa rende YOLOv3u più preciso per le attività di object detection?

Questo documento presenta una panoramica di tre modelli di rilevamento oggetti strettamente correlati, ovvero YOLOv3, YOLOv3-Ultralytics e YOLOv3u.

YOLOv3: Questa è la terza versione dell'algoritmo di object detection You Only Look Once (YOLO). Originariamente sviluppato da Joseph Redmon, YOLOv3 ha migliorato i suoi predecessori introducendo funzionalità come le previsioni multiscala e tre diverse dimensioni di kernel di rilevamento.

YOLOv3u: Si tratta di una versione aggiornata di YOLOv3-Ultralytics che incorpora l'head suddiviso senza ancore e senza objectness utilizzato nei modelli YOLOv8. YOLOv3u mantiene la stessa backbone e l'architettura del neck di YOLOv3, ma con l'detection head aggiornato di YOLOv8.

YOLOv3: Ha introdotto l'uso di tre diverse scale per il rilevamento, sfruttando tre diverse dimensioni di kernel di rilevamento: 13x13, 26x26 e 52x52. Ciò ha migliorato significativamente la precisione del rilevamento per oggetti di diverse dimensioni. Inoltre, YOLOv3 ha aggiunto funzionalità come le previsioni multi-etichetta per ogni bounding box e una migliore rete di estrazione delle caratteristiche.

YOLOv3u: Questo modello aggiornato incorpora l'head split anchor-free, objectness-free di YOLOv8. Eliminando la necessità di anchor box predefinite e di objectness score, questo design dell'head di detect può migliorare la capacità del modello di detect oggetti di varie dimensioni e forme. Ciò rende YOLOv3u più robusto e accurato per le attività di object detection.

YOLOv3 è progettato specificamente per il rilevamento di oggetti compiti. Ultralytics supporta tre varianti di YOLOv3: yolov3u, yolov3-tinyu e yolov3-sppu. u nel nome indica che questi utilizzano l'head anchor-free di YOLOv8, a differenza della loro architettura originale che è basata su anchor. Questi modelli sono rinomati per la loro efficacia in vari scenari del mondo reale, bilanciando accuratezza e velocità. Ogni variante offre caratteristiche e ottimizzazioni uniche, rendendole adatte a una vasta gamma di applicazioni.

Tutti e tre i modelli supportano un set completo di modalità, garantendo versatilità nelle varie fasi del deployment del modello e dello sviluppo. Queste modalità includono Inference, Validation, Training ed Export, fornendo agli utenti un toolkit completo per un'efficace object detection.

Questa tabella fornisce una panoramica immediata delle capacità di ciascuna variante di YOLOv3, evidenziandone la versatilità e l'idoneità per varie attività e modalità operative nei flussi di lavoro di rilevamento oggetti.

Questo esempio fornisce semplici esempi di addestramento e inferenza di YOLOv3. Per la documentazione completa su queste e altre modalità, consultare le pagine di documentazione Predict, Train, Val ed Export.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

Se utilizzi YOLOv3 nella tua ricerca, cita gli articoli originali su YOLO e il repository Ultralytics YOLOv3:

Grazie a Joseph Redmon e Ali Farhadi per aver sviluppato l'originale YOLOv3.

YOLOv3 è la terza iterazione dell'algoritmo di rilevamento oggetti YOLO (You Only Look Once) sviluppato da Joseph Redmon, noto per il suo equilibrio tra accuratezza e velocità, che utilizza tre diverse scale (13x13, 26x26 e 52x52) per i rilevamenti. YOLOv3-Ultralytics è l'adattamento di YOLOv3 da parte di Ultralytics che aggiunge il supporto per più modelli pre-addestrati e facilita la personalizzazione del modello. YOLOv3u è una variante aggiornata di YOLOv3-Ultralytics, che integra la testa divisa anchor-free e objectness-free di YOLOv8, migliorando la robustezza e l'accuratezza del rilevamento per oggetti di varie dimensioni. Per maggiori dettagli sulle varianti, fare riferimento alla serie YOLOv3.

L'addestramento di un modello YOLOv3 con Ultralytics è semplice. Puoi addestrare il modello utilizzando Python o CLI:

Per opzioni e linee guida di addestramento più complete, visitare la nostra documentazione sulla modalità di addestramento.

YOLOv3u migliora YOLOv3 e YOLOv3-Ultralytics incorporando l'head diviso senza ancore e senza objectness utilizzato nei modelli YOLOv8. Questo aggiornamento elimina la necessità di anchor box predefinite e punteggi di objectness, migliorando la sua capacità di rilevare oggetti di varie dimensioni e forme in modo più preciso. Ciò rende YOLOv3u una scelta migliore per attività di object detection complesse e diversificate. Per ulteriori informazioni, consultare la sezione Funzionalità chiave.

È possibile eseguire l'inferenza utilizzando i modelli YOLOv3 tramite script python o comandi CLI:

Consulta la documentazione sulla modalità di inferenza per maggiori dettagli sull'esecuzione dei modelli YOLO.

YOLOv3, YOLOv3-Tiny e YOLOv3-SPP supportano principalmente attività di rilevamento oggetti. Questi modelli possono essere utilizzati per varie fasi di implementazione e sviluppo del modello, come Inferenza, Convalida, Addestramento ed Esportazione. Per una serie completa di attività supportate e dettagli più approfonditi, visitare la nostra documentazione sulle attività di Object Detection.

Se utilizzi YOLOv3 nella tua ricerca, cita gli articoli originali su YOLO e il repository Ultralytics YOLOv3. Esempio di citazione BibTeX:

Per maggiori dettagli sulle citazioni, consultare la sezione Citazioni e ringraziamenti.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3u model
model = YOLO("yolov3u.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv3u model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv3u model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov3u.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv3u model and run inference on the 'bus.jpg' image
yolo predict model=yolov3u.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@article{redmon2018yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal={arXiv preprint arXiv:1804.02767},
  year={2018}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3u model
model = YOLO("yolov3u.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## YOLOv3 و YOLOv3u

**URL:** https://docs.ultralytics.com/ar/models/yolov3/

**Contents:**
- YOLOv3 و YOLOv3u
- نظرة عامة
- الميزات الرئيسية
- المهام والأوضاع المدعومة
- أمثلة الاستخدام
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هي الاختلافات بين YOLOv3 و YOLOv3-Ultralytics و YOLOv3u؟
  - كيف يمكنني تدريب نموذج YOLOv3 باستخدام Ultralytics؟
  - ما الذي يجعل YOLOv3u أكثر دقة لمهام الكشف عن الأجسام؟

تعرض هذه الوثيقة نظرة عامة على ثلاثة نماذج للكشف عن الأجسام وثيقة الصلة، وهي YOLOv3 و YOLOv3-Ultralytics و YOLOv3u.

YOLOv3: هذا هو الإصدار الثالث من خوارزمية الكشف عن الأجسام (YOLO) You Only Look Once. تم تطوير YOLOv3 في الأصل بواسطة جوزيف ريدمون، وقد حسّن YOLOv3 على سابقاتها من خلال تقديم ميزات مثل التنبؤات متعددة المقاييس وثلاثة أحجام مختلفة من نوى الكشف.

YOLOv3u: هذه نسخة محدثة من YOLOv3-Ultralytics تتضمن الرأس المنفصل الخالي من المرساة والخالي من الموضوعية المستخدم في نماذج YOLOv8. تحافظ YOLOv3u على نفس العمود الفقري وهيكل العنق مثل YOLOv3 ولكن مع رأس الكشف المحدث من YOLOv8.

YOLOv3: قدم استخدام ثلاثة مقاييس مختلفة للكشف، والاستفادة من ثلاثة أحجام مختلفة من نوى الكشف: 13x13 و 26x26 و 52x52. وقد أدى ذلك إلى تحسين دقة الكشف عن الأجسام ذات الأحجام المختلفة بشكل كبير. بالإضافة إلى ذلك، أضاف YOLOv3 ميزات مثل التنبؤات متعددة التصنيفات لكل مربع إحاطة وشبكة استخلاص ميزات أفضل.

YOLOv3u: يتضمن هذا النموذج المحدث الرأس المنفصل الخالي من المرساة والخالي من الكائنات من YOLOv8. من خلال إلغاء الحاجة إلى مربعات إرساء محددة مسبقًا وعلامات الكائنات، يمكن لتصميم رأس الاكتشاف هذا تحسين قدرة النموذج على اكتشاف الكائنات ذات الأحجام والأشكال المختلفة. هذا يجعل YOLOv3u أكثر قوة ودقة لمهام الكشف عن الكائنات.

تم تصميم YOLOv3 خصيصًا لـ اكتشاف الكائنات المهام. تدعم Ultralytics ثلاثة متغيرات من YOLOv3: yolov3u, yolov3-tinyu و yolov3-sppu. إن u يشير الاسم إلى أنها تستخدم رأس YOLOv8 الخالي من المرساة، على عكس بنيتها الأصلية القائمة على المرساة. تشتهر هذه النماذج بفعاليتها في سيناريوهات العالم الحقيقي المختلفة، وتحقيق التوازن بين الدقة والسرعة. يقدم كل متغير ميزات وتحسينات فريدة، مما يجعلها مناسبة لمجموعة من التطبيقات.

تدعم جميع النماذج الثلاثة مجموعة شاملة من الأوضاع، مما يضمن تعدد الاستخدامات في مختلف مراحل نشر النموذج وتطويره. تتضمن هذه الأوضاع الاستدلال و التحقق و التدريب و التصدير، مما يمنح المستخدمين مجموعة أدوات كاملة للكشف الفعال عن الأجسام.

يوفر هذا الجدول عرضًا سريعًا لإمكانيات كل متغير من متغيرات YOLOv3، مع تسليط الضوء على تنوعه وملاءمته لمختلف المهام وأوضاع التشغيل في مهام سير عمل الكشف عن الأجسام.

يقدم هذا المثال أمثلة بسيطة لتدريب واستدلال YOLOv3. للاطلاع على الوثائق الكاملة لهذه الأنماط وغيرها، راجع صفحات الوثائق الخاصة بـ Predict وTrain وVal وExport.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

إذا كنت تستخدم YOLOv3 في بحثك، فيرجى الاستشهاد بأوراق YOLO الأصلية ومستودع Ultralytics YOLOv3:

شكرًا لجوزيف ريدمون وعلي فرهادي لتطويرهما YOLOv3 الأصلي.

YOLOv3 هو التكرار الثالث لخوارزمية detect الكائنات YOLO (You Only Look Once) التي طورها جوزيف ريدمون، والمعروفة بتوازنها بين الدقة والسرعة، باستخدام ثلاثة مقاييس مختلفة (13x13، 26x26، و 52x52) لعمليات الـ detect. YOLOv3-Ultralytics هو تكييف Ultralytics لـ YOLOv3 الذي يضيف دعمًا لمزيد من النماذج المدربة مسبقًا ويسهل تخصيص النموذج. YOLOv3u هو نسخة مطورة من YOLOv3-Ultralytics، يدمج رأس الانقسام الخالي من الارتساء والخالي من الكائنية من YOLOv8، مما يحسن متانة الـ detect ودقتها لأحجام الكائنات المختلفة. لمزيد من التفاصيل حول المتغيرات، ارجع إلى سلسلة YOLOv3.

يعد تدريب نموذج YOLOv3 باستخدام Ultralytics أمرًا مباشرًا. يمكنك تدريب النموذج باستخدام Python أو CLI:

للحصول على خيارات وإرشادات تدريب أكثر شمولاً، تفضل بزيارة وثائق وضع التدريب الخاصة بنا.

يعمل YOLOv3u على تحسين YOLOv3 و YOLOv3-Ultralytics من خلال دمج الرأس المنفصل الخالي من المرساة والخالي من الموضوعية المستخدم في نماذج YOLOv8. تعمل هذه الترقية على إلغاء الحاجة إلى مربعات الارتساء المحددة مسبقًا وعلامات الموضوعية، مما يعزز قدرتها على اكتشاف الكائنات ذات الأحجام والأشكال المختلفة بدقة أكبر. وهذا يجعل YOLOv3u خيارًا أفضل لمهام الكشف عن الكائنات المعقدة والمتنوعة. لمزيد من المعلومات، راجع قسم الميزات الرئيسية.

يمكنك إجراء الاستدلال باستخدام نماذج YOLOv3 إما عن طريق نصوص Python أو أوامر CLI:

راجع وثائق وضع الاستدلال لمزيد من التفاصيل حول تشغيل نماذج YOLO.

تدعم YOLOv3 و YOLOv3-Tiny و YOLOv3-SPP بشكل أساسي مهام الكشف عن الأجسام. يمكن استخدام هذه النماذج في مراحل مختلفة من نشر النموذج وتطويره، مثل الاستدلال والتحقق والتدريب والتصدير. للحصول على مجموعة شاملة من المهام المدعومة والمزيد من التفاصيل المتعمقة، تفضل بزيارة وثائق مهام الكشف عن الأجسام.

إذا كنت تستخدم YOLOv3 في بحثك، فيرجى الاستشهاد بأوراق YOLO الأصلية ومستودع Ultralytics YOLOv3. مثال على اقتباس BibTeX:

لمزيد من التفاصيل حول الاقتباس، راجع قسم الاقتباسات والإقرارات.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3u model
model = YOLO("yolov3u.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv3u model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv3u model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov3u.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv3u model and run inference on the 'bus.jpg' image
yolo predict model=yolov3u.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@article{redmon2018yolov3,
  title={YOLOv3: An Incremental Improvement},
  author={Redmon, Joseph and Farhadi, Ali},
  journal={arXiv preprint arXiv:1804.02767},
  year={2018}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv3u model
model = YOLO("yolov3u.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## YOLOv4: High-Speed and Precise Object Detection

**URL:** https://docs.ultralytics.com/models/yolov4/

**Contents:**
- YOLOv4: High-Speed and Precise Object Detection
- Introduction
- Architecture
- Bag of Freebies
- Features and Performance
- Usage Examples
- Conclusion
- Citations and Acknowledgments
- FAQ
  - What is YOLOv4 and why should I use it for object detection?

Welcome to the Ultralytics documentation page for YOLOv4, a state-of-the-art, real-time object detector launched in 2020 by Alexey Bochkovskiy at https://github.com/AlexeyAB/darknet. YOLOv4 is designed to provide the optimal balance between speed and accuracy, making it an excellent choice for many applications.

YOLOv4 architecture diagram. Showcasing the intricate network design of YOLOv4, including the backbone, neck, and head components, and their interconnected layers for optimal real-time object detection.

YOLOv4 stands for You Only Look Once version 4. It is a real-time object detection model developed to address the limitations of previous YOLO versions like YOLOv3 and other object detection models. Unlike other convolutional neural network (CNN) based object detectors, YOLOv4 is not only applicable for recommendation systems but also for standalone process management and human input reduction. Its operation on conventional graphics processing units (GPUs) allows for mass usage at an affordable price, and it is designed to work in real-time on a conventional GPU while requiring only one such GPU for training.

YOLOv4 makes use of several innovative features that work together to optimize its performance. These include Weighted-Residual-Connections (WRC), Cross-Stage-Partial-connections (CSP), Cross mini-Batch Normalization (CmBN), Self-adversarial-training (SAT), Mish-activation, Mosaic data augmentation, DropBlock regularization, and CIoU loss. These features are combined to achieve state-of-the-art results.

A typical object detector is composed of several parts including the input, the backbone, the neck, and the head. The backbone of YOLOv4 is pretrained on ImageNet and is used to predict classes and bounding boxes of objects. The backbone could be from several models including VGG, ResNet, ResNeXt, or DenseNet. The neck part of the detector is used to collect feature maps from different stages and usually includes several bottom-up paths and several top-down paths. The head part is what is used to make the final object detections and classifications.

YOLOv4 also makes use of methods known as "bag of freebies," which are techniques that improve the accuracy of the model during training without increasing the cost of inference. Data augmentation is a common bag of freebies technique used in object detection, which increases the variability of the input images to improve the robustness of the model. Some examples of data augmentation include photometric distortions (adjusting the brightness, contrast, hue, saturation, and noise of an image) and geometric distortions (adding random scaling, cropping, flipping, and rotating). These techniques help the model to generalize better to different types of images.

YOLOv4 is designed for optimal speed and accuracy in object detection. The architecture of YOLOv4 includes CSPDarknet53 as the backbone, PANet as the neck, and YOLOv3 as the detection head. This design allows YOLOv4 to perform object detection at an impressive speed, making it suitable for real-time applications. YOLOv4 also excels in accuracy, achieving state-of-the-art results in object detection benchmarks like COCO.

When compared to other models in the YOLO family, such as YOLOv5 and YOLOv7, YOLOv4 maintains a strong position in the balance between speed and accuracy. While newer models may offer certain advantages, YOLOv4's architectural innovations continue to make it relevant for many applications requiring real-time performance.

As of the time of writing, Ultralytics does not currently support YOLOv4 models. Therefore, any users interested in using YOLOv4 will need to refer directly to the YOLOv4 GitHub repository for installation and usage instructions.

Here is a brief overview of the typical steps you might take to use YOLOv4:

Visit the YOLOv4 GitHub repository: https://github.com/AlexeyAB/darknet.

Follow the instructions provided in the README file for installation. This typically involves cloning the repository, installing necessary dependencies, and setting up any necessary environment variables.

Once installation is complete, you can train and use the model as per the usage instructions provided in the repository. This usually involves preparing your dataset, configuring the model parameters, training the model, and then using the trained model to perform object detection.

Please note that the specific steps may vary depending on your specific use case and the current state of the YOLOv4 repository. Therefore, it is strongly recommended to refer directly to the instructions provided in the YOLOv4 GitHub repository.

We regret any inconvenience this may cause and will strive to update this document with usage examples for Ultralytics once support for YOLOv4 is implemented.

YOLOv4 is a powerful and efficient object detection model that strikes a balance between speed and accuracy. Its use of unique features and bag of freebies techniques during training allows it to perform excellently in real-time object detection tasks. YOLOv4 can be trained and used by anyone with a conventional GPU, making it accessible and practical for a wide range of applications including surveillance systems, autonomous vehicles, and industrial automation.

For those looking to implement object detection in their projects, YOLOv4 remains a strong contender, especially when real-time performance is a priority. While Ultralytics currently focuses on supporting newer YOLO versions like YOLOv8 and YOLO11, the architectural innovations introduced in YOLOv4 have influenced the development of these later models.

We would like to acknowledge the YOLOv4 authors for their significant contributions in the field of real-time object detection:

The original YOLOv4 paper can be found on arXiv. The authors have made their work publicly available, and the codebase can be accessed on GitHub. We appreciate their efforts in advancing the field and making their work accessible to the broader community.

YOLOv4, which stands for "You Only Look Once version 4," is a state-of-the-art real-time object detection model developed by Alexey Bochkovskiy in 2020. It achieves an optimal balance between speed and accuracy, making it highly suitable for real-time applications. YOLOv4's architecture incorporates several innovative features like Weighted-Residual-Connections (WRC), Cross-Stage-Partial-connections (CSP), and Self-adversarial-training (SAT), among others, to achieve state-of-the-art results. If you're looking for a high-performance model that operates efficiently on conventional GPUs, YOLOv4 is an excellent choice.

The architecture of YOLOv4 includes several key components: the backbone, the neck, and the head. The backbone, which can be models like VGG, ResNet, or CSPDarknet53, is pretrained to predict classes and bounding boxes. The neck, utilizing PANet, connects feature maps from different stages for comprehensive data extraction. Finally, the head, which uses configurations from YOLOv3, makes the final object detections. YOLOv4 also employs "bag of freebies" techniques like mosaic data augmentation and DropBlock regularization, further optimizing its speed and accuracy.

"Bag of freebies" refers to methods that improve the training accuracy of YOLOv4 without increasing the cost of inference. These techniques include various forms of data augmentation like photometric distortions (adjusting brightness, contrast, etc.) and geometric distortions (scaling, cropping, flipping, rotating). By increasing the variability of the input images, these augmentations help YOLOv4 generalize better to different types of images, thereby improving its robustness and accuracy without compromising its real-time performance.

YOLOv4 is designed to optimize both speed and accuracy, making it ideal for real-time object detection tasks that require quick and reliable performance. It operates efficiently on conventional GPUs, needing only one for both training and inference. This makes it accessible and practical for various applications ranging from recommendation systems to standalone process management, thereby reducing the need for extensive hardware setups and making it a cost-effective solution for real-time object detection.

To get started with YOLOv4, you should visit the official YOLOv4 GitHub repository. Follow the installation instructions provided in the README file, which typically include cloning the repository, installing dependencies, and setting up environment variables. Once installed, you can train the model by preparing your dataset, configuring the model parameters, and following the usage instructions provided. Since Ultralytics does not currently support YOLOv4, it is recommended to refer directly to the YOLOv4 GitHub for the most up-to-date and detailed guidance.

**Examples:**

Example 1 (css):
```css
@misc{bochkovskiy2020yolov4,
      title={YOLOv4: Optimal Speed and Accuracy of Object Detection},
      author={Alexey Bochkovskiy and Chien-Yao Wang and Hong-Yuan Mark Liao},
      year={2020},
      eprint={2004.10934},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## YOLOv4: Object Detection ad Alta Velocità e Precisione

**URL:** https://docs.ultralytics.com/it/models/yolov4/

**Contents:**
- YOLOv4: Object Detection ad Alta Velocità e Precisione
- Introduzione
- Architettura
- Bag of Freebies
- Caratteristiche e prestazioni
- Esempi di utilizzo
- Conclusione
- Citazioni e ringraziamenti
- FAQ
  - Cos'è YOLOv4 e perché dovrei usarlo per la object detection?

Benvenuti nella pagina di documentazione di Ultralytics per YOLOv4, un rilevatore di oggetti in tempo reale all'avanguardia lanciato nel 2020 da Alexey Bochkovskiy su https://github.com/AlexeyAB/darknet. YOLOv4 è progettato per fornire l'equilibrio ottimale tra velocità e precisione, rendendolo una scelta eccellente per molte applicazioni.

Diagramma dell'architettura di YOLOv4. Presentazione dell'intricato design di rete di YOLOv4, inclusi i componenti backbone, neck e head, e i loro livelli interconnessi per il rilevamento di oggetti in tempo reale ottimale.

YOLOv4 sta per You Only Look Once versione 4. È un modello di object detection in tempo reale sviluppato per affrontare i limiti delle versioni precedenti di YOLO come YOLOv3 e altri modelli di object detection. A differenza di altri rilevatori di oggetti basati su reti neurali convoluzionali (CNN), YOLOv4 non è applicabile solo ai sistemi di raccomandazione, ma anche alla gestione autonoma dei processi e alla riduzione dell'input umano. Il suo funzionamento su unità di elaborazione grafica (GPU) convenzionali consente un utilizzo di massa a un prezzo accessibile ed è progettato per funzionare in tempo reale su una GPU convenzionale richiedendone solo una per l'addestramento.

YOLOv4 utilizza diverse funzionalità innovative che lavorano insieme per ottimizzare le sue prestazioni. Queste includono Weighted-Residual-Connections (WRC), Cross-Stage-Partial-connections (CSP), Cross mini-Batch Normalization (CmBN), Self-adversarial-training (SAT), Mish-activation, Mosaic data augmentation, DropBlock regularization e CIoU loss. Queste caratteristiche sono combinate per ottenere risultati all'avanguardia.

Un tipico rilevatore di oggetti è composto da diverse parti, tra cui l'input, il backbone, il neck e l'head. Il backbone di YOLOv4 è pre-addestrato su ImageNet e viene utilizzato per prevedere classi e bounding box degli oggetti. Il backbone potrebbe provenire da diversi modelli tra cui VGG, ResNet, ResNeXt o DenseNet. La parte del neck del rilevatore viene utilizzata per raccogliere feature map da diverse fasi e di solito include diversi percorsi bottom-up e diversi percorsi top-down. La parte dell'head è ciò che viene utilizzato per effettuare le rilevazioni e le classificazioni finali degli oggetti.

YOLOv4 utilizza anche metodi noti come "bag of freebies", ovvero tecniche che migliorano la precisione del modello durante l'addestramento senza aumentare il costo dell'inferenza. L'aumento dei dati è una tecnica comune di bag of freebies utilizzata nell'object detection, che aumenta la variabilità delle immagini di input per migliorare la robustezza del modello. Alcuni esempi di aumento dei dati includono distorsioni fotometriche (regolazione di luminosità, contrasto, tonalità, saturazione e rumore di un'immagine) e distorsioni geometriche (aggiunta di ridimensionamento, ritaglio, capovolgimento e rotazione casuali). Queste tecniche aiutano il modello a generalizzare meglio a diversi tipi di immagini.

YOLOv4 è progettato per velocità e precisione ottimali nell'object detection. L'architettura di YOLOv4 include CSPDarknet53 come backbone, PANet come neck e YOLOv3 come detection head. Questo design consente a YOLOv4 di eseguire l'object detection a una velocità impressionante, rendendolo adatto per applicazioni in tempo reale. YOLOv4 eccelle anche in termini di precisione, ottenendo risultati all'avanguardia in benchmark di object detection come COCO.

Rispetto ad altri modelli della famiglia YOLO, come YOLOv5 e YOLOv7, YOLOv4 mantiene una posizione di rilievo nell'equilibrio tra velocità e accuratezza. Sebbene i modelli più recenti possano offrire alcuni vantaggi, le innovazioni architetturali di YOLOv4 continuano a renderlo rilevante per molte applicazioni che richiedono prestazioni in tempo reale.

Al momento in cui scriviamo, Ultralytics non supporta attualmente i modelli YOLOv4. Pertanto, tutti gli utenti interessati a utilizzare YOLOv4 dovranno fare riferimento direttamente al repository GitHub di YOLOv4 per le istruzioni di installazione e utilizzo.

Ecco una breve panoramica dei passaggi tipici che potresti intraprendere per utilizzare YOLOv4:

Visita il repository GitHub di YOLOv4: https://github.com/AlexeyAB/darknet.

Segui le istruzioni fornite nel file README per l'installazione. Ciò comporta in genere la clonazione del repository, l'installazione delle dipendenze necessarie e la configurazione di eventuali variabili d'ambiente necessarie.

Una volta completata l'installazione, puoi addestrare e utilizzare il modello secondo le istruzioni d'uso fornite nel repository. Ciò di solito comporta la preparazione del dataset, la configurazione dei parametri del modello, l'addestramento del modello e quindi l'utilizzo del modello addestrato per eseguire il rilevamento degli oggetti.

Si prega di notare che i passaggi specifici possono variare a seconda del caso d'uso specifico e dello stato attuale del repository YOLOv4. Pertanto, si consiglia vivamente di fare riferimento direttamente alle istruzioni fornite nel repository GitHub di YOLOv4.

Ci scusiamo per l'inconveniente che ciò potrebbe causare e ci impegneremo ad aggiornare questo documento con esempi di utilizzo per Ultralytics una volta implementato il supporto per YOLOv4.

YOLOv4 è un modello di object detection potente ed efficiente che raggiunge un equilibrio tra velocità e precisione. L'uso di caratteristiche uniche e tecniche di bag of freebies durante l'addestramento gli consente di ottenere prestazioni eccellenti nelle attività di object detection in tempo reale. YOLOv4 può essere addestrato e utilizzato da chiunque disponga di una GPU convenzionale, rendendolo accessibile e pratico per una vasta gamma di applicazioni, tra cui sistemi di sorveglianza, veicoli autonomi e automazione industriale.

Per coloro che desiderano implementare il rilevamento di oggetti nei loro progetti, YOLOv4 rimane un valido contendente, soprattutto quando la performance in tempo reale è una priorità. Mentre Ultralytics si concentra attualmente sul supporto delle versioni più recenti di YOLO come YOLOv8 e YOLO11, le innovazioni architetturali introdotte in YOLOv4 hanno influenzato lo sviluppo di questi modelli successivi.

Desideriamo ringraziare gli autori di YOLOv4 per i loro significativi contributi nel campo del rilevamento di oggetti in tempo reale:

L'articolo originale su YOLOv4 è disponibile su arXiv. Gli autori hanno reso il loro lavoro pubblicamente disponibile e il codice può essere consultato su GitHub. Apprezziamo i loro sforzi nel far progredire il settore e nel rendere il loro lavoro accessibile alla comunità più ampia.

YOLOv4, che sta per "You Only Look Once versione 4", è un modello di object detection in tempo reale all'avanguardia sviluppato da Alexey Bochkovskiy nel 2020. Raggiunge un equilibrio ottimale tra velocità e accuratezza, rendendolo altamente adatto per applicazioni in tempo reale. L'architettura di YOLOv4 incorpora diverse caratteristiche innovative come Weighted-Residual-Connections (WRC), Cross-Stage-Partial-connections (CSP) e Self-adversarial-training (SAT), tra le altre, per ottenere risultati all'avanguardia. Se stai cercando un modello ad alte prestazioni che funzioni in modo efficiente su GPU convenzionali, YOLOv4 è una scelta eccellente.

L'architettura di YOLOv4 include diversi componenti chiave: il backbone, il neck e l'head. Il backbone, che può essere costituito da modelli come VGG, ResNet o CSPDarknet53, è pre-addestrato per prevedere classi e bounding box. Il neck, che utilizza PANet, collega le feature map da diverse fasi per un'estrazione completa dei dati. Infine, l'head, che utilizza configurazioni di YOLOv3, effettua le rilevazioni finali degli oggetti. YOLOv4 impiega anche tecniche "bag of freebies" come l'aumento dei dati a mosaico e la regolarizzazione DropBlock, ottimizzando ulteriormente la sua velocità e precisione.

"Bag of freebies" si riferisce a metodi che migliorano l'accuratezza di training di YOLOv4 senza aumentare il costo di inferenza. Queste tecniche includono varie forme di aumento dei dati come distorsioni fotometriche (regolazione di luminosità, contrasto, ecc.) e distorsioni geometriche (ridimensionamento, ritaglio, ribaltamento, rotazione). Aumentando la variabilità delle immagini di input, questi aumenti aiutano YOLOv4 a generalizzare meglio a diversi tipi di immagini, migliorando così la sua robustezza e accuratezza senza compromettere le sue prestazioni in tempo reale.

YOLOv4 è progettato per ottimizzare sia la velocità che l'accuratezza, rendendolo ideale per attività di object detection in tempo reale che richiedono prestazioni rapide e affidabili. Funziona in modo efficiente su GPU convenzionali, necessitandone solo una sia per l'addestramento che per l'inferenza. Questo lo rende accessibile e pratico per varie applicazioni, dai sistemi di raccomandazione alla gestione autonoma dei processi, riducendo così la necessità di configurazioni hardware estese e rendendolo una soluzione экономически efficace per l'object detection in tempo reale.

Per iniziare con YOLOv4, dovresti visitare il repository GitHub ufficiale di YOLOv4. Segui le istruzioni di installazione fornite nel file README, che in genere includono la clonazione del repository, l'installazione delle dipendenze e l'impostazione delle variabili d'ambiente. Una volta installato, puoi addestrare il modello preparando il tuo dataset, configurando i parametri del modello e seguendo le istruzioni d'uso fornite. Poiché Ultralytics attualmente non supporta YOLOv4, si consiglia di fare riferimento direttamente al GitHub di YOLOv4 per la guida più aggiornata e dettagliata.

**Examples:**

Example 1 (css):
```css
@misc{bochkovskiy2020yolov4,
      title={YOLOv4: Optimal Speed and Accuracy of Object Detection},
      author={Alexey Bochkovskiy and Chien-Yao Wang and Hong-Yuan Mark Liao},
      year={2020},
      eprint={2004.10934},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## YOLOv4: كشف دقيق وعالي السرعة عن الأجسام

**URL:** https://docs.ultralytics.com/ar/models/yolov4/

**Contents:**
- YOLOv4: كشف دقيق وعالي السرعة عن الأجسام
- مقدمة
- البنية
- حقيبة المكافآت المجانية
- الميزات والأداء
- أمثلة الاستخدام
- الخلاصة
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هو YOLOv4 ولماذا يجب علي استخدامه في الكشف عن الأجسام؟

مرحبًا بك في صفحة وثائق Ultralytics الخاصة بـ YOLOv4، وهي أداة متطورة للكشف عن الأجسام في الوقت الفعلي تم إطلاقها في عام 2020 بواسطة Alexey Bochkovskiy على https://github.com/AlexeyAB/darknet. تم تصميم YOLOv4 لتوفير التوازن الأمثل بين السرعة والدقة، مما يجعلها خيارًا ممتازًا للعديد من التطبيقات.

مخطط هيكلية YOLOv4. يعرض التصميم الشبكي المعقد لـ YOLOv4، بما في ذلك المكونات الأساسية والعنق والرأس، والطبقات المترابطة الخاصة بها للكشف الأمثل عن الأجسام في الوقت الفعلي.

يرمز YOLOv4 إلى You Only Look Once الإصدار الرابع. وهو نموذج للكشف عن الأجسام في الوقت الفعلي تم تطويره لمعالجة القيود المفروضة على إصدارات YOLO السابقة مثل YOLOv3 ونماذج الكشف عن الأجسام الأخرى. بخلاف أدوات الكشف الأخرى عن الأجسام المستندة إلى شبكة عصبونية التفافية (CNN)، فإن YOLOv4 ليست قابلة للتطبيق فقط لأنظمة التوصية ولكن أيضًا لإدارة العمليات المستقلة وتقليل المدخلات البشرية. يتيح تشغيلها على وحدات معالجة الرسومات (GPUs) التقليدية استخدامها على نطاق واسع وبسعر معقول، وهي مصممة للعمل في الوقت الفعلي على وحدة معالجة رسومات (GPU) تقليدية مع طلب وحدة معالجة رسومات واحدة فقط للتدريب.

يستخدم YOLOv4 العديد من الميزات المبتكرة التي تعمل معًا لتحسين أدائه. وتشمل هذه الميزات اتصالات الوزن المتبقية (WRC)، واتصالات الأجزاء المتقاطعة (CSP)، والتطبيع المصغر المتقاطع Batch Normalization (CmBN)، والتدريب الذاتي الخصوم (SAT)، وتنشيط Mish، وزيادة البيانات Mosaic، وتسوية DropBlock، وخسارة CIoU. يتم دمج هذه الميزات لتحقيق أحدث النتائج.

يتكون كاشف الكائنات النموذجي من عدة أجزاء بما في ذلك المدخلات، والعمود الفقري (backbone)، والرقبة (neck)، والرأس (head). يتم تدريب العمود الفقري لـ YOLOv4 مسبقًا على ImageNet ويستخدم للتنبؤ بالفئات والمربعات المحيطة (bounding boxes) للكائنات. يمكن أن يكون العمود الفقري من عدة نماذج بما في ذلك VGG أو ResNet أو ResNeXt أو DenseNet. يستخدم جزء الرقبة من الكاشف لجمع خرائط الميزات (feature maps) من مراحل مختلفة وعادة ما يتضمن عدة مسارات من الأسفل إلى الأعلى وعدة مسارات من الأعلى إلى الأسفل. الجزء الرأسي هو ما يستخدم لإجراء عمليات detect الكائنات والتصنيفات النهائية.

تستخدم YOLOv4 أيضًا طرقًا تعرف باسم "حقيبة الأشياء المجانية"، وهي تقنيات تعمل على تحسين دقة النموذج أثناء التدريب دون زيادة تكلفة الاستدلال. زيادة البيانات هي تقنية شائعة في حقيبة الأشياء المجانية المستخدمة في اكتشاف الكائنات، والتي تزيد من تقلب الصور المدخلة لتحسين قوة النموذج. تتضمن بعض أمثلة زيادة البيانات تشويهات قياس ضوئي (تعديل السطوع والتباين واللون والتشبع والضوضاء في الصورة) وتشويهات هندسية (إضافة تحجيم عشوائي واقتصاص وقلب وتدوير). تساعد هذه التقنيات النموذج على التعميم بشكل أفضل لأنواع مختلفة من الصور.

تم تصميم YOLOv4 لتحقيق السرعة والدقة المثلى في الكشف عن الكائنات. تشتمل بنية YOLOv4 على CSPDarknet53 باعتباره العمود الفقري، وPANet باعتباره الرقبة، وYOLOv3 باعتباره رأس الكشف. يتيح هذا التصميم لـ YOLOv4 إجراء الكشف عن الكائنات بسرعة مذهلة، مما يجعله مناسبًا للتطبيقات في الوقت الفعلي. يتفوق YOLOv4 أيضًا في الدقة، حيث يحقق أحدث النتائج في معايير الكشف عن الكائنات مثل COCO.

بالمقارنة مع النماذج الأخرى في عائلة YOLO، مثل YOLOv5 و YOLOv7، يحافظ YOLOv4 على مكانة قوية في التوازن بين السرعة والدقة. في حين أن النماذج الأحدث قد تقدم مزايا معينة، إلا أن الابتكارات المعمارية لـ YOLOv4 لا تزال تجعلها ذات صلة بالعديد من التطبيقات التي تتطلب أداءً في الوقت الفعلي.

اعتبارًا من وقت كتابة هذا التقرير، لا تدعم Ultralytics حاليًا نماذج YOLOv4. لذلك، سيحتاج أي مستخدمين مهتمين باستخدام YOLOv4 إلى الرجوع مباشرةً إلى مستودع YOLOv4 GitHub للحصول على إرشادات التثبيت والاستخدام.

فيما يلي نظرة عامة موجزة عن الخطوات النموذجية التي قد تتخذها لاستخدام YOLOv4:

قم بزيارة مستودع YOLOv4 GitHub: https://github.com/AlexeyAB/darknet.

اتبع الإرشادات المتوفرة في ملف README للتثبيت. يتضمن هذا عادةً استنساخ المستودع وتثبيت التبعيات الضرورية وإعداد أي متغيرات بيئية ضرورية.

بمجرد اكتمال التثبيت، يمكنك تدريب النموذج واستخدامه وفقًا لإرشادات الاستخدام المتوفرة في المستودع. يتضمن هذا عادةً إعداد مجموعة البيانات الخاصة بك وتكوين معلمات النموذج وتدريب النموذج ثم استخدام النموذج المدرب لإجراء الكشف عن الأجسام.

يرجى ملاحظة أن الخطوات المحددة قد تختلف وفقًا لحالة الاستخدام المحددة الخاصة بك والحالة الحالية لمستودع YOLOv4. لذلك، يوصى بشدة بالرجوع مباشرةً إلى الإرشادات المتوفرة في مستودع YOLOv4 GitHub.

نأسف لأي إزعاج قد يسببه هذا وسنسعى جاهدين لتحديث هذا المستند بأمثلة استخدام لـ Ultralytics بمجرد تنفيذ دعم YOLOv4.

YOLOv4 هو نموذج قوي وفعال لاكتشاف الكائنات يحقق توازنًا بين السرعة والدقة. يتيح له استخدامه للميزات الفريدة وتقنيات حقيبة الأشياء المجانية أثناء التدريب الأداء بشكل ممتاز في مهام الكشف عن الكائنات في الوقت الفعلي. يمكن تدريب YOLOv4 واستخدامه من قبل أي شخص لديه وحدة معالجة رسومات تقليدية، مما يجعله في متناول الجميع وعمليًا لمجموعة واسعة من التطبيقات بما في ذلك أنظمة المراقبة و المركبات ذاتية القيادة و الأتمتة الصناعية.

بالنسبة لأولئك الذين يتطلعون إلى تنفيذ الكشف عن الكائنات في مشاريعهم، يظل YOLOv4 منافسًا قويًا، خاصةً عندما تكون الأولوية للأداء في الوقت الفعلي. بينما تركز Ultralytics حاليًا على دعم إصدارات YOLO الأحدث مثل YOLOv8 و YOLO11، فقد أثرت الابتكارات المعمارية التي تم تقديمها في YOLOv4 على تطوير هذه النماذج اللاحقة.

نود أن نعرب عن تقديرنا لمؤلفي YOLOv4 لمساهماتهم الكبيرة في مجال الكشف عن الأجسام في الوقت الفعلي:

يمكن العثور على ورقة YOLOv4 الأصلية على arXiv. لقد أتاح المؤلفون عملهم للجمهور، ويمكن الوصول إلى قاعدة التعليمات البرمجية على GitHub. نحن نقدر جهودهم في تطوير هذا المجال وإتاحة عملهم للمجتمع الأوسع.

YOLOv4، التي تعني "You Only Look Once الإصدار 4"، هو نموذج حديث للكشف عن الأجسام في الوقت الفعلي تم تطويره بواسطة Alexey Bochkovskiy في عام 2020. إنه يحقق توازنًا مثاليًا بين السرعة و الدقة، مما يجعله مناسبًا للغاية للتطبيقات في الوقت الفعلي. يتضمن هيكل YOLOv4 العديد من الميزات المبتكرة مثل Weighted-Residual-Connections (WRC) و Cross-Stage-Partial-connections (CSP) و Self-adversarial-training (SAT)، من بين أمور أخرى، لتحقيق أحدث النتائج. إذا كنت تبحث عن نموذج عالي الأداء يعمل بكفاءة على وحدات معالجة الرسومات (GPUs) التقليدية، فإن YOLOv4 يعد خيارًا ممتازًا.

تتضمن بنية YOLOv4 عدة مكونات رئيسية: العمود الفقري (backbone)، والرقبة (neck)، والرأس (head). العمود الفقري، الذي يمكن أن يكون نماذج مثل VGG أو ResNet أو CSPDarknet53، مدرب مسبقًا للتنبؤ بالفئات والمربعات المحيطة (bounding boxes). الرقبة، التي تستخدم PANet، تربط خرائط الميزات (feature maps) من مراحل مختلفة لاستخراج البيانات الشامل. أخيرًا، الرأس، الذي يستخدم تكوينات من YOLOv3، يقوم بعمليات detect الكائنات النهائية. تستخدم YOLOv4 أيضًا تقنيات "حقيبة الهدايا المجانية" (bag of freebies) مثل زيادة البيانات الفسيفسائية (mosaic data augmentation) وتنظيم DropBlock، مما يزيد من تحسين سرعتها ودقتها.

تشير "حقيبة المكافآت المجانية" إلى الأساليب التي تعمل على تحسين دقة التدريب لـ YOLOv4 دون زيادة تكلفة الاستدلال. تتضمن هذه التقنيات أشكالًا مختلفة من زيادة البيانات مثل التشوهات الضوئية (تعديل السطوع والتباين وما إلى ذلك) والتشوهات الهندسية (التحجيم والقص والقلب والتدوير). من خلال زيادة تقلب صور الإدخال، تساعد هذه الزيادات YOLOv4 على التعميم بشكل أفضل لأنواع مختلفة من الصور، وبالتالي تحسين متانتها ودقتها دون المساس بأدائها في الوقت الفعلي.

تم تصميم YOLOv4 لتحسين كل من السرعة والدقة، مما يجعله مثاليًا لمهام الكشف عن الأجسام في الوقت الفعلي التي تتطلب أداءً سريعًا وموثوقًا. إنه يعمل بكفاءة على وحدات معالجة الرسومات (GPUs) التقليدية، ولا يحتاج إلا إلى واحدة لكل من التدريب والاستدلال. وهذا يجعله في متناول الجميع وعمليًا لمختلف التطبيقات التي تتراوح من أنظمة التوصية إلى إدارة العمليات المستقلة، وبالتالي يقلل الحاجة إلى إعدادات الأجهزة المكثفة ويجعله حلاً فعالاً من حيث التكلفة للكشف عن الأجسام في الوقت الفعلي.

للبدء في استخدام YOLOv4، يجب عليك زيارة مستودع YOLOv4 GitHub الرسمي. اتبع إرشادات التثبيت المتوفرة في ملف README، والتي تتضمن عادةً استنساخ المستودع وتثبيت التبعيات وإعداد متغيرات البيئة. بمجرد التثبيت، يمكنك تدريب النموذج عن طريق إعداد مجموعة البيانات الخاصة بك وتكوين معلمات النموذج واتباع إرشادات الاستخدام المتوفرة. نظرًا لأن Ultralytics لا تدعم YOLOv4 حاليًا، فمن المستحسن الرجوع مباشرةً إلى YOLOv4 GitHub للحصول على أحدث الإرشادات وأكثرها تفصيلاً.

**Examples:**

Example 1 (css):
```css
@misc{bochkovskiy2020yolov4,
      title={YOLOv4: Optimal Speed and Accuracy of Object Detection},
      author={Alexey Bochkovskiy and Chien-Yao Wang and Hong-Yuan Mark Liao},
      year={2020},
      eprint={2004.10934},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```

---

## YOLOv7: Bag-of-Freebies addestrabile

**URL:** https://docs.ultralytics.com/it/models/yolov7/

**Contents:**
- YOLOv7: Bag-of-Freebies addestrabile
- Confronto tra i rilevatori di oggetti SOTA
- Panoramica
- Caratteristiche principali
- Esempi di utilizzo
  - Esportazione ONNX
  - Esportazione TensorRT
- Citazioni e ringraziamenti
- FAQ
  - Cos'è YOLOv7 e perché è considerato una svolta nel object detection in tempo reale?

YOLOv7, rilasciato a luglio 2022, ha rappresentato un significativo progresso nel rilevamento di oggetti in tempo reale al momento del suo rilascio. Ha raggiunto il 56,8% di AP su GPU V100, stabilendo nuovi benchmark al momento della sua introduzione. YOLOv7 ha superato i rilevatori di oggetti contemporanei come YOLOR, YOLOX, Scaled-YOLOv4 e YOLOv5 in velocità e accuratezza. Il modello è addestrato sul dataset MS COCO da zero senza utilizzare altri dataset o pesi pre-addestrati. Il codice sorgente di YOLOv7 è disponibile su GitHub. Si noti che modelli più recenti come YOLO11 e YOLO26 hanno da allora raggiunto una maggiore accuratezza con un'efficienza migliorata.

Dai risultati nella tabella di confronto YOLO sappiamo che il metodo proposto ha il miglior compromesso velocità-accuratezza in modo completo. Se confrontiamo YOLOv7-tiny-SiLU con YOLOv5-N (r6.1), il nostro metodo è più veloce di 127 fps e più preciso del 10,7% su AP. Inoltre, YOLOv7 ha il 51,4% di AP a una frequenza di fotogrammi di 161 fps, mentre PPYOLOE-L con lo stesso AP ha solo una frequenza di fotogrammi di 78 fps. In termini di utilizzo dei parametri, YOLOv7 è inferiore del 41% rispetto a PPYOLOE-L.

Se confrontiamo YOLOv7-X con una velocità di inferenza di 114 fps con YOLOv5-L (r6.1) con una velocità di inferenza di 99 fps, YOLOv7-X può migliorare l'AP del 3,9%. Se YOLOv7-X viene confrontato con YOLOv5-X (r6.1) di scala simile, la velocità di inferenza di YOLOv7-X è di 31 fps più veloce. Inoltre, in termini di quantità di parametri e calcolo, YOLOv7-X riduce il 22% dei parametri e l'8% del calcolo rispetto a YOLOv5-X (r6.1), ma migliora l'AP del 2,2% (Source).

Il rilevamento di oggetti in tempo reale è una componente importante in molti sistemi di computer vision, tra cui il tracking multi-oggetto, la guida autonoma, la robotica e l'analisi di immagini mediche. Negli ultimi anni, lo sviluppo del rilevamento di oggetti in tempo reale si è concentrato sulla progettazione di architetture efficienti e sul miglioramento della velocità di Inference API di varie CPU, GPU e unità di elaborazione neurale (NPU). YOLOv7 supporta sia GPU mobile che dispositivi GPU, dall'edge al cloud.

A differenza dei tradizionali object detector in tempo reale che si concentrano sull'ottimizzazione dell'architettura, YOLOv7 introduce un focus sull'ottimizzazione del processo di addestramento. Ciò include moduli e metodi di ottimizzazione progettati per migliorare l'accuratezza dell'object detection senza aumentare il costo di inferenza, un concetto noto come "trainable bag-of-freebies".

YOLOv7 introduce diverse caratteristiche chiave:

Riparamentrizzazione del modello: YOLOv7 propone un modello riparametrizzato pianificato, che è una strategia applicabile ai layer in diverse reti con il concetto di percorso di propagazione del gradiente.

Assegnazione dinamica delle etichette: Il training del modello con più livelli di output presenta un nuovo problema: "Come assegnare target dinamici agli output di diversi branch?" Per risolvere questo problema, YOLOv7 introduce un nuovo metodo di assegnazione delle etichette chiamato coarse-to-fine lead guided label assignment.

Scalabilità estesa e composta: YOLOv7 propone metodi di "estensione" e "scalabilità composta" per il rilevatore di oggetti in tempo reale che possono utilizzare efficacemente parametri e calcoli.

Efficienza: Il metodo proposto da YOLOv7 può ridurre efficacemente circa il 40% dei parametri e il 50% del calcolo del rilevatore di oggetti in tempo reale all'avanguardia, e ha una velocità di inferenza più rapida e una maggiore accuratezza di detect.

Al momento in cui scriviamo, Ultralytics supporta solo l'inferenza ONNX e TensorRT per YOLOv7.

Per utilizzare il modello YOLOv7 ONNX con Ultralytics:

(Opzionale) Installa Ultralytics ed esporta un modello ONNX per avere le dipendenze richieste installate automaticamente:

Esporta il modello YOLOv7 desiderato utilizzando l'exporter nel repository YOLOv7:

Modifica il grafico del modello ONNX per essere compatibile con Ultralytics utilizzando il seguente script:

Puoi quindi caricare il modello ONNX modificato ed eseguire normalmente l'inferenza con esso in Ultralytics:

Seguire i passaggi 1-2 nella sezione Esportazione ONNX.

Installa il TensorRT Pacchetto Python:

Esegui lo script seguente per convertire il modello ONNX modificato in un motore TensorRT:

Carica ed esegui il modello in Ultralytics:

Desideriamo ringraziare gli autori di YOLOv7 per il loro significativo contributo nel campo del rilevamento di oggetti in tempo reale:

Il paper originale di YOLOv7 è disponibile su arXiv. Gli autori hanno reso il loro lavoro pubblicamente disponibile e il codice può essere consultato su GitHub. Apprezziamo i loro sforzi nel far progredire il settore e nel rendere il loro lavoro accessibile alla comunità più ampia.

YOLOv7, rilasciato a luglio 2022, è stato un significativo modello di rilevamento oggetti in tempo reale che ha raggiunto eccellenti velocità e accuratezza al momento del suo rilascio. Ha superato modelli contemporanei come YOLOX, YOLOv5 e PPYOLOE sia nell'utilizzo dei parametri che nella velocità di inferenza. Le caratteristiche distintive di YOLOv7 includono la riparametrizzazione del modello e l'assegnazione dinamica delle etichette, che ottimizzano le sue prestazioni senza aumentare i costi di inferenza. Per maggiori dettagli tecnici sulla sua architettura e sulle metriche di confronto con altri rilevatori di oggetti all'avanguardia, fare riferimento all'articolo su YOLOv7.

YOLOv7 introduce diverse innovazioni, tra cui la riparametrizzazione del modello e l'assegnazione dinamica delle etichette, che migliorano il processo di addestramento e aumentano la precisione dell'inferenza. Rispetto a YOLOv5, YOLOv7 aumenta significativamente la velocità e la precisione. Ad esempio, YOLOv7-X migliora la precisione del 2,2% e riduce i parametri del 22% rispetto a YOLOv5-X. Confronti dettagliati sono disponibili nella tabella delle prestazioni confronto tra YOLOv7 e i rilevatori di oggetti SOTA.

Al momento, Ultralytics supporta solo l'inferenza ONNX e TensorRT di YOLOv7. Per eseguire la versione esportata ONNX e TensorRT di YOLOv7 con Ultralytics, consultare la sezione Esempi di utilizzo.

Per installare e addestrare un modello YOLOv7 personalizzato, segui questi passaggi:

Prepara il tuo dataset e configura i parametri del modello secondo le istruzioni d'uso fornite nel repository. Per ulteriori indicazioni, visita il repository YOLOv7 su GitHub per le informazioni e gli aggiornamenti più recenti.

Dopo l'addestramento, è possibile esportare il modello in ONNX o TensorRT per l'uso in Ultralytics come mostrato in Esempi di utilizzo.

YOLOv7 offre diverse caratteristiche chiave che rivoluzionano l'object detection in tempo reale:

Per ulteriori dettagli su queste funzionalità, consultare la sezione Panoramica di YOLOv7.

**Examples:**

Example 1 (unknown):
```unknown
pip install ultralytics
yolo export model=yolo26n.pt format=onnx
```

Example 2 (unknown):
```unknown
git clone https://github.com/WongKinYiu/yolov7
cd yolov7
python export.py --weights yolov7-tiny.pt --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640
```

Example 3 (sql):
```sql
import numpy as np
import onnx
from onnx import helper, numpy_helper

# Load the ONNX model
model_path = "yolov7/yolov7-tiny.onnx"  # Replace with your model path
model = onnx.load(model_path)
graph = model.graph

# Fix input shape to batch size 1
input_shape = graph.input[0].type.tensor_type.shape
input_shape.dim[0].dim_value = 1

# Define the output of the original model
original_output_name = graph.output[0].name

# Create slicing nodes
sliced_output_name = f"{original_output_name}_sliced"

# Define initializers for slicing (remove the first value)
start = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_start")
end = numpy_helper.from_array(np.array([7], dtype=np.int64), name="slice_end")
axes = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_axes")
steps = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_steps")

graph.initializer.extend([start, end, axes, steps])

slice_node = helper.make_node(
    "Slice",
    inputs=[original_output_name, "slice_start", "slice_end", "slice_axes", "slice_steps"],
    outputs=[sliced_output_name],
    name="SliceNode",
)
graph.node.append(slice_node)

# Define segment slicing
seg1_start = numpy_helper.from_array(np.array([0], dtype=np.int64), name="seg1_start")
seg1_end = numpy_helper.from_array(np.array([4], dtype=np.int64), name="seg1_end")
seg2_start = numpy_helper.from_array(np.array([4], dtype=np.int64), name="seg2_start")
seg2_end = numpy_helper.from_array(np.array([5], dtype=np.int64), name="seg2_end")
seg3_start = numpy_helper.from_array(np.array([5], dtype=np.int64), name="seg3_start")
seg3_end = numpy_helper.from_array(np.array([6], dtype=np.int64), name="seg3_end")

graph.initializer.extend([seg1_start, seg1_end, seg2_start, seg2_end, seg3_start, seg3_end])

# Create intermediate tensors for segments
segment_1_name = f"{sliced_output_name}_segment1"
segment_2_name = f"{sliced_output_name}_segment2"
segment_3_name = f"{sliced_output_name}_segment3"

# Add segment slicing nodes
graph.node.extend(
    [
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg1_start", "seg1_end", "slice_axes", "slice_steps"],
            outputs=[segment_1_name],
            name="SliceSegment1",
        ),
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg2_start", "seg2_end", "slice_axes", "slice_steps"],
            outputs=[segment_2_name],
            name="SliceSegment2",
        ),
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg3_start", "seg3_end", "slice_axes", "slice_steps"],
            outputs=[segment_3_name],
            name="SliceSegment3",
        ),
    ]
)

# Concatenate the segments
concat_output_name = f"{sliced_output_name}_concat"
concat_node = helper.make_node(
    "Concat",
    inputs=[segment_1_name, segment_3_name, segment_2_name],
    outputs=[concat_output_name],
    axis=1,
    name="ConcatSwapped",
)
graph.node.append(concat_node)

# Reshape to [1, -1, 6]
reshape_shape = numpy_helper.from_array(np.array([1, -1, 6], dtype=np.int64), name="reshape_shape")
graph.initializer.append(reshape_shape)

final_output_name = f"{concat_output_name}_batched"
reshape_node = helper.make_node(
    "Reshape",
    inputs=[concat_output_name, "reshape_shape"],
    outputs=[final_output_name],
    name="AddBatchDimension",
)
graph.node.append(reshape_node)

# Get the shape of the reshaped tensor
shape_node_name = f"{final_output_name}_shape"
shape_node = helper.make_node(
    "Shape",
    inputs=[final_output_name],
    outputs=[shape_node_name],
    name="GetShapeDim",
)
graph.node.append(shape_node)

# Extract the second dimension
dim_1_index = numpy_helper.from_array(np.array([1], dtype=np.int64), name="dim_1_index")
graph.initializer.append(dim_1_index)

second_dim_name = f"{final_output_name}_dim1"
gather_node = helper.make_node(
    "Gather",
    inputs=[shape_node_name, "dim_1_index"],
    outputs=[second_dim_name],
    name="GatherSecondDim",
)
graph.node.append(gather_node)

# Subtract from 100 to determine how many values to pad
target_size = numpy_helper.from_array(np.array([100], dtype=np.int64), name="target_size")
graph.initializer.append(target_size)

pad_size_name = f"{second_dim_name}_padsize"
sub_node = helper.make_node(
    "Sub",
    inputs=["target_size", second_dim_name],
    outputs=[pad_size_name],
    name="CalculatePadSize",
)
graph.node.append(sub_node)

# Build the [2, 3] pad array:
# 1st row -> [0, 0, 0] (no padding at the start of any dim)
# 2nd row -> [0, pad_size, 0] (pad only at the end of the second dim)
pad_starts = numpy_helper.from_array(np.array([0, 0, 0], dtype=np.int64), name="pad_starts")
graph.initializer.append(pad_starts)

zero_scalar = numpy_helper.from_array(np.array([0], dtype=np.int64), name="zero_scalar")
graph.initializer.append(zero_scalar)

pad_ends_name = "pad_ends"
concat_pad_ends_node = helper.make_node(
    "Concat",
    inputs=["zero_scalar", pad_size_name, "zero_scalar"],
    outputs=[pad_ends_name],
    axis=0,
    name="ConcatPadEnds",
)
graph.node.append(concat_pad_ends_node)

pad_values_name = "pad_values"
concat_pad_node = helper.make_node(
    "Concat",
    inputs=["pad_starts", pad_ends_name],
    outputs=[pad_values_name],
    axis=0,
    name="ConcatPadStartsEnds",
)
graph.node.append(concat_pad_node)

# Create Pad operator to pad with zeros
pad_output_name = f"{final_output_name}_padded"
pad_constant_value = numpy_helper.from_array(
    np.array([0.0], dtype=np.float32),
    name="pad_constant_value",
)
graph.initializer.append(pad_constant_value)

pad_node = helper.make_node(
    "Pad",
    inputs=[final_output_name, pad_values_name, "pad_constant_value"],
    outputs=[pad_output_name],
    mode="constant",
    name="PadToFixedSize",
)
graph.node.append(pad_node)

# Update the graph's final output to [1, 100, 6]
new_output_type = onnx.helper.make_tensor_type_proto(
    elem_type=graph.output[0].type.tensor_type.elem_type, shape=[1, 100, 6]
)
new_output = onnx.helper.make_value_info(name=pad_output_name, type_proto=new_output_type)

# Replace the old output with the new one
graph.output.pop()
graph.output.extend([new_output])

# Save the modified model
onnx.save(model, "yolov7-ultralytics.onnx")
```

Example 4 (python):
```python
from ultralytics import ASSETS, YOLO

model = YOLO("yolov7-ultralytics.onnx", task="detect")

results = model(ASSETS / "bus.jpg")
```

---

## YOLOv7: Trainable Bag-of-Freebies

**URL:** https://docs.ultralytics.com/models/yolov7/

**Contents:**
- YOLOv7: Trainable Bag-of-Freebies
- Comparison of SOTA object detectors
- Overview
- Key Features
- Usage Examples
  - ONNX Export
  - TensorRT Export
- Citations and Acknowledgments
- FAQ
  - What is YOLOv7 and why is it considered a breakthrough in real-time object detection?

YOLOv7, released in July 2022, was a significant advancement in real-time object detection at its time of release. It achieved 56.8% AP on GPU V100, setting new benchmarks when introduced. YOLOv7 outperformed contemporary object detectors such as YOLOR, YOLOX, Scaled-YOLOv4, and YOLOv5 in speed and accuracy. The model is trained on the MS COCO dataset from scratch without using any other datasets or pretrained weights. Source code for YOLOv7 is available on GitHub. Note that newer models like YOLO11 and YOLO26 have since achieved higher accuracy with improved efficiency.

From the results in the YOLO comparison table we know that the proposed method has the best speed-accuracy trade-off comprehensively. If we compare YOLOv7-tiny-SiLU with YOLOv5-N (r6.1), our method is 127 fps faster and 10.7% more accurate on AP. In addition, YOLOv7 has 51.4% AP at frame rate of 161 fps, while PPYOLOE-L with the same AP has only 78 fps frame rate. In terms of parameter usage, YOLOv7 is 41% less than PPYOLOE-L.

If we compare YOLOv7-X with 114 fps inference speed to YOLOv5-L (r6.1) with 99 fps inference speed, YOLOv7-X can improve AP by 3.9%. If YOLOv7-X is compared with YOLOv5-X (r6.1) of similar scale, the inference speed of YOLOv7-X is 31 fps faster. In addition, in terms the amount of parameters and computation, YOLOv7-X reduces 22% of parameters and 8% of computation compared to YOLOv5-X (r6.1), but improves AP by 2.2% (Source).

Real-time object detection is an important component in many computer vision systems, including multi-object tracking, autonomous driving, robotics, and medical image analysis. In recent years, real-time object detection development has focused on designing efficient architectures and improving the inference speed of various CPUs, GPUs, and neural processing units (NPUs). YOLOv7 supports both mobile GPU and GPU devices, from the edge to the cloud.

Unlike traditional real-time object detectors that focus on architecture optimization, YOLOv7 introduces a focus on the optimization of the training process. This includes modules and optimization methods designed to improve the accuracy of object detection without increasing the inference cost, a concept known as the "trainable bag-of-freebies".

YOLOv7 introduces several key features:

Model Re-parameterization: YOLOv7 proposes a planned re-parameterized model, which is a strategy applicable to layers in different networks with the concept of gradient propagation path.

Dynamic Label Assignment: The training of the model with multiple output layers presents a new issue: "How to assign dynamic targets for the outputs of different branches?" To solve this problem, YOLOv7 introduces a new label assignment method called coarse-to-fine lead guided label assignment.

Extended and Compound Scaling: YOLOv7 proposes "extend" and "compound scaling" methods for the real-time object detector that can effectively utilize parameters and computation.

Efficiency: The method proposed by YOLOv7 can effectively reduce about 40% parameters and 50% computation of state-of-the-art real-time object detector, and has faster inference speed and higher detection accuracy.

As of the time of writing, Ultralytics only supports ONNX and TensorRT inference for YOLOv7.

To use YOLOv7 ONNX model with Ultralytics:

(Optional) Install Ultralytics and export an ONNX model to have the required dependencies automatically installed:

Export the desired YOLOv7 model by using the exporter in the YOLOv7 repo:

Modify the ONNX model graph to be compatible with Ultralytics using the following script:

You can then load the modified ONNX model and run inference with it in Ultralytics normally:

Follow steps 1-2 in the ONNX Export section.

Install the TensorRT Python package:

Run the following script to convert the modified ONNX model to TensorRT engine:

Load and run the model in Ultralytics:

We would like to acknowledge the YOLOv7 authors for their significant contributions in the field of real-time object detection:

The original YOLOv7 paper can be found on arXiv. The authors have made their work publicly available, and the codebase can be accessed on GitHub. We appreciate their efforts in advancing the field and making their work accessible to the broader community.

YOLOv7, released in July 2022, was a significant real-time object detection model that achieved excellent speed and accuracy at its time of release. It surpassed contemporary models such as YOLOX, YOLOv5, and PPYOLOE in both parameters usage and inference speed. YOLOv7's distinguishing features include its model re-parameterization and dynamic label assignment, which optimize its performance without increasing inference costs. For more technical details about its architecture and comparison metrics with other state-of-the-art object detectors, refer to the YOLOv7 paper.

YOLOv7 introduces several innovations, including model re-parameterization and dynamic label assignment, which enhance the training process and improve inference accuracy. Compared to YOLOv5, YOLOv7 significantly boosts speed and accuracy. For instance, YOLOv7-X improves accuracy by 2.2% and reduces parameters by 22% compared to YOLOv5-X. Detailed comparisons can be found in the performance table YOLOv7 comparison with SOTA object detectors.

As of now, Ultralytics only supports YOLOv7 ONNX and TensorRT inference. To run the ONNX and TensorRT exported version of YOLOv7 with Ultralytics, check the Usage Examples section.

To install and train a custom YOLOv7 model, follow these steps:

Prepare your dataset and configure the model parameters according to the usage instructions provided in the repository. For further guidance, visit the YOLOv7 GitHub repository for the latest information and updates.

After training, you can export the model to ONNX or TensorRT for use in Ultralytics as shown in Usage Examples.

YOLOv7 offers several key features that revolutionize real-time object detection:

For further details on these features, see the YOLOv7 Overview section.

**Examples:**

Example 1 (unknown):
```unknown
pip install ultralytics
yolo export model=yolo26n.pt format=onnx
```

Example 2 (unknown):
```unknown
git clone https://github.com/WongKinYiu/yolov7
cd yolov7
python export.py --weights yolov7-tiny.pt --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640
```

Example 3 (sql):
```sql
import numpy as np
import onnx
from onnx import helper, numpy_helper

# Load the ONNX model
model_path = "yolov7/yolov7-tiny.onnx"  # Replace with your model path
model = onnx.load(model_path)
graph = model.graph

# Fix input shape to batch size 1
input_shape = graph.input[0].type.tensor_type.shape
input_shape.dim[0].dim_value = 1

# Define the output of the original model
original_output_name = graph.output[0].name

# Create slicing nodes
sliced_output_name = f"{original_output_name}_sliced"

# Define initializers for slicing (remove the first value)
start = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_start")
end = numpy_helper.from_array(np.array([7], dtype=np.int64), name="slice_end")
axes = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_axes")
steps = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_steps")

graph.initializer.extend([start, end, axes, steps])

slice_node = helper.make_node(
    "Slice",
    inputs=[original_output_name, "slice_start", "slice_end", "slice_axes", "slice_steps"],
    outputs=[sliced_output_name],
    name="SliceNode",
)
graph.node.append(slice_node)

# Define segment slicing
seg1_start = numpy_helper.from_array(np.array([0], dtype=np.int64), name="seg1_start")
seg1_end = numpy_helper.from_array(np.array([4], dtype=np.int64), name="seg1_end")
seg2_start = numpy_helper.from_array(np.array([4], dtype=np.int64), name="seg2_start")
seg2_end = numpy_helper.from_array(np.array([5], dtype=np.int64), name="seg2_end")
seg3_start = numpy_helper.from_array(np.array([5], dtype=np.int64), name="seg3_start")
seg3_end = numpy_helper.from_array(np.array([6], dtype=np.int64), name="seg3_end")

graph.initializer.extend([seg1_start, seg1_end, seg2_start, seg2_end, seg3_start, seg3_end])

# Create intermediate tensors for segments
segment_1_name = f"{sliced_output_name}_segment1"
segment_2_name = f"{sliced_output_name}_segment2"
segment_3_name = f"{sliced_output_name}_segment3"

# Add segment slicing nodes
graph.node.extend(
    [
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg1_start", "seg1_end", "slice_axes", "slice_steps"],
            outputs=[segment_1_name],
            name="SliceSegment1",
        ),
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg2_start", "seg2_end", "slice_axes", "slice_steps"],
            outputs=[segment_2_name],
            name="SliceSegment2",
        ),
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg3_start", "seg3_end", "slice_axes", "slice_steps"],
            outputs=[segment_3_name],
            name="SliceSegment3",
        ),
    ]
)

# Concatenate the segments
concat_output_name = f"{sliced_output_name}_concat"
concat_node = helper.make_node(
    "Concat",
    inputs=[segment_1_name, segment_3_name, segment_2_name],
    outputs=[concat_output_name],
    axis=1,
    name="ConcatSwapped",
)
graph.node.append(concat_node)

# Reshape to [1, -1, 6]
reshape_shape = numpy_helper.from_array(np.array([1, -1, 6], dtype=np.int64), name="reshape_shape")
graph.initializer.append(reshape_shape)

final_output_name = f"{concat_output_name}_batched"
reshape_node = helper.make_node(
    "Reshape",
    inputs=[concat_output_name, "reshape_shape"],
    outputs=[final_output_name],
    name="AddBatchDimension",
)
graph.node.append(reshape_node)

# Get the shape of the reshaped tensor
shape_node_name = f"{final_output_name}_shape"
shape_node = helper.make_node(
    "Shape",
    inputs=[final_output_name],
    outputs=[shape_node_name],
    name="GetShapeDim",
)
graph.node.append(shape_node)

# Extract the second dimension
dim_1_index = numpy_helper.from_array(np.array([1], dtype=np.int64), name="dim_1_index")
graph.initializer.append(dim_1_index)

second_dim_name = f"{final_output_name}_dim1"
gather_node = helper.make_node(
    "Gather",
    inputs=[shape_node_name, "dim_1_index"],
    outputs=[second_dim_name],
    name="GatherSecondDim",
)
graph.node.append(gather_node)

# Subtract from 100 to determine how many values to pad
target_size = numpy_helper.from_array(np.array([100], dtype=np.int64), name="target_size")
graph.initializer.append(target_size)

pad_size_name = f"{second_dim_name}_padsize"
sub_node = helper.make_node(
    "Sub",
    inputs=["target_size", second_dim_name],
    outputs=[pad_size_name],
    name="CalculatePadSize",
)
graph.node.append(sub_node)

# Build the [2, 3] pad array:
# 1st row -> [0, 0, 0] (no padding at the start of any dim)
# 2nd row -> [0, pad_size, 0] (pad only at the end of the second dim)
pad_starts = numpy_helper.from_array(np.array([0, 0, 0], dtype=np.int64), name="pad_starts")
graph.initializer.append(pad_starts)

zero_scalar = numpy_helper.from_array(np.array([0], dtype=np.int64), name="zero_scalar")
graph.initializer.append(zero_scalar)

pad_ends_name = "pad_ends"
concat_pad_ends_node = helper.make_node(
    "Concat",
    inputs=["zero_scalar", pad_size_name, "zero_scalar"],
    outputs=[pad_ends_name],
    axis=0,
    name="ConcatPadEnds",
)
graph.node.append(concat_pad_ends_node)

pad_values_name = "pad_values"
concat_pad_node = helper.make_node(
    "Concat",
    inputs=["pad_starts", pad_ends_name],
    outputs=[pad_values_name],
    axis=0,
    name="ConcatPadStartsEnds",
)
graph.node.append(concat_pad_node)

# Create Pad operator to pad with zeros
pad_output_name = f"{final_output_name}_padded"
pad_constant_value = numpy_helper.from_array(
    np.array([0.0], dtype=np.float32),
    name="pad_constant_value",
)
graph.initializer.append(pad_constant_value)

pad_node = helper.make_node(
    "Pad",
    inputs=[final_output_name, pad_values_name, "pad_constant_value"],
    outputs=[pad_output_name],
    mode="constant",
    name="PadToFixedSize",
)
graph.node.append(pad_node)

# Update the graph's final output to [1, 100, 6]
new_output_type = onnx.helper.make_tensor_type_proto(
    elem_type=graph.output[0].type.tensor_type.elem_type, shape=[1, 100, 6]
)
new_output = onnx.helper.make_value_info(name=pad_output_name, type_proto=new_output_type)

# Replace the old output with the new one
graph.output.pop()
graph.output.extend([new_output])

# Save the modified model
onnx.save(model, "yolov7-ultralytics.onnx")
```

Example 4 (python):
```python
from ultralytics import ASSETS, YOLO

model = YOLO("yolov7-ultralytics.onnx", task="detect")

results = model(ASSETS / "bus.jpg")
```

---

## YOLOv7: مجموعة الأدوات المجانية القابلة للتدريب

**URL:** https://docs.ultralytics.com/ar/models/yolov7/

**Contents:**
- YOLOv7: مجموعة الأدوات المجانية القابلة للتدريب
- مقارنة بين أحدث أدوات الكشف عن الأجسام (SOTA)
- نظرة عامة
- الميزات الرئيسية
- أمثلة الاستخدام
  - تصدير ONNX
  - تصدير TensorRT
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هو YOLOv7 ولماذا يعتبر طفرة في الوقت الحقيقي لاكتشاف الأجسام؟

كان YOLOv7، الذي صدر في يوليو 2022، تقدمًا كبيرًا في الكشف عن الكائنات في الوقت الفعلي وقت إصداره. حقق 56.8% AP على GPU V100، مسجلاً معايير جديدة عند تقديمه. تفوق YOLOv7 على كاشفات الكائنات المعاصرة مثل YOLOR و YOLOX و Scaled-YOLOv4 و YOLOv5 في السرعة والدقة. تم تدريب النموذج على مجموعة بيانات MS COCO من الصفر دون استخدام أي مجموعات بيانات أخرى أو أوزان مدربة مسبقًا. يتوفر الكود المصدري لـ YOLOv7 على GitHub. لاحظ أن النماذج الأحدث مثل YOLO11 و YOLO26 قد حققت منذ ذلك الحين دقة أعلى بكفاءة محسّنة.

من النتائج الموجودة في جدول مقارنة YOLO، نعلم أن الطريقة المقترحة لديها أفضل مقايضة بين السرعة والدقة بشكل شامل. إذا قارنا YOLOv7-tiny-SiLU مع YOLOv5-N (r6.1)، فإن طريقتنا أسرع بمقدار 127 إطارًا في الثانية وأكثر دقة بنسبة 10.7٪ في AP. بالإضافة إلى ذلك، فإن YOLOv7 لديها 51.4٪ AP بمعدل إطارات 161 إطارًا في الثانية، في حين أن PPYOLOE-L بنفس AP لديها معدل إطارات 78 إطارًا في الثانية فقط. من حيث استخدام المعلمات، فإن YOLOv7 أقل بنسبة 41٪ من PPYOLOE-L.

إذا قارنا YOLOv7-X بسرعة استدلال 114 إطارًا في الثانية مع YOLOv5-L (r6.1) بسرعة استدلال 99 إطارًا في الثانية، فيمكن لـ YOLOv7-X تحسين AP بنسبة 3.9%. إذا تمت مقارنة YOLOv7-X مع YOLOv5-X (r6.1) ذي المقياس المماثل، فإن سرعة استدلال YOLOv7-X أسرع بمقدار 31 إطارًا في الثانية. بالإضافة إلى ذلك، فيما يتعلق بكمية المعلمات والحساب، يقلل YOLOv7-X من 22% من المعلمات و 8% من الحساب مقارنة بـ YOLOv5-X (r6.1)، ولكنه يحسن AP بنسبة 2.2% (المصدر).

يعد الكشف عن الكائنات في الوقت الفعلي مكونًا مهمًا في العديد من أنظمة رؤية الكمبيوتر، بما في ذلك تتبع متعدد الكائنات، والقيادة الذاتية، والروبوتات، وتحليل الصور الطبية. في السنوات الأخيرة، ركز تطوير الكشف عن الكائنات في الوقت الفعلي على تصميم معماريات فعالة وتحسين سرعة الاستدلال لوحدات المعالجة المركزية ووحدات معالجة الرسومات ووحدات المعالجة العصبية المختلفة (NPUs). يدعم YOLOv7 كلاً من أجهزة GPU المحمولة وأجهزة GPU، من الحافة إلى السحابة.

بخلاف كاشفات الكائنات في الوقت الفعلي التقليدية التي تركز على تحسين الهندسة المعمارية، يقدم YOLOv7 تركيزًا على تحسين عملية التدريب. يتضمن ذلك وحدات وأساليب تحسين مصممة لتحسين دقة اكتشاف الكائنات دون زيادة تكلفة الاستدلال، وهو مفهوم يعرف باسم "حقيبة الحيل المجانية القابلة للتدريب".

يقدم YOLOv7 العديد من الميزات الرئيسية:

إعادة تحديد معلمات النموذج: يقترح YOLOv7 نموذجًا مُعاد تحديده مُخطط له، وهي إستراتيجية قابلة للتطبيق على الطبقات في الشبكات المختلفة مع مفهوم مسار انتشار التدرج.

تعيين تسمية ديناميكية: يطرح تدريب النموذج بطبقات إخراج متعددة مشكلة جديدة: "كيفية تعيين أهداف ديناميكية لمخرجات الفروع المختلفة؟" لحل هذه المشكلة، يقدم YOLOv7 طريقة جديدة لتعيين التسميات تسمى تعيين التسميات الموجه من الخشن إلى الدقيق.

التحجيم الممتد والمركب: تقترح YOLOv7 طرق "التحجيم الممتد" و"التحجيم المركب" لكاشف الكائنات في الوقت الفعلي الذي يمكنه استخدام المعلمات والحساب بشكل فعال.

الكفاءة: يمكن للطريقة التي اقترحها YOLOv7 أن تقلل بشكل فعال حوالي 40٪ من المعلمات و 50٪ من حسابات أحدث أجهزة الكشف عن الكائنات في الوقت الفعلي، ولديها سرعة استدلال أسرع ودقة detect أعلى.

حتى وقت كتابة هذه السطور، تدعم Ultralytics استدلال ONNX و TensorRT فقط لـ YOLOv7.

لاستخدام نموذج YOLOv7 ONNX مع Ultralytics:

(اختياري) قم بتثبيت Ultralytics وتصدير نموذج ONNX لتثبيت التبعيات المطلوبة تلقائيًا:

قم بتصدير نموذج YOLOv7 المطلوب باستخدام المصدر في مستودع YOLOv7:

قم بتعديل مخطط نموذج ONNX ليكون متوافقًا مع Ultralytics باستخدام البرنامج النصي التالي:

يمكنك بعد ذلك تحميل نموذج ONNX المعدل وتشغيل الاستدلال به في Ultralytics بشكل طبيعي:

اتبع الخطوتين 1-2 في قسم تصدير ONNX.

قم بتثبيت TensorRT حزمة Python:

شغّل البرنامج النصي التالي لتحويل نموذج ONNX المعدل إلى محرك TensorRT:

قم بتحميل وتشغيل النموذج في Ultralytics:

نود أن نتقدم بالشكر لمؤلفي YOLOv7 لمساهماتهم الكبيرة في مجال الكشف عن الأجسام في الوقت الفعلي:

يمكن العثور على ورقة YOLOv7 الأصلية على arXiv. لقد أتاح المؤلفون عملهم للجمهور، ويمكن الوصول إلى قاعدة التعليمات البرمجية على GitHub. نحن نقدر جهودهم في تطوير هذا المجال وإتاحة عملهم للمجتمع الأوسع.

كان YOLOv7، الذي صدر في يوليو 2022، نموذجًا مهمًا للكشف عن الكائنات في الوقت الفعلي حقق سرعة ودقة ممتازة وقت إصداره. لقد تفوق على النماذج المعاصرة مثل YOLOX و YOLOv5 و PPYOLOE في كل من استخدام المعلمات وسرعة الاستدلال. تشمل الميزات المميزة لـ YOLOv7 إعادة تحديد معلمات النموذج وتعيين التسميات الديناميكي، مما يحسن أداءه دون زيادة تكاليف الاستدلال. لمزيد من التفاصيل التقنية حول بنيته ومقاييس المقارنة مع كاشفات الكائنات الأخرى المتطورة، ارجع إلى ورقة YOLOv7.

يقدم YOLOv7 العديد من الابتكارات، بما في ذلك إعادة تحديد معلمات النموذج وتعيين التسميات الديناميكي، مما يعزز عملية التدريب ويحسن دقة الاستدلال. بالمقارنة مع YOLOv5، يعزز YOLOv7 السرعة والدقة بشكل كبير. على سبيل المثال، يحسن YOLOv7-X الدقة بنسبة 2.2٪ ويقلل المعلمات بنسبة 22٪ مقارنة بـ YOLOv5-X. يمكن العثور على مقارنات تفصيلية في جدول الأداء مقارنة YOLOv7 بكاشفات الكائنات SOTA.

حتى الآن، تدعم Ultralytics استدلال YOLOv7 ONNX و TensorRT فقط. لتشغيل إصدار YOLOv7 المُصدَّر بتنسيق ONNX و TensorRT باستخدام Ultralytics، تحقق من قسم أمثلة الاستخدام.

لتثبيت وتدريب نموذج YOLOv7 مخصص، اتبع الخطوات التالية:

قم بإعداد مجموعة البيانات الخاصة بك وتهيئة معلمات النموذج وفقًا لـ تعليمات الاستخدام المتوفرة في المستودع. لمزيد من الإرشادات، تفضل بزيارة مستودع YOLOv7 GitHub للحصول على أحدث المعلومات والتحديثات.

بعد التدريب، يمكنك تصدير النموذج إلى ONNX أو TensorRT لاستخدامه في Ultralytics كما هو موضح في أمثلة الاستخدام.

يقدم YOLOv7 العديد من الميزات الرئيسية التي تحدث ثورة في الكشف عن الأجسام في الوقت الفعلي:

لمزيد من التفاصيل حول هذه الميزات، راجع قسم نظرة عامة على YOLOv7.

**Examples:**

Example 1 (unknown):
```unknown
pip install ultralytics
yolo export model=yolo26n.pt format=onnx
```

Example 2 (unknown):
```unknown
git clone https://github.com/WongKinYiu/yolov7
cd yolov7
python export.py --weights yolov7-tiny.pt --grid --end2end --simplify --topk-all 100 --iou-thres 0.65 --conf-thres 0.35 --img-size 640 640 --max-wh 640
```

Example 3 (sql):
```sql
import numpy as np
import onnx
from onnx import helper, numpy_helper

# Load the ONNX model
model_path = "yolov7/yolov7-tiny.onnx"  # Replace with your model path
model = onnx.load(model_path)
graph = model.graph

# Fix input shape to batch size 1
input_shape = graph.input[0].type.tensor_type.shape
input_shape.dim[0].dim_value = 1

# Define the output of the original model
original_output_name = graph.output[0].name

# Create slicing nodes
sliced_output_name = f"{original_output_name}_sliced"

# Define initializers for slicing (remove the first value)
start = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_start")
end = numpy_helper.from_array(np.array([7], dtype=np.int64), name="slice_end")
axes = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_axes")
steps = numpy_helper.from_array(np.array([1], dtype=np.int64), name="slice_steps")

graph.initializer.extend([start, end, axes, steps])

slice_node = helper.make_node(
    "Slice",
    inputs=[original_output_name, "slice_start", "slice_end", "slice_axes", "slice_steps"],
    outputs=[sliced_output_name],
    name="SliceNode",
)
graph.node.append(slice_node)

# Define segment slicing
seg1_start = numpy_helper.from_array(np.array([0], dtype=np.int64), name="seg1_start")
seg1_end = numpy_helper.from_array(np.array([4], dtype=np.int64), name="seg1_end")
seg2_start = numpy_helper.from_array(np.array([4], dtype=np.int64), name="seg2_start")
seg2_end = numpy_helper.from_array(np.array([5], dtype=np.int64), name="seg2_end")
seg3_start = numpy_helper.from_array(np.array([5], dtype=np.int64), name="seg3_start")
seg3_end = numpy_helper.from_array(np.array([6], dtype=np.int64), name="seg3_end")

graph.initializer.extend([seg1_start, seg1_end, seg2_start, seg2_end, seg3_start, seg3_end])

# Create intermediate tensors for segments
segment_1_name = f"{sliced_output_name}_segment1"
segment_2_name = f"{sliced_output_name}_segment2"
segment_3_name = f"{sliced_output_name}_segment3"

# Add segment slicing nodes
graph.node.extend(
    [
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg1_start", "seg1_end", "slice_axes", "slice_steps"],
            outputs=[segment_1_name],
            name="SliceSegment1",
        ),
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg2_start", "seg2_end", "slice_axes", "slice_steps"],
            outputs=[segment_2_name],
            name="SliceSegment2",
        ),
        helper.make_node(
            "Slice",
            inputs=[sliced_output_name, "seg3_start", "seg3_end", "slice_axes", "slice_steps"],
            outputs=[segment_3_name],
            name="SliceSegment3",
        ),
    ]
)

# Concatenate the segments
concat_output_name = f"{sliced_output_name}_concat"
concat_node = helper.make_node(
    "Concat",
    inputs=[segment_1_name, segment_3_name, segment_2_name],
    outputs=[concat_output_name],
    axis=1,
    name="ConcatSwapped",
)
graph.node.append(concat_node)

# Reshape to [1, -1, 6]
reshape_shape = numpy_helper.from_array(np.array([1, -1, 6], dtype=np.int64), name="reshape_shape")
graph.initializer.append(reshape_shape)

final_output_name = f"{concat_output_name}_batched"
reshape_node = helper.make_node(
    "Reshape",
    inputs=[concat_output_name, "reshape_shape"],
    outputs=[final_output_name],
    name="AddBatchDimension",
)
graph.node.append(reshape_node)

# Get the shape of the reshaped tensor
shape_node_name = f"{final_output_name}_shape"
shape_node = helper.make_node(
    "Shape",
    inputs=[final_output_name],
    outputs=[shape_node_name],
    name="GetShapeDim",
)
graph.node.append(shape_node)

# Extract the second dimension
dim_1_index = numpy_helper.from_array(np.array([1], dtype=np.int64), name="dim_1_index")
graph.initializer.append(dim_1_index)

second_dim_name = f"{final_output_name}_dim1"
gather_node = helper.make_node(
    "Gather",
    inputs=[shape_node_name, "dim_1_index"],
    outputs=[second_dim_name],
    name="GatherSecondDim",
)
graph.node.append(gather_node)

# Subtract from 100 to determine how many values to pad
target_size = numpy_helper.from_array(np.array([100], dtype=np.int64), name="target_size")
graph.initializer.append(target_size)

pad_size_name = f"{second_dim_name}_padsize"
sub_node = helper.make_node(
    "Sub",
    inputs=["target_size", second_dim_name],
    outputs=[pad_size_name],
    name="CalculatePadSize",
)
graph.node.append(sub_node)

# Build the [2, 3] pad array:
# 1st row -> [0, 0, 0] (no padding at the start of any dim)
# 2nd row -> [0, pad_size, 0] (pad only at the end of the second dim)
pad_starts = numpy_helper.from_array(np.array([0, 0, 0], dtype=np.int64), name="pad_starts")
graph.initializer.append(pad_starts)

zero_scalar = numpy_helper.from_array(np.array([0], dtype=np.int64), name="zero_scalar")
graph.initializer.append(zero_scalar)

pad_ends_name = "pad_ends"
concat_pad_ends_node = helper.make_node(
    "Concat",
    inputs=["zero_scalar", pad_size_name, "zero_scalar"],
    outputs=[pad_ends_name],
    axis=0,
    name="ConcatPadEnds",
)
graph.node.append(concat_pad_ends_node)

pad_values_name = "pad_values"
concat_pad_node = helper.make_node(
    "Concat",
    inputs=["pad_starts", pad_ends_name],
    outputs=[pad_values_name],
    axis=0,
    name="ConcatPadStartsEnds",
)
graph.node.append(concat_pad_node)

# Create Pad operator to pad with zeros
pad_output_name = f"{final_output_name}_padded"
pad_constant_value = numpy_helper.from_array(
    np.array([0.0], dtype=np.float32),
    name="pad_constant_value",
)
graph.initializer.append(pad_constant_value)

pad_node = helper.make_node(
    "Pad",
    inputs=[final_output_name, pad_values_name, "pad_constant_value"],
    outputs=[pad_output_name],
    mode="constant",
    name="PadToFixedSize",
)
graph.node.append(pad_node)

# Update the graph's final output to [1, 100, 6]
new_output_type = onnx.helper.make_tensor_type_proto(
    elem_type=graph.output[0].type.tensor_type.elem_type, shape=[1, 100, 6]
)
new_output = onnx.helper.make_value_info(name=pad_output_name, type_proto=new_output_type)

# Replace the old output with the new one
graph.output.pop()
graph.output.extend([new_output])

# Save the modified model
onnx.save(model, "yolov7-ultralytics.onnx")
```

Example 4 (python):
```python
from ultralytics import ASSETS, YOLO

model = YOLO("yolov7-ultralytics.onnx", task="detect")

results = model(ASSETS / "bus.jpg")
```

---

## YOLOv9: A Leap Forward in Object Detection Technology

**URL:** https://docs.ultralytics.com/models/yolov9/

**Contents:**
- YOLOv9: A Leap Forward in Object Detection Technology
- Introduction to YOLOv9
- Core Innovations of YOLOv9
  - Information Bottleneck Principle
  - Reversible Functions
  - Impact on Lightweight Models
  - Programmable Gradient Information (PGI)
  - Generalized Efficient Layer Aggregation Network (GELAN)
- YOLOv9 Benchmarks
- Performance on MS COCO Dataset

YOLOv9 marks a significant advancement in real-time object detection, introducing groundbreaking techniques such as Programmable Gradient Information (PGI) and the Generalized Efficient Layer Aggregation Network (GELAN). This model demonstrates remarkable improvements in efficiency, accuracy, and adaptability, setting new benchmarks on the MS COCO dataset. The YOLOv9 project, while developed by a separate open-source team, builds upon the robust codebase provided by UltralyticsYOLOv5, showcasing the collaborative spirit of the AI research community.

Watch: YOLOv9 Training on Custom Data using Ultralytics | Industrial Package Dataset

In the quest for optimal real-time object detection, YOLOv9 stands out with its innovative approach to overcoming information loss challenges inherent in deep neural networks. By integrating PGI and the versatile GELAN architecture, YOLOv9 not only enhances the model's learning capacity but also ensures the retention of crucial information throughout the detection process, thereby achieving exceptional accuracy and performance.

YOLOv9's advancements are deeply rooted in addressing the challenges posed by information loss in deep neural networks. The Information Bottleneck Principle and the innovative use of Reversible Functions are central to its design, ensuring YOLOv9 maintains high efficiency and accuracy.

The Information Bottleneck Principle reveals a fundamental challenge in deep learning: as data passes through successive layers of a network, the potential for information loss increases. This phenomenon is mathematically represented as:

where I denotes mutual information, and f and g represent transformation functions with parameters theta and phi, respectively. YOLOv9 counters this challenge by implementing Programmable Gradient Information (PGI), which aids in preserving essential data across the network's depth, ensuring more reliable gradient generation and, consequently, better model convergence and performance.

The concept of Reversible Functions is another cornerstone of YOLOv9's design. A function is deemed reversible if it can be inverted without any loss of information, as expressed by:

with psi and zeta as parameters for the reversible and its inverse function, respectively. This property is crucial for deep learning architectures, as it allows the network to retain a complete information flow, thereby enabling more accurate updates to the model's parameters. YOLOv9 incorporates reversible functions within its architecture to mitigate the risk of information degradation, especially in deeper layers, ensuring the preservation of critical data for object detection tasks.

Addressing information loss is particularly vital for lightweight models, which are often under-parameterized and prone to losing significant information during the feedforward process. YOLOv9's architecture, through the use of PGI and reversible functions, ensures that even with a streamlined model, the essential information required for accurate object detection is retained and effectively utilized.

PGI is a novel concept introduced in YOLOv9 to combat the information bottleneck problem, ensuring the preservation of essential data across deep network layers. This allows for the generation of reliable gradients, facilitating accurate model updates and improving the overall detection performance.

GELAN represents a strategic architectural advancement, enabling YOLOv9 to achieve superior parameter utilization and computational efficiency. Its design allows for flexible integration of various computational blocks, making YOLOv9 adaptable to a wide range of applications without sacrificing speed or accuracy.

Benchmarking in YOLOv9 using Ultralytics involves evaluating the performance of your trained and validated model in real-world scenarios. This process includes:

By benchmarking, you can ensure that your model not only performs well in controlled testing environments but also maintains high performance in practical, real-world applications.

Watch: How to Benchmark the YOLOv9 Model Using the Ultralytics Python Package

The performance of YOLOv9 on the COCO dataset exemplifies its significant advancements in real-time object detection, setting new benchmarks across various model sizes. Table 1 presents a comprehensive comparison of state-of-the-art real-time object detectors, illustrating YOLOv9's superior efficiency and accuracy.

YOLOv9's iterations, ranging from the tiny t variant to the extensive e model, demonstrate improvements not only in accuracy (mAP metrics) but also in efficiency with a reduced number of parameters and computational needs (FLOPs). This table underscores YOLOv9's ability to deliver high precision while maintaining or reducing the computational overhead compared to prior versions and competing models.

Comparatively, YOLOv9 exhibits remarkable gains:

The YOLOv9c model, in particular, highlights the effectiveness of the architecture's optimizations. It operates with 42% fewer parameters and 21% less computational demand than YOLOv7 AF, yet it achieves comparable accuracy, demonstrating YOLOv9's significant efficiency improvements. Furthermore, the YOLOv9e model sets a new standard for large models, with 15% fewer parameters and 25% less computational need than YOLOv8x, alongside an incremental 1.7% improvement in AP.

These results showcase YOLOv9's strategic advancements in model design, emphasizing its enhanced efficiency without compromising on the precision essential for real-time object detection tasks. The model not only pushes the boundaries of performance metrics but also emphasizes the importance of computational efficiency, making it a pivotal development in the field of computer vision.

YOLOv9, released in February 2024, represented a pivotal development in real-time object detection, offering significant improvements in terms of efficiency, accuracy, and adaptability. By addressing critical challenges through innovative solutions like PGI and GELAN, YOLOv9 set new benchmarks at its time of release. While newer models like YOLO11 and YOLO26 have since been released with additional improvements, YOLOv9's architectural innovations continue to influence the field.

This example provides simple YOLOv9 training and inference examples. For full documentation on these and other modes see the Predict, Train, Val and Export docs pages.

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLO() class to create a model instance in python:

CLI commands are available to directly run the models:

The YOLOv9 series offers a range of models, each optimized for high-performance Object Detection. These models cater to varying computational needs and accuracy requirements, making them versatile for a wide array of applications.

This table provides a detailed overview of the YOLOv9 model variants, highlighting their capabilities in object detection tasks and their compatibility with various operational modes such as Inference, Validation, Training, and Export. This comprehensive support ensures that users can fully leverage the capabilities of YOLOv9 models in a broad range of object detection scenarios.

Training YOLOv9 models will require more resources and take longer than the equivalent sized YOLOv8 model.

We would like to acknowledge the YOLOv9 authors for their significant contributions in the field of real-time object detection:

The original YOLOv9 paper can be found on arXiv. The authors have made their work publicly available, and the codebase can be accessed on GitHub. We appreciate their efforts in advancing the field and making their work accessible to the broader community.

YOLOv9 introduces groundbreaking techniques such as Programmable Gradient Information (PGI) and the Generalized Efficient Layer Aggregation Network (GELAN). These innovations address information loss challenges in deep neural networks, ensuring high efficiency, accuracy, and adaptability. PGI preserves essential data across network layers, while GELAN optimizes parameter utilization and computational efficiency. Learn more about YOLOv9's core innovations that set new benchmarks on the MS COCO dataset.

YOLOv9 outperforms state-of-the-art real-time object detectors by achieving higher accuracy and efficiency. On the COCO dataset, YOLOv9 models exhibit superior mAP scores across various sizes while maintaining or reducing computational overhead. For instance, YOLOv9c achieves comparable accuracy with 42% fewer parameters and 21% less computational demand than YOLOv7 AF. Explore performance comparisons for detailed metrics.

You can train a YOLOv9 model using both Python and CLI commands. For Python, instantiate a model using the YOLO class and call the train method:

For CLI training, execute:

Learn more about usage examples for training and inference.

YOLOv9 is designed to mitigate information loss, which is particularly important for lightweight models often prone to losing significant information. By integrating Programmable Gradient Information (PGI) and reversible functions, YOLOv9 ensures essential data retention, enhancing the model's accuracy and efficiency. This makes it highly suitable for applications requiring compact models with high performance. For more details, explore the section on YOLOv9's impact on lightweight models.

YOLOv9 supports various tasks including object detection and instance segmentation. It is compatible with multiple operational modes such as inference, validation, training, and export. This versatility makes YOLOv9 adaptable to diverse real-time computer vision applications. Refer to the supported tasks and modes section for more information.

**Examples:**

Example 1 (unknown):
```unknown
I(X, X) >= I(X, f_theta(X)) >= I(X, g_phi(f_theta(X)))
```

Example 2 (unknown):
```unknown
X = v_zeta(r_psi(X))
```

Example 3 (python):
```python
from ultralytics import YOLO

# Build a YOLOv9c model from scratch
model = YOLO("yolov9c.yaml")

# Build a YOLOv9c model from pretrained weight
model = YOLO("yolov9c.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv9c model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 4 (sql):
```sql
# Build a YOLOv9c model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov9c.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv9c model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov9c.yaml source=path/to/bus.jpg
```

---

## YOLOv9: Un balzo in avanti nella tecnologia di Object Detection

**URL:** https://docs.ultralytics.com/it/models/yolov9/

**Contents:**
- YOLOv9: Un balzo in avanti nella tecnologia di Object Detection
- Introduzione a YOLOv9
- Innovazioni Core di YOLOv9
  - Principio del collo di bottiglia dell'informazione
  - Funzioni reversibili
  - Impatto sui modelli leggeri
  - Informazioni sul gradiente programmabile (PGI)
  - Rete di aggregazione di livelli efficienti generalizzata (GELAN)
- Benchmark di YOLOv9
- Performance sul dataset MS COCO

YOLOv9 segna un significativo passo avanti nel rilevamento di oggetti in tempo reale, introducendo tecniche innovative come le Informazioni sul Gradiente Programmabile (PGI) e la Generalized Efficient Layer Aggregation Network (GELAN). Questo modello dimostra notevoli miglioramenti in termini di efficienza, accuratezza e adattabilità, stabilendo nuovi standard di riferimento sul dataset MS COCO. Il progetto YOLOv9, pur essendo sviluppato da un team open-source separato, si basa sulla solida codebase fornita da UltralyticsYOLOv5, dimostrando lo spirito collaborativo della comunità di ricerca sull'IA.

Guarda: Addestramento di YOLOv9 su dati personalizzati utilizzando Ultralytics | Dataset Industrial Package

Nella ricerca dell'object detection in tempo reale ottimale, YOLOv9 si distingue per il suo approccio innovativo per superare le sfide di perdita di informazioni inerenti alle reti neurali profonde. Integrando PGI e la versatile architettura GELAN, YOLOv9 non solo migliora la capacità di apprendimento del modello, ma garantisce anche la conservazione di informazioni cruciali durante il processo di detection, ottenendo così precisione e prestazioni eccezionali.

I progressi di YOLOv9 sono profondamente radicati nell'affrontare le sfide poste dalla perdita di informazioni nelle reti neurali profonde. Il principio dell'Information Bottleneck e l'uso innovativo delle Reversible Functions sono fondamentali per la sua progettazione, garantendo che YOLOv9 mantenga alta efficienza e accuratezza.

L'Information Bottleneck Principle rivela una sfida fondamentale nell'apprendimento profondo: man mano che i dati passano attraverso i livelli successivi di una rete, il potenziale di perdita di informazioni aumenta. Questo fenomeno è rappresentato matematicamente come:

dove I indica l'informazione reciproca, e f e g rappresentano le funzioni di trasformazione con parametri theta e phi, rispettivamente. YOLOv9 contrasta questa problematica implementando il Programmable Gradient Information (PGI), che aiuta a preservare i dati essenziali attraverso la profondità della rete, garantendo una generazione di gradienti più affidabile e, di conseguenza, una migliore convergenza e performance del modello.

Il concetto di Funzioni Reversibili è un'altra pietra angolare del design di YOLOv9. Una funzione è considerata reversibile se può essere invertita senza alcuna perdita di informazioni, come espresso da:

con psi e zeta come parametri rispettivamente per la funzione reversibile e la sua inversa. Questa proprietà è fondamentale per il deep learning architetture, poiché consente alla rete di mantenere un flusso di informazioni completo, consentendo in tal modo aggiornamenti più accurati ai parametri del modello. YOLOv9 incorpora funzioni reversibili all'interno della sua architettura per mitigare il rischio di degrado delle informazioni, specialmente negli strati più profondi, garantendo la conservazione dei dati critici per le attività di object detection.

Affrontare la perdita di informazioni è particolarmente importante per i modelli leggeri, che sono spesso sotto-parametrizzati e inclini a perdere informazioni significative durante il processo di feedforward. L'architettura di YOLOv9, attraverso l'uso di PGI e funzioni reversibili, garantisce che anche con un modello semplificato, le informazioni essenziali necessarie per un detect accurato degli oggetti vengano conservate e utilizzate efficacemente.

PGI è un concetto innovativo introdotto in YOLOv9 per combattere il problema del collo di bottiglia delle informazioni, garantendo la conservazione dei dati essenziali attraverso i livelli della rete neurale profonda. Ciò consente la generazione di gradienti affidabili, facilitando aggiornamenti accurati del modello e migliorando le prestazioni complessive di detect.

GELAN rappresenta un progresso architettonico strategico, che consente a YOLOv9 di ottenere un utilizzo dei parametri e un'efficienza computazionale superiori. Il suo design consente un'integrazione flessibile di vari blocchi computazionali, rendendo YOLOv9 adattabile a un'ampia gamma di applicazioni senza sacrificare velocità o accuratezza.

Il benchmarking in YOLOv9 utilizzando Ultralytics implica la valutazione delle prestazioni del modello addestrato e convalidato in scenari reali. Questo processo include:

Attraverso il benchmarking, puoi assicurarti che il tuo modello non solo funzioni bene in ambienti di test controllati, ma mantenga anche alte prestazioni in applicazioni pratiche del mondo reale.

Guarda: Come effettuare il benchmark del modello YOLOv9 utilizzando il pacchetto Ultralytics python

Le prestazioni di YOLOv9 sul dataset COCO esemplificano i suoi significativi progressi nel rilevamento di oggetti in tempo reale, stabilendo nuovi benchmark in varie dimensioni di modelli. La Tabella 1 presenta un confronto completo dei rilevatori di oggetti in tempo reale all'avanguardia, illustrando l'efficienza superiore e l'accuratezza di YOLOv9.

Le iterazioni di YOLOv9, che vanno dalla tiny t variante tiny a quella estesa e model, dimostrano miglioramenti non solo in termini di accuratezza (metriche mAP) ma anche di efficienza con un numero ridotto di parametri ed esigenze computazionali (FLOP). Questa tabella sottolinea la capacità di YOLOv9 di fornire prestazioni elevate precisione mantenendo o riducendo il sovraccarico computazionale rispetto alle versioni precedenti e ai modelli concorrenti.

Comparativamente, YOLOv9 mostra notevoli guadagni:

Il modello YOLOv9c, in particolare, evidenzia l'efficacia delle ottimizzazioni dell'architettura. Opera con il 42% in meno di parametri e il 21% in meno di domanda computazionale rispetto a YOLOv7 AF, eppure raggiunge un'accuratezza comparabile, dimostrando i significativi miglioramenti di efficienza di YOLOv9. Inoltre, il modello YOLOv9e stabilisce un nuovo standard per i modelli di grandi dimensioni, con il 15% in meno di parametri e il 25% in meno di necessità computazionale rispetto a YOLOv8x, insieme a un miglioramento incrementale dell'1,7% in AP.

Questi risultati dimostrano i progressi strategici di YOLOv9 nella progettazione del modello, sottolineando la sua maggiore efficienza senza compromettere la precisione essenziale per le attività di object detection in tempo reale. Il modello non solo spinge i confini delle metriche di performance, ma sottolinea anche l'importanza dell'efficienza computazionale, rendendolo uno sviluppo fondamentale nel campo della computer vision.

YOLOv9, rilasciato a febbraio 2024, ha rappresentato uno sviluppo cruciale nel rilevamento di oggetti in tempo reale, offrendo miglioramenti significativi in termini di efficienza, precisione e adattabilità. Affrontando sfide critiche attraverso soluzioni innovative come PGI e GELAN, YOLOv9 ha stabilito nuovi parametri di riferimento al momento del suo rilascio. Sebbene modelli più recenti come YOLO11 e YOLO26 siano stati successivamente rilasciati con ulteriori miglioramenti, le innovazioni architettoniche di YOLOv9 continuano a influenzare il settore.

Questo esempio fornisce semplici esempi di addestramento e inferenza di YOLOv9. Per la documentazione completa su queste e altre modalità, consultare le pagine di documentazione Predict, Train, Val ed Export.

PyTorch pre-addestrato *.pt modelli, così come la configurazione *.yaml file possono essere passati alla YOLO() classe per creare un'istanza del modello in python:

Sono disponibili comandi CLI per eseguire direttamente i modelli:

La serie YOLOv9 offre una gamma di modelli, ciascuno ottimizzato per Object Detection ad alte prestazioni. Questi modelli soddisfano diverse esigenze computazionali e requisiti di accuratezza, rendendoli versatili per una vasta gamma di applicazioni.

Questa tabella fornisce una panoramica dettagliata delle varianti del modello YOLOv9, evidenziandone le capacità nelle attività di object detection e la loro compatibilità con varie modalità operative come Inference, Validation, Training ed Export. Questo supporto completo garantisce che gli utenti possano sfruttare appieno le capacità dei modelli YOLOv9 in un'ampia gamma di scenari di object detection.

L'addestramento dei modelli YOLOv9 richiederà più risorse e richiederà più tempo rispetto al modello YOLOv8 model di dimensioni equivalenti.

Desideriamo ringraziare gli autori di YOLOv9 per il loro significativo contributo nel campo del rilevamento di oggetti in tempo reale:

Il paper originale di YOLOv9 è disponibile su arXiv. Gli autori hanno reso il loro lavoro pubblicamente disponibile e il codice può essere consultato su GitHub. Apprezziamo i loro sforzi nel far progredire il settore e nel rendere il loro lavoro accessibile alla comunità più ampia.

YOLOv9 introduce tecniche rivoluzionarie come il Programmable Gradient Information (PGI) e la Generalized Efficient Layer Aggregation Network (GELAN). Queste innovazioni affrontano le sfide della perdita di informazioni nelle reti neurali profonde, garantendo elevata efficienza, accuratezza e adattabilità. PGI preserva i dati essenziali attraverso i layer della rete, mentre GELAN ottimizza l'utilizzo dei parametri e l'efficienza computazionale. Scopri di più sulle innovazioni principali di YOLOv9 che stabiliscono nuovi benchmark sul dataset MS COCO.

YOLOv9 supera i rilevatori di oggetti in tempo reale all'avanguardia ottenendo maggiore accuratezza ed efficienza. Sul dataset COCO, i modelli YOLOv9 mostrano punteggi mAP superiori in varie dimensioni, mantenendo o riducendo il sovraccarico computazionale. Ad esempio, YOLOv9c raggiunge un'accuratezza comparabile con il 42% in meno di parametri e il 21% in meno di domanda computazionale rispetto a YOLOv7 AF. Esplora i confronti delle prestazioni per metriche dettagliate.

Puoi addestrare un modello YOLOv9 usando sia comandi Python che CLI. Per Python, crea un'istanza di un modello usando la YOLO classe e chiamare il train metodo:

Per l'addestramento tramite CLI, eseguire:

Scopri di più sugli esempi di utilizzo per l'addestramento e l'inferenza.

YOLOv9 è progettato per mitigare la perdita di informazioni, il che è particolarmente importante per i modelli leggeri spesso inclini a perdere informazioni significative. Integrando le Informazioni sul Gradiente Programmabile (PGI) e le funzioni reversibili, YOLOv9 garantisce la conservazione dei dati essenziali, migliorando l'accuratezza e l'efficienza del modello. Questo lo rende altamente adatto per applicazioni che richiedono modelli compatti con prestazioni elevate. Per maggiori dettagli, esplora la sezione sull'impatto di YOLOv9 sui modelli leggeri.

YOLOv9 supporta varie attività, tra cui il rilevamento di oggetti e la segmentazione di istanze. È compatibile con diverse modalità operative come l'inferenza, la convalida, l'addestramento e l'esportazione. Questa versatilità rende YOLOv9 adattabile a diverse applicazioni di visione artificiale in tempo reale. Fare riferimento alla sezione attività e modalità supportate per ulteriori informazioni.

**Examples:**

Example 1 (unknown):
```unknown
I(X, X) >= I(X, f_theta(X)) >= I(X, g_phi(f_theta(X)))
```

Example 2 (unknown):
```unknown
X = v_zeta(r_psi(X))
```

Example 3 (python):
```python
from ultralytics import YOLO

# Build a YOLOv9c model from scratch
model = YOLO("yolov9c.yaml")

# Build a YOLOv9c model from pretrained weight
model = YOLO("yolov9c.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv9c model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 4 (sql):
```sql
# Build a YOLOv9c model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov9c.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv9c model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov9c.yaml source=path/to/bus.jpg
```

---

## YOLOv9: قفزة إلى الأمام في تكنولوجيا object detection

**URL:** https://docs.ultralytics.com/ar/models/yolov9/

**Contents:**
- YOLOv9: قفزة إلى الأمام في تكنولوجيا object detection
- مقدمة إلى YOLOv9
- الابتكارات الأساسية في YOLOv9
  - مبدأ عنق الزجاجة المعلوماتي
  - الدوال العكسية
  - التأثير على النماذج خفيفة الوزن
  - معلومات التدرج القابلة للبرمجة (PGI)
  - شبكة تجميع الطبقات الفعالة المعممة (GELAN)
- معايير YOLOv9
- الأداء على مجموعة بيانات MS COCO

يمثل YOLOv9 تطورًا كبيرًا في مجال الكشف عن الأجسام في الوقت الفعلي، حيث يقدم تقنيات رائدة مثل Programmable Gradient Information (PGI) و Generalized Efficient Layer Aggregation Network (GELAN). يُظهر هذا النموذج تحسينات ملحوظة في الكفاءة والدقة والقدرة على التكيف، مما يضع معايير جديدة على مجموعة بيانات MS COCO. يعتمد مشروع YOLOv9، الذي تم تطويره بواسطة فريق منفصل مفتوح المصدر، على قاعدة التعليمات البرمجية القوية التي توفرها UltralyticsYOLOv5، مما يدل على الروح التعاونية لمجتمع أبحاث الذكاء الاصطناعي.

شاهد: تدريب YOLOv9 على بيانات مخصصة باستخدام Ultralytics | مجموعة بيانات الحزم الصناعية

في السعي لتحقيق الكشف الأمثل عن الكائنات في الوقت الفعلي، تبرز YOLOv9 بنهجها المبتكر للتغلب على تحديات فقدان المعلومات المتأصلة في الشبكات العصبية العميقة. من خلال دمج PGI وبنية GELAN متعددة الاستخدامات، لا تعزز YOLOv9 قدرة النموذج على التعلم فحسب، بل تضمن أيضًا الاحتفاظ بالمعلومات الحاسمة طوال عملية الكشف، مما يحقق دقة وأداءً استثنائيين.

تستند تطورات YOLOv9 بشكل عميق إلى معالجة التحديات التي يفرضها فقدان المعلومات في الشبكات العصبية العميقة. يعتبر مبدأ Information Bottleneck والاستخدام المبتكر لوظائف Reversible Functions أساسيين لتصميمه، مما يضمن محافظة YOLOv9 على كفاءة ودقة عالية.

يكشف مبدأ عنق الزجاجة المعلوماتي عن تحدٍ أساسي في التعلم العميق: مع مرور البيانات عبر طبقات متتالية من الشبكة، يزداد احتمال فقدان المعلومات. يتم تمثيل هذه الظاهرة رياضيًا على النحو التالي:

حيث I تدل على المعلومات المتبادلة، و f و g تمثل دوال التحويل مع المعلمات theta و phi، على التوالي. تتصدى YOLOv9 لهذا التحدي من خلال تطبيق Programmable Gradient Information (PGI)، مما يساعد في الحفاظ على البيانات الأساسية عبر عمق الشبكة، مما يضمن توليد تدرج أكثر موثوقية، وبالتالي، تحسين تقارب النموذج وأدائه.

مفهوم الدوال العكسية هو حجر الزاوية الآخر في تصميم YOLOv9. تعتبر الدالة قابلة للعكس إذا كان من الممكن عكسها دون أي فقدان للمعلومات، كما هو معبر عنه بـ:

مع psi و zeta كمعاملات للدالة العكسية ودالتها العكسية، على التوالي. هذه الخاصية ضرورية لـ التعلم العميق تسمح الهيكليات للشبكة بالاحتفاظ بتدفق كامل للمعلومات، مما يتيح تحديثات أكثر دقة لمعلمات النموذج. تدمج YOLOv9 وظائف قابلة للعكس داخل هيكليتها للتخفيف من خطر تدهور المعلومات، خاصة في الطبقات العميقة، مما يضمن الحفاظ على البيانات الهامة لمهام detect الأجسام.

تعد معالجة فقدان المعلومات أمرًا حيويًا بشكل خاص للنماذج خفيفة الوزن، والتي غالبًا ما تكون ذات معلمات قليلة وعرضة لفقدان معلومات كبيرة أثناء عملية التغذية الأمامية. يضمن هيكل YOLOv9، من خلال استخدام PGI والوظائف القابلة للعكس، أنه حتى مع وجود نموذج مبسط، يتم الاحتفاظ بالمعلومات الأساسية المطلوبة لـ detect الكائنات بدقة واستخدامها بفعالية.

PGI هو مفهوم جديد تم تقديمه في YOLOv9 لمكافحة مشكلة عنق الزجاجة المعلوماتي، مما يضمن الحفاظ على البيانات الأساسية عبر طبقات الشبكة العميقة. يتيح ذلك إنشاء تدرجات موثوقة، مما يسهل تحديثات النموذج الدقيقة وتحسين أداء الكشف العام.

يمثل GELAN تقدمًا معماريًا استراتيجيًا، مما يمكّن YOLOv9 من تحقيق استخدام فائق للمعلمات وكفاءة حسابية. يسمح تصميمه بالتكامل المرن للكتل الحسابية المختلفة، مما يجعل YOLOv9 قابلاً للتكيف مع مجموعة واسعة من التطبيقات دون التضحية بالسرعة أو الدقة.

يتضمن القياس المعياري في YOLOv9 باستخدام Ultralytics تقييم أداء النموذج المدرب والمتحقق منه في سيناريوهات العالم الحقيقي. تتضمن هذه العملية:

من خلال القياس المعياري، يمكنك التأكد من أن النموذج الخاص بك لا يعمل بشكل جيد في بيئات الاختبار الخاضعة للرقابة فحسب، بل يحافظ أيضًا على أداء عالٍ في التطبيقات العملية في العالم الحقيقي.

شاهد: كيفية قياس أداء نموذج YOLOv9 باستخدام حزمة Ultralytics python

يوضح أداء YOLOv9 على مجموعة بيانات COCO تطوراته الكبيرة في الكشف عن الأجسام في الوقت الفعلي، مما يضع معايير جديدة عبر أحجام النماذج المختلفة. يقدم الجدول 1 مقارنة شاملة لأحدث أدوات الكشف عن الأجسام في الوقت الفعلي، مما يوضح الكفاءة الفائقة لـ YOLOv9 و الدقة.

تكرارات YOLOv9، بدءًا من الصغير t متغير إلى واسع النطاق e يوضح النموذج تحسينات ليس فقط في الدقة (مقاييس mAP) ولكن أيضًا في الكفاءة مع عدد أقل من المعلمات والاحتياجات الحسابية (FLOPs). يؤكد هذا الجدول قدرة YOLOv9 على تقديم أداء عالٍ الدقة مع الحفاظ على النفقات الحسابية أو تقليلها مقارنة بالإصدارات السابقة والنماذج المنافسة.

بالمقارنة، يُظهر YOLOv9 مكاسب ملحوظة:

يسلط نموذج YOLOv9c، على وجه الخصوص، الضوء على فعالية تحسينات الهندسة المعمارية. إنه يعمل بعدد أقل من المعلمات بنسبة 42٪ وطلب حسابي أقل بنسبة 21٪ من YOLOv7 AF، ولكنه يحقق دقة مماثلة، مما يدل على تحسينات الكفاءة الكبيرة في YOLOv9. علاوة على ذلك، يضع نموذج YOLOv9e معيارًا جديدًا للنماذج الكبيرة، مع عدد أقل من المعلمات بنسبة 15٪ وحاجة حسابية أقل بنسبة 25٪ من YOLOv8x، إلى جانب تحسن تدريجي بنسبة 1.7٪ في AP.

تُظهر هذه النتائج التطورات الاستراتيجية لـ YOLOv9 في تصميم النموذج، مؤكدة كفاءتها المحسنة دون المساومة على الدقة الأساسية لمهام الكشف عن الكائنات في الوقت الفعلي. لا يدفع النموذج حدود مقاييس الأداء فحسب، بل يؤكد أيضًا على أهمية الكفاءة الحاسوبية، مما يجعله تطورًا محوريًا في مجال رؤية الكمبيوتر.

مثّل YOLOv9، الذي صدر في فبراير 2024، تطورًا محوريًا في الكشف عن الكائنات في الوقت الفعلي، مقدمًا تحسينات كبيرة من حيث الكفاءة والدقة والقدرة على التكيف. من خلال معالجة التحديات الحرجة عبر حلول مبتكرة مثل PGI و GELAN، وضع YOLOv9 معايير جديدة وقت إصداره. بينما تم إصدار نماذج أحدث مثل YOLO11 و YOLO26 منذ ذلك الحين مع تحسينات إضافية، لا تزال ابتكارات YOLOv9 المعمارية تؤثر على هذا المجال.

يقدم هذا المثال أمثلة بسيطة لتدريب واستدلال YOLOv9. للاطلاع على الوثائق الكاملة لهذه الأنماط وغيرها، راجع صفحات الوثائق الخاصة بـ Predict وTrain وVal وExport.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

تقدم سلسلة YOLOv9 مجموعة من النماذج، تم تحسين كل منها للكشف عن الكائنات عالي الأداء. تلبي هذه النماذج الاحتياجات الحسابية المختلفة ومتطلبات الدقة، مما يجعلها متعددة الاستخدامات لمجموعة واسعة من التطبيقات.

يوفر هذا الجدول نظرة عامة مفصلة عن متغيرات نموذج YOLOv9، مع تسليط الضوء على قدراتها في مهام الكشف عن الأجسام وتوافقها مع أوضاع التشغيل المختلفة مثل Inference و Validation و Training و Export. يضمن هذا الدعم الشامل أن يتمكن المستخدمون من الاستفادة الكاملة من قدرات نماذج YOLOv9 في مجموعة واسعة من سيناريوهات الكشف عن الأجسام.

سيتطلب تدريب نماذج YOLOv9 موارد أكثر وسيستغرق وقتًا أطول من نموذج YOLOv8 ذي الحجم المكافئ.

نود أن نعرب عن تقديرنا لمؤلفي YOLOv9 لمساهماتهم الكبيرة في مجال الكشف عن الأجسام في الزمن الحقيقي:

يمكن العثور على ورقة YOLOv9 الأصلية على arXiv. لقد أتاح المؤلفون عملهم للجمهور، ويمكن الوصول إلى قاعدة التعليمات البرمجية على GitHub. نحن نقدر جهودهم في تطوير هذا المجال وإتاحة عملهم للمجتمع الأوسع.

يقدم YOLOv9 تقنيات رائدة مثل معلومات التدرج القابلة للبرمجة (PGI) وشبكة تجميع الطبقات الفعالة المعممة (GELAN). تعالج هذه الابتكارات تحديات فقدان المعلومات في الشبكات العصبية العميقة، مما يضمن كفاءة عالية ودقة وقابلية للتكيف. تحافظ PGI على البيانات الأساسية عبر طبقات الشبكة، بينما تعمل GELAN على تحسين استخدام المعلمات والكفاءة الحسابية. تعرف على المزيد حول الابتكارات الأساسية لـ YOLOv9 التي وضعت معايير جديدة على مجموعة بيانات MS COCO.

يتفوق YOLOv9 على أحدث أدوات الكشف عن الأجسام في الوقت الفعلي من خلال تحقيق دقة وكفاءة أعلى. في مجموعة بيانات COCO، تُظهر نماذج YOLOv9 درجات mAP فائقة عبر أحجام مختلفة مع الحفاظ على النفقات الحسابية أو تقليلها. على سبيل المثال، يحقق YOLOv9c دقة مماثلة مع عدد أقل من المعلمات بنسبة 42% وطلب حسابي أقل بنسبة 21% من YOLOv7 AF. استكشف مقارنات الأداء للحصول على مقاييس تفصيلية.

يمكنك تدريب نموذج YOLOv9 باستخدام أوامر Python و CLI. بالنسبة إلى Python، قم بإنشاء نموذج باستخدام YOLO الفئة واستدعاء train الطريقة:

بالنسبة لتدريب CLI، قم بتنفيذ:

تعرف على المزيد حول أمثلة الاستخدام للتدريب والاستدلال.

تم تصميم YOLOv9 للتخفيف من فقدان المعلومات، وهو أمر مهم بشكل خاص للنماذج خفيفة الوزن المعرضة غالبًا لفقدان معلومات كبيرة. من خلال دمج معلومات التدرج القابلة للبرمجة (PGI) والوظائف القابلة للعكس، يضمن YOLOv9 الاحتفاظ بالبيانات الأساسية، مما يعزز دقة النموذج وكفاءته. هذا يجعله مناسبًا للغاية للتطبيقات التي تتطلب نماذج مدمجة ذات أداء عالٍ. لمزيد من التفاصيل، استكشف القسم الخاص بـ تأثير YOLOv9 على النماذج خفيفة الوزن.

يدعم YOLOv9 مهام متنوعة بما في ذلك الكشف عن الأجسام و تقسيم المثيلات. وهو متوافق مع أوضاع التشغيل المتعددة مثل الاستدلال والتحقق والتدريب والتصدير. هذه المرونة تجعل YOLOv9 قابلاً للتكيف مع تطبيقات رؤية الكمبيوتر المتنوعة في الوقت الفعلي. راجع قسم المهام والأوضاع المدعومة لمزيد من المعلومات.

**Examples:**

Example 1 (unknown):
```unknown
I(X, X) >= I(X, f_theta(X)) >= I(X, g_phi(f_theta(X)))
```

Example 2 (unknown):
```unknown
X = v_zeta(r_psi(X))
```

Example 3 (python):
```python
from ultralytics import YOLO

# Build a YOLOv9c model from scratch
model = YOLO("yolov9c.yaml")

# Build a YOLOv9c model from pretrained weight
model = YOLO("yolov9c.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv9c model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 4 (sql):
```sql
# Build a YOLOv9c model from scratch and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov9c.yaml data=coco8.yaml epochs=100 imgsz=640

# Build a YOLOv9c model from scratch and run inference on the 'bus.jpg' image
yolo predict model=yolov9c.yaml source=path/to/bus.jpg
```

---

## YOLO-NAS

**URL:** https://docs.ultralytics.com/models/yolo-nas/

**Contents:**
- YOLO-NAS
- Overview
  - Key Features
- Pretrained Models
- Usage Examples
  - Inference and Validation Examples
- Supported Tasks and Modes
- Citations and Acknowledgments
- FAQ
  - What is YOLO-NAS and how does it improve over previous YOLO models?

Please note that Deci, the original creators of YOLO-NAS, have been acquired by NVIDIA. As a result, these models are no longer actively maintained by Deci. Ultralytics continues to support the usage of these models, but no further updates from the original team are expected.

Developed by Deci AI, YOLO-NAS is a groundbreaking object detection foundational model. It is the product of advanced Neural Architecture Search technology, meticulously designed to address the limitations of previous YOLO models. With significant improvements in quantization support and accuracy-latency trade-offs, YOLO-NAS represents a major leap in object detection.

Overview of YOLO-NAS. YOLO-NAS employs quantization-aware blocks and selective quantization for optimal performance. The model, when converted to its INT8 quantized version, experiences a minimal precision drop, a significant improvement over other models. These advancements culminate in a superior architecture with unprecedented object detection capabilities and outstanding performance.

Experience the power of next-generation object detection with the pretrained YOLO-NAS models provided by Ultralytics. These models are designed to deliver top-notch performance in terms of both speed and accuracy. Choose from a variety of options tailored to your specific needs:

Each model variant is designed to offer a balance between Mean Average Precision (mAP) and latency, helping you optimize your object detection tasks for both performance and speed.

Ultralytics has made YOLO-NAS models easy to integrate into your Python applications via our ultralytics python package. The package provides a user-friendly Python API to streamline the process.

The following examples show how to use YOLO-NAS models with the ultralytics package for inference and validation:

In this example we validate YOLO-NAS-s on the COCO8 dataset.

This example provides simple inference and validation code for YOLO-NAS. For handling inference results see Predict mode. For using YOLO-NAS with additional modes see Val and Export. YOLO-NAS on the ultralytics package does not support training.

PyTorch pretrained *.pt models files can be passed to the NAS() class to create a model instance in python:

CLI commands are available to directly run the models:

We offer three variants of the YOLO-NAS models: Small (s), Medium (m), and Large (l). Each variant is designed to cater to different computational and performance needs:

Below is a detailed overview of each model, including links to their pretrained weights, the tasks they support, and their compatibility with different operating modes.

If you employ YOLO-NAS in your research or development work, please cite SuperGradients:

We express our gratitude to Deci AI's SuperGradients team for their efforts in creating and maintaining this valuable resource for the computer vision community. We believe YOLO-NAS, with its innovative architecture and superior object detection capabilities, will become a critical tool for developers and researchers alike.

YOLO-NAS, developed by Deci AI, is a state-of-the-art object detection model leveraging advanced Neural Architecture Search (NAS) technology. It addresses the limitations of previous YOLO models by introducing features like quantization-friendly basic blocks and sophisticated training schemes. This results in significant improvements in performance, particularly in environments with limited computational resources. YOLO-NAS also supports quantization, maintaining high accuracy even when converted to its INT8 version, enhancing its suitability for production environments. For more details, see the Overview section.

You can easily integrate YOLO-NAS models into your Python application using the ultralytics package. Here's a simple example of how to load a pretrained YOLO-NAS model and perform inference:

For more information, refer to the Inference and Validation Examples.

YOLO-NAS introduces several key features that make it a superior choice for object detection tasks:

These features contribute to its high accuracy, efficient performance, and suitability for deployment in production environments. Learn more in the Key Features section.

YOLO-NAS models support various object detection tasks and modes such as inference, validation, and export. They do not support training. The supported models include YOLO-NAS-s, YOLO-NAS-m, and YOLO-NAS-l, each tailored to different computational capacities and performance needs. For a detailed overview, refer to the Supported Tasks and Modes section.

Yes, Ultralytics provides pretrained YOLO-NAS models that you can access directly. These models are pretrained on datasets like COCO, ensuring high performance in terms of both speed and accuracy. You can download these models using the links provided in the Pretrained Models section. Here are some examples:

**Examples:**

Example 1 (python):
```python
from ultralytics import NAS

# Load a COCO-pretrained YOLO-NAS-s model
model = NAS("yolo_nas_s.pt")

# Display model information (optional)
model.info()

# Validate the model on the COCO8 example dataset
results = model.val(data="coco8.yaml")

# Run inference with the YOLO-NAS-s model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO-NAS-s model and validate it's performance on the COCO8 example dataset
yolo val model=yolo_nas_s.pt data=coco8.yaml

# Load a COCO-pretrained YOLO-NAS-s model and run inference on the 'bus.jpg' image
yolo predict model=yolo_nas_s.pt source=path/to/bus.jpg
```

Example 3 (swift):
```swift
@misc{supergradients,
      doi = {10.5281/ZENODO.7789328},
      url = {https://zenodo.org/records/7789328},
      author = {Aharon,  Shay and {Louis-Dupont} and {Ofri Masad} and Yurkova,  Kate and {Lotem Fridman} and {Lkdci} and Khvedchenya,  Eugene and Rubin,  Ran and Bagrov,  Natan and Tymchenko,  Borys and Keren,  Tomer and Zhilko,  Alexander and {Eran-Deci}},
      title = {Super-Gradients},
      publisher = {GitHub},
      journal = {GitHub repository},
      year = {2021},
}
```

Example 4 (python):
```python
from ultralytics import NAS

# Load a COCO-pretrained YOLO-NAS-s model
model = NAS("yolo_nas_s.pt")

# Validate the model on the COCO8 example dataset
results = model.val(data="coco8.yaml")

# Run inference with the YOLO-NAS-s model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

---

## YOLO-World Model

**URL:** https://docs.ultralytics.com/models/yolo-world/

**Contents:**
- YOLO-World Model
- Overview
- Key Features
- Available Models, Supported Tasks, and Operating Modes
- Zero-shot Transfer on COCO Dataset
- Usage Examples
  - Train Usage
  - Predict Usage
  - Val Usage
  - Track Usage

The YOLO-World Model introduces an advanced, real-time UltralyticsYOLOv8-based approach for Open-Vocabulary Detection tasks. This innovation enables the detection of any object within an image based on descriptive texts. By significantly lowering computational demands while preserving competitive performance, YOLO-World emerges as a versatile tool for numerous vision-based applications.

Watch: YOLO World training workflow on custom dataset

YOLO-World tackles the challenges faced by traditional Open-Vocabulary detection models, which often rely on cumbersome Transformer models requiring extensive computational resources. These models' dependence on pre-defined object categories also restricts their utility in dynamic scenarios. YOLO-World revitalizes the YOLOv8 framework with open-vocabulary detection capabilities, employing vision-language modeling and pre-training on expansive datasets to excel at identifying a broad array of objects in zero-shot scenarios with unmatched efficiency.

Real-time Solution: Harnessing the computational speed of CNNs, YOLO-World delivers a swift open-vocabulary detection solution, catering to industries in need of immediate results.

Efficiency and Performance: YOLO-World slashes computational and resource requirements without sacrificing performance, offering a robust alternative to models like SAM but at a fraction of the computational cost, enabling real-time applications.

Inference with Offline Vocabulary: YOLO-World introduces a "prompt-then-detect" strategy, employing an offline vocabulary to enhance efficiency further. This approach enables the use of custom prompts computed apriori, including captions or categories, to be encoded and stored as offline vocabulary embeddings, streamlining the detection process.

Powered by YOLOv8: Built upon Ultralytics YOLOv8, YOLO-World leverages the latest advancements in real-time object detection to facilitate open-vocabulary detection with unparalleled accuracy and speed.

Benchmark Excellence: YOLO-World outperforms existing open-vocabulary detectors, including MDETR and GLIP series, in terms of speed and efficiency on standard benchmarks, showcasing YOLOv8's superior capability on a single NVIDIA V100 GPU.

Versatile Applications: YOLO-World's innovative approach unlocks new possibilities for a multitude of vision tasks, delivering speed improvements by orders of magnitude over existing methods.

This section details the models available with their specific pretrained weights, the tasks they support, and their compatibility with various operating modes such as Inference, Validation, Training, and Export, denoted by ✅ for supported modes and ❌ for unsupported modes.

All the YOLOv8-World weights have been directly migrated from the official YOLO-World repository, highlighting their excellent contributions.

The YOLO-World models are easy to integrate into your Python applications. Ultralytics provides user-friendly Python API and CLI commands to streamline development.

Watch: YOLO-World Model Usage examples with Ultralytics | Open Vocab, Prompt-Free & others 🚀

We strongly recommend to use yolov8-worldv2 model for custom training, because it supports deterministic training and also easy to export other formats i.e onnx/tensorrt.

Object detection is straightforward with the train method, as illustrated below:

PyTorch pretrained *.pt models as well as configuration *.yaml files can be passed to the YOLOWorld() class to create a model instance in python:

Object detection is straightforward with the predict method, as illustrated below:

This snippet demonstrates the simplicity of loading a pretrained model and running a prediction on an image.

Model validation on a dataset is streamlined as follows:

Object tracking with YOLO-World model on a video/images is streamlined as follows:

The YOLO-World models provided by Ultralytics come pre-configured with COCO dataset categories as part of their offline vocabulary, enhancing efficiency for immediate application. This integration allows the YOLOv8-World models to directly recognize and predict the 80 standard categories defined in the COCO dataset without requiring additional setup or customization.

The YOLO-World framework allows for the dynamic specification of classes through custom prompts, empowering users to tailor the model to their specific needs without retraining. This feature is particularly useful for adapting the model to new domains or specific tasks that were not originally part of the training data. By setting custom prompts, users can essentially guide the model's focus towards objects of interest, enhancing the relevance and accuracy of the detection results.

For instance, if your application only requires detecting 'person' and 'bus' objects, you can specify these classes directly:

Some users have found that appending an empty string "" as a background class can improve detection performance in certain scenarios. This behavior appears to be scenario-dependent and the exact mechanism is not fully understood:

You can also save a model after setting custom classes. By doing this you create a version of the YOLO-World model that is specialized for your specific use case. This process embeds your custom class definitions directly into the model file, making the model ready to use with your specified classes without further adjustments. Follow these steps to save and load your custom YOLO-World model:

First load a YOLO-World model, set custom classes for it and save it:

After saving, the custom_yolov8s.pt model behaves like any other pretrained YOLOv8 model but with a key difference: it is now optimized to detect only the classes you have defined. This customization can significantly improve detection performance and efficiency for your specific application scenarios.

This approach provides a powerful means of customizing state-of-the-art object detection models for specific tasks, making advanced AI more accessible and applicable to a broader range of practical applications.

WorldTrainerFromScratch is highly customized to allow training yolo-world models on both detection datasets and grounding datasets simultaneously. More details please checkout ultralytics.model.yolo.world.train_world.py.

We extend our gratitude to the Tencent AILab Computer Vision Center for their pioneering work in real-time open-vocabulary object detection with YOLO-World:

For further reading, the original YOLO-World paper is available on arXiv. The project's source code and additional resources can be accessed via their GitHub repository. We appreciate their commitment to advancing the field and sharing their valuable insights with the community.

The YOLO-World model is an advanced, real-time object detection approach based on the Ultralytics YOLOv8 framework. It excels in Open-Vocabulary Detection tasks by identifying objects within an image based on descriptive texts. Using vision-language modeling and pre-training on large datasets, YOLO-World achieves high efficiency and performance with significantly reduced computational demands, making it ideal for real-time applications across various industries.

YOLO-World supports a "prompt-then-detect" strategy, which utilizes an offline vocabulary to enhance efficiency. Custom prompts like captions or specific object categories are pre-encoded and stored as offline vocabulary embeddings. This approach streamlines the detection process without the need for retraining. You can dynamically set these prompts within the model to tailor it to specific detection tasks, as shown below:

YOLO-World provides several advantages over traditional Open-Vocabulary detection models:

Training a YOLO-World model on your dataset is straightforward through the provided Python API or CLI commands. Here's how to start training using Python:

Ultralytics offers multiple pretrained YOLO-World models supporting various tasks and operating modes:

To reproduce the official results from scratch, you need to prepare the datasets and launch the training using the provided code. The training procedure involves creating a data dictionary and running the train method with a custom trainer:

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLOWorld

# Load a pretrained YOLOv8s-worldv2 model
model = YOLOWorld("yolov8s-worldv2.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO-World model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a pretrained YOLOv8s-worldv2 model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov8s-worldv2.yaml data=coco8.yaml epochs=100 imgsz=640
```

Example 3 (sql):
```sql
from ultralytics import YOLOWorld

# Initialize a YOLO-World model
model = YOLOWorld("yolov8s-world.pt")  # or select yolov8m/l-world.pt for different sizes

# Execute inference with the YOLOv8s-world model on the specified image
results = model.predict("path/to/image.jpg")

# Show results
results[0].show()
```

Example 4 (julia):
```julia
# Perform object detection using a YOLO-World model
yolo predict model=yolov8s-world.pt source=path/to/image.jpg imgsz=640
```

---

## استكشف Ultralytics YOLOv8

**URL:** https://docs.ultralytics.com/ar/models/yolov8/

**Contents:**
- استكشف Ultralytics YOLOv8
- نظرة عامة
- الميزات الرئيسية لـ YOLOv8
- المهام والأوضاع المدعومة
- مقاييس الأداء
- أمثلة استخدام YOLOv8
- الاقتباسات والإقرارات
- الأسئلة الشائعة
  - ما هو YOLOv8 وكيف يختلف عن إصدارات YOLO السابقة؟
  - كيف يمكنني استخدام YOLOv8 لمهام رؤية الكمبيوتر المختلفة؟

تم إصدار YOLOv8 بواسطة Ultralytics في 10 يناير 2023، مقدمًا أداءً متطورًا من حيث الدقة والسرعة. بناءً على التطورات في إصدارات YOLO السابقة، قدم YOLOv8 ميزات وتحسينات جديدة تجعله خيارًا مثاليًا لمهام كشف الكائنات المتنوعة في مجموعة واسعة من التطبيقات.

شاهد: نظرة عامة على نموذج Ultralytics YOLOv8

استكشف ونفذ YOLOv8 مباشرة على Ultralytics .

تقدم سلسلة YOLOv8 مجموعة متنوعة من النماذج، كل منها متخصص في مهام محددة في رؤية الكمبيوتر. تم تصميم هذه النماذج لتلبية المتطلبات المختلفة، من الكشف عن الأجسام إلى المهام الأكثر تعقيدًا مثل تجزئة المثيلات، واكتشاف الوضع/النقاط الرئيسية، واكتشاف الأجسام الموجهة، والتصنيف.

تم تحسين كل نوع من سلسلة YOLOv8 للمهمة الخاصة به، مما يضمن أداءً ودقةً عالية. بالإضافة إلى ذلك، تتوافق هذه النماذج مع أوضاع التشغيل المختلفة بما في ذلك الاستدلال، و التحقق، و التدريب، و التصدير، مما يسهل استخدامها في مراحل مختلفة من النشر والتطوير.

يقدم هذا الجدول نظرة عامة على متغيرات نموذج YOLOv8، مع تسليط الضوء على قابليتها للتطبيق في مهام محددة وتوافقها مع أوضاع التشغيل المختلفة مثل الاستدلال والتحقق والتدريب والتصدير. إنه يعرض تنوع وقوة سلسلة YOLOv8، مما يجعلها مناسبة لمجموعة متنوعة من التطبيقات في رؤية الكمبيوتر.

راجع وثائق الكشف لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق الكشف لأمثلة الاستخدام مع هذه النماذج المدربة على Open Image V7، والتي تتضمن 600 فئة مدربة مسبقًا.

راجع وثائق التجزئة لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن 80 فئة مدربة مسبقًا.

راجع وثائق التصنيف لأمثلة الاستخدام مع هذه النماذج المدربة على ImageNet، والتي تتضمن 1000 فئة مدربة مسبقًا.

راجع وثائق تقدير الوضعيات لأمثلة الاستخدام مع هذه النماذج المدربة على COCO، والتي تتضمن فئة واحدة مدربة مسبقًا، وهي 'شخص'.

راجع وثائق الكشف الموجه لأمثلة الاستخدام مع هذه النماذج المدربة على DOTAv1، والتي تتضمن 15 فئة مدربة مسبقًا.

يقدم هذا المثال أمثلة بسيطة لتدريب واستدلال YOLOv8. للاطلاع على الوثائق الكاملة لهذه الأنماط وغيرها، راجع صفحات الوثائق الخاصة بـ Predict وTrain وVal وExport.

لاحظ أن المثال أدناه خاص بنماذج الكشف عن الكائنات Detect الخاصة بـ YOLOv8. للحصول على مهام إضافية مدعومة، راجع مستندات التقطيع و التصنيف و OBB ومستندات الوضع.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO() class لإنشاء مثيل نموذج في python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

منشور Ultralytics YOLOv8

لم تنشر Ultralytics ورقة بحثية رسمية لـ YOLOv8 نظرًا للطبيعة سريعة التطور للنماذج. نحن نركز على تطوير التكنولوجيا وتسهيل استخدامها، بدلاً من إنتاج وثائق ثابتة. للحصول على أحدث المعلومات حول بنية YOLO وميزاته واستخدامه، يرجى الرجوع إلى مستودع GitHub الخاص بنا و الوثائق.

إذا كنت تستخدم نموذج YOLOv8 أو أي برنامج آخر من هذا المستودع في عملك، فيرجى الاستشهاد به باستخدام التنسيق التالي:

يرجى ملاحظة أن مُعرِّف الكائن الرقمي (DOI) معلق وسيتم إضافته إلى الاقتباس بمجرد توفره. يتم توفير نماذج YOLOv8 بموجب تراخيص AGPL-3.0 و Enterprise.

تم تصميم YOLOv8 لتحسين أداء الكشف عن الأجسام في الوقت الفعلي من خلال الميزات المتقدمة. على عكس الإصدارات السابقة، يشتمل YOLOv8 على رأس Ultralytics مقسم وخالي من المرساة، و هياكل العمود الفقري والعنق الحديثة، ويوفر مقايضة مُحسَّنة بين الدقة والسرعة، مما يجعله مثاليًا للتطبيقات المتنوعة. لمزيد من التفاصيل، راجع قسمي النظرة العامة و الميزات الرئيسية.

يدعم YOLOv8 مجموعة واسعة من مهام رؤية الكمبيوتر، بما في ذلك الكشف عن الكائنات، وتقسيم المثيلات، والكشف عن الوضع/النقاط الرئيسية، والكشف عن الكائنات الموجهة، والتصنيف. تم تحسين كل متغير من النموذج لمهمته المحددة ومتوافق مع أوضاع التشغيل المختلفة مثل الاستدلال و التحقق من الصحة و التدريب و التصدير. ارجع إلى قسم المهام والأوضاع المدعومة لمزيد من المعلومات.

تحقق نماذج YOLOv8 أداءً حديثًا عبر مجموعات بيانات قياسية مختلفة. على سبيل المثال، يحقق نموذج YOLOv8n قيمة mAP (متوسط الدقة المتوسطة) تبلغ 37.3 على مجموعة بيانات COCO وسرعة 0.99 مللي ثانية على A100 TensorRT. يمكن العثور على مقاييس الأداء التفصيلية لكل متغير نموذج عبر المهام ومجموعات البيانات المختلفة في قسم مقاييس الأداء.

يمكن إجراء تدريب نموذج YOLOv8 باستخدام Python أو CLI. فيما يلي أمثلة لتدريب نموذج باستخدام نموذج YOLOv8 مُدرَّب مسبقًا على COCO على مجموعة بيانات COCO8 لـ 100 حقبة:

لمزيد من التفاصيل، قم بزيارة وثائق التدريب.

نعم، يمكن قياس أداء نماذج YOLOv8 من حيث السرعة والدقة عبر تنسيقات تصدير مختلفة. يمكنك استخدام PyTorch و ONNX و TensorRT والمزيد للقياس. فيما يلي أمثلة لأوامر القياس باستخدام Python و CLI:

للحصول على معلومات إضافية، تحقق من قسم مقاييس الأداء.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLOv8n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLOv8n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolov8n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLOv8n model and run inference on the 'bus.jpg' image
yolo predict model=yolov8n.pt source=path/to/bus.jpg
```

Example 3 (css):
```css
@software{yolov8_ultralytics,
  author = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title = {Ultralytics YOLOv8},
  version = {8.0.0},
  year = {2023},
  url = {https://github.com/ultralytics/ultralytics},
  orcid = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license = {AGPL-3.0}
}
```

Example 4 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)
```

---

## النماذج المدعومة بواسطة Ultralytics

**URL:** https://docs.ultralytics.com/ar/models/

**Contents:**
- النماذج المدعومة بواسطة Ultralytics
- النماذج المميزة
- البدء: أمثلة الاستخدام
- المساهمة بنماذج جديدة
- الأسئلة الشائعة
  - ما هو أحدث نموذج Ultralytics YOLO؟
  - كيف يمكنني تدريب نموذج YOLO على بيانات مخصصة؟
  - ما هي إصدارات YOLO التي تدعمها Ultralytics؟
  - لماذا يجب علي استخدام منصة Ultralytics لمشاريع التعلم الآلي؟
  - ما أنواع المهام التي يمكن لنماذج Ultralytics YOLO أداؤها؟

مرحبًا بك في وثائق نماذج Ultralytics! نحن نقدم الدعم لمجموعة واسعة من النماذج، كل منها مصمم خصيصًا لمهام محددة مثل الكشف عن الأجسام، و تقسيم المثيلات، و تصنيف الصور، و تقدير الوضعية، و تتبع الأجسام المتعددة. إذا كنت مهتمًا بالمساهمة بهيكلة النموذج الخاص بك في Ultralytics، فراجع دليل المساهمة الخاص بنا.

فيما يلي بعض النماذج الرئيسية المدعومة:

شاهد: قم بتشغيل نماذج Ultralytics YOLO في بضعة أسطر فقط من التعليمات البرمجية.

يوفر هذا المثال أمثلة بسيطة لتدريب واستدلال YOLO. للحصول على الوثائق الكاملة حول هذه الأنماط وغيرها، راجع صفحات وثائق التوقع و التدريب و التقييم و التصدير.

لاحظ أن المثال أدناه يسلط الضوء على نماذج YOLO11 Detect لـ object detection. للحصول على مهام إضافية مدعومة، راجع مستندات Segment و Classify و Pose.

PyTorch مدربة مسبقًا *.pt بالإضافة إلى نماذج التهيئة *.yaml يمكن تمرير الملفات إلى YOLO(), SAM(), NAS() و RTDETR() لإنشاء مثيل للنموذج في Python:

تتوفر أوامر CLI لتشغيل النماذج مباشرة:

هل أنت مهتم بالمساهمة بنموذجك في Ultralytics؟ هذا رائع! نحن منفتحون دائمًا على توسيع حافظة نماذجنا.

تَشعيب المستودع: ابدأ بتشعيب مستودع Ultralytics على GitHub.

استنساخ التشعيب الخاص بك: استنسخ التشعيب الخاص بك إلى جهازك المحلي وأنشئ فرعًا جديدًا للعمل عليه.

تنفيذ النموذج الخاص بك: أضف النموذج الخاص بك باتباع معايير وإرشادات البرمجة المتوفرة في دليل المساهمة الخاص بنا.

الاختبار بدقة: تأكد من اختبار النموذج الخاص بك بدقة، سواء بشكل مستقل أو كجزء من خط الأنابيب.

إنشاء طلب سحب: بمجرد رضاك عن النموذج الخاص بك، قم بإنشاء طلب سحب إلى المستودع الرئيسي للمراجعة.

مراجعة التعليمات البرمجية والدمج: بعد المراجعة، إذا كان النموذج الخاص بك يفي بمعاييرنا، فسيتم دمجه في المستودع الرئيسي.

للحصول على خطوات مفصلة، راجع دليل المساهمة الخاص بنا.

أحدث نموذج Ultralytics YOLO هو YOLO26، الذي صدر في يناير 2026. يتميز YOLO26 بالاستدلال الشامل الخالي من NMS، والنشر المحسّن على الحافة، ويدعم جميع المهام الخمس (detect، segment، التصنيف، تقدير الوضع، و obb) بالإضافة إلى إصدارات المفردات المفتوحة. لأحمال عمل الإنتاج المستقرة، يُعد كل من YOLO26 و YOLO11 خيارات موصى بها.

يمكن إنجاز تدريب نموذج YOLO على بيانات مخصصة بسهولة باستخدام مكتبات Ultralytics. إليك مثال سريع:

لمزيد من الإرشادات التفصيلية، تفضل بزيارة صفحة وثائق التدريب.

تدعم Ultralytics مجموعة شاملة من إصدارات YOLO (You Only Look Once) من YOLOv3 إلى YOLO11، جنبًا إلى جنب مع نماذج مثل YOLO-NAS و SAM و RT-DETR. تم تحسين كل إصدار لمهام مختلفة مثل الاكتشاف والتقسيم والتصنيف. للحصول على معلومات مفصلة حول كل نموذج، راجع وثائق النماذج التي تدعمها Ultralytics.

توفر منصة Ultralytics منصة شاملة بدون تعليمات برمجية لتدريب نماذج YOLO ونشرها وإدارتها. إنها تبسط سير العمل المعقدة، مما يمكّن المستخدمين من التركيز على أداء النموذج وتطبيقه. يوفر المركز أيضًا إمكانات التدريب السحابي، وإدارة شاملة لمجموعات البيانات، وواجهات سهلة الاستخدام لكل من المبتدئين والمطورين ذوي الخبرة.

تتميز نماذج Ultralytics YOLO بتعدد استخداماتها ويمكنها أداء مهام تشمل كشف الكائنات، وتجزئة الكائنات، والتصنيف، وتقدير الوضعيات، وكشف الكائنات الموجهة (obb). يدعم أحدث نموذج، YOLO26، جميع المهام الخمس بالإضافة إلى كشف المفردات المفتوحة. لمزيد من التفاصيل حول مهام محددة، يرجى الرجوع إلى صفحات المهام.

**Examples:**

Example 1 (python):
```python
from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("yolo26n.pt")

# Display model information (optional)
model.info()

# Train the model on the COCO8 example dataset for 100 epochs
results = model.train(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model("path/to/bus.jpg")
```

Example 2 (markdown):
```markdown
# Load a COCO-pretrained YOLO26n model and train it on the COCO8 example dataset for 100 epochs
yolo train model=yolo26n.pt data=coco8.yaml epochs=100 imgsz=640

# Load a COCO-pretrained YOLO26n model and run inference on the 'bus.jpg' image
yolo predict model=yolo26n.pt source=path/to/bus.jpg
```

Example 3 (python):
```python
from ultralytics import YOLO

# Load a YOLO model
model = YOLO("yolo26n.pt")  # or any other YOLO model

# Train the model on custom dataset
results = model.train(data="custom_data.yaml", epochs=100, imgsz=640)
```

Example 4 (unknown):
```unknown
yolo train model=yolo26n.pt data='custom_data.yaml' epochs=100 imgsz=640
```

---
