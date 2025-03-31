### CTFPI docker compose 3 - Race condition

## Scenario

In computing there's a phenomenon as race condition. They might not be easy to debug or even notice and there have been instances where a software flaw such has this was left unnoticed on a radiation therapy machine, and sadly led to loss of human lives. Another example was with GE Energy when their alarm subsystem had a race condition, making the alarming system to monitoring technicians unfunctional. This led to a blackout in 2003. https://en.wikipedia.org/wiki/Race_condition.

**What is a race condition?** Let's say we have a program that needs to wait exactly 0.000001 seconds to execute again, seems logical to put `delay(0.000001)`, but can we absolutely be sure this delay is precise every time? Depending on if the system uses scheduling, real-time interrupts or the delay function itself varies on something like CPU load, the delay might not always be truly what we want it to be.

Now if the code absolutely expects there to be some data after the delay when in reality there isn't some unexpected things start to happen.

Another well known example is with file reading and loading, like we shall do in this challenge.
Let's say there's a `data.txt` file. Our program uses threading where one function writes into the data file and the other function reads from the file. So basically two functions use the same file. 

Now let's say there's no delay or sleep or anything, the program just runs as fast as it can. At first it might seem fine but maybe after 5 minutes of working we see some data is missing or corrupted.

What might have happened is that there's a chance where one function was writing the data and exactly at the same time the other function wanted to read the uncomplete data.


In this challenge we first run the race condition and notice what's happening, and after that we will fix it.

## Prerequisites

Cloned the CTF-pi repository.

Are inside the `ctfpi0_6` directory.

`docker compose version` command works, if not: https://docs.docker.com/compose/install/
If the command shows the version info then docker compose is installed properly.

## Requirements

Do this task on  remote connection to Raspi.

Read the through all the files except the ones in `answers/`.

Run `docker compose up --build`

`python spammer.py`

Try to understand the mistake and fix send_flag.py or receive_flag.py

## Steps to complete



## Cleaning up

`docker compose down`

## Role in cybersecurity

It might not seem a cybersecurity topic at first, however..

