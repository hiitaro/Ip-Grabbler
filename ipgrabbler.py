from flask import Flask, request
import json
import os
from datetime import datetime
import requests

app = Flask(__name__)

LOG_FILE = "logs.json"
TELEGRAM_TOKEN = "YOUR_BOT_TOKEN"
TELEGRAM_CHAT_ID = "YOUR_TELEGRAM_CHAT_ID"

def get_ip_info(ip):
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719", timeout=5)
        return resp.json()
    except:
        return {"status": "fail"}

def send_telegram_alert(log_entry):
    message = (
        f"📡 New Visitor\n\n"
        f"IP: {log_entry['ip']}\n"
        f"Country: {log_entry.get('country')} ({log_entry.get('region')})\n"
        f"City: {log_entry.get('city')}\n"
        f"Time: {log_entry['time']}\n"
        f"Org: {log_entry.get('org')}\n"
        f"User-Agent:\n{log_entry['user_agent']}"
    )
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload, timeout=5)
    except:
        pass

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent')
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    info = get_ip_info(ip)
    log_entry = {
        "ip": ip,
        "time": time_now,
        "user_agent": ua,
        "country": info.get("country"),
        "region": info.get("regionName"),
        "city": info.get("city"),
        "isp": info.get("isp"),
        "org": info.get("org"),
        "lat": info.get("lat"),
        "lon": info.get("lon")
    }
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        data = []
    data.append(log_entry)
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    send_telegram_alert(log_entry)
    return "<h1>You got tracked 👀</h1><p>Your visit has been logged.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
