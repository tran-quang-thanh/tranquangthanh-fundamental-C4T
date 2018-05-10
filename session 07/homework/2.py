import numpy as np
import cv2

frame = cv2.imread("C:\\Users\\Administrator\\Downloads\\hand.jpg")
cv2.imshow("initial",frame)
kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
bin_erode = cv2.erode(frame,kernel)
bin_dilate = cv2.dilate(bin_erode,kernel)
cv2.imshow("anh",bin_dilate)
cv2.waitKey()
