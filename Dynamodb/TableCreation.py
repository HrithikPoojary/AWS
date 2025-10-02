import boto3 #type:ignore

dynamodb = boto3.resource('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us--west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
)

table  = dynamodb.create_table(
        TableName = 'Product',
        KeySchema = [
                {'AttributeName':'Product_id',
                 'KeyType':'HASH'} ,
                {'AttributeName':'Category',
                 'KeyType':'RANGE'}
        ],
        AttributeDefinitions = [
                {'AttributeName':'Product_id',
                 'AttributeType':'S'},
                {'AttributeName' : 'Category',
                 'AttributeType':'S'}
        ],
        ProvisionedThroughput = {
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
        }
)

print(f"Table Created  {table}")
table.meta.client.get_waiter("table_exists").wait(TableName='Product')
print('Table Status' , table.table_status)