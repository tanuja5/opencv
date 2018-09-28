import cv2
import numpy as np

#differentiate pens by color


#Open web cam
cam= cv2.VideoCapture(0)
ret, img=cam.read()


img=cv2.resize(img,(340,220))

#convert image to hsv
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#Red pen
lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])
mask=cv2.inRange(hsv,lowerBound,upperBound)

cv2.imshow("cam",img)
