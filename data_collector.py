from googlesearch import search
from webScraper import Scraper


def collect_data(person):
    text = ""
    print("ACM Author Profile:")
    text += scrape_acm(person)
    print("DBLP")
    text += scrape_dblp(person)
    print("Orcid")
    text += scrape_orcid(person)
    print("IEEE Xplore")
    text += scrape_IEEE(person)
    print("UIUR Experts")
    text += scrape_uiuc(person)
    return text


def scrape_acm(person):
    query = person + " ACM author profile"
    for url in search(query):
        if "https://dl.acm.org/profile" in url:
            scraper = Scraper(url, "xpath")
            return scraper.get_text("data_path_files/ACM.txt") + "\n"

def scrape_IEEE(person):
    query = person + " IEEE xplore"
    for url in search(query):
        if "https://ieeexplore.ieee.org/" in url:
            scraper = Scraper(url, "xpath")
            return scraper.get_text("data_path_files/IEEE.txt") + "\n"

def scrape_dblp(person):
    query = person + " dblp"
    for url in search(query):
        if "https://dblp.org/pid" in url:
            scraper = Scraper(url, "class_name")
            return scraper.get_text("data_path_files/dblp.txt") + "\n"

def scrape_uiuc(person):
    query = person + " uiuc experts"
    for url in search(query):
        if "https://experts.illinois.edu/" in url:
            scraper = Scraper(url, "class_name")
            return scraper.get_text("data_path_files/uiuc.txt") + "\n"

def scrape_orcid(person):
    query = person + " orcid"
    for url in search(query):
        if "https://orcid.org/" in url:
            scraper = Scraper(url, "tag_name")
            return scraper.get_text("data_path_files/orcid.txt") + "\n"



if __name__ == "__main__":
    txt = collect_data("kevin chenchuan chang")
    print(txt)
    
    
    