import cv2

vid = cv2.VideoCapture("Resources/Videoname.mp4")  # For specified Video path to Play
while True:
    success, img = vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to stop the  video
        break
