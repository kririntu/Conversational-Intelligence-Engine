import os
from langchain_classic.memory import ConversationBufferWindowMemory
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq




# -------------------------
# Split documents
# -------------------------

splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
                chunk_overlap=50
                )

docs = splitter.create_documents([
        "Machine learning is a subset of artificial intelligence.",
            "RAG combines retrieval with LLM generation."
            ])


# -------------------------
# Embeddings
# -------------------------

embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
            )


# -------------------------
# Vector store
# -------------------------

vectorstore = Chroma.from_documents(
            documents=docs,
                embedding=embeddings,
                    persist_directory="./chroma_db"
                    )

retriever = vectorstore.as_retriever(
            search_kwargs={"k":2}
            )


# -------------------------
# LLM
# Reads GROQ_API_KEY automatically
# -------------------------

llm = ChatGroq(
            model="llama-3.3-70b-versatile",
                temperature=0
                )


# -------------------------
# Prompt
# -------------------------

prompt = ChatPromptTemplate.from_template(
        """
        You are a helpful AI assistant.

        Use the context below.

        Context:
        {context}

        Conversation History:
        {history}

        Question:
        {question}
        """
        )


# -------------------------
# Memory
# -------------------------

memory = ConversationBufferWindowMemory(
            k=3,
                return_messages=True
                )


# -------------------------
# Build chain
# -------------------------

rag_chain = (

        {
                "context": retriever,
                    "question": RunnablePassthrough(),
                        "history": lambda x:
                                memory.load_memory_variables({})["history"]
                                }

        | prompt
        | llm
        )


# -------------------------
# function used by API
# -------------------------

def ask_question(query):

        response = rag_chain.invoke(query)

        memory.save_context({"input": query}, {"output": response.content}
                                        )

        return response.content
