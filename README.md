# Conversational Intelligence Engine

## Overview

A context-aware conversational AI system built using **LangChain, Groq LLM, FastAPI, and Streamlit**.

Unlike a stateless chatbot, this system maintains **conversation memory**, enabling coherent multi-turn interactions and context-aware responses.

---

## 🚀 Live Deployment

- **Frontend (Streamlit):**  
https://conversational-intelligence-enginegit-4eo6hq9mmvghtv33p9wxh8.streamlit.app/

- **Backend (FastAPI on Render):**  
https://conversational-intelligence-engine.onrender.com

---

## ✨ Features

- Context-aware conversational AI
- Short-term conversation memory
- Multi-turn dialogue support
- FastAPI backend for inference
- Streamlit frontend UI
- Input validation and error handling
- Handles edge cases:
  - Empty inputs
  - Repeated queries
  - Invalid requests

---

## 🧠 Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- Groq API
- Uvicorn

---

## 🏗️ System Architecture

User Query  
↓  
Streamlit Frontend  
↓  
FastAPI Backend  
↓  
Conversation Memory Loader  
↓  
Prompt Construction (LangChain)  
↓  
Groq LLM  
↓  
Generated Response  
↓  
Memory Update  

---

## 📁 Project Structure

Conversational-Intelligence-Engine/  
├── chatbot.py  
├── api.py  
├── app.py  
├── requirements.txt  
├── README.md  
├── screenshots/  
└── docs/  

---

## ⚙️ Installation

git clone https://github.com/yourusername/Conversational-Intelligence-Engine.git  
cd Conversational-Intelligence-Engine  
pip install -r requirements.txt  

---

## 🔐 Environment Variables

Create a `.env` file:

GROQ_API_KEY=your_api_key  

---

## ▶️ Run Locally

### Start Backend (FastAPI)

uvicorn api:app --reload  

Backend runs at:  
http://127.0.0.1:8000  

---

### Start Frontend (Streamlit)

streamlit run app.py  

Frontend runs at:  
http://localhost:8501  

---

## ☁️ Deployment Notes

### Frontend (Streamlit Cloud)

Make sure:
- requirements.txt is updated
- Backend URL is correctly set in app.py

---

### Backend (Render)

Start command:

uvicorn api:app --host 0.0.0.0 --port 10000  

Add environment variable:
- GROQ_API_KEY

---

## 📸 Demo

![Home](screenshots/homepage.png)

---


## 🧩 Design Decisions

- Conversation memory for contextual continuity
- Windowed memory to optimize performance
- Separation of backend and frontend
- Fast inference using Groq LLM
- Input validation for robustness

---

## 🔮 Future Improvements

- Persistent database-based memory
- Multi-user chat sessions
- Authentication system
- Long-term memory support
- Voice-based interaction
- Chat history dashboard
