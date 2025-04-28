from langchain.chains import ConversationalRetrievalChain
from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class RAGChain:
    def __init__(self, vectorstore, model_path="models/phi-2.Q4_K_M.gguf"):
        callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
        
        self.llm = LlamaCpp(
            model_path=model_path,
            temperature=0.7,
            max_tokens=1000,
            top_p=1,
            callback_manager=callback_manager,
            verbose=True,
            n_ctx=2048,  # Smaller context window for better performance
            n_gpu_layers=0  # CPU only for compatibility
        )
        
        self.retriever = vectorstore.as_retriever(
            search_kwargs={"k": 2}  # Reduced number of retrieved documents
        )
        
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=True,
        )
        
    def query(self, question, chat_history=[]):
        return self.chain({"question": question, "chat_history": chat_history})