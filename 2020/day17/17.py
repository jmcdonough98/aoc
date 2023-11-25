_input = """###..#..
.#######
#####...
#..##.#.
###..##.
##...#..
..#...#.
.#....##"""

_tinput = """.#.
..#
###"""
from itertools import product

def getInitialPoints(_input):
    t = _input.split('\n')
    pts = []
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j] == '#':
                pts.append((i,j,0,0))
    return pts
offsets = [-1,0,1]
def getAdjacentPointCount(pt,otherPts):
    c = 0
    for dx in offsets:
        for dy in offsets:
            for dz in offsets:
                for dw in offsets:
                    if  (dx,dy,dz,dw) != (0,0,0,0):
                        c += (pt[0] + dx, pt[1] + dy, pt[2] + dz, pt[3] + dw) in otherPts
    return c
pts = set(getInitialPoints(_input))

def nextGen(pts,_max):
    new = set()
    for i in range(-_max,_max+1):
        for j in range(-_max,_max+1):
            for k in range(-_max,_max+1):
                for l in range(-_max,_max+1):
                    if (i,j,k,l) in pts:
                        if getAdjacentPointCount((i,j,k,l),pts) in [2,3]:
                            new.add((i,j,k,l))
                    else:
                        if getAdjacentPointCount((i,j,k,l),pts) == 3:
                            new.add((i,j,k,l))
    return new        

for i in range(6):
    print(i)
    pts = nextGen(pts,2*(i+4))
print(len(pts), max([max(x,key = lambda y: abs(y)) for x in pts]))# print(nextGen(pts,4))
