# CTF-pi

## **WORK IN PROGRESS**

**Contains manuals and containers to turn your RaspBerry PI into a CTF box. WARNING: THIS WILL MAKE YOUR RASPBERRY PI INSECURE!!!**

CTF-pi focuses on teaching users IoT device security by turning their own RaspBerry Pi into a vulnerable device.
The goal is to show common misconfigurations and the effects it has on the security.

## How is CTF-pi different?

CTF-pi has more focus towards physical security, where the attacker might already be sitting next to the device or be inside the same network as the IoT device.
The challenges differ from classic online CTFs by: introducing challenges where the attacker can read data from GPIO pins, have access to USB ports and insert malware.
Introduce challenges with other hardware peripherals like touch screens and code locks for attackers to bypass their security.


## How to run CTF-pi

1. Clone the repository onto your Raspberry Pi
2. Find a challenge you like and open up it's directory
3. Run `docker-compose up --build -d` at the directory where Dockerfile is located
4. Read `manualx_x.md` for further setup and steps to solve
5. Find a hidden flag to complete the challenge

6. After using make sure to stop the containers and remove the CTF files if they are no longer necessary, can be done either manually or via `docker-compose down`