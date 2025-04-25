## CTF-pi - Weak file hosting 2 - Difficulty: ★☆☆☆☆

### Scenario

The web app code got updated, trying /admin directory doesn't work anymore, so the app isn't vulnerable any more right?

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_4` directory.

`docker compose` works.


### Objective

Run on Raspberry Pi:

`docker compose up -d`

`hostname -I` and go to http://ip-address from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp.

`app.py` is NOT meant to be viewed for solving this challenge

Find the flag hidden in the file hosting web app.



### **Hints**

View the website's source code, there's a clue hidden there.

The hidden flag directory can be found using tools like: `gobuster` `dirbuster` etc.

It is not easily guessable and the tool might take some time to find the hidden dir.

### Cleaning up

`docker compose down`