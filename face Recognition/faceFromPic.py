import cv2,os,datetime,sys
from PIL import Image
from PIL import ImageFilter
import face_recognition as fr
KnownPeople = [

    "Tommy Smith"

]

Tommy = fr.load_image_file("D:\\Programs\\Python\\face Recognition\\Known\\Tommy Smith.jpg")
TommyEncoding = fr.face_encodings(Tommy)[0]
cam = cv2.VideoCapture(0)

def takePic():


    while(True):

        date = datetime.datetime.today()
        ret, frame = cam.read()# returns t/f if frame is read correctly
        cv2.imshow('Press "q" to exit', frame)
        k = cv2.waitKey(33)

        if k == 27:#esc pressed
            cam.release()
            cv2.destroyAllWindows()

            break
        elif k == 32:
            # SPACE pressed
            imageName = "unknownImage"+ date.strftime("%Y%m%d%S") +".png" #change save file name
            imageName = "D:\\Programs\\Python\\face Recognition\\Unknown\\" + imageName
            cv2.imwrite(imageName, frame)
            print("image saved as, ", imageName)
            cam.release()
            cv2.destroyAllWindows()
            print("scanning...")
            

            unknownImage = fr.load_image_file(imageName)
            unknownEncoding = fr.face_encodings(unknownImage)[0]

            isTommy = fr.compare_faces([TommyEncoding],unknownEncoding)
            if isTommy:
                print("that is: ",KnownPeople[0])
            break


takePic()
