import boto3 #type:ignore

dynamodb = boto3.client('dynamodb',
                          endpoint_url = 'http://localhost:8000',
                          region_name = 'us-west-2a',
                          aws_access_key_id = 'fakeMyKeyId',
                          aws_secret_access_key = 'fakeSecretAccessKey'
) 
try :
        response = dynamodb.transact_write_items(
                TransactItems = [
                        {
                        'Update' : {
                        'TableName' : 'Product',
                                'Key' : {
                                        'Product_id': {'S':'p004'},
                                        'Category' : {'S' : 'Robo'}
                                },
                                'UpdateExpression' : 'set Amount = :a',
                                'ConditionExpression' : 'Amount > :val ',
                                'ExpressionAttributeValues' : 
                                        {
                                                ':a' : {'N' : '1' } ,
                                                ':val' :{'N' : '400' }
                                        },
                                'ReturnValuesOnConditionCheckFailure' : 'ALL_OLD'
                        }
                        }
                ],
                ReturnConsumedCapacity = 'INDEXES',
                ReturnItemCollectionMetrics = 'SIZE',
                ClientRequestToken = 'tx1234'
        )
        print(response)
except dynamodb.exceptions.TransactionCanceledException as e :
        print('Transaction Canceled' ,e)
