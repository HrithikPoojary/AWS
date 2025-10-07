import boto3 #type:ignore

dynamodb = boto3.client('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us-west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
) 
response = dynamodb.transact_write_items(
        TransactItems = [
                {
                        'ConditionCheck' : {
                                'TableName' : 'Product',
                                'Key' : {
                                        'Product_id': {'S' : 'p004'},
                                        'Category' : {'S' : 'Robo'}
                                },
                                'ConditionExpression' : 'Amount > :val',
                                'ExpressionAttributeValues' : {
                                        ':val' : {'N': '400'}
                                },
                                'ReturnValuesOnConditionCheckFailure' : 'ALL_OLD'

                        }
                }
        ],
        ReturnConsumedCapacity = 'INDEXES'
)
for i in response:
        print(i)