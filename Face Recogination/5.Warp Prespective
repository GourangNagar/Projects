# Also known as the work done by cam scanner when auto croping the image with thw help of corners

import cv2
import numpy as np

img = cv2.imread("Resources/test.jpeg")

width,height=206,208    #resultant image width and height based on coordinates
pts1 = np.float32([[173,175],[379,175],[173,375],[379,375]])  # all corner coordinates of resultant image
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])    # after warping new coordinates
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)
