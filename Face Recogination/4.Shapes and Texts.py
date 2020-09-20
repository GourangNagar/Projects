# Coloring image
# Coloring channels : Blue , Green , Red

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)    #Size of matrix and 3 show no. of channels
print(img.shape)     #for size

print(img)   #give matrix image

# without below lines default image will be black
img[200:300,100:300] = 255,0,0  #for only blue its 255 and range is defined b/w brackets
#img[:] = 255,0,0   #if i want to color full image 

cv2.imshow("Image",img)

cv2.waitKey(0)


# Line on image

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8) 

#cv2.line(img,(0,0),(400,400),(0,255,0),3)
#   img , start point ,end point , color , thickness

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# img.shape[1] for width and [0] for height

cv2.imshow("Image",img)

cv2.waitKey(0)


# Rectangle on image

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

#cv2.rectangle(img,(0,0),(300,450),(0,0,255),cv2.FILLED)
#   img , start point ,end point , color , to fill our rectangle/any number as thickness

cv2.rectangle(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),7)
# img.shape[1] for width and [0] for height

cv2.imshow("Image",img)

cv2.waitKey(0)


# Circles on image

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.circle(img,(400,100),100,(0,255,255),5) #yellow color
#   img , center ,radius , color , to fill circle/any number as thickness

cv2.imshow("Image",img)

cv2.waitKey(0)


# Texts on image

import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

cv2.putText(img,"Gourang ",(200,200),cv2.FONT_HERSHEY_COMPLEX,1.5,(255,255,0),2)
#   img , text ,origin , font , size , color , thickness

cv2.imshow("Image",img)

cv2.waitKey(0)
