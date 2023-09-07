from utime import sleep_ms
from components.motor import Motor
from components.endstop import Endstop
from components.lightSensor import LightSensor
from components.door import Door
from lightDoor import LightDoor
from libs.fs import ReadJsonFile
from libs.power import DeepSleep


# Setup sleep time
time_sliping_ms = 10000

# Default config
lightBreakpoint = 200
nearTop = 100
nearBottom = 100
overBottom = 30

# Load config from config file
config = ReadJsonFile("config.json")
if config != None:
    lightBreakpoint = config.get("lightBreakpoint")
    nearTop = config.get("nearTop")
    nearBottom = config.get("nearBottom")
    overBottom = config.get("overBottom")

# State
dimension=0
lastStep=0
lastState = ReadJsonFile("state.json")
if lastState != None:
    dimension = lastState.get("dimension")
    lastStep = lastState.get("lastStep")
    
# Create devices
motor = Motor(0,2,15,13, lastStep)
topEndstop = Endstop(14)
bottomEndstop = Endstop(12)
lightSensor= LightSensor(5,4)
door=Door(motor, topEndstop, bottomEndstop, nearTop, nearBottom, overBottom, dimension)
lightDoor=LightDoor(door, lightSensor, lightBreakpoint)
    
# Execute program
lightDoor.run()
sleep_ms(500)
DeepSleep(time_sliping_ms)
    
     











