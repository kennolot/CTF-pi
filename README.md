# CTF-pi 🥪🏴‍☠️

UPDATE: Don't have a Raspberry Pi? No worries, now every category of challenges except 3.physical_access can be completed from a Linux computer or Virtual Machine.

**Contains manuals and containers to turn your Raspberry Pi into a local CTF box. WARNING: THIS WILL MAKE YOUR RASPBERRY PI INSECURE!!!**

**Please make a backup, save it somewhere else, and do these challenges on clean device**

**Also since some docker tasks run on local network using vulnerable images, make sure the local network is safe**

| 0                                                                                          | 1                                                                                           | 2                                                                                                  | 3                                                                                              | 4                                                                                                  | 5                                                                                            | 6                                                                                                | 7                                                                                       |
|--------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [grep](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_0_grep)           | [guess](https://github.com/kennolot/CTF-pi/tree/main/1.weak_credentials/ctfpi1_0_guess)     | [basic](https://github.com/kennolot/CTF-pi/tree/main/2.weak_encryption/ctfpi2_0_basic)             | [badusb1](https://github.com/kennolot/CTF-pi/tree/main/3.physical_access/ctfpi3_0_badusb1)     | [source](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_0_source)       | [packet](https://github.com/kennolot/CTF-pi/tree/main/5.networking_problems/ctfpi5_0_packet) | [grafana1](https://github.com/kennolot/CTF-pi/tree/main/6.outdated_software/ctfpi6_0_grafana1)   | [HA](https://github.com/kennolot/CTF-pi/tree/main/7.insecure_api/ctfpi7_0_HA)           |
| [hidden](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_1_hidden)       | [default](https://github.com/kennolot/CTF-pi/tree/main/1.weak_credentials/ctfpi1_1_default) | [multi](https://github.com/kennolot/CTF-pi/tree/main/2.weak_encryption/ctfpi2_1_multi)             | [badusb2](https://github.com/kennolot/CTF-pi/tree/main/3.physical_access/ctfpi3_1_badusb2)     | [debug](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_1_debug)         | [scan](https://github.com/kennolot/CTF-pi/tree/main/5.networking_problems/ctfpi5_1_scan)     | [grafana2](https://github.com/kennolot/CTF-pi/tree/main/6.outdated_software/ctfpi6_1_grafana2)   | [rest](https://github.com/kennolot/CTF-pi/tree/main/7.insecure_api/ctfpi7_1_rest)       |
| [scripting](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_2_scripting) | [login](https://github.com/kennolot/CTF-pi/tree/main/1.weak_credentials/ctfpi1_2_login)     | [mqtt](https://github.com/kennolot/CTF-pi/tree/main/2.weak_encryption/ctfpi2_2_mqtt)               | [special](https://github.com/kennolot/CTF-pi/tree/main/3.physical_access/ctfpi3_2_special)     | [cmd](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_2_cmd)             | [http](https://github.com/kennolot/CTF-pi/tree/main/5.networking_problems/ctfpi5_2_http)     | [fluentbit](https://github.com/kennolot/CTF-pi/tree/main/6.outdated_software/ctfpi6_2_fluentbit) | [shop-extra](https://github.com/kennolot/CTF-pi/tree/main/7.insecure_api/ctfpi7_2_shop) |
| [docker dbg](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_3_dckrdbg)  |                                                                                             | [sidechannel](https://github.com/kennolot/CTF-pi/tree/main/2.weak_encryption/ctfpi2_3_sidechannel) | [uart](https://github.com/kennolot/CTF-pi/tree/main/3.physical_access/ctfpi3_3_uart)           | [files](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_3_files)         |                                                                                              |                                                                                                  |                                                                                         |
| [compose](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_4_compose)     |                                                                                             |                                                                                                    | [gpiolock](https://github.com/kennolot/CTF-pi/tree/main/3.physical_access/ctfpi3_4_gpiolock)   | [directory](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_4_directory) |                                                                                              |                                                                                                  |                                                                                         |
| [transmit](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_5_transmit)   |                                                                                             |                                                                                                    | [brutecode](https://github.com/kennolot/CTF-pi/tree/main/3.physical_access/ctfpi3_5_brutecode) | [msg](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_5_msg)             |                                                                                              |                                                                                                  |                                                                                         |
| [race](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_6_race)           |                                                                                             |                                                                                                    |                                                                                                | [upload](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_6_upload)       |                                                                                              |                                                                                                  |                                                                                         |
| [privesc](https://github.com/kennolot/CTF-pi/tree/main/0.learn_linux/ctfpi0_7_privesc)     |                                                                                             |                                                                                                    |                                                                                                | [os](https://github.com/kennolot/CTF-pi/tree/main/4.vulnerable_web_apps/ctfpi4_7_os)               |                                                                                              |                                                                                                  |                                                                                         |

CTF-pi focuses on teaching users IoT device security by turning their own Raspberry Pi into a vulnerable device.
The goal is to show common misconfigurations and the effect it has on the security.

" The "S" in IoT Stands for "Security" "

## Installing docker & compose for Raspberry Pi

1. Make sure you're connected to the internet.
2. Open the terminal.
3. Follow https://pimylifeup.com/raspberry-pi-docker/

## How to run CTF-pi

1. Clone the repository onto your Raspberry Pi
2. Find a challenge you like and open up it's directory from terminal
3. Read `README.md` for setup and steps to solve
4. Find a hidden flag or solution to complete the challenge
5. (Optional) Tinker around and maybe find weaknesses not covered in the manual
6. After using make sure to stop the containers and remove the CTF files, this can be done either manually or via `docker compose down`

## General guidelines when completing the challenges

For some challenges you will see a folder called 'answers', within is a flag.txt that contains the answer. Some challenges also provide a solution script of some sort. So it's best to look at them when you're stuck or have completed the challenge.

The shell scripts and Dockerfile + compose.yaml are only for building the tasks unless specified otherwise. They might spoil the challenge so be aware of that when looking at them. It is always a good practice to review unknown code though.

## How is CTF-pi different?

The user has no restrictions on how far to exploit the device. After finding the `flag.txt`, there is generally a way to further exploit the device or just tinker around. The user also doesn't have restrictions on what exploits to use, a BadUSB for example can be used to attack a web application, even though it's not talked about in manual.

CTF-pi has more focus towards physical security, where the attacker might already be sitting next to the device or be inside the same network as the IoT device. A few spoilers: BadUSB challenges and sniffing local network traffic.

If needed CTF-pi can be run offline.

## Before starting - do this only for the first time
1. `python3 -m venv /opt/ctfenv` Create a global virtual environment, fixes Docker warning.
2. Add to /home/username/.bashrc at the very end: 
```
if [ -d "/opt/ctfenv" ]; then
    source /opt/ctfenv/bin/activate
fi
```
This checks if directory /opt/ctfenv exists and if it does: activate the virtual environment.
Every time you open a new terminal it starts in this virtual environment.

Note:  When 2. is not done, then the user can just manually start the virtual environment by running:
`source /opt/ctfenv/bin/activate` but this is not automatic and this command has to be entered every new boot up.

When everything went as planned, there should be (ctfenv) before your username@hostname.

## For Raspberry Pi 5 users

There could be some software memory issues(Fluentbit, home assistant challenges), so when `docker compose logs` outputs jemalloc memory issues then most likely you need to change the pagesize from 16K to 4K, in `/boot/firmware/config.txt`.
```
# temporarily enable 4K PAGESIZE
kernel=kernel8.img
```
Make sure to reboot the Raspberry after the change, the pagesize can be reverted by removing this line.

## SSH connection hangs
The issue could be Raspi's WiFi power saving, try disabling it.
Try this command: `sudo iw wlan0 set power_save off`
