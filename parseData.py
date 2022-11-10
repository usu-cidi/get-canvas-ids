import os
import json
import sys
import csv

from getIDs import getInfo

def writeToReport(object, label):
    f = open("contextReport9170565.txt", "a")
    f.write(f"{label}: {object}\n")
    f.close()

apiResult = getInfo()

sepData = apiResult.split("\n")

fields = ["A Number", "Canvas ID"]
rows = []

for person in range(len(sepData)):
    if not (sepData[person] == ""):
        writeToReport(sepData[person], "doing this: ")
        parsedData = json.loads(sepData[person])
        writeToReport(parsedData['login_id'], parsedData['sortable_name'])
        writeToReport(parsedData['id'], parsedData['sortable_name'])
        rowToAdd = [parsedData['login_id'], parsedData['id']]
        rows.append(rowToAdd)
        writeToReport(rowToAdd, "Row added")

outFile = "userInfo.csv"

with open(outFile, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

os.remove("canvasData9170565.txt")
os.remove("contextReport9170565.txt")

os.system(f'open {outFile}')