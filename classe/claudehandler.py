import requests
import json

class Claude:
    def __init__(self):
        self.api_key = 'Bearer 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'

    def send_chat_message(self,message):
        endpoint = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": self.api_key,
            "Content-Type": "application/json"
        }
        data = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "system", "content": "You are a expert english proffesor with over 50 years of experience, only complete the assignment nothing more. Responses will be at mininum 50 words in length, no matter how short the message."},
                         {"role": "user", "content": message}],
            "max_tokens": 1000
        }

        response = requests.post(endpoint, headers=headers, data=json.dumps(data))
        response_json = response.json()

        try:
            return response_json['choices'][0]['message']['content']
        except:
            return 'Error: Could not send message'
