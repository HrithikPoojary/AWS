import boto3

s3_resource = boto3.resource('s3')

bucket_name = s3_resource.Bucket('snowflake-bucket-inv')

bucket_name.put_object(Key = 'loadingdata/')
