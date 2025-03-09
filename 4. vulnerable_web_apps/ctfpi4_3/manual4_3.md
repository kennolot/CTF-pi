## Weak file hosting 1

### Scenario

One of more common Raspberry Pi projects is a file server, your own "cloud" solution where you can upload files. This is also a good place for bad actors to breach and get access to your files.

This particular application hosts your files locally, so anyone using the same network as the Pi can access the uploaded files.

### Prerequisites

1x Raspberry Pi

### Requirements 

Be inside the current directory.

`docker compose up --build -d`

`hostname -I` and go to http://<ip-address>:8080 from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp

`app.py` is NOT meant to be viewed for solving this challenge

Find the flag hidden in the file hosting web app.


### Cleaning up

`docker compose down`


### **Hints**

View the website's source code, there's a clue hidden there.

The hidden flag directory is guessable, but tools like `gobuster` `dirbuster` etc can be used aswell.

