import requests
import json
from time import sleep


class Undetectable:
    def __init__(self):
        self.api_key = '1687794215217x250146038102561760'

    def send_message(self, message):
        url = "https://api.undetectable.ai/submit"
        headers = {
            'api-key': '1687794215217x250146038102561760',
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "content": f"{message}",
            "readability": "University",
            "purpose": "General Writing"
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        response = response.json()['id']
        sleep(45)
        url = "https://api.undetectable.ai/document"
        payload = json.dumps({
            "id": response
        })
        response = requests.request("POST", url, headers=headers, data=payload)
        response.raise_for_status()
        return response.json()['output']