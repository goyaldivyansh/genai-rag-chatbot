# genai-rag-chatbot

A great `README.md` file acts as the face of your repository. It explains what your project does, how it works underneath the hood, and how someone else can set it up on their own machine.

Here is a professionally formatted, production-ready `README.md` file tailored exactly to the code you just provided.

---

### 📝 Production-Ready `README.md`

Copy and paste everything inside the block below into a file named **`README.md`** in your project root directory.

```markdown
# 🤖 RAG Chatbot with Memory & Multi-Format Support

An AI-powered Retrieval-Augmented Generation (RAG) chatbot built with **Streamlit**, **LangChain**, and **Google Gemini 2.5 Flash**. This application allows users to upload local documents (`.pdf`), converts them into vector embeddings using a local Hugging Face transformer model, stores them in a **Chroma DB** vector store, and provides an interactive chat interface with full contextual memory.

---

## 🚀 Key Features

* **Dynamic Data Ingestion:** Upload and parse document structures using optimized text splitters.
* **Persistent Chat Memory:** Tracks user-assistant conversation states across Streamlit's structural execution loops.
* **Fully Local Embeddings:** High-performance phrase tracking using the `sentence-transformers/all-mpnet-base-v2` model running locally.
* **Semantic Search:** Harnesses Chroma DB vector indices to grab the top context blocks matching user input.
* **State-of-the-Art Core LLM:** Powers logical responses using Google's ultra-fast `gemini-2.5-flash` model.

---

## 🛠️ Code Architecture & Core Components Explained

The application logic is broken down into structured execution steps:

### 1. Initialization and State Control
Streamlit natively reruns the entire script file from top to bottom on every user submission. To prevent data erasure, `st.session_state` containers are configured at boot:
* `vector_db`: Retains the active vectorized index of your file across query interactions.
* `document_uploaded`: Tracks whether the system should display the uploader screen or the chat board.
* `chat_history`: Stores a dynamic array of previous message dictionaries (`role` and `content`).

### 2. The Ingestion Pipeline (`document_process`)
When a file passes through the file uploader:
1. **Document Extraction:** `PyPDFLoader` targets the saved storage path and reads the document text.
2. **Chunking Engine:** `RecursiveCharacterTextSplitter` breaks huge walls of text into micro-segments (`chunk_size=400`, `chunk_overlap=50`) to keep contextual references clean without overflowing the LLM window.
3. **Vectorizing Engine:** `HuggingFaceEmbeddings` maps textual information into numerical vector space using mathematical vectors.
4. **Vector Storage:** `Chroma.from_documents` compiles the vectors into a fast database for immediate retrieval.

### 3. Contextual Retrieval Engine
When you pass a message to `st.chat_input`, the script grabs the input text strings and fires an internal sequence:
1. **Vector Scan:** `vector_db.similarity_search` calculates mathematical distance to pull the top two (`k=2`) matching chunks.
2. **Context Compilation:** The page texts are bound together into a single global `context` variable block.
3. **History Extraction:** The code extracts the `chat_history` payload array into a raw transcript layout (`history_str`).
4. **Prompt Conditioning:** The variables are packed into an engineering-optimized prompt template:
```text
   Context from Document: ...
   Chat History: ...
   Current Question: ...

```

5. **Inference:** The bundled template maps to `llm.invoke(prompt)`, allowing Gemini to speak accurately based on your file history.

---

## 📋 Installation & Local Setup

Follow these steps to run the application on your computer:

### 1. Clone the Project Workspace

```bash
git clone [https://github.com/goyaldivyansh/genai-rag-chatbot.git](https://github.com/goyaldivyansh/genai-rag-chatbot.git)
cd genai-rag-chatbot

```

### 2. Configure a Virtual Environment

```bash
# Create environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate

# Activate environment (Mac/Linux)
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install streamlit langchain langchain-community langchain-huggingface langchain-chroma langchain-google-genai python-dotenv pydantic pypdf

```

### 4. Configure Your Environment Keys

Create a file named `.env` in the root folder of your project:

```env
GOOGLE_API_KEY=your_actual_gemini_api_key_here

```

### 5. Launch the Application

```bash
streamlit run app.py

```

---

## 🔒 Security Note

This repository contains a `.gitignore` profile mapping sensitive entries. **Never** remove `.env` from your tracking ignores, ensuring your Google API credentials remain locked away safely from public scraping bots.

```

```

```

```
