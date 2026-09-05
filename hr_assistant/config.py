import os
from dotenv import load_dotenv

load_dotenv()


GROQ_API_KEY=os.getenv("GROQ_API_KEY")
JINA_API_KEY=os.getenv("JINA_API_KEY")

VECTOR_STORE_PATH=os.path.join("data","faiss_index")

DATA_FILE_PATH=os.path.join("data", "hr_policy.txt")
LLM_MODEL_NAME="openai/gpt-oss-120b"
EMBEDDING_MODEL_NAME="jina-embeddings-v2-base-en"

CHUNK_SIZE=500
CHUNK_OVERLAP=50

TOP_K_RESULTS=3
SYSTEM_PROMPT=(
    "You are a friendly HR assistant. Always use seach_hr_policy tool to look up" 
"Facts before answering, If the answer is not in the search result say you do not know rather than guessing" 
)

def check_api_keys():
    if not GROQ_API_KEY: 
        raise ValueError("Missing GROQ_API_KEY")
    if not JINA_API_KEY:
        raise ValueError("Missing JINA_API_KEY")