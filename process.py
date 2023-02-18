import scraper
from datetime import time
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


class Booking:
    building = ""
    floor  = 0
    roomNumber  = 0
    days = []
    startTime =  time()
    endTime =  time()

    def __init__(self, room, roomTime):
        if (room != "TBA" and roomTime != "TBA"):
            self.building = room.split()[0]
            if (room.split()[1].isdigit()):
                self.floor = (room.split())[1][0]
                self.roomNumber = room.split()[1][1:]
            else:
                self.floor = -1
                self.roomNumber = room.split()[1]
            self.days = getDays(roomTime)
            self.startTime = getBeginTimeInTimeObject(roomTime)
            self.endTime = getEndTimeInTimeObject(roomTime)
        return
    
def prettyPrint(booking):
    print(booking.building)
    print(booking.floor)
    print(booking.roomNumber)
    for day in booking.days:
        print(day)
    print(booking.startTime)
    print(booking.endTime)
    return

def getBookings():
    bookings = []
    for i in range(0, len(rooms)):
        if (rooms[i] != "TBA" and times[i] != "TBA"):
            newBooking = Booking(rooms[i], times[i])
            bookings.append(newBooking)

    return bookings
