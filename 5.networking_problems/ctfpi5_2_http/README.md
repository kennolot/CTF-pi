## CTF-pi - plaintext traffic - Difficulty: ★★★☆☆

### Scenario

For this one you're in attacker's shoes again. You have already gained a remote desktop connection to the machine, but there's not much to do. However when scanning ports there's something interesting that comes up, find it yourself!

You've probably found a php login page, which is using HTTP.

Is HTTP secure for a login page? Probably not since everything transmitted is in plaintext.
Now you the attacker get a brilliant idea: listen in on the traffic that's being sent.

This way if we wait long enough we might find admin level credentials.


FOR MAXIMUM REALISM: edit the `backdoor.py` script so it captures the credentials and also sends it to you own machine. Real world attackers will generally use this approach to harvest your sensitive data.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi5_2` directory.

`docker compose` works.

`python` is installed.

### Objective

Run `docker compose up -d` this starts the login page.

First: go to `hostname -I` outputted IP address from your main machine `http://10.10.10.67/` using your browser.

P.S make sure Raspi and your main PC are on the same network, the login page is running only locally.

Open up wireshark find the correct interface(the one you currently use, data is being sent) and capture the packets on it. There will be too much going on, add a filter `http.request.method == "POST"` at first it's probably empty.

Now enter in some dummy data on the login page and click "Login", you will get the Login failed message. 

Check wireshark, now there's a packet outputted there, find `HTML Form URL Encoded`. What do you see? The login credentials that just got inputted!

Secondly: Remember, you have "remote connection" available, you can issue commands to the terminal itself. Open up the same website from Raspi, curl can also be used for pure terminal experience. 

Before logging in with dummy data first install `tcpdump` and then run it with `sudo tcpdump -i any -A 'tcp port 80'`.

Log in using dummy data from Raspi. Same as before, the username and password are readable.

Now for the main challenge: Run `python login_simulation.py` as the name suggest it simulates users trying to log in real time. Your task task is to capture the most important credentials, the admin ones. And get access to the admin account.

For extra challenge try creating `backdoor.py` which reads the credentials from the victim machine(Pi in this case) and sends it over to your main machine, so building a backdoor that the victim user doesn't even know that they're spied on.

### **Hints**

<details>
<summary>Click me</summary>

When capturing with tcpdump `| grep username` can be used for less messy output.

</details>

### Cleaning up

Run in Raspberry Pi's terminal.
```
docker compose down
```
