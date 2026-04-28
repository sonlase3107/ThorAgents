import sys
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from agent.news_agent import run_news_agent

console = Console()

DEFAULT_QUERY = "What are the most trending news stories right now?"


def main():
    query = " ".join(sys.argv[1:]).strip() or DEFAULT_QUERY

    console.print(Panel(f"[bold cyan]Query:[/bold cyan] {query}", expand=False))
    console.print("[dim]Agent is researching...[/dim]\n")

    result = run_news_agent(query)
    console.print(Markdown(result))


if __name__ == "__main__":
    main()
