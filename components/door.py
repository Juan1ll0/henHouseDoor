## Positions
# OVERTOP. Over top endstop -- NOT POSIBLE WITH ONLY TWO ENDSTOPS
# TOP. On top endstop
# NEARTOP. Under top endstop but inside near top %
# MIDDLE. Out of near zones.
# NEARBOTTOM. Over bottom endstop but inside near bottom %
# BOTTOM. On bottom endstop
# UNDERBOTTOM. Under bottom endstop
# UNKNOWN. On start device.

from libs.fs import WriteJsonFile, UpdateJsonFile

class Door:
    def __init__(self, motor, topEndstop, bottomEndstop, nearTop, nearBottom, overBottom, dimension=0):
        self.motor = motor
        self.topEndstop = topEndstop
        self.bottomEndstop = bottomEndstop
        self.nearTop = nearTop
        self.nearBottom = nearBottom
        self.overBottom = overBottom
        self.position = "UNKNOWN"
        self.dimension = dimension
        if self.dimension != 0:
            self.initialized = True
        else:
            self.initialized = False
        
    def setPosition(self):
        if self.initialized:
            if self.bottomEndstop.getStatus():
                self.position = "BOTTOM"
            elif self.topEndstop.getStatus():
                self.position = "TOP"
            elif self.nearTop > self.motor.getStep():
                self.position = "NEARTOP"
            elif (self.dimension - self.nearBottom) < self.motor.getStep():
                self.position = "NEARBOTTOM"
            elif self.dimension < self.motor.getStep():
                self.position = "OVERBOTTOM"
            else:
                self.position = "MIDDLE"
        else:
            if self.bottomEndstop.getStatus():
                self.position = "BOTTOM"
            elif self.topEndstop.getStatus():
                self.position = "TOP"
            else:
                self.position = "UNKNOWN"
        
    def goUp(self):
        print("Goup")
        while self.position != "TOP":
            self.motor.moveBackward(1)
            self.setPosition()
            if self.position == "NEARTOP":
                self.motor.setSpeed("SLOW")
        self.motor.setSpeed("FAST")
        UpdateJsonFile("state.json", "lastStep", self.motor.getStep())
        #self.motor.stop()
        
    def goDown(self):
        print("GoDown")
        while self.position != "BOTTOM":
            self.motor.moveForward(1)
            self.setPosition()
            if self.position == "NEARBOTTOM":
                self.motor.setSpeed("SLOW")
        # Complete close
        self.motor.moveForward(self.overBottom)
        self.motor.setSpeed("FAST")
        UpdateJsonFile("state.json", "lastStep", self.motor.getStep())
        #self.motor.stop()
                
    def getPosition(self):
        return self.position
        
    def reset(self):
        print("Reset", self.position)

        # go up to find first endstop
        while self.position != "TOP":
            self.motor.moveBackward(1)
            self.setPosition()
            if self.position == "TOP":
                self.motor.resetStep()

        # go down to find first endstop
        while self.position != "BOTTOM":
            self.motor.moveForward(1)
            self.setPosition()
            
            if self.position == "BOTTOM":
                self.dimension = self.motor.getStep()
                
        self.motor.setSpeed("FAST")
        self.initialized = True
        WriteJsonFile("state.json", {"dimension": self.dimension, "lastStep": self.motor.getStep()})