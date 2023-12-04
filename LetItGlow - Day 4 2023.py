from machine import Pin
import time
import random

#Set up input pins
redButton = Pin(2, Pin.IN, Pin.PULL_DOWN)
greenButton = Pin(3, Pin.IN, Pin.PULL_DOWN)

#Set up LED pins - bar LED
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

#List of LED segments
segment = [seg1, seg2, seg3, seg4, seg5]

#Scanning function
# while True:
#     
#     #For loop to turn each LED on and off in order
#     for led in segment:
#         led.value(1)
#         time.sleep(0.08)
#         led.value(0)
#     
#     #Reverse for loop, runs backward through list
#     for led in reversed (segment):
#         led.value(1)
#         time.sleep(0.08)
#         led.value(0)

# #Random light function
# while True:
#     
#     r = random.randint(0,4)
#     
#     segment[r].value(1)
#     
#     time.sleep(0.1)
#     
#     segment[r].value(0)


#Set initial count for index
count = -1

#Turn off all LEDS to start
seg1.value(0)
seg2.value(0)
seg3.value(0)
seg4.value(0)
seg5.value(0)

while True:
    
    time.sleep(0.01) #short delay to avoid program running too fast
    
    if greenButton.value() == 1:
        
        if count ==4:
            pass
        
        else:
            count = count +1
            segment[count].value(1) #light the LED at index no
            time.sleep(0.2)
    
    if redButton.value() ==1:
        
        if count == -1:
            pass
        
        else:
            segment[count].value(0) #turn off LED at index
            time.sleep(0.2)
            count = count -1