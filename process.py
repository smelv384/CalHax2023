import scraper
from datetime import time
import json
rooms, times = scraper.scrape_web("https://contacts.ucalgary.ca/info/cpsc/courses")

# Authors: Shaemus Melvin, Harry Lee
# Takes two arrays of rooms and times/dates, 

def getRoom():
    return room

def getDays(time):
    d = []
    for i in range(0, len(time)):
        if time[i] == 'M':
            d.append("Monday")
        elif time[i] == 'T':
            d.append("Tuesday")
        elif time[i] == 'W':
            d.append("Wednesday")
        elif time[i] == 'R':
            d.append("Thursday")
        elif time[i] == 'F':
            d.append("Friday")
    return d

def getBeginTime(roomTime):
    timeStr = roomTime.split()
    return timeStr[1]

def getEndTime(roomTime):
    timeStr = roomTime.split()
    return timeStr[3]

def getBeginTimeInTimeObject(roomTime):
    timeString = getBeginTime(roomTime)
    tim = timeString.split(':')
    return time(hour = int(tim[0]), minute = int(tim[1]))

def getEndTimeInTimeObject(roomTime):
    timeString = getEndTime(roomTime)
    tim = timeString.split(':')
    return time(hour = int(tim[0]), minute = int(tim[1]))
    
from datetime import time

class Booking:
    building = ""
    floor  = 0
    roomNumber  = 0
    days = []
    startTime =  time()
    endTime =  time()
    id = -1

    def __init__(self, room, roomTime, id):
        if (room != "TBA" and roomTime != "TBA"):
            self.building = room.split()[0]
            print(room)
            if (room.split()[1].isdigit()):
                self.floor = (room.split())[1][0]
                self.roomNumber = room.split()[1][1:]
            else:
                self.floor = -1
                self.roomNumber = room.split()[1]
            self.days = getDays(roomTime)
            self.startTime = getBeginTimeInTimeObject(roomTime)
            self.endTime = getEndTimeInTimeObject(roomTime)
            self.id = id
        return

def prettyPrint(booking):
    output = ""
    output += ((booking.building) + "\n")
    output += ((str(booking.floor)) + "\n")
    output += ((str(booking.roomNumber)) + "\n")
    for day in booking.days:
        output += ((day) + "\n")
    output += ((str(booking.startTime)) + "\n")
    output += ((str(booking.endTime)) + "\n")
    return output

def getBookings():
    bookings = []
    for i in range(0, len(rooms)):
        if (rooms[i] != "TBA" and times[i] != "TBA"):
            newBooking = Booking(rooms[i], times[i], i)
            bookings.append(newBooking)
            prettyPrint(newBooking)

    return bookings


def toJson():
    jsonList = []
    bookingList = getBookings()
    print(prettyPrint(bookingList[0]))
    for booking in bookingList:
        prettyPrint(booking)
        bookingJson = ""
        bookingJson = "".join('{"building" : ' + booking.building + ',"floor":' + booking.floor + ',"roomNumber":' + booking.roomNumber + ', "days": [')
        for day in booking.days:
            bookingJson.join('"' + day + '",')
        bookingJson = bookingJson.join('], "startTime": ' + str(booking.startTime) + ', "endTime": ' + str(booking.endTime) + ',"id":' + str(booking.id) + '}')
        
        print(bookingJson)
        properJson = json.loads(bookingJson)

        print(json.dumps(properJson, indent=4))
        jsonList.append(properJson)
    return jsonList

toJson()

# getBookings()