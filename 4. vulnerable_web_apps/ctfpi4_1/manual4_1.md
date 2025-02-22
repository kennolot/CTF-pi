## Vulnerable flask webapp - 1

### Scenario 

You are auditing the security in a factory, as you got a tour before the audit you that a bunch of screens had some sensor data on them, is it possible to reach that and possibly
find a weakness where ever it is hosted.


### Prerequisites

1x Raspberry Pi powered on. Preferably running Raspberry Pi OS.

Raspi connected to your router via wireless or cable

### Requirements

While inside the current directory run from the console to start the webapp

`docker-compose up --build -d`

### Cleaning up

When done with the tasks run `docker-compose down` to remove the containers and other ctf files

### **Hints**

We can see that the debug mode is enabled, there has to be a way to access it.

`127.0.0.1:8080/`

There might be a subdirectory on the site.
