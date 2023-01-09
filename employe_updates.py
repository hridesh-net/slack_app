class EmpUpdates:
    """Encapsulates an Amazon DynamoDB table of employees daily update data
    """
    
    def __init__(self) -> None:
        """:param dyn_resource: A Boto3 DynamoDB resource
        """
        self.dyn_resource = dyn_resource
        self.table = None
    
    def create_table(self, table_name):
        """
        Creates an Amazon DynamoDB table that can be used to store emp. updates date.
        The table uses the Date of submission as the partition key and the employee ID[user_id in the slack] as sort key. 

        Args:
            table_name (_str()_): The name of the table to create.
        
        return:
            The newly created table        
        
        """
        try:
            self.table = self.dyn_resource.create_table(
                TableName = table_name,
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
            self.table.wait_until_exists()
        except ClientError as err:
            logger.error(
                "Couldn't create table %s. Here's why: %s: %s", table_name, err.response['Error']['Code'], err.response['Error']['Message']
            )
            raise
        else:
            return self.table