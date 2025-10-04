import boto3 #type:ignore

dynamodb = boto3.resource('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us--west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
)

response = dynamodb.create_table(
        TableName = 'Employees',
        KeySchema = [
                {'AttributeName':'Department'
                 ,'KeyType':'HASH' }
        ],
        AttributeDefinitions = [
                {'AttributeName':"Department"
                 ,'AttributeType':'S'}
        ],
        ProvisionedThroughput = {
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
        }
)
print('Table Created')