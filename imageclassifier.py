#pip install opencv-python
import numpy as np
import sys
import cv2
import tensorflow as tf# just used ti test
cascPath = 'haarcascade_frontalface.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
hello = tf.constant("hello world")
sess = tf.Session()
print(sess.run(hello))
defaultcam = cv2.VideoCapture(0)

while(True):
    ret, frame = defaultcam.read()# returns t/f if frame is read correctly
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.imshow('Press "q" to exit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
defaultcam.release()
cv2.destroyAllWindows()
