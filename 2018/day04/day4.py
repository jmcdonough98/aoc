import datetime
from collections import defaultdict

f = open('input.txt','r')
entries = f.read().splitlines()
entries.sort()

guards = defaultdict(int)
for e in entries:
    if e[19] == "G":
        guard = e.split("#")[1].split(" ")[0]
        i = 0
        continue
    if i % 2 == 0:
        sleepTime =  datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
    else:
        wakeTime = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        guards[guard] += int((wakeTime - sleepTime).total_seconds() / 60)
    i += 1

maxTime = 0.0
print len(guards)
for g in guards:
    if guards[g] > maxTime:
        maxTime = guards[g]
        maxGuard = g

minutes = defaultdict(int)

for e in entries:
    if e[19] == "G":
        if e.split("#")[1].split(" ")[0] == maxGuard:
            correctGuard = True
        else:
            correctGuard = False
        i = 0
        continue

    if correctGuard and i % 2 == 0:
        start = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        
    if correctGuard and i % 2 ==1:
        end = datetime.datetime.strptime(e[1:17], "%Y-%m-%d %H:%M")
        delta = int((end - start).total_seconds() / 60)
        startMinute = start.minute
        for j in range(delta):
            minutes[(startMinute+j)] += 1
    i += 1

maxCount = 0
for m in minutes:
    if minutes[m] > maxCount:
        maxMinute = m
        maxCount = minutes[m]

print int(maxGuard)*maxMinute