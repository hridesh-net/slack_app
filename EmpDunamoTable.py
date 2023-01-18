import boto3
from datetime import date

# Get the service resource.
dynamodb = boto3.resource('dynamodb')
#
# # Create the DynamoDB table.
# table = dynamodb.create_table(
#     TableName='empUpdates',
#     KeySchema=[
#         {
#             'AttributeName': 'submission_date',
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'user_id',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'submission_date',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'user_id',
#             'AttributeType': 'S'
#         },
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 10,
#         'WriteCapacityUnits': 10
#     }
# )
#
# # Wait until the table exists.
# table.wait_until_exists()
#
# # Print out some data about the table.
# print(table.item_count)

table = dynamodb.Table('empUpdates')

print(table.creation_date_time)

Date = date.today()

Date = str(Date)

data = {
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

table.put_item(
    Item = data
)

print('data sent to dynamodb')