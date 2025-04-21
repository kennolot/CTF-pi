## CTF-pi - Weak file hosting 4 - Difficulty: ★★☆☆☆

### Scenario

The previous web app developer was notified and is currently fixing their app issues. 

His friend however copied his code and made a few changes, take a peek at `app/app.py` and see what has changed from `ctfpi4_5/app/app.py`.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_6` directory.

`docker compose` works.

### Objective 

Run on Raspberry Pi:

`docker compose up --build -d`

`hostname -I` and go to http://<ip-address> from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp.

Check out the `app/app.py` for source code.

Find the flag hidden in the file hosting web app.

### **Hints**


Are user inputs sanitized?

Upload a file named `test.txt` for example.

`;` escapes the command.

Answer: `/uploads/test.txt;cd hidden && cd admin && cat flag.txt`


### Cleaning up

`docker compose down`