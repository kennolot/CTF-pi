## CTF-pi - Physical Access - Reading from exposed UART pins - Difficulty: ★★★☆☆

### Scenario

You've found a Raspberry Pi seemingly all by itself, you notice it has power and also has a few wires connecting it to another device.

It seems the connections correspond to UART, what could it mean?

Let's see if we can read what's being transmitted.


### Prerequisites

Have a microcontroller like raspberry pico or arduino etc. A way to read UART pins.

Raspberry Pi.

Main computer.

Jumper cables, typically F-F.

USB cable.

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi3_3` directory.

Make sure `python` is installed, also the libraries needed (serial).

### Objective 

Make sure Raspberry Pi (NOT pico) has UART enabled. For that click on top-left on raspberry logo > Preferences > Raspberry Pi Configuration > Interfaces > Enable Serial Port and disable Serial Console. Remember what was there before so we can change these back afterwards. Reboot.

On raspberry Pi: run
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

Make sure the USB is connected between your pico and main computer(Windows etc).

The end result should look something like this: (ignore the bottom GREEN, BLACK, BLUE as they're for debug and not needed for us)

![Alt text](https://cdn.xingosoftware.com/elektor/images/fetch/dpr_1,w_625,h_736,c_fit/https%3A%2F%2Fwww.elektormagazine.com%2Fassets%2Fupload%2Fimg%2Fpublic%2Foriginal%2F210045-013-94-original-figure-13.jpg "Connections")

(Credits to https://datasheets.raspberrypi.com/pico/getting-started-with-pico.pdf for the image)

Now everything needed should be done, run `send_flag.py` on Raspberry Pi.

Onto the actual challenge, for Pico write a code `read_flag.py`  that reads UART data and prints it. We shall uncover the secrets sent to us by Raspberry Pi. Find which baudrate is common and try it, when output is logical then baudrate is probably chosen correctly.


### **Hints**

<details>
<summary>Click me</summary>

When stuck you may read source code from `send_flag.py`.

Check the comment on `send_flag.py`, if you get port errors or don't receive anything at all you may need to change serial port to your own, for Pi 5 it should be `/dev/ttyAMA0`.

If you get stuck there's a solution file in `answers/`

</details>

### Cleaning up

Revert the settings if needed. Disable Serial Port, enable Serial Console, or however it was before.
