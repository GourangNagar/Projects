import cv2
import numpy as np

img = cv2.imread("Resources/test.jpeg")

imghor = np.hstack((img,img)) # Join Images Horizontally
imgver = np.vstack((img,img)) # Join Image Vertically

cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical",imgver)

cv2.waitKey(0)
