# MAKE SURE THIS GPIO LIBRARY MATCHES YOUR MODEL, I USE PI 5
# !!!!
from gpiozero import Button
from signal import pause
import time

# pin numbers marked with GPIOx, the x is the number of the pin (BCM), for example GPIO4 would be 4.
# check the pinout for your model check if they match before running the code.
# The green pins here should be good to use: https://cdn.sparkfun.com/assets/learn_tutorials/4/2/4/header_pinout.jpg
buttons = [4, 17, 27, 22, 5, 6]
buttons = {pin: Button(pin, pull_up=True) for pin in buttons}
# list where we remember "digits"
entered_digits = []

with open("answers/PIN.txt", "r") as PIN:
	PIN = int(PIN.read().strip())

with open("answers/flag.txt", "r") as flag:
	flag = flag.read().strip()

def pressed(pin):
    global entered_digits

    # for debounce we only register the same digit once
    if len(entered_digits) == 0 or entered_digits[-1] != pin:
        entered_digits.append(pin)
        print(f"Detected pin {pin}, code entered so far: {entered_digits}")

        # PIN code length is 3.
        if len(entered_digits) >= 3:
            print(f"Full code entered: {entered_digits}")
            print("**Beep, Beep**")

            # check if entered PIN code is correct
            entered_digits = int(''.join(map(str, entered_digits)))
            if entered_digits == PIN:
            	print("Door opens! Come on in!")
            	print(flag)
            else:
            	print("INCORRECT PIN CODE!")

            # reset entered code finally
            entered_digits = []
            #time.sleep(1)

for pin, button in buttons.items():
    button.when_pressed = lambda b=pin: pressed(b)

print("Touch pins with GND wire to enter code...")
pause()  # wait forever (until CTRL+C)