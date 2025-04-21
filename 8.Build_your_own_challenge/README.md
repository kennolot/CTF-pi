## How to build your own Raspberry Pi CTF challenges?

Similar to the ones used in this project.

### Structure

Docker's compose.yaml and Dockerfile are the most efficient way to build challenges.

They do a pretty good job providing isolation from main system but also are easier
to manage than for example a shell script that automates the build.

Utilizing docker is an easy way to connect and do challenges from different device than being forced to do things locally on Raspberry Pi.

Docker also has plenty of already built projects so there's no need to do everything from scratch.
Example CTF-pi 6. and 7. Images like python or alpine Linux.

The usual compose.yaml structure I've used is:

```
services: # group of services, can be multiple
  mqtt-broker: # a single service, can be any name
    image: eclipse-mosquitto:latest # an image, that can be found on docker hub registry.
    container_name: mqtt-broker # optional, name the container
    restart: unless-stopped # also optional but useful, without it a crash would end the #conteiner
    volumes: # from main physical device onto a container's directory.
    	# here we take contents from local filesystem and mount it into container.
      - ./mosquitto/config:/mosquitto/config
    ports: # publishing or mapping, ex host port 1883 gets mapped to container's 1883.
    	# this makes the services accessible outside the container.
      - "1883:1883"
      - "9001:9001"
```

Dockerfile can also be used:

Example from `ctfpi5_0`

```
FROM python:3.13-slim # get python image with version 3.13, slim is lightweight version

WORKDIR /app # set a directory within the container that will get populated

COPY source/broadcast.py . # COPY [source] [dest], in this case copy from local Raspberry #directory to current directory (.), current directory we set /app

COPY answers/flag.txt . # same thing but with flag

RUN chmod 400 flag.txt # similar to linux command, set file permissions.

EXPOSE 1337 # make the port accessible outside the container

CMD ["python", "broadcast.py"] # run this command like you would on linux terminal, broadcast.py #is a custom made script.
```

Example of `broadcast.py`

```
import socket
import time

UDP_IP = "255.255.255.255"
UDP_PORT = 1337

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

with open("flag.txt", "r") as f:
	flag = f.read().strip()


while True:
    message = flag.encode()
    sock.sendto(message, (UDP_IP, UDP_PORT))    
    time.sleep(10)
```

compose.yaml

```
services:
  name:
    build: . # build is Dockerfile, which is currently located in the same directory on Pi # that compose.yaml is, so when docker compose up is ran it builds from Dockerfile
    network_mode: "host" # can also be replaced with ports:, but currently this line does not isolate container network, so container will directly use the host network.
```



### Scalability - for multiplayer

`compose.yaml` has an option to specify a range of ports instead of only a single port.
This ensures each challenger can have a separate container running for them without colliding with others.


