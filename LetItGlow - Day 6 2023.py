import time
from machine import Pin
from neopixel import NeoPixel

#Define the LED pin no () and the number of LEDs (1)
GRBled1 = NeoPixel(Pin(2), 1)
GRBled2 = NeoPixel(Pin(5), 1)

#Define GRB colour variables
white = 240,140,225
red = 0,255,0
green = 255,0,0
blue = 0,0,255
yellow = 255,175,150
orange = 238,223,105
pink = 150,150,200
purple = 40,100,255
iceblue = 150,25,200
unicorn = 175,150,255
bogey = 215,100,0

# #Fill LED with colour variable
# GRBled.fill((unicorn))
# 
# #Write data to the LED
# GRBled.write()

#Define list of colours
colours = [white, red, green, blue, yellow, orange, pink, purple, iceblue, unicorn, bogey]

# while True:
#     
#     for colour in colours:
#         
#         GRBled.fill((colour))
#         
#         GRBled.write()
#         
#         time.sleep(0.2)

# #Fading GRB
# while True:
#     
#     for i in range(255):
#         
#         GRBled.fill((i, 0, 0))
#         
#         GRBled.write()
#         
#         time.sleep(0.005)
#         
#     for i in reversed (range(255)):
#         
#         GRBled.fill((0,i,0))
#         
#         GRBled.write()
#         
#         time.sleep(0.005)

#Light passing

while True:
    
    for i in range(255):
        GRBled1.fill((150,i,200))
        GRBled1.write()
        time.sleep(0.005)
        
    GRBled1.fill((0,0,0))
    GRBled1.write()
    
    for i in reversed (range(255)):
        GRBled2.fill((150,i,200))
        GRBled2.write()
        time.sleep(0.005)
        
    GRBled2.fill((0,0,0))
    GRBled2.write()
    