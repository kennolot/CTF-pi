## 1_1 webapp with flask

### Scenario 

You are auditing the security in a factory, as you got a tour before the audit you that a bunch of screens had some sensor data on them, is it possible to reach that and possibly
find a weakness where ever it is hosted.

### Requirements

1x RaspBerry Pi
1x RaspBerry Pi Power supply
1x SD-card and Operating System installed (Preferred Raspberry Pi OS)

Raspi connected to your router via wireless or cable
Remote access to Raspi using Raspberry Pi connect, VNC etc.. (to run the docker)

### Prerequisites

Docker and docker-compose.

While inside the current directory run from the console to start the webapp

`docker-compose up --build -d`

### Cleaning up

When done with the tasks run `docker-compose down` to remove the containers and other ctf files

### *Hints*

We can see that the debug mode is enabled, there has to be a way to access it.

`127.0.0.1:8080/`

There might be a subdirectory on the site.
