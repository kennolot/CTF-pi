### CTF-pi - OWASP juice shop - going further - Difficulty: ???

All credits go to: https://hub.docker.com/r/bkimminich/juice-shop

## Scenario

I just had to include OWASP juice shop as the last challenge.

The juice shop is kind of like a final boss fight of CTF-pi, it has around 90 challenges and is directed towards a weak web app, so not only does it contain API, it contains SQL injections, XSS, and even blockchain challenges!

There are a TON of resources and walkthroughs made for it.

## Prerequisites

Have cloned CTF-pi repository onto your Pi.

Are currently inside the `ctfpi7_2` directory.

### Objective

`docker compose up --build -d` to pull OWASP juice shop and launch the app.

`hostname -I` to find out which IP the service is running on and visit it in your browser. Your main computer or even a phone can access this, as long as they are within the same network as Raspberry Pi.

Port is set to 3000

The website looks like an average online store, but it is riddled with weaknesses, your job is to find them.

## Cleaning up

`docker compose down` in Raspi's terminal. 