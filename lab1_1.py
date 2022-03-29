import io
import boto3

BUCKET_NAME = 'mardo-test-12345'

s3 = boto3.resource('s3')
s3.create_bucket(Bucket=BUCKET_NAME)
# bucket = s3.Bucket(BUCKET_NAME)
# bucket.delete()
bucket_versioning = s3.BucketVersioning(BUCKET_NAME)
bucket_versioning.enable()

with open('hello.txt', 'w') as f:
    f.write('Hello, Python and AWS!')

s3.meta.client.upload_file("hello.txt", BUCKET_NAME, 'hello-in-bucket.txt')
file_object = io.BytesIO(b'Created in memory!')
s3.meta.client.upload_fileobj(file_object, BUCKET_NAME, 'data-from-mem.txt')
file_object = io.BytesIO(b'Created in memory ver. 2!')
s3.meta.client.upload_fileobj(file_object, BUCKET_NAME, 'data-from-mem-2.txt',
                              ExtraArgs={
                                  'Metadata': {'createdBy': 'process'},
                                  'ACL': 'public-read',
                                  # 'GrantRead': 'uri="http://acs.amazonaws.com/groups/global/AllUsers"',
                              })

bucket = s3.Bucket(BUCKET_NAME)
for o in bucket.objects.all():
    print(o.get()['Body'].read())