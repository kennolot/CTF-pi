## CTF-pi - Docker compose - Difficulty: ★☆☆☆☆

### Scenario

Running a container usually takes multiple commands to type in, usually one for building and other for running. Also when it comes to setting up multiple containers then there's more manual work involved by specifying ports, volumes etc.

Docker compose should automatically be installed with Docker and it really shines when it comes to scalability, but for CTF-pi it also reduces the need for running multiple commands or specifying too many options.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_4` directory.

`docker compose version` command works, if not: https://docs.docker.com/compose/install/

### Objective

Do this task on Linux terminal: remote connection on Raspberry Pi.

Read what's inside `Dockerfile` and `compose.yaml` and `script.sh`

Find a way to run docker compose and find the flag.

### Steps to complete

```
docker compose up --build
```
It prints out the flag.