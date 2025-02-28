## Weak file hosting 3

### Scenario

Seems like the person patching the security issues is fed up, let's see if the final fixes worked, or can we still find out about their secrets.

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

View the website's source code

View more developer tools like console, maybe something pops out.

