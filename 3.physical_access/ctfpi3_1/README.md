### CTF-pi - Physical Access - Exploiting open USB ports with our own BadUSB 2 - Difficulty: ★★★☆☆

## Scenario

Now let's take a more privacy related approach, after completing the first challenge we know we can run pretty much any commands we want via BadUSB. 

However for this challenge let's try something littler "quieter". Let's try taking a screenshot from the Raspberry's screen!

NOTE!

For this challenge there is no flag.txt, the challenge is completed when you have a screenshot taken from Raspberry Pi viewable from your main machine.

## Prerequisites

Have a pico-ducky that we made in the previous challenge working.

Raspberry Pi ready to be hacked.

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi3_1` directory.

## Requirements 

Find a way to take a screenshot using duckyscript.

Plug in pico-usb into the raspi and retrieve the screenshot.

## **Hints**

`grim` capabilities

## Cleaning up

If your script saved the screenshot onto the pico, you might want to delete the image since pico has very limited space.
