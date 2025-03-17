### Home assistant - 

## Scenario



## Prerequisites

Have cloned CTF-pi repository onto your Pi.

Are currently inside the `ctfpi7_1` directory.

## Requirements

`docker compose up --build -d` to pull Home Assistant and launch the app.

`hostname -I` to find out which IP the service is running on and visit it in your browser. Your main computer or even a phone can access this, as long as they are within the same network as Raspberry Pi.

Find Home Assistant's default port, enter it into the addressbar in your browser http://<ip>:<port> 

Do the onboarding registration with some dummy data, doesn't have to be your real details.




## Steps to complete




## Cleaning up

`docker compose down` in Raspi's terminal. 