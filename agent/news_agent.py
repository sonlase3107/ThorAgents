from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage

from config.settings import ANTHROPIC_API_KEY, MODEL_NAME
from tools.search import build_news_search_tool
from tools.news_scraper import scrape_article
from agent.prompts import SYSTEM_PROMPT


def build_agent():
    llm = ChatAnthropic(
        model=MODEL_NAME,
        anthropic_api_key=ANTHROPIC_API_KEY,
        temperature=0,
    )
    tools = [build_news_search_tool(), scrape_article]
    return create_react_agent(llm, tools, prompt=SYSTEM_PROMPT)


def run_news_agent(query: str) -> str:
    agent = build_agent()
    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    return result["messages"][-1].content
