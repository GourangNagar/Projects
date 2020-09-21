import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

img = cv2.imread("Resources/faces.jpg")
img1 = cv2.imread("Resources/faces1.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1Gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
faces1 = faceCascade.detectMultiScale(img1Gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,0),2)
    
for (x,y,w,h) in faces1:
    cv2.rectangle(img1,(x,y),(w+x,h+y),(0,255,0),2)

cv2.imshow("Image", img)
cv2.imshow("Image1", img1)

cv2.waitKey(0)
