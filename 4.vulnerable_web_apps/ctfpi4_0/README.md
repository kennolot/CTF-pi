## CTF-pi - Vulnerable web app - 1 - Difficulty: ★☆☆☆☆

### Scenario 

You are at your friend's house and notice a Raspberry Pi running, you ask your friend about it and he says it's for automating things around the house, not revealing much details about it, however he says the control panel is password protected and he is using php to verify the users. He wants you to try break into his "control panel" and find a hidden text file within. He opens up his laptop and opens the remote connection to Pi, now it's time for you to attempt to break into the web application.


### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_0` directory.

`docker compose` works.

### Objective

Run `docker compose up --build -d` on Raspberry Pi.

`hostname -I` and enter one of the IPs there into your browser on your main machine(make sure Raspi and main PC are in the same network).

or

Complete it inside your Raspi using Raspberry Pi Connect, VNC, etc.

Find the admin's password from the vulnerable php login page.

### Cleaning up

When done with the tasks run `docker compose down` to remove the containers and other ctf files.

### Steps to complete

We enter the IP the web server is running on and since we know it's a web application we can add a port 80, but this is not required as by default port 80 is used to access the http website(make sure you are at http, not https for this challenge).

Now we should be greeted by a password prompt, our friend mentioned something about php, so we should check if we can reach the index.php. For that we can try adding `/index.php?source=1` after the port, so our current query looks something like `http://10.10.10.12:80/index.php?source=1`. Now we are able to see a source code and see the hardcoded password within, try entering it into the password prompt and we should get the flag.
