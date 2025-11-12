from datetime import timedelta
import datetime
import math

def convertTime(inputWeek, inputDay, inputHour, inputMinute, inputSecond):

    if inputWeek == None:
        inputWeek = 0
    if inputDay == None:
        inputDay = 0
    if inputHour == None:
        inputHour = 0
    if inputMinute == None:
        inputMinute = 0
    if inputSecond == None:
        inputSecond = 0

    now = datetime.datetime.now() + timedelta(weeks=inputWeek, days=inputDay, hours=inputHour, minutes=inputMinute, seconds=inputSecond)
    timestamp = math.floor(now.timestamp())
    result = (f"<t:{timestamp}:f> - which is <t:{timestamp}:R>")
    return result
