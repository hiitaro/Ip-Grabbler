# 🔎IPGrabbler

**IPGrabbler** is a simple Flask utility for tracking visitors to a web page. Each time the main page (`/`) is visited, the service saves visitor information to a log file and sends a notification to Telegram.

## 🔧️How it works

1. When a user visits the main page:
    - The IP address and User-Agent are determined.
    - Additional IP information is retrieved via [ip-api.com](https://ip-api.com/).
    - All data (IP, time, country, region, city, ISP, organization, coordinates, User-Agent) are saved to `logs.json`.
    - A Telegram notification is sent with visit details.

2. The user sees a message that their visit has been logged.

## 📁Files

- `ipgrabbler.py` — main Flask application script.
- `logs.json` — log of all visits.

## 🛠️Setup

1. Install dependencies:
    git clone:
    ```sh
    git clone https://github.com/hiitaro/Ip-Grabbler.git
    cd Ip-Grabbler
    ```
    ```sh
    pip install flask requests
    ```
    or
    ```sh
    pip install -r requirements.txt
    ```
2. Set your Telegram token and chat_id in the `TELEGRAM_TOKEN` and `TELEGRAM_CHAT_ID` variables in [`ipgrabbler.py`](ipgrabbler.py).
3. Run the application:
    ```sh
    python ipgrabbler.py
    ```
4. Open `http://localhost:5000/` in your browser.

---

## 📄Json example:
```json
[
  {
    "ip": "127.0.0.1",
    "time": "2025-06-10 19:35:27",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 OPR/119.0.0.0",
    "country": null,
    "region": null,
    "city": null,
    "isp": null,
    "org": null,
    "lat": null,
    "lon": null
  }
]
```

## ⚠️Warning

- Use for educational purposes and on your own resources only.
- Do not use to track users without their consent.
