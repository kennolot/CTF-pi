## Weak/common linux user credentials

### Scenario 

You've gotten your hands on a Raspberry Pi that comes with already some users created for it, however the user that interests us the most has password set.

People sometimes forget to change default passwords in a hurry, or also set a very weak password and think they'll change it later. Let's try and see if this is the case here.

### Prerequisites

Be on your Raspberry Pi(VNC, Raspi connect, keyboard&mouse)

Have cloned this repository and are inside the `ctfpi1_0` directory



### Objective

Run these commands to create the weak ctf user:
`chmod +x create_acc.sh` `./create_acc.sh`

After the script finishes try to log into a newly created account.

Username `weakaccount1` is the username.

NOTE! After running the script again it deletes the old ctf user and generates a new one. With a new password.

### **Hints**

`su - weakaccount1`

What is usually the default password of Raspberry Pi?

Common passwords of embedded devices?

Try finding examples of weak passwords online.

There's a `inputs.txt` file under `answers/` that contains the passwords the script chooses from, they are common and weak.

### Cleaning up

After finding the `flag.txt`

Run the command `sudo deluser --remove-home weakaccount1`
