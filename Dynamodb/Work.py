import boto3 #type:ignore
from boto3.dynamodb.conditions import Key,Attr #type:ignore
dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)


table = dynamodb.Table('Product')
empty = []
lists = ['p004','p001']
for i in lists:
        response = table.query(
                KeyConditionExpression = Key('Product_id').eq(i)
                                )
        empty.append(response)

for i in range(0,len(empty)):
        print(empty[i]['Items'][0]['Product_id'])