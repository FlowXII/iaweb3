from langchain_community.llms import Ollama
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

class Chatbot:
    def __init__(self, vector_store, temperature=0.7):
        self.llm = Ollama(model="mistral", temperature=temperature)
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Chain sans RAG
        self.simple_chain = self.llm
        
        # Chain avec RAG
        self.rag_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            memory=self.memory
        )
    
    def get_response(self, question: str, use_rag: bool = True):
        if use_rag:
            response = self.rag_chain({"question": question})
            return response['answer']
        else:
            response = self.simple_chain.predict(question)
            return response 