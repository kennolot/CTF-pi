## CTF-pi - Physical Access - Messing with GPIO pins - more complex codelock - Difficulty: ★★★★☆


**WARNING**

Make sure you are absolutely certain that you have connected the proper pins between Pico and Pi.

Ex: 5V into a 3.3V will damage your device. Also 3.3V output into a 0V output will also damage your device, if you are not certain find information online or don't practically do the task at all, reading the code provided will give a good idea aswell.

### Scenario

Okay. Thanks to the previous task findings I made the codelock a-lot more secure, can you find a way to break in now?

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi3_5` directory.

For this we need a Raspberry Pi which acts as the computer behind code lock.

Raspberry Pi pico.

Jumper wires.

USB cable.

Preferrably a breadboard for connections.

### Objective

Read the source code `codelock.py`. Especially which pins are programmed, you'll need to connect these.

Write a brute forcing tool which we use to break into the codelock `bruteforce.py`

Do the proper connections and double check them before running any code.

Make sure Pico's and Pi's Ground pins are connected.

Pico should be connected to your main PC/laptop via USB, and run on Thonny etc.

Once you are certain all is well: `sudo python codelock.py` on your Raspberry Pi, PS you might want to `sudo python codelock.py > result.txt` so instead of printing to terminal everything goes into this .txt file, later you can CTRL+F the flag.

From Thonny run `bruteforce.py` Make sure Pico is selected as the device and hit run.

The brute forcer should try all the PIN combinations.

After a correct PIN is inserted, the imaginary door opens and the flag gets outputted.

### **Hints**

<details>
<summary>Click me</summary>

`bruteforce.py` has a solution already made, it's just commented.

</details>
