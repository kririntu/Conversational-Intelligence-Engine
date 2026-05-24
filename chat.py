import streamlit as st
import requests

st.title("RAG Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# display history
for msg in st.session_state.messages:
    st.write("You:", msg["user"])
    st.write("Bot:", msg["bot"])

# chat input automatically resets
question = st.chat_input("Type your message")

if question:

    response = requests.post(
        "http://127.0.0.1:8000/chat",
        json={"question": question}
    )

    answer = response.json()["response"]

    st.session_state.messages.append(
        {"user": question, "bot": answer}
    )

    st.rerun()