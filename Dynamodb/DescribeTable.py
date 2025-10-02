import boto3 

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
table = dynamodb.Table("Product")

response = table.meta.client.describe_table(TableName="Product")

print(response['Table'])