from collections import defaultdict

gr = open('input.txt','r').read().split('\n')
valid = lambda x: (-1 < x[0] < len(gr)) and (-1 < x[1] < len(gr[0]))
nbhd = lambda x: [(x[0],x[1] + 1), (x[0]+1,x[1]), (x[0],x[1]-1),(x[0]-1,x[1])] 

def getConnectedPipes(x, t): # pipes could go off the side, but those by definition will not be in the loop
    B = nbhd(x)
    if t == "|":
        return [B[1], B[3]]
    elif t == "-":
        return [B[0],B[2]]
    elif t == "L":
        return [B[0], B[3]]
    elif t == "J":
        return [B[2],B[3]]
    elif t == "7":
        return [B[1],B[2]]
    elif t == "F":
        return [B[0],B[1]]
    elif t == "S":
        return 1
    return None

def findStart(gr):
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] == "S":
                return (i,j)
def findPath(gr, start):
    path = [start]
    for pt in nbhd(start):
        tmp = getConnectedPipes(pt, gr[pt[0]][pt[1]])
        if tmp != None and start in tmp:
            path.append(pt)
            break
    while True:
        currPt = path[-1]
        nbhs = getConnectedPipes(currPt, gr[currPt[0]][currPt[1]])
        if nbhs[0] in path and nbhs[1] in path: # loop closed
            break
        elif nbhs[0] in path:
            path.append(nbhs[1])
        elif nbhs[1] in path:
            path.append(nbhs[0])
    return path

def scaleGrid():
    newGrid = []
    for i in range(len(gr)):
        newGrid += ["","",""]
        for j in range(len(gr[i])):
            if gr[i][j] == ".":
                newGrid[3*i] +=    "..."
                newGrid[3*i+1] +=  "..."
                newGrid[3*i+2] +=  "..."
            if gr[i][j] == "|":
                newGrid[3*i] +=    ".|."
                newGrid[3*i+1] +=  ".|."
                newGrid[3*i+2] +=  ".|."
            if gr[i][j] == "-":
                newGrid[3*i] +=    "..."
                newGrid[3*i+1] +=  "---"
                newGrid[3*i+2] +=  "..."
            if gr[i][j] == "L":
                newGrid[3*i] +=    ".|."
                newGrid[3*i+1] +=  ".L-"
                newGrid[3*i+2] +=  "..."
            if gr[i][j] == "F":
                newGrid[3*i] +=    "..."
                newGrid[3*i+1] +=  ".F-"
                newGrid[3*i+2] +=  ".|."
            if gr[i][j] == "7":
                newGrid[3*i] +=    "..."
                newGrid[3*i+1] +=  "-7."
                newGrid[3*i+2] +=  ".|."
            if gr[i][j] == "J":
                newGrid[3*i] +=    ".|."
                newGrid[3*i+1] +=  "-J."
                newGrid[3*i+2] +=  "..."
    return newGrid

def part2(scaledGrid, origGrid, path, oldPath):
    path = set(path)
    seen = defaultdict(bool)
    for p in path:
        seen[p] = True
    regions = []
    interior = []
    # find connected components of points not on loop
    for i in range(len(scaledGrid)):
        for j in range(len(scaledGrid[i])):
            if seen[(i,j)]:
                continue 
            newRegion = set([(i,j)])
            isInterior = True
            bndry = set(nbhd((i,j)))
            while len(bndry) > 0:
                curr = bndry.pop()
                newRegion.add(curr)
                seen[curr] = True
                if curr[0] in [0, len(scaledGrid)] or curr[1] in [0, len(scaledGrid[0])]:
                    isInterior = False
                for pt in nbhd(curr):
                    if valid(pt) and not seen[pt] and pt not in path:
                        bndry.add(pt)
            regions.append(newRegion)
            interior.append(isInterior)
    # for each non loop point in the original grid
    # it is in the interior of the loop if and only if the 
    # corresponding scaled point is in the interior of the scaled loop
    count = 0
    for i in range(len(origGrid)):
        for j in range(len(origGrid[0])):
            if (i,j) not in oldPath:
                tmp = (3*i, 3*j)
                for k in range(len(regions)):
                    if tmp in regions[k]:
                        count += int(interior[k])
    return count
start = findStart(gr)
path = findPath(gr, start)
print("Part 1:", len(path) // 2)

for t in "|-LJ7F":
    if set(getConnectedPipes(path[0], t)) == set([path[1], path[-1]]):
        gr[path[0][0]] = gr[path[0][0]][:path[0][1]] + t + gr[path[0][0]][path[0][1] + 1:]

oldgr = gr
gr = scaleGrid()
newStart = (3*start[0] + 1, 3*start[1] + 1) # center of 3x3 grid corresponding to old start point
newPath = findPath(gr, newStart)

print("Part 2:", part2(gr, oldgr, newPath, path))
