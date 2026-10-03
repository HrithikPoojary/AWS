import json
import boto3 #type:ignore

def lambda_handler(event, context):
    
    dynamodb = boto3.client("dynamodb")

    response = dynamodb.create_table(
        TableName = 'transaction',
        AttributeDefinitions = [
            {
                "AttributeName" : "transaction_id",
                "AttributeType" : 'N'
            },
            {
                "AttributeName" : "account_number",
                "AttributeType" : "S"
            },
            {
                "AttributeName":"asset_external_id",
                "AttributeType" : "S"
            }
        ] ,
        KeySchema = [

           {
            "AttributeName":"transaction_id",
            "KeyType" : "HASH"
           }
        ],

        GlobalSecondaryIndexes = [

                    {
                        "IndexName" : "Account_Asset_GSI",
                        "KeySchema" : [
                            {
                                "AttributeName" : "account_number",
                                "KeyType" : "HASH" 
                            },
                            {
                                "AttributeName" : "asset_external_id",
                                "KeyType" : "RANGE"
                            }
                        ],
                        "Projection" :{
                            "ProjectionType" : "ALL"
                                        },
                                        
                        "ProvisionedThroughput" : {
                            "ReadCapacityUnits" :2,
                            "WriteCapacityUnits" :2
                        }
                        
                    }

         ],
        ProvisionedThroughput = {
            "ReadCapacityUnits" : 2,
            "WriteCapacityUnits" : 2
        },
        StreamSpecification = {
            "StreamEnabled" : True,
            "StreamViewType" : "NEW_AND_OLD_IMAGES"
        }
    )


    return {
        'statusCode': 200,
        'response': "Transaction table has been created" 
    }
