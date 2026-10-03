import json
from boto3.dynamodb.types import TypeDeserializer  #type:ignore
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def deserializer_type(item):

    deserializer = TypeDeserializer()

    return {
        k: deserializer.deserialize(v)
        for k,v in item.items()
    }

def lambda_handler(event, context):
    
    records = event["Records"]

    for record in records:

        item = deserializer_type(record["dynamodb"]["NewImage"])

        logger.info(
            f"The transaction for {item['asset_external_id']} "
            f"of quantity {item['quantity']} is successful!"
            )


    return {
        'statusCode': 200,
        'body': "Successfull"
    }
