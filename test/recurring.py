import os
import schedule
import time
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv

load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']
SLACK_TOKEN = os.environ['SLACK_BOT_TOKEN']


def send_message():
    client = WebClient(token=SLACK_TOKEN)
    try:
        # Call the chat.postMessage method using the WebClient
        response = client.chat_postMessage(
            channel="#general",
            text="Hello world!")
        print(response)
    except SlackApiError as e:
        print("Error sending message: {}".format(e))


schedule.every().day.at("18:36").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
