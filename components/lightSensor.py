from machine import Pin, I2C
from libs.bh1750 import BH1750

class LightSensor:
    def __init__(self, sclPin, sdaPin):
        scl = Pin(sclPin)
        sda = Pin(sdaPin)
        i2c = I2C(scl,sda)
        self.sensor = BH1750(i2c)
        
    def read(self):
        return self.sensor.luminance(BH1750.CONT_LOWRES)