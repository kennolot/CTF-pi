## Weak file hosting 2

### Scenario

The web app code got updated, trying /admin directory doesn't work anymore, so the app isn't vulnerable any more right?

### Prerequisites

1x Raspberry Pi

### Requirements 

Be inside the current directory.

`docker-compose up --build -d`

`hostname -I` and go to http://<ip-address>:8080 from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp

`app.py` is NOT meant to be viewed for solving this challenge

Find the flag hidden in the file hosting web app.


### Cleaning up

`docker-compose down`


### **Hints**

View the website's source code, there's a clue hidden there.

The hidden flag directory can be found using tools like: `gobuster` `dirbuster` etc.

It is not easily guessable and the tool might take some time to find the hidden dir.

