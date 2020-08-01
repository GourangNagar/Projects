import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)
# Defining kernel/matrix of always ones of size 5 x 5

img = cv2.imread("Resources/imagename.jpg") 
# To read a specific image from path

imgGray  = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
# converting colored image to gray scale

imgBlur  = cv2.GaussianBlur(imgGray,(31,31),0)
# here 7 x 7 is kernel size... must be odd number...blurness is directly prop. to k size

imgCanny = cv2.Canny(img,100,100)
# Here 100 and 100 are lower and upper threshold values and converting to edged image

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
# It can modify image dilation and iteration gives size of each edge

imgEroded = cv2.erode(imgDilation,kernel,iterations=1)
# It can modify eroded image and iteration gives size of each edge

cv2.imshow("Gray Image", imgGray)                           # To print that specific gray image
cv2.imshow("Blur Image", imgBlur)                           # To print that specific blur image
cv2.imshow("Canny Image", imgCanny)                         # To print that specified edged image
cv2.imshow("Dilation Image", imgDilation)                   # To print that specified Dilated image
cv2.imshow("Eroded Image", imgEroded)                       # To print that specified Eroded image

cv2.waitKey(0)                                              # for infinite delay else image will stop
