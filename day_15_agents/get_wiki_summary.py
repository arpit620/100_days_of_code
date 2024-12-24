from typing import Tuple
from agents.wiki_lookup_agents import lookup as wiki_lookup_agent
from chains.custom_chains import get_summary_chain
from utils.scrape_wiki import scrape_wiki_page
from utils.output_parsers import Summary


def get_wiki_summary(name: str, mock: bool = False) -> Tuple[str, Summary]:
    # url = wiki_lookup_agent(name)
    url = wiki_lookup_agent(name, mock=mock)
    content = scrape_wiki_page(url)
    chain = get_summary_chain()
    result = chain.invoke(input={"information": content})
    return url, result

if __name__ == "__main__":
    # url, result = get_wiki_summary("Steve Jobs")
    url, result = get_wiki_summary("Elon Musk", mock=True)
    print(url)
    print(result)


