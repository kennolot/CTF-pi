## CTF-pi - Docker privilege escalation


### Scenario

Throughout the challenges Docker will be used plenty of times. Docker makes building the challenges easier, provides an isolated environment to run software on. 

However Docker itself by default introduces a few new security risks.

One major problem being that Docker runs as root by default. When you `-it` inside the container you will see that the user is root. 

Now a Raspberry Pi specific problem is that by default the user created has sudo rights without a password, so Raspberry Pi is basically also privileged.

Now if someone managed to breach the application running inside the container, they would still have access only inside that container as root, not the real system. However, with few configurations on the host system side an attacker could move from "isolated" container onto your main host system. That's very bad.

For this challenge a flag has been hidden on the host machine, the flag has to be read from within the container. Before I mentioned Docker being isolated, it's time to break it.

### Prerequisites

Cloned `CTF-pi` on Raspberry Pi

Are in `ctfpi7_0` directory.

Docker is installed and works.

### Objective

Find the flag on host system under `/answers/flag.txt` from the Docker container.

Use any means necessary. There will be multiple solutions.

### **Hints**

https://gtfobins.github.io/gtfobins/docker/

Docker compose is not needed here specifically, but can also be used.

The simplest approach is to mount a sensitive directory, in this challenge `/answers/flag.txt`, in real world this could be `/` or `/etc` directory which will reveal sensitive host details.

`docker run -v /:/mnt --rm -it alpine chroot /mnt sh`


### Cleaning up

When within Docker interactive shell: `exit`.

Run `docker ps` and you should see no containers running.

If there's somehow a container running `docker stop <container_id>`, make sure `docker ps` doesn't output that something is running.