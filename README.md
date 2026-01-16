# RAG AI Chatbot

A **Retrieval-Augmented Generation (RAG) based AI chatbot** that enables users to ask questions and generate summaries **strictly from an ebook**.  
Built using **LangChain, LangGraph, ChromaDB, FastAPI, and Streamlit**, this project demonstrates an agentic RAG pipeline with clean routing, retrieval, and answer generation.

## ⚙️ Environment Setup

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
CHROMA_DIR=./chroma_db
LLM_MODEL=gemini-2.5-flash
HF_EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

## Install dependencies:
```
pip install -r requirements.txt`
```

## PDF Ingestion
Place your ebook PDF in the project root and run:

```
python -m app.ingest
```

## Backend (FastAPI)
Start the backend server:
```
uvicorn backend.main:app --reload
```

## Frontend (Streamlit)
Run the frontend:
```
streamlit run frontend/front.py
```

## Tech Stack

- LangChain
- LangGraph
- ChromaDB
- FastAPI
- Streamlit
- HuggingFace Embeddings
- Google Gemini LLM
