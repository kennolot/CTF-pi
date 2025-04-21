## CTF-pi - Home assistant - webhooks - Difficulty: ★☆☆☆☆

### Scenario

It's time to try out home automation, for that there's a well established free and open-source project called "Home Assistant".

It offers a simple interface and low coding knowledge setup to turn your home into a Smart home.

Basic features include turning lights on or off, measuring indoor temperatures.

Furthermore there's a way to configure remote control with your home and capturing data with webhooks, that's what this challenge is about.

Generally webhooks do not have any authentication, so when we run home automation within the local network, anyone who's also inside the same network and knows the webhook name AKA id, can then call it or retrieve it's data.

This comes with a security risk, the webhook could trigger on every log in and reveal the user who are logging in, increasing the attack surface. 

Webhooks can also be used to toggle electronic devices within your house and someone flicking your lights wouldn't be desired.

### Prerequisites

Have cloned CTF-pi repository onto your Pi.

Are currently inside the `ctfpi7_0` directory.

### Objective

`docker compose up --build -d` to pull Home Assistant and launch the app.

`hostname -I` to find out which IP the service is running on and visit it in your browser. Your main computer or even a phone can access this, as long as they are within the same network as Raspberry Pi.

Find Home Assistant's default port, enter it into the addressbar in your browser http://<ip>:<port> 

Do the onboarding registration with some dummy data, doesn't have to be your real details.

Create a webhook via the web UI. Webhook should send a persistent notification.


### Steps to complete

While inside the Home Assistant dashboard go to Settings > Automations & scenes > Create Automation > Create new automation.

When > Add trigger > Others > scroll until you see Webhook, click it.

Change webhook ID to something simple for this challenge: "supersecretdata" notice the suggestion below it.

Then do > Add action > Notifications > Send a persistent notification > Enter any message you want and click Save. Click save again.

Now since webhooks use POST method we need to send a POST method to webhook. For that we can use curl on Linux or Postman on windows.
```
curl -X POST http://<ip>:<port>/api/webhook/supersecretdata (or the webhook ID you chose).
```
Check the notifications on your Home Assistant dashboard. A device with no authentication did that!

Check out the other triggers and conditions and try to find weaknesses in them.


### Cleaning up

`docker compose down` in Raspi's terminal. 