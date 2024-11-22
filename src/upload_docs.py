from cloud_config import CloudConfig
import requests

def create_and_upload_test_docs():
    s3_client = CloudConfig.configure_aws()
    
    # Documents test
    documents = [
        {
            "title": "ia_basics.txt",
            "content": """
            L'intelligence artificielle est une technologie qui permet aux machines 
            d'imiter l'intelligence humaine. Elle inclut le machine learning et le deep learning.
            """
        },
        {
            "title": "ml_basics.txt",
            "content": """
            Le machine learning est une branche de l'IA qui permet aux systèmes 
            d'apprendre à partir de données sans être explicitement programmés.
            """
        }
    ]
    
    # Upload vers S3
    for doc in documents:
        s3_client.put_object(
            Bucket=CloudConfig.BUCKET_NAME,
            Key=f"docs/{doc['title']}",
            Body=doc['content'].encode('utf-8')
        )
        print(f"Uploaded {doc['title']}")

if __name__ == "__main__":
    create_and_upload_test_docs() 