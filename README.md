# calculAI_video_analysis

## Introduction
Video analysis using Yolo and openCV library which will read video as frames and detect objects in that frames. I saved all videos files and output json file in local videos folder.

## Dependencies
Docker image with python 3.7 and opencv 4.1.0

Build and tag the image "sudo docker build -t opencvcalculai ."

Run docker file "sudo docker run -d opencvcalculai:latest"

Run this command "xhost local:root" when erro occures as "Gtk-WARNING **: 06:49:47.946: cannot open display: unix:0"

docker-compose build

docker-compose up 

or

Install below required library in your local machine.

1) python 3.7
2) opencv 4.1.0
3) numpy 


## Download Pre-Trained Yolov3 Model file
Download the pre-trained YOLO v3 weights file from this [link](https://drive.google.com/file/d/1AECks3mc2Xwe2BjvNdC_QKiiKZF8wt35/view?usp=sharing) and place it in the current directory

## Quick Start



This analyse python file using Yolov3 to detect objects from videos and save object names as JSON file in videos folder.


## Sample Output
I have uploaded sample json file results in videos folder.

{'remote', 'cup', 'cell phone', 'person'}
