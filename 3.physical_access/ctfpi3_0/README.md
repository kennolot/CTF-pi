### Physical Access - Reading from exposed UART pins.

## Scenario

You've found a Raspberry Pi seemingly all by itself, you notice it has power and also has a few wires connecting it to another device.

It seems the connections correspond to UART, what could it mean?

Let's see if we can read what's being transmitted.


## Prerequisites

Have a microcontroller like raspberry pico or arduino etc. A way to read GPIO pins.

Raspberry Pi.

Main computer.

Jumper cables, typically F-F.

USB cable.

## Requirements 

Make sure Raspberry Pi (NOT pico) has UART enabled. For that click on top-left on raspberry logo > Preferences > Raspberry Pi Configuration > Interfaces > Enable Serial Port and disable Serial Console. Remember what was there before so we can change these back afterwards. Reboot.

On raspberry Pi run
```
pip install pyserial
```

Install Thonny onto your main machine(Windows etc): https://thonny.org/

Raspberry Pi Pico:

We will be installing micropython on it, so everything currently on pico probably gets wiped and replaced.

https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/3

Complete what's said on this page, also at the bottom click Continue, and try if LED blink works. If there's an error about package not existing then: https://projects.raspberrypi.org/en/projects/introduction-to-the-pico/4


After everything mentioned above is working and verified, you may connect the wires.

https://timhanewich.medium.com/using-uart-between-a-raspberry-pi-pico-and-raspberry-pi-3b-raspbian-71095d1b259f

Find the correct pinouts on Raspberry Pi and Raspberry Pi Pico for UART, REMEMBER: Rx and Tx should cross, meaning Pico's Tx goes to Pi's Rx, and Pi's Tx goes to Pico's Rx.

On pinout these are generally marked as UARTx, 'x' being a number.

For this challenge both Rx and Tx aren't necessary, since we only want to see what Pi is sending out. AKA Pi's Tx should connect to Pico's Rx and that's it.

We need a ground wire too, connect GND from Raspberry Pi to GND on Raspberry Pi Pico.

Now everything needed should be done, run `send_flag.py` on Raspberry Pi.


## Steps to solve

Onto the actual challenge, for Pico write a code `read_flag.py`  that reads UART data and prints it. We shall uncover the secrets sent to us by Raspberry Pi.

Check the source code from `send_flag.py` and try to read the flag.

Check the comment, if you get port errors or don't receive anything at all you may need to change serial port to your own.

If you get stuck there's a solution file in `answers/`


## Cleaning up

Revert the settings if needed. Disable Serial Port, enable Serial Console, or however it was before.