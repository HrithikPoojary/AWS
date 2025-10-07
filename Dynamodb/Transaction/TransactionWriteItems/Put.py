import boto3 #type:ignore

dynamodb = boto3.client('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us-west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
) 
response = dynamodb.transact_write_items(
        TransactItems = [
                # Put
                {
                'Put' : {
                                'TableName' : 'Product',
                                'Item' : 
                                {
                                        'Product_id' : {'S' : 'p004'},
                                        'Category' : {'S' : 'Robo'},
                                        'Amount' : {'N' : '500'}
                                },
                                'ConditionExpression' : 'attribute_not_exists(Amount)',
                                'ReturnValuesOnConditionCheckFailure' : 'ALL_OLD'
                        }

                }
        ] 
)
print(response)