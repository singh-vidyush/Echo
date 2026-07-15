from src.file_loader import FileLoader
from src.data_chunk import Chunking

a = FileLoader()
data = a.loader()

b = Chunking()
chunk = b.data_chunk(data)
print(len(chunk))

