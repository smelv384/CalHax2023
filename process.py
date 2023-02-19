import unicodedata
from scraper import rooms, times
from datetime import time

rooms_edited = list()
times_edited = list()
daysAndTime = list()

for i in range(0, len(rooms)):
    rooms_edited.append(unicodedata.normalize("NFKD", rooms[i]))
for j in range(0, len(times)):
    times_edited.append(unicodedata.normalize("NFKD", times[j]))
    daysAndTime.append(times_edited[j].split(" ", 1))

def getRoom():
    return rooms_edited

def getDays():
    d = list()
    for i in range(0, len(daysAndTime)):
        days = daysAndTime[i][0]
        a = []
        for j in range(0, len(days)):
            if days[j] == 'M':
                a.append("Monday")
            elif days[j] == 'T':
                a.append("Tuesday")
            elif days[j] == 'W':
                a.append("Wednesday")
            elif days[j] == 'R':
                a.append("Thursday")
            else:
                a.append("Friday")
        d.append(a)
    return d

def getBeginTime():
    t = list()
    for i in range(0, len(daysAndTime)):
        print(daysAndTime)
        time = daysAndTime[i][1].split(" - ")
        t.append(time[0])
    return t

def getEndTime():
    t = list()
    for i in range(0, len(daysAndTime)):
        time = daysAndTime[i][1].split(" - ")
        t.append(time[1])
    return t

def getBeginTimeInTimeObject():
    timeList = getBeginTime()
    ttimeList = list()
    for i in range(0, len(timeList)):
        tim = timeList[i].split(':')
        ttimeList.append(time(hour = tim[0], minute = tim[1]))
    return time(hour = tim[0], minute = tim[1])

def getEndTimeInTimeObject():
    timeList = getEndTime()
    ttimeList = list()
    for i in range(0, len(timeList)):
        tim = timeList[i].split(':')
        ttimeList.append(time(hour = tim[0], minute = tim[1]))
    return time(hour = tim[0], minute = tim[1])
print("getDays: ")
print(getDays())
print("getBeginTime: ")
print(getBeginTime())
print("getEndTime: ")
print(getEndTime())
print("getBeginTimeInTimeObject: ")
print(getBeginTimeInTimeObject())
print("getEndTimeInTimeObject: ")
print(getEndTimeInTimeObject())