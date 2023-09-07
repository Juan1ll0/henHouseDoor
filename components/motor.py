import libs.stepper as stepper
from machine import Pin

class Motor:
    def __init__(self, in1Pin, in2Pin, in3Pin, in4Pin, lastStep):
        self.fast=stepper.create(Pin(in1Pin,Pin.OUT),Pin(in2Pin,Pin.OUT),Pin(in3Pin,Pin.OUT),Pin(in4Pin,Pin.OUT),delay=1)
        self.slow=stepper.create(Pin(in1Pin,Pin.OUT),Pin(in2Pin,Pin.OUT),Pin(in3Pin,Pin.OUT),Pin(in4Pin,Pin.OUT),delay=3)
        self.speed = "FAST"
        self.step = lastStep
    
    def setSpeed(self, speed):
        self.speed = speed
        
    def moveForward(self, steps):
        if self.speed == "FAST":
            self.fast.step(steps,1)
        else:
            self.slow.step(steps,1)
        self.step += steps
            
    def moveBackward(self, steps):
        if self.speed == "FAST":
            self.fast.step(steps,-1)
        else:
            self.slow.step(steps,-1)
        self.step -= steps
            
    def resetStep(self):
        self.step = 0
        
    def getStep(self):
        return self.step
            
    def stop(self):
        self.fast.reset()
        self.slow.reset()