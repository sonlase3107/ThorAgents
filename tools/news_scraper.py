import requests
from bs4 import BeautifulSoup
from langchain_core.tools import tool
from config.settings import MAX_ARTICLE_CHARS, REQUEST_TIMEOUT

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}

# Tags that typically hold boilerplate rather than article content
_NOISE_TAGS = ["script", "style", "nav", "header", "footer", "aside", "form", "iframe"]


@tool
def scrape_article(url: str) -> str:
    """Fetch and extract the main text content of a news article from a URL.

    Use this after finding article URLs via search to read the full content
    before summarizing or analyzing trends.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.RequestException as e:
        return f"Failed to fetch article: {e}"

    soup = BeautifulSoup(response.text, "lxml")

    for tag in soup(_NOISE_TAGS):
        tag.decompose()

    # Prefer semantic article containers; fall back to <body>
    container = (
        soup.find("article")
        or soup.find("main")
        or soup.find(class_=lambda c: c and "article" in c.lower())
        or soup.body
    )

    if not container:
        return "Could not extract article content."

    text = " ".join(container.get_text(separator=" ").split())
    return text[:MAX_ARTICLE_CHARS] + ("..." if len(text) > MAX_ARTICLE_CHARS else "")
