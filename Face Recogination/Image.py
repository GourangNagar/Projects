import cv2

img = cv2.imread("Resources/imagename.jpg")   # To read a specific image from path
cv2.imshow("Output",img)                      # To print that specific image
cv2.waitKey(0)                        # for infinite delay else image will stop