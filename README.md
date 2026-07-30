# 🚚 AI Supply Chain Intelligence – Delay Detection & Solution BOT (SCI-BOT)

https://colab.research.google.com/drive/1efP92B8uC8yQoMGnydca1crzOVCKhY6S#scrollTo=ktk_v7iQuIxR

> **An AI-Powered Multi-Agent Supply Chain Intelligence System using LangGraph, LangChain, RAG, Memory, FastAPI, Groq LLM and Gradio for intelligent shipment tracking, delay detection, risk assessment, and business decision support.**

---

# 📌 Problem Statement

Supply chain and logistics companies often face challenges in tracking shipments, identifying delays, monitoring supplier performance, evaluating weather impact, and assessing business risks. Traditional shipment tracking systems typically display only shipment status and require manual analysis to understand the causes of delays and determine the next course of action.

This project addresses these challenges by integrating **Multi-Agent AI**, **LangGraph**, **LangChain**, **Retrieval-Augmented Generation (RAG)**, **Conversation Memory**, and **External Business Tools** into a single intelligent assistant. The chatbot retrieves live shipment information, analyses multiple business factors, and generates professional AI-powered reports with actionable recommendations.

---

# 🎯 Project Objectives

- Track shipments using multiple search methods
- Detect shipment delays automatically
- Retrieve shipment-related knowledge using RAG
- Analyse supplier availability
- Evaluate weather impact on delivery
- Assess shipment risks
- Generate intelligent business recommendations
- Produce professional shipment reports
- Improve customer support through AI automation

---

# 🌟 Key Features

- Multi-Agent AI Workflow
- LangGraph Orchestration
- LangChain Tool Calling
- Retrieval-Augmented Generation (RAG)
- Conversation Memory
- AI-Powered Risk Assessment
- Weather Analysis
- Supplier Analysis
- Executive Shipment Report Generation
- Input Validation
- Interactive Gradio Interface

---

# 🤖 Multi-Agent Architecture

The chatbot consists of multiple specialised AI agents.

| Agent | Responsibility |
|--------|----------------|
| Input Agent | Accepts customer request |
| Customer Lookup Agent | Retrieves customer details |
| RAG Retriever Agent | Retrieves relevant documents |
| Shipment Agent | Retrieves shipment information |
| Supplier Agent | Retrieves supplier information |
| Weather Agent | Retrieves weather conditions |
| Risk Analysis Agent | Evaluates shipment risks |
| LLM Agent | Generates AI business report |
| Output Agent | Displays final response |

---

# 🔄 Multi-Agent Workflow

```text
Customer
    │
    ▼
Input Validation
    │
    ▼
Customer Lookup Agent
    │
    ▼
RAG Retrieval Agent
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

# 🚀 Why Multi-Agent AI?

Instead of using a single AI model to perform every task, this project divides responsibilities among specialised agents.

### Advantages

- Modular architecture
- Independent task execution
- Easy maintenance
- Better scalability
- Easier debugging
- Reusable agents
- Improved accuracy
- Faster workflow management

---

# 🔗 Why LangGraph?

LangGraph is responsible for orchestrating the entire workflow.

### LangGraph Advantages

- Controls execution flow
- Maintains application state
- Coordinates multiple agents
- Supports conditional routing
- Handles sequential execution
- Simplifies workflow management
- Enables complex AI pipelines

Without LangGraph:

- Manual workflow coding
- Complex state management
- Difficult debugging
- Limited scalability

---

# 🔗 Why LangChain?

LangChain provides the building blocks required by each AI agent.

### LangChain Components Used

- Prompt Templates
- Tool Calling
- Output Parser
- Conversation Memory
- State Management
- LLM Integration

### Advantages

- Faster AI application development
- Easy tool integration
- Standardised prompt management
- Structured output handling
- Memory management
- Easy integration with vector databases

---

# 📚 Retrieval-Augmented Generation (RAG)

The chatbot retrieves domain-specific knowledge before generating responses.

### RAG Pipeline

```
Documents
      │
      ▼
Text Splitter
      │
      ▼
Sentence Transformer Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Semantic Search
      │
      ▼
Relevant Context
      │
      ▼
Groq LLM
```

### Advantages of RAG

- Uses project knowledge base
- Reduces hallucinations
- Improves response accuracy
- Supports semantic search
- Easy document updates
- Faster retrieval
- Better business recommendations

---

# 🧠 Conversation Memory

The chatbot stores conversation history to maintain context.

### Memory Benefits

- Context-aware responses
- Follow-up question handling
- Better user experience
- Reduced repeated questions
- Improved conversation continuity

---

# 🛠 External Tools

The chatbot integrates multiple business tools.

- Customer Lookup Tool
- Shipment Tool
- Supplier Tool
- Weather Tool
- Risk Assessment Tool

---

# 🛡 Input Validation

Before executing the LangGraph workflow, all user inputs are validated.

| Validation | Description |
|------------|-------------|
| Search Value | Cannot be empty |
| Question | Cannot be empty |
| Shipment ID | Format: SHP1001 |
| Mobile Number | Digits only |
| Mobile Number | Exactly 10 digits |
| Email Address | Valid email format |
| Order ID | Format: ORD1001 |
| Customer Name | Minimum 3 characters |
| Customer Name | Alphabetic characters only |

### Validation Benefits

- Prevents invalid requests
- Stops incorrect workflow execution
- Saves LLM/API calls
- Improves user experience
- Reduces unnecessary processing

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

# ⚙ Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| User Interface | Gradio |
| Multi-Agent Framework | LangGraph |
| AI Framework | LangChain |
| LLM | Groq |
| Retrieval | RAG |
| Embedding Model | Sentence Transformers |
| Vector Database | FAISS |
| Memory | LangChain Memory |
| API Framework | FastAPI |

---

# 📂 Project Structure

```
AI-Supply-Chain-Intelligence-Delay-Detection-Solution-BOT/
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
│   └── workflow/
├── tests/
├── requirements.txt
└── README.md
```

---

# 📈 Business Benefits

- Intelligent shipment tracking
- Faster delay detection
- Improved logistics visibility
- AI-assisted decision making
- Reduced manual analysis
- Better customer service
- Increased operational efficiency
- Scalable AI architecture

---

# 📧 Contact

**Sugumar R**

📧 contact.sugumarai@gmail.com

---

## ⭐ If you found this project useful, please consider giving it a Star on GitHub.
