### Home assistant - REST API

## Scenario

Another option is to use REST API with home assistant, when webhooks' main idea is to trigger every time an event happens and on its own, then REST works by pulling instead, so for example to check if lights are on, a request asking the device has to be sent.

The main use case of this API is to control the system using our own commands.

This means we could write a python script that sends a request to an endpoint, the endpoint then responds by changing the states, print logs etc.

With this however comes a problem, people will generally keep their passwords secret, but with API keys they can be forgotten easily. Since for example a python script needs to know the API key for authorization, then they are left as plaintext into variables.

In this challenge we will see that a leaked API key is pretty much as valuable to the attacker as username and password.

https://developers.home-assistant.io/docs/api/rest/ Provides everything someone could do when they have authorized themselves with an API key.

## Prerequisites

Have cloned CTF-pi repository onto your Pi.

Are currently inside the `ctfpi7_1` directory.

Installed `requests` via pip. 
`sudo chown -R <raspi_user>:<raspi_user> /opt/ctfenv` Command might be needed if you get errors with pip install permission denied.

## Requirements

`docker compose up --build -d` to pull Home Assistant and launch the app.

`hostname -I` to find out which IP the service is running on and visit it in your browser. Your main computer or even a phone can access this, as long as they are within the same network as Raspberry Pi.

Find Home Assistant's default port, enter it into the addressbar in your browser http://<ip>:<port> 

Do the onboarding registration with some dummy data, don't have to be your real details.

Create an API token.

Try using it with the provided `request.py` script.

NOTE! There is NO flag.txt for this challenge.

## Steps to complete

While on the Dashboard of home assistant go to > profile > Security > Long-lived access tokens > Create token > name it anything > Copy to clipboard. 

Edit the python script with your token and IP.

Run: `python3 request.py` `> text.txt` can be added to write the result to file for easier reading.

What potentially valuable information can you find?

https://developers.home-assistant.io/docs/api/rest/ Check out other possible requests.



## Cleaning up

`docker compose down` in Raspi's terminal. 