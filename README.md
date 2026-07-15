# 🏡 Echo – AI-Powered Real Estate Knowledge Assistant

Echo is a Retrieval-Augmented Generation (RAG) chatbot designed for the real estate domain. It combines semantic search, document retrieval, vector databases, and Google's Gemini models to provide accurate, context-aware answers from a custom real estate knowledge base.

The system ingests documents from multiple formats, converts them into searchable embeddings, retrieves the most relevant information, and generates intelligent responses grounded in the uploaded knowledge base.

---

## ✨ Features

### 📂 Multi-Format Document Ingestion
Echo can load and process:

- PDF documents
- DOCX documents
- TXT files
- JSON files

This enables organizations to consolidate knowledge from different sources into a single searchable system.

---

### ✂️ Intelligent Document Chunking

Multiple chunking strategies are supported:

- Recursive Character Chunking
- Semantic Chunking
- Fixed-Size Chunking
- Paragraph-Based Chunking
- Overlapping Chunking

This ensures optimal retrieval quality depending on the document structure and use case.

---

### 🧠 Dense Vector Search

Uses:

- Hugging Face Embeddings
- Chroma Vector Database
- sentence-transformers/all-MiniLM-L6-v2

Documents are transformed into vector representations to enable semantic understanding instead of traditional keyword matching.

Example:

```text
User Query:
"What residential projects are available in Bangalore?"

The system retrieves content even if the exact wording
does not exist in the document collection.
```

---

### 🔍 Retrieval-Augmented Generation (RAG)

Echo follows the RAG architecture:

```text
Documents
    │
    ▼
File Loader
    │
    ▼
Document Chunking
    │
    ▼
Vector Embeddings
    │
    ▼
Chroma Vector Database
    │
    ▼
Retriever
    │
    ▼
Gemini LLM
    │
    ▼
Generated Answer
```

The model answers only using retrieved context from the knowledge base.

---

### 🤖 Gemini-Powered Responses

The application integrates with Google's Gemini models to provide:

- Context-aware responses
- Reduced hallucinations
- Natural language explanations
- Domain-focused conversations

---

## 📁 Project Structure

```text
Echo/
│
├── data/
│   ├── documents/
│   ├── pdf/
│   ├── txt/
│   └── json/
│
├── chroma_db/
│
├── src/
│   ├── file_loader.py
│   ├── data_chunk.py
│   ├── vectorization.py
│   ├── retrieving.py
│
├── .env.example
├── requirements.txt
├── test.py
└── README.md
```

---

## 🏗️ Architecture

### 1. File Loading

The `FileLoader` module scans the data directory and loads all supported documents.

Supported loaders:

| Format | Loader |
|----------|----------|
| PDF | PyPDFLoader |
| DOCX | Docx2txtLoader |
| TXT | TextLoader |
| JSON | JSONLoader |

---

### 2. Chunk Generation

The `Chunking` module converts large documents into smaller chunks suitable for embedding and retrieval.

Available methods:

```python
recursive_overlap()
semantic_chunk()
fixed_chunking()
paragraph_chunking()
overlap_chunking()
```

---

### 3. Vectorization

The `Vectorization` module:

- Generates embeddings
- Creates a Chroma vector database
- Persists embeddings locally
- Reuses existing databases when available

Embedding Model:

```text
sentence-transformers/all-MiniLM-L6-v2
```

---

### 4. Retrieval

The retriever performs similarity search against the vector database.

Current configuration:

```python
top_k = 3
```

The most relevant chunks are retrieved and passed to Gemini for response generation.

---

### 5. Response Generation

A carefully designed prompt instructs Gemini to behave as:

```text
Senior Real Estate Advisor Chatbot
```

Knowledge scope includes:

- Company Profile
- Company Overview
- Real Estate Knowledge
- Project Portfolio

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/singh-vidyush/Echo.git

cd Echo
```

---

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

Activate:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / Mac

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create:

```bash
.env
```

Add:

```env
GEMINI_API=your_gemini_api_key
```

---

### 5. Add Knowledge Base Documents

Place your files inside:

```text
data/
```

Examples:

```text
data/documents/company_profile.docx

data/documents/project_portfolio.pdf

data/json/faq.json

data/txt/about_company.txt
```

---

### 6. Run Application

```bash
python test.py
```

---

## 💬 Example Conversation

```text
Ask question...

What projects does the company offer?

------------------------------------------------

The company offers residential, commercial,
and mixed-use real estate projects across
multiple locations...
```

---

## 🎯 Use Cases

### Real Estate Companies

- Company knowledge assistant
- Project discovery chatbot
- Internal employee knowledge base
- Property recommendation assistant

### Enterprises

- Policy question answering
- Document intelligence
- Internal helpdesk chatbot
- Knowledge management system

### Education

- RAG learning project
- LangChain implementation reference
- Vector database demonstration
- LLM application development

---

## 📊 Technology Stack

### Frameworks

- LangChain
- LangChain Community
- LangChain Experimental

### Vector Database

- ChromaDB

### Embeddings

- Hugging Face Embeddings
- sentence-transformers

### LLM

- Google Gemini

### Language

- Python 3.11+

---

## 🔒 Security Best Practices

Add the following to `.gitignore`:

```gitignore
.env
chroma_db/
__pycache__/
*.pyc
```

Never commit:

- API Keys
- Environment Variables
- Production Databases

Use:

```text
.env.example
```

for configuration templates.

---

## 🛣️ Future Enhancements

- Hybrid Retrieval (Dense + Sparse Search)
- BM25 Integration
- Reranking Models
- FastAPI Backend
- Streamlit Interface
- React Frontend
- Conversation Memory
- Multi-Agent Architecture
- Source Citations
- Real-Time Document Upload
- Authentication & Authorization

---

## 📈 Roadmap

### Phase 1 ✅

- Document Loading
- Chunking
- Vectorization
- Retrieval
- Gemini Integration

### Phase 2 🚧

- Hybrid Search
- Better Prompt Engineering
- Evaluation Metrics
- Response Grounding

### Phase 3 🎯

- Web Application
- User Management
- Cloud Deployment
- Production Monitoring

---

## 👨‍💻 Author

**Vidyush Singh**

Backend Developer | AI Enthusiast | ML Engineer

GitHub: https://github.com/singh-vidyush

---

## ⭐ Support

If you found this project useful:

- Star the repository
- Fork the project
- Contribute improvements
- Share feedback

---

### Built with ❤️ using LangChain, ChromaDB, Hugging Face Embeddings, and Google Gemini.