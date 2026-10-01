# 30 Days of AI

A hands-on 30-day journey to learn AI engineering with Python and build practical AI applications from scratch.

The goal is not just to learn AI concepts, but to understand how the pieces connect and eventually build production-ready AI applications.

---

## 🚀 Roadmap

```text
30-days-of-ai/
│
├── 01-python-for-ai/
├── 02-llms/
├── 03-prompting/
├── 04-embeddings/
├── 05-vector-databases/
├── 06-rag/
├── 07-tool-calling/
├── 08-ai-agents/
├── 09-fastapi/
├── 10-nextjs/
├── 11-production/
│
├── projects/
│   ├── 01-ai-chatbot/
│   ├── 02-semantic-search/
│   ├── 03-rag-chatbot/
│   └── 04-ai-agent/
│
└── README.md
```

---

# 📅 30-Day Learning Plan

## Day 1–2 — Python for AI

📁 `01-python-for-ai/`

### Topics

* Python fundamentals for AI
* Functions
* Lists, dictionaries and data structures
* File handling
* Environment variables
* APIs
* JSON
* Async programming
* `asyncio`
* `aiohttp`
* Pydantic
* Working with external APIs

### Practical work

Built programs that:

```text
Python
   ↓
API Request
   ↓
JSON Response
   ↓
Pydantic Validation
   ↓
Useful Output
```

### Key learning

Understand how Python is used to communicate with APIs and process structured data.

---

# Day 3 — LLMs

📁 `02-llms/`

### Goal

Understand how Large Language Models work at a practical developer level and learn how to communicate with an LLM through an API.

### Topics

* What is an LLM?
* Tokens
* Tokenization
* Next-token prediction
* Context window
* System messages
* User messages
* Assistant responses
* Conversation history
* LLM APIs
* API keys
* Environment variables
* Model parameters
* Hallucinations
* Basic chatbot architecture

### Practical project

Build a simple command-line AI chatbot using Python and an LLM API.

```text
User
  ↓
Python Application
  ↓
LLM API
  ↓
Large Language Model
  ↓
AI Response
  ↓
Conversation History
  ↓
Next User Question
```

### Requirements

* [x] API key stored in environment variable
* [x] System message
* [x] User input
* [x] LLM response
* [x] Conversation history
* [x] Multiple questions in one conversation
* [x] Experiment with model settings
* [x] README documentation

### Key learning

Understand that an LLM application is not simply:

```text
Question → AI → Answer
```

A conversational application maintains context:

```text
System
   ↓
User
   ↓
Assistant
   ↓
User
   ↓
Assistant
   ↓
User
   ↓
Assistant
```

---

# Day 4 — Prompting

📁 `03-prompting/`

### Goal

Learn how to communicate with LLMs effectively and consistently.

### Topics

* What makes a good prompt?
* Clear instructions
* Context
* Constraints
* Few-shot prompting
* Zero-shot prompting
* Role prompting
* Structured output
* JSON output
* Prompt templates
* Prompt iteration
* Prompt evaluation

### Practical work

Create multiple prompts for the same task and compare the results.

```text
Weak Prompt
    ↓
LLM
    ↓
Inconsistent Result


Improved Prompt
    ↓
LLM
    ↓
More Controlled Result
```

### Key learning

Learn that prompt quality affects the reliability and usefulness of an LLM application.

---

# Day 5 — Embeddings

📁 `04-embeddings/`

### Goal

Understand how text can be converted into numerical representations that capture semantic relationships.

### Topics

* What is an embedding?
* Vectors
* Dimensions
* Semantic similarity
* Cosine similarity
* Text → Embedding
* Query → Embedding

### Core concept

```text
Text
  ↓
Embedding Model
  ↓
Vector
```

Example:

```text
"Python developer"
        ↓
[0.12, -0.43, 0.81, ...]
```

### Practical project

Build a simple semantic similarity program.

---

# Day 6 — Vector Databases

📁 `05-vector-databases/`

### Goal

Learn how embeddings are stored and searched efficiently.

### Topics

* Vector databases
* Vector indexing
* Similarity search
* Metadata
* Queries
* Top-K results
* Chroma / Qdrant / other vector databases

### Core concept

```text
Documents
    ↓
Embeddings
    ↓
Vector Database
    ↓
Similarity Search
    ↓
Relevant Documents
```

---

# Day 7 — RAG

📁 `06-rag/`

### Goal

Understand Retrieval-Augmented Generation and build a basic RAG system.

### Topics

* What is RAG?
* Knowledge base
* Document loading
* Chunking
* Embeddings
* Vector search
* Retrieval
* Context
* LLM generation

### Core architecture

```text
User Question
      ↓
Question Embedding
      ↓
Vector Database
      ↓
Relevant Documents
      ↓
Context
      ↓
LLM
      ↓
Answer
```

### Practical project

Build a simple document-based RAG chatbot.

---

# Day 8 — Tool Calling

📁 `07-tool-calling/`

### Goal

Learn how an LLM can decide when to call external functions or tools.

### Topics

* What is tool calling?
* Functions
* Tool schemas
* Arguments
* Tool execution
* Returning tool results to the model

### Core architecture

```text
User
 ↓
LLM
 ↓
Should I use a tool?
 ↓
Tool Call
 ↓
Python Function / API
 ↓
Tool Result
 ↓
LLM
 ↓
Final Answer
```

### Practical project

Build an AI assistant that can call Python functions or external APIs.

---

# Day 9 — AI Agents

📁 `08-ai-agents/`

### Goal

Understand how LLMs, tools, memory and reasoning loops can be combined into agentic systems.

### Topics

* What is an AI agent?
* Agent loop
* Tools
* Planning
* Memory
* Tool selection
* Multi-step tasks
* Agent limitations

### Core architecture

```text
User Goal
    ↓
Agent
    ↓
Think / Decide
    ↓
Tool
    ↓
Tool Result
    ↓
Think / Decide
    ↓
Final Answer
```

### Practical project

Build a small AI agent capable of using multiple tools.

---

# Day 10 — FastAPI

📁 `09-fastapi/`

### Goal

Turn AI functionality into a backend API.

### Topics

* FastAPI
* API routes
* Request validation
* Pydantic
* Async endpoints
* Error handling
* Environment variables
* AI API integration

### Architecture

```text
Frontend
   ↓
FastAPI
   ↓
AI Application
   ↓
LLM / RAG / Agent
   ↓
Response
```

---

# Day 11 — Next.js

📁 `10-nextjs/`

### Goal

Build a frontend for the AI backend.

### Topics

* Next.js
* React
* Components
* API calls
* Chat UI
* Loading states
* Error handling
* Streaming responses

### Architecture

```text
Next.js
   ↓
FastAPI
   ↓
AI Backend
   ↓
LLM
```

---

# Day 12–30 — Production AI

📁 `11-production/`

The remaining days focus on turning prototypes into production-ready AI applications.

### Topics

* Project architecture
* Authentication
* Database integration
* Caching
* Logging
* Error handling
* Monitoring
* Rate limiting
* Security
* API optimization
* Cost management
* Docker
* Deployment
* CI/CD
* Testing
* Evaluation
* Production monitoring

### Goal

Move from:

```text
AI Prototype
```

to:

```text
Production AI Application
```

---

# 🏗️ Projects

The learning roadmap will eventually be combined into four larger projects.

## 1. AI Chatbot

📁 `projects/01-ai-chatbot/`

Technologies:

```text
Python
LLM
Prompting
FastAPI
Next.js
```

Architecture:

```text
Next.js
   ↓
FastAPI
   ↓
LLM
   ↓
Response
```

---

## 2. Semantic Search

📁 `projects/02-semantic-search/`

Technologies:

```text
Python
Embeddings
Vector Database
```

Architecture:

```tex
```
