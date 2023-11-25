from collections import defaultdict
s = open('input.txt','r').read().split('\n')

def pointFromCoordString(s):
    i = 0
    x,y,z = 0,0,0
    while i < len(s):
        if s[i] in ['s','n']:
            token = s[i:i+2]
            i += 1
        else:
            token = s[i]
        if token == 'e':
            x += 1
            y -= 1
        elif token == 'ne':
            x += 1
            z -= 1
        elif token == 'nw':
            y += 1
            z -= 1
        elif token == 'w':
            x -= 1
            y += 1
        elif token == 'sw':
            x -= 1
            z += 1
        elif token == 'se':
            z += 1
            y -= 1
        else:
            print('you fucked up')
        i += 1
    return (x,y,z)      
def generateGrid(s):
    points = set()
    for line in s:
        pt = pointFromCoordString(line)
        if pt in points:
            points.remove(pt)
        else:
            points.add(pt)
    return points

def simulateDay(pts):
    neighbors = defaultdict(int)
    new = set()
    for p in pts:
        adj = getNeighbors(*p)
        for x in adj:
            neighbors[x] += 1
    for p in neighbors:
        if p in pts: 
            if (1 <= neighbors[p] <= 2):
                new.add(p)
        elif neighbors[p] == 2:
            new.add(p)
    return new
    
getNeighbors = lambda x,y,z: set([(x+1,y,z-1),(x,y+1,z-1),(x-1,y+1,z),(x-1,y,z+1),(x,y-1,z+1),(x+1,y-1,z)])

def day24(n):
    points = generateGrid(s)
    print("Part 1: {}".format(len(points)))
    for i in range(n):
        points = simulateDay(points)
    print("Part 2: {}".format(len(points)))
day24(100)