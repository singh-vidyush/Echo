import os
from dotenv import load_dotenv
from file_loader import FileLoader
from data_chunk import Chunking
from vectorization import Vectorization
from retrieving import Retrieve

if __name__ == "__main__":
    fun1 = FileLoader()
    data = fun1.loader()

    fun2 = Chunking(data)
    chunk = fun2.recursive_overlap()

    fun3 = Vectorization(chunk)
    vector_db = fun3.chunk_vectorization()

    load_dotenv()
    gemini_api = os.getenv("GEMINI_API")
    
    retrieve = Retrieve(vector_db, gemini_api, gemini_model= "gemini-3.1-flash-lite")
    retrieve.data_retrieve()

