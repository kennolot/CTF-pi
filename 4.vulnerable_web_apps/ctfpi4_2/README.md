## Vulnerable flask webapp - 2

### Scenario 

You found the debug message, and you have been given the source code for the web `app.py` (in this repository), read over the source code and see if you can find something weak to get further access to the system.

### Prerequisites

Raspberry Pi powered on. Preferably running Raspberry Pi OS

Raspi connected to your router via wireless or cable

### Requirements

While inside the current directory run from the console to start the webapp

`docker compose up --build -d`

### Cleaning up

When done with the tasks run `docker compose down` to remove the containers and other ctf files

### **Hints**

Open up the app.py in this directory. There's an interesting comment left behind

Can you figure out what os.popen does?

In the url bar try to enter `http://127.0.0.1:8080/ping?ip=127.0.0.1`

Since it's using terminal to ping, can we reach further than just ping command?

`http://127.0.0.1:8080/ping?ip=127.0.0.1;ls` (notice the ls command), now we also see files on the system, meaning we have terminal access, can you find the flag?

