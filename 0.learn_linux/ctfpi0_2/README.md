### CTFPI - coding challenge

## Scenario

Someone has written their own encryptor where they can input sensitive text and it comes out as random gibberish.

However you have received access to the source code `generator.py`. From that we can figure out the key: anything between two capital 'A' is considered a secret, so if "world" gets sent as input what comes out is AwA, AoA, ArA, AlA, AdA. Everything else around it becomes random letters.

Try to write a decryptor to `challenge.py` that finds out the author's secret.

## Prerequisites

Have cloned CTF-pi onto your Raspberry Pi. (This challenge can be done on any machine)

Are inside `ctfpi0_2` directory

## Requirements

Firstly check out the code in `generator.py` and afterwards `python generator.py` to run it.

Make sure `code.txt` has random text generated into it.

Once all is OK, open challenge.py in your favorite code editor and try to find the flag hidden inside this gibberish.

REMEMBER! The flag characters are between two capital 'A' letters so "AsA" means 's' is one letter from the flag.

## **Hints**

python's `re` library is very useful here.

A(.)A RegEx.

The solution code is under `answers/`

## Aftermath

generator.py can be modified however you like, change the flag, number of generater letters. Test if other inputs work with your code.