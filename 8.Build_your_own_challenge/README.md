## How to build your own Raspberry Pi CTF challenges?

Similar to the ones used in this project.

### Structure

Docker's compose.yaml and Dockerfile are the most efficient way to build challenges.

They do a pretty good job providing isolation from main system but also are easier
to manage than for example a shell script that automates the build.

Utilizing docker is an easy way to connect and do challenges from different device than being forced to do things locally on Raspberry Pi.

Docker also has plenty of already built projects so there's no need to do everything from scratch.
Example CTF-pi 6. and 7. Images like python or alpine Linux.

The usual `compose.yaml` structure I've used is:

```
# group of services, can be multiple
services:
  mqtt-broker: # a single service, can be any name
    # an image, that can be found on docker hub registry.
    image: eclipse-mosquitto:latest
    container_name: mqtt-broker # optional, name the container
    # also optional but useful, container can only be stopped by user developer, crash or anything else will cause it to restart
    restart: unless-stopped
    volumes:
      # from main physical device onto a container's directory.
    	# here we take contents from local filesystem and mount it into container.
      - ./mosquitto/config:/mosquitto/config
    ports: 
    # publishing or mapping, Ex: host port 1883 gets mapped to container's 1883.
    # this makes the services accessible outside the container.
      - "1883:1883"
      - "9001:9001"
```

Dockerfile can also be used:

Example from `ctfpi5_0`

```
# get python image with version 3.13, slim is lightweight version
FROM python:3.13-slim 

WORKDIR /app # set a directory within the container that will get populated

# COPY [source] [dest], in this case copy from local Raspberry 
# directory to current directory (.), current directory we set /app
COPY source/broadcast.py . 

COPY answers/flag.txt . # same thing but with flag

# similar to linux command, set file permissions.
RUN chmod 400 flag.txt 

EXPOSE 1337 # make the port accessible outside the container

# run this command like you would on linux terminal, broadcast.py is a custom made script.
CMD ["python", "broadcast.py"] 
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

`compose.yaml`

```
services:
  name:
    # build is Dockerfile, which is currently located in the same directory on Pi that compose.yaml is, so when docker compose up is ran it builds from Dockerfile
    build: . 
    # can also be replaced with ports:, but currently this line does not isolate container network, so container will directly use the host network.
    network_mode: "host" 
```

For more examples feel free to check out the challange source codes.

This directory also contains a sample structure of what a typical challenge environment will look like.

`README.md` will automatically get displayed in GitHub if a directory containing it is opened. So for CTF-pi all the manuals are written in file `README.md`. Md stands for markdown and is a simple way to format documents.