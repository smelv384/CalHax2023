import scraper
from datetime import time
room, tim = scraper.scraper.web()
daysAndTime = tim.split(" ", 1)

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
    time = daysAndTime[1].split(" - ")
    return time[0]

def getEndTime():
    t = list()
    time = daysAndTime[1].split(" - ")
    return time[1]

def getBeginTimeInTimeObject():
    timeString = getBeginTime()
    tim = timeString.split(':')
    timee = time(hour = tim[0], minute = tim[1])

def getEndTimeInTimeObject():
    timeString = getEndTime()
    tim = timeString.split(':')
    timee = time(hour = tim[0], minute = tim[1])