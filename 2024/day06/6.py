def parseInput(_input):
    wallPos = set()
    for i in range(len(_input)):
        for j in range(len(_input[i])):
            if _input[i][j] == "#":
                wallPos.add((i,j))
            elif _input[i][j] == "^":
                guardPos = (i,j)
    height, width = len(_input), len(_input[0])
    return height, width, wallPos, guardPos

def walkGuard(height, width, wallPos, guardPos):
    dirs = [(-1,0),(0,1),(1,0),(0,-1)]
    currDir = 0 
    visited = set()
    while 0 <= guardPos[0] < height and 0 <= guardPos[1] < width:
        if (guardPos, currDir) in visited:
            return True, None
        visited.add((guardPos,currDir))
        tmp = (guardPos[0] + dirs[currDir][0], guardPos[1] + dirs[currDir][1])
        if tmp in wallPos:
            currDir = (currDir + 1) % 4
        else:
            guardPos = tmp
    return False, len(set(x[0] for x in visited))

def day6(_input):
    height, width, wallPos, guardPos = parseInput(_input)
    p1 = walkGuard(height, width, wallPos, guardPos)[1]
    p2 = 0
    for i in range(height):
        for j in range(width):
            if (i,j) not in wallPos and \
                walkGuard(height, width, wallPos.union([(i,j)]), guardPos)[0]:
                p2 += 1
    return p1, p2
    
if __name__ == "__main__":
    _input = open('input.txt').read().split('\n')
    p1, p2 = day6(_input)
    print("Part 1:", p1)
    print("Part 2:", p2)
