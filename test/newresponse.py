from datetime import date
import datetime

data = {
    'submission_date': datetime.date(2023, 1, 10), 
    'team_id': 'T04F75F9SKV', 
    'user_id': 'U04FX011280', 
    'user_name': 'hridesh.khandal', 
    datetime.date(2023, 1, 10): {
        'name': 'testing data 101', 
        'yesterday': 'testing yesterday', 
        datetime.date(2023, 1, 10): 
            'testing today', 
            'blocker': 'testing blocker'
        }
    }


data2 = {
    'submission_date': '2023-01-10', 
    'user_id': 'U04FX011280', 
    'team_id': 'T04F75F9SKV', 
    'user_name': 'hridesh.khandal', 
    '2023-01-10': {
        'name': 'Hridesh', 
        'yesterday': 'Was testing the data receiving from the slack bot', 
        '2023-01-10': '-  Connecting DynamoDB with the Slack Bot I have created.\n- Will be working on the Zoom attendance app', 
        'blocker': 'None'
    }
}

data3 = {
    'submission_date': '2023-01-10', 
    'user_id': 'U04J9N38MMF', 
    'team_id': 'T04F75F9SKV', 
    'user_name': 'lokendersinghshekhawa', 
    '2023-01-10': {
        'name': 'lokender', 
        'yesterday': 'done 2 coding questions', 
        '2023-01-10': 'will be studying for tomorrow iot exam', 
        'blocker': 'null'
    }
}

