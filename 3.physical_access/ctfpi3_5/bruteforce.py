# this code is meant for raspberry Pico.
# one option to crack the code:
from machine import Pin
import time

# set the pins you want to use to send signals from Pico.
# connect these pico GPIO pins to the Raspi codelock used pins.
# THESE ARE PICO PINS NOT RASPBERRY PI!! BCM PIN NUMBERING
PICO_PINS = [22, 21, 20, 19, 18, 17]
pins = [Pin(p, Pin.IN) for p in PICO_PINS]


#pin.value(0) AKA send grounding signals only, otherwise
# there's a risk to damage GPIO pins if instead of ground a high voltage is used.
# if you don't feel confident then uncomment the solution(touch_pin) and use it instead.

# this code simulates the manual touching of GPIO pins, but much faster than a human could.
# def touch_pin(pin):
# 	pin.init(Pin.OUT)
# 	pin.value(0) # ground
# 	time.sleep(0.2)
# 	pin.init(Pin.IN) # let go

# def brute_force():    
# 	for pin1 in PICO_PINS:
# 		for pin2 in PICO_PINS:
# 			for pin3 in PICO_PINS:

# 				combo = [pin1, pin2, pin3]
# 				print("Trying combo:", combo)                        
# 				for pin_num in combo:
# 					pin = Pin(pin_num, Pin.OUT)
# 					touch_pin(pin)
# 					time.sleep(0.2)    
brute_force()
print("bruteforcing ended")
