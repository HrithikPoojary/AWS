import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

table = dynamodb.create_table(
                TableName = 'Student',
                KeySchema = [
                        {'AttributeName':'Student_id',
                         'KeyType' : 'HASH'
                         }
                ],
                AttributeDefinitions = [
                        {'AttributeName':'Student_id',
                         'AttributeType': 'N'}
                ],
                ProvisionedThroughput = {
                        'ReadCapacityUnits' :1,
                        'WriteCapacityUnits':1
                }
)
print('Table Creating')
table.meta.client.get_waiter('table_exists').wait(TableName = 'Student')
print('Table Status : ' , table.table_status)