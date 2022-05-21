import cv2
import numpy as np

camera = cv2.VideoCapture(0)
while (True):
    ret, frame = camera.read()
    if frame is None:
        break
    #BGR para HSV
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #definindo as mascaras para cor verde / green color mask
    lower = np.array([40,70,80])
    upper = np.array([75,255,255])

    #identificação do objeto  // identifying object
    mask = cv2.inRange(hsvFrame,lower,upper)

    outline,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    if(outline):
        maxArea = cv2.contourArea(outline[0])
        idMaxOutline = 0
        j = 0
        for i in outline:
            if maxArea < cv2.contourArea(i):
                maxArea = cv2.contourArea(i)
                idMaxOutline = j
            j += 1
        x,y,w,h = cv2.boundingRect(outline[idMaxOutline])

        if(maxArea > 100):
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),3)
            cv2.drawContours(frame, [outline[idMaxOutline]], 0, (139, 0, 139), 3)

            
    
    cv2.imshow('frame', frame)
    cv2.imshow('mask',mask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()