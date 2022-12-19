import cv2
import numpy as np
kamera=cv2.VideoCapture(0)
while True:

    ret,frame=kamera.read()
    hsvframe=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #red
    lowred=np.array([161,155,84])
    highred=np.array([179,255,255])
    redmask=cv2.inRange(hsvframe,lowred,highred)
    red=cv2.bitwise_and(frame,frame,mask=redmask)
    #blue
    lowred=np.array([94,80,2])
    highred=np.array([126,255,255])
    bluemask=cv2.inRange(hsvframe,lowred,highred)
    blue=cv2.bitwise_and(frame,frame,mask=bluemask)
    #cv2.imshow("resim",frame)
    cv2.imshow("red",red)

    cv2.imshow("redmask",redmask)
    cv2.imshow("blue",blue)

    cv2.imshow("bluemask",bluemask)
    if cv2.waitKey(25)==27:
         break
kamera.relase()
cv2.destroyAllWindows()
