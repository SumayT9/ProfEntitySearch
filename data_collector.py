from urllib.request import urlopen
from bs4 import BeautifulSoup
from googlesearch import search
import re

def extract_data_from_url(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(['script', 'noscript', 'style', 'meta', 'header', 'footer', 'button', 'a']):
        script.extract()    # rip it out

    # get text
    # print(soup.prettify())
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    chunks = (chunk if chunk.count(".") > 1 and chunk.count("@") == 0 and not chunk.startswith("https://") else None for chunk in chunks)
    text = ('. ').join(chunk for chunk in chunks if chunk)
    return text

def search_google(query, n):
    urls = [url for url in search(query) if "ratemyprofessors" not in url and "reddit" not in url and "github.com" not in url]
    return urls[:n]

if __name__ == "__main__":
    url = "https://www.semanticscholar.org/author/Geoffrey-Challen/32203761"
    text = ""
    text += extract_data_from_url(url)
    # except:
    #     print("fail")