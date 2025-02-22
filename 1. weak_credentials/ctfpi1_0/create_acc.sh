#!/bin/bash

#
# This script creates a vulnerable account, but with low privileges over the system.
# This script contains the password that the ctf player wouldn't know! But has to guess it.
#
# Also create random pass with new run and delete the old ctf user.


username = "weakaccount1"
password = ("pi" "12345" "qwerty" "password" "pass" "admin")

randvar = "${password[RANDOM % ${#password[@]}]}"

if id "$username" &>/dev/null; then    
    sudo deluser --remove-home "$username"
fi

sudo useradd -ms /bin/bash "$username"

echo "$username:$password" | sudo chpasswd

sudo cp ./answers/flag.txt "/home/$username/flag.txt"

sudo chown "$username":"$username" "/home/$username/flag.txt"
sudo chmod 400 "/home/$username/flag.txt"