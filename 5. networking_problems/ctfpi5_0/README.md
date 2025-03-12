## Plain text network transmission

### Scenario 

While doing your audits you found an open port `1337` broadcasting on a Raspberry pi. You know it's broadcasting because every device inside the network saw data coming to `1337`. Can you figure out what data is being transmitted to all devices within the network?

### Prerequisites

Raspberry Pi powered on. Preferably running Raspberry Pi OS.

Raspi connected to your router via wireless or cable

Laptop or Desktop PC to be used for scanning the network.

Install wireshark onto your laptop/PC

!! Make sure you are on the same interface as the Raspberry. If Raspberry is connected to WiFi, then should your host machine too !!

### Requirements

While inside the current directory and on Pi run from the console:

`docker compose up --build -d`


### Cleaning up

When done with the tasks run `docker compose down` to remove the containers and other ctf files

### **Hints**

You are free to examine the source code for this challenge.

Since we know it's broadcast, then is it TCP or UDP?

Wireshark filter `udp.port == 1337`

