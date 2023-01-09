import boto3

# Get the service resource.
dynamodb = boto3.resources('dynamodb')

# Create the DynamoDB table
table = dynamodb.create_table(
    TableName='empUpdates',
    KeySchema=[
        {'AttributeName': 'date', 'type': 'HASH'},          # Partition Key
        {'AttributeName': 'user_id', 'type': 'RANGE'}       # Sort Key
    ],
                    
    AttributeDefinitions=[
        {'AttributeName': 'date', 'AttributeType': 'N'},
        {'AttributeName': 'user_id', 'AttributeType': 'S'}
    ],
    ProvisionedThroughput={'ReadCapacityUnits': 10, 'WriteCapacityUnits': 10}
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)