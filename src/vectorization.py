from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class Vectorization:
    def __init__(self, chunk):
        self.chunk = chunk
        self.embedding_path = 'chroma_db'
        self.embedding_model = HuggingFaceEmbeddings(model_name= "sentence-transformers/all-MiniLM-L6-v2")

    def chunk_vectorization(self):
        if Path(self.embedding_path).exists():
            vector_db = Chroma(
                persist_directory = self.embedding_path,
                embedding_function = self.embedding_model
            )
        else:
            vector_db = Chroma.from_documents(
                documents = self.chunk,
                persist_directory = self.embedding_path,
                embedding = self.embedding_model,
            )

        return vector_db