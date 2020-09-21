import cv2
import numpy as np

def empty(a):
    pass

# Creating a Taskbar
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)

# The minimum values are changed using mask initial value 
# Values varies fromm image to image
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)    # Minimum hue
cv2.createTrackbar("Hue Max","Trackbars",179,179,empty)  # Maximum hue
cv2.createTrackbar("Sat Min","Trackbars",75,255,empty)   # Saturation Min
cv2.createTrackbar("Sat Max","Trackbars",255,255,empty)  # Sat. Max
cv2.createTrackbar("Val Min","Trackbars",105,255,empty)  # Value min
cv2.createTrackbar("Val Max","Trackbars",255,255,empty)  # Value max
while True:
    img = cv2.imread("Resources/download.jpg")
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)   # creating a HSV image 
    
    hmin = cv2.getTrackbarPos("Hue Min","Trackbars")
    hmax = cv2.getTrackbarPos("Hue Max", "Trackbars")
    satmin = cv2.getTrackbarPos("Sat Min", "Trackbars")
    satmax = cv2.getTrackbarPos("Sat Max", "Trackbars")
    valmin = cv2.getTrackbarPos("Val Min", "Trackbars")
    valmax = cv2.getTrackbarPos("Val Max", "Trackbars")
    
    print(hmin,hmax,satmin,satmax,valmin,valmax)  # Displaying all values corresponding to trackbar shifts
    
    lower = np.array([hmin,satmin,valmin])
    upper = np.array([hmax, satmax, valmax])
    
    mask = cv2.inRange(imgHSV,lower,upper)  # Mask is the most important part 
    # It use trackbar values and make a new image corresponding to it and helps to get image
    # In mask unwanted colors should be black and colors we need should be white

    imgResult = cv2.bitwise_and(img,img,mask=mask)
    # Bitwise AND just comparing mask image and original image so that we can detect our color


    cv2.imshow("HSV Imagel",imgHSV)
    cv2.imshow("Original",img)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)

    cv2.waitKey(1)
