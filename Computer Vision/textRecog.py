from PIL import Image
from PIL import ImageFilter
import pytesseract,os,cv2,datetime,sys
import numpy as np
#path doesnt work for somereason
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'
cls = lambda: os.system('cls')

def openImage():
    cls()
    print("items in file 'images':")
    fileList = []
    fileCount = 0
    for (dirpath, dirnames, filenames) in os.walk("D:\Programs\Python\Computer Vision\images"):
        fileList.extend(filenames)
        for file in fileList:
            print("--",fileList[fileCount])
            fileCount = fileCount + 1


    imageName = input("image name: ")
    if imageName in fileList:
        imageName = "D:\Programs\Python\Computer Vision\images\\" + imageName

        recognizedText = pytesseract.image_to_string(Image.open(imageName))
        print(recognizedText)
    else:
        print("invalid")

def takePic():
    cam = cv2.VideoCapture(0)

    while True:
        date = datetime.datetime.today()
        ret, frame = cam.read()# returns t/f if frame is read correctly

        cv2.imshow('Press "esc" to exit', frame)
        k = cv2.waitKey()

        if k%256 == 27:#esc pressed
            cam.release()
            cv2.destroyAllWindows()
            break
        elif k%256 == 32:
            # SPACE pressed
            imageName = "TextRecogImage"+ date.strftime("%Y%m%d%S") +".png" #change save file name
            cv2.imwrite(imageName, frame)
            print("image saved as, ", imageName)
            cam.release()
            cv2.destroyAllWindows()
            print("Checking for recognizeable text...")
            imageName = "D:\Programs\Python\Computer Vision\\" + imageName
            recognizedText = pytesseract.image_to_string(Image.open(imageName))
            print(recognizedText)
            break
def live():#live text detcetion
    cam = cv2.VideoCapture(0)
    faceCascPath = "D:\Programs\Python\Computer Vision\CASCADES\haarcascade_frontalface.xml"
    faceCascade = cv2.CascadeClassifier(faceCascPath)
    k = cv2.waitKey(1)
    while True:
        ret, frame = cam.read()# returns t/f if frame is read correctly
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
        cv2.imshow('Press "esc" to exit', frame)

        if k%256 == 27:#esc pressed
            cam.release()
            cv2.destroyAllWindows()
            break



liveOrImage = input("use image(1) || Take Picture (2) || live(3)")

if liveOrImage == str(1):
    openImage()
elif liveOrImage == str(2):
    takePic()
elif liveOrImage == str(3):
    live()
