import os, logging
from datetime import date
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
# from dotenv import load_dotenv
#
# load_dotenv()
# SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
# SLACK_APP_TOKEN = os.environ['SLACK_APP_TOKEN']

slack_app_token = 'xapp-1-A04FH0VLC84-4516027161495-b6a13d5b9509bbb2c7211631f08e059a1d07f84f980451c548e9ef227594429f'
# Initializes your app with your bot token and socket mode handler
app = App(token='xoxb-4517185332675-4524600647986-cr65m8SnFFpkVscOoB3yhZAn')


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

        if (i['type'] == 'input'):

            if (i['label']['text'] == 'Name'):

                name_id = i['block_id']

            elif (i['label']['text'] == "Yesterday's update"):
                y_id = i['block_id']

            elif (i['label']['text'] == "Today's Task"):
                t_id = i['block_id']

            elif (i['label']['text'] == "Blocker"):
                blocker_id = i['block_id']
    
    name = body['view']['state']['values'][name_id]['plain_text_input-action']['value']
    
    y = body['view']['state']['values'][y_id]['plain_text_input-action']['value']

    t = body['view']['state']['values'][t_id]['plain_text_input-action']['value']

    blocker = body['view']['state']['values'][blocker_id]['plain_text_input-action']['value']
    
    team_id = body['team']['id']
    
    user_id = body['user']['id']
    
    user_name = body['user']['name']
    
    present_date = date.today()
    
    # data to send at back-end
    data_rec = {
        'date': present_date,
        'team_id': team_id,
        'user_id': user_id,
        'user_name': user_name,
        'user_response': {
            'name': name,
            'yesterday': y,
            present_date: t,
            'blocker': blocker
        }
    }
    
    print(data_rec)


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, slack_app_token).start()