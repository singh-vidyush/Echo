from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

class Embedding:
    def __init__(self, embedding_path = 'chroma_db'):
        self.embedding_path = embedding_path

    def chunk_embedding(self, chunk, embedding_model):
        if Path(self.embedding_path).exists():
            vector_db = Chroma(
                persist_directory = self.embedding_path,
                embedding_function = embedding_model
            )
        else:
            vector_db = Chroma.from_documents(
                documents = chunk,
                persist_directory = self.embedding_path,
                embedding = embedding_model,
            )

        return vector_db