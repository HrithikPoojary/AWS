import boto3 #type:ignore

dynamodb = boto3.client(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

response = dynamodb.update_table(
        TableName = 'Product',
        StreamSpecification = {
                'StreamEnabled' : True ,
                'StreamViewType' : 'NEW_AND_OLD_IMAGES'
        }
)
for i in response:
        print(i)