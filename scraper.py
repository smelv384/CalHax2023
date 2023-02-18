import requests
from bs4 import BeautifulSoup

def scrape_web():
    URL = "https://contacts.ucalgary.ca/info/cpsc/courses"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("div", class_="unitis-course-list")
    list_items = table.findAll("tr", class_="collapsed primary-row collapsed-primary-row")
    for item in list_items:
        
        print(item.prettify())
        
scrape_web()
