import boto3 #type:ignore
from boto3.dynamodb.conditions import Attr #type: ignore
dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
table = dynamodb.Table('Product')

response = table.scan(
        FilterExpression = Attr('Category').eq('Electronics')
)
for item in response['Items']:
        print(item)