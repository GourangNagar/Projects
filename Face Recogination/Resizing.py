import cv2
import numpy as np

img = cv2.imread("Resources/test.jpeg")
print(img.shape)

imgResize = cv2.resize(img,(1000,554)) # h , v
print(imgResize.shape)

imgCropped = img[62:492,50:500] # v , h

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
