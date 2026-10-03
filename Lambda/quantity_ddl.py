import json
import boto3 #type:ignore

def lambda_handler(event, context):

    dynamodb = boto3.client("dynamodb")

    quantity = dynamodb.create_table(
        TableName = "quantity",
        AttributeDefinitions = [
            {
                "AttributeName" : "account_number",
                "AttributeType" : "S"
            },
            {
                "AttributeName" : "asset_external_id",
                "AttributeType" : "S"
            }
        ],
        KeySchema = [
            {
                "AttributeName" : "account_number",
                "KeyType" : "HASH"
            },
            {
                "AttributeName" : "asset_external_id",
                "KeyType" : "RANGE"
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
        'body': json.dumps('Quantity Table has been created!')
    }
