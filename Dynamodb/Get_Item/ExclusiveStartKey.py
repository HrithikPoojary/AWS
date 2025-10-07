import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

product = dynamodb.Table('Product')
response = product.scan()

items = response['Items']
print(response)
while 'LastEvaluateKey' in response:
        response = product.scan(
                ExclusiveStartKey = response['LastEvaluateKey']
        )
        items.extend(response['Items'])
print(items)