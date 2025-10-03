import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
dynamodb.create_table(
        TableName = 'Data',
        KeySchema = [
                {'AttributeName' : 'Data_name', 
                'KeyType' : 'HASH'},
                {'AttributeName' :'Data_id',
                 'KeyType' : 'RANGE'}
        ],
        AttributeDefinitions = [
                {'AttributeName':'Data_name',
                 'AttributeType':'S'},
                 {'AttributeName':'Data_id',
                  'AttributeType':'N'}
        ],
        ProvisionedThroughput = {
                'ReadCapacityUnits' : 1,
                'WriteCapacityUnits' :1
        }
)
print('Created')