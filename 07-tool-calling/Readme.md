# Day 8: Tool Calling

## 📌 Overview

This project explores **tool calling** using Python and the Google Gemini API. Tool calling allows an AI model to request the execution of Python functions to perform tasks and use their results in its response.

## 🎯 Objectives

- Understand how AI tool calling works.
- Define Python functions as tools.
- Let Gemini select appropriate tools based on user questions.
- Return tool results to the AI for a final answer.

## 🛠️ Technologies Used

- Python
- Google Colab
- Google Gemini API
- Google Gen AI SDK

## ⚙️ How It Works

1. The user asks a question.
2. Gemini selects a suitable tool and provides its arguments.
3. Python executes the requested function.
4. The result is returned to Gemini.
5. Gemini generates the final answer.

## 💻 Tools Implemented

- `add()` — Adds two numbers.
- `multiply()` — Multiplies two numbers.
- `subtract()` — Subtract two numbers.
- `get_square()` — Calculates the square of a number.

## 🚀 Key Learnings

- How to connect Python functions to Gemini.
- How AI models request tool execution.
- How to use multiple tools in an AI application.
- The difference between tool calling and normal text generation.

## 🔮 Future Improvements

- Connect tools to external APIs.
- Integrate tool calling with a RAG system.
- Explore MCP servers and AI agents.

## ✅ Conclusion

This project demonstrates the fundamentals of AI tool calling and provides a foundation for building AI assistants that can perform tasks using external functions.

**Day 8 of my 30 Days of AI roadmap — Learning Tool Calling!**
