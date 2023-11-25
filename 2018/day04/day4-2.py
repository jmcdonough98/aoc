import datetime
from collections import defaultdict

f = open('input.txt','r')
entries = f.read().splitlines()
entries.sort()

guardIDs = []
minutes = []
for e in entries:
    if e[19] == "G":
        guardID = e.split("#")[1].split(" ")[0]
        if guardID not in guardIDs:
            guardIDs.append(guardID)
            minutes.append(defaultdict(int))
        j = guardIDs.index(guardID)
        i = 0
        continue
    if i % 2 == 0:
        sleepTime =  datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
    else:
        wakeTime = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        delta = int((wakeTime- sleepTime).total_seconds() / 60)
        startMinute = sleepTime.minute
        for k in range(delta):
            minutes[j][(startMinute+k)] += 1
    i += 1

max = 0
for i in range(len(minutes)):
    for m in minutes[i]:
        if minutes[i][m] > max:
            max = minutes[i][m]
            minute = m
            ID = guardIDs[i]
print minute*int(ID)