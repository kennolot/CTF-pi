## How to build your own Raspberry Pi CTF challenges?

Similar to these.

### Structure

docker compose.yaml and Dockerfile are the most efficient way to build challenges.

They do a pretty good job providin isolation from main system but also are easier
to manage than for example a shell script that automates the build.

Docker also has plenty of already built projects so there's no need to do everything from scratch.
Example CTF-pi 6. and 7.

The usual compose.yaml structure I've used on this is:

...




### Scalability - for multiplayer

`compose.yaml` has an option to specify a range of ports instead of only a single port.
This ensures each challenger can have a separate container running for them without colliding with others.


