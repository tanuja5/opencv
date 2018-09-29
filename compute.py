import cv2
import numpy as np

#differentiate pens by color


#Open web cam
cap= cv2.VideoCapture(0)
#returns true if camera is on
cap.isOpened()


while(1):
    ret, img = cap.read()

    # converting frame(img == BGR) to HSV(hue-saturation-value)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # blue color

    blue_lower = np.array([99,115,150],np.uint8)
    blue_upper = np.array([110,255,255],np.uint8)

    # black color

    black_lower = np.array([0,0,0],np.uint8)
    black_upper = np.array([180,255,30],np.uint8)

    # all color together

    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    black = cv2.inRange(hsv, black_lower, black_upper)

    # Morphological Transform- Dilation

    kernal = np.ones((5, 5), "uint8")

    
    blue = cv2.dilate(blue, kernal)
    res_blue = cv2.bitwise_and(img, img, mask = blue)

    black = cv2.dilate(black, kernal)
    res_black = cv2.bitwise_and(img, img, mask = black)

    # Tracking black
    (_, contours, hierarchy)=cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 2)
            cv2.putText(img, "Black Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0))
            
    # Tracking blue
    (_, contours, hierarchy)=cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0))
            

    
    cv2.imshow("Color Tracking", img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
