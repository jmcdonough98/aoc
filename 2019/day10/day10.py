
import math
from fractions import Fraction
with open("input.txt","r") as f:
    field = f.read().split("\n")
pts = []
for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == '#':
            pts.append((j,i))

def findBestPoint(points):
    slopes = {}
    for pt1 in points:
        x1,y1 = pt1
        slopes[pt1] = {}
        for pt2 in points:
            if pt2 == pt1:
                continue
            x2,y2 = pt2
            s = math.atan2((y2-y1),x2-x1)
            if s in slopes[pt1]:
                slopes[pt1][s].append((x2,y2))
            else:
                slopes[pt1][s] = [(x2,y2)]
    return slopes

slopes = findBestPoint(pts)
pt = max(slopes,key=lambda p: len(slopes[p]))
print("PART 1:",pt, len(slopes[pt]))

dist = lambda p: abs(pt[1] - p[1]) + abs(pt[0] - p[0])
sortedAngles = sorted(slopes[pt].items())
for angle in sortedAngles:
    angle[1].sort(key=dist)
count = 0
for i in range(len(sortedAngles)):
    if sortedAngles[i][0] < -math.pi/2:
        continue
    sortedAngles[i][1].pop(0)
    count += 1
for i in range(len(sortedAngles)):
    count += 1
    if count == 200:
        tmp = sortedAngles[i][1].pop(0)
        print("PART 2:", tmp[0]* 100 + tmp[1])
        break
    else:
        sortedAngles[i][1].pop(0)
