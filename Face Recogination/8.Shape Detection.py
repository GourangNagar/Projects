import cv2
import numpy as np

def getContours(img):     # function help us to find contour and shape detection
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)  #detect shape in whole picture
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)  # area of each shape

        if area > 500:   # helps to remove small elements / non shape images
            cv2.drawContours(imgContour, cnt, -1, (255,0,0), 3)  #draw boundaries
            peri = cv2.arcLength(cnt , True)
            #print(peri)            #print perimeter
            approx = cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))     # printing no. of sides
            objCor = len(approx)       # storing sides
            x,y,w,h = cv2.boundingRect(approx)    #all four coordinates

            if objCor == 3: objectType = "Triangles"  # if sides = 3 then triangle
            elif objCor == 4:
                aspRatio = w/float(h)      # w/h of a square = 1 and we are considering 0.05 error
                if aspRatio > 0.95 and aspRatio < 1.05 :objectType = "Square"
                else: objectType = "Rectangle"    # else rectangle
            elif objCor > 4 : objectType = "Circles"   # if want to add more shapes we can and else become circle in that case
            else: objectType = "None"       # in case of undefined shape

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)        # creating box around and writing objectType on it
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,0),2)
                                             # 10 pixels above and right from center

img = cv2.imread("Resources/shapes.jpg")
imgContour = img.copy()

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
imgBlank = np.zeros_like(img)

getContours(imgCanny)

cv2.imshow("Original",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Blank",imgBlank)
cv2.imshow("Contour",imgContour)

cv2.waitKey(0)
