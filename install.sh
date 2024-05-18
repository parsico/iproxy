#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN} ░▀░ █▀▀█ █▀▀█ █▀▀█ █░█ █░░█"
echo -e "${GREEN} ▀█▀ █░░█ █▄▄▀ █░░█ ▄▀▄ █▄▄█"
echo -e "${GREEN} ▀▀▀ █▀▀▀ ▀░▀▀ ▀▀▀▀ ▀░▀ ▄▄▄█${NC}"
echo -e "${YELLOW}https://github.com/parsico${NC}"
echo -e "${RED}Powered By PARSICO.ORG${NC}"
echo -e ""
echo -e ""
echo -e "${GREEN}-----------------------------------------${NC}"
echo -e ""
echo -e "${GREEN}Welcome to the Parsico iProxy!${NC} Please select an option:"
echo -e "${GREEN}1. Install iProxy"
echo -e "2. View Fake-TLS Site List"
echo -e "3. Create Proxy with Legacy Kernel${NC}"
echo -e ""
echo -e "${GREEN}-----------------------------------------${NC}"

read -p "Enter your choice (1 / 2 / 3): " choice

if [ "$choice" = "1" ]; then
    apt update && apt upgrade -y
    wget https://raw.githubusercontent.com/parsico/iproxy/main/iproxy.py
    sudo apt-get install python3 -y
    sudo apt install python3-pip -y
    python3 iproxy.py
elif [ "$choice" = "2" ]; then
    echo -e "${GREEN}Fake TLS domains:${NC}"
    wget -qO- https://raw.githubusercontent.com/parsico/iproxy/main/fake-tls-domain.txt
elif [ "$choice" = "3" ]; then
    echo -e "${GREEN}Creating Proxy with Legacy Kernel...${NC}"
    curl -o MTProtoProxyInstall.sh -L https://git.io/fjo34 && bash MTProtoProxyInstall.sh
else
    echo "Incorrect command. Script aborted."
fi
