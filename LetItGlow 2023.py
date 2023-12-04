#Imports
from machine import Pin
import time

#Pin setup
greenLED = Pin(25, Pin.OUT) #Set GP25 as an output
redLED = Pin(14, Pin.OUT) #Set GP14 as an output
#
#Practice turning on manually
# greenLED.value(0)
# redLED.value(0)


## Program Start ##

for i in range(10):
    
    redLED.value(1)
    time.sleep(0.5)
    
    redLED.value(0)
    time.sleep(0.5)

print("Program finished!")
