from machine import Pin
import time

#Set up switch input pins
dip1 = Pin(6, Pin.IN, Pin.PULL_DOWN)
dip2 = Pin(5, Pin.IN, Pin.PULL_DOWN)
dip3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
dip4 = Pin(3, Pin.IN, Pin.PULL_DOWN)
dip5 = Pin(2, Pin.IN, Pin.PULL_DOWN)

#Set up LED pins - bar LED
seg1 = Pin(13, Pin.OUT)
seg2 = Pin(12, Pin.OUT)
seg3 = Pin(11, Pin.OUT)
seg4 = Pin(10, Pin.OUT)
seg5 = Pin(9, Pin.OUT)

#List of LED segments
segment = [seg1, seg2, seg3, seg4, seg5]

#Function1

def program1():
    
    for led in segment:
        led.value(1)
        time.sleep(0.1)
        led.value(0)

#Function2
        
def program2():
    
    for led in reversed (segment):
        led.value(1)
        time.sleep(0.1)
        led.value(0)

#main program loop
    
while True:
    
    if dip1.value() == 1 or dip2.value() == 1:
        print("Prog 1 running")
        program1()
    
    if dip3.value() == 1 or dip4.value() == 1:
        print("Prog 2 running")
        program2()

    