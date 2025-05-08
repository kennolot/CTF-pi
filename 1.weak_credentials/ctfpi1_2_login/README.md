## CTF-pi - Login page - Difficulty: ★★★★☆

### Scenario

While doing a security audit for a company you find out that they are running a website with login prompt.

This might be a security hole, you should look further.


### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi1_2` directory.

`docker compose` is installed.

`python` is installed.

### Objective

`hostname -I` on Raspberry Pi find out which IP the website is running on and visit it from your browser.

To challenge yourself more don't use `hostname -I`, act like you don't have any access to the Pi, you know the device is connected to the same local network as your machine, scan your local network to find Pi's IP.

Task completion doesn't have to be within Raspberry Pi, personal computer that's connected to the same network can access the page aswell.

Do this task from your main PC(to simulate realsitic environment), but if really needed doing it locally on Raspberry Pi also works.

Once you land at the webpage that asks for a password: try common passwords from before.

If you can't get the correct password that's okay, we should write a password brute forcing tool `cracker.py`. 

Before we know what data to send to the website, in your browser right click > View page source. 

Page source should reveal that form method is "post".

Now write a script that sends a post request to this exact site.

The script should start with single character like 'a', 'b', 'c' into the login box, ascii_lowercase() will be fine to use here.

Try every lowercase character possible a-z. Once all single characters have been tested, try combinations like "aa", "ab", "ca" etc.. 

Every time the page responds with "Invalid credentials, please try again." the loop should go on, the loop should break if the response is something else.

Hitting the correct password will output the flag in format CTFPI{..}.

When you feel stuck, feel free to check out all the files except `answers/`.

Also note: there are tools already made that do this exact thing, one of them is BurpSuite.


### **Hints**

<details>
<summary>Click me</summary>
  
POST requests are used for login.

The password is 3 lowercase characters long.

Linux command that will do the same thing as opening browser and clicking submit:

`curl -X POST http://10.10.10.67 -F "password=ekr"`

</details>

### Cleaning up

```
docker compose down
```
