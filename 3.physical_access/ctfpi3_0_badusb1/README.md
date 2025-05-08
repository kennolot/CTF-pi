## CTF-pi - Physical Access - Exploiting open USB ports with our own BadUSB - Difficulty: ★★★☆☆


### Scenario

This time we've found an otherwise inaccessible Raspberry device running in an IoT environment. It was hidden from plain sight and there doesn't seem to be a lot of ways to breach it's security. However we see that the USB ports of the raspi are completely exposed.

We have overheard someone and know that the `flag.txt` is inside the pi home directory.

In this scenario we are building our own BadUSB, a device when plugged into another device(Raspberry Pi in our case) delivers malware, executes malicious commands etc. By the end of this we will see that even a device that is completely offline or otherwise unreachable is still possible to exploit with exposed USB ports.

### Prerequisites

Have a **Raspberry Pico** or equivalent like Arduino etc that can be turned into BadUSB.

Have a data transmitting USB A -> Micro USB(Typically) cable or an adapter.

Have your Raspberry Pi as the victim device.

### Objective

For a video tutorial: https://www.youtube.com/watch?v=ctCmOhoT9po (Guide by Austin's Lab)

When using Raspberry Pico, we need to download https://github.com/dbisu/pico-ducky and follow the instructions provided on this page.

Run the following commands on Raspberry Pi when inside the directory that contains this manual `cp answers/flag.txt ~`, we'll just copy the flag onto home directory for easier access, do not read it as you'll be using BadUSB to read it.

Create your own `payload.dd` for pico & save it there, when plugged into the USB of Raspberry Pi gives you shell access remotely or in any way read the flag.txt in home directory.

### Steps to complete

<details>
<summary>Click me</summary>

After setting up the BadUSB device, we are now ready to write our own simple payload.

Open up a text editor(even Notepad is fine) and name it `payload.dd`.

Into the `payload.dd` we can start writing our malicious script.
I have provided an example in this directory of a working solution, but you are free to experiment on your own

After the payload is written simply make sure the BadUSB is NOT in setup mode and plug it into the USB port of Raspberry Pi, your script should execute on its own.

Docs page for bunch of useful Duckyscript commands: https://docs.hak5.org/hak5-usb-rubber-ducky/duckyscript-tm-quick-reference

Valid solutions could also utilise netcat(`nc`), using `scp` or writing the flag.txt onto the BadUSB storage.

When using the example provided we can see it uses python http.server to display the flag.txt on our local network server.
To view the address the server is at we run `hostname -I` from the Raspberry Pi remote connection ex. 10.10.10.24 so it's at http://10.10.10.24:8000.
We can simply visit local address we have and flag.txt file should be hosted there, containing our answer.

</details>

### Cleaning up

When you are done just delete the flag from the home directory of raspi:
`rm ~/flag.txt` 
