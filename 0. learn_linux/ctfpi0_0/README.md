## Searching the logs - 1

### Scenario

Now you are put into the attacker's shoes, you have gained access either remotely or physically to a security flawed IoT device. Unfortunately for the attacker the device is running in low privilege
mode and there's not a lot of things we can do currently. However we notice a strange folder we have access to called "device_logs" maybe it's worth looking into that?

### Prerequisites

Can be done from your main machine, or on your Pi.

Have cloned this repository and are inside the `ctfpi0_0` directory


### Requirements

Open the `device_logs` folder and you will see bunch of gibberish.

### Completion

Check out the folder `answers/` and see if the flag.txt matches your findings.

### **Hints**

Seems like there are a lot of logs and random junk folders to be searching manually, maybe we can user linux terminal commands for this?

Since we wan't to get further access to the device we might want to look for credentials

Maybe log ins are logged on the device_logs