import face_recognition as fr
import cv2

Tommy = fr.load_image_file("D:\\Programs\\Python\\face Recognition\\Known\\Tommy Smith.jpg")
TommyEncoding = fr.face_encodings(Tommy)[0]
cam = cv2.VideoCapture(0)


while True:
