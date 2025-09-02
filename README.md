# Basic IP Scanner

A simple Python-based network scanner that scans a given subnet (e.g., `192.168.1.0/24`) to identify live hosts by sending ping requests.

## Features
- Scans any IPv4 subnet you specify
- Detects live hosts via ICMP ping
- Lightweight and easy to run — no special libraries required

## Requirements
- Python 3.x
- `ping` utility available in the system environment
- Internet or LAN access to the target network

## Usage
1. Clone or download this repository.
2. Open the terminal in the project folder.
3. Run:
   ```bash
   python main.py
