import boto3 #type:ignore
from boto3.dynamodb.conditions import Key,Attr #type:ignore
dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

table = dynamodb.Table('Student')

response = table.get_item(
        Key = {
                'Student_id':5
        }
)
print(response['Item'])