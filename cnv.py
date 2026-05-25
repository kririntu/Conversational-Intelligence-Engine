from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Conversation History:
{history}

Question:
{question}
"""
)

memory = ConversationBufferWindowMemory(
    k=3,
    return_messages=True
)

chat_chain = (
{
    "question": RunnablePassthrough(),
    "history": lambda x:
        memory.load_memory_variables({})["history"]
}
| prompt
| llm
)

def ask_question(query):

    response = chat_chain.invoke(query)

    memory.save_context(
        {"input": query},
        {"output": response.content}
    )

    return response.content
