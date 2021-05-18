import cv2 as cv
import numpy as np 
class hsvSetter:
    
    
    def __init__(self,ID,lowerRange,higherRange):
        self.LValue = 0
        self.UValue = 255
        self.id = ID
        self.hsv = [lowerRange,higherRange]
        
    def updateLHue(self,value):
        self.hsv[0][0] = value
    
        
    def updateUHue(self,value):
        self.hsv[1][0] = value
        
    def updateUSaturation(self,value):
        self.hsv[1][1] = value
        
    def updateLSaturation(self,value):
        self.hsv[0][1] = value
        
    def updateUBrightness(self,value):
        self.hsv[1][2] = value
        
    def updateLBrightness(self,value):
        self.hsv[0][2] = value
        
    def getLHue(self):
        return self.hsv[0][0]
    
        
    def getUHue(self):
        return self.hsv[1][0]
        
    def getUSaturation(self):
        return self.hsv[1][1]
        
    def getLSaturation(self):
        return self.hsv[0][1]      
    def getUBrightness(self):
        return self.hsv[1][2]      
    def getLBrightness(self):
        return self.hsv[0][2]
    def getLowColorRange(self):
        return np.array(self.hsv[0])
    def getHighColorRange(self):
        return np.array(self.hsv[1])

    def setHsvValues(self,resultWindow):
        
       cv.createTrackbar("LHue "+str(self.id), resultWindow,self.getLHue(),255,self.updateLHue)
       cv.createTrackbar("LSaturation "+str(self.id), resultWindow,self.getLSaturation(),255,self.updateLSaturation)
       cv.createTrackbar("LBrightness "+str(self.id), resultWindow,self.getLBrightness(),255,self.updateLBrightness)
       cv.createTrackbar("UHue "+str(self.id), resultWindow,self.getUHue(),255,self.updateUHue)    
       cv.createTrackbar("USaturation "+str(self.id), resultWindow,self.getUSaturation(),255,self.updateUSaturation)    
       cv.createTrackbar("UBrightness "+str(self.id), resultWindow,self.getUBrightness(),255,self.updateUBrightness) 
       
    def saveHsvValues(self):
         file = open("colorsRange.txt","a")
         file.write("ID - " + str(self.id))
         file.write("LOW - " + str(self.hsv[0]))
         file.write("HIGH - " + str(self.hsv[1]))
         file.close()
def adjustFrame(rawFrame):
    #This func adjust the axis of frame 
    fixedFrame = rawFrame
    fixedFrame =  cv.flip(fixedFrame,1)
    fixedFrame = cv.flip(fixedFrame,0)
    return fixedFrame 
        
if __name__ == "__main__":  
    cap = cv.VideoCapture(0)
    colorRange = [hsvSetter(0,[0,0,0],[255,255,255]),hsvSetter(1,[0,0,0],[255,255,255])]
    while True:
        isCapturing,frame = cap.read()
        frame = adjustFrame(frame)
        
        cv.imshow("result0",frame)
        cv.imshow("result1",frame)
        for i in range(len(colorRange)):
            colorRange[i].setHsvValues("result"+str(i))
        # colorRange[0].setHsvValues("result"+str(0))
        # colorRange[1].setHsvValues("result"+str(1))
        
        
        key = cv.waitKey(1)
        if key  == ord("q"):
            
            cv.destroyAllWindows()
            cap.release()
            break
        elif key == ord("s"):
            for i in colorRange:
                i.saveHsvValues()
                
            