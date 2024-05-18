import subprocess

def run_commands():
    commands = [
        "sudo apt update",
        "sudo apt upgrade -y",
        "sudo apt-get install chrony -y",
        "sudo systemctl start chrony",
        "sudo systemctl enable chrony",
        "curl -L -o mtp_install.sh https://git.io/fj5ru",
        "bash mtp_install.sh"
    ]
    
    for command in commands:
        try:
            print(f"Running: {command}")
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running: {command}")
            print(e)
            break

if __name__ == "__main__":
    run_commands()
