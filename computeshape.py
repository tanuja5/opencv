cap = cv2.VideoCapture(0) #Webcam Capture

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    template = cv2.imread('pen0.png',cv2.IMREAD_GRAYSCALE)
        #w, h = template.shape[::-1]
        
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    print(np.where(res>=0.8))
    cv2.imshow('Test',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()	
