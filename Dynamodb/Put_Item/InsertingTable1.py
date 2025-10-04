import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

table = dynamodb.Table('Product')

with table.batch_writer() as batch:
        batch.put_item(
                Item = {
                        'Product_id' : 'p004',
                        'Category' : 'Bus',
                        'Name' : 'Vehicale'
                }
        )
        batch.put_item(
                Item = {
                        'Product_id' : 'p005',
                        'Category' : 'Plane',  
                        'Name':'Laptop'
                }
        )
print('Inserted 3 items')