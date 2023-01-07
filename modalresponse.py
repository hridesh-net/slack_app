{
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
