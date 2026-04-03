import os
import json
import matplotlib.pyplot as plt
import numpy as np

read_path = os.getcwd() + str("/json/")
jsonList = []

xpoints = np.array([])
ypoints = np.array([])

highest_gil = 0
highest_gil_day = ""
# some absurdly high default number
lowest_gil = 9999999
lowest_gil_day = ""
total_gil = 0
average_gil = 0

index = 0
iterator = 0
days = 0

def updateList():
    global jsonList
    for file in os.listdir("json"):
        jsonList.append(file)
        jsonList = sorted(jsonList)

def updateVariables():
    # is there a better way of doing this? probably. do i care? yeah a little bit
    # does it work? yeah, so i'm not going to change it. 
    global xpoints, ypoints, highest_gil, highest_gil_day, lowest_gil, lowest_gil_day, total_gil, average_gil,index, iterator
    for item in jsonList:
        with open(read_path + item, "r") as current_file:
            data = json.load(current_file)

        date = data["date"]        
        xpoints = np.append(xpoints, date)

        gil = data["gil_obtained"]
        ypoints = np.append(ypoints, gil)

        if gil > highest_gil:
            highest_gil = gil
            highest_gil_day = date
            index = iterator
        iterator += 1

        if gil < lowest_gil:
            lowest_gil = gil
            lowest_gil_day = date

        total_gil = total_gil + gil
    average_gil = total_gil / len(jsonList)
    iterator = 0

def resizeList(number):
    # update list size based on an input number of days given
    global jsonList, days

    # check if the input is larger than array. if it is, stop because it will break
    if (number > 30 or number < 2):
        print("Invalid input, createChart(input) must be between 2 and 30.")
        exit(1)

    if (number > len(jsonList)):
        print("There aren't enough data points to fully satisfy the chart. A chart will still be created with the available data points.")
        days = len(jsonList)

    jsonList = jsonList[-number:]

# matplotlib ----------------------------------------------------------------------------------------------------------------
# I KNOW IT'S UGLY BUT IT IS DESIGNED TO BE USED ONLY ONCE SO WHO CARES
def createChart(number=7):
    # update list, resize list based on input
    updateList()
    resizeList(number)
    updateVariables()
    
    # for my eyes
    plt.style.use('dark_background')
    
    # stops it from using scientific notation
    plt.rcParams["axes.formatter.limits"] = (-99, 99)
    plt.figure(figsize=(11, 6), dpi=180)

    # labels
    if (days > 1):
        plt.title("Amount earned in the past " + str(days) + " day(s)")
    else:
        plt.title("Amount earned in the past " + str(number) + " day(s)")
    plt.xlabel("Date (YYYY-MM-DD)")
    plt.ylabel("Gil obtained")

    # lines
    plt.axvspan(index, index, color="green", alpha=1)   # highest earning day
    plt.axhline(highest_gil, color="green", linestyle="--", alpha=1)
    plt.axhline(average_gil, color="darkorange", linestyle="--", alpha=0.5)
    plt.axhline(lowest_gil, color="darkred", linestyle="--", alpha=1)

    # plotting values
    plt.plot(xpoints, ypoints, color="cyan")
    plt.plot(xpoints, ypoints, "o")
    plt.grid(color = 'cyan', alpha=0.25)

    # x ticks
    plt.xticks(xpoints, rotation=-45, ha="left")

    # y ticks
    ax_left = plt.gca()
    ax_left.set_ylim(0, highest_gil * 1.1)
    ax_left.set_yticks(np.arange(0, highest_gil * 1.1, 100000))

    ax_right = ax_left.twinx()
    ax_right.set_ylim(ax_left.get_ylim())
    ax_right.set_yticks([highest_gil, average_gil, lowest_gil])

    # finalize and save as png
    plt.tight_layout()
    plt.savefig("chart.png")


