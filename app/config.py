import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHROMA_DIR = os.getenv("CHROMA_DIR")
LLM_MODEL = os.getenv("LLM_MODEL")
HF_EMBEDDING_MODEL = os.getenv("HF_EMBEDDING_MODEL")
