from pynput import mouse
import cv2 as cv 
import numpy as np
from HSVClass import hsvSetter
from dinoControl import Dino
cap = cv.VideoCapture(0)

NUMBER_OF_DIFFRENT_COLORS = 2 # currently only 1 color is supported bugs comes with more than one color
highColors = [[255,255,255],[255,255,255]]
lowColors = [[0, 92, 216],[255,255,255]]
colorsRange = []
mouseSensivity =  4
a,f = cap.read()
size =  f.shape
dinoControl = Dino(size[0],size[1])
for i in range(NUMBER_OF_DIFFRENT_COLORS):
    c = hsvSetter(i,lowColors[i],highColors[i])
    colorsRange.append(c)
def setMouseSensivity(value):
    global mouseSensivity
    mouseSensivity = value
def getMouseSensivity():
    return  mouseSensivity   
def  calculateContours(mask):
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if  cv.contourArea(contour) > 2500:
            
            #epsilon = 0.1*cv.arcLength(contour,True) # epsilon is some% of conotour arm length (0.1 = 10%)
            #simpleContour = cv.approxPolyDP(contour,epsilon,True)
            
            
            return  contour
    
    
def calulateCentroidContour(contour):
    
    M = cv.moments(contour)

    if M['m00'] != 0 or M["m00"] != 0:
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        return (cx,cy)
    
    
    
def setMask(hsv,colorsRange):
    mask  =  cv.inRange(hsv,colorsRange[0].getLowColorRange(),colorsRange[0].getHighColorRange())
    cv.imshow("trackbars"+str(0),mask)
    for i in range(1,len(colorsRange)):
        mask2 = cv.inRange(hsv,colorsRange[i].getLowColorRange(),colorsRange[i].getHighColorRange())
        
        #for i in range(1,len(colorsRange)):
        cv.imshow("trackbars"+str(i),mask2)
        mask = cv.bitwise_or(mask,mask2)
        
    
    
    
    return mask

def adjustFrame(rawFrame):
    #This func adjust the axis of frame 
    
    fixedFrame = rawFrame
    fixedFrame =  cv.flip(fixedFrame,1)
    fixedFrame = cv.flip(fixedFrame,0)
    return fixedFrame 

def getResult(rawFrame,mask):
    result = cv.bitwise_and(rawFrame,rawFrame, mask= mask)
    return result  

def displayOutputs(hsv,rawFrame,mask,res):
    cv.imshow("hsv",hsv) 
    cv.imshow("raw",rawFrame)
    cv.imshow("mask",mask)
    cv.imshow("result",res)
    

def handelCameraFailException():
    
    cv.destroyAllWindows()
    cap.release() 
    raise Exception("Please check the camera")
MouseController = mouse.Controller()        
def controlMouse(coordinates):
    if coordinates !=  None:
        x = coordinates[0]  
        y =coordinates[1]   
        
        MouseController.press(mouse.Button.left)
        MouseController.position = (x*getMouseSensivity(),y*getMouseSensivity())
    cv.createTrackbar("mouseSensivity", "raw",getMouseSensivity(),10,setMouseSensivity) 
while True:
    for i in range(len(colorsRange)):   
             colorsRange[i].setHsvValues("trackbars"+str(i))
    isCapturing,rawFrame = cap.read()
      #print(rawFrame.shape)
    if not isCapturing:
        handelCameraFailException()
    #rawFrame =  cv.resize(rawFrame,(1920//2,1080//2))
    rawFrame = adjustFrame(rawFrame)
    hsv = cv.cvtColor(rawFrame, cv.COLOR_BGR2HSV)
    mask = setMask(hsv,colorsRange) 
    res = getResult(rawFrame,mask)
    
    
    
    countour = calculateContours(mask)
         
    cv.drawContours(rawFrame,countour, -1, (255,0,0), 3)
    coordinates = calulateCentroidContour(countour)   
      
    dinoControl.controller(coordinates)
    
    displayOutputs(hsv,rawFrame,mask,res)     
    key = cv.waitKey(1)
    if key == ord("q"):
        cv.destroyAllWindows()
        cap.release()
        break     
    elif key == ord("s"):
        file = open("colorsRange.txt","w")
        file.write("")
        file.close()
        for i in colorsRange:
            i.saveHsvValues()
    
                  