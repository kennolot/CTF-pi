## CTF-pi - Coding challenge - Difficulty: ★★☆☆☆

### Scenario

Someone has written their own encryptor where they can input sensitive text and it comes out as random gibberish.

However you have received access to the source code `generator.py`. From that we can figure out the key: anything between two capital 'A' is considered a secret, so if "world" gets sent as input what comes out is AwA, AoA, ArA, AlA, AdA. Everything else around it becomes random letters.

Try to write a decryptor script to `challenge.py` that finds out the author's secret.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi0_2` directory.

`python --version` outputs something, meaning python is installed.

### Objective

First check out the code in `generator.py` and afterwards `python generator.py` to run it.

Make sure `code.txt` has random text generated into it.

Once all is OK, open `challenge.py` in your favorite code editor and try to find the flag hidden inside this gibberish.

REMEMBER! The flag characters are between two capital 'A' letters so "AsA" means 's' is one letter from the flag.

### **Hints**

<details>
<summary>Click me</summary>


python's `re` library is very useful here.

A(.)A RegEx.

The solution code is under `answers/`
</details>

### Your own challenge

generator.py can be modified however you like, change the flag, number of generated letters. Test if other inputs work with your code.
