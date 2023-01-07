from datetime import date

body = {
    'type': 'view_submission', 
    'team': {
        'id': 'T04F75F9SKV', 
        'domain': 'testing-appglobal'
    }, 
    'user': {
        'id': 'U04FX011280', 
        'username': 'hridesh.khandal', 
        'name': 'hridesh.khandal', 
        'team_id': 'T04F75F9SKV'
    }, 
    'api_app_id': 'A04FH0VLC84', 
    'token': 'IIPPQMWdh26TDrbw1E3ksGoc', 
    'trigger_id': '4608913449218.4517185332675.9c1736b9b4d7c7130d7ea5e19c6c7a41', 
    'view': {
        'id': 'V04HGAX9HB9', 
        'team_id': 'T04F75F9SKV', 
        'type': 'modal', 
        'blocks': [
            {
                'type': 'section', 
                'block_id': 'JAvd', 
                'text': {
                    'type': 'mrkdwn', 
                    'text': 'Hello, please Enter your daily updates.*', 
                    'verbatim': False
                }
            }, 
            {
                'type': 'divider', 
                'block_id': 'IqBD'
            }, 
            {
                'type': 'input', 
                'block_id': 'sg1fZ', 
                'label': {
                    'type': 'plain_text', 
                    'text': 'Name', 
                    'emoji': True
                }, 
                'optional': False, 
                'dispatch_action': False, 
                'element': {
                    'type': 'plain_text_input', 
                    'action_id': 'plain_text_input-action',
                    'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}
                }
            }, 
            {
                'type': 'input', 
                'block_id': 'EyhaF', 
                'label': {
                    'type': 'plain_text', 
                    'text': "Yesterday's update", 
                    'emoji': True
                }, 
                'optional': False, 
                'dispatch_action': False, 
                'element': {
                    'type': 'plain_text_input', 
                    'action_id': 'plain_text_input-action', 
                    'multiline': True, 
                    'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}
                }
            }, 
            {
                'type': 'input', 
                'block_id': '55xuJ', 
                'label': {
                    'type': 'plain_text', 
                    'text': "Today's Task", 
                    'emoji': True
                }, 
                'optional': False, 
                'dispatch_action': False, 
                'element': {
                    'type': 'plain_text_input', 
                    'action_id': 'plain_text_input-action', 
                    'multiline': True, 
                    'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}
                }
            }, 
            {
                'type': 'input', 
                'block_id': 'ab9e', 
                'label': {
                    'type': 'plain_text', 
                    'text': 'Blocker',
                    'emoji': True
                }, 
                'optional': False, 
                'dispatch_action': False, 
                'element': {
                    'type': 'plain_text_input', 
                    'action_id': 'plain_text_input-action', 
                    'dispatch_action_config': {'trigger_actions_on': ['on_enter_pressed']}
                }
            }
        ], 
        'private_metadata': '', 
        'callback_id': 'scrum_invoke', 
        'state': {
            'values': {
                'sg1fZ': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input', 
                        'value': 'testing 101'
                    }
                }, 
                'EyhaF': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input',
                        'value': 'yesterday 101'
                    }
                }, 
                '55xuJ': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input', 
                        'value': 'today 101'
                    }
                }, 
                'ab9e': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input', 
                        'value': 'Blocker 101'
                    }
                }
            }
        }, 
        'hash': '1673079502.yymDRvo5', 
        'title': {
            'type': 'plain_text', 
            'text': 'Scrum_Bot', 
            'emoji': True
        }, 
        'clear_on_close': False, 
        'notify_on_close': False, 
        'close': {
            'type': 'plain_text', 
            'text': 'Cancel', 
            'emoji': True
        },
        'submit': {
            'type': 'plain_text', 
            'text': 'Submit',
            'emoji': True
        },
        'previous_view_id': None,
        'root_view_id': 'V04HGAX9HB9',
        'app_id': 'A04FH0VLC84',
        'external_id': '', 
        'app_installed_team_id': 'T04F75F9SKV',
        'bot_id': 'B04FBK8UMRB'
    }, 
    'response_urls': [], 
    'is_enterprise_install': False, 
    'enterprise': None
}

name = str()
name_id = str()
y = str()
y_id = str()
t = str()
t_id = str()
blocker = str()
blocker_id = str()

for i in body['view']['blocks']:
    # if (type(diction[key]) is not dict):
    #     print(type(diction[key]))
    #     print("\n\n")
    # else:
    #     print("this is a dictionary")
    #     print("\n\n")
    # print(i)
    if (i['type'] == 'input'):
        # print(i['label']['text'])
        if (i['label']['text'] == 'Name'):
            # print("true")
            name_id = i['block_id']
            
        elif (i['label']['text'] == "Yesterday's update"):
            y_id = i['block_id']
            
        elif (i['label']['text'] == "Today's Task"):
            t_id = i['block_id']
    
        elif (i['label']['text'] == "Blocker"):
            blocker_id = i['block_id']
    
    # break
    
    # for key in i:
    #     print(i[key])
        
    #     if (key == 'type' and i[key] == 'input'):
    #         print('true')
            
    #     print("\n\n")
    #     break

# print(name_id)
# print(y_id)
# print(t_id)
# print(blocker_id)

# print(body['view']['state']['values'][name_id]['plain_text_input-action']['value'])

name = body['view']['state']['values'][name_id]['plain_text_input-action']['value']
# print(name)

y = body['view']['state']['values'][y_id]['plain_text_input-action']['value']
# print(y)

t = body['view']['state']['values'][t_id]['plain_text_input-action']['value']
# print(t)

blocker = body['view']['state']['values'][blocker_id]['plain_text_input-action']['value']
# print(blocker)

team_id = body['team']['id']
# print(team_id)

user_id = body['user']['id']
# print(user_id)

user_name = body['user']['name']
# print(user_name)

present_date = date.today()
print(present_date)

response = {
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

print(response)

# print(body['view']['state'])