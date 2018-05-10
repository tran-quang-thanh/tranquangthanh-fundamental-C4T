import numpy as np
import cv2

cap = cv2.VideoCapture(0)
lower = np.array([0,78,78])
higher = np.array([21,203,255])
while (True):
    ret,frame = cap.read()
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    binImg = cv2.inRange(hsvImage,lower,higher)
    cv2.imshow("den trang",binImg)
    ret, contours, hierarchy = cv2.findContours(binImg, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i in range(len(contours)):
        M = cv2.moments(contours[i])
        cx = int(M['m10'])
        cy = int(M['m01'])
        cv2.circle(frame,(cx,cy),5,(0,0,255),5)
    cv2.imshow("video",frame)
    key = cv2.waitKey(10)
    if key == ord("q"):
        break
