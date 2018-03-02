#pip install imutils, opencv-python
from imutils.video import VideoStream
from imutils.video import FPS
import imutils
import numpy as np
import argparse
import cv2
import time

ap = argparse.ArgumentParser()#allows for cmd commands
ap.add_argument("-p", "--prototxt", required=True,
	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,
	help="path to Caffe pre-trained model")
ap.add_argument("-c", "--confidence", type=float, default=0.2,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

CLASSES = ["Background","Airplane","Bicycle","Boat","Dog", "Horse", "Motorcycle", "Person", "Pottedplant", "Sheep",
	"Sofa", "train", "tvmonitor"]
