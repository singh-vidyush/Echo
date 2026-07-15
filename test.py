import os
from dotenv import load_dotenv

from file_loader import FileLoader
from data_chunk import Chunking
from vectorization import Vectorization
from retrieving import Retrieve


def main():
    print("\n" + "=" * 60)
    print("🚀 Echo - Real Estate Knowledge Assistant")
    print("=" * 60)

    # Load environment variables
    load_dotenv()

    gemini_api = os.getenv("GEMINI_API")

    if not gemini_api:
        raise ValueError(
            "GEMINI_API not found. Please check your .env file."
        )

    # Step 1: Load documents
    print("\n📂 Loading documents...")
    loader = FileLoader()

    documents = loader.loader()

    print(f"✅ Loaded {len(documents)} documents")

    # Step 2: Chunk documents
    print("\n✂️ Chunking documents...")

    chunker = Chunking(documents)

    chunks = chunker.recursive_overlap()
    # Alternatively:
    # chunks = chunker.semantic_chunk()
    # chunks = chunker.paragraph_chunking()

    print(f"✅ Created {len(chunks)} chunks")

    # Step 3: Create / Load Vector Database
    print("\n🧠 Initializing Vector Database...")

    vectorizer = Vectorization(chunks)

    vector_db = vectorizer.chunk_vectorization()

    print("✅ ChromaDB ready")

    # Step 4: Start Retriever
    print("\n🤖 Starting Echo Assistant...")
    print("Type 'exit', 'quit', or 'stop' to end the session.\n")

    chatbot = Retrieve(
        vector_db=vector_db,
        gemini_api=gemini_api,
        gemini_model="gemini-2.5-flash",
    )

    chatbot.data_retrieve()


if __name__ == "__main__":
    main()
