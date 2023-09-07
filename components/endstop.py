from machine import Pin

class Endstop:
    def __init__(self, pin, inverse=True):
        self.endstop = Pin(pin, Pin.IN)
        self.inverse = inverse
    def getStatus(self):
        return not self.endstop.value() if self.inverse else self.endstop.value()
            
    