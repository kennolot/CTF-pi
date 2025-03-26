### CTFPI Docker compose

## Scenario

Running a container usually takes multiple commands to type in, usually one for building and other for running. Also when it comes to setting up multiple containers then there's more manual work involved by specifying ports, volumes etc.

Docker compose should automatically be installed with Docker and it shines when it comes to scalability, but for CTFPI it also reduces the need for running multiple commands.

## Prerequisites

Cloned the CTF-pi repository.

Are inside the `ctfpi0_4` directory.

`docker compose version` command works, if not: https://docs.docker.com/compose/install/

## Requirements

Do this task on Linux terminal: either remote connection on Raspi or your personal machine.

Read what's inside Dockerfile and compose.yaml & script.sh

Find a way to run docker compose and find the flag.

## Steps to complete

```
docker compose up --build
```
It prints out the flag.