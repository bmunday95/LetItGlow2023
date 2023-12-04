#Imports
from machine import Pin
import time

#Set up botton name and GPIO pin no.
#Set the pin as an input and use a pull down

redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

#Set up LED output

redLED = Pin(14, Pin.OUT)

#Set up counter variable
count = 0

##Program Start##

while True:
    
    time.sleep(0.2)
    
    redLED.value(0) #LED off until button pressed
    
    if redButton.value() == 1:
        count = count -1
        redLED.value(1)
        print(count)
        
    if greenButton.value() == 1:
        count = count +1
        redLED.value(1)
        print(count)