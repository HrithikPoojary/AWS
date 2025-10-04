import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
table = dynamodb.Table('Data')
with table.batch_writer() as batch:
        batch.put_item(
                Item = {
                        'Data_name':'D1',
                        'Data_id': 1
                }
        )
        batch.put_item(
                Item = {
                        'Data_name':'D1',
                        'Data_id': 2
                }
        )
        batch.put_item(
                Item = {
                        'Data_name':'D1',
                        'Data_id': 3
                }
        )
        batch.put_item(
                Item = {
                        'Data_name':'D1',
                        'Data_id': 4
                }
        )
        batch.put_item(
                Item = {
                        'Data_name':'D1',
                        'Data_id': 5
                }
        )
        batch.put_item(
                Item = {
                        'Data_name':'D1',
                        'Data_id': 6
                }
        )
print("Inserted")