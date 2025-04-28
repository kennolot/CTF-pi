#!/bin/bash

#
# This script creates a vulnerable account, but with low privileges over the system.
# This script contains the password that the ctf player wouldn't know! But has to guess it.
#
# Also create random pass with new run and delete the old ctf user.


username="weakaccount1"
password[0]="pi"
password[1]="12345"
password[2]="qwerty"
password[3]="password"
password[4]="pass"
password[5]="admin"

# randomization source: https://stackoverflow.com/questions/35623462/bash-select-random-string-from-list
size=${#password[@]}
index=$(($RANDOM % $size))

randvar=${password[$index]}

if id "$username" &>/dev/null; then    
    sudo deluser --remove-home "$username"
fi

sudo useradd -ms /bin/bash "$username"

echo "$username:$randvar" | sudo chpasswd

sudo cp ./answers/flag.txt "/home/$username/flag.txt"

sudo chown "$username":"$username" "/home/$username/flag.txt"
sudo chmod 400 "/home/$username/flag.txt"