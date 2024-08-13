import requests
import json
import os

def send_to_discord(message):
    webhook_url = "https://discordapp.com/api/webhooks/1214036002000207902/AispkCs7rD2llyKHhA6BIvnRxLaqd3buvEIH3vGzvZtLDW93OSJEWhYH1HyUbezv04eU"
    if webhook_url:
        payload = {
            "content": message
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Failed to send message to Discord:", response.text)

if __name__ == "__main__":
    send_to_discord("Kubernetes Tests Finished")
