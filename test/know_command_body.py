import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('empUpdates')

body = {
    'token': 'IIPPQMWdh26TDrbw1E3ksGoc', 
    'team_id': 'T04F75F9SKV', 
    'team_domain': 'testing-appglobal', 
    'channel_id': 'C04F79UN4RY', 
    'channel_name': 'slack-application', 
    'user_id': 'U04FX011280', 
    'user_name': 'hridesh.khandal', 
    'command': '/know', 
    'text': '2023-01-18', 
    'api_app_id': 'A04FH0VLC84', 
    'is_enterprise_install': 'false', 
    'response_url': 'https://hooks.slack.com/commands/T04F75F9SKV/4660781019285/SiguFiJ1m3T6PMo7tQlZijMx', 
    'trigger_id': '4666191907508.4517185332675.f6bf5e19699b8473586ae562f0f73d13'
}

date = body

response = table.get_item(
    Key={
        'submission_date': body['text'],
        'user_id': body['user_id']
    }
)
print(response)
print("\n\n")
item = response['Item']
print(item)



######## response output ################
AWS_DDb_response = {
    'Item': {
        '2023-01-18': {
            'name': 'test103', 
            'yesterday': 'yesterday', 
            'blocker': 'none', 
            '2023-01-18': 'today'
        }, 
        'submission_date': '2023-01-18', 
        'user_id': 'U04FX011280', 
        'team_id': 'T04F75F9SKV', 
        'user_name': 'hridesh.khandal'
    }, 
    'ResponseMetadata': {
        'RequestId': 'GV68S4L80SLT1Q2KNPGMMQGN8BVV4KQNSO5AEMVJF66Q9ASUAAJG', 
        'HTTPStatusCode': 200, 
        'HTTPHeaders': {
            'server': 'Server', 
            'date': 'Wed, 18 Jan 2023 20:20:31 GMT', 
            'content-type': 'application/x-amz-json-1.0', 
            'content-length': '267', 
            'connection': 'keep-alive', 
            'x-amzn-requestid': 'GV68S4L80SLT1Q2KNPGMMQGN8BVV4KQNSO5AEMVJF66Q9ASUAAJG', 
            'x-amz-crc32': '3716600900'
        }, 
        'RetryAttempts': 0
    }
}

AWS_DDb_Item = {
    '2023-01-18': {
        'name': 'test103', 
        'yesterday': 'yesterday', 
        'blocker': 'none', 
        '2023-01-18': 'today'
    }, 
    'submission_date': '2023-01-18', 
    'user_id': 'U04FX011280', 
    'team_id': 'T04F75F9SKV', 
    'user_name': 'hridesh.khandal'
}