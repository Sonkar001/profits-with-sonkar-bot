import time
import requests
import os

# ==== CONFIG ====
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# ==== FUNCTION ====
def send_telegram(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    print("📩 Telegram response:", response.text)

# ==== MAIN ====
print("✅ Profits with Sonkar™ scalping bot is now running...")
send_telegram("🟢 Test alert: Profits with Sonkar™ bot has started successfully!")
print("✅ Test completed. Telegram message sent.")

# Prevent early exit
while True:
    time.sleep(60)  # keep alive so Render doesn't mark it as failed
