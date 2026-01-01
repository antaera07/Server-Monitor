import os
import platform
import shutil

# List of servers to ping
servers = ["8.8.8.8", "1.1.1.1"]  # Google DNS & Cloudflare DNS

print("=== Server Uptime Check ===")
for server in servers:
    param = "-n" if platform.system().lower() == "windows" else "-c"
    response = os.system(f"ping {param} 1 {server}")
    if response == 0:
        print(f"{server} is ONLINE")
    else:
        print(f"{server} is OFFLINE")

print("\n=== Disk Usage ===")
total, used, free = shutil.disk_usage("/")
print(f"Total: {total // (2**30)} GB")
print(f"Used: {used // (2**30)} GB")
print(f"Free: {free // (2**30)} GB")
