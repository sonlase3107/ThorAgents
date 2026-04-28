import os
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

MODEL_NAME = "claude-sonnet-4-6"
MAX_SEARCH_RESULTS = 5
MAX_ARTICLE_CHARS = 4000
REQUEST_TIMEOUT = 15
