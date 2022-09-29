from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class Scraper():
    """
    By.CLASS_NAME : UIUC,  dblp 
    By.XPATH : IEEE, ACM
    By.TAG_NAME : orchid
    """
    def __init__(self, url, field):
            self.data = {"Awards" : "", "Research Interests" : "", "Achievements" : "", "Education" : "", "Research Activities" : "", "Work Experience" : ""} 
            self.url = url
            self.chrome_options = Options()
            self.chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=self.chrome_options)
            if field == "class_name":
                self.field = By.CLASS_NAME
            elif field == "xpath":
                self.field = By.XPATH
            elif field == "tag_name":
                self.field = By.TAG_NAME


    def get_text(self, path):
        self.driver.get(self.url)
        with open(path, "r") as classNameFile:
            for line in classNameFile.readlines():
                l = str(line)
                field, data = l.split("|")
                text = ""
                for elem in self.driver.find_elements(self.field, data):
                    raw_text = elem.text
                    raw_text = raw_text.replace("\n", "; ")
                    text += raw_text + "; "
                self.data[field] += text + ". "
            return text


if __name__ == "__main__":
    scraper = Scraper("https://scholar.google.com/citations?user=HaI6LesAAAAJ&hl=en", "class_name")
    print(scraper.get_text("data_path_files/dblp.txt"))
