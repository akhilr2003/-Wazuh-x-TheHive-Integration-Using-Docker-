#!/usr/bin/env python3
import json, sys, requests, os

THEHIVE_URL = os.environ.get("THEHIVE_URL", "http://THEHIVE_IP_OR_HOST:9000")
API_KEY     = os.environ.get("THEHIVE_API_KEY")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Read alert JSON: argv[1] (file path from Wazuh) OR stdin (manual tests)
def read_alert():
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        with open(sys.argv[1], "r") as f:
            return json.load(f)
    return json.load(sys.stdin)

alert = read_alert()

# Build payload
severity = int(alert.get('rule', {}).get('level', 3))
if severity < 1: severity = 1
if severity > 4: severity = 4  # TheHive 5 expects 1–4

payload = {
  "title": f"Wazuh alert - {alert.get('rule', {}).get('description', 'No description')}",
  "source": "wazuh",
  "sourceRef": f"wazuh-{int(os.times().elapsed)}",
  "severity": severity,
  "type": "wazuh_alert",
  "date": int(alert.get('@timestamp', 0)) if isinstance(alert.get('@timestamp', 0), int) else None,
  "tags": ["wazuh"],
  "observables": [o for o in [
      {"dataType": "ip", "data": alert.get('srcip')} if alert.get('srcip') else None,
      {"dataType": "ip", "data": alert.get('dstip')} if alert.get('dstip') else None
  ] if o],
  "description": json.dumps(alert)
}

r = requests.post(f"{THEHIVE_URL}/api/v1/alert", headers=headers, data=json.dumps(payload), timeout=15)
print(r.status_code, r.text)