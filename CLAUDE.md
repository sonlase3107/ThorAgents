# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Copy and fill in API keys
cp .env.example .env

# Run with default query (top trending news right now)
python main.py

# Run with a specific topic
python main.py "AI breakthroughs this week"
python main.py "climate policy latest developments"
```

## Architecture

This is a LangChain/LangGraph ReAct agent that discovers and summarizes trending news from online newspapers.

**Execution flow:**
1. `main.py` parses the CLI query and calls `run_news_agent(query)`
2. `agent/news_agent.py` builds a `create_react_agent` (LangGraph prebuilt) with `claude-sonnet-4-6` and two tools
3. The agent loops: searches → scrapes → synthesizes until it has enough to produce a trend report
4. Final Markdown report is printed via `rich`

**Tools** (`tools/`):
- `search_news` — wraps `TavilySearchResults`; returns URLs + snippets for a query
- `scrape_article` — fetches a URL, strips noise tags, returns up to `MAX_ARTICLE_CHARS` of body text

**Agent reasoning** (`agent/prompts.py`):
- System prompt enforces a fixed report structure: Top Trends, Key Stories, Emerging Signals, Sources
- Temperature is set to 0 for consistent, factual output

**Config** (`config/settings.py`):
- `MODEL_NAME`, `MAX_SEARCH_RESULTS`, `MAX_ARTICLE_CHARS`, `REQUEST_TIMEOUT` are the main tuning knobs

## API Keys Required

| Key | Where to get |
|-----|-------------|
| `ANTHROPIC_API_KEY` | console.anthropic.com |
| `TAVILY_API_KEY` | app.tavily.com (free tier available) |
