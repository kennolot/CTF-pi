### Physical Access - Exploiting open USB ports with our own bad-USB.


## Scenario

This time we've found an otherwise inaccessible Raspberry device running in an IoT environment. It was hidden from plain sight and there doesn't seem to be a lot of ways to breach it's security. However we see that the USB ports of the raspi are completely exposed.

In this scenario we are building our own Bad-USB, a device when plugged into another device(Raspberry Pi in our case) delivers malware, executes malicious commands etc. By the end of this we will see that even a device that is completely offline or otherwise unreachable is still possible to exploit with exposed USB ports.

## Requirements

1x ** Raspberry Pico ** or equivalent like Arduino etc.

1x A data transmitting USB A -> Micro USB(Typically) cable or an adapter.

1x Raspberry Pi

## Prerequisites

For a video tutorial: https://www.youtube.com/watch?v=ctCmOhoT9po (Guide by Austin's Lab)

When using Raspberry Pico, we need to download https://github.com/dbisu/pico-ducky and follow the instructions provided on this page.


## Steps to complete

