import streamlit as st
import requests

st.title("Conversational-Intelligence Chatbot")

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
        "https://conversational-intelligence-engine-1.onrender.com/chat",
        json={"question": question}
    )

    answer = response.json()["response"]

    st.session_state.messages.append(
        {"user": question, "bot": answer}
    )

    st.rerun()
