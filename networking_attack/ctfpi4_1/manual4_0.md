### Plain text network transmission

### Scenario 

While doing your audits you found an open port `1337` broadcasting on a Raspberry pi. You know it's broadcasting because every device inside the network saw data coming to `1337`. Can you figure out what data is being transmitted to all deviced within the network?

### Requirements

1x RaspBerry Pi
1x RaspBerry Pi Power supply
1x SD-card and Operating System installed (Preferred Raspberry Pi OS)

Raspi connected to your router via wireless or cable
Remote access to Raspi using Raspberry Pi connect, VNC etc.. (to run the docker)

Laptop or Desktop PC to be used for scanning the network. With WiFi.

### Prerequisites

Docker and docker-compose.

While inside the current directory and on Pi run from the console:

`docker-compose up --build -d`

Install wireshark onto your laptop/PC

### Cleaning up

When done with the tasks run `docker-compose down` to remove the containers and other ctf files

### ** Hints **

You are free to examine the source code for this challenge.

Since we know it's broadcast, then is it TCP or UDP?

Wireshark filter `udp.port == 1337`

