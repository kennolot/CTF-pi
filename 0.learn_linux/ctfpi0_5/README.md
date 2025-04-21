### CTFPI Docker compose 2 - Send & Receive

## Scenario

Now it's time to run two containers, one for sending data, other for reading data sent by first container.

This challenge will be more interactive as the receiver part is missing.

It is your task to fix it. NOTE! No need to change Dockerfile or compose.yaml, only change receiver/receive_flag.py file

Depending on how you write the solution we might have introduced something called Race condition into our code, so if you get odd errors or results, check `ctfpi0_6`.

## Prerequisites

Cloned the CTF-pi repository.

Are inside the `ctfpi0_5` directory.

`docker compose version` command works, if not: https://docs.docker.com/compose/install/
If the command shows the version info then docker compose is installed properly.

### Objective

Do this task using remote connection on Raspi.

Read what's inside Dockerfiles and compose.yaml, sender/send_flag.py

Complete receiver/receive_flag.py: read and decode the content from `flag_encoded.txt`.

Print from receive_flag.py the flag.

Check if your code works:
```
docker compose up --build
```

The solution is correct if receiver can print out the encoded flag in human readable form.

CTRL+C to terminate/close the application.

## **Hints**

Sender encodes the letters on by one into unicode.

File accessible for both the python apps is `flag_encoded.txt`

receive_flag.py should use `chr()` to convert unicode into human readable form.

There's an example code given in `answers/`

