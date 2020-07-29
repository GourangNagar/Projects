import cv2

vid = cv2.VideoCapture(0)
vid.set(3,640)   # Width of screen
vid.set(4,480)   # Hight of screen
vid.set(10,100)  # Brightness of Webcam

while True:
    success, img = vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):   # press q to stop webcam
        break
