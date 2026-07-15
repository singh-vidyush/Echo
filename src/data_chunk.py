from langchain_text_splitters import  RecursiveCharacterTextSplitter

class Chunking:
    def __init__(self):
        pass
    
    def data_chunk(self, docs):
        return RecursiveCharacterTextSplitter(
            chunk_size = 500,
            chunk_overlap = 100
        ).split_documents(docs)