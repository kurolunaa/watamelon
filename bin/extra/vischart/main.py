import datetime
import jsonMaker
import os
import json
from vischart import createChart

today = jsonMaker.Entry(gil=470500, items=[4, 5, 5, 0, 0, 0, 0, 5])

# ignore all of this! this is to quickly create a bunch of data that i can't really automate because it would take more time to create something to automate it than it would to do this
                                                          # n, e, b, r, n, e, b, r
# a = jsonMaker.Entry(datetime.datetime(2026, 2, 27), 392500, [5, 0, 0, 0, 5, 9, 0, 0])
# b = jsonMaker.Entry(datetime.datetime(2026, 2, 28), 399000, [0, 5, 0, 0, 13, 0, 0, 10])
# c = jsonMaker.Entry(datetime.datetime(2026, 3, 1), 472500, [0, 0, 13, 0, 4, 5, 0, 0])

# entryList = [a, b, c]
# def createEntries(list):
#     for entry in list:
#         jsonMaker.makeJSON(entry)

# createEntries(entryList)

jsonMaker.makeJSON(today)
createChart(30)

# DEBUG FOR EVERY FILE IN LIST
# jsonList = []
# average = 0
# read_path = os.getcwd() + str("/json/")

# for file in os.listdir("json"):
#     jsonList.append(file)
#     jsonList = sorted(jsonList)

# for item in jsonList:
#     with open(read_path + item, "r") as current_file:
#             data = json.load(current_file)

