import numpy as np
from pynput import keyboard

class Dino:
    def __init__(self,maxX,maxY):
        self.triggerGapRatio = [3,1,3] # 2:1:2
        self.triggerAreaTop = (maxY * self.triggerGapRatio[0]/ np.sum(self.triggerGapRatio))
        self.noTriggerArea = (maxY * self.triggerGapRatio[1]/ np.sum(self.triggerGapRatio))
        self.triggerAreaBottom = self.triggerAreaTop + self.noTriggerArea
        self.keyboardController = keyboard.Controller()
        self.isJumpable = True
        print(maxX)
        print(maxY)
    def controller(self,coordinates):
        if coordinates != None:
            if coordinates[1] > self.triggerAreaTop and coordinates[1] < self.triggerAreaBottom :
                self.isJumpable = True
                self.keyboardController.release(keyboard.Key.down)
                print("neutral")
            elif coordinates[1] < self.triggerAreaTop and self.isJumpable:
                
                print("Jumped")
                self.keyboardController.press(keyboard.Key.space)
                self.keyboardController.release(keyboard.Key.space)
                self.isJumpable = False
            elif  coordinates[1] > self.triggerAreaBottom and self.isJumpable:
                self.keyboardController.press(keyboard.Key.down)
                self.isJumpable = False
                print("down")
                
    
            
             
      
        