# 🚚 AI Supply Chain Intelligence – Delay Detection & Solution BOT (SCI-BOT)

https://colab.research.google.com/drive/1efP92B8uC8yQoMGnydca1crzOVCKhY6S#scrollTo=ktk_v7iQuIxR


> An AI-powered Multi-Agent Supply Chain Intelligence System that detects shipment delays, analyzes risks, retrieves knowledge using RAG, and generates intelligent business recommendations using LangGraph, LangChain, Groq LLM, and FastAPI.

---

## 📌 Project Overview

AI Supply Chain Intelligence – Delay Detection & Solution BOT (SCI-BOT) is an intelligent logistics assistant that enables customers to track shipments using multiple search options and receive AI-generated shipment analysis.

The chatbot combines:

- Multi-Agent AI
- LangGraph Workflow
- LangChain
- Retrieval-Augmented Generation (RAG)
- Groq LLM
- External Business Tools
- Conversation Memory
- FastAPI
- Gradio UI

to provide real-time shipment intelligence and business recommendations.

---

# 🎯 Objectives

- Detect shipment delays
- Retrieve shipment information
- Analyze supplier performance
- Evaluate weather impact
- Perform risk assessment
- Generate executive shipment reports
- Recommend corrective actions
- Estimate business impact

---

# ✨ Features

## Customer Search Options

Users can search using:

- Shipment ID
- Mobile Number
- Email Address
- Order ID
- Customer Name

---

## AI Powered Workflow

```
Customer Input
      │
      ▼
Input Validation
      │
      ▼
LangGraph Workflow
      │
      ▼
Customer Lookup Agent
      │
      ▼
RAG Retriever Agent
      │
      ▼
Shipment Agent
      │
      ▼
Supplier Agent
      │
      ▼
Weather Agent
      │
      ▼
Risk Analysis Agent
      │
      ▼
LLM Agent (Groq)
      │
      ▼
Professional AI Report
```

---

# 🤖 Multi-Agent Architecture

| Agent | Responsibility |
|--------|----------------|
| Input Node | Accepts customer request |
| Customer Lookup Agent | Finds customer details |
| RAG Retriever Agent | Retrieves relevant documents |
| Shipment Agent | Retrieves shipment information |
| Supplier Agent | Retrieves supplier information |
| Weather Agent | Retrieves weather conditions |
| Risk Analysis Agent | Calculates shipment risk |
| LLM Agent | Generates intelligent report |
| Output Node | Displays final AI response |

---

# 🧠 LangChain Components

- Prompt Templates
- Tool Calling
- Output Parser
- Conversation Memory
- State Management
- LLM Integration

---

# 📚 RAG Pipeline

- Documents
- Text Splitter
- Sentence Transformers
- Embedding Generation
- FAISS Vector Database
- Semantic Retrieval

---

# 🔧 External Tools

The chatbot integrates with multiple tools.

- Customer Lookup Tool
- Shipment Tool
- Supplier Tool
- Weather Tool
- Risk Assessment Tool

---

# 🛡 Input Validation

Before executing the LangGraph workflow, the application validates all user inputs.

| Validation | Description |
|------------|-------------|
| Search Value | Cannot be empty |
| Question | Cannot be empty |
| Shipment ID | Format: SHP1001 |
| Mobile Number | Exactly 10 digits |
| Mobile Number | Digits only |
| Email Address | Valid email format |
| Order ID | Format: ORD1001 |
| Customer Name | Minimum 3 characters |
| Customer Name | Letters and spaces only |

If validation fails:

- Workflow execution stops
- External tools are not executed
- LLM is not called
- User receives a validation error message

---

# 📊 AI Generated Report

The chatbot automatically generates:

- Executive Summary
- Shipment Status
- Weather Impact
- Supplier Analysis
- Risk Assessment
- Recommended Actions
- Estimated Business Impact

---

# ⚙ Technologies Used

| Category | Technology |
|----------|------------|
| Programming | Python |
| UI | Gradio |
| AI Framework | LangChain |
| Multi-Agent | LangGraph |
| Retrieval | RAG |
| Vector Database | FAISS |
| Embeddings | Sentence Transformers |
| LLM | Groq |
| API | FastAPI |
| Memory | LangChain Memory |

---

# 📁 Project Structure

```
AI-Supply-Chain-Intelligence-Delay-Detection-Solution-BOT
│
├── app.py
├── data/
├── documents/
├── src/
│   ├── graph/
│   ├── nodes/
│   ├── tools/
│   ├── memory/
│   ├── validation/
│   └── ...
├── tests/
├── requirements.txt
└── README.md
```

---

# 🚀 How to Run

```bash
git clone <repository-url>

cd AI-Supply-Chain-Intelligence-Delay-Detection-Solution-BOT

pip install -r requirements.txt

python app.py
```

---

# 📈 Business Benefits

- Faster shipment tracking
- Early delay detection
- Intelligent risk analysis
- Improved customer satisfaction
- AI-assisted decision making
- Reduced manual effort
- Real-time logistics insights

---

# 📧 Contact

**Sugumar R**

📧 contact.sugumarai@gmail.com

---

## ⭐ If you found this project useful, please consider giving it a Star on GitHub.
