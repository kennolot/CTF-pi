## CTF-pi - Side channel attack

### Scenario

There are times when source code isn't available, all that's provided is the app itself, that all the other users use, AKA a final product.

This can also be utilized for bug bounties or closed source programs. Even on physical CPUs.

For this challenge time based side channel attack will be performed. Basically what's happening in very deep level is that there's a piece of code that checks the input of user and compares it to the real programmed value. 

When the program immediately outputs that the value is incorrect then most likely the very first character the user inputted was already incorrect, thus there is no need read further inputs.

However when the program "thinks" for a little then there's a chance that some input might be correct as the program checks if the input matches the real value.

In real world these delays will be in microseconds or even lower and possibly with noise also. So these attacks will be difficult to perform and find in real world. This challenge simulates a 1 second delay for each character.

We had a hacker breach the Raspberry Pi, even though the malware they spreaded got removed there still might be backdoors left by the attacker. Try to find it.


### Prerequisites

Have cloned `CTF-pi` on Raspberry Pi.

`docker compose` works.

Raspi and main computer within same local network if you wish to do the challenge from other device, not directly on Raspberry Pi.

### Requirements

Find the hacker's C2C server. 

The hacker could have made some mistakes on their own, find the mistake.

Either by hand(will be tedious) or modify the script `sidechannel.py` to try all lowercase character combinations, when it takes longer than usual to load, you might have inputted the correct character, keep appending to it and the loading times will become longer and longer.

The challenge is completed when you gain access to the hacker account.


### **Hints**

Open ports can be scanned with nmap.

The error 404 might be fake.

Use gobuster to find which directory is being used actually.

For GET request Try inputting  `?password=CTF`, you might notice it loading longer, the server processes it, so the inputted string is correct.


For POST requests:
```
curl -X POST http://10.10.10.67:8000/comunicator -F "password"="CTF"
```

`server/app.py` will reveal the backend logic when you're truly stuck on this challenge.


### Cleaning up

```
docker compose down
```

### Role in physical security

Hardware hacker Joe Grand made a good demonstration how this same thing can be applied to hack hardware: https://www.youtube.com/watch?v=2-zQp26nbY8

Side channel attacks are a big topic on their own and can have many ways to be exploited, AMD processors(CVE-2023-20583), Linux kernel(CVE-2021-35477), Texas Instruments digital signal processors OMAP-L138 (CVE-2022-25332). Even though some of these are low severity and difficult to perform in real world, these possibilities should not be overlooked when designing systems.