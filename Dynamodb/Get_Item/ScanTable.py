import boto3 # type: ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

table = dynamodb.Table('Product')

response = table.scan()

for item in response['Items']:
        print(item)