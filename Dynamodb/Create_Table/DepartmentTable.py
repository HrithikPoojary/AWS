import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

response = dynamodb.create_table(
        TableName = 'Department',
        KeySchema = [
                {'AttributeName':'department','KeyType':'HASH'},
                {'AttributeName':'employee_id','KeyType':'RANGE'}
        ],
        AttributeDefinitions = [
                {'AttributeName':'department','AttributeType':'S'},
                {'AttributeName' : 'employee_id','AttributeType':'S'},
                {'AttributeName' : 'salary','AttributeType':'N'},
                {'AttributeName' : 'role','AttributeType':'S'},
                {'AttributeName' : 'joindate','AttributeType':'S'}
        ],
        LocalSecondaryIndexes = [
                {
                        'IndexName' : 'Department-Salary-Index',
                        'KeySchema' : [
                               { 'AttributeName':'department', 'KeyType':'HASH'},
                               {'AttributeName':'salary','KeyType':'RANGE'}
                        ],
                        'Projection' : {
                                'ProjectionType' : 'INCLUDE',
                                'NonKeyAttributes' : ['joindate']
                        }
                }
        ],
        GlobalSecondaryIndexes = [
                {
                        'IndexName': 'Role-Join-Index',
                        'KeySchema' : [
                                {'AttributeName' : 'role','KeyType':'HASH' },
                                {'AttributeName' : 'joindate','KeyType':'RANGE' }
                        ],
                        'Projection' : {
                                'ProjectionType' : 'ALL'
                        },
                        'ProvisionedThroughput' : {
                                'ReadCapacityUnits':1,
                                'WriteCapacityUnits':1
                        }
                }
        ],
        ProvisionedThroughput = {
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
        }
        
)
print('Table Created')
print(response)