#!/bin/bash

# ANSI color codes
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN} ░▀░ █▀▀█ █▀▀█ █▀▀█ █░█ █░░█"
echo -e "${GREEN} ▀█▀ █░░█ █▄▄▀ █░░█ ▄▀▄ █▄▄█"
echo -e "${GREEN} ▀▀▀ █▀▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀ ▄▄▄█${NC}"
echo -e "${GREEN}Welcome to the Parsico iProxy!${NC} Please enter '1' or '2' to proceed."
echo -e "${GREEN}https://github.com/parsico${NC}"

read -p "Enter your choice: " choice

if [ "$choice" = "1" ]; then
    apt update && apt upgrade -y
    wget https://raw.githubusercontent.com/parsico/iproxy/main/iproxy.py
    sudo apt-get install python3 -y
    sudo apt install python3-pip -y
    python3 iproxy.py
elif [ "$choice" = "2" ]; then
    echo -e "${GREEN}Fake TLS domains:${NC}"
    wget -qO- https://raw.githubusercontent.com/parsico/iproxy/main/fake-tls-domain.txt
else
    echo "Incorrect command. Script aborted."
fi
