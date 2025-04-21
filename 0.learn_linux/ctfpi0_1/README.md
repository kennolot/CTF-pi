### Nothing inside here?

## Scenario

When opening this directory `ctfpi0_1` from Linux terminal and running `ls` there seems to only be the README file there.

But is it turly the case?

## Prerequisites

Cloned the CTF-pi repository onto your Raspberry pi.

Are inside the `ctfpi0_1` directory.

### Objective

Do this task on Linux terminal: either remote connection on Raspi or your personal machine.

Find the hidden flag.txt.

## Hints

`ls -la`  `cd` `cat` are the commands.

## Why is this a big deal?

Plenty of applications create hidden directories. Usually they're meant for storing configurations or something about the environment for the app to run properly.

But sometimes these files can contain something sensitive, or a better view to the insides of running application.

Now when we ran `ls` then dot directories weren't shown to us. But they are there like an ordinary directory for git.

So what could happen is that we generated .config/ and did `git add .` or `git add -A` to stage all files at once, committed and pushed it into the server. For us we didn't see anything with `ls` but git gladly pushed the hidden directories to the server.

When opening the repository from GitHub: CTF-pi/0.learn_linux/ctfpi0_1 the "hidden" files are all there.