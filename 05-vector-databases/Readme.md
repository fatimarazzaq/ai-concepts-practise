# Day 5 — Vector Databases

Learn to store and search text embeddings using Python, Sentence Transformers, ChromaDB, and Google Colab.

## Goals

- Understand vector databases and embeddings.
- Store documents, vectors, IDs, and metadata in ChromaDB.
- Perform semantic search and metadata filtering.
- Persist data using Google Drive.
- Understand how vector databases support RAG.

## Tools

- Python and Google Colab
- Sentence Transformers: `all-MiniLM-L6-v2` (384-dimensional embeddings)
- ChromaDB
- Google Drive for persistent storage

## Project Structure

```text
05-vector-databases/
├── README.md
└── 05-vector-database.ipynb
```

## Setup

Install dependencies in Colab:

```python
!pip -q install chromadb sentence-transformers
```

Load the embedding model:

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")
```

## 1. Prepare Documents and Metadata

```python
documents = [
    "Python is a programming language used for AI development.",
    "Machine learning allows computers to learn patterns from data.",
    "ChromaDB stores embeddings and supports vector similarity search.",
    "Neural networks are an important part of deep learning.",
    "FastAPI is used to build APIs with Python.",
    "RAG combines document retrieval with language model generation.",
    "Next.js is a framework for building web applications.",
    "Embeddings represent text as numerical vectors."
]

ids = [f"doc_{i}" for i in range(len(documents))]

metadatas = [
    {"topic": "python"},
    {"topic": "machine_learning"},
    {"topic": "vector_database"},
    {"topic": "deep_learning"},
    {"topic": "backend"},
    {"topic": "rag"},
    {"topic": "frontend"},
    {"topic": "embeddings"}
]
```

## 2. Generate Embeddings

```python
embeddings = model.encode(
    documents,
    convert_to_numpy=True
)

print("Number of embeddings:", len(embeddings))
print("Vector dimensions:", embeddings.shape)
print("First vector:", embeddings[0][:10])
```

**Expected shape:** `(8, 384)`

Each document is converted into a 384-dimensional numerical vector.

## 3. Create a Persistent ChromaDB Collection

Mount Google Drive in Colab:

```python
from google.colab import drive
drive.mount("/content/drive")

DB_PATH = "/content/drive/MyDrive/chroma_ai_db"

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name="ai_learning",
    metadata={"hnsw:space": "cosine"}
)
```

## 4. Save Documents and Embeddings

```python
collection.upsert(
    ids=ids,
    documents=documents,
    embeddings=embeddings.tolist(),
    metadatas=metadatas
)

print("Records:", collection.count())
```

`upsert()` inserts new records and updates existing records with matching IDs.

## 5. Semantic Search

```python
query = "How can I build applications using AI?"
query_embedding = model.encode(query).tolist()

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3,
    include=["documents", "metadatas", "distances"]
)

for i, document in enumerate(results["documents"][0]):
    print(f"Document: {document}")
    print(f"Topic: {results['metadatas'][0][i]['topic']}")
    print(f"Cosine distance: {results['distances'][0][i]:.4f}")
    print("-" * 40)
```

With cosine distance, lower values generally indicate closer vectors. Distances are not probabilities.

## 6. Filter by Metadata

Retrieve documents belonging to the `python` topic:

```python
python_docs = collection.get(
    where={"topic": "python"},
    include=["documents", "metadatas"]
)

print(python_docs["documents"])
```

## 7. Verify Persistence

After restarting the Colab runtime, mount Google Drive again if necessary, then reopen the database:

```python
client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection(name="ai_learning")

print("Saved records:", collection.count())
```

Keep the database directory in Google Drive to preserve records between sessions.

## Key Concepts

- **Collection:** A named group of records.
- **Embedding:** A numerical representation of text.
- **Metadata:** Additional information attached to a record.
- **Similarity search:** Retrieves vectors closest to a query vector.
- **Top-K:** The number of nearest results requested.
- **Persistence:** Saves data so it can be reopened later.

## How This Connects to RAG

```text
User Question
    ↓
Query Embedding
    ↓
Vector Database Search
    ↓
Relevant Documents
    ↓
LLM Context
    ↓
Generated Answer
```

## Learning Checklist

- [ ] Generate text embeddings.
- [ ] Create a ChromaDB collection.
- [ ] Save documents, vectors, and metadata.
- [ ] Run semantic searches.
- [ ] Filter records by metadata.
- [ ] Verify persistent storage.
- [ ] Understand the role of vector databases in RAG.

## Next

**RAG — Retrieval-Augmented Generation**

Learn document loading, chunking, retrieval, and how to use retrieved context to answer questions.

## Resources

- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Sentence Transformers Documentation](https://www.sbert.net/)
- [Google Colab](https://colab.research.google.com/)
