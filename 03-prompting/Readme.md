# Day 3 — Prompting

## 🎯 Goal

Learn how to write effective prompts for Large Language Models (LLMs) and control the quality, structure, and behavior of their responses.

---

## 📚 What I Learned

### 1. Prompt Engineering

Prompt engineering is the process of designing clear instructions for an LLM so it produces the desired response.

A good prompt usually contains:

```text
Role
  ↓
Task
  ↓
Context
  ↓
Constraints
  ↓
Output Format
```

Example:

```text
You are a Python tutor.

Task:
Explain what an API is.

Context:
The learner knows basic Python but is new to APIs.

Constraints:
- Use simple English
- Give one example
- Keep the explanation short

Output:
Definition → Explanation → Example
```

---

## 2. Zero-Shot Prompting

Zero-shot prompting means asking the model to perform a task without providing examples.

Example:

```text
Classify the sentiment of this sentence:

"I really enjoyed this product."

Return: Positive, Negative, or Neutral.
```

---

## 3. Few-Shot Prompting

Few-shot prompting provides examples to show the LLM how the task should be performed.

Example:

```text
Text: "I love this product."
Sentiment: Positive

Text: "This product is terrible."
Sentiment: Negative

Text: "The product is okay."
Sentiment:
```

The examples help the model understand the expected pattern.

---

## 4. Role Prompting

Role prompting gives the LLM a specific role or perspective.

Example:

```text
You are a senior Python developer.

Review the following code and identify:
1. Bugs
2. Performance issues
3. Possible improvements
```

Roles can include:

* Python Tutor
* Software Engineer
* Code Reviewer
* Data Analyst
* Technical Writer

---

## 5. Context

Providing context helps the LLM understand the situation before completing the task.

Instead of:

```text
Explain RAG.
```

A better prompt is:

```text
Explain RAG to a Python developer
who is new to Generative AI.

Explain:
1. What RAG is
2. Why it is needed
3. How it works
4. Give a simple example
```

---

## 6. Constraints

Constraints control how the model should respond.

Examples:

```text
Answer in 3 bullet points.
```

```text
Keep the answer below 100 words.
```

```text
Use simple English.
```

```text
Give exactly 3 examples.
```

```text
Return the answer as JSON.
```

---

## 7. Structured Output

LLMs normally return natural language, but applications often need structured data.

Example prompt:

```text
Extract information from the following text.

Return exactly this format:

{
    "name": "",
    "age": "",
    "occupation": "",
    "skills": []
}
```

Structured output is useful when connecting LLMs with Python applications, APIs, databases, RAG systems, and AI agents.

---

## 8. Prompt Comparison

A major lesson from this day was that the quality of the prompt affects the quality and consistency of the response.

### Basic Prompt

```text
Explain RAG.
```

### Improved Prompt

```text
You are an AI tutor.

Explain Retrieval-Augmented Generation (RAG)
to a Python developer who is new to AI.

Explain:
1. What RAG is
2. Why it is needed
3. How it works
4. Give a simple example

Use simple English and keep the answer concise.
```

The second prompt provides the model with more context, clear instructions, and constraints.

---

# 🧪 Practice Project — Text Analyzer

Built a small LLM-based text analyzer using Python and Gemini.

### Input

```text
Python is an amazing programming language.
I use it for APIs, automation and AI applications.
```

### Prompt

The LLM was instructed to analyze the text and return structured information.

### Expected Output

```json
{
    "summary": "...",
    "sentiment": "...",
    "topics": [],
    "keywords": [],
    "language": "..."
}
```

### Architecture

```text
User Text
    ↓
Python
    ↓
Prompt
    ↓
Gemini API
    ↓
Structured Response
    ↓
Python
    ↓
Display Result
```

---

# 🔑 Key Takeaways

* Clear prompts produce more useful and consistent results.
* Give the model a clear role when appropriate.
* Clearly define the task.
* Provide relevant context.
* Use constraints to control the response.
* Few-shot examples can demonstrate the expected behavior.
* Structured output is important for real applications.
* Prompt engineering is especially useful when building RAG systems and AI agents.

---

# 🛠️ Technologies Used

* Python
* Google Gemini API
* `google-genai`
* Google Colab
* Git
* GitHub

---

# 📁 Folder Structure

```text
03-prompting/
│
├── prompting.ipynb
└── README.md
```

---

## 🚀 Next Step

### Day 4 — Embeddings

Next, I will learn how text can be converted into numerical vectors called **embeddings** and how those vectors can be used for **semantic similarity and search**.

```text
Text
 ↓
Embedding Model
 ↓
Vector
 ↓
Similarity
 ↓
Semantic Search
```
