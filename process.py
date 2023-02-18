import scraper

room, time = scraper.scraper.web()
daysAndTime = time.split(" ", 1)

def getRoom():
    return room

def getDays():
    d = list()
    days = daysAndTime[0]
    for i in range(0, len(days)):
        if days[i] == 'M':
            d.append("Monday")
        elif days[i] == 'T':
            d.append("Tuesday")
        elif days[i] == 'W':
            d.append("Wednesday")
        elif days[i] == 'R':
            d.append("Thursday")
        else:
            d.append("Friday")
    return d

def getBeginTime():
    t = list()
    timee = daysAndTime[1].split(" - ")
    return timee[0]

def getEndTime():
    t = list()
    timee = daysAndTime[1].split(" - ")
    return timee[1]