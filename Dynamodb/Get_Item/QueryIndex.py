import boto3 #type:ignore
from boto3.dynamodb.conditions import Key,Attr #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
department = dynamodb.Table('Department')
response = department.query(
        IndexName = 'Department-Salary-Index',
        KeyConditionExpression = Key('department').eq('d1') & Key('salary').eq(100)
)
print(response['Items'])