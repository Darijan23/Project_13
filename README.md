# Project 13
## Person Detection in Thermal Images​

made based on the Darknet framework available at: https://github.com/AlexeyAB/darknet

### About the project
**Input:** Thermal image from surveillance video recording 

**Dataset:** http://ieee-dataport.org/open-access/thermal-image-dataset-person-detection-uniri-tid

**Output**: detection of the person in the image (bounding box with confidence score)​

**Requirements:** 
- Recognition and localization of the person​
- Multiple persons should be detected​
- Evaluating detection performance - average precision​


### Basic Terms
**Classification** - categorizing objects in a picture
- example: ***in this picture is a person***

**Detection** - categorizing and locating object in a picture

**Segmentation** - dividing a picture into segments that represent objects or their parts, sorts pixels into larger components [https://missinglink.ai/guides/computer-vision/image-segmentation-deep-learning-methods-applications/]

### YOLO - You Only Look Once
Yolo is a state-of-the-art real time object detection system that works as followed:
1. Single neural network is applied to the full image
2. Region division -> bounding boxes, probabilities for each region
3. Weighting probabilities, post processing

[https://pjreddie.com/darknet/yolo/]

### Metrics
AP-The average precision over all 10 IoU thresholds (i.e., [0.5:0.05:0.95]) of all object categories​

APIOU = 0.50 - The average precision over all object categories when the IoU overlap with ground truth is larger than 0.50​

APIOU = 0.75 - The average precision over all object categories when the IoU overlap with ground truth is larger than 0.75​

​

MS COCO original script for calculation [https://github.com/cocodataset/cocoapi]​

Script [https://github.com/Cartucho/mAP] for IoU display on selected images​

### Evaluation metrics
IoU (intersect over union) - average intersect over union of objects and detections for a certain threshold

mAP (mean average precision) - mean value of average precisions for each class
- due to having only one class, we have only AP

[https://github.com/AlexeyAB/darknet]

### Database
Avalable at: http://ieee-dataport.org/open-access/thermal-image-dataset-person-detection-uniri-tid
(University of Rijeka, UNIRI-TID)

- train set: 3790 images
- val set: 2527 images
- ratio: 60 : 40

We distributed various types of weather scenes evenly among two sets

### Training
For training and testing we used Darknet framework [https://github.com/AlexeyAB/darknet]

In .cfg file for training we set the resolution grid:
- width: 416
- height = 416
- batch = 16
- max_batches: 6000

Using the transfer learning, YOLOv4 model pre-trained on MS COCO [] dataset, we trained  on thermal images for about 5 hours​

​### Realization of tasks

Task 1: Recognition and localization of a person
- We made a person detection script. It took images from an input folder and after YOLOv4 detection saved images with detection markers into an output folder

Task 2: Multiple people to be detected​
- Additionaly, along with finding bounding boxes and confidence scores, we added code to count the number of people on an image

Task 3: Evaluating detection performance  -average precision​
- We evaluated the performance of the YOLOv4 model on thermal images with a model trained only on the MS COCO data set and a model that was trained on 60% of the obtained thermal images by knowledge transfer
- Detection enhancement present for each metric: 
  - AO from 15% to 54%
  - AP50 from 28% to 99% 
  - AP75 from 10% to 50% ​
  - AP scales: from 2% to 40%, 
  - APm 13% na 54%
  - APL 52% na 61%​​

Even 60% of images training with the UNIRI-TID model lead to great results

### Successful result example

<a href="https://ibb.co/cDCwBc7"><img src="https://i.ibb.co/zG7FMh0/det347.jpg" alt="det347" border="0"></a>

### Unsuccessful result example

<a href="https://ibb.co/r6SJ128"><img src="https://i.ibb.co/xj0QRq9/det240.jpg" alt="det240" border="0"></a>