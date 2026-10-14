# Day 6: Retrieval-Augmented Generation (RAG)

## 📌 Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system that answers questions using relevant information retrieved from a document database.

Instead of relying only on an LLM's existing knowledge, RAG retrieves relevant documents and provides them as context to Gemini to generate more accurate, context-based answers.

## 🎯 Objectives

- Understand how RAG works.
- Convert questions into embeddings.
- Retrieve relevant documents from ChromaDB.
- Generate answers using the Gemini API.
- Display source documents and retrieval distances.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Google Colab** — Development environment
- **Sentence Transformers** — Generate text embeddings
- **ChromaDB** — Store and retrieve vector embeddings
- **Google Gemini API** — Generate answers using retrieved context
- **Google Drive** — Persist the vector database

## ⚙️ How It Works

1. **Question:** The user submits a question.
2. **Embedding:** The question is converted into a numerical vector.
3. **Retrieval:** ChromaDB searches for the most relevant documents.
4. **Context Building:** Retrieved documents are combined into a context.
5. **Answer Generation:** Gemini generates an answer using the retrieved context.
6. **Source Display:** The system returns the answer, source documents, metadata, and distances.

## 📂 Project Structure

```text
06-rag/
├── 06-rag.ipynb
└── README.md
```

## 💻 Example

**Question:**
```text
What is RAG, and how does it work?
```

**Expected Output:**

The system retrieves relevant information about RAG from the vector database and asks Gemini to generate an answer based on that context. It also displays the retrieved sources and their distances.

*The exact answer depends on the documents stored in the database.*

## 🚀 Key Learnings

- How Retrieval-Augmented Generation works.
- How semantic search helps find relevant information.
- How to connect ChromaDB with an LLM.
- How to ground LLM responses in retrieved documents.
- Why source information is useful for understanding and evaluating answers.

## 🔮 Future Improvements

- Support PDF uploads and multiple documents.
- Improve chunking and retrieval quality.
- Add a web interface for asking questions.
- Evaluate answer accuracy and retrieval performance.
- Add conversation history for follow-up questions.

## ✅ Conclusion

This project demonstrates the fundamentals of building a RAG pipeline by combining vector search with Gemini. It is an important step toward building document assistants, knowledge-base chatbots, and AI applications that answer questions using custom data.

---

**Day 6 of my 30 Days of AI roadmap — Learning RAG!**
