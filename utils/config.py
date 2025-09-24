from dotenv import load_dotenv
import  os

load_dotenv()

class Config:
    """All configuration variables for the application."""
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    EMBEDDING_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-4o-mini"

    # Text processing settings
    DEFAULT_CHUNK_SIZE = 1000
    DEFAULT_CHUNK_OVERLAP = 200
    MAX_CHUNK_SIZE = 2000
    MIN_CHUNK_SIZE = 500

    # RAG settings
    DEFAULT_TOP_K = 5
    MAX_TOP_K = 10



