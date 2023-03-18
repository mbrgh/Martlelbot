import os
import requests
import time

bot_token = os.environ['BOT_TOKEN']
chat_id = os.environ['CHAT_ID']
username = os.environ['USERNAME']
password = os.environ['PASSWORD']
url = os.environ['URL']

data = {'username': username, 'password': password}

while True:
    response = requests.post(url, data=data)
    response_text = response.text
    print(response_text)  # Print the response from the server
    
    # Send the response text to the chat using Telegram Bot API
    if bot_token and chat_id:
        telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        telegram_data = {"chat_id": chat_id, "text": response_text}
        requests.post(telegram_url, data=telegram_data)

    time.sleep(240)  # Wait for 4 minutes
