## CTF-pi - Searching the logs - 1 - Difficulty: ★☆☆☆☆

### Scenario

You are put into the attacker's shoes, you have gained access either remotely or physically to a security flawed IoT device. Unfortunately for the attacker the device is running in low privilege
mode and there's not a lot we can do currently. However we notice a strange folder we have access to called "device_logs" maybe it's worth looking into that?

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_0` directory.

### Objective

Preferrably do this on Raspberry Pi remote connection.

Open the `device_logs` folder and you will see bunch of gibberish.

Using linux terminal commands like `ls`, `cat`, `grep` or `find`, try to find "user" logs.

The flag is hidden somewhere in the .txt files in `device_logs`.

The flag is in the format of CTFPI{..}

Reminder, the `answers` directory contains the real answer, it should be viewed only when the flag is found properly to see if you've found the correct flag.

### **Hints**

Seems like there are a lot of logs and random junk folders to be searching manually. Use `grep` or `find` 

Since we want to get further access to the device we might want to look for credentials. Or logs where some "user" is trying to log in.

`grep -rw './device_logs' -e 'user'`