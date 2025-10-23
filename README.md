<img width="1536" height="1024" alt="ChatGPT Image Oct 23, 2025, 10_45_04 AM (1)" src="https://github.com/user-attachments/assets/99031ada-a491-4795-885b-2dbe1332df75" />


# 🧠 Beginner-Friendly SOC Lab — Wazuh + TheHive Integration 🛡️💚

> “When alerts buzz, TheHive listens 🐝⚡ — your first step into SOC automation.”

Welcome to your **SOC Lab Project** — a hands-on guide to building your own **SIEM + Incident Response automation setup** using **Wazuh** and **TheHive** inside **Ubuntu** 🐧.  
This project is designed for **beginners**, so everything is explained step-by-step — crisp, clean, and in true cyber-lab style 😎.

---

## ⚙️ What You’ll Learn

- 🌐 Install **Ubuntu**, **Wazuh**, and **TheHive**
- 🐋 Deploy **TheHive + Elasticsearch** easily using **Docker**
- 🔗 Connect **Wazuh → TheHive** so alerts create cases automatically
- 🧩 Understand how real SOCs detect and respond to threats
- ⚡ Learn how basic SOC automation works — all inside your home lab!

---

## 🧰 What’s Included

| File | Description |
|------|--------------|
| 🧾 **README.md** | The main guide — beginner-friendly and clear. |
| 🐋 **docker-compose.yml** | Deploys TheHive + Elasticsearch with one command. |
| ⚙️ **wazuh_ossec_integration.conf** | Snippet to link Wazuh alerts directly to TheHive. |
| 🧠 **wazuh_forwarder_script.sh** | Helper script to install Python dependencies. |
| 🔐 **thehive_env_example.env** | Example environment variables for TheHive. |
| 📘 **PROJECT_OVERVIEW.pdf** | PDF version of this guide — ready for reports or submissions. |

---

## 🪜 Step-by-Step Setup

### 1️⃣ Ubuntu Setup
Use **Ubuntu Server 22.04 LTS** (2 CPU, 4GB RAM minimum).
```bash
sudo apt update && sudo apt upgrade -y
