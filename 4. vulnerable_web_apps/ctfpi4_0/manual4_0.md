## Vulnerable web app - 1

### Scenario 

You are at your friend's house and notice a Raspberry Pi running, you ask your friend about it and he says it's for automating things around the house, not revealing much details about it, however he says the control panel is password protected and he is using php to verify the users. He wants you to try break into his "control panel" and find a hidden text file within. He opens up his laptop and opens the remote connection to Pi, now it's tme for you to attempt to break into the web application.


### Prerequisites

Raspberry Pi powered on. Preferably running Raspberry Pi OS.

Raspi connected to your router via wireless or cable

Have cloned this repository and are inside the `ctfpi4_0` directory

### Requirements

Run `docker-compose up --build -d`

`hostname -I` and enter one of the IPs there along with the port into your browser on your main machine.

or

Complete it inside your Raspi using VNC, raspi connect, etc.

### Cleaning up

When done with the tasks run `docker-compose down` to remove the containers and other ctf files

### Steps to complete

We enter the IP the web server is running on and since we know it's a web application we can add a port 8080 to access the http web server(make sure you are at http, not https for this challenge).

Now we should be greeted by a password prompt, our friend mentioned something about php, so we should check if we can reach the index.php. For that we can try adding `/index.php?source=1` after the port, so our current query looks something like `http://10.10.10.12:8080/index.php?source=1`. Now we are able to see a source code and see the hardcoded password within, try entering it into the password prompt and we should get the flag.
