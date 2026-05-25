# README.md for Your GitHub Project

````md
# 📚 RAG Chatbot with Memory using Gemini + LangChain + ChromaDB

A powerful Retrieval-Augmented Generation (RAG) chatbot built using Streamlit, LangChain, Google Gemini 2.5 Flash, HuggingFace embeddings, and ChromaDB.

This application allows users to upload PDF documents and ask contextual questions about the content. The chatbot remembers conversation history and provides intelligent responses grounded in the uploaded document.

---

# 🚀 Features

✅ Upload PDF documents  
✅ Automatic document chunking  
✅ Semantic search using vector embeddings  
✅ ChromaDB vector database integration  
✅ Conversational memory support  
✅ Gemini 2.5 Flash integration  
✅ Streamlit chat interface  
✅ Local embeddings using HuggingFace  
✅ Context-aware responses from documents  

---

# 🧠 Tech Stack

| Technology | Purpose |
|---|---|
| Streamlit | Frontend UI |
| LangChain | LLM orchestration |
| Gemini 2.5 Flash | Large Language Model |
| HuggingFace Embeddings | Text embeddings |
| ChromaDB | Vector database |
| RecursiveCharacterTextSplitter | Document chunking |
| PyPDFLoader | PDF processing |

---

# 📂 Project Structure

```bash
project/
│
├── app.py
├── .env
├── requirements.txt
└── uploaded_document.pdf
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git

cd rag-chatbot
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file in the root directory.

```env
GOOGLE_API_KEY=your_google_api_key
```

Get your API key from:

https://aistudio.google.com/app/apikey

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

---

# 📖 How It Works

## Step 1 — Upload PDF

The user uploads a PDF document through the Streamlit UI.

## Step 2 — Document Processing

The PDF is loaded using:

```python
PyPDFLoader
```

---

## Step 3 — Text Chunking

The document is split into smaller chunks using:

```python
RecursiveCharacterTextSplitter
```

Configuration:

```python
chunk_size=400
chunk_overlap=50
```

---

## Step 4 — Generate Embeddings

Embeddings are generated using HuggingFace model:

```python
sentence-transformers/all-mpnet-base-v2
```

---

## Step 5 — Store in ChromaDB

Document embeddings are stored inside Chroma Vector Database for semantic retrieval.

---

## Step 6 — Similarity Search

When the user asks a question:

- Relevant chunks are retrieved
- Context is generated
- Chat history is included
- Prompt is sent to Gemini 2.5 Flash

---

## Step 7 — AI Response

The chatbot generates contextual answers grounded in the uploaded document.

---

# 💬 Example Questions

- Summarize the document
- What are the key points?
- Explain chapter 2
- What is the conclusion?
- Who is the author?
- Give me important highlights

---

# 🧠 Memory Support

The chatbot maintains chat history using:

```python
st.session_state.chat_history
```

This allows follow-up questions and contextual conversations.

---

# 📦 requirements.txt

```txt
streamlit
python-dotenv
langchain
langchain-community
langchain-text-splitters
langchain-huggingface
langchain-google-genai
chromadb
pypdf
sentence-transformers
docx2txt
```

---

# 🖼️ Application Preview

## Upload Document

- Upload PDF file
- Processing starts automatically
- Embeddings generated

## Chat Interface

- Ask questions naturally
- Context-aware responses
- Chat history preserved

---

# 🔥 Future Improvements

- Multi-file upload support
- DOCX and TXT support
- Source citations
- Streaming responses
- Chat export
- Authentication
- Cloud deployment
- Pinecone integration
- ConversationalRetrievalChain
- Docker support

---

# 🌐 Deployment Options

You can deploy this project on:

- Hugging Face Spaces
- Streamlit Cloud
- Render
- Railway
- AWS
- Azure

---

# 📚 Concepts Used

This project demonstrates:

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Embeddings
- Prompt Engineering
- Conversational AI
- LLM Integration
- Context Injection
- Memory Handling

---

# 🎯 Learning Outcomes

By building this project, you will learn:

✅ LangChain fundamentals  
✅ RAG pipeline architecture  
✅ ChromaDB vector storage  
✅ LLM application development  
✅ Streamlit frontend development  
✅ Embedding generation  
✅ Prompt engineering  
✅ Context-aware chatbot development  

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first to discuss what you would like to change.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Divyansh Goyal

LinkedIn: [https://linkedin.com/in/your-linkedin](https://www.linkedin.com/in/divyanshgoyal25/)

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub to support the project.
````
