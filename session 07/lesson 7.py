import cv2
import numpy as np

I = cv2.imread("C:\\Users\\Administrator\\Downloads\\shape.jpg")
cv2.namedWindow("shape",cv2.WINDOW_NORMAL)
cv2.imshow("shape",I)
cv2.waitKey(1)
#
B = I[:,:,0]   #I[rows,cols,channel],":" de chay tat ca cac gia tri
G = I[:,:,1]
R = I[:,:,2]
cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.waitKey(1)
#
C_plus = B&R&G
cv2.imshow("newImage",C_plus)
cv2.waitKey(1)
#convert Image to binary
ret, binImg = cv2.threshold(C_plus,100,255,cv2.THRESH_BINARY_INV)
cv2.imshow("binImg",binImg)
cv2.waitKey(1)
#find contour
ret,contours,hierarchy = cv2.findContours(binImg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# print(ret)
# for i in contours:
#     cv2.drawContours(I,i,-1,(255,0,255),5)
for i in range(len(contours)):
    cv2.drawContours(I,contours,i,(255,0,255),5)
    leni = cv2.arcLength(contours[i],True)
    print("lenght of contour:", leni)
    areai = cv2.contourArea(contours[i])
    print("area contour:", areai)
    # approximate polygon
    nedges = cv2.approxPolyDP(contours[i],5,True)
    print("polyedges:", len(nedges))
    if (len(nedges) == 3):
        cv2.putText(I,"tam giac",(nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,255,0)) #ve chu len anh
    if (len(nedges) == 4):
        cv2.putText(I,"HCN",(nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,255,0))
    if (len(nedges) > 9):
        cv2.putText(I,"Hinh tron",(nedges[0][0][0],nedges[0][0][1]),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.5,(0,255,0))
    # xac dinh tam cua hinh
    M = cv2.moments(contours[i])
    cx = int(M['m10']/M['m00'])  #xem anh dien thoai
    cy = int(M['m01']/M['m00'])
    cv2.circle(I,(cx,cy),10,(120,255,0),5)
cv2.imshow("Image countour",I)
cv2.waitKey()

