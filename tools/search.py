from langchain_community.tools.tavily_search import TavilySearchResults
from config.settings import MAX_SEARCH_RESULTS


def build_news_search_tool() -> TavilySearchResults:
    """Return a Tavily search tool scoped to recent news."""
    return TavilySearchResults(
        max_results=MAX_SEARCH_RESULTS,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=False,
        include_images=False,
        name="search_news",
        description=(
            "Search the web for the latest and most trending news articles on a topic. "
            "Returns a list of relevant URLs with snippets. "
            "Use this first to discover what is currently trending."
        ),
    )
