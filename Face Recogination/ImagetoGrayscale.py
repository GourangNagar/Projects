import cv2

img = cv2.imread("Resources/imagename.jpg")                 # To read a specific image from path
imgGray = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)            # conversion to gray scale
cv2.imshow("Gray Image", imgGray)                           # To print that specific gray image
cv2.waitKey(0)                                              # for infinite delay else image will stop
