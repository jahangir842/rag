from langchain_community.embeddings import HuggingFaceEmbeddings
from chromadb import PersistentClient
from langchain_community.vectorstores import Chroma

class EmbeddingsManager:
    def __init__(self, persist_directory="data/chroma"):
        self.embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        self.persist_directory = persist_directory
        
    def create_vectorstore(self, documents):
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )