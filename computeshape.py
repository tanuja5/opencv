cap = cv2.VideoCapture(0) #Webcam Capture

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    template = cv2.imread('pen0.png',cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
        
    res = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    
    loc=np.where(res >= 0.7)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+ w, pt[1] + h), (0,255,0), 3)
        
    #cv2.imshow('Test',frame)
    cv2.imshow('Test1', res)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()	
