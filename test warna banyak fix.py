import cv2
import numpy as np

#load Haar Cascade Tomat
#tomato_cascade = cv2.CascadeClassifier('/home/pi/opencv-master/data/haarcascades/haarcascade_tomat.xml')

#set nilai threshold untuk deteksi warna
cap=cv2.VideoCapture(0)
lower_red=np.array([0,148,56])
upper_red=np.array([10,255,255])
lower_green=np.array([60,0,157])
upper_green=np.array([106,77,255])
lower_yellow=np.array([20,100,100])
upper_yellow=np.array([30,255,255])

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    # detect warna merah
    mask_red=cv2.inRange(hsv,lower_red,upper_red)
    _,mask_red=cv2.threshold(mask_red,254,255,cv2.THRESH_BINARY)
    _, cnts_red, _=cv2.findContours(mask_red,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts_red:
        if cv2.contourArea(c) > 600:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("Matang merah"),(x+w+10,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
            
    # detect warna hijau
    mask_green=cv2.inRange(hsv,lower_green,upper_green)
    _,mask_green=cv2.threshold(mask_green,254,255,cv2.THRESH_BINARY)
    _,cnts_green, _=cv2.findContours(mask_green,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts_green:
        if cv2.contourArea(c) > 600:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("Mentah hijau"),(x+w+10,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)
    
    # detect warna kuning
    mask_yellow=cv2.inRange(hsv,lower_yellow,upper_yellow)
    _,mask_yellow=cv2.threshold(mask_yellow,254,255,cv2.THRESH_BINARY)
    _,cnts_yellow, _=cv2.findContours(mask_yellow,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for c in cnts_yellow:
        if cv2.contourArea(c) > 600:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame,("Matang kuning"),(x+w+10,y+h),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

    # detect menggunakan Haar cascade classifier        
    


    #show the output image      
    cv2.imshow("FRAME",frame)
    if cv2.waitKey(1)&0xFF==27:   
        break
        
cap.release()
cv2.destroyAllWindows()
