import numpy as np
import cv2

#Load Image RGB
I = cv2.imread("C:\\Users\\Administrator\\Downloads\\shape.jpg")
cv2.imshow("I", I)

# convert Whiter color to black
[rows, cols, c] = I.shape;
for i in range(rows):
    for j in range(cols):
        if I[i,j,0] >200 and I[i,j,1] >200 and I[i,j,2] >200 :
            I[i,j,:] = 0;
cv2.imshow("Inew", I)
# Extract chanel B
B = I[:,:,0]
# Extract chanel G
G = I[:,:,1]
# Extract chanel R
R = I[:,:,2]
# Thresold for chanel B
thresh,blue = cv2.threshold(B,200,255,cv2.THRESH_BINARY)
thresh,green = cv2.threshold(G,200,255,cv2.THRESH_BINARY)
thresh,red = cv2.threshold(R,200,255,cv2.THRESH_BINARY)
C_plus = blue|green|red
cv2.imshow("binaryImage",C_plus)
cv2.waitKey()
