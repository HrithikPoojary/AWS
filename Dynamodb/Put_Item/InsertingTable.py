import boto3 #type: ignore

dynamodb = boto3.resource(
        'dynamodb',
        endpoint_url = 'http://localhost:8000',
        region_name = 'us-west-2a',
        aws_access_key_id = 'fakeMyKeyId',
        aws_secret_access_key = 'fakeSecretAccessKey'
)
table = dynamodb.Table("Product")

response = table.put_item(
        Item = {
                # Partition Key And Sort Key
                'Product_id' :'p001',          # S
                'Category' : 'Electronics',    # S

                # Scalar Data type
                'Name' :'Smartphone',             # s
                'Price' : 400,                 # N 
                'Stock' : 5 ,                  # N
                'ManualPDF' : b"binary_data" ,  # B
                # Document Datatype
                'Details' : {      # M -(Map/Dict)
                        'Brand':'Sumsung',
                        'Model':'Galaxy24',
                        'Features':['5G','OLED','128GB']   # L -list
                },
                #Set Types
                'Availablecolors' : {'Black','White','Blue'}, # SS
                'DiscountRates' : {5,10,15}                  # SN
        }
)

print('Item Inserted :' ,  response)