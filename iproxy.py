import subprocess
import base64
import sys
from importlib import import_module

def install_and_import(package):
    try:
        import_module(package)
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", package], check=True)
        globals()[package] = import_module(package)

# Install necessary packages
install_and_import("tqdm")
install_and_import("colorama")

from tqdm import tqdm
from colorama import init, Fore, Style

def run_commands():
    encoded_commands = [
        "c3VkbyBhcHQgdXBkYXRl",
        "c3VkbyBhcHQgdXBncmFkZSAteQ==",
        "c3VkbyBhcHQgaW5zdGFsbCBweXRob24zLXBpcCAteQo=",
        "cGlwMyBpbnN0YWxsIHRxZG0=",
        "c3VkbyBwaXAgaW5zdGFsbCBjb2xvcmFtYQ==",
        "c3VkbyBhcHQtZ2V0IGluc3RhbGwgY2hyb255IC15",
        "c3VkbyBzeXN0ZW1jdGwgc3RhcnQgY2hyb255",
        "c3VkbyBzeXN0ZW1jdGwgZW5hYmxlIGNocm9ueQ==",
        "Y3VybCAtTCAtbyBtdHBfaW5zdGFsbC5zaCBodHRwczovL2dpdC5pby9majVydQ==",
        "YmFzaCBtdHBfaW5zdGFsbC5zaA=="
    ]
    init(autoreset=True)
    print(Fore.YELLOW + "Welcome to the iProxy setup script!\n")

    for encoded_command in tqdm(encoded_commands, desc="iProxy has been successfully installed", unit="command"):
        command = base64.b64decode(encoded_command).decode('utf-8')
        try:
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running: {command}")
            print(e)
            break
    
    decision = input("Do you want to install the fake website and BBR? (y/n): ")
    if decision.lower() == 'y':
        try:
            subprocess.run("wget -N --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh && chmod +x bbr.sh && bash bbr.sh", check=True, shell=True)
            subprocess.run("apt install nginx -y", check=True, shell=True)
            subprocess.run("rm -rf /usr/share/nginx/html/*", check=True, shell=True)
            subprocess.run("cd /usr/share/nginx/html/ && wget https://github.com/V2RaySSR/Trojan/raw/master/web.zip", check=True, shell=True)
            subprocess.run("unzip web.zip", check=True, shell=True)
            subprocess.run("systemctl start nginx", check=True, shell=True)
            subprocess.run("systemctl stop nginx", check=True, shell=True)
            subprocess.run("systemctl restart nginx", check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print("Error occurred while running installation commands.")
            print(e)
    
    decision = input("Do you want to check server details and speed? (y/n): ")
    if decision.lower() == 'y':
        try:
            subprocess.run("wget -qO- bench.sh | bash", check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print("Error occurred while running server details command.")
            print(e)

    init(autoreset=True)
    print(Fore.YELLOW + "")
    print("█ █▀█ █▀█ █▀█ ▀▄▀ █▄█")
    print("█ █▀▀ █▀▄ █▄█ █░█ ░█░")
    print("installed -https://github.com/parsico/iproxy")
    print("\n" + Style.RESET_ALL)

if __name__ == "__main__":
    run_commands()
