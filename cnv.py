from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

import re
import nltk
from nltk.corpus import words

# Download dictionary
nltk.download('words')

english_words = set(words.words())


# ---------------- LLM ----------------
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)


# ---------------- Prompt ----------------
prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Conversation History:
{history}

Question:
{question}
"""
)


# ---------------- Memory ----------------
memory = ConversationBufferWindowMemory(
    k=3,
    return_messages=True
)


# ---------------- Chain ----------------
chat_chain = (
{
    "question": RunnablePassthrough(),
    "history": lambda x: memory.load_memory_variables({})["history"]
}
| prompt
| llm
)


# ---------------- History store ----------------
query_history = []


# ---------------- Dictionary Ratio ----------------
def dictionary_ratio(text):

    tokens = text.lower().split()

    if not tokens:
        return 0

    valid_words = sum(
        token in english_words
        for token in tokens
    )

    return valid_words / len(tokens)


# ---------------- Gibberish Check ----------------
def is_gibberish(text):

    text = text.strip().lower()

    if not text:
        return True

    # too many special characters
    if len(text) > 0:
        special_ratio = len(re.findall(r'[^a-zA-Z0-9\s]', text)) / len(text)
        if special_ratio > 0.6:
            return True

    tokens = text.split()

    # if multiple tokens and none are dictionary words → gibberish
    if len(tokens) > 1:
        valid = sum(token in english_words for token in tokens)
        if valid == 0:
            return True

    return False


# ---------------- Main Function ----------------
def ask_question(query):

    # None check
    if query is None:
        return "Give valid input"

    if not isinstance(query, str):
        return "Give valid input"

    query = query.strip()

    # empty input
    if query == "":
        return "It looks like you didn't type anything. How can I help you?"

    # literal quotes
    if query in ['""', "''"]:
        return "Give valid input"

    # short input
    if len(query) < 2:
        return "Give valid input"

    # max length
    MAX_LENGTH = 2000
    if len(query) > MAX_LENGTH:
        return "Give valid input"

    # gibberish check
    if is_gibberish(query):
        return "Give valid input"

    # repeated query check (last only)
    if query_history and query.lower() == query_history[-1]:
        return "Repeated query detected"

    # dictionary ratio check (only weak filtering)
    ratio = dictionary_ratio(query)
    if len(query.split()) > 1 and ratio == 0:
        return "Input seems meaningless"

    try:

        # LLM call
        response = chat_chain.invoke(query)

        # save memory
        memory.save_context(
            {"input": query},
            {"output": response.content}
        )

        # store history
        query_history.append(query.lower())

        
        return response.content

    except Exception as e:
        return f"Error: {str(e)}"