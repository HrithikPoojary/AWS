import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
table = dynamodb.Table('Student')

with table.batch_writer() as batch:
        batch.put_item(
                Item = {
                        'Student_id' : 1,
                        'Name' : 'Luffy',
                        'Department':'Caption'
                }
        )
        batch.put_item(
                Item = {
                        'Student_id': 2,
                        'Name' :'Zoro' ,
                        'Deaprtment' :'Swordsman'
                }
        )
        batch.put_item(
                Item = {
                        'Student_id' :3,
                        'Name' :'Nami' ,
                        'Deparment': 'Navigator'
                }
        ),
        batch.put_item(
                Item = {
                        'Student_id' :4,
                        'Name' :'Ussop' ,
                        'Deparment': 'Sniper'
                }
        )
        batch.put_item(
                Item = {
                        'Student_id' :5,
                        'Name' :'Sanji' ,
                        'Deparment': 'Cook'
                }
        )

print('Inserted successfully')