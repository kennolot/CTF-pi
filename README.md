# 🦴 CTF-pi 🦴

## **WORK IN PROGRESS** 👷

**Contains manuals and containers to turn your Raspberry Pi into a CTF box. WARNING: THIS WILL MAKE YOUR RASPBERRY PI INSECURE!!!**

**Please make a backup and do these challenges on clean device**

CTF-pi focuses on teaching users IoT device security by turning their own Raspberry Pi into a vulnerable device.
The goal is to show common misconfigurations and the effects it has on the security.

## How is CTF-pi different?

The user has no restrictions on how far to exploit the device. After finding the `flag.txt`, there is generally a way to further exploit the device or just tinker around.

CTF-pi has more focus towards physical security, where the attacker might already be sitting next to the device or be inside the same network as the IoT device.

The challenges differ from classic online CTFs by: introducing challenges where the attacker can read data from GPIO pins, have access to USB ports and insert malware.

Introduce challenges with other hardware peripherals like touch screens and code locks for attackers to bypass their security.


## General guidelines when completing the challenges

For some challenges you will see a folder called 'answers', within is a flag.txt that contains the answer. Some challenges also provide a solution of some sort. Both of these should be viewed after completing the challenge.


The shell scripts and Dockerfile + docker-compose.yml are only for building the tasks unless specified otherwise. They might spoil the challenge so be aware of that when looking at them. It is always a good practice to review unknown code.

## How to run CTF-pi

1. Clone the repository onto your Raspberry Pi
2. Find a challenge you like and open up it's directory
3. Run `docker-compose up --build -d` in the directory where Dockerfile is located
4. Read `manualx_x.md` for further setup and steps to solve
5. Find a hidden flag to complete the challenge
6. (Optional) Tinker around and maybe find weaknesses not covered in the manual

7. After using make sure to stop the containers and remove the CTF files, this can be done either manually or via `docker-compose down`
