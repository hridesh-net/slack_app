import boto3


class DynamoData:
    """Encapsulating an Amazon DynamoDB table of employee data
    """

    def __init__(self):
        self.dyn_resources = boto3.resource('dynamodb')
        self.table = self.dyn_resources.Table('empUpdates')

    def add_updates(self, data):
        self.table.put_item(
            Item=data
        )

    def get_data(self, key_parameter):
        # print(key_parameter)
        response_data = self.table.get_item(
            Key={
                'submission_date': key_parameter['submission_date'],
                'user_id': key_parameter['user_id']
            }
        )
        # print(response_data)
        # print("\n\n")
        item = response_data['Item']
        # print(item)
        return item
