import re
from time import time

class Interval:
    def __init__(self,intervals):
        self.intervals = intervals
    def add(self,tmp):
        self.intervals.append(tmp)
        self.cleanup()
    def cleanup(self):
        changed = True
        while changed:
            changed = self.cleanupHelper()
    def cleanupHelper(self):
        for i in range(len(self.intervals)):
            for j in range(i+1,len(self.intervals)):
                a = self.intervals[i]
                b = self.intervals[j]
                tmp = self.checkPair(a,b)
                if tmp != None:
                    self.intervals.remove(a)
                    self.intervals.remove(b)
                    self.intervals.append(tmp)
                    return True 
        return False
    def checkPair(self,a,b):
        if a[0] <= b[0] <= a[1]:
            return [min(a[0],b[0]), max(a[1],b[1])]
        if b[0] <= a[0] <= b[1]:
            return [min(a[0],b[0]), max(a[1],b[1])]
        return None 
    def length(self):
        return sum(1 + x[1] - x[0] for x in self.intervals)
    def contains(self,pt):
        return any(x[0] <= pt <= x[1] for x in self.intervals)

def parseInput():
    norm = lambda x,y: abs(x[0]-y[0]) + abs(x[1]-y[1])
    s = open('input.txt','r').read().split('\n')
    pattern = re.compile(r"(-?\d+)")
    sensors = []
    radii = []
    beacons = set()
    for line in s:
        x1,y1,x2,y2 = list(map(int, pattern.findall(line)))
        x = (x1,y1)
        y = (x2,y2)
        d = norm(x,y)
        sensors.append(x)
        beacons.add(y)
        radii.append(d)
    return sensors, beacons, radii


t0 = time()
sensors, beacons, radii = parseInput()
N = 4000000
specCol = 2000000

for col in range(N):
    tmp = Interval([])
    for i in range(len(sensors)):
        x = sensors[i]
        rowDist = radii[i] - abs(x[1] - col)
        if rowDist >= 0:
            tmp.add([x[0] -(rowDist),x[0]+rowDist])
    if col == specCol:
        print("Part 1:", tmp.length() - sum(x[1] == col for x in beacons if tmp.contains(x[1])))

    # Grug intersection with [0,N]
    for i in range(len(tmp.intervals)):
        if tmp.intervals[i][0] < 0:
            tmp.intervals[i][0] = 0
        if tmp.intervals[i][1] > N:
            tmp.intervals[i][1] = N

    # We are assuming there is exactly one gap, i.e. a unique answer.
    if tmp.length() != N + 1: 
        print("Part 2:", col + N * (min(tmp.intervals, key = lambda x: x[1])[1] + 1))
        break
print("Time:", time() - t0)


