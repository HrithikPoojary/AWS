import boto3 #type:ignore
from boto3.dynamodb.conditions import Attr,Key #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
product = dynamodb.Table('Product')

response = product.scan(Limit =3)

# for i in response:
#         print(i)
print(response['Items'])