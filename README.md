# RAG-Powered Chatbot System 🤖

This project is a **Retrieval-Augmented Generation (RAG) based chatbot application** built using **Streamlit**, **LangChain**, and **Groq LLMs**.  
It allows users to ask questions based on **PDF documents** or **web-scraped content**.


---

## ⚠️ Important Note


⚠️ ** A valid Groq API key is mandatory to run this application.**

- Users must create a Groq account and generate an API key from:  
  https://console.groq.com/keys
- The application will **not function without a valid API key**
- The API key can be provided in either of the following ways:
  - Add it to a `.env` file as `GROQ_API_KEY`
  - Enter it directly in the Streamlit sidebar at runtime

> 🔐 For security reasons, API keys are never stored or logged by the application.


## 🚀 Features

- 📄 PDF-based Question Answering
- 🌐 Website-based Question Answering using Web Scraping
- 🧠 Semantic search using FAISS vector database
- 🔎 Context-aware responses using RAG
- 🔐 User-provided Groq API Key
- 🎨 Interactive UI built with Streamlit
- 🐳 Docker support for easy deployment

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **FAISS**
- **HuggingFace Embeddings**
- **Groq LLM API**
- **BeautifulSoup & Requests (Web Scraping)**
- **Docker**

---

---

## 🌐 Web Scraping Module (Separate Explanation)

### 📁 `Web_Scraping/rag_web_scraping.py`

This file **only contains the web scraping logic** and is kept separate for better modularity and reusability.

### 🔹 Purpose
- Scrapes textual content from a given website URL
- Extracts meaningful text from HTML elements such as:
  - Paragraphs (`<p>`)
  - Lists (`<li>`)
  - Tables (`<td>`)
  - Headings (`<h1>`, `<h2>`, `<h3>`)
- Prepares clean text data that can later be used for:
  - Vector embedding
  - RAG-based question answering
    
---

### 🔹 Why Separate?
- Keeps scraping logic independent from UI
- Easy to reuse or extend scraping functionality
- Improves code readability and maintainability

> ⚠️ Note: This file **does not contain LLM, embeddings, or vector database logic**.  
> It strictly focuses on **web data extraction only**.


---


## 💬 How It Works (High Level)

- User uploads a PDF or provides a website URL
- Content is extracted and split into smaller text chunks
- Text chunks are converted into embeddings using HuggingFace models
- FAISS stores embeddings for fast semantic retrieval
- Relevant context is fetched based on the user query
- Groq LLM generates accurate answers using Retrieval-Augmented Generation (RAG)


## ▶️ How to Run the Application

### 3️⃣ Run the App

```bash
streamlit run rag_streamlit_app.py
```

### 🐳 Run with Docker
Build the Docker image:

```bash
docker build -t rag-chatbot .
```

### 🐳 Run the container:

```bash
docker run -p 8501:8501 rag-chatbot
```

### Then --> open your browser and navigate to:

```bash
http://localhost:8501
```






