from dataclasses import dataclass
from threading import Thread
from time import sleep
from typing import List, Literal, Self, Any, Callable, Optional

import cv2
import numpy as np
from cv2 import Mat, cvtColor, COLOR_RGB2GRAY, VideoCapture
from numpy import ndarray, dtype, generic
from numpy.linalg import linalg
from pyapriltags import Detector, Detection

detector = Detector(
    families = "tag36h11",  #
    nthreads = 2,  # 线程数
    quad_decimate = 1.0,  # 降采样
    refine_edges = False,  # 边缘细化
    debug = False,  # 调试模式
)


#cap = cv2.VideoCapture(0)
image = cv2.imread('0.png')

if not cap.isOpened():
    print("无法打开摄像头")
else:
    ret, frame = cap.read()
if not ret:
    print("无法获取帧")
else:
    image = frame
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    detections = detector.detect(gray_image)
    print(detections)
cap.release()
