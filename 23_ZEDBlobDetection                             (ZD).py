#!/usr/bin/env python
import cv2
import numpy as np
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float32
from cv_bridge import CvBridge, CvBridgeError
import sys
import threading


class Detector:
    YELLOW = [np.array(x, np.uint8) for x in [[25,100,100], [35, 255, 255]] ]
    MAX_DETECTIONS = 1
    ERODE = (5,5)
    

    def get_filtered_contours(self,img):
        hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        
        hsv_img = cv2.erode(hsv_img, self.ERODE, iterations=10)  #XXX
        frame_threshed = cv2.inRange(hsv_img, self.YELLOW[0], self.YELLOW[1])
        ret,thresh = cv2.threshold(frame_threshed, self.YELLOW[0][0], 255, 0)
         

        filtered_contours = []
        contours, hierarchy = cv2.findContours(\
                thresh,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_SIMPLE)
        contour_area = [ (cv2.contourArea(c), (c) ) for c in contours]
        contour_area = sorted(contour_area,reverse=True, key=lambda x: x[0])

        height,width = img.shape[:2]
        for j, (area,(cnt)) in enumerate(contour_area):
            if j > self.MAX_DETECTIONS: continue
            x,y,w,h = cv2.boundingRect(cnt)
            box = (x,y,w,h)
            d =  0.5*(x-width/2)**2 + (y-height)**2 
            if d < 20000: continue # filter tiny

            mask = np.zeros(thresh.shape,np.uint8)
            cv2.drawContours(mask,[cnt],0,255,-1)
            mean_val = cv2.mean(img,mask = mask)
            aspect_ratio = float(w)/h
            filtered_contours.append( (cnt, box, d, aspect_ratio, mean_val) )
        return filtered_contours


    def contour_match(self, img):
        '''
        Returns 1. Image with bounding boxes added
                2. an ObstacleImageDetectionList
        '''

        height,width = img.shape[:2]
        
        # get filtered contours
        contours = self.get_filtered_contours(img)
        
        for (cnt, box, ds, aspect_ratio, mean_color)  in contours:
                        
            # plot box and label around contour
            x,y,w,h = box
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img,"yellow", (x,y), font, 1,mean_color,4)
            cv2.rectangle(img,(x,y),(x+w,y+h), mean_color,2)
        return img

class StaticObjectDetectorNode:
    def __init__(self):
        self.name = 'static_object_detector_node'
        
        self.detector = Detector()
        self.thread_lock = threading.Lock()
        self.sub_image = rospy.Subscriber("/camera/rgb/image_rect_color", Image, self.cbImage, queue_size=1)
        self.pub_image = rospy.Publisher("~detection_image", Image, queue_size=1)
        self.bridge = CvBridge()

        rospy.loginfo("[%s] Initialized." %(self.name))


    def cbImage(self,image_msg):
        thread = threading.Thread(target=self.processImage,args=(image_msg,))
        thread.setDaemon(True)
        thread.start()

    def processImage(self, image_msg):
        if not self.thread_lock.acquire(False):
            return
        try:
            image_cv=self.bridge.imgmsg_to_cv2(image_msg,"bgr8")
        except CvBridgeErrer as e:
            print e
        img = self.detector.contour_match(image_cv)
        height,width = img.shape[:2]
        try:
            self.pub_image.publish(self.bridge.cv2_to_imgmsg(img, "bgr8"))
        except CvBridgeError as e:
            print(e)

        self.thread_lock.release()

if __name__=="__main__":
	rospy.init_node('static_object_detector_node')
	node = StaticObjectDetectorNode()
	rospy.spin()
