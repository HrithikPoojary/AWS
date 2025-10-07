import boto3 #type:ignore

dynamodb = boto3.client('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us-west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
) 

response = dynamodb.transact_get_items(
        TransactItems = [
                {
                        'Get' : {
                                'TableName' : 'Product',
                                'Key' : {
                                        'Product_id': {'S':'p004'},
                                        'Category' : {'S':'Robo'}
                                },
                                'ProjectionExpression' : 'Category , Amount'
                        }
                }
        ]
)
print(response)