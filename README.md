# 📄 RAG Document Assistant

An AI-powered **Retrieval-Augmented Generation (RAG)** application that allows users to upload documents and ask questions in natural language. The application retrieves the most relevant information from the uploaded documents using semantic search and generates accurate, context-aware responses using a Large Language Model (LLM).

---

## 🚀 Features

- 📂 Upload multiple PDF, DOCX, and TXT documents
- 📄 Automatic document loading and text extraction
- ✂️ Intelligent text chunking
- 🧠 Semantic search using HuggingFace Embeddings
- ⚡ Fast document retrieval with FAISS Vector Store
- 🤖 AI-generated responses using Groq LLM
- 💻 Interactive Streamlit web interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- HuggingFace Embeddings
- FAISS
- Groq API (Llama 3)
- PyPDF
- python-docx

---

## 📌 Project Workflow

```text
Upload Documents
        │
        ▼
Load & Extract Text
        │
        ▼
Split into Chunks
        │
        ▼
Generate Embeddings
        │
        ▼
Store Embeddings in FAISS
        │
        ▼
User Asks a Question
        │
        ▼
Retrieve Relevant Chunks
        │
        ▼
Groq LLM
        │
        ▼
Generate Final Answer
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/RAG-Document-Assistant.git
```

### 2. Navigate to the Project Folder

```bash
cd RAG-Document-Assistant
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure the API Key

This project uses the **Groq API** to generate AI responses.

1. Create a file named `.env` in the project root.

2. Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You can get a free API key by creating an account on the **Groq Developer Console**.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📤 Uploading Documents

After launching the application:

1. Open the Streamlit application in your browser.
2. Use the **Upload Files** button to upload one or more supported documents.
3. Ask questions related to the uploaded content.
4. The assistant retrieves the most relevant document chunks and generates an AI-powered response.

### Supported File Types

- PDF (.pdf)
- Microsoft Word (.docx)
- Text Files (.txt)

---

## 📁 Runtime Folders

The following folders are **not included** in this repository because they are created automatically while the application is running:

- **uploads/** – Temporarily stores documents uploaded through the Streamlit interface.
- **faiss_store/** – Stores the generated FAISS vector database used for semantic search.

These folders are generated automatically during runtime, so no manual setup is required.

---

## 🔮 Future Improvements

- Multi-document conversations
- Chat history
- Source citations
- Conversation memory
- ChromaDB integration
- Cloud deployment

---

## 💡 Note

This project uses **Groq** as the Large Language Model provider because it offers a generous free developer tier with fast inference, making it well-suited for learning, experimentation, and portfolio projects.

---

## 👨‍💻 Author

**Anjum Kousar**

B.Tech Computer Science Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, Natural Language Processing, Retrieval-Augmented Generation (RAG), and Generative AI.
