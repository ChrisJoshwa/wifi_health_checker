# WiFi Access Point Health Checker

A Python-based automation tool to remotely check the health of multiple WiFi Access Points (APs) over SSH.

## Features
- Connect to multiple APs using SSH
- Check uptime, running processes, and memory/CPU usage
- Multi-threaded execution for faster checks
- Export results to CSV

## Requirements
- Python 3.8+
- Dependencies listed in `requirements.txt`

## Installation
```bash
git clone https://github.com/<your-username>/wifi_health_checker.git
cd wifi_health_checker
pip install -r requirements.txt

## Testing Without Real Devices

To test this tool without connecting to real Access Points, use the following entry in your device list CSV:

```csv
ip,username,password
test_ap,dummy,dummy

