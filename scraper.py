import requests
from bs4 import BeautifulSoup



# Author: Shaemus Melvin
# Takes in the course list url, outputs the list of rooms and times taken according to the course list
def scrape_web(URL):
    rooms = []
    times = []
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    table = soup.findAll("div", class_="item-list")
    for list_items in table:
        for item in list_items:
            roomList = item.findAll("td", style="width:6em")
            for room in roomList:
                rooms.append(room.text)

            
            timeList = item.findAll("td", style="width:11em")
            for time in timeList:
                if not len(time.text.split()) == 4:
                    rooms = rooms[:-1]
                    # firstTime = time.text[:15]
                    # secondTime = time.text[15:]
                    # times.append(firstTime)
                    # times.append(secondTime)
                else:
                    times.append(time.text)

    return rooms, times

def printClass(rooms, times):
    for i in range(0, len(times)):
        print(i)
        print(len(rooms))
        print(rooms[i])
        print(times[i])


rooms, times = scrape_web("https://contacts.ucalgary.ca/info/cpsc/courses")

printClass(rooms, times)
