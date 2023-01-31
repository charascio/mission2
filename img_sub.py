#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import numpy as np

def RedRecognition(image):

    img = CvBridge.imgmsg_to_cv2(image, "bgr8")
    
    def cv_show(name, img):
        cv2.imshow(name, img)
        cv2.waitKey(0)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    low_hsv = np.array([0, 43, 46])
    high_hsv = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)

    median = cv2.medianBlur(mask, 5)

    contours, hierarchy = cv2.findContours(median, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    img2 = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv_show('img', img2)



def subscriber():
    rospy.init_node("sub")

    img = rospy.Subscriber("img_process", Image, RedRecognition, queue_size=10)

    rospy.spin()

if __name__ == "__main__":
    subscriber()