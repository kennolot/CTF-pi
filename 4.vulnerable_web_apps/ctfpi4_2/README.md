## CTF-pi - Vulnerable flask webapp - 2 - Difficulty: ★★☆☆☆

### Scenario 

You found the debug message, and you have been given the source code for the web `app.py` (in this repository), read over the source code and see if you can find something weak to get further access to the system.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_2` directory.

### Objective

While inside the current directory run from the terminal to start the webapp:

`docker compose up --build -d`

Open up  `app/app.py` and read the source code.

Find the vulnerability and exploit it.

Read the flag.txt.

### **Hints**


Can you figure out what os.popen does?

In the url bar try to enter `http://127.0.0.1:8080/ping?ip=127.0.0.1`

Since it's using terminal to ping, can we reach further than just ping command?

`http://127.0.0.1:8080/ping?ip=127.0.0.1;ls` (notice the ls command), now we also see files on the system, meaning we have terminal access, can you find the flag?

### Cleaning up

When done with the tasks run `docker compose down` to remove the containers and other ctf files.