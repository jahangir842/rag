from pathlib import Path
from typing import List
from langchain_community.document_loaders import DirectoryLoader, PDFPlumberLoader

class DocumentLoader:
    def __init__(self, data_dir: str = "data/pdfs"):
        self.data_dir = Path(data_dir)
        
    def load_documents(self) -> List:
        """Load documents from the data directory."""
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True, exist_ok=True)
            return []
            
        loader = DirectoryLoader(
            self.data_dir,
            glob="**/*.pdf",
            loader_cls=PDFPlumberLoader
        )
        return loader.load()