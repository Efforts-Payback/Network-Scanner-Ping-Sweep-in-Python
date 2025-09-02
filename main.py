#!/usr/bin/env python3
# ping_sweep.py — Simple simulated network scanner

import random
import time

# Change the base network here
base_network = "192.168.1"

print("Scanning network:", base_network + ".0/24")

for i in range(1, 11):  # scans .1 to .10
    ip = f"{base_network}.{i}"
    # simulate network delay
    time.sleep(0.2)
    # randomly decide if "up"
    is_up = random.choice([True, False])
    if is_up:
        print(f"[+] {ip} is up")
    else:
        print(f"[-] {ip} is down")
