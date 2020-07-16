# Project 13 - Person Detection in Thermal Images​

made based on the Darknet framework available at: https://github.com/AlexeyAB/darknet

## Content
- [Project 13 - Person Detection in Thermal Images​](#project-13---person-detection-in-thermal-images)
  - [Content](#content)
  - [About the project](#about-the-project)
  - [Basic Terms](#basic-terms)
  - [YOLO - You Only Look Once](#yolo---you-only-look-once)
  - [Metrics](#metrics)
  - [Evaluation metrics](#evaluation-metrics)
  - [Database](#database)
  - [Training](#training)
  - [Realizaion of tasks](#realizaion-of-tasks)
    - [SuccSuccessful result example](#succsuccessful-result-example)
    - [Unsuccessful result example](#unsuccessful-result-example)
  - [Results](#results)
    - [Detection results of a YOLOv4 model trained only on the MS COCO data set​](#detection-results-of-a-yolov4-model-trained-only-on-the-ms-coco-data-set)
    - [Detection results of a model trained on the MS COCO data set and thermal images](#detection-results-of-a-model-trained-on-the-ms-coco-data-set-and-thermal-images)
  - [Conclusion](#conclusion)

## About the project
**Input:** Thermal image from surveillance video recording 

**Dataset:** http://ieee-dataport.org/open-access/thermal-image-dataset-person-detection-uniri-tid

**Output**: detection of the person in the image (bounding box with confidence score)​

**Requirements:** 
- Recognition and localization of the person​
- Multiple persons should be detected​
- Evaluating detection performance - average precision​


## Basic Terms
**Classification** - categorizing objects in a picture
- example: ***in this picture is a person***

**Detection** - categorizing and locating object in a picture

**Segmentation** - dividing a picture into segments that represent objects or their parts, sorts pixels into larger components [https://missinglink.ai/guides/computer-vision/image-segmentation-deep-learning-methods-applications/]

<a href="https://imgbb.com/"><img src="https://i.ibb.co/PMhwm6Z/example4.jpg" alt="example4" style="width:400px"></a>

[http://ronny.rest/tutorials/module/seg_01/segmentation_01_intro/]

## YOLO - You Only Look Once
Yolo is a state-of-the-art real time object detection system that works as followed:
1. Single neural network is applied to the full image
2. Region division -> bounding boxes, probabilities for each region
3. Weighting probabilities, post processing

[https://pjreddie.com/darknet/yolo/]

## Metrics
AP-The average precision over all 10 IoU thresholds (i.e., [0.5:0.05:0.95]) of all object categories​

APIOU = 0.50 - The average precision over all object categories when the IoU overlap with ground truth is larger than 0.50​

APIOU = 0.75 - The average precision over all object categories when the IoU overlap with ground truth is larger than 0.75​

​

MS COCO original script for calculation [https://github.com/cocodataset/cocoapi]​

Script [https://github.com/Cartucho/mAP] for IoU display on selected images​

## Evaluation metrics
IoU (intersect over union) - average intersect over union of objects and detections for a certain threshold

mAP (mean average precision) - mean value of average precisions for each class
- due to having only one class, we have only AP

[https://github.com/AlexeyAB/darknet]

## Database
Avalable at: http://ieee-dataport.org/open-access/thermal-image-dataset-person-detection-uniri-tid
(University of Rijeka, UNIRI-TID)

- train set: 3790 images
- val set: 2527 images
- ratio: 60 : 40

We distributed various types of weather scenes evenly among two sets

## Training
For training and testing we used Darknet framework [https://github.com/AlexeyAB/darknet]

In .cfg file for training we set the resolution grid:
- width: 416
- height = 416
- batch = 16
- max_batches: 6000

Using the transfer learning, YOLOv4 model pre-trained on MS COCO [] dataset, we trained  on thermal images for about 5 hours​

<<<<<<< HEAD
=======
### Realization of tasks
>>>>>>> efd3393ad8e1045c49f3eebfa8b8613b59e07c0c

## Realizaion of tasks
Task 1: Recognition and localization of a person
- We made a person detection script. It took images from an input folder and after YOLOv4 detection saved images with detection markers into an output folder

Task 2: Multiple people to be detected​
- Additionaly, along with finding bounding boxes and confidence scores, we added code to count the number of people on an image

Task 3: Evaluating detection performance  -average precision​
- We evaluated the performance of the YOLOv4 model on thermal images with a model trained only on the MS COCO data set and a model that was trained on 60% of the obtained thermal images by knowledge transfer
- Detection enhancement for each metric: 
  - AO from 15% to 54%
  - AP50 from 28% to 99% 
  - AP75 from 10% to 50% ​
  - APs from 2% to 40%, 
  - APm from 13% to 54%
  - APL from 52% to 61%​​

Even 60% of images training with the UNIRI-TID model led to great results

### SuccSuccessful result example

<img src = "https://i.ibb.co/zG7FMh0/det347.jpg" width="300"/>

### Unsuccessful result example

<img src = "https://i.ibb.co/xj0QRq9/det240.jpg" width="300"/>
<<<<<<< HEAD

## Results
### Detection results of a YOLOv4 model trained only on the MS COCO data set​

```
Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all         | maxDets=100 ] = 0.135​

Average Precision  (AP) @[ IoU=0.50          | area=   all         | maxDets=100 ] = 0.276​

Average Precision  (AP) @[ IoU=0.75          | area=   all         | maxDets=100 ] = 0.100​

Average Precision  (AP) @[ IoU=0.50:0.95 | area= small      | maxDets=100 ] = 0.016​

Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium  | maxDets=100 ] = 0.131​

Average Precision  (AP) @[ IoU=0.50:0.95 | area= large       | maxDets=100 ] = 0.517​

Number of ground-truth objects: 3714​

Number of detected objects: 1128 (tp:1106, fp:22)​
```

### Detection results of a model trained on the MS COCO data set and thermal images

```
Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all         | maxDets=100 ] = 0.536​

Average Precision  (AP) @[ IoU=0.50          | area=   all         | maxDets=100 ] = 0.987​

Average Precision  (AP) @[ IoU=0.75          | area=   all         | maxDets=100 ] = 0.502​

Average Precision  (AP) @[ IoU=0.50:0.95 | area= small      | maxDets=100 ] = 0.403​

Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium  | maxDets=100 ] = 0.544​

Average Precision  (AP) @[ IoU=0.50:0.95 | area= large       | maxDets=100 ] = 0.611​
​

Number of ground-truth objects: 3714​

Number of detected objects: 3892 (tp:3658, fp:234)​
```

## Conclusion
We had to make a person detector for infrared images. We decided to do that with YOLO v4 and the Darknet framework because it seemed the fastest and most accurate, and it gave better results than we expected.
=======
>>>>>>> efd3393ad8e1045c49f3eebfa8b8613b59e07c0c
