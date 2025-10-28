<img width="1536" height="1024" alt="ChatGPT Image Oct 23, 2025, 10_45_04 AM (1)" src="https://github.com/user-attachments/assets/29cad623-bb2f-4c2c-a81e-7d8768d333c4" />


# 🧠  SOC Lab — Wazuh + TheHive Integration Using Docker 🛡️💚

> “When alerts buzz, TheHive listens 🐝⚡ — your first step into SOC automation.”

Welcome to your **SOC Lab Project** — a hands-on guide to building your own **SIEM + Incident Response automation setup** using **Wazuh** and **TheHive** inside **Ubuntu** 🐧.  This project is designed for **beginners**, so everything is explained step-by-step — crisp, clean, and in true cyber-lab style 😎.


## ⚙️ What You’ll Learn

- 🌐 Install **Ubuntu**, **Wazuh**, and **TheHive**
- 🐋 Deploy **TheHive + Elasticsearch** easily using **Docker**
- 🔗 Connect **Wazuh → TheHive** so alerts create cases automatically
- 🧩 Understand how real SOCs detect and respond to threats
- ⚡ Learn how basic SOC automation works — all inside your home lab!


## 🧰 What’s Included

| File | Description |
|------|--------------|
| 🧾 **README.md** | The main guide — beginner-friendly and clear. |
| 🐋 **docker-compose.yml** | Deploys TheHive + Elasticsearch with one command. |
| ⚙️ **wazuh_ossec_integration.conf** | Snippet to link Wazuh alerts directly to TheHive. |
| 🧠 **wazuh_forwarder_script.sh** | Helper script to install Python dependencies. |
| 🔐 **thehive_env_example.env** | Example environment variables for TheHive. |



## Installation:-

1️⃣ Ubuntu Setup
Use Ubuntu Server 22.04 LTS (2 CPU, 4GB RAM minimum).
```bash
sudo apt update && sudo apt upgrade -y
```
2️⃣ Install Docker & Docker Compose
```bash
sudo apt install -y ca-certificates curl gnupg lsb-release
```
```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
```bash
sudo usermod -aG docker $USER
newgrp docker
```
3️⃣ Deploy TheHive Using Docker

Copy docker-compose.yml to /opt/thehive/ and run:
```bash
docker compose up -d
```
Access TheHive UI → http://<YOUR_SERVER_IP>:9000

💡 If you don’t see anything: check logs using
```bash
docker compose logs -f
```

4️⃣ Install Wazuh Manager
Follow the official docs 👇
https://documentation.wazuh.com/current/installation-guide/wazuh-server/step-by-step.html?utm_source=chatgpt.com
(Install repo → run setup → start wazuh-manager.)


5️⃣ Create TheHive API Key

1)Log in to TheHive UI

2)Go to Settings → API Keys

3)Create a new key and copy it

6️⃣ Configure Wazuh → TheHive Integration

Add this to /var/ossec/etc/ossec.conf:
```bash
<integration>
  <name>thehive</name>
  <hook_url>http://YOUR_THEHIVE_IP:9000/api/alert</hook_url>
  <api_key>YOUR_THEHIVE_API_KEY</api_key>
  <level>7</level>
  <alert_format>json</alert_format>
</integration>
```
Restart Wazuh:
```bash
sudo systemctl restart wazuh-manager
```
7️⃣ Test the Setup

Trigger a test alert (failed SSH login works great):
```bash
ssh invalid@yourserver
```
Then open TheHive → Alerts tab — you should see a fresh alert buzzing in 🐝.

🧠 How It Works

Wazuh detects suspicious activities

TheHive manages alerts and cases

Integration automates alert forwarding — a mini SOC in action ⚡


## credits


  Created by Pepe (Akhil R.)

🛡️Cybersecurity Engineer | EC-Council Certified SOC Analyst🔍

💬 “Every log tells a story — listen carefully, and you’ll find the intruder.” 👾