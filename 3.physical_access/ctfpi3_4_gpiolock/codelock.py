# MAKE SURE THIS GPIO LIBRARY MATCHES YOUR MODEL, I USE PI 5
# !!!!
from gpiozero import DigitalOutputDevice
import time

current_step = 0
entered_code = []

# pin numbers marked with GPIOx, the x is the number of the pin (BCM), for example GPIO4 would be 4.
# check the pinout for your model check if they match before running the code.
# The green pins here should be good to use: https://cdn.sparkfun.com/assets/learn_tutorials/4/2/4/header_pinout.jpg
with open("answers/PIN.txt", "r") as PIN:
	PIN = PIN.read().split()

steps = [DigitalOutputDevice(pin) for pin in PIN]

with open("answers/flag.txt", "r") as flag:
	flag = flag.read()


while current_step < len(PIN):
	out_pin = steps[current_step]
	out_pin.on()
	
	while True:
	    inp = input("Enter one PIN code digit: ")
	    if inp == PIN[current_step]:
	        break
	    else:
	        print("Incorrect, Try again: ")

	entered_code.append(inp)
	print("Entered code:", entered_code)
	out_pin.off()
	current_step += 1	

print("** Beep, Beep **")
print("** The door opens **")

print(flag)