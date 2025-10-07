import boto3 #type:ignore

dynamodb  = boto3.client(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)

response= dynamodb.batch_get_item(
        RequestItems = {
                'Product' :
                        {'Keys' : [ 
                                {'Product_id' : {'S' : 'p001'},
                                'Category' : {'S' : 'Electronics'}} 
                                ],
                                'ProjectionExpression' : 'Product_id , Category'
                        } ,
                'Employees' : {
                        'Keys' : [
                                {'Department' :{'S' : 'captain'}}
                        ],
                        'ProjectionExpression' : 'Department'
                }
        },
        ReturnConsumedCapacity = 'TOTAL'
)
print(response)