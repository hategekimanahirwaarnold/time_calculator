import re
import math

def add_time(start, duration, day = ""):
    alldays = {
        "Monday": ["Monday", 0], 
        "Tuesday": ["Tuesday", 1], 
        "Wednesday": ["Wednesday", 2], 
        "Thursday": ["Thursday", 3], 
        "Friday": ["Friday", 4], 
        "Saturday": ["Saturday", 5], 
        "Sunday": ["Sunday", 6]
    }
    # print("start: ", start, "duration: ", duration)
    if day:
        day = day.lower()
        splitted = re.findall(r'\w', day)
        splitted[0] = splitted[0].upper()
        day = "".join(splitted)
    startHour = int(re.findall(r'(\d+):', start)[0])
    addHour = int(re.findall(r'(\d+):', duration)[0])
    startMin = int(re.findall(r':(\d+)', start)[0])
    addMin = int(re.findall(r':(\d+)', duration)[0])
    am_pm = re.findall(r'\d+\s([a-z]+)', start, re.IGNORECASE)[0]
    
    # check all parameters if they are extracted well
    # if day:
    #     print("day: ", day)
    # print("starting hour: ", startHour, "starting minutes: ", startMin, "am_pm: ", am_pm)
    # print("add hour: ", addHour, "add minutes: ", addMin)
    # start operations
    finalday = ""
    minutes = startMin + addMin
    if minutes > 59:
        addHour = addHour + 1
        minutes = minutes % 60
    hours = startHour + addHour
    finalHour = hours % 12
    if finalHour == 0:
        finalHour = 12
    # print("All hours: ", hours, "final hour: ", finalHour, "All minutes: ", minutes)
    if hours >= 12:
        cycles = math.ceil(addHour / 12)
        toaddOnPosition = 0
        # print("Hours greater than 12! cycles: ", cycles)
        if am_pm == "AM":
            if cycles % 2 == 1:
                am_pm = "PM"
            if cycles / 2 == 1:
                finalday = "(next day)"
                toaddOnPosition = 1
            elif cycles / 2 > 1:
                toaddOnPosition = math.floor(cycles / 2)
                finalday = "(" + str(toaddOnPosition) + " days later)"
        elif am_pm == "PM":
            if cycles % 2 == 1:
                am_pm = "AM"
            if cycles == 1:
                finalday = "(next day)"
                toaddOnPosition = 1
            elif cycles / 2 > 1:
                toaddOnPosition = math.ceil(cycles / 2)
                finalday = "(" + str(toaddOnPosition) + " days later)"
        if day:
            position = alldays[day][1]
            # print("Initial position of the day: ", position, "day: ", alldays[day][0])
            position = (position + toaddOnPosition) % 7
            # print("final position: ", position)
            for one in alldays.values():
                # print("One of the days: ", one)
                if one[1] == position:
                    day = one[0]
                    # print("final day: ", day)
                    break

    # print("final am_pm: ", am_pm)
    # print("following day: ", finalday)
    finalHour = str(finalHour)

    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)
    string = finalHour + ":" + minutes + " " + am_pm
    if day:
        string = string + ", " + day
    if finalday:
        string = string + " " + finalday
    return string
