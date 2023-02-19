import scraper
from datetime import time
import pandas as pd

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

class Day:
    def booking_to_timelists(self):
        pd.date_range(start='2023-02-19', end='2023-02-25', freq='1D')
        # date + start_time
        # date + end_time
        # df['TDate'] +=  pd.to_timedelta(df.Hour, unit='h')
        # print (df)
        t1 = pd.to_datetime('2023-02-19 08:00:00')
        t2 = pd.to_datetime('2023-02-19 21:00:00')
        #t3 = pd.to_datetime('2023-02-25 00:00:00')
        series = pd.date_range(t1,t2,freq='15min')
        iso8601 = [t.strftime('%Y%m%dT%H:%M%SZ') for t in series]
        return iso8601

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
            newBooking = Booking(rooms[i], times[i])
            bookings.append(newBooking)
            prettyPrint(newBooking)
    return bookings

# check if there is an overlap between two time slots
def has_overlap(a_start, a_end, b_start, b_end):
    latest_start = max(a_start, b_start)
    earliest_end = min(a_end, b_end)
    return latest_start <= earliest_end

def has_overlap(bookingA: Booking, bookingB: Booking):
    has_overlap(bookingA.startTime(), bookingA.endTime(), bookingB.startTime(), bookingB.endTime())

def user_booking_overlap(user_booking: Booking):
    bookings = getBookings()
    for classbooking in bookings:
        if set(classbooking.days).intersection(user_booking.days):
            if has_overlap(user_booking, classbooking):
                return True
    return False
