import cv2
import numpy as np
classifer=cv2.CascadeClassifier("haarcascade_fullbody.xml")
capture=cv2.VideoCapture('walking.mp4')
while capture.isOpened():
    ret,frame=capture.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=classifer.detectMultiScale(gray,1.6,5)
    for(x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),10)
        cv2.imshow('int',frame)
        if cv2.waitKey(1)==13:
            break
capture.release()
cv2.destroyAllWindows()