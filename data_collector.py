from urllib.request import urlopen
from bs4 import BeautifulSoup
from googlesearch import search

def extract_data_from_url(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")

    # kill all script and style elements
    for script in soup(['[document]','noscript','header','html','meta','head', 'input','script','style']):
        script.extract()    # rip it out

    # get text
    text = soup.get_text()

    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    chunks = (chunk if chunk.count(".") > 1 else "" for chunk in chunks)
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

# extract_data_from_url("https://www.cnn.com/2017/01/12/politics/biden-awarded-presidential-medal-of-freedom")

def search_google(query):
    urls = [url for url in search(query)]
    return urls