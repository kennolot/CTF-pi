## CTF-pi - Weak credentials - Default configuration - Difficulty: ★☆☆☆☆

### Scenario 

A developer set up `redis` to help manage user sessions on the Raspberry Pi custom application.

The configuration is bery basic, redis is set to run on default port and everything else hasn't been changed.

Now you, the attacker found out about it, can you find a way to retrieve data from redis backend?


### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi1_1` directory.

Docker is installed and working.

`docker compose version` outputs a version, meaning docker compose works.


### Objective

To keep the challenge more difficult do not read `compose.yaml` and `init.sh`. After completion you may freely check them out.

Run: `docker compose up -d` on Raspberry Pi.

`hostname -I` to find out the IP, where redis is running on, usually it's the first IP.

Also find the default redis port.

Do this task on Raspberry Pi, over a remote connection.

Find the default login and a way to retrieve the hidden flag from redis.

### **Hints**

Do we even need a username or password?

`hostname -I` to find out the IP.

`redis-cli -h <ip>`

Make sure `redis-cli` is installed

`keys *` to retrieve all set keys

`get <key>`

`quit` to leave redis-cli

### Cleaning up

Run:
```
docker compose down
```