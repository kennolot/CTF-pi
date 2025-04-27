## CTF-pi - Docker compose 3 - Race condition - Difficulty: ★★★☆☆

### Scenario

In computing there's a phenomenon as race condition. They might not be easy to debug or even notice and there have been instances where a software flaw such has this was left unnoticed on a radiation therapy machine, and sadly led to loss of human lives. Another example was with GE Energy when their alarm subsystem had a race condition, making the alarming system to monitoring technicians unfunctional. This led to a blackout in 2003. https://en.wikipedia.org/wiki/Race_condition.

**What is a race condition?** Let's say we have a program that needs to wait exactly 0.000001 seconds to execute again, seems logical to put `delay(0.000001)`, but can we absolutely be sure this delay is precise every time? Depending on if the system uses scheduling, real-time interrupts or the delay function itself varies on something like CPU load, the delay might not always be truly what we want it to be.

Now if the code absolutely expects there to be some data after the delay when in reality there isn't some unexpected things start to happen.

Another well known example is with file reading and writing.
Let's say there's a `data.txt` file. Our program uses threading where one function writes into the data file and the other function reads from the file. So basically two functions use the same file. 

Now let's say there's no delay or sleep or anything, the program just runs as fast as it can. At first it might seem fine but maybe after 5 minutes of working we see some data is missing or incorrect.

What might have happened is that there's a chance where one function was writing the data and exactly at the same time the other function wanted to read the uncomplete data.

Another example might be with a bank account: imagine a bank account with $1000 balance. Withdraw(100) function gets called and returns $900, the new balance. But now imagine two withdraw(100) requests happen at exactly the same time, both of them read the balance $1000 and return $900, but the user withdrew $200, the bank got exploited and lost $100 to the attacker.

In this challenge we introduce race condition with two Docker containers, first run the race condition and notice what's happening, and after that we will fix it.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_6` directory.

`docker compose version` command works, if not: https://docs.docker.com/compose/install/
If the command shows the version info then docker compose is installed properly.

### Objective

Do this on Raspberry Pi remote connection.

Read through all the files except the ones in `answers/`.

Run `docker compose up --build`

Both of the python programs will read the counter from a file and increment it.

Try to understand the mistake and fix `increment_1.py` and `increment_2.py`

### Steps to complete

First things first, let's see if the problem we think even occurs, run docker compose and read what's printed in the terminal. Is it what we expect? Answer: at first everything will probably run fine, but keep a close eye on the output and be ready to terminate the program(CTRL+C) when an error gets displayed. Sometimes error might happen early, sometimes it will run for a minute without errors.

The error should be about JSON data not being correct.

To complete this challenge fix `increment_1.py` and `increment_2.py` so that they politely take turns updating the incrementer, working in sync with eachother. 

The challenge will be solved when no error gets displayed until incrementer reaches 3000.

A very big HINT: fcntl.flock()


### Cleaning up

`docker compose down`

### Role in cybersecurity

It might not seem a cybersecurity topic at first, however race conditions are an easy way to cause denial of service, a function reads data that it doesn't expect for example and crashes as a result.

https://nvd.nist.gov/vuln/detail/cve-2024-45300 This CVE enabled attackers to rapidly apply coupon codes or discounts without limits.

https://www.lumificyber.com/threat-library/cve-2024-6387-race-condition-in-signal-handling-for-openssh/ Goes over how root access got gained from race condition.

