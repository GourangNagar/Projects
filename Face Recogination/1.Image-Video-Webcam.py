# Image
import cv2

img = cv2.imread("Resources/imagename.jpg")   # To read a specific image from path
cv2.imshow("Output",img)                      # To print that specific image
cv2.waitKey(0)                        # for infinite delay else image will stop


# Video
import cv2

vid = cv2.VideoCapture("Resources/Videoname.mp4")  # For specified Video path to Play
while True:
    success, img = vid.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # press q to stop the  video
        break


s        
