from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_PORTFOLIO_PATH = BASE_DIR / "data" / "raw" / "portfolio.csv"
PROCESSED_PORTFOLIO_PATH = BASE_DIR / "data" / "processed" / "portfolio_clean.csv"

CHROMA_DIR = BASE_DIR / "vectorstore" / "chromadb"
OUTPUT_DIR = BASE_DIR / "outputs" / "generated_emails"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
COLLECTION_NAME = "portfolio_collection"