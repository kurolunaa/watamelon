import datetime
import json
import os

path = os.getcwd()
deleteArray = []

class Entry:
    # default values: today's date, 0 gil, 0 of every item
    # item list: extravagant necklaces, earrings, bracelet, rings, and nonextravagant necklaces, earrings, bracelets, and rings
    # is there a better way of inputing items instead of putting in numbers? yeah probably.
    # does it work? yeah, and there are only 8 items i care about, so no, i'm not going to change it.
    def __init__(self, date=datetime.datetime.now(), gil=0, items=[0, 0, 0, 0, 0, 0, 0, 0]):

        # data values (date, gil, items[])
        self.date = date.strftime("%Y-%m-%d")
        self.gil = gil
        self.items = items
        
def convertItemsToDict(entry):
    items = {
        "extravagant_salvaged_necklaces":    entry.items[0],
        "extravagant_salvaged_earrings":     entry.items[1],
        "extravagant_salvaged_bracelets":    entry.items[2],
        "extravagant_salvaged_rings":        entry.items[3],
        "salvaged_necklaces":                entry.items[4],
        "salvaged_earrings":                 entry.items[5],
        "salvaged_bracelets":                entry.items[6],
        "salvaged_rings":                    entry.items[7]
    }

    # for key, value in items.items():
    #     if value == 0:
    #         deleteArray.append(key)
            
    return(items)

def deleteEmptyItems(dict):
    for key in deleteArray:
        del dict[key]
    
    deleteArray.clear()
    return dict

def createFullEntry(entry):
    full = {
        "date": entry.date,
        "gil_obtained": entry.gil,
        # "items": deleteEmptyItems(convertItemsToDict(entry))
        "items": convertItemsToDict(entry)
    }
    return full

def checkIfFileExists(entry):
    fileName = str(entry["date"]) + ".json"
    for file in os.listdir("json"):
        if (fileName == file):
            print(fileName + " already exists and has been overwritten.")
            # ideally, would like to create a form of "confirmation" prompt, but since this will all be handled over a single slash command in discord, we ball

def makeJSON(entry):
    output = createFullEntry(entry)
    checkIfFileExists(output)

    json_str = json.dumps(output, indent=4)
    filename = output["date"] + ".json"
    full_path = os.path.join(path + "/json", filename)

    with open(full_path, "w+") as f:
        f.write(json_str)
