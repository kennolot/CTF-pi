### Physical Access - Messing with GPIO pins.

## Scenario

I've built a simple codelock prototype, and one day I want to start selling it to the world.
Can you run my code and test if it is secure?

## Prerequisites

Have a remote connection or in any other way a way to access Raspberry Pi's terminal

Cloned the `CTF-pi` onto your Raspberry Pi.

Are currently in the `ctfpi3_4` directory in your raspi's terminal.

Read before you run `sudo python codelock.py`


## Requirements

This challenge is meant to be solved with multimeter, however there are more ways(Steps to complete for further info).

For option one you'll need a Raspberry Pi, a basic multimeter.

For option 2 you'll need a Raspi and a Raspberry Pico, an USB cable and 2 jumper wires F-F.

For option 3 you'll only need the Raspi to run the code on.


## Steps to complete

**Option one:**

Multimeter, the logic of the codelock is flawed, so every correct PIN code input pin that needs to be pressed is in HIGH state(3.3V). 

To put it simply, the codelock expects only the correct input so only the correct pin has it's state set.

It's more comfortable to probe on breadboard but it's not required. 

Now open up a Raspberry Pi pinout like this one: https://cdn.sparkfun.com/assets/learn_tutorials/4/2/4/header_pinout.jpg

We know that only GPIO pins are utilized for codelock, we can also assume special use GPIO pins are not used(green colored pins on pinout). 

Touch with the black multimeter probe the GND(Ground) pin on Raspberry Pi, hold it there.

Keep the pinout open next to you.

With the other, red probe touch each of the suitable GPIO pins until you see a reading of 3.3V on the multimeter, that means the pin is in HIGH state and since the source code uses HIGH states we most probably know that this is one of the correct PIN digits.

So for example when touching GND and GPIO17, we get a reading of 3.3V on multimeter, insert 17 into the terminal of the python program.

HOWEVER!!

You might be seeing multiple "Green" GPIO pins showing 3.3V, that's not a mistake. For example pins 0-8 have pull-ups enabled, this basically means their default state is already HIGH or 3.3V. Pins from 9-27 are by default 0V. Keep this in mind when you think you've found the correct pin but get INCORRECT CODE.

After you found and the terminal says that indeed you've gotten the correct pin it takes a new PIN digit, keep entering digits until the program prints the flag.

If you want to try a new PIN, edit `answers/PIN.txt` with new GPIO pin values.

**Option 2:**

Using the raspberry pico, for this we need 2 jumper wires a pico and a usb cable. 

For the Pico you should write a code. Pick one suitable GPIO on Pico and program it as input pin, when the input reads HIGH or somewhere around 3.3V then notify by blinking an LED etc, that we may have found the correct pin.

Connect the Pico's ground to Pi's ground and start connecting the other jumper wire to Raspi's GPIO ports(basically testing the ports one by one), when the Pico's GPIO reads 3.3V then blink an LED.


**Option 3:**

Since this codelock logic is weak, one can just simply try all the GPIO pin numbers in the terminal, nothing gets reset and there's no timeouts. This is also called brute forcing.

Simply keep the pinout open and input the GPIOx, "x" being the digit.
