import os
from dotenv import load_dotenv
from src.document_loader import DocumentLoader
from src.embeddings import EmbeddingsManager
from src.rag_chain import RAGChain

def main():
    load_dotenv()
    
    print("RAG Application Starting...")
    
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please add your OpenAI API key to the .env file")
        return

    loader = DocumentLoader()
    print("\nChecking for documents in data/pdfs directory...")
    documents = loader.load_documents()
    
    if not documents:
        print("No documents found in data/pdfs directory.")
        print("Please add some PDF files to the data/pdfs directory and try again.")
        return
    
    print(f"\nFound {len(documents)} documents:")
    for doc in documents:
        print(f"- {doc.metadata.get('source', 'Unknown document')}")
        
    print("\nCreating vector embeddings... This may take a while for large documents.")
    embeddings_manager = EmbeddingsManager()
    vectorstore = embeddings_manager.create_vectorstore(documents)
    
    print("\nInitializing RAG chain...")
    rag_chain = RAGChain(vectorstore)
    
    print("\nReady to answer questions! (Type 'quit' to exit)")
    chat_history = []
    
    while True:
        question = input("\nEnter your question: ")
        if question.lower() == 'quit':
            break
            
        result = rag_chain.query(question, chat_history)
        print("\nAnswer:", result["answer"])
        chat_history.append((question, result["answer"]))

if __name__ == "__main__":
    main()