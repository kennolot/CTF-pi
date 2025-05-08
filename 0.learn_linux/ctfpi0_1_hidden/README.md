## CTF-pi - Nothing inside here? - Difficulty: ★☆☆☆☆

### Scenario

Git repositories are a common way to get sensitive keys leaked. Most of the time this is done by an accident.

Imagine you have just finished your project and want to upload(push) your work to the server like GitHub.

When opening this directory `ctfpi0_1` from Raspberry Pi's Linux terminal and running `ls` there seems to only be the README file there.

But is it truly the case?

Note! "dot" or "." infront of a filename or directory name in Linux means it's hidden.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_1` directory.

### Objective

Do this task on Linux terminal: remote connection on Raspi.

Find the hidden flag.txt.

### Hints

<details>
<summary>Click me</summary>

`ls -la` `cd` `cat`. `-a` flag will list all the files, even hidden.
</details>

### Why is this a big deal?

Plenty of applications create hidden directories. Usually they're meant for storing configurations or something about the environment for the app to run properly.

But sometimes these files can contain something sensitive, or a better view to the insides of running application.

Now when we ran `ls` then dot directories weren't shown to us. But they are there like an ordinary directory for git.

So what could happen is that we generated .config/ and did `git add .` or `git add -A` to stage all files at once, committed and pushed it into the server. For us we didn't see anything with `ls` but git gladly pushed the hidden directories to the server.

When opening the repository from GitHub: CTF-pi/0.learn_linux/ctfpi0_1 the "hidden" files are all there.
