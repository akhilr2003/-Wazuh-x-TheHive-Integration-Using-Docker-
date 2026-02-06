<img width="1536" height="1024" alt="ChatGPT Image Oct 23, 2025, 10_45_04 AM (1)" src="https://github.com/user-attachments/assets/29cad623-bb2f-4c2c-a81e-7d8768d333c4" />

# 🔗 Wazuh → TheHive Alert Integration (Custom Connector)

A custom integration that automatically forwards Wazuh SIEM alerts to **TheHive** for incident response and case management.
This project uses a Wazuh custom integration block, a shell wrapper, and a Python script to transform and push alerts into TheHive via API.

This setup is useful for SOC labs and real-world blue team workflows where detections from Wazuh must be converted into investigation-ready alerts in TheHive.

---

## 🧠 Overview

When Wazuh generates an alert:

1. Wazuh triggers a **custom integration**
2. A shell script receives the alert JSON file
3. The script calls a Python connector
4. Python formats the alert into TheHive schema
5. Alert is pushed into **TheHive API**
6. TheHive creates a new alert ready for case creation

---

## 🏗️ Architecture Flow

Wazuh Alert
→ Custom Integration Block
→ Shell Wrapper
→ Python Sender Script
→ TheHive REST API
→ Alert Created in TheHive

---

## 📂 Project Files

### Integration Block

Defines the custom integration inside Wazuh:



---

### Shell Wrapper Script

Responsible for:

* Receiving Wazuh alert JSON path
* Selecting correct Python interpreter
* Passing TheHive credentials via environment variables
* Sending alert JSON to Python script



---

### Python Alert Sender

Responsible for:

* Reading alert JSON
* Mapping Wazuh severity → TheHive severity (1–4)
* Building observables (IP addresses)
* Creating TheHive alert via API call



---

## ⚙️ Requirements

* Wazuh Manager installed
* TheHive 5 running (Docker or server)
* Python 3
* Python requests library
* Wazuh custom integration enabled
* TheHive API key

Install dependency:

```
pip install requests
```

---

## 🐝 TheHive Setup

Start TheHive (Docker recommended).

Default API endpoint:

```
http://<THEHIVE_IP>:9000
```

Generate API Key:

```
TheHive UI → User → API Keys → Create
```

Copy the key for configuration.

---

## 🛡️ Wazuh Integration Setup

### Step 1 — Copy Files

```
/var/ossec/integrations/custom-thehive
/var/ossec/integrations/custom/thehive-alerts.py
```

Make executable:

```
chmod +x custom-thehive
chmod +x thehive-alerts.py
```

---

### Step 2 — Configure Integration Block

Add to:

```
/var/ossec/etc/ossec.conf
```

```
<integration>
  <name>custom-thehive</name>
  <level>4</level>
  <alert_format>json</alert_format>
</integration>
```

---

### Step 3 — Edit Shell Script Credentials

Update:

```
THEHIVE_URL="http://YOUR_THEHIVE_IP:9000"
THEHIVE_API_KEY="YOUR_API_KEY"
```

---

### Step 4 — Restart Wazuh

```
systemctl restart wazuh-manager
```

---

## 🧪 Testing

Trigger a Wazuh alert:

```
sudo logger "test alert"
```

Check:

```
TheHive → Alerts → New alert appears
```

---

## 🗂️ Alert Mapping Logic

| Wazuh Field      | TheHive Field  |
| ---------------- | -------------- |
| Rule description | Alert title    |
| Rule level       | Severity (1–4) |
| srcip/dstip      | Observables    |
| Full JSON        | Description    |
| Timestamp        | Date           |

---

## 🚨 Severity Conversion

Wazuh rule level → TheHive severity:

```
<1 → 1
>4 → 4
```

Ensures compatibility with TheHive severity scale.

---

## 🔐 Security Notes

* Use API keys — never passwords
* Restrict TheHive API access via firewall
* Store keys outside source code for production
* Use HTTPS in production deployments

---

## 🎯 Use Cases

* SOC alert pipeline
* Incident response automation
* Wazuh + TheHive lab environments
* Threat investigation workflows
* Case creation automation

---

## 🚀 Future Improvements

* Add MITRE ATT&CK mapping
* Add hostname observables
* Add hash observables
* Auto-case creation
* Alert deduplication
* Severity tuning logic
* Tag enrichment

---

## 👤 Author

Akhil R | CyberSecurity Engineer

---

## 📜 License

Lab / educational use.




