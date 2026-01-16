from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from app.config import CHROMA_DIR, HF_EMBEDDING_MODEL


_embeddings = None


def get_embeddings():
    global _embeddings
    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name=HF_EMBEDDING_MODEL
        )
    return _embeddings


def get_vectorstore():
    return Chroma(
        collection_name="agentic_ai_ebook",
        persist_directory=CHROMA_DIR,
        embedding_function=get_embeddings()
    )
