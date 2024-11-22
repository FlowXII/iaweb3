import os
from dotenv import load_dotenv

load_dotenv()

class CloudConfig:
    AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
    AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
    BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")

    @staticmethod
    def configure_aws():
        import boto3
        return boto3.client(
            's3',
            aws_access_key_id=CloudConfig.AWS_ACCESS_KEY,
            aws_secret_access_key=CloudConfig.AWS_SECRET_KEY
        ) 