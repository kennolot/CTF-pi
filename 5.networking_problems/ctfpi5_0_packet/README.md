## CTF-pi - Famous packet - Difficulty: ★☆☆☆☆

### Scenario 

While doing your audits you found an open port `1337` broadcasting on a Raspberry pi. You know it's broadcasting because every device inside the network saw data coming to `1337`. Can you figure out what data is being transmitted to all devices within the network?

### Prerequisites

Install wireshark onto your main computer.

!! Make sure your main computer is on the same network as the Raspberry !!

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi5_0` directory.

`docker compose` works.

### Objective

While inside the current directory and on Pi run from the console:

`docker compose up -d`

Source code is not needed, all the info needed is that local network is used and port 1337.

Using wireshark, find the proper interface which receives data and filter by port.

Read the packet's message.


### **Hints**

<details>
<summary>Click me</summary>

You are free to examine the source code for this challenge when stuck.

Since we know it's broadcast, then is it TCP or UDP?

Wireshark filter `udp.port == 1337`

</details>

### Cleaning up

When done with the tasks run `docker compose down` to remove the containers and other ctf files.
