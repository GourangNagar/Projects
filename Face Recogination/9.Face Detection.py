import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")  # Calling Inbuilt xml file helps to detect face

img = cv2.imread("Resources/faces.jpg")

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(w+x,h+y),(0,255,0),2)     # making rectangle boxes around detections
    
cv2.imshow("Image", img)
cv2.waitKey(0)
