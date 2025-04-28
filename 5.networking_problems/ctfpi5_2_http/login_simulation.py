import subprocess
import requests
import random
import time

# get the IP from "hostname -I" terminal command
raspi_ip = subprocess.check_output("hostname -I", shell=True).decode().split()[0]
print(raspi_ip)
URL = f"http://{raspi_ip}/login.php"

usernames = ["piuser", "pi314", "demoadmin", "anonymous", "test"]
passwords = ["raspberry", "password", "letmein", "$ss65", "pi"]
real_cred = ["admin", "4am_SECRET_sandw3ch.1"]

def random_login():
    # 10% chance for real admin credentials.
    if random.random() < 0.1:
        return real_cred
    return [random.choice(usernames), random.choice(passwords)]

print(f"Random users will start logging in on: {URL}")
print("Capture these logins using backdoor.py or tcpdump")
while True:
    user, pw = random_login()
    try:
        response = requests.post(URL, data={"username": user, "password": pw})
        print("Login attempted")
    except Exception as e:
        print(f"Error connecting: {e}")
    time.sleep(random.randint(1, 5))
