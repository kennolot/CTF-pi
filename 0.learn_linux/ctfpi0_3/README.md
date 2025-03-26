### CTFPI Docker container

## Scenario

There's this Dockerfile, the task is to understand what it does and how the flag.txt
can be retrieved without modifying the `Dockerfile` itself or looking at `answers`.

The command meant to be used here is very helpful when debugging within the containers.

Interactive shell!

## Prerequisites

Cloned the CTF-pi repository.

Are inside the `ctfpi0_3` directory.

`docker run` command works, Docker is installed.

## Requirements

Do this task on Linux terminal: either remote connection on Raspi or your personal machine.

Find the contents of flag.txt.

## Steps to complete

The Dockerfile is very basic, what should be of interest is the COPY command.

When container is ran all it does is COPY <source host> <destination container>

The first problem with this Dockerfile is that nothing gets built and ran.

So for something to actually happen first thing would be to build it!

```
docker build --tag my-ctfpi-image .
```
`--tag` is to name the image it builds into.
`.` means the directory we are currently in, which contains the Dockerfile.

After running the command and build succeeds:
```
docker run --rm --it my-ctfpi-image bash
```
`--rm` is used when you need the container to be deleted after the task for it is complete.
`--it` when docker run is used with this command it takes you straight inside the container.
`bash` is the shell used inside the container.

Now this commands lands us inside the container with shell access.
Since we saw what the COPY inside Dockerfile did, there's nothing more to do than run:
```
cat /tmp/flag.txt
```
After the flag type `exit` to leave interactive shell.