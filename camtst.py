#pip install opencv-python
import numpy as np
import cv2
defaultcam = cv2.VideoCapture(0)
while(True):
    ret, frame = defaultcam.read()# returns t/f if frame is read correctly
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Press "q" to exit', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
defaultcam.release()
cv2.destroyAllWindows()
