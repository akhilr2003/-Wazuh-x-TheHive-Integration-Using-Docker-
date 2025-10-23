#!/bin/bash
# Example helper: installs Python deps for Wazuh -> TheHive python integration (if needed)
# Run on the Wazuh manager
set -e
sudo apt update
sudo apt install -y python3 python3-pip
sudo pip3 install thehive4py requests
echo "Dependencies installed: thehive4py, requests"
