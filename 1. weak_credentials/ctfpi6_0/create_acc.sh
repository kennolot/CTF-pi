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

# finish from here