# this code is meant for raspberry Pico.
# one option to crack the code:
from machine import Pin
from itertools import product
import time

# set the pins used by codelock
TARGET_PINS = [4, 17, 27, 22, 5, 6]
pins = [Pin(p, Pin.IN) for p in TARGET_PINS]


#pin.value(0) AKA send grounding signals only, otherwise
# there's a risk to damage GPIO pins if instead of ground a high voltage is used.
# if you don't feel confident then uncomment the solution(touch_pin) and use it instead.

# this code simulates the manual touching of GPIO pins, but much faster than a human could.
def touch_pin(pin):
    pin.init(Pin.OUT)
    pin.value(0) # ground
    time.sleep(0.1)
    pin.init(Pin.IN) # let go

def brute_force():    
    for combo in product(TARGET_PINS, repeat=CODE_LENGTH):
        print("Trying combo:", combo)
        for pin_num in combo:
            pin = Pin(pin_num, Pin.OUT)
            touch_pin(pin)
            time.sleep(0.1)        
brute_force()