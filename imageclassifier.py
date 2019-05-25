#pip install opencv-python
import numpy as np
import sys
import cv2

faceCascPath = 'haarcascade_frontalface.xml'
faceCascade = cv2.CascadeClassifier(faceCascPath)

defaultcam = cv2.VideoCapture(0)
#
while(True):
    ret, frame = defaultcam.read()# returns t/f if frame is read corr
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
        print("(",x,",",y,")")
        if(x < 200 and y < 200):
            print("top left")
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, "Face", (x, y), font, 1.0, (255, 255, 255), 1)




    cv2.imshow('Press "q" to exit', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
defaultcam.release()
cv2.destroyAllWindows()
