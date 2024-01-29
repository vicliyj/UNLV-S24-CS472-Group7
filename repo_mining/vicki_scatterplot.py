import csv
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

with open('data/file2_rootbeer.csv') as csvfile:
    csvfile = csv.reader(csvfile)
    rows = list(csvfile)

earliestDate = datetime.fromisoformat(rows[1][2])
rows = rows[1:]
for row in rows:
    currDate = datetime.fromisoformat(row[2])
   
    if currDate < earliestDate:
        earliestDate = currDate

def howManyWeeks(currDate):
    curr = datetime.fromisoformat(currDate)
    monday1 = (curr - timedelta(days=curr.weekday()))
    monday2 = (earliestDate - timedelta(days=earliestDate.weekday()))

    return (monday1 - monday2).days / 7

authors = dict()
filename = dict()
fileCount = 1;

for row in rows:
    if row[0] not in filename:
        filename[row[0]] = fileCount
        fileCount += 1

for row in rows:
    author = row[1]

    if author not in authors:
        authors[author] = [[],[]]
    authors[author][0].append(filename[row[0]])
    authors[author][1].append(howManyWeeks(row[2]))

for author, yea in authors.items():
    plt.scatter(yea[0], yea[1])
plt.xlabel("file")
plt.ylabel("weeks")
plt.show()
