## CTF-pi - Docker compose 2 - Send & Receive - Difficulty: ★★☆☆☆

### Scenario

Now it's time to run two containers, one for sending data, other for reading data sent by first container.

This challenge will be more interactive as the receiver part is missing.

It is your task to implement it. NOTE! No need to change Dockerfile or compose.yaml, only change `receiver/receive_flag.py` file.

Depending on how you write the solution we might have introduced something called Race condition into our code, so if you get odd errors or results, check `ctfpi0_6`.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_5` directory.

`docker compose version` command works, if not: https://docs.docker.com/compose/install/
If the command shows the version info then docker compose is installed properly.

`python --version` command works, python is installed.

### Objective

Do this task with remote connection on Raspberry Pi.

Read what's inside `Dockerfiles` and `compose.yaml` and `sender/send_flag.py`.

Complete `receiver/receive_flag.py`: read and decode the content from `/app/answers/flag_encoded.txt`.

Print the flag from `receive_flag.py`.

Check if your code works:
```
docker compose up --build
```

The solution is correct if receiver can print out the encoded flag(created by `sender/send_flag.py`) in human readable form.

CTRL+C to terminate/close the application.

### **Hints**

<details>
<summary>Click me</summary>
  
Sender encodes the letters on by one into unicode.

File accessible for both the python apps is `/app/answers/flag_encoded.txt`

`receive_flag.py` should use `chr()` to convert unicode into human readable form.

There's an example code given in `answers/`

</details>
