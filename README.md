# Conversational Intelligence Engine

## Overview

A context-aware conversational AI system built using LangChain, Groq LLM, ChromaDB, FastAPI, and Streamlit.

Unlike a stateless chatbot, the system maintains recent conversation history and retrieves relevant contextual information using Retrieval-Augmented Generation (RAG), enabling more intelligent and natural interactions.

The project is deployed with:

- FastAPI backend API
- Streamlit frontend interface
- ChromaDB vector storage
- Groq-powered LLM inference

---

## Features

- Context-aware conversation
- Retrieval-Augmented Generation (RAG)
- Conversation memory
- FastAPI backend
- Streamlit frontend
- ChromaDB vector database
- Sentence-transformer embeddings
- Previous interaction awareness
- Edge-case handling:
    - Empty input
    - Repeated queries
    - Invalid input

---

## Tech Stack

- Python
- LangChain
- Groq API
- ChromaDB
- HuggingFace Embeddings
- Sentence Transformers
- FastAPI
- Streamlit

---

## System Architecture

User Query
↓
Streamlit Frontend
↓
FastAPI API
↓
Load Conversation Memory
↓
Embedding Generation
↓
Retrieve Context from ChromaDB
↓
Prompt Construction
↓
Groq LLM
↓
Contextual Response
↓
Update Memory

---

## Project Structure

```text
Conversational-Intelligence-Engine/
│
├── chatbot.py
├── api.py
├── app.py
├── requirements.txt
├── README.md
├── screenshots/
└── docs/
```

---

## Installation

Clone repository:

```bash
git clone https://github.com/yourusername/Conversational-Intelligence-Engine.git
```

Move into directory:

```bash
cd Conversational-Intelligence-Engine
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```text
GROQ_API_KEY=your_api_key
```

---

## Run FastAPI backend

```bash
uvicorn api:app --reload
```

API runs at:

```text
http://127.0.0.1:8000
```

---

## Run Streamlit frontend

```bash
streamlit run app.py
```

---

## Deployment

Frontend:

YOUR_STREAMLIT_URL

Backend:

YOUR_RENDER_URL

---

## Demo

(Add screenshots)

![Home](screenshots/homepage.png)



---

## Example

User:

How do I proceed to the next stage?

Bot:

To proceed to the next stage, I would need more context regarding your current task or process...

---

## Design Decisions

- Implemented RAG architecture for retrieval
- Added memory window for conversational continuity
- Limited memory size for efficiency
- Used FastAPI to separate backend logic
- Used Streamlit for lightweight deployment
- Included input validation and edge-case handling

---

## Future Improvements

- Multi-user conversation support
- Authentication
- PDF upload capability
- Persistent memory storage
- Advanced reranking
