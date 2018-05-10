import numpy as np
import cv2
def callback(x):
    pass

#connect webcam
cap = cv2.VideoCapture(0)
lower = np.array([0,78,78])
higher = np.array([21,203,255])

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)
while(True):
    ret,frame = cap.read()
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #convert to binary
    binImage = cv2.inRange(hsvImage,lower,higher)

    cv2.imshow("binImage", binImage)
    cv2.imshow("hsvImage", hsvImage)
    cv2.imshow("video",frame)
    key = cv2.waitKey(30)
    if key == ord("q"):
        break

