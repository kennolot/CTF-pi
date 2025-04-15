## CTF-pi: Scanning a "black box"

### Scenario

Typically an attacker doesn't know what services are run on ports. With the exception of HTTP port 80 or 8080 like we're familiar with, but also port 22 which is SSH etc, manually trying if there's a website running works, but if there are hundreds of services and where only one of them could be vulnerable then it doesn't make sense to do it manually.

This is where a tool called `nmap` comes in. Featuring fully automatic port scanning, not only TCP but also UDP ones. Script scanning, determining the service version...

For this challenge only the machine IP is known `hostname -I`, can you find the vulnerability on this machine.

Note, nmap scan doesn't have to be local, anyone anywhere could run an nmap scan, even on google.com (Try it out)

PS the challenge dockerfile should be ran from Pi itself, but rest of it can be done from any device.

### Prerequisites

Cloned `CTF-pi` on raspi.

Are inside `ctfpi5_1` directory.

`nmap` is installed on whichever system you intend to use to scan with.


### Requirements 

`docker compose up --build -d` and multiple services will start running on raspi.

Run `nmap <hostname -I>` aka place your raspi's IP there to start the scan. Note, you may need to dig deeper than default scan.

Find the weakness, and flag.txt to solve it.

### **Hints**

The port is not well known.

The SSH and FTP and HTTP services(common ports) are misleading for this challenge. Even if you manage to hack your way in, they most likely are a dead end.

Try scanning all the possible ports.

An interesting port with service unknown should be revealed.

Try more nmap capabilities like default NSE scripts, version detection, agressive scan etc.

Now with more details the actual vulnerable application can be identified.

Use the knowledge from `4.vulnerable_web_apps` to find the flag.txt

### Cleaning up

```
docker compose down
```