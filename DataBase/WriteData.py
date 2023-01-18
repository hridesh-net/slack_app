import boto3

class WriteData:
    """Encapsulating an Amazon DynamoDB table of employee data
    """
    def __init__(self):
        self.dyn_resources = boto3.resource('dynamodb')
        self.table = self.dyn_resources.Table('empUpdates')
    
    def add_updates(self, data):
        self.table.put_item(
            Item=data
        )
