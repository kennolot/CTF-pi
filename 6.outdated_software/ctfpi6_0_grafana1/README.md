## CTF-pi - Outdated software - Grafana - Difficulty: ★★☆☆☆

### Scenario 

From Wikipedia: Grafana is a multi-platform open source analytics and interactive visualization web application. It can produce charts, graphs, and alerts for the web when connected to supported data sources.

We have Grafana running on our Raspi, is there a way to exploit it?

For this challenge we know the `username: ctfpi` `password: ctfpi`

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi6_0` directory.

`docker compose` works.


### Objective

Run within this directory on Raspi: `docker compose up -d` (Using remote shell)

`hostname -I` to find out which IP the service is running on and visit it in your browser. Your main computer or even a phone can access this, as long as they are within the same network as Raspberry Pi.

Which port is Grafana running on by default? Find out.

Find an existing vulnerability and exploit it(HTML injection), once you think you figured it out check: `answers/flag.txt`. NOTE! The flag IS NOT a text file you need to find!!


### Steps to complete

Google reveals that default Grafana port is 3000, and `hostname -I` reveals the IP, in my case the address to the service is: `10.10.10.67:3000`.

Enter this into your URL bar of your browser and you land on Grafana login page. 

Note the version it shows at the bottom of the page, we will need it.

Grafana default settings actually block brute force log-in attempts, after 5 fails you get a 5 minute cooldown before you can log in. That is bad news for an attacker and they have to find a better solution to find log-in credentials. To save time we can assume we've already gotten the credentials.

Log in using `username: ctfpi` `password: ctfpi`

Google for Grafana 6.2.4 exploits and Exploit-DB result should show up, open it and try to understand.

Inside our Grafana app > Add data source > TestData DB > Save & Test.

Then Create Dashboard > Add Query > General settings > Drilldown Links > Add link.

Inside the Title box add
```
<img src="https://www.shutterstock.com/image-vector/have-been-pwned-you-hacked-260nw-2148073239.jpg">
```

Click back > Go to dashboard > Do you want to save your changes? > Save > Save

Now when you hover over the Title pop out you can see the Pwned or whatever image you chose, this can actually be any HTML code, and this is not meant to happen. Luckily Grafana also sanitizes, so html script tag doesn't work which would be catastrophic. 

However this still can pose a risk, not specifically in this version of Grafana but in general one way for an attacker to leverage HTML injection is to use InnerHTML. That means the attacker attaches an image which doesn't exist, and since it doesn't exist an onerror parameter executes and does something the attacker wants.

On later versions of Grafana this vulnerability has been fixed, so keep your programs up to date.

### Cleaning up

`docker compose down`