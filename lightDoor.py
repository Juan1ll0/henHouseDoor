import machine

class LightDoor:
    def __init__(self, door, lightSensor, lightBreakpoint):
        self.door = door
        self.lightSensor = lightSensor
        self.lightBreakpoint = lightBreakpoint
        if machine.reset_cause() == machine.DEEPSLEEP_RESET:
            print('woke from a deep sleep')
            self.door.setPosition()
        else:
            self.door.reset()
        
    def run(self):      
        currentPosition = self.door.getPosition()
        lux = self.lightSensor.read()
        print("Lux:", lux)
        if lux > self.lightBreakpoint and currentPosition != "TOP":
            self.door.goUp()
        elif lux <= self.lightBreakpoint and currentPosition != "BOTTOM":
            self.door.goDown()