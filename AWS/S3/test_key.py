from boto3.session import Session

ACCESS_KEY = ''
SECRET_KEY = ''

session = Session(aws_access_key_id=ACCESS_KEY,
                  aws_secret_access_key=SECRET_KEY)

s3 = session.resource('s3')

bucket = s3.Bucket('akeyless-gator-cluster-backups-staging-us-east-2')

for s3_file in bucket.objects.all():
    print(s3_file.key)

# some_binary_data = b'Here we have some data'
# object = s3.Object(bucket, 'filename.txt')
# object.put(Body=some_binary_data)
