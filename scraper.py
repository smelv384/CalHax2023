import requests
from bs4 import BeautifulSoup

# Author: Shaemus Melvin
# Takes in the course list url, outputs the list of rooms and times taken according to the course list
def scrape_web(URL):
    rooms = []
    times = []
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    table = soup.find("div", class_="unitis-course-list")
    list_items = table.findAll("tr", class_="collapsed primary-row collapsed-primary-row")
    for item in list_items:
        room = item.find("td", style="width:6em")
        print(room.text)
        rooms.append(room.text)
        time = item.find("td", style="width:11em")
        times.append(time.text)
        print(time.text)

    return rooms, times


rooms, times = scrape_web("https://contacts.ucalgary.ca/info/cpsc/courses")