#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def publisher():

    rospy.init_node("pub")

    img = rospy.Publisher("img_process", Image, queue_size=10)

    bridge = CvBridge()

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():

        cap = cv2.VideoCapture(0)

        cap.set(3, 256)
        cap.set(4, 256)
        cap.set(5, 60)

        while True:
            flag, frame = cap.read()

            img.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))

            rospy.loginfo("Success")

            rate.sleep() 

if __name__ == "__main__":
    publisher()


        
