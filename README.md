# calculAI_video_analysis

## Introduction
Video analysis using Yolo and openCV library which will read video as frames and detect objects in that frames. I saved all videos files and output json file in local videos folder.

## Dependencies
Docker image with python 3.7 and opencv 4.1.0

Build and tag the image "sudo docker build -t opencvcalculai ."

or

Install python 3.7 , opencv 4.1.0 and numpy install in your machine 


## Download Pre-Trained Yolov3 Model file
Download the pre-trained YOLO v3 weights file from this [link](https://drive.google.com/file/d/1AECks3mc2Xwe2BjvNdC_QKiiKZF8wt35/view?usp=sharing) and place it in the current directory

## Quick Start
Generate video from webcam using webcam.py

 `$ python3 webcam.py`

 The above python file will read input from webcam and save in the videos folder.


We can Analyse video files and get detected object names using analyse.py

 `$ python3 analyse.py --video videos/video_0.7177935927284033.mp4`


This analyse python file using Yolov3 to detect objects from videos and save object names as JSON file in videos folder.


## Sample Output
Check videos folder and json files

{'remote', 'cup', 'cell phone', 'person'}
