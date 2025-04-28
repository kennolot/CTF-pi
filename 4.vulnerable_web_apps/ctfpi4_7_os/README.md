## CTF-pi - Weak file hosting 5 - Difficulty: ★★☆☆☆

### Scenario

The hidden directories have now been fixed, let's try for one last time if the website is truly safe this time.

You might have noticed that all the app doesn't really restrict any uploads, we can upload anything we want. Is there a way to exploit that?

There is a source code provided `app/app.py` check it out.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi4_7` directory.

`docker compose` works.

### Objective 

Run on Raspi:

`docker compose up -d`

`hostname -I` and go to http://ip-address from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp

There is a source code provided `app/app.py` check it out.

Write your own `exploit.py`

Find the flag hidden in the file hosting web app.



### **Hints**

Using `subprocess` `ospopen` `os.system` .. in context like this is very very dangerous.

From the source `app.py` it seems that .py files are accepted, we should upload our own and see!

There's a very basic `exploit_example.py` provided, however in real world any python code could be executed, including ransomware, spyware..

### Cleaning up

`docker compose down`