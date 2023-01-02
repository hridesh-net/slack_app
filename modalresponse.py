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
    'trigger_id': '4578845983845.4517185332675.ce97912567e4d4cd7026737693d179ef',
    'view': {
        'id': 'V04H0QVKELD',
        'team_id': 'T04F75F9SKV',
        'type': 'modal',
        'blocks': [
            {
                'type': 'section',
                'block_id': 'PdO',
                'text': {
                    'type': 'mrkdwn',
                    'text': 'Hello,please Enter your daily updates.*',
                    'verbatim': False
                }
            },
            {
                'type': 'divider',
                'block_id': 'sVrq'
            },
            {
                'type': 'input',
                'block_id': 'I89',
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
                    'dispatch_action_config': {
                        'trigger_actions_on': ['on_enter_pressed']
                    }
                }
            },
            {
                'type': 'input',
                'block_id': 'ogsf',
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
                    'dispatch_action_config': {
                        'trigger_actions_on': ['on_enter_pressed']
                    }
                }
            },
            {
                'type': 'input',
                'block_id': 'SlDj',
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
                    'dispatch_action_config': {
                        'trigger_actions_on': ['on_enter_pressed']
                    }
                }
            },
            {
                'type': 'input',
                'block_id': 'S1Q',
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
                    'dispatch_action_config': {
                        'trigger_actions_on': ['on_enter_pressed']
                    }
                }
            }
        ],
        'private_metadata': '',
        'callback_id': 'scrum_invoke',
        'state': {
            'values': {
                'I89': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input',
                        'value': 'testing modal'
                    }
                },
                'ogsf': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input',
                        'value': 'testing body'
                    }
                },
                'SlDj': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input',
                        'value': 'testing modal response'
                    }
                },
                'S1Q': {
                    'plain_text_input-action': {
                        'type': 'plain_text_input',
                        'value': 'none'
                    }
                }
            }
        },
        'hash': '1672521371.0gu1fbLw',
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
        'root_view_id': 'V04H0QVKELD',
        'app_id': 'A04FH0VLC84',
        'external_id': '',
        'app_installed_team_id': 'T04F75F9SKV',
        'bot_id': 'B04FBK8UMRB'
    },
    'response_urls': [],
    'is_enterprise_install': False,
    'enterprise': None
}
