## Weak file hosting 4

### Scenario

The previous web app developer was notified and is currently fixing their app issues. 

His friend however copied his code and made a few changes, take a peek at `app/app.py` and see what has changed from `ctfpi4_5/app/app.py`.

### Prerequisites

1x Raspberry Pi

### Requirements 

Be inside the current directory.

`docker compose up --build -d`

`hostname -I` and go to http://<ip-address>:8080 from Pi remote connection
or a machine that's connected to the same local network where Pi hosts the webapp

Find the flag hidden in the file hosting web app.


### Cleaning up

`docker compose down`


### **Hints**

Check out the `app/app.py` for source code.

Are user inputs sanitized?

Upload a file named `pwd` for example, in linux terminal this would print the current active directory. What's happening here?

`;` escapes the command.

Answer: `/uploads/test.txt;cd hidden && cd admin && cat flag.txt`