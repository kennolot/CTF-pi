## CTF-pi - Weak file hosting 1 - Difficulty: ★☆☆☆☆

### Scenario

One of more common Raspberry Pi projects is a file server, your own "cloud" solution where you can upload files. This is also a good place for bad actors to breach and get access to your files.

This particular application hosts your files locally, so anyone using the same network as the Pi can access the uploaded files.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_3` directory.

`docker compose` works.

### Objective 

Run:

`docker compose up --build -d`

`hostname -I` and go to http://<ip-address> from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp.

`app.py` is NOT meant to be viewed for solving this challenge

View the website's source code, there's a clue hidden there.

Find the flag hidden in the file hosting web app.

### **Hints**

The flag is hidden in a directory, other than /uploads or /.

The hidden flag directory is guessable, but tools like `gobuster` `dirbuster` etc can be used aswell.


### Cleaning up

`docker compose down`


