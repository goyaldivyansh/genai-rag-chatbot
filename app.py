import os
from time import sleep
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_google_genai import ChatGoogleGenerativeAI

# Initialize LLM (Gemini 2.5 Flash)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# Initialize session states cleanly
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

# This list will store our chat history tuples: {"role": "user/assistant", "content": "text"}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

## Document loading and embedding pipeline
def document_process(path):
    loader = PyPDFLoader(path)
    docs = loader.load()

    ## Splitting text into manageable chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=400,
        chunk_overlap=50
    )
    docs = splitter.split_documents(docs)

    ## Local HuggingFace Embeddings
    embeddings = HuggingFaceEmbeddings(
        model="sentence-transformers/all-mpnet-base-v2"
    )
    
    ## Create and save Chroma vector database to session state
    vector_db = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
    )
    
    st.session_state.vector_db = vector_db
    st.session_state.document_uploaded = True


st.subheader("RAG chatbot with Memory")

### 1. Document Upload UI
if not st.session_state.document_uploaded:
    file = st.file_uploader(label="Select your file", type="pdf")
    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())
        
        with st.spinner("Processing document and generating vector embeddings..."):
            document_process("./uploaded_document.pdf")
        
        st.success("Document successfully processed!")
        sleep(1.5)
        st.rerun()

### 2. Active Chat UI 
if st.session_state.document_uploaded and st.session_state.vector_db:
    
    #. Render existing conversation history on screen refresh
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])


    # Simple message container for history display if you want to scale later
    query = st.chat_input("Ask a question about your document")
    
    if query:
        
        # Display the user's new message instantly
        with st.chat_message("user"):
            st.write(query)
            
        # Append user message to memory state
        st.session_state.chat_history.append({"role": "user", "content": query})

        # FIX 1: Access similarity_search from the actual vector_db object
        documents = st.session_state.vector_db.similarity_search(query=query, k=2)
        
        context = ""
        for doc in documents:
            # FIX 2: Corrected property name to .page_content
            context += doc.page_content + "\n\n"

        # 4. Format chat history into a string for the model prompt
        history_str = ""
        for msg in st.session_state.chat_history[:-1]: # exclude the latest question we just added
            history_str += f"{msg['role'].capitalize()}: {msg['content']}\n"

        # Construct Prompt Template
        prompt = f"""You are a helpful assistant. Use the following context to answer the user's question accurately. 
        If the answer cannot be found in the context, politely say so.
        
        Context from Document:
        {context}
        
        Chat History:
        {history_str}
        
        Current Question: {query}
        Assistant:"""
        
        # Get AI Response
        with st.spinner("Thinking..."):
            result = llm.invoke(prompt)
        
        # Display the output clearly in the Streamlit App interface
        with st.chat_message("assistant"):
            st.write(result.content)
            
        # Append assistant response to memory state
        st.session_state.chat_history.append({"role": "assistant", "content": result.content})