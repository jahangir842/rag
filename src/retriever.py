from typing import List
from .embeddings import EmbeddingsManager

class Retriever:
    def __init__(self, embeddings_manager: EmbeddingsManager):
        self.embeddings_manager = embeddings_manager

    def retrieve_relevant_documents(self, query: str, k: int = 3) -> List[str]:
        """Retrieve the most relevant documents for the given query."""
        results = self.embeddings_manager.search_similar(query, k)
        return results['documents'][0]

    def get_context(self, query: str, k: int = 3) -> str:
        """Get concatenated context from relevant documents."""
        documents = self.retrieve_relevant_documents(query, k)
        return "\n\n".join(documents)