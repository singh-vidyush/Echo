from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader, Docx2txtLoader, TextLoader, JSONLoader

class FileLoader:
    def __init__(self, data_path = 'data'):
        self.docs = []
        self.data_path = data_path

    def loader(self):
        self.docs += DirectoryLoader(
            self.data_path, glob = '**/*.pdf', loader_cls = PyPDFLoader
        ).load()
        self.docs += DirectoryLoader(
            self.data_path, glob = '**/*.txt', loader_cls = TextLoader
        ).load()
        self.docs += DirectoryLoader(
            self.data_path, glob = '**/*.docx', loader_cls = Docx2txtLoader
        ).load()
        self.docs += DirectoryLoader(
            self.data_path, glob = '**/*.json', loader_cls = JSONLoader, loader_kwargs={
            "jq_schema": ".[]",
            "text_content": False,
        }).load()

        return self.docs