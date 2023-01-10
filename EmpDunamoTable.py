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

table.put_item(
    Item = {
        'submission_date': Date,
        'team_id': 'T04F75F9SKV', 
        'user_id': 'U04FX011280', 
        'user_name': 'hridesh.khandal', 
        Date: {
            'name': 'testing data 101', 
            'yesterday': 'testing yesterday', 
            Date: 'testing today',
            'blocker': 'testing blocker'
        }
    }
)

print('data sent to dynamodb')