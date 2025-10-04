import boto3 #type:ignore

dynamodb = boto3.resource('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us-west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
) 
product = dynamodb.Table('Product')

response = product.update_item(
        Key = {
                'Product_id' : 'p001',
                'Category' : 'Electronics'
        },
        UpdateExpression = "ADD Price :p , Availablecolors :c",
        ExpressionAttributeValues = {
                ':p' : 10,
                ':c' : {'Red','White'}
        },
        ReturnValues = 'UPDATED_NEW'
)
print(response)

