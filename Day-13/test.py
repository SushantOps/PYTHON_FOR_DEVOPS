import boto3

client = boto3.client('s3')

response = client.create_bucket{
    Bucket=='sushant-bucket-12e',
}

print(response)