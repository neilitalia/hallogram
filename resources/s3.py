from dotenv import load_dotenv, find_dotenv
import os
import boto3

load_dotenv(find_dotenv())

S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")

s3 = boto3.client(
    's3',
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET)
s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(S3_BUCKET)
