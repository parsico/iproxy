#!/bin/bash
echo " ░▀░ █▀▀█ █▀▀█ █▀▀█ █░█ █░░█"
echo " ▀█▀ █░░█ █▄▄▀ █░░█ ▄▀▄ █▄▄█"
echo " ▀▀▀ █▀▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀ ▄▄▄█"
echo "Welcome to the Parsico script! Please enter 'y' to proceed."

read -p "Enter your command: " input

if [ "$input" = "y" ]; then
    apt update && apt upgrade -y
    wget https://raw.githubusercontent.com/parsico/iproxy/main/iproxy.py
    sudo apt-get install python3 -y
    sudo apt install python3-pip -y
    python3 iproxy.py
else
    echo "Incorrect command. Script aborted."
fi
