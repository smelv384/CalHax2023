import scraper

room, time = scraper.scraper.web()

def getDay():
    d = list()
    days = time.split(" ", 1)
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