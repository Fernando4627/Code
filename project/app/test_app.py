import unittest
import requests
import json
from pymongo import MongoClient

class TestWebApp(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://web:8080"
        self.webhook_url = "https://discordapp.com/api/webhooks/1214036002000207902/AispkCs7rD2llyKHhA6BIvnRxLaqd3buvEIH3vGzvZtLDW93OSJEWhYH1HyUbezv04eU"

    def send_to_discord(self, message):
        payload = {
            "content": message
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(self.webhook_url, data=json.dumps(payload), headers=headers)
        if response.status_code != 200:
            print("Failed to send message to Discord:", response.text)

    def test_hello_endpoint(self):
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, 'Welcome to the Python web app!')
        self.send_to_discord("Hello Endpoint Test Passed")

    def test_login(self):
        data = {"username": "username", "password": "password"}
        response = requests.post(self.base_url + '/login', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Login successful")
        self.send_to_discord("Login Test Passed")

    def test_comment(self):
        data = {"comment": "This is a test comment."}
        response = requests.post(self.base_url + '/comment', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Comment added successfully")
        self.send_to_discord("Comment Test Passed")

    def test_email(self):
        data = {"email": "test@example.com"}
        response = requests.post(self.base_url + '/email', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Email submitted successfully")
        self.send_to_discord("Email Test Passed")

if __name__ == '__main__':
    unittest.main()

