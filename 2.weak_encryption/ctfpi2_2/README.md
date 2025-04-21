## Ctf-pi 2_2 - The Standard for IoT Messaging

### Scenario

MQTT (Message Queuing Telemetry Transport) is the de facto data exchange protocol for IoT messaging.

![Alt text](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2017/01/mqtt_broker.png?resize=750%2C303&quality=100&strip=all&ssl=1 "MQTT")

![Alt text](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/09/MQTT-Publish-Subscribe-Example.png?w=732&quality=100&strip=all&ssl=1 "MQTT")

https://randomnerdtutorials.com/what-is-mqtt-and-how-it-works/

Basically it works like this: there's a boss in a workplace who gets to decide what the workers have to do. The employees report their work to the boss, who then decides what happens, in most cases the boss forwards the work done by their employee to another different worker, who receives the message that the work is done and he can start doing his work.

The boss separates his workers into groups, so only the assigned workers receive messages from other workers.

In technical terms the boss is the broker, usually a Raspberry Pi or similar, and workers are the devices like sensors and lamps.

There are topics like house/kitchen/lamp, garage/door. Say we have a garage door with a light sensor, it closes when it gets dark. The time hits 11PM and it's dark enough, sensor PUBLISHES a message to topic garage/door, now the automatic garage door, which has SUBSCRIBED to the garage/door topic suddenly sees a message on the topic "Garage: close". The garage door closes.

This is called a machine-to-machine communication.

Read more: https://www.hivemq.com/mqtt/


For this challenge we just have a Pi which sends messages to itself.

Good thing is that the sensitive data isn't sent in plain text, but how secure is the implemented encryption.

It uses AES, which is the current strongest encryption! AES-256 is even used by governments to encrypt confidential data. So is it uncrackable? To put it short, yes it is, even the supercomputers would take billions of years to crack it.

HOWEVER! Even the strongest encryption will not work if the developer makes a mistake.

And this is what has happened here.


### Prerequisites

Raspberry Pi preferrably with remote connection set up.

Multiple computers can be used but make sure Raspberry is connected to localhost and so is the other computer. However doing it all on raspberry remote connection also works.

Cloned the CTF-pi repository onto your Raspberry.

Are inside the ctfpi2_2 directory.

`docker compose` works. 

Proper python packages are installed, check the source code or run it and read the error.

### Objective

You have access to `mqtt_encrypt.py` file, this is where the encryption happens.

Understand what it's doing and write a `decrypt.py` to crack the flag which is sent via a message to subscribed devices.

Run `python decrypt.py` if it's ready, then `python mqtt_encrypt.py` which sends the encrypted message and decrypt reads and hopefully cracks it.


### **Hints**

Read the source code `mqtt_encrypt.py` notice the comments.

The variables contain sensitive keys, which help us breach this encryption.

There are multiple things going on, first AES, then base64. Do it in reverse to crack it.

`cipher = AES.new(key, AES.MODE_CBC, iv)` key is given, iv is also given and is first 16 bytes.


`answers/answer/py` has a working solution.

### Cleaning up

```
docker compose down
```