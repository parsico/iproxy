import subprocess
import base64

def run_commands():
    encoded_commands = [
        "YXB0IHVwZGF0ZQ==",
        "YXB0IHVwZ3JhZGUgLXk=",
        "c3VkbyBhcHQtZ2V0IGluc3RhbGwgY2hyb255",
        "c3VkbyBzeXN0ZW1jdGwgc3RhcnQgY2hyb255",
        "c3VkbyBzeXN0ZW1jdGwgaW5zdGFsbCBjaHJvbnk=",
        "Y3VybCAtTCAtbyBtdHBfaW5zdGFsbC5zaCBodHRwczovL2dpdC5pby9majVydQ==",
        "YmFzaCBtdHBfaW5zdGFsbC5zaA=="
    ]

    for encoded_command in encoded_commands:
        command = base64.b64decode(encoded_command).decode('utf-8')
        try:
            print(f"Running: {command}")
            subprocess.run(command, check=True, shell=True)
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while running: {command}")
            print(e)
            break

if __name__ == "__main__":
    run_commands()
