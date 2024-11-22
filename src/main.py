from chat import Chatbot
from document_loader import DocumentLoader
from cloud_config import CloudConfig
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import Chroma

def test_chatbot(question: str):

    cloud_config = CloudConfig()
    cloud_config.configure_aws()

    print("\n=== Test avec documents locaux ===")
    local_loader = DocumentLoader("./data/documents", use_cloud=False)
    local_documents = local_loader.load_and_split()

    print("\n=== Test avec documents cloud ===")
    cloud_loader = DocumentLoader(None, use_cloud=True, bucket_name=CloudConfig.BUCKET_NAME)
    cloud_documents = cloud_loader.load_and_split()

    all_documents = local_documents + cloud_documents

    embeddings = OllamaEmbeddings(model="mistral")
    vector_store = Chroma.from_documents(all_documents, embeddings)

    standard_chatbot = Chatbot(vector_store, temperature=0.7)
    creative_chatbot = Chatbot(vector_store, temperature=0.9)

    print("\n=== Réponses du chatbot ===")
    print(f"Question: {question}\n")
    
    print("1. Sans RAG (température 0.7):")
    print(standard_chatbot.get_response(question, use_rag=False))
    
    print("\n2. Avec RAG (température 0.7):")
    print(standard_chatbot.get_response(question, use_rag=True))
    
    print("\n3. Avec RAG (température 0.9):")
    print(creative_chatbot.get_response(question, use_rag=True))

if __name__ == "__main__":
    test_chatbot("Quelle est la différence entre l'intelligence artificielle et le machine learning?") 