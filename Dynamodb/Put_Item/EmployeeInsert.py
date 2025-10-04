import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
employees = dynamodb.Table('Employees')

with employees.batch_writer() as batch :
        batch.put_item(
                Item = {
                        'emd_id':'e1',
                        'name':'Luffy',
                        'Department':'captain',
                        'bounty':3000
                }
        )
        batch.put_item(
                Item = {
                        'emd_id':'e2',
                        'name':'Zoro',
                        'Department':'swardsman',
                        'bounty':1100
                }
        )
        batch.put_item(
                Item = {
                        'emd_id':'e3',
                        'name':'Nami',
                        'Department':'navigator',
                        'bounty':500
                }
        )
print('Employees Table has been inserted successfully')