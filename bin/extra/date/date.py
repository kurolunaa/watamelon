import datetime
import math

def convertTime(inputYear = None, inputMonth = None, inputDay = None, inputHour = None, inputMinute = None, inputSecond = None):
    now = datetime.datetime.now()
    currentSecond = now.second
    currentMinute = now.minute
    currentHour = now.hour
    currentDay = now.day
    currentMonth = now.month
    currentYear = now.year
    
    # inputYear = 1   # 1 - 9999
    # inputMonth = 1     # 1 - 12
    # inputDay = 1       # 1 - 31*
    # inputHour = 0      # 0 - 23
    # inputMinute = 0    # 0 - 59
    # inputSecond = 0    # 0 - 59

    if (inputYear != None):
        currentYear = inputYear
    if (inputMonth != None):
        currentMonth = inputMonth
    if (inputDay != None):
        currentDay = inputDay
    if (inputHour != None):
        currentHour = inputHour
    if (inputMinute != None):
        currentMinute = inputMinute
    if (inputSecond != None):
        currentSecond = inputSecond

    # exception checking for february not having a 29th, 30th, or 31st day
    if (inputMonth == 2):
        if (check_valid_date(inputMonth, inputDay)):
            currentDay = 28
            newTime = datetime.datetime(currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSecond)
            returnTime = "<t:" + str(math.floor(newTime.timestamp())) + ":f>"
            relativeTime = "<t:" + str(math.floor(newTime.timestamp())) + ":R>"
            monthString = "February"

            dateString = ""
            if (inputDay == 29):
                dateString = "29th"
            elif (inputDay == 30):
                dateString = "30th"
            elif (inputDay == 31):
                dateString = "31st"

            # print(f"{month_to_string(inputMonth)} doesn't have a {dateString} day, so I pushed the day back to the earliest valid date.\n{returnTime} - which is {relativeTime}")
            return(f"{month_to_string(inputMonth)} doesn't have a {dateString} day, so I pushed the day back to the earliest valid date.\n{returnTime} - which is {relativeTime}")    

    # exception checking for certain months not having a 31st day
    if (inputMonth != 2):
        if (check_valid_date(inputMonth, inputDay)):
            inputDay = 30
            currentDay = inputDay
            newTime = datetime.datetime(currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSecond)
            returnTime = "<t:" + str(math.floor(newTime.timestamp())) + ":f>"
            relativeTime = "<t:" + str(math.floor(newTime.timestamp())) + ":R>"

            # print(f"{month_to_string(inputMonth)} doesn't have a 31st day, so I pushed the day back to the earliest valid date.\n{returnTime} - which is {relativeTime}")
            return(f"{month_to_string(inputMonth)} doesn't have a 31st day, so I pushed the day back to the earliest valid date.\n{returnTime} - which is {relativeTime}")
    
    # (currentYear + inputYear), (currentMonth + inputMonth), (currentDay + inputDay), (currentHour + inputHour), (currentMinute + inputMinute), (currentSecond + inputSecond)
    # currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSecond
    newTime = datetime.datetime(currentYear, currentMonth, currentDay, currentHour, currentMinute, currentSecond)
    returnTime = "<t:" + str(math.floor(newTime.timestamp())) + ":f>"
    relativeTime = "<t:" + str(math.floor(newTime.timestamp())) + ":R>"

    # print(str(returnTime) + " - which is " + str(relativeTime))
    return (str(returnTime) + " - which is " + str(relativeTime))

def check_valid_date(month, day):
    # if inputMonth is february(2) AND day is 29, 30, or 31, return True
    if ((month == 2 and day == 29)
        or (month == 2 and day == 30)
        or (month == 2 and day == 31)):
        return True
    
    # if inputMonth is april(4), june(6), september(9), november(11) AND day is 31, return True
    if ((month == 4 and day == 31)
        or (month == 6 and day == 31)
        or (month == 9 and day == 31)
        or (month == 11 and day == 31)):
        return True

    # else, the date is valid so return False
    return False

def month_to_string(month):
    if (month == 1):
        month = "January"
    elif (month == 2):
        month = "February"
    elif (month == 3):
        month = "March"
    elif (month == 4):
        month = "April"
    elif (month == 5):
         month = "May"
    elif (month == 6):
        month = "June"
    elif (month == 7):
        month = "July"
    elif (month == 8):
        month = "August"
    elif (month == 9):
        month = "September"
    elif (month == 10):
        month = "October"
    elif (month == 11):
        month = "November"
    elif (month == 12):
        month = "December"

    return month