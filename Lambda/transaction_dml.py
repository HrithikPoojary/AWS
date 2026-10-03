import json
import boto3        #type:ignore


def lambda_handler(event, context):
    
    dynamo_db = boto3.resource("dynamodb")

    table = dynamo_db.Table("transaction")

    with table.batch_writer() as batch:

        batch.put_item(
            Item = {
            "transaction_id" : 456,
            "account_number" : "68750-90796",
            "asset_external_id" : "AMZN"
            }
        )


    return {
        'statusCode': 200,
        'body': json.dumps('Data has been inserted!')
    }
