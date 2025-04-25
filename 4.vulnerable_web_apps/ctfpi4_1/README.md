## CTF-pi - Vulnerable flask webapp - 1 - Difficulty: ★☆☆☆☆

### Scenario 

You are auditing the security in a factory, as you get a tour before the audit you notice that a bunch of screens had some sort of sensor data on them, since all of them looked the same it might be some central application running within the network.

Try to find more details about it.


### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_1` directory.

### Objective

Only read the source code after the challenge is solved.

While inside the current directory run from the console to start the webapp:

`docker compose up -d`

`hostname -I` and find the running webapp.

Find the hidden debug info from webapp.

### **Hints**

We can see that the debug mode is enabled, there has to be a way to access it.

There might be a subdirectory on the site.

### Cleaning up

When done with the tasks run `docker compose down` to remove the containers and other ctf files.