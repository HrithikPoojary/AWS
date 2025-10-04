import boto3 #type:ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-east-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
employees = dynamodb.Table('Department')

with employees.batch_writer() as batch :
        batch.put_item(
                Item = {
                        'department':'d1',
                        'employee_id':'e1',
                        'salary':100,
                        'role':'Manager',
                        'joindate': 'no'
                }
        )
        batch.put_item(
                Item = {
                        'department':'d2',
                        'employee_id':'e2',
                        'salary':10,
                        'role':'HR',
                        'joindate': 'mon'
                }
        )
        batch.put_item(
                Item = {
                        'department':'d3',
                        'employee_id':'e3',
                        'salary':50,
                        'role':'Developer',
                        'joindate': 'sun'
                }
        )
print('Employees Table has been inserted successfully')