#showing diffrent color format derived from webcam
import cv2 as cv
import numpy as np
resize = 0.5 
# https://docs.opencv.org/3.4/de/d25/imgproc_color_conversions.html #all Color conversion documentation
colorConversion = {
    "cv::COLOR_BGR2GRAY":cv.COLOR_BGR2GRAY
    ,"COLOR_BGR2XYZ":cv.COLOR_BGR2XYZ
    ,"COLOR_BGR2YCrCb":cv.COLOR_BGR2YCrCb
    ,"COLOR_BGR2HSV":cv.COLOR_BGR2HSV
    ,"cv::COLOR_BGR2HLS":cv.COLOR_BGR2HLS
    ,"cv::COLOR_BGR2Lab":cv.COLOR_BGR2Lab
    ,"cv::COLOR_BGR2Luv":cv.COLOR_BGR2Luv
    }
cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("No camera found")
    exit()
switch = True
while True:
    isCapturing,frame = cap.read()
   
    frame =  cv.flip(frame,1)
    frame = cv.flip(frame,0)
    
    if not isCapturing:
        print("Please check Camera")
    h,w = frame.shape[0:2]
    frame = cv.resize(frame,(int(w*resize),int(h*resize)))
    cv.imshow("original",frame)
    for i in colorConversion:
        test =  cv.cvtColor(frame,colorConversion[i])
        cv.imshow(i,test)
        
    key = cv.waitKey(1) 
    if key == ord("q"):# ms to wait
        cap.release()
        cv.destroyAllWindows()
        break
    elif key == ord("c"):
        if switch:
            switch = False
        else:
            switch = True