# Day 8: AI Agents — Customer Support Assistant

## 📌 Overview

This project demonstrates how to build a simple AI agent using Python and the Google Gemini API. The agent helps customers check order details, track delivery status, and verify refund eligibility by calling Python functions as tools.

It uses a sample order database to simulate a real-world customer support system.

## 🎯 Objectives

- Understand the fundamentals of AI agents.
- Connect Python functions to Gemini using tool calling.
- Let the AI select appropriate tools based on user questions.
- Retrieve order information and check refund eligibility.
- Generate responses based on tool results.

## 🛠️ Technologies Used

- **Python** — Core programming language
- **Google Colab** — Development environment
- **Google Gemini API** — AI reasoning and response generation
- **Google Gen AI SDK** — Function and tool calling

## ⚙️ How It Works

1. The customer asks a question about an order.
2. Gemini determines which tool is needed.
3. Python executes the selected function.
4. The tool returns order details or a refund eligibility decision.
5. Gemini uses the results to generate a response.

## 🔧 Tools Implemented

- `lookup_order()` — Retrieves order details and delivery status.
- `check_refund_eligibility()` — Checks whether an order meets the sample refund policy.

**Refund policy:** Only delivered orders within 14 days of delivery are eligible. Checking eligibility does not issue an actual refund.

## 🧪 Example Questions

- Where is my order ORD-1001?
- Can I get a refund for ORD-1002?
- Has the refund window expired for ORD-1003?
- Can you check order ORD-9999?

## 🚀 Key Learnings

- How AI agents use tools to complete tasks.
- How to connect Gemini with Python functions.
- How to combine AI decision-making with rule-based logic.
- Why tools should return reliable data instead of relying on AI-generated guesses.

## 🔮 Future Improvements

- Connect to a real order-management API or database.
- Add customer authentication and authorization.
- Integrate a RAG system for answering policy questions.
- Build a web interface using FastAPI and Next.js.
- Add logging, error handling, and automated tests.

## ⚠️ Limitations

This is an educational prototype using mock order data. It does not connect to a real store, process payments, or issue refunds.

## ✅ Conclusion

This project demonstrates the fundamentals of building a tool-using AI agent for customer support. It provides a foundation for developing more advanced AI assistants that interact with APIs, databases, and external services.

**Day 8 of my 30 Days of AI roadmap — Learning AI Agents!**
