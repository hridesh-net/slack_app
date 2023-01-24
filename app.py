import os, logging
import boto3
import schedule
import time
import datetime
from datetime import date
import DataBase.DynamoData as DynamoData
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from dotenv import load_dotenv

## initializing dynamodata #####
update_data = DynamoData.DynamoData()

# Loading Environment variables
load_dotenv()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']

# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)


def log_request(logger, body, next):
    logger.debug(body)
    next()


# Listens to incoming messages that contain "hello"
@app.message("hello scrum bot")
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there submit your daily report <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Submit Report Here"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there submit your daily report <@{message['user']}>!"
    )


@app.action("button_click")
def action_button_click(body, ack, say, client, logger):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> ")
    logger.info(body)
    ack()
    # print(respond)

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "title": {
                "type": "plain_text",
                "text": "Scrum_Bot",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "type": "modal",
            "callback_id": "scrum_invoke",
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hello, please Enter your daily updates.*"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Name",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Yesterday's update",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Today's Task",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Blocker",
                        "emoji": True
                    }
                }
            ]
        }
    )
    logger.info(res)


@app.command("/scrum_bot")
def report_taker(body, ack, respond, client, logger):
    logger.info(body)
    ack()
    # print(respond)
    # print(respond)

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "title": {
                "type": "plain_text",
                "text": "Scrum_Bot",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
                "emoji": True
            },
            "type": "modal",
            "callback_id": "scrum_invoke",
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "Hello, please Enter your daily updates.*"
                    }
                },
                {
                    "type": "divider"
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Name",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Yesterday's update",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Today's Task",
                        "emoji": True
                    }
                },
                {
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Blocker",
                        "emoji": True
                    }
                }
            ]
        }
    )
    logger.info(res)


# The path that allows for your server to receive information from the modal sent in Slack
@app.view("scrum_invoke")
def view_submission(ack, body, client, logger):
    ack()
    # logger.info(body["view"]["state"]["values"])
    # print(body["user"])
    # print("\n\n")
    # print(body["view"]["state"]["values"])
    # print(body)
    name = str()
    name_id = str()
    y = str()
    y_id = str()
    t = str()
    t_id = str()
    blocker = str()
    blocker_id = str()

    # To take the block/fields IDs
    for i in body['view']['blocks']:

        if i['type'] == 'input':

            if i['label']['text'] == 'Name':

                name_id = i['block_id']

            elif i['label']['text'] == "Yesterday's update":
                y_id = i['block_id']

            elif i['label']['text'] == "Today's Task":
                t_id = i['block_id']

            elif i['label']['text'] == "Blocker":
                blocker_id = i['block_id']

    name = body['view']['state']['values'][name_id]['plain_text_input-action']['value']

    y = body['view']['state']['values'][y_id]['plain_text_input-action']['value']

    t = body['view']['state']['values'][t_id]['plain_text_input-action']['value']

    blocker = body['view']['state']['values'][blocker_id]['plain_text_input-action']['value']

    team_id = body['team']['id']

    user_id = body['user']['id']

    user_name = body['user']['name']

    submission_date = date.today()

    submission_date = str(submission_date)

    # data to send at back-end
    data_rec = {
        'submission_date': submission_date,
        'user_id': user_id,
        'team_id': team_id,
        'user_name': user_name,
        submission_date: {
            'name': name,
            'yesterday': y,
            submission_date: t,
            'blocker': blocker
        }
    }

    print("Sending Data")

    update_data.add_updates(data_rec)
    print("data send successful")

    # print(data_rec)


@app.command("/know_me")
def get_updates(body, ack, say, logger):
    logger.info(body)
    ack()
    # print(body)

    date = body['text']
    user_id = body['user_id']

    key = {
        'submission_date': date,
        'user_id': user_id
    }
    # update_data.get_data(key)
    rec_data = update_data.get_data(key)
    print(rec_data)

    say(
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Hello, your updates are.*"
                }
            },
            {
                "type": "divider"
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Yesterday updates are:",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": rec_data[date]['yesterday']
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Today's updates are:",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": rec_data[date][date]
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "plain_text",
                    "text": "Blockers:",
                    "emoji": True
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": rec_data[date]['blocker']
                }
            }
        ],
        text=f"These are your updates"
    )


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ.get("SLACK_APP_TOKEN")).start()


    # def send_message():
    #     client = WebClient(token=SLACK_BOT_TOKEN)
    #     try:
    #         # Call the chat.postMessage method using the WebClient
    #         response = client.chat_postMessage(
    #             channel="C04F79UN4RY",
    #             text="Hello world!")
    #         print(response)
    #     except SlackApiError as e:
    #         print("Error sending message: {}".format(e))
    #
    #
    # schedule.every().day.at("04:22").do(send_message)
    #
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)
