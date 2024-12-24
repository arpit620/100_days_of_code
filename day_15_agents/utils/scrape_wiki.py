import requests
from bs4 import BeautifulSoup

def scrape_wiki_page(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to load page {url}")
    
    soup = BeautifulSoup(response.content, 'html.parser')
    content = soup.find(id="bodyContent")
    
    if not content:
        raise Exception("Could not find the body content on the page")
    
    paragraphs = content.find_all('p', limit=3)
    first_two_paragraphs = "\n\n".join([p.get_text() for p in paragraphs])
    
    return first_two_paragraphs


if __name__ == "__main__":
    # Example usage:
    # url = "https://en.wikipedia.org/wiki/Web_scraping"
    url = "https://en.wikipedia.org/wiki/Elon_Musk"
    
    print(scrape_wiki_page(url))
