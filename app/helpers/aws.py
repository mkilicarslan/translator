import boto3
from app import app

# AWS_ACCESS = app.config['AWS_ACCESS']
# AWS_SECRET = app.config['AWS_SECRET']
# BUCKET_NAME = app.config['AWS_S3_BUCKET']

AWS_Translate = boto3.client(service_name='translate')
AWS_Polly = boto3.client(service_name='polly')
AWS_Transcribe = boto3.client(service_name='transcribe')
