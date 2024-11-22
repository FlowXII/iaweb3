from langchain.document_loaders import DirectoryLoader, S3DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentLoader:
    def __init__(self, source_path, use_cloud=False, bucket_name=None):
        if use_cloud:
            self.loader = S3DirectoryLoader(bucket=bucket_name)
        else:
            self.loader = DirectoryLoader(source_path)
            
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    
    def load_and_split(self):
        documents = self.loader.load()
        return self.text_splitter.split_documents(documents) 