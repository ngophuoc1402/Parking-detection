# SMART PARKING DETECTION SYSTEM

## Overview
This project aims to build a computer vision system to detect parking slot occupancy from a video. Given a parking lot video, the system will determine if the parking slot is occupied or empty.

Key assumption
- The camera is static
- Parking slots do not change position
>> This allow the system to use predefined slot regions without recalibration


### Planned Pipeline
1. Frame extraction
- Input: A video of parking car view 
- Output: Frames 

2. Vehicle detection 
- Input: Frames/ Images 
- Output: Bounding boxes of objects 
          Confidence scores for each objects

3. Parking slot definition
- Manually define parking slot regions
- Each slot is represented as a rectangle (or polygon if needed)

4. Occupancy Determination 
- Compute the overlap between:
  + Detected vehicles bounding boxes
  + Predefined parking slots

- (Maybe use CNN classifier)

5. Temporal Smoothing
- Major voting (last 5-10 frames)
>> handles missing detections, flickering

6. Evaluation
- Metrics: accuracy, precision, recall, f1-score

## Expected output:
- A demo video
- A csv file contains: frame, timestamp, slot id, occupancy, iou

#### Notes: This project is for my graduation as well as learning journey in Computer vision,
