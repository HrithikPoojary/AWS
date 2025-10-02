import boto3

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
table = dynamodb.Table('Product')

with table.batch_writer() as batch :
        batch.put_item(
                Item = {
                        'Product_id':'p002',
                        'Category' : 'Laptop',
                        'Name':'MacBook2',
                        'Price':300,
                        'Colour' :{'White', 'Black','Blue'}
                }
        )
        batch.put_item(
                Item = {
                        'Product_id' : 'p003',
                        'Category':'Watch',
                        'Name' : 'PeterEnglad',
                        'Price' : 100,
                        'AvailableDiscout' : {
                                'ICIC':[1,3,1],
                                'Axis':[3,4,6],
                                'HDFC':[5,7,8,8]
                        }
                }
        )
print('Inserted 2 data Successfully')